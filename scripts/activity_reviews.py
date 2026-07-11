"""Match TripAdvisor and Google reviews to specific activities by keyword."""

from __future__ import annotations

from google_reviews_data import google_review_list
from reviews import (
    GOOGLE_RATING_VALUE,
    GOOGLE_REVIEWS_URL,
    GOOGLE_REVIEW_COUNT,
    TRIPADVISOR_URL,
    aggregate_rating,
    review_list,
)

# Keywords searched in both EN and HR review text (case-insensitive).
ACTIVITY_REVIEW_KEYWORDS: dict[str, list[str]] = {
    "human-catapult": [
        "catapult",
        "human catapult",
        "katapult",
        "ljudska katapult",
        "obstacles",
    ],
    "high-swing": [
        "swing",
        "giant swing",
        "3g swing",
        "ljulja",
        "visoka ljulja",
        "12 meter",
        "12.5",
        "rides",
    ],
    "training-route": [
        "training route",
        "yellow",
        "žuta",
        "trening",
        "2 meter",
        "2 metres",
        "2 m",
        "lowest route",
        "route at 2",
        "tracks",
    ],
    "low-zipline": [
        "treetop",
        "krošnj",
        "6 and 9",
        "6 m",
        "blue course",
        "113",
        "high-ropes",
        "high ropes",
        "visoke staze",
        "trees",
        "shade",
        "tracks",
    ],
    "valley-zipline": [
        "zipline",
        "zip line",
        "zip-line",
        "120 m",
        "120 meter",
        "valley",
        "dolinski",
    ],
    "devils-causeway": [
        "causeway",
        "devil",
        "vražj",
        "unicycle",
        "monocycle",
        "monocikl",
    ],
    "climbing-wall": [
        "climbing",
        "climb",
        "penja",
        "climbing wall",
        "penjački",
    ],
    "aerotrim": [
        "aerotrim",
        "gyroscope",
        "žiroskop",
    ],
    "20m-drop": [
        "free fall",
        "quick jump",
        "20 m",
        "20 meter",
        "20-metre",
        "pad s",
        "rides",
        "adrenaline",
    ],
}

LABELS = {
    "en": {
        "heading": "TripAdvisor reviews mentioning {activity}",
        "summary": "{rating} on TripAdvisor · {count} reviews",
        "read_all": "All {count} reviews on TripAdvisor",
        "generic_heading": "What guests say",
        "google_heading": "Google reviews mentioning {activity}",
        "google_summary": "{rating} on Google · {count}",
        "google_read_all": "Read more reviews on Google",
        "google_generic_heading": "What guests say on Google",
    },
    "hr": {
        "heading": "TripAdvisor recenzije koje spominju {activity}",
        "summary": "{rating} na TripAdvisoru · {count} recenzija",
        "read_all": "Svih {count} recenzija na TripAdvisoru",
        "generic_heading": "Što kažu gosti",
        "google_heading": "Google recenzije koje spominju {activity}",
        "google_summary": "{rating} na Googleu · {count}",
        "google_read_all": "Više recenzija na Googleu",
        "google_generic_heading": "Što gosti kažu na Googleu",
    },
}


def _truncate_quote(text: str, limit: int = 220) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0].rstrip(".,;:!?") + "…"


def _format_review_date(date_str: str, lang: str) -> str:
    parts = date_str.split("-")
    if len(parts) == 1:
        return date_str
    year, month, day = parts
    if lang == "hr":
        months = ["sij", "velj", "ožu", "tra", "svi", "lip", "srp", "kol", "ruj", "lis", "stu", "pro"]
        return f"{int(day)}. {months[int(month) - 1]} {year}."
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{months[int(month) - 1]} {day}, {year}"


def score_review_for_activity(review: dict, en_slug: str) -> int:
    keywords = ACTIVITY_REVIEW_KEYWORDS.get(en_slug, [])
    if not keywords:
        return 0
    haystack = f"{review.get('en', '')} {review.get('hr', '')}".lower()
    return sum(1 for keyword in keywords if keyword.lower() in haystack)


def generic_reviews(*, limit: int = 1) -> list[dict]:
    """Reviews that praise the park without naming a specific attraction."""
    named_attractions = [
        "catapult",
        "katapult",
        "swing",
        "ljulja",
        "zipline",
        "free fall",
        "quick jump",
        "climbing",
        "penja",
        "aerotrim",
        "gyroscope",
        "unicycle",
        "monocycle",
        "causeway",
        "vražj",
    ]
    candidates: list[tuple[str, dict]] = []
    for review in review_list():
        text = f"{review.get('en', '')} {review.get('hr', '')}".lower()
        if any(word in text for word in named_attractions):
            continue
        candidates.append((review["date"], review))
    candidates.sort(key=lambda item: item[0], reverse=True)
    return [review for _, review in candidates[:limit]]


