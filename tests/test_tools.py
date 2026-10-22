import copy
import unittest
from tools.audit import Page, audit_page, check_links, inventory, origin, redirect_map_errors, sitemap_entries
from tools.catalogue import compare, validate


def snapshot():
    return {"schema_version": 1, "metadata": {"site_id": "fixture-site", "catalog_version": "V1_CATALOG",
        "source": "synthetic", "extracted_at": "2026-10-22T00:00:00Z", "complete": True,
        "total_products": 1, "total_categories": 1, "total_variants": 1},
        "categories": [{"id": "c1", "name": "Brand", "slug": "brand", "visible": True, "localized": {}}],
        "products": [{"id": "p1", "master_id": "master-1", "parent_master_id": None,
            "name": "Fixture", "slug": "fixture", "sku": "001", "barcode": "000123",
            "currency": "CAD", "price": "12.50", "sale_price": None,
            "options": [{"name": "Size", "choices": ["250ml"]}],
            "variants": [{"id": "v1", "master_id": "master-v1", "sku": "001-a", "barcode": "000124",
                "choices": {"Size": "250ml"}, "price": "12.50", "inventory": {"quantity": 3}, "media": [],
                "visible": True, "price_data": {"actual": "12.50", "compare_at": None}}],
            "inventory": {"tracked": True, "quantity": 3}, "category_ids": ["c1"],
            "media": ["https://example.com/image1"], "localized": {"fr": {"name": "Exemple"}},
            "fresha_ids": ["f1"], "visible": True, "description": "Synthetic",
            "modifiers": [], "tax": {}, "shipping": {}, "seo": {}, "subscriptions": [], "digital": {}}]}


