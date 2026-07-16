# Glavani Park — Cloudflare Pages deployment checklist

Production domain: **https://glavani-park.com**

## 1. Connect repository

**Important:** Create a **Pages** project, not a **Workers** project.

1. Cloudflare Dashboard → **Workers & Pages** → **Create** → select the **Pages** tab → **Connect to Git**
2. Select this repository and branch `main`
3. Use the settings below (do **not** use a subdirectory as the build output)

If your project only shows **Build command** + **Deploy command** (both required) and defaults to `npx wrangler deploy`, you created a **Workers** project by mistake. Delete it and recreate using the **Pages** tab above.

## 2. Build settings

### Option A — Cloudflare Pages (recommended)

| Setting | Value |
|---------|--------|
| **Build command** | `npm install && pip install pillow && SITE_BASE=https://glavani-park.com python3 scripts/build_site.py` |
| **Build output directory** | `/` (repository root) |
| **Root directory** | `/` |
| **Deploy command** | *(none — field not shown on Pages)* |

The build emits static HTML into `en/`, `hr/`, and the repo root, plus `functions/` for form handling. Pages publishes automatically after a successful build.

### Option B — Workers Builds (if Deploy command is required)

Some accounts only offer **Workers** Git integration, which **requires** a deploy command. Do **not** use `npx wrangler deploy` — that uploads the whole repo as a Worker and fails with **Asset too large**.

| Setting | Value |
|---------|--------|
| **Build command** | `npm install && pip install pillow && SITE_BASE=https://glavani-park.com python3 scripts/build_site.py` |
| **Deploy command** | `npx wrangler pages deploy . --project-name=glavaniparkwebsite` |

Replace `glavaniparkwebsite` with your Pages project name. This deploys as **Pages** (respects `functions/` for forms, ignores `node_modules`). You may need to create the Pages project first: **Workers & Pages** → **Create** → **Pages** → **Upload assets** (create empty project), then connect Git or use the deploy command above.

**Do not** use `npx wrangler deploy` for this site.

## 3. Environment variables (Production)

| Variable | Required | Purpose |
|----------|----------|---------|
| `RESEND_API_KEY` | **Yes** (forms) | Sends contact + booking emails via Resend |
| `SITE_BASE` | Recommended | `https://glavani-park.com` — canonical URLs in sitemap/schema |
| `GA4_MEASUREMENT_ID` | Optional | Google Analytics 4 (loads after cookie consent) |
| `GSC_VERIFICATION` | Optional | Google Search Console HTML verification meta tag |
| `CLOUDFLARE_ANALYTICS_TOKEN` | Optional | Cloudflare Web Analytics beacon |

## 4. Custom domain, DNS & redirects

Cloudflare Pages `_redirects` only handles **path-based** rules. **Domain-level** redirects (www → apex, apex trailing slash) use **Bulk Redirects** — Cloudflare’s recommended approach.

### 4a. Import Bulk Redirects (required once)

1. Cloudflare Dashboard → **Rules** → **Bulk Redirects** → **Create Bulk Redirect List**
2. Import `cloudflare-bulk-redirects.csv` from this repository
3. Create a **Bulk Redirect Rule** that applies the list
4. Verify with: `curl -I https://www.glavani-park.com/` → `Location: https://glavani-park.com/...`

| Source | Target | Purpose |
|--------|--------|---------|
| `www.glavani-park.com` | `https://glavani-park.com` | www → apex (subpath + query preserved) |
| `glavani-park.com` | `https://glavani-park.com/` | Enforce HTTPS + trailing slash on apex |
| `www.glavanipark.com` / `glavanipark.com` | `https://glavani-park.com` | Legacy domain → new apex |

Also enable **SSL/TLS → Always Use HTTPS** for the zone.

### 4b. Custom domains & DNS

1. Pages project → **Custom domains** → add `glavani-park.com` and `www.glavani-park.com`
2. Set **glavani-park.com** as the primary/canonical hostname
3. `_redirects` in the repo handles CMS path migrations (e.g. `/en/human_catapult` → `/en/human-catapult/`)

### DNS records (at your registrar or Cloudflare DNS)

- `glavani-park.com` → CNAME to `<project>.pages.dev` (proxied)
- `www` → CNAME to `<project>.pages.dev` (proxied) — redirected to apex by Bulk Redirects

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
| **Can't leave Deploy command empty** | You have a **Workers** project, not **Pages**. Recreate via **Create → Pages** tab, or set deploy to `npx wrangler pages deploy . --project-name=glavaniparkwebsite` (see Option B above). |
| **Deploy fails: `Asset too large` / `workerd` 122 MiB** | Replace `npx wrangler deploy` with `npx wrangler pages deploy . --project-name=glavaniparkwebsite`, or switch to a Pages project (Option A). |
| **Wrangler asks “Cloudflare Pages deployment?” then fails** | Same as above — use `wrangler pages deploy`, not `wrangler deploy`. |
| Forms return 500 | Set `RESEND_API_KEY`; verify Resend domain/sender |
| Wrong canonical URLs | Set `SITE_BASE=https://glavani-park.com` in Cloudflare env |
| Old CMS URLs 404 | Ensure `_redirects` deployed (Cloudflare Pages, not plain static hosting without redirects) |
| Build fails on images | Legacy `glavanipark.com` must be reachable during build, or commit images to repo |