def score_google_review_for_activity(review: dict, en_slug: str) -> int:
    score = score_review_for_activity(review, en_slug)
    featured = review.get("featured_for") or []
    if en_slug in featured:
        score += 10
    return score


def google_generic_reviews(*, limit: int = 1) -> list[dict]:
    """Google reviews with no strong activity tie-in."""
    named_attractions = [
        word
        for slug, slug_keywords in ACTIVITY_REVIEW_KEYWORDS.items()
        for word in slug_keywords
    ]
    candidates: list[tuple[str, dict]] = []
    for review in google_review_list():
        if review.get("featured_for"):
            continue
        text = review.get("en", "").lower()
        if any(word.lower() in text for word in named_attractions):
            continue
        candidates.append((review["date"], review))
    candidates.sort(key=lambda item: item[0], reverse=True)
    return [review for _, review in candidates[:limit]]


def google_reviews_for_activity(en_slug: str, *, limit: int = 1) -> list[dict]:
    scored: list[tuple[int, str, dict]] = []
    for review in google_review_list():
        score = score_google_review_for_activity(review, en_slug)
        if score:
            scored.append((score, review["date"], review))
    scored.sort(key=lambda item: (-item[0], item[1]))
    matched = [review for _, _, review in scored[:limit]]
    if matched:
        return matched
    return google_generic_reviews(limit=limit) or google_review_list()[:limit]


def _render_review_teaser(
    *,
    modifier: str,
    aria_label: str,
    heading: str,
    summary: str,
    reviews: list[dict],
    quote_key: str,
    lang: str,
    read_all_label: str,
    read_all_url: str,
) -> str:
    blocks = []
    for review in reviews:
        quote = _truncate_quote(review[quote_key])
        when = _format_review_date(review["date"], lang)
        blocks.append(
            f"""<blockquote class="review-teaser__quote">
        <p>“{quote}”</p>
        <cite class="review-teaser__author">{review['author']} · {when}</cite>
      </blockquote>"""
        )

    return f"""<aside class="review-teaser review-teaser--activity{modifier}" aria-label="{aria_label}">
      <h3 class="review-teaser__heading">{heading}</h3>
      <p class="review-teaser__summary"><strong>{summary}</strong></p>
      {"".join(blocks)}
      <p class="review-teaser__link"><a href="{read_all_url}" target="_blank" rel="noopener noreferrer">{read_all_label}</a></p>
    </aside>"""


def render_google_activity_reviews(activity: dict, lang: str) -> str:
    """Show a Google quote matched to this activity (1 review)."""
    data = activity[lang]
    en_slug = activity["en_slug"]
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    summary = labels["google_summary"].format(
        rating=GOOGLE_RATING_VALUE,
        count=GOOGLE_REVIEW_COUNT[lang],
    )
    read_all = labels["google_read_all"]

    matched = google_reviews_for_activity(en_slug, limit=1)
    has_specific = bool(score_google_review_for_activity(matched[0], en_slug)) if matched else False
    heading = (
        labels["google_heading"].format(activity=data["h1"])
        if has_specific
        else labels["google_generic_heading"]
    )

    return _render_review_teaser(
        modifier=" review-teaser--google",
        aria_label=heading,
        heading=heading,
        summary=summary,
        reviews=matched,
        quote_key=quote_key,
        lang=lang,
        read_all_label=read_all,
        read_all_url=GOOGLE_REVIEWS_URL,
    )


def reviews_for_activity(en_slug: str, *, limit: int = 2) -> list[dict]:
    scored: list[tuple[int, str, dict]] = []
    for review in review_list():
        score = score_review_for_activity(review, en_slug)
        if score:
            scored.append((score, review["date"], review))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [review for _, _, review in scored[:limit]]


def render_activity_reviews(activity: dict, lang: str) -> str:
    """Show TripAdvisor and Google quotes matched to this activity."""
    data = activity[lang]
    en_slug = activity["en_slug"]
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    aggregate = aggregate_rating()
    rating = aggregate["rating_value"]
    count = aggregate["rating_count"]
    summary = labels["summary"].format(rating=rating, count=count)
    read_all = labels["read_all"].format(count=count)

    matched = reviews_for_activity(en_slug, limit=2)
    has_specific = bool(matched)
    if not matched:
        matched = generic_reviews(limit=1) or review_list()[:1]

    heading = (
        labels["heading"].format(activity=data["h1"])
        if has_specific
        else labels["generic_heading"]
    )

    tripadvisor = _render_review_teaser(
        modifier="",
        aria_label=heading,
        heading=heading,
        summary=summary,
        reviews=matched,
        quote_key=quote_key,
        lang=lang,
        read_all_label=read_all,
        read_all_url=TRIPADVISOR_URL,
    )
    google = render_google_activity_reviews(activity, lang)
    return f"{tripadvisor}\n      {google}"
