"""Validate and compare normalized exports, never raw Wix API payloads.

Adapters require verified source schemas. No write or migration operations.
"""
import argparse
import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

PRODUCT_FIELDS = {
    "id", "master_id", "parent_master_id", "name", "slug", "sku", "barcode",
    "currency", "price", "sale_price", "options", "variants", "inventory",
    "category_ids", "media", "localized", "fresha_ids", "visible",
    "description", "modifiers", "tax", "shipping", "seo", "subscriptions", "digital",
}
VARIANT_FIELDS = {"id", "master_id", "sku", "barcode", "choices", "price", "inventory", "media", "visible", "price_data"}
CATEGORY_FIELDS = {"id", "name", "slug", "visible", "localized"}
METADATA_FIELDS = {"site_id", "catalog_version", "source", "extracted_at", "complete", "total_products", "total_categories", "total_variants"}


def unique(records, key, label):
    found = {}
    for record in records:
        if not isinstance(record, dict):
            raise ValueError(label + " records must be objects")
        value = record.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{label}.{key} requires a nonempty string")
        if value in found:
            raise ValueError(f"Duplicate {label}.{key}: {value}")
        found[value] = record
    return found


def amount(value, label, nullable=False):
    if value is None and nullable:
        return
    if not isinstance(value, str):
        raise ValueError(label + " must be a decimal string")
    try:
        number = Decimal(value)
        if not number.is_finite() or number < 0:
            raise ValueError(label + " must be finite and nonnegative")
    except InvalidOperation as exc:
        raise ValueError(label + " invalid decimal") from exc


def validate(snapshot):
    if not isinstance(snapshot, dict):
        raise ValueError("Snapshot must be an object")
    if type(snapshot.get("schema_version")) is not int or snapshot["schema_version"] != 1:
        raise ValueError("Expected normalized schema_version 1, not raw API data")
    metadata = snapshot.get("metadata", {})
    if not isinstance(metadata, dict) or not METADATA_FIELDS <= metadata.keys() or metadata["complete"] is not True:
        raise ValueError("Complete extraction metadata is required")
    for name in ("site_id", "catalog_version", "source", "extracted_at"):
        if not isinstance(metadata[name], str) or not metadata[name].strip():
            raise ValueError("Missing extraction metadata: " + name)
    if metadata["catalog_version"] not in ("V1_CATALOG", "V3_CATALOG"):
        raise ValueError("catalog_version must be V1_CATALOG or V3_CATALOG")
    if any(type(metadata[name]) is not int or metadata[name] < 0 for name in ("total_products", "total_categories", "total_variants")):
        raise ValueError("Extraction totals must be nonnegative integers")
    products = snapshot.get("products")
    categories = snapshot.get("categories")
    if not isinstance(products, list) or not isinstance(categories, list):
        raise ValueError("products and categories must be lists")
    if metadata["total_products"] != len(products) or metadata["total_categories"] != len(categories):
        raise ValueError("Extraction totals disagree with record counts")
    by_id = unique(products, "id", "product")
    masters = unique(products, "master_id", "product")
    by_category = unique(categories, "id", "category")
    all_variants = []
    for category in categories:
        if not CATEGORY_FIELDS <= category.keys():
            raise ValueError("Incomplete category: " + category["id"])
        typed_fields(category, {"name": str, "slug": str, "visible": bool, "localized": dict})
    for product in products:
        label = product["id"]
        if not PRODUCT_FIELDS <= product.keys():
            raise ValueError("Incomplete product " + label + ": " + str(sorted(PRODUCT_FIELDS - product.keys())))
        typed_fields(product, {"name": str, "slug": str, "currency": str, "visible": bool,
            "options": list, "variants": list, "inventory": dict, "media": list,
            "localized": dict, "category_ids": list, "fresha_ids": list,
            "description": str, "modifiers": list, "tax": dict, "shipping": dict,
            "seo": dict, "subscriptions": list, "digital": dict})
        if len(product["currency"]) != 3 or not product["currency"].isalpha() or not product["currency"].isupper():
            raise ValueError("currency requires a three-letter uppercase code")
        string_list(product["category_ids"], "category_ids")
        string_list(product["fresha_ids"], "fresha_ids")
        option_choices = {}
        for option in product["options"]:
            if not isinstance(option, dict):
                raise ValueError("options require objects with name and choices")
            typed_fields(option, {"name": str, "choices": list})
            if not option["name"] or option["name"] in option_choices:
                raise ValueError("Option names must be nonempty and unique")
            string_list(option["choices"], "option choices")
            if not option["choices"]:
                raise ValueError("Option choices must be nonempty")
            option_choices[option["name"]] = option["choices"]
        parent = product["parent_master_id"]
        if parent is not None and (parent not in masters or parent == product["master_id"]):
            raise ValueError("Invalid parent association: " + label)
        if not isinstance(product["category_ids"], list) or any(x not in by_category for x in product["category_ids"]):
            raise ValueError("Unknown category membership: " + label)
        if len(product["category_ids"]) != len(set(product["category_ids"])):
            raise ValueError("Duplicate category membership: " + label)
        for field in ("sku", "barcode"):
            if not isinstance(product[field], str):
                raise ValueError(field + " must remain a string: " + label)
        amount(product["price"], label + ".price")
        amount(product["sale_price"], label + ".sale_price", nullable=True)
        if not isinstance(product["variants"], list):
            raise ValueError("variants must be a list: " + label)
        unique(product["variants"], "master_id", "variant within " + label)
        if metadata["catalog_version"] == "V3_CATALOG" and not product["variants"]:
            raise ValueError("V3 products require at least one variant")
        for variant in product["variants"]:
            if not VARIANT_FIELDS <= variant.keys():
                raise ValueError("Incomplete variant in " + label)
            typed_fields(variant, {"choices": dict, "inventory": dict, "media": list, "visible": bool, "price_data": dict})
            if variant["choices"].keys() != option_choices.keys() or any(
                    value not in option_choices[name] for name, value in variant["choices"].items()):
                raise ValueError("Variant choices do not match product options")
            for field in ("sku", "barcode"):
                if not isinstance(variant[field], str):
                    raise ValueError("Variant " + field + " must be a string")
            amount(variant["price"], label + ".variant.price")
            all_variants.append(variant)
    unique(all_variants, "id", "variant")
    if len(all_variants) != metadata["total_variants"]:
        raise ValueError("Extraction totals disagree with variant count")
    variant_masters = unique(all_variants, "master_id", "variant")
    if variant_masters.keys() & masters.keys():
        raise ValueError("Product and variant master identity namespaces overlap")
    for product in products:
        visited, node = set(), product
        while node["parent_master_id"] is not None:
            if node["master_id"] in visited:
                raise ValueError("Parent cycle: " + product["id"])
            visited.add(node["master_id"])
            node = masters[node["parent_master_id"]]
    return by_id, by_category


