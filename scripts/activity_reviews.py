"""Match TripAdvisor reviews to specific activities by keyword."""

from __future__ import annotations

from reviews import TRIPADVISOR_URL, aggregate_rating, review_list

# Keywords searched in both EN and HR review text (case-insensitive).
ACTIVITY_REVIEW_KEYWORDS: dict[str, list[str]] = {
    "human-catapult": [
        "catapult",
        "human catapult",
        "katapult",
        "ljudska katapult",
    ],
    "high-swing": [
        "swing",
        "giant swing",
        "3g swing",
        "ljulja",
        "visoka ljulja",
        "12 meter",
        "12.5",
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
    ],
}

LABELS = {
    "en": {
        "heading": "TripAdvisor reviews mentioning {activity}",
        "summary": "{rating} on TripAdvisor · {count} reviews",
        "read_all": "All {count} reviews on TripAdvisor",
        "generic_heading": "What guests say",
    },
    "hr": {
        "heading": "TripAdvisor recenzije koje spominju {activity}",
        "summary": "{rating} na TripAdvisoru · {count} recenzija",
        "read_all": "Svih {count} recenzija na TripAdvisoru",
        "generic_heading": "Što kažu gosti",
    },
}


def _truncate_quote(text: str, limit: int = 220) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0].rstrip(".,;:!?") + "…"


def _format_review_date(date_str: str, lang: str) -> str:
    year, month, day = date_str.split("-")
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


def reviews_for_activity(en_slug: str, *, limit: int = 2) -> list[dict]:
    scored: list[tuple[int, str, dict]] = []
    for review in review_list():
        score = score_review_for_activity(review, en_slug)
        if score:
            scored.append((score, review["date"], review))
    scored.sort(key=lambda item: (-item[0], item[1]), reverse=True)
    return [review for _, _, review in scored[:limit]]


def render_activity_reviews(activity: dict, lang: str) -> str:
    """Show TripAdvisor quotes that mention this activity (up to 2)."""
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

    blocks = []
    for review in matched:
        quote = _truncate_quote(review[quote_key])
        when = _format_review_date(review["date"], lang)
        blocks.append(
            f"""<blockquote class="review-teaser__quote">
        <p>“{quote}”</p>
        <cite class="review-teaser__author">{review['author']} · {when}</cite>
      </blockquote>"""
        )

    return f"""<aside class="review-teaser review-teaser--activity" aria-label="{heading}">
      <h3 class="review-teaser__heading">{heading}</h3>
      <p class="review-teaser__summary"><strong>{summary}</strong></p>
      {"".join(blocks)}
      <p class="review-teaser__link"><a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer">{read_all}</a></p>
    </aside>"""