class CatalogueTests(unittest.TestCase):
    def test_identical_snapshots_pass(self):
        self.assertTrue(compare(snapshot(), snapshot())["equal"])

    def test_preservation_fields_are_detected(self):
        for field, value in [("master_id", "changed"), ("sku", "1"), ("price", "13.00"),
                             ("category_ids", []), ("fresha_ids", []), ("media", []),
                             ("localized", {}), ("inventory", {"quantity": 0})]:
            with self.subTest(field=field):
                after = snapshot()
                after["products"][0][field] = value
                report = compare(snapshot(), after)
                self.assertFalse(report["equal"])
                self.assertEqual(report["changes"][0]["field"], field)

    def test_variant_change_detected(self):
        after = snapshot()
        after["products"][0]["variants"][0]["id"] = "v2"
        self.assertEqual(compare(snapshot(), after)["changes"][0]["field"], "variants")

    def test_duplicate_ids_fail(self):
        data = snapshot()
        data["products"].append(copy.deepcopy(data["products"][0]))
        data["metadata"]["total_products"] = 2
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            validate(data)

    def test_orphan_parent_fails(self):
        data = snapshot()
        data["products"][0]["parent_master_id"] = "missing"
        with self.assertRaisesRegex(ValueError, "parent"):
            validate(data)

    def test_missing_incomplete_or_count_mismatch_fails(self):
        for field, value in [("complete", False), ("total_products", 100)]:
            data = snapshot()
            data["metadata"][field] = value
            with self.assertRaises(ValueError):
                validate(data)
        data = snapshot()
        del data["products"][0]["media"]
        with self.assertRaisesRegex(ValueError, "Incomplete"):
            validate(data)

    def test_missing_categories_and_numeric_sku_fail(self):
        for field, value in [("category_ids", ["missing"]), ("sku", 1), ("price", "NaN")]:
            data = snapshot()
            data["products"][0][field] = value
            with self.assertRaises(ValueError):
                validate(data)

    def test_id_change_is_not_silently_matched(self):
        after = snapshot()
        after["products"][0]["id"] = "new"
        self.assertEqual({x["change"] for x in compare(snapshot(), after)["changes"]}, {"added", "removed"})

    def test_malformed_containers_rejected(self):
        for data in ([], {"schema_version": 1, "metadata": None}):
            with self.assertRaises(ValueError):
                validate(data)
        data = snapshot()
        data["products"] = [None]
        with self.assertRaises(ValueError):
            validate(data)

    def test_strict_boolean_and_container_types(self):
        for field, value in [("visible", 1), ("options", None), ("localized", []),
                             ("media", {}), ("currency", None), ("fresha_ids", [None])]:
            data = snapshot()
            data["products"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate(data)
        data = snapshot()
        data["metadata"]["total_products"] = True
        with self.assertRaises(ValueError):
            validate(data)

    def test_nested_type_drift_and_removed_null_field_detected(self):
        before, after = snapshot(), snapshot()
        before["products"][0]["inventory"] = {"tracked": True}
        after["products"][0]["inventory"] = {"tracked": 1}
        self.assertFalse(compare(before, after)["equal"])
        before, after = snapshot(), snapshot()
        before["products"][0]["extra"] = None
        self.assertFalse(compare(before, after)["equal"])

    def test_variant_choices_and_global_master_collisions_rejected(self):
        data = snapshot()
        data["products"][0]["variants"][0]["choices"] = {"Size": "missing"}
        with self.assertRaisesRegex(ValueError, "choices"):
            validate(data)
        data = snapshot()
        other = copy.deepcopy(data["products"][0])
        other.update(id="p2", master_id="master-2")
        other["variants"][0]["id"] = "v2"
        data["products"].append(other)
        data["metadata"]["total_products"] = 2
        data["metadata"]["total_variants"] = 2
        with self.assertRaisesRegex(ValueError, "Duplicate variant.master_id"):
            validate(data)

    def test_v3_missing_variants_cannot_pass(self):
        data = snapshot()
        data["metadata"].update(catalog_version="V3_CATALOG", total_variants=0)
        data["products"][0]["variants"] = []
        with self.assertRaisesRegex(ValueError, "V3 products"):
            validate(data)


class FakeReader:
    base = "https://example.com"

    def __init__(self, pages):
        self.pages = pages

    def get(self, url):
        body = self.pages[url]
        if isinstance(body, Exception):
            raise body
        return 200, url, body, {}


class AuditTests(unittest.TestCase):
    def test_nested_namespaced_sitemaps(self):
        result = inventory(FakeReader({
            "https://example.com/sitemap.xml": '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc>https://example.com/products.xml</loc></sitemap></sitemapindex>',
            "https://example.com/products.xml": '<urlset><url><loc>https://example.com/product/p1</loc></url></urlset>'}))
        self.assertTrue(result["complete"])
        self.assertEqual(result["urls"], ["https://example.com/product/p1"])

    def test_access_failure_is_not_empty_success(self):
        result = inventory(FakeReader({"https://example.com/sitemap.xml": OSError("403")}))
        self.assertFalse(result["complete"])
        self.assertTrue(result["errors"])

    def test_truncation_is_not_complete(self):
        result = inventory(FakeReader({"https://example.com/sitemap.xml": '<urlset><url><loc>https://example.com/a</loc></url><url><loc>https://example.com/b</loc></url></urlset>'}), limit=1)
        self.assertTrue(result["truncated"])
        self.assertFalse(result["complete"])

    def test_cross_origin_refused(self):
        result = inventory(FakeReader({"https://example.com/sitemap.xml": '<sitemapindex><sitemap><loc>https://other.com/x</loc></sitemap></sitemapindex>'}))
        self.assertFalse(result["complete"])

    def test_unsafe_origins_rejected(self):
        for url in ["http://example.com", "https://user:secret@example.com", "https://example.com:123"]:
            with self.assertRaises(ValueError):
                origin(url)

    def test_seo_metadata_and_internal_links(self):
        html = '<title>Brand</title><meta name="description" content="Description"><link rel="canonical" href="https://example.com/brand"><a href="/product/p1#top">P</a>'
        result = audit_page(FakeReader({"https://example.com/brand": html}), "https://example.com/brand")
        self.assertEqual(result["issues"], [])
        self.assertEqual(result["internal_links"], ["https://example.com/product/p1"])

    def test_missing_metadata_fails(self):
        result = audit_page(FakeReader({"https://example.com/": "<body>empty</body>"}), "https://example.com/")
        self.assertIn("expected-one-canonical", result["issues"])

    def test_http_header_noindex_fails(self):
        class HeaderReader:
            base = "https://example.com"
            def get(self, url):
                return 200, url, '<title>T</title><meta name="description" content="D"><link rel="canonical" href="https://example.com/">', {"X-Robots-Tag": "noindex"}
        self.assertIn("noindex-review-required", audit_page(HeaderReader(), "https://example.com/")["issues"])

    def test_broken_links_and_partial_link_coverage_fail(self):
        reader = FakeReader({"https://example.com/": '<a href="/a">A</a><a href="/b">B</a>',
            "https://example.com/a": "ok", "https://example.com/b": OSError("404")})
        report = check_links(reader, "https://example.com/")
        self.assertFalse(report["passed"])
        self.assertTrue(report["complete_for_source_html"])
        partial = check_links(reader, "https://example.com/", max_links=1)
        self.assertFalse(partial["complete_for_source_html"])
        self.assertFalse(partial["passed"])

    def test_redirect_chain_cycle_duplicate_and_status(self):
        rows = [{"old_url": "https://example.com/a", "new_url": "https://example.com/b", "status": "301"},
                {"old_url": "https://example.com/b", "new_url": "https://example.com/a", "status": "302"},
                {"old_url": "https://example.com/a", "new_url": "https://example.com/b", "status": "301"}]
        errors = redirect_map_errors(rows)
        self.assertTrue(any("chain or cycle" in x for x in errors))
        self.assertTrue(any("duplicate" in x for x in errors))
        self.assertTrue(any("301" in x for x in errors))

    def test_valid_redirect_proposal(self):
        self.assertEqual(redirect_map_errors([{"old_url": "https://example.com/a", "new_url": "https://example.com/b", "status": "301"}]), [])


if __name__ == "__main__":
    unittest.main()
