# Shared technical task register and Work handoff

Prepared in the local repository. This is the shared artifact for a future handoff;
no message has been sent to the separate ChatGPT Work project or Wix administrator.
The engineering feature branch is backed up on GitHub. No deployment, production update,
catalogue migration or payment occurred.

| ID | Workstream / owner | State | Deliverable / next evidence |
|---|---|---|---|
| ENV-01 | Cloud setup / Codex | Toolkit and live browser access verified | Frozen installation; existing platform CA verified; approved access to Chromium NSS database; reusable instructions saved |
| A-01 | Technical discovery / Work + Codex | Blocked on dashboard/source access | Record editor/catalogue versions, complete product/category counts, apps, Velo imports/scripts and dependency inventory |
| A-02 | Current official research / Codex | Completed for initial architecture | Exact official sources and field correspondences in official-findings.md; site eligibility still unknown |
| B-01 | Category architecture / Codex + Work | Provisional | Native shared category page preferred; validate AG Hair and target Studio controls against architecture acceptance gates |
| C-01 | Catalog V3 assessment / Work + Codex | Existing-site availability warning; eligibility unknown | Official request article says migration unavailable but mentions banner; require dashboard/Wix support confirmation, ID guarantees and forward repair plan |
| C-02 | Preservation tooling / Codex | Implemented and fixture-tested | Strict normalized snapshot comparison; needs actual schemas, exporter and real baseline |
| D-01 | Catalogue Lab / Work + owner | Source location unknown | Locate original app/repository and six-tab workbook through existing project records; owner need not know Git details |
| D-02 | Catalogue Lab adapters / Codex | Deferred until source found | Inspect existing code/contracts first; preserve features/IDs; isolate any justified adapter change |
| E-01 | SEO inventory / Codex + Work | Public sitemap and AG Hair HTTP checks complete | 1,434 URLs, 1,020 product-page URLs, 11 sitemap documents, 40/40 AG Hair internal destinations 200; supplement with dashboard/search sources |
| E-02 | Redirect plan / Codex | Validator ready; actual mapping unprepared | Build evidence-backed old/new map after complete URL inventory and route decision; no redirects activated |
| F-01 | Automated tools / Codex | Fixture tests passed | Unit and synthetic desktop/mobile browser coverage; see validation evidence |
| F-02 | Site QA / Codex + Work | Desktop/mobile baseline completed; review findings | 24 products each, no overflow, keyboard product-link focus reached, no H1 observed; complete commerce acceptance still requires isolated context |
| R-01 | Review/staging / Codex | Reviewed; GitHub API access restored | Main README boundaries preserved; draft PR prepared from docs/proposed-pr.md |
| L-01 | Production launch / Work + owner | Not authorized | Owner approval of concrete migration, redirect and launch plan after all gates pass |

Codex claims the `tools/`, `tests/`, technical documentation and evidence components for
this foundation. Work retains editor/browser configuration, visual layout and launch
coordination. This register is shared through the repository; no separate Work notification
is claimed. Coordinate new claims here before overlapping edits.

| IDs | Dependencies | Acceptance criteria |
|---|---|---|
| ENV-01 | Existing checkout, Node/Python/Chromium, registry access | Exact saved install runs; live NSS access documented; fixture and real baseline outcomes kept distinct |
| A-01/A-02 | Authorized dashboard/source evidence; current official docs | Version/count/dependency inventory has sources; unknowns remain explicit; contradictions escalated |
| B-01 | A-01, actual Category page availability and plan controls | One native category pilot meets responsive/branding/filter/SEO requirements before reuse |
| C-01/C-02 | A-01/A-02, complete real exports, supported pathway | Wix-confirmed eligibility; complete ID/variant/mapping comparisons; no unexplained differences; owner approval before action |
| D-01/D-02 | Locate Lab repo/workbook, inspect actual contracts | Existing features/IDs/parents preserved; any adapter reviewed and tested; no live Lab deployment |
| E-01/E-02 | Public and dashboard/search URL sources, target route decisions | Inventory reconciled across sources; approved mapping has no loops/chains; HTTP and canonical targets validated |
| F-01/F-02 | Tools, trusted browser, real manifests, isolated commerce context | Required QA matrix passes with real counts/results; skip/unrun/fail remain distinct; no real transactions |
| R-01 | Review and relevant passing checks, current main | Draft PR references evidence and limitations, preserves main policies, modifies only feature branch |
| L-01 | Prior gates, approved cutover/recovery plan | Explicit owner approval and Work launch coordination; no autonomous production publishing |

## Work's dashboard evidence checklist

1. Confirm supplied site ID and actual editor/Stores catalogue versions. Capture available
   Studio transition/branch controls and official guidance linked by that interface.
2. Determine exactly what a branch/copy shares with production: products, inventory, orders,
   translations, payment/business settings. Establish isolation before any commerce testing.
3. Inspect AG Hair and representative categories (small, large, empty, translated): page
   type, widgets, imagery/descriptions, sorting/filtering, product links, mobile behavior,
   manually maintained category content and attached code.
4. Export or inventory Velo/frontend/backend modules, custom code, npm packages, installed
   apps and external integration configurations without secret values.
5. Locate Catalogue Lab through existing project records, deployments and workbook links.
   Record repository/app location, six workbook tabs and actual export/import specifications.
   Obtain read-only complete product/category/variant/mapping exports securely.
6. Record route/SEO settings for default/secondary languages, canonicals, hreflang, category
   pages, native product pages and any redirects. Provide approved analytics landing URLs
   if available to detect sitemap gaps.
7. Establish a supported isolated checkout/payment test context with the owner; document
   delivery/tax/discount/stock dependencies. Never place a live order to prove readiness.

## Configuration and owner actions

Environment network draft adds only `www.lesalondieppe.com`, `lesalondieppe.com`,
`dev.wix.com`, `support.wix.com`, `static.wixstatic.com`, `static.parastorage.com`,
`siteassets.parastorage.com`, `api.github.com` (for the authorized draft PR);
package-manager/GitHub presets remain preserved.
Tested complete `install_script` and toolkit `start_skill` were saved. There is no app
server to start; retained dependencies and synthetic tests are distinct from live Wix QA.
Review and save the changes in environment settings, then publish the prepared cloud
environment when satisfied. This publishes the cloud snapshot, not either production site.
The draft save itself does not apply network changes or publish. Retry blocked read-only
requests after settings propagate; HTTP retries now succeed. Discover additional exact
destinations only when an affected operation requires them.

The owner explicitly approved the CA trust action after the initial automatic-review
rejection. Follow-up fingerprint checks corrected the earlier missing-CA diagnosis:
the platform CA already exists as `OpenAI-nebula-dns`. Verified live Chromium works when
execution can access that NSS database outside the read-only filesystem sandbox. No new
trust anchor or TLS bypass was needed. GitHub API access now works after network propagation.

No new secret is requested: there is no inspected integration requiring one yet. Existing
Git remote reads were attempted with platform authentication, without copying credentials.
Authenticated Wix inspection is still needed; connect through the supported product flow
or have Work supply read-only dashboard evidence. Do not send passwords/tokens in chat.

This is not migration or launch readiness. The owner must approve a concrete plan before
irreversible catalogue migration, bulk live updates, production redirects or publishing.

Code is retained on `engineering/wix-migration-foundation` and backed up on GitHub. Initial
remote probes returned no refs; a later probe found main and its engineering-boundary README.
That README is preserved, with toolkit details moved to docs/toolkit.md. No protected branch
was modified or pushed. A cloud draft save is separate from Git publication, environment
publication and fresh-task restoration; the latter two remain unverified.
