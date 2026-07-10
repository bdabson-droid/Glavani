"""Visitor reviews — TripAdvisor aggregate + reviews fetched at build time."""

from __future__ import annotations

import json
from pathlib import Path

GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Glavani+Park+Barban"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Attraction_Review-g1157701-d1973802-Reviews-Glavani_Park-Barban_Istria.html"
FACEBOOK_URL = "https://www.facebook.com/glavanipark"
GOOGLE_RATING_VALUE = 4.8
GOOGLE_REVIEW_COUNT = {"en": "900+ reviews", "hr": "900+ recenzija"}
SNAPSHOT_PATH = Path(__file__).resolve().parent / "reviews_snapshot.json"


def _load_snapshot() -> dict:
    if not SNAPSHOT_PATH.exists():
        raise FileNotFoundError(
            f"Missing {SNAPSHOT_PATH.name}. Run: python3 scripts/fetch_reviews.py"
        )
    return json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))


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


def render_google_review_badge(lang: str) -> str:
    """Compact Google rating for hero areas."""
    if lang == "hr":
        text = f"{GOOGLE_RATING_VALUE} na Googleu · {GOOGLE_REVIEW_COUNT['hr']}"
        label = "Ocjena na Googleu"
    else:
        text = f"{GOOGLE_RATING_VALUE} on Google · {GOOGLE_REVIEW_COUNT['en']}"
        label = "Google rating"
    return (
        f'<p class="review-badge review-badge--google">'
        f'<span class="review-badge__stars" aria-hidden="true">★★★★★</span> '
        f'<a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener noreferrer" '
        f'aria-label="{label}"><strong>{text}</strong></a></p>'
    )


def render_hero_review_badges(lang: str) -> str:
    return (
        f'<div class="hero__review-badges">'
        f"{render_google_review_badge(lang)}"
        f"{render_review_badge(lang)}"
        f"</div>"
    )
