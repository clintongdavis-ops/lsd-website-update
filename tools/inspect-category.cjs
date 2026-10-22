// Read-only AG Hair baseline; observations are not full site acceptance tests.
const { chromium, devices } = require('@playwright/test');
const fs = require('node:fs');
const url = 'https://www.lesalondieppe.com/shop-aghair';

async function main() {
  fs.mkdirSync('artifacts', { recursive: true });
  const runId = new Date().toISOString();
  const screenshotDirectory = `artifacts/category-${runId.replaceAll(':', '-')}`;
  fs.mkdirSync(screenshotDirectory);
  const report = { runId, observedAt: runId, url, browserVersion: null, complete: false,
    scope: 'Public unauthenticated observations; non-GET/HEAD HTTP and WebSockets blocked; not commerce, performance or accessibility acceptance',
    profiles: [] };
  const save = () => fs.writeFileSync('artifacts/live-browser-discovery.json', JSON.stringify(report, null, 2) + '\n');
  save(); // Invalidate previous success even if launch or a later profile fails.
  let browser;
  try {
    browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/usr/bin/chromium' });
    report.browserVersion = browser.version();
    const profiles = [
      { name: 'desktop', options: { viewport: { width: 1440, height: 900 } } },
      { name: 'mobile', options: { ...devices['Pixel 7'], viewport: { width: 390, height: 844 } } },
    ];
    for (const profile of profiles) {
      const context = await browser.newContext({ ...profile.options, serviceWorkers: 'block' });
      try {
        let blockedNonReadRequests = 0;
        let blockedWebSockets = 0;
        const failedHosts = new Set();
        await context.routeWebSocket('**/*', socket => { blockedWebSockets++; socket.close(); });
        await context.route('**/*', route => {
          if (['GET', 'HEAD'].includes(route.request().method())) return route.continue();
          blockedNonReadRequests++;
          return route.abort('blockedbyclient');
        });
        const page = await context.newPage();
        page.on('requestfailed', request => {
          try { failedHosts.add(new URL(request.url()).host); } catch { /* no raw URL logging */ }
        });
        const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
        if (response?.status() !== 200) throw new Error(`${profile.name}: expected HTTP 200`);
        const products = page.locator('[data-hook="product-list-grid-item"]');
        await products.first().waitFor({ state: 'visible', timeout: 30000 });
        const links = products.locator('a[href^="https://www.lesalondieppe.com/product-page/"]');
        let productFocused = false;
        for (let tab = 0; tab < 100; tab++) {
          await page.keyboard.press('Tab');
          productFocused = await links.evaluateAll(nodes => nodes.includes(document.activeElement));
          if (productFocused) break;
        }
        // Return to the page top before capturing the representative viewport.
        await page.evaluate(() => scrollTo(0, 0));
        const geometry = await page.evaluate(() => ({
          innerWidth, scrollWidth: document.documentElement.scrollWidth,
          hasHorizontalOverflow: document.documentElement.scrollWidth > innerWidth + 1,
        }));
        const issues = [];
        if (geometry.hasHorizontalOverflow) issues.push('horizontal-overflow');
        if (!productFocused) issues.push('product-link-not-focused-within-100-tabs');
        if (await page.locator('h1').count() === 0) issues.push('no-h1-observed');
        const screenshot = `${screenshotDirectory}/${profile.name}.png`;
        await page.screenshot({ path: screenshot });
        report.profiles.push({ profile: profile.name, viewport: profile.options.viewport,
          userAgent: await page.evaluate(() => navigator.userAgent), status: response.status(),
          title: await page.title(), headings: await page.locator('h1,h2,h3').allTextContents(),
          renderedProducts: await products.count(), firstProductVisible: await products.first().isVisible(),
          productFocusedWithin100Tabs: productFocused, geometry, issues,
          blockedNonReadRequests, blockedWebSockets, failedHosts: [...failedHosts].sort(), screenshot });
        save();
      } finally { await context.close(); }
    }
    report.complete = true;
    save();
    console.log(JSON.stringify(report, null, 2));
    // Issue observations require review; exit 1 is not necessarily an application defect.
    return report.profiles.some(result => result.issues.length) ? 1 : 0;
  } catch (error) {
    report.error = error.message;
    save();
    throw error;
  } finally { if (browser) await browser.close(); }
}
main().then(code => { process.exitCode = code; }).catch(error => {
  console.error(error.message);
  process.exitCode = 2;
});
