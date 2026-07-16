"""Production site URLs, analytics, and third-party integration IDs."""

from __future__ import annotations

import os

# Primary domain (Cloudflare Pages)
PRODUCTION_BASE = "https://www.glavani-park.com"
# Legacy domain — redirect at DNS/CDN; emails stay on glavanipark.com
LEGACY_BASE = "https://www.glavanipark.com"

# Contact form — set FORMSPREE_FORM_ID in Cloudflare Pages environment variables
FORMSPREE_FORM_ID = os.environ.get("FORMSPREE_FORM_ID", "").strip()

# Analytics — optional; set in Cloudflare Pages env when ready
GA4_MEASUREMENT_ID = os.environ.get("GA4_MEASUREMENT_ID", "").strip()
GSC_VERIFICATION = os.environ.get("GSC_VERIFICATION", "").strip()
CLOUDFLARE_ANALYTICS_TOKEN = os.environ.get("CLOUDFLARE_ANALYTICS_TOKEN", "").strip()

CONTACT_SLUGS = {"en": "contact", "hr": "kontakt"}
PRIVACY_SLUGS = {"en": "privacy-policy", "hr": "pravila-privatnosti"}
COOKIE_SLUGS = {"en": "cookie-policy", "hr": "pravila-kolacica"}
TERMS_SLUGS = {"en": "terms-of-use", "hr": "uvjeti-koristenja"}
