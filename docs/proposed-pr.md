Prepare a read-only engineering foundation for the Wix Studio migration while keeping the existing Wix commerce backend and authoritative catalogue workflow intact. The native shared Category page is the preferred design; actual site eligibility, Velo dependencies and Catalogue Lab contracts still need dashboard/source evidence.

Includes:
- Current official Wix findings, field-level V1/V3 correspondence, preservation/contingency plan and a technical Work task register.
- Public sitemap inventory of 1,434 URLs, including 1,020 product-page URLs; all 40 internal destinations discovered in AG Hair server HTML returned 200. These are not authoritative catalogue counts or a full site crawl.
- Read-only sitemap, SEO, link and redirect-proposal checks; a strict normalized catalogue comparator; desktop/mobile browser smoke harness.

Validation: exact reusable install script (`npm ci` and `npm test`) completed; 24 unit tests and four synthetic Chromium tests passed. Comparator CLI exit statuses 0/1/2 and redirect proposal CLI were exercised. Read-only specialist reviews found and corrected typing, incomplete-variant, header-SEO and request-blocking gaps. Main's engineering-boundary README is preserved; toolkit commands live in docs/toolkit.md.

Release blockers remain explicit: authenticated Wix/version data and Catalogue Lab source/exports are unavailable. Current Wix guidance says existing-site catalogue migration is unavailable while also mentioning a banner, so dashboard/Wix support confirmation is required. V3 cannot downgrade; a published Studio branch cannot revert to Classic publication, and branches share business data.

Live Chromium navigation failed proxy-CA trust. Automatic approval review rejected persistent user trust-store modification; no TLS bypass was used. Live commerce, performance/accessibility and redirect checks remain unrun. No production site/catalogue updates, deployments, subscription changes, orders or payments occurred. This draft is for technical review, not migration or launch approval.
