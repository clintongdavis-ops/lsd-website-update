# Discovery evidence

Recorded 2026-10-22 (client date, America/Halifax). No secret values recorded.

| Observation | Evidence | Implication |
|---|---|---|
| Runtime became ready | Environment wait tool returned `status: ready` | Workspace inspection was performed after provisioning |
| Selected checkout initially empty | `/workspace/lsd-website-update` contained only `.git`; `git status`: no commits on `work`; no tracked files | No existing Wix/Velo/Catalogue Lab source to inspect |
| Git remote probe returned no refs | `git ls-remote origin HEAD refs/heads/main` completed without a returned ref; `git show-ref` found none | No remote base ref available for a normal PR at baseline; not a missing-token diagnosis |
| Available runtimes | Node 24.19.0, Python 3.12.14, Chromium 154.0.8037.57 | Suitable for toolkit and browser harness |
| Initial npm cache path unwritable | npm attempted `/home/agent/.npm/_cacache` and failed ENOENT | Corrected with `--cache /tmp/lsd-npm-cache`; verification not disabled |
| Dependencies installed | Registry resolved `@playwright/test` 1.64.1, lockfile generated, `npm ci` succeeded | Reproducible package installation available |
| Live read-only access blocked | `curl -I https://www.lesalondieppe.com/sitemap.xml` and `curl -I https://dev.wix.com/`: CONNECT tunnel 403 from proxy | Public site inventory and current official documentation not verified |
| Initial audit DNS failure | Preflight direct DNS lookup failed despite configured HTTPS proxy | Audit adjusted to let configured egress proxy resolve hostnames; local/private literal checks retained |
| Available secret names checked | Relevant exported names: `GH_TOKEN` present; no Wix/Fresha/catalogue/Google names found | No values printed; token presence does not establish Wix access |
| Connected tools checked | No Wix, Sheets, Fresha or browser-admin connector available | Site identity/version/counts and integration contracts remain unverified |
| Owner does not know Lab location | Owner reply in chat | Locate through existing project/Work records; do not rebuild or ask for secret values |
| Parallel technical review | Architecture and catalogue assessment agents; read-only reviews of code | Review feedback integrated; separate artifacts do not imply external Work contact |

## Subsequent verified outcomes

The saved network changes propagated during this session. Verified HTTPS HTTP reads of
the public site and current Wix documentation now work; initial 403 observations above
are historical. See `public-discovery.json`, `public-url-inventory.csv`,
`aghair-http-audit.json`, `aghair-links.json` and `docs/official-findings.md`.

Public sitemap traversal: 11 documents, 1,434 unique URLs, including 1,020 `/product-page/`
URLs, 147 `/collections/` URLs and 147 `/copy-of-collections/` URLs. No fetch errors or
limit truncation occurred. Sitemap coverage is not a complete catalogue export.
AG Hair returned 200, a self-canonical, title/description and en-ca/x-default alternates.
All 40 discovered server-HTML internal links returned 200. Content identity and all-site
broken-link coverage are not established. Initial HTML has 24 rendered product items.

Chromium initially failed `ERR_CERT_AUTHORITY_INVALID` and automatic review rejected CA
import. The owner then explicitly approved the trust work. The initial missing-CA diagnosis
was incorrect: fingerprint comparison proves the existing NSS certificate
`OpenAI-nebula-dns` matches `environment-proxy-ca.crt` (SHA-256
`C71B4D1E9D7775C538C688AB10CEA9CE417D7312E89838F9D15FF73256CD7FC3`). Importing
that duplicate returns success without a second nickname. Live Chromium succeeds when run
with approved normal access to the NSS database outside the filesystem sandbox. TLS
verification remains enabled; no new trust anchor or bypass was required.

Chromium's official Linux certificate-store instructions were read at
https://github.com/chromium/chromium/blob/main/docs/linux/cert_management.md. They document
the M146 default store change and fallback to the existing `$HOME/.pki/nssdb`.

## Evidence boundaries

No complete all-source live URL inventory, authoritative product/category count, Velo dependency graph, V3
eligibility result, Studio compatibility confirmation, real commerce test or performance
baseline is available. These remain explicit tasks, not inferred passes.

Current official findings are cited separately. Architecture implementation and migration
eligibility remain site-specific gates requiring dashboard/source evidence.
