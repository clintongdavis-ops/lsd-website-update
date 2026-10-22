# Shared technical task register and Work handoff

Prepared in the local repository. This is the shared artifact for a future handoff;
no message has been sent to the separate ChatGPT Work project or Wix administrator.
The engineering feature branch is backed up on GitHub. No deployment, production update,
catalogue migration or payment occurred.

| ID | Workstream / owner | State | Deliverable / next evidence |
|---|---|---|---|
| ENV-01 | Cloud setup / Codex | Local toolkit verified; draft saved | Frozen npm installation, Python and Chromium harness; HTTP network works; live browser trust approval pending |
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
| F-02 | Site QA / Codex + Work | HTTP sample passed; live browser blocked | Chromium certificate trust approval; actual manifests and isolated commerce context required; no orders/payments |
| R-01 | Review/staging / Codex | Local review and branch | Review fixes tested; feature branch pushed; current main README boundaries preserved during integration |
| L-01 | Production launch / Work + owner | Not authorized | Owner approval of concrete migration, redirect and launch plan after all gates pass |

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
`siteassets.parastorage.com`; package-manager/GitHub presets remain preserved.
Tested complete `install_script` and toolkit `start_skill` were saved. There is no app
server to start; retained dependencies and synthetic tests are distinct from live Wix QA.
Review and save the changes in environment settings, then publish the prepared cloud
environment when satisfied. This publishes the cloud snapshot, not either production site.
The draft save itself does not apply network changes or publish. Retry blocked read-only
requests after settings propagate; HTTP retries now succeed. Discover additional exact
destinations only when an affected operation requires them.

Automatic approval review rejected importing the supplied proxy CA into Chromium's user
trust store because it changes a persistent security boundary beyond explicit authorization.
The existing system trust bundle supports verified HTTP discovery; no verification bypass
was used. Live browser QA needs approval of that specific trust change or a platform-provided
supported browser trust configuration. Local fixture browser tests remain usable.

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
