"""Homepage review carousel — curated Google and TripAdvisor blurbs."""

from __future__ import annotations

import html

from reviews import (
    GOOGLE_RATING_VALUE,
    GOOGLE_REVIEWS_URL,
    GOOGLE_REVIEW_COUNT,
    TRIPADVISOR_URL,
    aggregate_rating,
)

HOME_CAROUSEL_REVIEWS: list[dict] = [
    {
        "source": "google",
        "author": "Charlotte",
        "date": "2026",
        "en": (
            "The human catapult was insane!! So fast, and so much fun!! The obstacles were challenging, "
            "but still placed at a suitable height, and can be enjoyed by both children and adults. "
            "The park dog was also extremely adorable and friendly."
        ),
        "hr": (
            "Ljudska katapulta je bila nevjerojatna — tako brza i zabavna! Prepreke su bile izazovne, "
            "ali na prikladnoj visini za djecu i odrasle. Pas u parku bio je presladak i druželjubiv."
        ),
    },
    {
        "source": "tripadvisor",
        "author": "Sandra",
        "date": "2025-07-08",
        "en": (
            "The human catapult was a unique experience and worth visiting the park for (once in all Croatia). "
            "The 12 meter high swing, the 120 meter long zipline at 30 meters height, and the free fall from "
            "20 meters make the park a real experience. We can recommend it 100%!"
        ),
        "hr": (
            "Ljudska katapulta sama po sebi vrijedi posjeta — jedinstvena u Hrvatskoj. Ljuljačka od 12 m, "
            "zipline od 120 m na 30 m visine i slobodan pad s 20 m čine pravo iskustvo. 100% preporuka!"
        ),
    },
    {
        "source": "google",
        "author": "Rowan Hope",
        "date": "2026",
        "en": (
            "The zip-line (arguably the best in pula) and the catapult were insane! The kindness and humour "
            "the staff bring give the park a certain charm that you simply won't find anywhere else. "
            "Would 100% recommend glavani park!"
        ),
        "hr": (
            "Zipline (vjerojatno najbolji kod Pule) i katapult bili su nevjerojatni! Ljubaznost i humor "
            "osoblja daju parku šarm koji nećete naći drugdje. 100% preporučujem Glavani Park!"
        ),
    },
    {
        "source": "google",
        "author": "Carsten Stauer",
        "date": "2026",
        "en": (
            "A must for every adventurer and adrenaline junkie! Worth every penny! Better than any commercial "
            "theme park. And the staff/owners are incredibly welcoming."
        ),
        "hr": (
            "Obavezno za svakog avanturistu i ljubitelja adrenalina! Vrijedi svake kune — bolje od bilo "
            "kakvog komercijalnog tematskog parka. Osoblje i vlasnici nevjerojatno su gostoljubivi."
        ),
    },
    {
        "source": "tripadvisor",
        "author": "Renate V.",
        "date": "2023-08-13",
        "en": (
            "We went back with our daughters, who are now 14, 12 and 10 years old. It was amazing! "
            "Staff is also really patient and friendly. When we are in the area again, we will definitely come back!"
        ),
        "hr": (
            "Vratili smo se s kćerima od 14, 12 i 10 godina. Bilo je nevjerojatno! Osoblje je stvarno "
            "strpljivo i ljubazno. Kad budemo opet u okolici, sigurno se vraćamo!"
        ),
    },
    {
        "source": "google",
        "author": "Michal Pysny",
        "date": "2025",
        "en": (
            "We visited with our 2 daughters — 6 & 7 years old. Calm and quiet atmosphere, professional and "
            "very friendly guides. In every moment we felt safe and secured."
        ),
        "hr": (
            "Posjetili smo s dvije kćeri od 6 i 7 godina. Mirna atmosfera i profesionalan, vrlo prijateljski "
            "pristup vodiča. U svakom trenutku smo se osjećali sigurno."
        ),
    },
    {
        "source": "tripadvisor",
        "author": "Georg B.",
        "date": "2023-07-11",
        "en": (
            "Been here for the second time. It's great! Nigel's team is very accommodating and competent. "
            "Fully recommended. We will come back!"
        ),
        "hr": (
            "Drugi put ovdje — odlično je! Nigelov tim je vrlo susretljiv i stručan. Potpuna preporuka. "
            "Vratit ćemo se!"
        ),
    },
    {
        "source": "google",
        "author": "N W",
        "date": "2025",
        "en": (
            "All the rides here are very safe (that's our main concern). Nigel and his crew will accompany "
            "you all the way so you are not doing this alone. Thanks again for such an amazing experience!"
        ),
        "hr": (
            "Sve atrakcije su vrlo sigurne — to nam je bila glavna briga. Nigel i ekipa su uz vas cijelo "
            "vrijeme. Hvala još jednom na nevjerojatnom iskustvu!"
        ),
    },
]

