# QA and SEO migration gates

Current automated results validate tools and synthetic browser fixtures. Public HTTP
discovery succeeded: 1,434 sitemap URLs and all 40 server-HTML internal AG Hair links
returned HTTP 200. This is not catalogue completeness or full site QA. Live browser QA
now completes for desktop and emulated Pixel 7 with authorized NSS database access and
TLS checks enabled. Both profiles have no H1 observed; helper exit 1 requires review.
Authenticated site/source access is still absent.

## URL inventory and mapping

Collect public sitemap index and every child sitemap, navigation/internal links, Wix
dashboard page/SEO exports, category/product URLs, translated URLs and owner-supplied
analytics/Search Console landing-page exports where authorized. Compare these sources
to identify unlisted and orphan pages; public sitemap discovery alone is not complete.
Do not invent URL patterns from Wix defaults. AG Hair metadata and native gallery hooks
were inspected over HTTP; dynamic interactions remain unverified. The tracked
`evidence/public-url-inventory.csv` contains every sitemap URL with route decisions pending.
It is an inventory, not the redirect CSV input; targets cannot be supplied before route review.
Matching `/collections/` and `/copy-of-collections/` slugs warrant duplicate-content review;
do not delete or redirect either set without comparing content and canonical intent.

Map old URL → proposed target URL → reason → source evidence → approval state. Use CSV
columns `old_url,new_url,status` for structural validation. Additional columns are allowed.
Avoid unnecessary redirects when URLs can remain stable. Reject duplicate sources,
self-redirects, loops and chains. Approved old URLs should return a single permanent
301 to the expected target; targets must return 200 with intended canonical, indexability,
language and content. `audit.py redirects` checks proposals only, not HTTP redirect chains.
Cross-origin redirects require explicit review outside the current same-origin audit tool.
No production redirect activation is implemented.

For every category/product and representative editorial page: verify title, description,
canonical uniqueness/target, robots directives, hreflang reciprocity, sitemap inclusion,
internal links and appropriate structured data. Detect duplicate indexable category pages.
Use rendered browser checks alongside server HTML, and verify expected metadata values,
not simply their presence. Fetch linked destinations before claiming broken-link coverage.

## Test matrix

| Area | Repeatable test | Required context/evidence | Current state |
|---|---|---|---|
| Tool integrity | Unit tests: incomplete sitemap/errors, ID loss, orphan parent, SKU/price/media/membership drift, redirect loops | Synthetic fixtures with failure assertions | Implemented |
| Browser harness | Desktop 1440×900 and mobile 390×844 metadata, category content, product hrefs, overflow, keyboard focus | Synthetic HTML intercepted in Chromium | Implemented |
| Real desktop/mobile | Native-hook observations with proper desktop/mobile UA, geometry, focus and screenshots | Fresh unauthenticated contexts; non-GET/HEAD HTTP, WebSockets and service workers blocked | Two profiles completed; 24 items each, no horizontal overflow, product-link focus reached; no H1 observed; full acceptance unrun |
| Navigation/category links | All discovered links reach expected page/language, no broken targets | Complete crawl sources, bounded GETs and final URL/status reports | HTTP link checker implemented; AG Hair 40/40 destinations 200; content identity/site-wide coverage unrun |
| Variants | All valid combinations map to exact IDs, SKU, media, price and stock rules | Verified isolated test site/data and source baseline | Unrun |
| Pricing/inventory | Compare complete baseline and after snapshots, reconcile sales | Exports, extraction timestamps, explicit delta ledger | Comparator implemented; real exports unavailable |
| Sort/filter | Assert ordered product IDs/price order, filter memberships, reset and empty states | Actual native controls/selectors and baseline catalogue | Unrun |
| Add-to-cart | Correct variant, quantity, price, currency, unavailable-item handling, cart cleanup | Owner-approved isolated commerce context; prove no live order side effect | Unrun; absent from read-only suite |
| Checkout | Validate native checkout handoff and configured delivery/tax/discount behavior | Verified Wix-supported test mode and authorized test data | Unrun; never place real orders or charge |
| SEO/redirects | Old→target 301 chain, target 200, intended canonical/hreflang/sitemap | Approved mapping and staged/public deployment | Proposal validator implemented; HTTP redirects unrun |
| Performance | Repeated cold/warm measurements, median results and variance | Same Chromium/device/network profile; baseline and target | Unrun; no performance claim |
| Accessibility | Automated audit plus keyboard, focus, screen reader and contrast review | Actual rendered target, documented audit tool/version | Unrun; focus smoke is not conformance |

For every run record commit, test target, time, browser/version, viewport, network profile,
fixture vs real data, pass/fail/skip counts and artifacts. No numeric performance target or
improvement can be asserted until baseline measurement and agreement on budgets.
Required failures must be diagnosed as environment vs application defects. Do not modify
production data, relax assertions or count skipped/zero-test runs as passes.

## Release stop conditions

Unknown migration eligibility, unsupported reversal/repair plan, unexplained ID/count
differences, missing mappings, shared rehearsal commerce data, live payment risk, broken
critical URLs, failed variant/cart behavior, or missing owner approval stop the relevant
release action. Tool readiness does not grant site migration or production launch readiness.
