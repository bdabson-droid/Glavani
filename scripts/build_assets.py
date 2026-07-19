"""Minify static assets and generate Cloudflare Pages _headers."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def minify_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{}:;,>+~])\s*", r"\1", css)
    return css.strip()


def minify_js(js: str) -> str:
    js = re.sub(r"/\*[\s\S]*?\*/", "", js)
    js = re.sub(r"(^|[^:])//.*$", r"\1", js, flags=re.M)
    js = re.sub(r"\n\s*\n", "\n", js)
    return js.strip()


def build_minified_assets() -> None:
    css_src = ROOT / "assets" / "css" / "site.css"
    css_dst = ROOT / "assets" / "css" / "site.min.css"
    css_dst.write_text(minify_css(css_src.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"  asset: {css_dst.relative_to(ROOT)}")

    js_dir = ROOT / "assets" / "js"
    for src in js_dir.glob("*.js"):
        if src.name.endswith(".min.js"):
            continue
        dst = src.with_suffix(".min.js")
        dst.write_text(minify_js(src.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"  asset: {dst.relative_to(ROOT)}")


def build_headers() -> None:
    content = """# Cloudflare Pages — security and cache headers
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Content-Security-Policy: default-src 'self'; base-uri 'self'; form-action 'self'; script-src 'self' 'unsafe-inline' https://unpkg.com https://static.cloudflareinsights.com https://www.googletagmanager.com https://challenges.cloudflare.com; style-src 'self' 'unsafe-inline' https://unpkg.com; img-src 'self' data: https:; font-src 'self'; connect-src 'self' https://api.resend.com https://cloudflareinsights.com https://www.google-analytics.com; frame-src https://www.google.com https://www.youtube.com; object-src 'none'

/assets/css/*
  Cache-Control: public, max-age=86400, must-revalidate

/assets/js/*
  Cache-Control: public, max-age=31536000, immutable

/images/*
  Cache-Control: public, max-age=31536000, immutable
"""
    (ROOT / "_headers").write_text(content, encoding="utf-8")
    print("  page: _headers")
