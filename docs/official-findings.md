# Verified Wix findings and decision implications

Official pages fetched successfully over HTTPS on 2026-10-22. These establish general
platform behavior; authenticated dashboard eligibility for this site is still unknown.

## Studio and native category architecture

| Official source | Confirmed behavior | Consequence |
|---|---|---|
| [Create a Studio version](https://support.wix.com/en/article/studio-editor-creating-a-studio-version-of-a-wix-editor-site) | Creates a separate editable branch; dashboard/business data, including products, are shared; design does not transfer; Premium needed to create and Studio plan needed to publish | Do not reimport products merely to redesign. Verify actual site controls and plan; do not change subscriptions autonomously |
| [About Studio branches](https://support.wix.com/en/article/studio-editor-about-studio-branches-of-wix-editor-sites) | “Once you publish the Studio branch, it is not possible to go back and republish the original Wix Editor branch.” Wix recommends duplicating beforehand; duplicates are separate sites without shared dashboard/data | Studio branch is not a commerce sandbox. Classic republish is not a rollback. Duplicate strategy requires a separate approved launch/contingency plan |
| Same branch article | Apps/data mostly shared; designs/pages/elements not transferred; some apps unsupported; older branches may require manual slug alignment | Inventory apps/Velo/pages and verify every old/new route; do not assume general data sharing preserves all dependencies |
| [Multilingual across branches](https://support.wix.com/en/article/wix-multilingual-request-managing-translations-across-site-branches) | Translation Manager only shows content from the published branch | Plan translated Studio content/QA around this limitation before launch |
| [About the Category page](https://support.wix.com/en/article/wix-stores-about-the-category-page) | Shared customization applies across categories; category image/description, native sidebar/filter/grid controls | Supports native-first shared architecture |
| [Customize Category page](https://support.wix.com/en/article/wix-stores-customizing-the-category-page) | “The Category page is not yet available to everyone.” Native responsive grid, sort/filter, options/cart controls; vertical menus disappear at small Studio breakpoints | Actual site availability and responsive controls are acceptance gates; provide mobile navigation |
| [Multiple category pages](https://support.wix.com/en/article/wix-stores-creating-multiple-category-pages) | Native Add Page Variant can start from original design or Velo; assign one variant to multiple categories; allowance depends on Premium plan | Use a small set of native presentation variants if needed; verify plan allowance, avoid per-category duplication |

The dedicated current branch articles describe a supported branch pathway. Older general
rebuild guidance/search snippets can conflict; rely on current dedicated documentation and
this site's actual controls. No exact variant allowance or app/Velo compatibility is assumed.

## Catalogue versioning and migration

| Official source | Confirmed behavior | Consequence |
|---|---|---|
| [Catalog Versioning](https://dev.wix.com/docs/api-reference/business-solutions/stores/catalog-versioning/introduction) | V1 and V3 are not backwards compatible; “Once a store has been upgraded to V3, it will not be downgraded to V1.” Page displayed update 13 October 2026 | Irreversible-upgrade approval gate; plan backups and forward repair, never promise downgrade |
| [Get Catalog Version](https://dev.wix.com/docs/api-reference/business-solutions/stores/catalog-versioning/get-catalog-version) | Read-only `GET https://www.wixapis.com/stores/v3/provision/version`; published scope Read v3 catalog (PII) | Requires authorized Wix context; not inferred from public markup, Studio or a generic GitHub token |
| [Version sample flow](https://dev.wix.com/docs/api-reference/business-solutions/stores/catalog-versioning/sample-flow) | Values `V1_CATALOG` and `V3_CATALOG` guide API routing | Catalogue Lab should detect generation and select a version adapter after existing source inspection |
| [Catalog V3 introduction](https://dev.wix.com/docs/api-reference/business-solutions/stores/catalog-v3/introduction) | Each site supports one generation at a time | Branch creation does not establish V3 upgrade; mixed-generation sites need compatible integrations |
| [V1 to V3 guide](https://dev.wix.com/docs/api-reference/business-solutions/stores/catalog-v3/catalog-v1-to-v3-migration-guide) | “This guide does not provide an automatic migration path.” Page displayed update 30 December 2025 | It is an integration/schema migration guide, not proof this site can initiate an upgrade |
| [Existing-site catalogue migration request](https://support.wix.com/en/article/wix-stores-request-migrating-site-to-the-new-product-catalog) | “Currently, it is not possible to migrate an existing Wix Stores site to the new product catalog.” Gives creating a new site as workaround; the same page also mentions a migration banner | Official guidance is internally inconsistent. Do not assume an existing-site upgrade is available; require actual dashboard and Wix support confirmation |

## Verified field correspondence from migration guide

| V1 concept/path | V3 correspondence / behavior | Preservation test |
|---|---|---|
| Product `id`; `variants[i].id` | `id`; `variantsInfo.variants[i].id` | Schema correspondence does not prove IDs survive an actual site upgrade |
| No variant on simple product | Every V3 product has at least one variant | Reject V3 normalized records with zero variants |
| `manageVariants` / product options | Removed; managed options → options; unmanaged → modifiers | Preserve selections, price modifiers and option combinations separately |
| `customTextFields` | `FREE_TEXT` modifiers | Preserve field definitions, required flags and limits; do not collapse into variant options |
| Product-level price | Variant-level prices | Discounted original → `compareAtPrice.amount`; discounted → `actualPrice.amount`; no-discount original → actual, compare-at empty |
| Products Query/Search variants | V3 Query/Search omit variants; Read-Only Variants API needed for variant-centric queries | Explicit variant retrieval/pagination and independent totals required |
| `collectionIds[i]` | `directCategories[i].id` | Compare ID/membership sets; verify category ordering separately |
| `inventoryItemId` on product | Dedicated inventory service; product/variant identity used | Export all applicable inventory/location data separately |
| `productPageUrl.base`, `.path` | `url.url`, `url.relativePath` | Compare full URLs and relative paths; add redirects only when needed |
| Product/media fields | Changed structure with URL/dimensions/alt counterparts | Preserve order, primary/variant media and alt; verify resolution |
| Domain events/webhooks | Separate V1/V3 events | Inventory current consumers and update subscriptions with version-specific tests |

Shipping, tax groups, unit pricing, visibility, descriptions, SEO, digital/subscription data
and all feature-specific fields still need exact inspected source/target contracts. The
normalized comparator preserves declared containers and unknown fields, but cannot prove
an exporter included every business field. Catalogue Lab adapters must cover them explicitly.

The existing-site migration request article is a concrete availability warning, not a
reason to rebuild/reimport the live store. Proceed with native category modernization
independently where supported and preserve the existing catalogue until a site-specific
supported pathway and approved plan exist. Do not create a replacement store autonomously.

No authenticated version call, owner-facing upgrade eligibility, supported ID preservation
contract or migration action for site `89082970-5cc7-4abf-be8a-8249f6a7755e` has been verified.
