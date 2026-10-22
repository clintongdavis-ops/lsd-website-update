"""Bounded, same-origin, read-only discovery. Standard library only.

Not a Wix export adapter. Never submits forms or authenticates to Wix.
"""
import argparse
import csv
import ipaddress
import json
import socket
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

MAX_BYTES = 8_000_000


def origin(url):
    p = urllib.parse.urlsplit(url)
    if p.scheme != "https" or not p.hostname or p.username or p.password or p.port not in (None, 443):
        raise ValueError("Use a public HTTPS origin without credentials or a custom port")
    return "https://" + p.hostname.lower()


def public_host(host):
    if host == "localhost" or host.endswith((".localhost", ".local", ".internal")):
        raise ValueError("Local network destinations are not supported")
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        address = None
    if address is not None:
        if not address.is_global:
            raise ValueError("Private/local network destinations are not supported")
        return
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?", host) or "." not in host:
        raise ValueError("A public DNS hostname is required")
    # The cloud egress proxy resolves names. Local DNS may intentionally be unavailable.
    # Respect that route; its network policy governs resolved destinations.
    if urllib.request.getproxies().get("https"):
        return
    addresses = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError("Private/local network destinations are not supported")


class SameOriginRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self, allowed_origin):
        self.allowed_origin = allowed_origin

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if origin(newurl) != self.allowed_origin:
            raise ValueError("Cross-origin redirect refused: " + newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


class Reader:
    def __init__(self, base):
        self.base = origin(base)
        public_host(urllib.parse.urlsplit(self.base).hostname)
        self.opener = urllib.request.build_opener(SameOriginRedirect(self.base))

    def get(self, url):
        if origin(url) != self.base:
            raise ValueError("Cross-origin request refused")
        req = urllib.request.Request(url, headers={"User-Agent": "LSD-Migration-Audit/0.1 (read-only)"})
        with self.opener.open(req, timeout=30) as response:
            data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError("Response exceeds size limit")
            headers = {key: ", ".join(response.headers.get_all(key)) for key in response.headers.keys()}
            return response.status, response.url, data.decode("utf-8", errors="replace"), headers


def sitemap_entries(xml):
    root = ET.fromstring(xml)
    kind = root.tag.rsplit("}", 1)[-1]
    if kind not in ("sitemapindex", "urlset"):
        raise ValueError("Expected sitemapindex or urlset")
    entries = []
    for child in root:
        for field in child:
            if field.tag.rsplit("}", 1)[-1] == "loc" and field.text:
                entries.append(field.text.strip())
    return kind, entries


def inventory(reader, limit=10000, max_sitemaps=100):
    queue, seen, urls, errors = [reader.base + "/sitemap.xml"], set(), set(), []
    truncated = False
    while queue:
        if len(seen) >= max_sitemaps:
            truncated = True
            break
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            _, _, xml, _ = reader.get(url)
            kind, entries = sitemap_entries(xml)
            for entry in entries:
                if origin(entry) != reader.base:
                    raise ValueError("Cross-origin sitemap entry refused")
                if kind == "sitemapindex":
                    if entry not in seen and entry not in queue:
                        queue.append(entry)
                else:
                    urls.add(entry)
                    if len(urls) > limit:
                        truncated = True
                        urls.remove(entry)
                        break
        except (ValueError, OSError, ET.ParseError) as exc:
            errors.append({"url": url, "error": str(exc)})
        if truncated:
            break
        time.sleep(0.1)
    return {"origin": reader.base, "source": "public sitemap (not full site or catalogue export)",
            "sitemaps": sorted(seen), "urls": sorted(urls), "errors": errors,
            "truncated": truncated, "complete": not errors and not truncated and bool(urls)}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.canonicals, self.links, self.hreflang = [], [], []
        self.description, self.robots = "", ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "link":
            rel = a.get("rel", "").lower().split()
            if "canonical" in rel:
                self.canonicals.append(a.get("href", ""))
            if "alternate" in rel and a.get("hreflang"):
                self.hreflang.append({"language": a["hreflang"], "url": a.get("href", "")})
        if tag == "meta":
            name = a.get("name", "").lower()
            if name == "description":
                self.description = a.get("content", "")
            if name == "robots":
                self.robots = a.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def audit_page(reader, url):
    status, final, html, headers = reader.get(url)
    page = Page()
    page.feed(html)
    issues = []
    if not page.title.strip():
        issues.append("missing-title")
    if not page.description.strip():
        issues.append("missing-description")
    if len(page.canonicals) != 1:
        issues.append("expected-one-canonical")
    elif page.canonicals[0] != final:
        issues.append("canonical-differs-review-required")
    header_robots = ", ".join(value for key, value in headers.items() if key.lower() == "x-robots-tag")
    directives = set(re.split(r"[\s,;:]+", (page.robots + ", " + header_robots).lower()))
    if directives & {"noindex", "none"}:
        issues.append("noindex-review-required")
    return {"url": url, "final_url": final, "status": status, "title": page.title.strip(),
            "description": page.description, "canonicals": page.canonicals,
            "robots": page.robots, "x_robots_tag": header_robots, "hreflang": page.hreflang,
            "internal_links": sorted({urllib.parse.urljoin(final, x).split("#")[0]
                for x in page.links if urllib.parse.urljoin(final, x).startswith(reader.base + "/")}),
            "issues": issues}


def check_links(reader, url, max_links=100):
    source = audit_page(reader, url)
    links = source["internal_links"]
    results = []
    for link in links[:max_links]:
        try:
            status, final, _, _ = reader.get(link)
            results.append({"url": link, "status": status, "final_url": final})
        except (OSError, ValueError) as exc:
            results.append({"url": link, "error": str(exc)})
        time.sleep(0.1)
    complete = bool(links) and len(links) <= max_links
    return {"source_url": url, "discovered_internal_links": len(links), "checked": len(results),
            "complete_for_source_html": complete, "results": results,
            "passed": complete and all(x.get("status") == 200 for x in results),
            "scope": "Server-HTML internal links only; not a site-wide crawl or content-identity test"}


def redirect_map_errors(rows):
    errors, mapping = [], {}
    for row in rows:
        old, new = row.get("old_url", ""), row.get("new_url", "")
        try:
            origin(old)
            origin(new)
        except ValueError as exc:
            errors.append(str(exc))
        if old in mapping:
            errors.append("duplicate source: " + old)
        if old == new:
            errors.append("self redirect: " + old)
        if row.get("status") != "301":
            errors.append("expected proposed 301: " + old)
        mapping[old] = new
    for source, target in mapping.items():
        if target in mapping:
            errors.append("chain or cycle: " + source)
    return sorted(set(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    inv = sub.add_parser("inventory")
    inv.add_argument("origin")
    inv.add_argument("--limit", type=int, default=10000)
    inv.add_argument("--max-sitemaps", type=int, default=100)
    page = sub.add_parser("page")
    page.add_argument("url")
    links = sub.add_parser("links")
    links.add_argument("url")
    links.add_argument("--max-links", type=int, default=100)
    redirects = sub.add_parser("redirects")
    redirects.add_argument("csv", help="Columns: old_url,new_url,status; validates proposals only")
    args = parser.parse_args()
    try:
        if args.command == "inventory":
            if args.limit < 1 or args.max_sitemaps < 1:
                raise ValueError("Limits must be positive")
            result = inventory(Reader(args.origin), args.limit, args.max_sitemaps)
            ok = result["complete"]
        elif args.command == "page":
            result = audit_page(Reader(args.url), args.url)
            ok = not result["issues"]
        elif args.command == "links":
            if args.max_links < 1:
                raise ValueError("max-links must be positive")
            result = check_links(Reader(args.url), args.url, args.max_links)
            ok = result["passed"]
        else:
            with Path(args.csv).open(newline="") as handle:
                rows = list(csv.DictReader(handle))
            errors = redirect_map_errors(rows)
            result = {"rows": len(rows), "errors": errors, "production_changes": False}
            ok = bool(rows) and not errors
        print(json.dumps(result, indent=2))
        return 0 if ok else 1
    except (ValueError, OSError, ET.ParseError) as exc:
        print(json.dumps({"error": str(exc), "complete": False}, indent=2))
        return 2


if __name__ == "__main__":
    sys.exit(main())
