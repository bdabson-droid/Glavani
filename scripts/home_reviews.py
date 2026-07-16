"""Homepage testimonials — compact Google rating and short guest quotes."""

from __future__ import annotations

import html

from reviews import GOOGLE_RATING_VALUE, GOOGLE_REVIEWS_URL, GOOGLE_REVIEW_COUNT

HOME_TESTIMONIAL_QUOTES: list[dict] = [
    {
        "author": "Carsten Stauer",
        "en": (
            "A must for every adventurer! Better than any commercial theme park — "
            "and the staff are incredibly welcoming."
        ),
        "hr": (
            "Obavezno za svakog avanturistu! Bolje od komercijalnog tematskog parka — "
            "osoblje je nevjerojatno gostoljubivo."
        ),
    },
    {
        "author": "Rowan Hope",
        "en": (
            "The zipline and catapult were insane! The kindness and humour the staff bring "
            "give the park a charm you won't find anywhere else."
        ),
        "hr": (
            "Zipline i katapult bili su nevjerojatni! Ljubaznost i humor osoblja daju parku "
            "šarm koji nećete naći drugdje."
        ),
    },
    {
        "author": "Michal Pysny",
        "en": (
            "We visited with our daughters aged 6 and 7. Professional, friendly guides — "
            "we felt safe the whole time."
        ),
        "hr": (
            "Posjetili smo s kćerima od 6 i 7 godina. Profesionalni, prijateljski vodiči — "
            "cijelo vrijeme smo se osjećali sigurno."
        ),
    },
]

LABELS = {
    "en": {
        "heading": "Guest testimonials",
        "rating_aria": "{rating} out of 5 stars on Google",
        "rating_text": "<strong>{rating}</strong> on Google · {count}",
        "read_google": "Read all reviews on Google",
    },
    "hr": {
        "heading": "Što kažu gosti",
        "rating_aria": "{rating} od 5 zvjezdica na Googleu",
        "rating_text": "<strong>{rating}</strong> na Googleu · {count}",
        "read_google": "Sve recenzije na Googleu",
    },
}


def render_home_testimonials(lang: str) -> str:
    labels = LABELS[lang]
    quote_key = "hr" if lang == "hr" else "en"
    rating_aria = labels["rating_aria"].format(rating=GOOGLE_RATING_VALUE)
    rating_text = labels["rating_text"].format(
        rating=GOOGLE_RATING_VALUE,
        count=GOOGLE_REVIEW_COUNT[lang],
    )

    quotes = []
    for item in HOME_TESTIMONIAL_QUOTES:
        quote = html.escape(item[quote_key])
        author = html.escape(item["author"])
        quotes.append(
            f"""<blockquote class="home-testimonials__quote">
          <p>“{quote}”</p>
          <cite class="home-testimonials__author">— {author}</cite>
        </blockquote>"""
        )

    return f"""<section class="section section--theme-forest home-testimonials" aria-labelledby="home-testimonials-heading">
      <div class="section__inner home-testimonials__inner">
        <h2 id="home-testimonials-heading">{labels['heading']}</h2>
        <p class="home-testimonials__rating" role="img" aria-label="{rating_aria}">
          <span class="home-testimonials__stars" aria-hidden="true">★★★★★</span>
          <span class="home-testimonials__score">{rating_text}</span>
        </p>
        <div class="home-testimonials__quotes">
          {"".join(quotes)}
        </div>
        <p class="home-testimonials__link">
          <a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener noreferrer">{labels['read_google']}</a>
        </p>
      </div>
    </section>"""
