#!/usr/bin/env python3
"""Post-build checks: links, images, legacy hosting references, SEO basics."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

BAD_HTML_PATTERNS = [
    (re.compile(r"formspree\.io", re.I), "Formspree reference"),
    (re.compile(r"preview-banner"), "Preview banner"),
    (re.compile(r"preview-booking-guard"), "Preview booking guard"),
    (re.compile(r"https?://www\.glavanipark\.com", re.I), "Legacy web domain in HTML"),
    (re.compile(r"https?://www\.glavani-park\.com", re.I), "www canonical domain in HTML"),
]

REQUIRED_ROOT_FILES = [
    "index.html",
    "404.html",
    "robots.txt",
    "sitemap.xml",
    "_redirects",
    "_headers",
    "functions/_middleware.ts",
    "package.json",
]


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.images: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        src = attr.get("href") or attr.get("src")
        if not src:
            return
        if tag == "a" and attr.get("href"):
            self.links.append((attr["href"], "href"))
        elif tag in ("img", "script", "link") and attr.get("src"):
            self.images.append((attr["src"], "src"))
        elif tag == "link" and attr.get("href"):
            self.images.append((attr["href"], "href"))


def resolve_path(page: Path, target: str) -> Path | None:
    if target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
        return None
    path_part = target.split("#", 1)[0].split("?", 1)[0]
    if not path_part or path_part == "#":
        return None
    if path_part.startswith("/"):
        return ROOT / path_part.lstrip("/")
    return (page.parent / path_part).resolve()


def iter_html_files() -> list[Path]:
    files = [ROOT / "index.html", ROOT / "404.html"]
    files.extend((ROOT / "en").rglob("index.html"))
    files.extend((ROOT / "hr").rglob("index.html"))
    return sorted(files)


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_ROOT_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required file: {rel}")

    html_files = iter_html_files()
    if len(html_files) < 50:
        errors.append(f"Expected 50+ HTML pages, found {len(html_files)}")

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        is_root_redirect = rel == Path("index.html")
        for pattern, label in BAD_HTML_PATTERNS:
            if pattern.search(text):
                errors.append(f"{rel}: {label}")
        if "<title>" not in text or 'meta name="description"' not in text:
            errors.append(f"{rel}: missing title or meta description")
        if 'rel="canonical"' not in text:
            errors.append(f"{rel}: missing canonical URL")
        if 'property="og:title"' not in text or 'name="twitter:card"' not in text:
            if not is_root_redirect:
                errors.append(f"{rel}: missing Open Graph or Twitter tags")

        parser = LinkParser()
        parser.feed(text)
        for target, kind in parser.links + parser.images:
            resolved = resolve_path(path, target)
            if resolved is None:
                continue
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue
            if kind in ("src", "href") and not resolved.exists():
                errors.append(f"{rel}: broken {kind} → {target}")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if "https://glavani-park.com" not in sitemap:
        errors.append("sitemap.xml: missing glavani-park.com URLs")
    if "glavanipark.com" in sitemap:
        errors.append("sitemap.xml: contains legacy glavanipark.com")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "Sitemap: https://glavani-park.com/sitemap.xml" not in robots:
        errors.append("robots.txt: wrong sitemap URL")

    if errors:
        print("Site verification failed:")
        for err in errors[:40]:
            print(f"  - {err}")
        if len(errors) > 40:
            print(f"  ... and {len(errors) - 40} more")
        return 1

    print(f"Site verification passed ({len(html_files)} HTML files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
