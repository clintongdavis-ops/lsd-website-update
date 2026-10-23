# Parallel collection-route review

Observed 2026-10-23. The original public sitemap contained 147 `/collections/` URLs and
147 `/copy-of-collections/` URLs. The accompanying route-pair CSV matches equal path
suffixes only; it does not prove equivalent content or prescribe redirects.

## Representative HTTP evidence

Four suffixes were checked under both prefixes: `ag-care`, `milkshake`, `shampoos`, and
`all-products`. All eight returned 200 without redirect, each with a self-canonical and
generic title `LSD Le Salon Dieppe`. Initial HTML had no meta description, H1–H3 headings
or distinct product-page links. No sampled response had meta robots or `X-Robots-Tag`.
This establishes no observed exclusion in those responses, not Google indexing status.

The separate `/shop-aghair` page returned 200, informative title/description, brand content,
self-canonical and 24 distinct product-page links. See `evidence/collection-route-samples.json`
for sampled statuses, exact URLs, metadata and raw-response hashes.

## Public route configuration dependency

The public `script#wix-viewer-model` contains
`siteFeaturesConfigs.dynamicPages.prefixToRouterFetchData` entries for both prefixes.
Each `optionsData.bodyData.config.patterns["/{name}"].config` declares source collection
`Stores/Collections`, page size 6, lowercase routing, name-ascending order and `seoV2: true`.
Their item-route SEO settings declare description expression `{_id}`, image `{mainMedia}`
and `robots: index`. Distinct page roles are titled `Collections (Name)` and
`Copy of Collections (Name)`. `/collections` also defines a list route with page size 12.
The public model is described here selectively; no complete bootstrap payload is copied.

This verifies parallel dynamic CMS templates over the same Stores collection, not identical
layouts, audiences or results. It is a concrete dependency for the V1/V3 assessment:
verify any future catalogue generation's support for this system collection/schema rather
than assuming these templates survive unchanged. It does not authenticate the site version.

Both routers declare `fetchUsingGet: true` and a base path ending
`/_api/dynamic-pages-router/v1`. No official read-only public contract for this internal
endpoint was established, and no new POST allowance was made. Browser probes blocked
non-GET/HEAD HTTP, WebSockets and service workers. Only telemetry/site-member POST paths
were observed blocked in the focused AG pair capture; no router POST was observed.

Constrained browser probes found blank views for the AG pair and some other samples;
`/collections/shampoos` and `/collections/all-products` displayed an access-restricted
message. One copy-of-milkshake browser probe timed out. These short, constrained observations
do not establish production permissions defects or rendered content equivalence.

## Decisions required before any redirect

The combination of sitemap exposure, common source collection, generic metadata and
independent self-canonicals creates a concrete duplicate/low-value-indexing risk. Work
must confirm intended audience, permissions, actual rendered content, inbound links and
Search Console performance for both templates. Decide an authoritative route only after
those checks and the native-category pilot's target routes are known.

If a template is unintended, prepare a reviewed per-URL action: preserve, correct metadata,
restrict/indexing change where appropriate, or redirect to a genuinely equivalent native
page. Replace the description-ID expression if retained. No blanket deletion, noindex or
301 activation is authorized by this report. All target decisions in the route-pair CSV
remain pending owner review.
