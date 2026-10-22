const fs = require('node:fs');
const { test, expect } = require('@playwright/test');

// With no manifest this exercises the harness against synthetic HTML only.
// Live selectors and expectations must come from inspected Wix pages.
const live = Boolean(process.env.LSD_QA_MANIFEST);
const fixture = {
  url: 'https://fixture.invalid/brand', title: 'Fixture Brand',
  canonical: 'https://fixture.invalid/brand', description: 'Synthetic catalogue category',
  heading: 'Fixture Brand', productSelector: '[data-product]',
  productLinkSelector: '[data-product] a', minProducts: 1,
};
const target = live ? JSON.parse(fs.readFileSync(process.env.LSD_QA_MANIFEST, 'utf8')) : fixture;
for (const name of Object.keys(fixture)) {
  if (target[name] === undefined || target[name] === '') throw new Error(`Manifest requires ${name}`);
}
const targetUrl = new URL(target.url);
if (targetUrl.protocol !== 'https:' || targetUrl.username || targetUrl.password) throw new Error('HTTPS without credentials required');
if (!Number.isInteger(target.minProducts) || target.minProducts < 1) throw new Error('Use a representative nonempty category');

test.beforeEach(async ({ page, context }) => {
  await context.route('**/*', async route => {
    const request = route.request();
    // No cart/checkout/form mutations. Some Wix rendering uses POST for queries;
    // failures must be reviewed, not worked around by allowing all writes.
    if (!['GET', 'HEAD'].includes(request.method())) return route.abort('blockedbyclient');
    if (!live) {
      if (request.url() !== fixture.url) return route.abort();
      return route.fulfill({ contentType: 'text/html', body: `<!doctype html><html lang="en"><head>
        <title>Fixture Brand</title><meta name="description" content="Synthetic catalogue category">
        <link rel="canonical" href="https://fixture.invalid/brand"><meta name="viewport" content="width=device-width">
        </head><body><nav aria-label="Main"><a href="/">Home</a></nav><main>
        <h1>Fixture Brand</h1><section aria-label="Products"><article data-product>
        <a href="/product/fixture">Fixture shampoo</a><p>CAD $12.50</p>
        </article></section></main></body></html>` });
    }
    return route.continue();
  });
  const response = await page.goto(target.url, { waitUntil: 'domcontentloaded' });
  expect(response.status()).toBe(200);
});

test(`${live ? 'target' : 'synthetic harness'}: SEO and category content`, async ({ page }) => {
  await expect(page).toHaveTitle(target.title);
  await expect(page.locator('link[rel="canonical"]')).toHaveCount(1);
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', target.canonical);
  await expect(page.locator('meta[name="description"]')).toHaveAttribute('content', target.description);
  await expect(page.getByRole('heading', { name: target.heading, exact: true })).toBeVisible();
  await expect.poll(() => page.locator(target.productSelector).count()).toBeGreaterThanOrEqual(target.minProducts);
});

test(`${live ? 'target' : 'synthetic harness'}: responsive URL shape and product keyboard focus`, async ({ page }) => {
  const links = page.locator(target.productLinkSelector);
  await expect(links.first()).toBeVisible();
  expect(await links.count()).toBeGreaterThan(0);
  for (const href of await links.evaluateAll(nodes => nodes.map(n => n.href))) {
    const url = new URL(href);
    expect(url.protocol).toBe('https:');
    expect(url.origin).toBe(targetUrl.origin);
  }
  await expect.poll(() => page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBe(true);
  let productFocused = false;
  for (let tab = 0; tab < 100; tab++) {
    await page.keyboard.press('Tab');
    productFocused = await links.evaluateAll(nodes => nodes.includes(document.activeElement));
    if (productFocused) break;
  }
  expect(productFocused).toBe(true);
});
