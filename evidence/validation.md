# Validation results

2026-10-22. Target: engineering toolkit in `/workspace/lsd-website-update`.

| Check | Outcome | Scope |
|---|---|---|
| Frozen installation (`npm ci`) | Passed, including rerun through exact saved install script | Lockfile and dependencies unchanged by refresh |
| Python unit suite | 24 passed, 0 failed, 0 skipped | Synthetic preservation/error/SEO/link/redirect fixtures |
| Playwright suite | 4 passed, 0 failed, 0 skipped | Intercepted synthetic HTML, desktop/mobile Chromium; no live site validation |
| Comparator CLI | Expected exits 0 (same), 1 (changed), 2 (malformed) verified; JSON output parsed | Synthetic normalized snapshots |
| Inspector failure handling | Exit 2 and replacement of stale prior-success report verified | Deliberately missing browser executable in an isolated temporary working directory |
| Redirect proposal CLI | Exit 0 with valid synthetic proposal | Structural proposal check; no live redirect activation |
| Public sitemap | 11 documents, 1,434 unique URLs, no errors/truncation | Published sitemap coverage only |
| AG Hair HTTP SEO | 200; title, description, self-canonical, en-ca/x-default alternates observed | Server HTML and headers, not all SEO semantics |
| AG Hair internal HTTP destinations | 40 checked, all 200 | Links from server HTML; identity/semantic correctness not established |
| Current official docs | Read successfully; exact links/excerpts recorded | General platform behavior, not this site's authenticated eligibility |
| Real desktop/mobile Chromium | Two profiles completed; helper exit 1 for no H1 observed | 200, 24 rendered items each; no overflow; product link reached by Tab; real UA/device profile; request restrictions recorded |
| Authenticated Wix/version and Catalogue Lab | Unrun: access/source/export unavailable | No compatibility or ID-preservation success claimed |
| Cart/checkout, performance, accessibility, real redirects | Unrun | Planned gates; no transactions or production changes |
| Code review | Two read-only specialist reviews; concrete findings fixed and regression tests passed | Final comparator review found no remaining critical issue within limited normalized contract |
| Configuration persistence | Saved confirmed, requires publication | Install script, agent startup instructions and eight exact network domains; presets preserved |

The install script was executed in its documented directory and then saved unchanged.
No service is required for this toolkit. Synthetic tests require no network. Live HTTP
access and live Chromium now succeed with approved NSS database access. The existing
trusted CA was reused; verification remains enabled. The helper's no-H1 observation is
a review finding, not a passing full-site audit.
The environment supports toolkit development, but full migration environment readiness,
cloud publication and fresh-task restoration are not claimed.

The feature branch was pushed to GitHub, and main's engineering-boundary README was
integrated without modifying main. Runtime tool/test code is unchanged from the validated
commit. Initial draft PR creation failed because the egress proxy refused api.github.com
(CONNECT 403); both unauthenticated root and authenticated repository read probes also
failed at the proxy. Git push success does not establish API access. The domain is saved
in the environment draft; subsequent authenticated repository API reads now succeed.
docs/proposed-pr.md retains the current intended description.
Draft PR #1 was subsequently created and attached to this task:
https://github.com/clintongdavis-ops/lsd-website-update/pull/1. It is unmerged.

The live inspector received a read-only review. Result freshness, unique screenshot
directories, WebSocket blocking and product-destination link precision were corrected
and exercised by the current run. The Pixel 7 profile uses its recorded Android UA;
Chromium engine version and layout width are recorded separately, not presented as
a physical-device test. Blocked requests, including some static assets, limit rendering
acceptance; the baseline is an observation, not a production quality certificate.
