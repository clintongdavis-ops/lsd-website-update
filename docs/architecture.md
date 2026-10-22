# Technical architecture and compatibility report

Status: provisional architecture; site-specific compatibility is unverified.
Evidence date: 2026-10-22 (client date, America/Halifax).
Site supplied by owner: `89082970-5cc7-4abf-be8a-8249f6a7755e`.

## Evidence and scope

The owner reports Classic Wix Editor, Wix Stores Catalog V1, Velo, Multilingual,
Premium, existing category pages, a Catalogue Lab and a six-tab Master Catalogue
workbook with Wix/Fresha mappings. These are inputs, not authenticated observations.
The selected Git checkout contains no existing application or Velo source. No Wix,
Google Sheets or Fresha connector is available. Public website and current Wix
documentation now work after the network update. See the evidence log and
[verified official findings](official-findings.md).
Product counts, category relationships, code dependencies, transition availability,
Catalog V3 eligibility and source integration contracts remain unknown.

## Category architecture decision

| Approach | Decision | Gate |
|---|---|---|
| Native shared Wix Stores category page | Preferred provisional architecture | Demonstrate required category-bound imagery/descriptions, native grid, filters/sorting, SEO and translations in the actual target editor |
| Studio variants/reusable sections | Presentation exceptions only | Prove available controls, category binding and maintainability without duplicate product records |
| Custom CMS/Velo storefront | Deferred | Native acceptance failure and approved gap analysis must justify custom maintenance and commerce/SEO obligations |

Retain native product pages, options/variant selection, inventory, pricing, cart and
checkout. Reuse existing product/category records and mappings where the supported
transition preserves them. Do not promise that IDs survive until verified. Do not
create a second catalogue in CMS. Category-grid variant purchase is optional unless
the owner identifies it as a requirement; native product-page selection is the default.

AG Hair is the supplied design reference. HTTP inspection confirms 24 rendered product
items, filters and cart controls. Desktop/mobile browser baselines now complete with verified
HTTPS and authorized NSS access. Both display 24 product items and expose no H1; this is an
observed baseline issue for the native category pilot, not full SEO/accessibility validation.
Work should
identify its actual page type, content/widgets, responsive settings, manually curated
elements, category binding and page code. Reproduce category imagery, brand description
and styling using shared native settings first. Preserve readable long product titles,
consistent image presentation, stock states, keyboard access and mobile grid usability.

## Studio transition gates

A Studio branch is not a Catalog V3 upgrade or a commerce sandbox. Current official Wix
guidance confirms a Studio branch shares dashboard/business data, including products;
design/pages/elements do not carry over. Premium is required to create and a Studio plan
to publish. Once Studio is published the original Classic branch cannot be republished.
A duplicate is an independent site, not a shared-data rollback. Verify actual controls,
apps, Velo and URLs before proposing a transition. Translation Manager shows only the
published branch, which affects prelaunch translation QA.

Inventory page IDs/routes, Velo element IDs, event handlers, backend/web modules, imports,
custom scripts, npm dependencies, installed apps, third-party services, multilingual URL
rules, SEO overrides and any custom product/category pages. Classify each as preserved,
reconfigured, recreated, incompatible or unknown, with evidence. Until source export and
dashboard inspection are available, no site-specific dependency can be classified as compatible.

The site is not ready for a Studio transition or Catalog V3 migration approval. No Velo
adapter is justified yet. Build version-specific adapters only against verified schemas
and tested existing Catalogue Lab contracts, preserving Master Product IDs and parents.

## Data flow and ownership

Authoritative Master Catalogue → existing Catalogue Lab → documented Wix/Fresha mappings
→ native commerce catalogue → native category/product/cart/checkout.

This is the owner's described flow, pending source inspection. The engineering toolkit
reads snapshots and public URLs only. Work owns dashboard actions, visuals and launch
coordination; Codex owns specifications, adapters where justified, validation and review.
The repository handoff is prepared locally; no external Work message has been sent.

## Evidence to collect from official sources

Current sources and exact field correspondences are captured in
[official findings](official-findings.md). Catalog generations are not backwards compatible,
V3 cannot downgrade to V1, and the schema guide is not an automatic upgrade path.
Get Catalog Version is an authenticated read-only API; the owner's V1 statement remains
unverified. Cross-check general behavior against this site's dashboard controls and source.