LABELS = {
    "en": {
        "heading": "What guests say",
        "lead": (
            "{google_rating} on Google · {google_count} · "
            "{ta_rating} on TripAdvisor · {ta_count} reviews"
        ),
        "prev": "Previous review",
        "next": "Next review",
        "source_google": "Google review",
        "source_tripadvisor": "TripAdvisor review",
        "read_google": "More on Google",
        "read_tripadvisor": "More on TripAdvisor",
    },
    "hr": {
        "heading": "Što kažu gosti",
        "lead": (
            "{google_rating} na Googleu · {google_count} · "
            "{ta_rating} na TripAdvisoru · {ta_count} recenzija"
        ),
        "prev": "Prethodna recenzija",
        "next": "Sljedeća recenzija",
        "source_google": "Google recenzija",
        "source_tripadvisor": "TripAdvisor recenzija",
        "read_google": "Više na Googleu",
        "read_tripadvisor": "Više na TripAdvisoru",
    },
}


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


def render_home_reviews_carousel(lang: str) -> str:
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    aggregate = aggregate_rating()
    lead = labels["lead"].format(
        google_rating=GOOGLE_RATING_VALUE,
        google_count=GOOGLE_REVIEW_COUNT[lang],
        ta_rating=aggregate["rating_value"],
        ta_count=aggregate["rating_count"],
    )

    slides = []
    for review in HOME_CAROUSEL_REVIEWS:
        source = review["source"]
        is_google = source == "google"
        source_label = labels["source_google"] if is_google else labels["source_tripadvisor"]
        read_label = labels["read_google"] if is_google else labels["read_tripadvisor"]
        read_url = GOOGLE_REVIEWS_URL if is_google else TRIPADVISOR_URL
        modifier = " review-carousel__slide--google" if is_google else " review-carousel__slide--tripadvisor"
        quote = html.escape(review[quote_key])
        when = _format_review_date(review["date"], lang)
        slides.append(
            f"""<article class="review-carousel__slide{modifier}">
          <p class="review-carousel__source">{source_label}</p>
          <p class="review-carousel__stars" aria-hidden="true">★★★★★</p>
          <blockquote class="review-carousel__quote">
            <p>“{quote}”</p>
          </blockquote>
          <cite class="review-carousel__author">{html.escape(review['author'])} · {when}</cite>
          <p class="review-carousel__link"><a href="{read_url}" target="_blank" rel="noopener noreferrer">{read_label}</a></p>
        </article>"""
        )

    return f"""<section class="section section--theme-forest home-reviews" aria-labelledby="home-reviews-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="home-reviews-heading">{labels['heading']}</h2>
          <p>{lead}</p>
        </div>
        <div class="review-carousel" data-review-carousel tabindex="0">
          <button type="button" class="review-carousel__nav review-carousel__nav--prev" aria-label="{labels['prev']}" data-review-prev>‹</button>
          <div class="review-carousel__viewport">
            <div class="review-carousel__track" data-review-track>
              {"".join(slides)}
            </div>
          </div>
          <button type="button" class="review-carousel__nav review-carousel__nav--next" aria-label="{labels['next']}" data-review-next>›</button>
          <div class="review-carousel__dots" data-review-dots role="tablist" aria-label="{labels['heading']}"></div>
        </div>
      </div>
    </section>"""
