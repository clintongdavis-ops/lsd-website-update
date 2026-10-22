# Validation results

2026-10-22. Target: engineering toolkit in `/workspace/lsd-website-update`.

| Check | Outcome | Scope |
|---|---|---|
| Frozen installation (`npm ci`) | Passed, including rerun through exact saved install script | Lockfile and dependencies unchanged by refresh |
| Python unit suite | 24 passed, 0 failed, 0 skipped | Synthetic preservation/error/SEO/link/redirect fixtures |
| Playwright suite | 4 passed, 0 failed, 0 skipped | Intercepted synthetic HTML, desktop/mobile Chromium; no live site validation |
| Comparator CLI | Expected exits 0 (same), 1 (changed), 2 (malformed) verified; JSON output parsed | Synthetic normalized snapshots |
| Redirect proposal CLI | Exit 0 with valid synthetic proposal | Structural proposal check; no live redirect activation |
| Public sitemap | 11 documents, 1,434 unique URLs, no errors/truncation | Published sitemap coverage only |
| AG Hair HTTP SEO | 200; title, description, self-canonical, en-ca/x-default alternates observed | Server HTML and headers, not all SEO semantics |
| AG Hair internal HTTP destinations | 40 checked, all 200 | Links from server HTML; identity/semantic correctness not established |
| Current official docs | Read successfully; exact links/excerpts recorded | General platform behavior, not this site's authenticated eligibility |
| Real desktop/mobile Chromium | Blocked: ERR_CERT_AUTHORITY_INVALID | Platform proxy CA missing from Chromium user trust; import rejected by automatic approval review |
| Authenticated Wix/version and Catalogue Lab | Unrun: access/source/export unavailable | No compatibility or ID-preservation success claimed |
| Cart/checkout, performance, accessibility, real redirects | Unrun | Planned gates; no transactions or production changes |
| Code review | Two read-only specialist reviews; concrete findings fixed and regression tests passed | Final comparator review found no remaining critical issue within limited normalized contract |
| Configuration persistence | Saved confirmed, requires publication | Install script, agent startup instructions and seven exact network domains; presets preserved |

The install script was executed in its documented directory and then saved unchanged.
No service is required for this toolkit. Synthetic tests require no network. Live HTTP
access now succeeds; live browser trust remains a separate unresolved setup requirement.
The environment supports toolkit development, but full migration environment readiness,
cloud publication and fresh-task restoration are not claimed.
