# LSD migration engineering

Technical foundation for Le Salon Dieppe / LSD Beauty. No production writer, publisher,
catalogue migrator, or payment/order automation is included.

## Local setup

Use the existing isolated cloud checkout; do not create another worktree for routine startup.
Node 24 (tested 24.19.0), npm, Python 3.12+, and Chromium are required. Chromium is already
installed in this cloud image. Set `CHROMIUM_PATH` if a different verified installation is used.

```sh
cd /workspace/lsd-website-update
npm ci --cache /tmp/lsd-npm-cache --no-audit --no-fund
npm test
```

There is no application server: this repository began empty and is an engineering toolkit,
not the existing Wix site or Catalogue Lab source. Tests exercise synthetic data and a
synthetic browser page. Passing them validates the tools, not the production website.

## Read-only discovery and validation

```sh
mkdir -p artifacts
python3 tools/audit.py inventory https://www.lesalondieppe.com > artifacts/sitemap.json
python3 tools/audit.py page https://www.lesalondieppe.com/shop-aghair > artifacts/aghair.json
python3 tools/audit.py links https://www.lesalondieppe.com/shop-aghair > artifacts/aghair-links.json
python3 tools/audit.py redirects path/to/proposed-redirects.csv
python3 tools/catalogue.py path/to/normalized-before.json path/to/normalized-after.json
```

Exit status: 0 = check passed, 1 = differences/incomplete audit, 2 = invalid input or request
failure. Preserve command exit codes. Do not treat an empty, blocked, or truncated inventory
as complete. Sitemap coverage excludes unlisted, hidden and orphan URLs. The page command
reports linked URLs; `links` checks their HTTP destinations within the specified limit. It reads server HTML, not a
rendered Wix page. Cross-origin redirects/entries need separate review and are refused.
Redirect validation checks the proposed CSV only; it does not activate or verify live redirects.

Private exports and results belong in ignored `artifacts/` or an approved secure store.
Do not commit customer data, secrets, full environment dumps or proprietary raw exports.
See [normalized export contract](catalogue-contract.md) before using the comparator.

## Browser QA

`npm run test:browser` runs desktop/mobile harness tests with intercepted synthetic HTML.
For real read-only category checks, create a JSON manifest outside tracked source with all
fields from `tests/browser/category.spec.cjs`'s fixture, using verified URLs, expectations,
and inspected selectors. Run:

```sh
LSD_QA_MANIFEST=/absolute/path/to/manifest.json npm run test:browser
```

The browser blocks non-GET/HEAD requests. Wix may need POST queries to render; diagnose
any resulting failure rather than claiming the site is broken or enabling writes broadly.
Live Chromium currently fails platform-proxy certificate trust. Adding the platform CA to
its persistent user trust store was rejected by automatic approval review; explicit owner
approval is pending. TLS verification remains enabled. HTTP discovery works with the
platform-provided trusted system bundle; synthetic Chromium tests work without networking.

No add-to-cart, checkout, sorting/filter correctness, payment, performance or full accessibility
validation is claimed by this smoke suite. See the [QA plan](qa-plan.md) for those gates.

Start with [architecture](architecture.md), [evidence](../evidence/discovery.md),
[task register and Work handoff](task-register.md). Production publication and irreversible
catalogue changes require owner approval of a concrete plan.
