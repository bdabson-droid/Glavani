# Glavani Park — Cloudflare Pages deployment checklist

Production domain: **https://glavani-park.com**

## 1. Connect repository

1. Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. Select this repository and branch `main`
3. Use the settings below (do **not** use a subdirectory as the build output)

## 2. Build settings

| Setting | Value |
|---------|--------|
| **Build command** | `npm install && pip install pillow && SITE_BASE=https://glavani-park.com python3 scripts/build_site.py` |
| **Build output directory** | `/` (repository root) |
| **Root directory** | `/` |

The build emits static HTML into `en/`, `hr/`, and the repo root, plus `functions/` for form handling.

## 3. Environment variables (Production)

| Variable | Required | Purpose |
|----------|----------|---------|
| `RESEND_API_KEY` | **Yes** (forms) | Sends contact + booking emails via Resend |
| `SITE_BASE` | Recommended | `https://glavani-park.com` — canonical URLs in sitemap/schema |
| `GA4_MEASUREMENT_ID` | Optional | Google Analytics 4 (loads after cookie consent) |
| `GSC_VERIFICATION` | Optional | Google Search Console HTML verification meta tag |
| `CLOUDFLARE_ANALYTICS_TOKEN` | Optional | Cloudflare Web Analytics beacon |

## 4. Custom domain & DNS

1. Pages project → **Custom domains** → add `glavani-park.com` and `www.glavani-park.com`
2. Set **glavani-park.com** as the primary/canonical hostname
3. `_redirects` in the repo 301-redirects `www` and legacy `glavanipark.com` hosts to `https://glavani-park.com`

### DNS records (at your registrar or Cloudflare DNS)

- `glavani-park.com` → CNAME to `<project>.pages.dev` (proxied)
- `www` → CNAME to `<project>.pages.dev` (proxied) — redirected to apex by `_redirects`

## 5. Resend (email delivery)

1. Create a Resend account and verify domain **glavanipark.com**
2. Add sender `info@glavanipark.com` (used as the From address in `functions/_middleware.ts`)
3. Paste the API key into Cloudflare Pages → **Settings** → **Environment variables** as `RESEND_API_KEY`
4. Test contact (`/en/contact/`) and booking (`/en/reservation/`) forms after deploy

## 6. Post-deploy verification

Run locally after build:

```bash
SITE_BASE=https://glavani-park.com python3 scripts/build_site.py
python3 scripts/verify_site.py
```

After deploy, manually check:

- [ ] https://glavani-park.com/ redirects to `/hr/`
- [ ] https://www.glavani-park.com/ → 301 → `https://glavani-park.com/`
- [ ] https://www.glavanipark.com/en/human_catapult → 301 → new activity URL
- [ ] `/robots.txt` and `/sitemap.xml` load with `glavani-park.com` URLs
- [ ] Contact and booking forms return success JSON
- [ ] Lighthouse (mobile): Performance, Accessibility, Best Practices ≥ 95; SEO 100

## 7. Search & analytics

1. **Google Search Console** — add property `https://glavani-park.com`, verify via `GSC_VERIFICATION` env var or DNS
2. Submit `https://glavani-park.com/sitemap.xml`
3. Enable **GA4** or **Cloudflare Web Analytics** when ready (cookie banner appears automatically)

## 8. What stays on glavanipark.com (intentional)

- Email address: `info@glavanipark.com`
- Build-time image sources from the legacy CMS (downloaded at build, not served live)
- CMS path redirects in `_redirects` and `404.html` for old bookmarked URLs

## 9. GitHub Actions

Workflow `.github/workflows/pages.yml` builds and verifies on every push to `main`. Cloudflare Pages performs the live deploy when connected to Git; the workflow artifact is for CI validation only.

## 10. Troubleshooting

| Issue | Fix |
|-------|-----|
| Forms return 500 | Set `RESEND_API_KEY`; verify Resend domain/sender |
| Wrong canonical URLs | Set `SITE_BASE=https://glavani-park.com` in Cloudflare env |
| Old CMS URLs 404 | Ensure `_redirects` deployed (Cloudflare Pages, not plain static hosting without redirects) |
| Build fails on images | Legacy `glavanipark.com` must be reachable during build, or commit images to repo |