def typed_fields(record, fields):
    for field, expected in fields.items():
        if type(record.get(field)) is not expected:
            raise ValueError(field + " requires " + expected.__name__)


def string_list(values, label):
    if any(not isinstance(x, str) or not x for x in values) or len(values) != len(set(values)):
        raise ValueError(label + " requires unique nonempty strings")


def exact(value):
    # Preserve JSON types: Python considers True == 1 and 1 == 1.0.
    return json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False)


def normalize(product):
    result = dict(product)
    # Memberships and external ID sets have no order; media and options retain order.
    result["category_ids"] = sorted(product["category_ids"])
    result["fresha_ids"] = sorted(product["fresha_ids"])
    result["variants"] = sorted(product["variants"], key=lambda x: x["id"])
    return result


def compare(before, after):
    old, old_categories = validate(before)
    new, new_categories = validate(after)
    if before["metadata"]["site_id"] != after["metadata"]["site_id"]:
        raise ValueError("Different site IDs; review any rehearsal mapping explicitly")
    changes = []
    for kind, left, right in (("product", old, new), ("category", old_categories, new_categories)):
        for key in sorted(left.keys() - right.keys()):
            changes.append({"kind": kind, "id": key, "change": "removed"})
        for key in sorted(right.keys() - left.keys()):
            changes.append({"kind": kind, "id": key, "change": "added"})
        for key in sorted(left.keys() & right.keys()):
            a = normalize(left[key]) if kind == "product" else left[key]
            b = normalize(right[key]) if kind == "product" else right[key]
            for field in sorted(a.keys() | b.keys()):
                if field not in a or field not in b or exact(a[field]) != exact(b[field]):
                    # Avoid printing potentially sensitive catalogue values to logs.
                    changes.append({"kind": kind, "id": key, "field": field, "change": "changed"})
    return {"equal": not changes, "changes": changes,
            "before_products": len(old), "after_products": len(new),
            "before_categories": len(old_categories), "after_categories": len(new_categories),
            "note": "Differences require review; this tool neither migrates nor approves them"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    args = parser.parse_args()
    try:
        result = compare(json.loads(args.before.read_text()), json.loads(args.after.read_text()))
        print(json.dumps(result, indent=2))
        return 0 if result["equal"] else 1
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(json.dumps({"error": str(exc), "equal": False}))
        return 2


if __name__ == "__main__":
    sys.exit(main())
