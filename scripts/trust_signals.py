"""Trust badges, awards, and social proof for conversion surfaces."""

from __future__ import annotations

from reviews import GOOGLE_REVIEWS_URL, TRIPADVISOR_URL, aggregate_rating

LABELS = {
    "en": {
        "tripadvisor": "TripAdvisor",
        "google": "Google",
        "reviews": "reviews",
        "read_google": "Read on Google",
        "read_tripadvisor": "Read on TripAdvisor",
        "award": "Certificate of Excellence",
        "award_years": "TripAdvisor · 2017 & 2018",
        "visitors": "Thousands of visitors every season",
        "since": "Family-run since 2012",
        "largest": "Croatia's largest adventure park",
        "ce": "CE-certified equipment",
        "media": "As featured in",
        "kroatide": "Kroatide travel guide",
        "pitchup": "Pitchup.com partner",
    },
    "hr": {
        "tripadvisor": "TripAdvisor",
        "google": "Google",
        "reviews": "recenzija",
        "read_google": "Pročitajte na Googleu",
        "read_tripadvisor": "Pročitajte na TripAdvisoru",
        "award": "Certificate of Excellence",
        "award_years": "TripAdvisor · 2017. i 2018.",
        "visitors": "Tisuće posjetitelja svake sezone",
        "since": "Obiteljski park od 2012.",
        "largest": "Najveći avanturistički park u Hrvatskoj",
        "ce": "CE certificirana oprema",
        "media": "Preporučeno u",
        "kroatide": "Kroatide vodič",
        "pitchup": "Pitchup.com partner",
    },
}


def book_cta_labels(lang: str) -> dict[str, str]:
    if lang == "hr":
        return {
            "book_tickets": "Rezervirajte ulaznice",
            "visit_today": "Posjetite danas — nazovite za dostupnost",
            "book_now": "Rezervirajte odmah",
            "book": "Rezerviraj",
        }
    return {
        "book_tickets": "Book Tickets",
        "visit_today": "Visit Today - Call For Availability",
        "book_now": "Book Now",
        "book": "Book",
    }


def render_trust_strip(lang: str, *, in_footer: bool = False) -> str:
    labels = LABELS[lang]
    aggregate = aggregate_rating()
    rating = aggregate["rating_value"]
    count = aggregate["rating_count"]
    if lang == "hr":
        ta_line = f"<strong>{rating}</strong> na TripAdvisoru · {count} {labels['reviews']}"
        aria = "Znakovi povjerenja i nagrade"
    else:
        ta_line = f"<strong>{rating}</strong> on TripAdvisor · {count} {labels['reviews']}"
        aria = "Trust signals and awards"
    modifier = " trust-strip--footer" if in_footer else ""
    return f"""<div class="trust-strip{modifier}" aria-label="{aria}">
      <ul class="trust-strip__list">
        <li class="trust-strip__item trust-strip__item--tripadvisor">
          <a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer">
            <span class="trust-strip__stars" aria-hidden="true">★★★★★</span>
            <span>{ta_line}</span>
          </a>
        </li>
        <li class="trust-strip__item trust-strip__item--google">
          <a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener noreferrer">
            <span class="trust-strip__icon" aria-hidden="true">G</span>
            <span>{labels['read_google']}</span>
          </a>
        </li>
        <li class="trust-strip__item trust-strip__item--award">
          <img src="/images/tripadvisor-certificate-excellence.webp" alt="{labels['award']}" width="80" height="80" loading="lazy">
          <span>{labels['award_years']}</span>
        </li>
        <li class="trust-strip__item trust-strip__item--stat">
          <span class="trust-strip__icon" aria-hidden="true">👥</span>
          <span>{labels['visitors']}</span>
        </li>
        <li class="trust-strip__item trust-strip__item--stat">
          <span class="trust-strip__icon" aria-hidden="true">🛡️</span>
          <span>{labels['ce']}</span>
        </li>
        <li class="trust-strip__item trust-strip__item--media">
          <span class="trust-strip__media-label">{labels['media']}</span>
          <span class="trust-strip__logos">
            <img src="/images/kroatide-travel-guide.webp" alt="{labels['kroatide']}" width="72" height="28" loading="lazy">
            <img src="/images/pitchup-partner.webp" alt="{labels['pitchup']}" width="72" height="28" loading="lazy">
          </span>
        </li>
      </ul>
    </div>"""
