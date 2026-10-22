# Catalogue assessment and normalized comparison contract

Catalog V3 feasibility for this site: **undetermined**. No migration endpoint is called.
Studio and catalogue migration are separate decisions. No Catalogue Lab implementation
has been located or modified. Snapshot fields are logical, not raw Wix API names.
Verified API correspondences and current source links are in [official findings](official-findings.md).
Wix's existing-site migration request article currently says migration to the new catalogue
is unavailable, while also mentioning a dashboard migration banner. That inconsistency
requires dashboard/Wix support confirmation; there is no verified executable upgrade path
for this site. Modernizing category presentation need not wait for or force a V3 upgrade.

## Field-level preservation map

| Logical field | Baseline → target validation | Contingency/gate |
|---|---|---|
| Wix product, variant, category IDs | Exact identities and counts; explicit reconciliation for changed IDs | Never silently join by name or SKU |
| Master Product ID | Exact strings, uniqueness at documented entity level | Current comparator assumes globally unique variant masters and distinct product/variant master namespaces; confirm actual model first and adapt the tool rather than changing authoritative IDs |
| Parent-product associations | Exact parents, no missing/self/cyclic parents | Preserve original associations, no merges/splits without explicit plan |
| Options/variants | Names, ordered choices, combinations, variant count, IDs and fields | Verify actual API representation and unsupported combinations |
| SKU/barcode | Exact strings including leading zeros | Report blanks and duplicates separately; do not assume uniqueness |
| Prices | Currency, exact decimal strings, sale settings and variant prices | Reconcile sale schedule and tax behavior separately |
| Inventory | Tracking, location scope, quantities, availability, backorder/preorder | Reconcile legitimate sales between extraction times |
| Categories | IDs, titles/slugs/visibility/localization and membership sets | Check ordering and any collection/category terminology in actual APIs |
| Media | Ordered media, primary image, variant associations and alt text | Preserve source references and verify resolution separately |
| Localized content | Names, descriptions, slugs, visibility and language coverage | Do not erase missing locale data during normalization |
| Fresha mappings | External IDs, ID types, coverage and ambiguity | Preserve existing mapping contract; no inferred SKU join |
| SEO/commerce dependencies | Product/category routes, discounts, related products, subscriptions where used | Verify actual installed features; do not infer from export absence |

## Snapshot contract (schema_version 1)

`tools/catalogue.py` accepts normalized JSON, not raw Wix responses. Keep raw exports
and extraction manifests securely alongside normalized outputs. Implement no adapter
until both actual source schema and current official target schema are reviewed.

Root: `schema_version: 1`, `metadata`, `products: []`, `categories: []`.
Metadata requires nonempty `site_id`, `catalog_version`, `source`, `extracted_at`,
`complete: true`, `total_products`, `total_categories`, `total_variants`. Catalogue version is
`V1_CATALOG` or `V3_CATALOG`. V3 products require at least one variant; Products V3
Query/Search alone omit variants and are not a complete extraction. Completeness must be established
by the exporter (all pages, scopes and languages), not guessed by this comparator.

Category fields: `id`, `name`, `slug`, `visible`, `localized`.
Product fields: `id`, `master_id`, `parent_master_id` (null or existing product master),
`name`, `slug`, `sku`, `barcode`, `currency`, `price`, `sale_price`, `options`, `variants`,
`inventory`, `category_ids`, `media`, `localized`, `fresha_ids`, `visible`, `description`,
`modifiers`, `tax`, `shipping`, `seo`, `subscriptions`, `digital`.
Variant fields: `id`, `master_id`, `sku`, `barcode`, `choices`, `price`, `inventory`, `media`,
`visible`, `price_data`. Product `price` is a normalized effective summary, not a V3 field.
Keep actual/compare-at/sale/unit pricing and schedules in variant `price_data` and any
additional source fields. `modifiers` and `subscriptions` are lists; tax/shipping/SEO/digital
containers are objects. Preserve unsupported-feature state explicitly; an empty container
must be justified by the source, never used to discard fields. Variant choices must match
the declared product options; unmanaged choices/custom text belong in modifiers.
IDs/SKUs/barcodes and money use strings. `sale_price` may be null. Product prices must
be finite nonnegative decimals. Object structures for `inventory`, `localized`, `choices`,
options and media must preserve all source detail; do not collapse to a single stock flag
or image URL if the export contains more. Normalization sorts category/Fresha membership
sets and variants by ID; media/options remain ordered. Unknown additional fields are
compared too, including key removal and JSON type changes. Nested inventory quantities
and feature-specific business rules are preserved/compared, not fully semantically validated.
Differences fail even when they might be legitimate (such as live sales).
Review them; there is no automatic acceptance or mapping override.

The tool cannot establish source completeness, validate every Wix business rule or prove
the export is restorable. Empty total-zero exports are legitimate only with independent
evidence. Adapter fixtures must cover representative real records before real use.

## Migration sequence and rollback

1. Obtain actual version/eligibility, official migration prerequisites and ID guarantees.
2. Locate Catalogue Lab source and six-tab workbook schema; inventory consumers and API versions.
3. Take timestamped complete exports and immutable ID/mapping manifests. Store securely.
4. Prove any rehearsal site's isolation from production commerce and payment configuration.
5. Rehearse only with owner-approved test data/context; compare all normalized records.
6. Exercise variants, price/stock rules, categories, translations and safe checkout handoff.
7. Present owner with execution plan, delta handling, cutover gates and supported contingency.
8. Execute live migration only after explicit approval. Reconcile post-cutover counts and IDs.

Official Wix documentation explicitly rules out a V3→V1 downgrade. Exports alone are not
a rollback. Obtain supported restoration capabilities and document forward repair/support
escalation before approval. The primary current safeguard is to stop before migration.
Studio publication also prevents republishing the original Classic branch; a separate
duplicate has independent data and is not a drop-in commerce rollback.
Any domain/subscription/site switching remains a separate Work/owner launch decision.

For Catalogue Lab, keep current flows operating. Once found, inspect import/export schemas,
pagination, retries, variants, ID persistence and six-tab controls. Add version-specific
adapters only as needed on isolated branches, with fixtures demonstrating preserved IDs,
parents and existing features. No rebuild, deployment or live overwrite is authorized.
