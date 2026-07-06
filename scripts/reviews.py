"""Visitor reviews — TripAdvisor aggregate + reviews fetched at build time."""

from __future__ import annotations

import json
from pathlib import Path

GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Glavani+Park+Barban"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Attraction_Review-g1157701-d1973802-Reviews-Glavani_Park-Barban_Istria.html"
FACEBOOK_URL = "https://www.facebook.com/glavanipark"
SNAPSHOT_PATH = Path(__file__).resolve().parent / "reviews_snapshot.json"


def _load_snapshot() -> dict:
    if not SNAPSHOT_PATH.exists():
        raise FileNotFoundError(
            f"Missing {SNAPSHOT_PATH.name}. Run: python3 scripts/fetch_reviews.py"
        )
    return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))


def _stars_label(rating: int, lang: str) -> str:
    if lang == "hr":
        return f"{rating} od 5 zvjezdica"
    return f"{rating} out of 5 stars"


def _render_stars(rating: int) -> str:
    rating = max(1, min(5, int(rating)))
    return "★" * rating + "☆" * (5 - rating)


_SNAPSHOT: dict | None = None


def _snapshot() -> dict:
    global _SNAPSHOT
    if _SNAPSHOT is None:
        _SNAPSHOT = _load_snapshot()
    return _SNAPSHOT


def reset_cache() -> None:
    global _SNAPSHOT
    _SNAPSHOT = None


def aggregate_rating() -> dict:
    return _snapshot()["aggregate"]


def review_list() -> list[dict]:
    return _snapshot()["reviews"]

LABELS = {
    "en": {
        "heading": "What Visitors Say",
        "summary": (
            "{rating} on TripAdvisor · {count} reviews"
        ),
        "sample_note": "Latest reviews from TripAdvisor — read all {count} on TripAdvisor",
        "google": "Google",
        "tripadvisor": "TripAdvisor",
        "prev": "Previous review",
        "next": "Next review",
        "read_google": "More on Google",
        "read_tripadvisor": "All {count} reviews on TripAdvisor",
    },
    "hr": {
        "heading": "Što kažu posjetitelji",
        "summary": "{rating} na TripAdvisoru · {count} recenzija",
        "sample_note": "Najnovije recenzije s TripAdvisora — pročitajte svih {count} na TripAdvisoru",
        "google": "Google",
        "tripadvisor": "TripAdvisor",
        "prev": "Prethodna recenzija",
        "next": "Sljedeća recenzija",
        "read_google": "Više na Googleu",
        "read_tripadvisor": "Svih {count} recenzija na TripAdvisoru",
    },
}


def _format_review_date(date_str: str, lang: str) -> str:
    year, month, day = date_str.split("-")
    if lang == "hr":
        months = ["sij", "velj", "ožu", "tra", "svi", "lip", "srp", "kol", "ruj", "lis", "stu", "pro"]
        return f"{int(day)}. {months[int(month) - 1]} {year}."
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{months[int(month) - 1]} {day}, {year}"


def _source_badge(source: str, labels: dict) -> str:
    mod = "google" if source == "google" else "tripadvisor"
    name = labels["google"] if source == "google" else labels["tripadvisor"]
    return f'<span class="review-card__source review-card__source--{mod}">{name}</span>'


def render_reviews_section(lang: str) -> str:
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    aggregate = aggregate_rating()
    reviews = review_list()
    rating = aggregate["rating_value"]
    count = aggregate["rating_count"]
    summary = labels["summary"].format(rating=rating, count=count)
    sample_note = labels["sample_note"].format(count=count)
    tripadvisor_cta = labels["read_tripadvisor"].format(count=count)

    cards = []
    for review in reviews:
        when = _format_review_date(review["date"], lang)
        stars = _render_stars(review.get("rating", 5))
        stars_label = _stars_label(review.get("rating", 5), lang)
        cards.append(
            f"""<article class="review-card" data-review-author="{review['author']}" data-review-date="{review['date']}" data-review-rating="{review.get('rating', 5)}">
          {_source_badge(review["source"], labels)}
          <div class="review-card__stars" aria-label="{stars_label}">{stars}</div>
          <blockquote class="review-card__quote"><p>{review[quote_key]}</p></blockquote>
          <cite class="review-card__author">{review['author']} · {when}</cite>
        </article>"""
        )
    cards_html = "\n        ".join(cards)

    return f"""<section class="section section--wide section--theme-reviews" id="reviews" aria-labelledby="reviews-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="reviews-heading">{labels['heading']}</h2>
          <p class="reviews-summary"><strong>{summary}</strong></p>
          <p class="reviews-summary-note">{sample_note}</p>
        </div>
        <div class="reviews-carousel" data-reviews-carousel>
          <button type="button" class="reviews-carousel__nav reviews-carousel__nav--prev" aria-label="{labels['prev']}" data-reviews-prev>‹</button>
          <div class="reviews-carousel__track" tabindex="0" data-reviews-track>
            {cards_html}
          </div>
          <button type="button" class="reviews-carousel__nav reviews-carousel__nav--next" aria-label="{labels['next']}" data-reviews-next>›</button>
        </div>
        <p class="reviews-carousel__links">
          <a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer">{tripadvisor_cta}</a>
          <span aria-hidden="true">·</span>
          <a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener noreferrer">{labels['read_google']}</a>
        </p>
      </div>
    </section>"""


def render_review_badge(lang: str) -> str:
    """Compact TripAdvisor rating for hero areas."""
    aggregate = aggregate_rating()
    rating = aggregate["rating_value"]
    count = aggregate["rating_count"]
    if lang == "hr":
        text = f"{rating} na TripAdvisoru · {count} recenzija"
        label = "Ocjena na TripAdvisoru"
    else:
        text = f"{rating} on TripAdvisor · {count} reviews"
        label = "TripAdvisor rating"
    return (
        f'<p class="review-badge">'
        f'<span class="review-badge__stars" aria-hidden="true">★★★★★</span> '
        f'<a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="{label}"><strong>{text}</strong></a></p>'
    )


def render_review_teaser(lang: str) -> str:
    """Single featured review + rating for conversion points."""
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    aggregate = aggregate_rating()
    reviews = review_list()
    if not reviews:
        return ""
    review = reviews[0]
    rating = aggregate["rating_value"]
    count = aggregate["rating_count"]
    summary = labels["summary"].format(rating=rating, count=count)
    quote = review[quote_key]
    if len(quote) > 180:
        quote = quote[:177].rstrip() + "…"
    tripadvisor_cta = labels["read_tripadvisor"].format(count=count)
    if lang == "hr":
        heading = "Što kažu gosti"
    else:
        heading = "What guests say"
    return f"""<aside class="review-teaser" aria-label="{heading}">
      <p class="review-teaser__summary"><strong>{summary}</strong></p>
      <blockquote class="review-teaser__quote"><p>“{quote}”</p></blockquote>
      <cite class="review-teaser__author">{review['author']}</cite>
      <p class="review-teaser__link"><a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer">{tripadvisor_cta}</a></p>
    </aside>"""
