# Native AG Hair category pilot specification

Status: ready for dashboard configuration review; no Studio page or store data was changed.
Owner: Work for editor configuration, Codex for checks, owner for shared-data/launch approval.
Dependencies: actual Studio branch and app parity, native Category page availability, plan
variant allowance, and confirmed category identity/membership from the dashboard.

## Binding and route requirements

Use the existing AG Hair commerce category and products. Confirm its actual Wix category
ID in the dashboard; `/shop-aghair` and the dynamic `/collections/ag-care` slug alone do
not establish category identity. Do not import products or create a second CMS catalogue.
The published AG Hair view currently renders 24 product cards; this is not the total
category count or an authoritative membership manifest.

Prefer the shared native Stores Category page. Use one native page variant only if a
demonstrated brand-layout requirement cannot be expressed by the shared design. Keep the
native product page, variants, stock, price, cart and checkout components.

Retain `/shop-aghair` if the supported native route configuration allows it. Verify the
actual generated target URL and route conflicts before committing to preservation. If the
native route must differ, prepare an evidence-backed old→new recommendation; keep the old
page live until the owner approves cutover/redirects. Do not choose the parallel dynamic
collection templates as redirect targets based on matching slugs alone.

## Editor configuration checklist

| Component | Pilot configuration / requirement | Acceptance evidence |
|---|---|---|
| Category identity | Native binding to verified existing category ID | Dashboard ID and complete membership source; no imports/reassignment |
| Header | Category name as a meaningful H1, brand image and existing description | Rendered accessible heading and category-specific content; current baseline has no H1 |
| Brand assets | Reuse approved AG imagery and existing brand introduction | Responsive crop and descriptive accessible alternative; decorative images identified |
| Product grid | Responsive native grid with readable names/prices and stable image areas | Desktop/mobile views, long names and multiple media ratios; no overflow |
| Product identity | Native links reach expected product and language | Link-ID mapping against approved catalogue baseline |
| Options/sizes | Preserve native product selection; make selectors/programmatic names accessible | Options/variant identity and stock/price remain consistent; no inferred SKU matching |
| Sort/filter | Native sort plus appropriate existing category/price/size/need filters | Correct sets/order/reset/empty states; label sort control and visible filters |
| Cart | Keep native behavior; do not use a custom substitute | Safe isolated-context cart test before approval; no live order/payment |
| Navigation | Native responsive category navigation with usable touch targets | Keyboard focus, mobile menu availability and label/target-size review |
| SEO/languages | Intended title/description/canonical/robots/hreflang and structured data | Server and rendered checks against explicit expected values for each language |

Studio branches share business data. Editing category records, memberships, inventory,
prices, images or descriptions may affect the live site even while designing an unpublished
branch. Use current approved values first; obtain approval for any required shared-data
change. Branch-local presentation changes are separate from commerce-record changes.

## Accessibility findings to resolve during the pilot

The October 23 axe baseline flags an unnamed desktop button, an unnamed mobile sort
select (`#sortBy`), contrast issues, small targets, and desktop list semantics; mobile also
has an ARIA attribute finding. Counts/selectors are in the accessibility evidence. These
are automated observations under constrained rendering, not a full conformance verdict.
Resolve through native component configuration and current supported Wix widgets first.
If a native control itself remains defective, record its exact component/version and
escalate to Wix before proposing custom commerce code.

## Pilot release gate

Work records one configured unpublished pilot and its actual target URL, component types,
category binding, shared-data changes (if any), breakpoints and language coverage. Codex
then runs the target-specific checks. Approve reuse only after responsive navigation,
product links, options, sorting/filtering, stock/pricing, safe cart/checkout entry, SEO,
accessibility review and agreed performance measurements pass. Existing public baseline
checks do not substitute for this pilot acceptance. No numerical performance improvement
is promised before comparable baseline/target measurement.
