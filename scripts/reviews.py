"""Visitor reviews carousel — Google & TripAdvisor 5-star excerpts."""

GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Glavani+Park+Barban"
TRIPADVISOR_URL = "https://www.tripadvisor.com/Search?q=Glavani+Park+Barban"

REVIEWS = {
    "en": [
        {
            "source": "tripadvisor",
            "quote": "Super nice park — different from the average climbing parks. You can choose a catapult or swing, and the guidance is excellent.",
            "author": "TripAdvisor visitor",
        },
        {
            "source": "google",
            "quote": "A day full of adrenaline! Staff were super nice and always on hand. The human catapult alone is worth the visit — unique in Croatia.",
            "author": "Google reviewer",
        },
        {
            "source": "tripadvisor",
            "quote": "We came with kids aged 10, 8 and 6. Great explanation and support on the routes, then the giant swing together. Calm, helpful staff — a brilliant day.",
            "author": "Family visitor",
        },
        {
            "source": "google",
            "quote": "Instructors were friendly and gave clear instructions. Really fun exploring every attraction — highly recommend for thrill seekers in Istria.",
            "author": "Google reviewer",
        },
        {
            "source": "tripadvisor",
            "quote": "The youngest couldn't get enough of it. Staff were patient when things didn't work out first time. Wonderful day — we'll definitely be back!",
            "author": "Family visitor",
        },
        {
            "source": "google",
            "quote": "A great adventure park with a professional team. Well maintained, unique rides, and you only pay for what you do. 100% recommended.",
            "author": "Google reviewer",
        },
        {
            "source": "tripadvisor",
            "quote": "We spent a lovely day with two children aged 9 and 12. Staff are very friendly — you choose which attractions to try and build up at your own pace.",
            "author": "Family visitor",
        },
        {
            "source": "google",
            "quote": "Really fun exploring every attraction in the park. Great for thrill seekers visiting the Istrian peninsula — instructors were brilliant throughout.",
            "author": "Google reviewer",
        },
        {
            "source": "tripadvisor",
            "quote": "The 12 m swing, 120 m zipline, 20 m free fall and human catapult make this a real experience. Staff super nice, helpful and always nearby.",
            "author": "TripAdvisor visitor",
        },
        {
            "source": "google",
            "quote": "Amazing day out! Clear safety briefing, friendly instructors, and a nice cold drink afterwards. We will definitely come back when we are in the area again.",
            "author": "Google reviewer",
        },
        {
            "source": "tripadvisor",
            "quote": "Been here for the second time and it was just as good. You only pay for what you do, which makes it very affordable — and staff remember returning guests.",
            "author": "Returning visitor",
        },
        {
            "source": "google",
            "quote": "Quiet day with few tourists — even better. Routes from 2 m up to 9 m, fun for teens and manageable for younger kids on the lowest course.",
            "author": "Family visitor",
        },
        {
            "source": "tripadvisor",
            "quote": "Four teenage boys and they loved every minute — catapult, swing, ice cream break, and excellent guidance. Different from your average climbing park.",
            "author": "TripAdvisor visitor",
        },
    ],
    "hr": [
        {
            "source": "tripadvisor",
            "quote": "Super park — drugačiji od prosječnih penjačkih parkova. Možete odabrati katapultu ili ljuljačku, a vodstvo je izvrsno.",
            "author": "Posjetitelj s TripAdvisora",
        },
        {
            "source": "google",
            "quote": "Dan pun adrenalina! Osoblje je bilo super i uvijek dostupno. Ljudska katapulta sama po sebi vrijedi posjeta — jedinstvena u Hrvatskoj.",
            "author": "Google recenzija",
        },
        {
            "source": "tripadvisor",
            "quote": "Došli smo s djecom (10, 8 i 6 godina). Odlična objašnjenja i podrška na stazama, zatim zajedno na veliku ljuljačku. Mirno, korisno osoblje — sjajan dan.",
            "author": "Obiteljski posjetitelj",
        },
        {
            "source": "google",
            "quote": "Instruktori su bili ljubazni i dali jasne upute. Zabavno je istraživati svaku atrakciju — toplo preporučujemo avanturistima u Istri.",
            "author": "Google recenzija",
        },
        {
            "source": "tripadvisor",
            "quote": "Mlađe dijete nije moglo dočekati ponovno. Osoblje je strpljivo kad nešto ne uspije odmah. Prekrasan dan — sigurno se vraćamo!",
            "author": "Obiteljski posjetitelj",
        },
        {
            "source": "google",
            "quote": "Odličan avanturistički park s profesionalnim timom. Uredan, jedinstvene atrakcije, a plaćate samo ono što radite. 100% preporuka.",
            "author": "Google recenzija",
        },
        {
            "source": "tripadvisor",
            "quote": "Proveli smo prekrasan dan s djecom od 9 i 12 godina. Osoblje je vrlo ljubazno — sami birate atrakcije i postupno se upuštate u avanturu.",
            "author": "Obiteljski posjetitelj",
        },
        {
            "source": "google",
            "quote": "Zabavno je istraživati svaku atrakciju u parku. Odlično za avanturiste na Istarskom poluotoku — instruktori su bili izvrsni.",
            "author": "Google recenzija",
        },
        {
            "source": "tripadvisor",
            "quote": "Ljuljačka od 12 m, zipline od 120 m, slobodan pad s 20 m i ljudska katapulta — pravo iskustvo. Osoblje super, korisno i uvijek blizu.",
            "author": "Posjetitelj s TripAdvisora",
        },
        {
            "source": "google",
            "quote": "Fantastičan izlet! Jasna sigurnosna obuka, ljubazni instruktori i hladno piće na kraju. Sigurno se vraćamo kad budemo opet u okolici.",
            "author": "Google recenzija",
        },
        {
            "source": "tripadvisor",
            "quote": "Drugi put ovdje i opet odlično. Plaćate samo ono što radite, što je vrlo pristupačno — osoblje prepoznaje goste koji se vraćaju.",
            "author": "Ponovni posjetitelj",
        },
        {
            "source": "google",
            "quote": "Mirniji dan s manje turista — još bolje. Staze od 2 m do 9 m, zabavno za tinejdžere, a mlađa djeca uživaju na najnižoj stazi.",
            "author": "Obiteljski posjetitelj",
        },
        {
            "source": "tripadvisor",
            "quote": "Četiri tinejdžera i uživali su u svakoj minuti — katapulta, ljuljačka, sladoled i odlično vodstvo. Drugačije od prosječnog penjačkog parka.",
            "author": "Posjetitelj s TripAdvisora",
        },
    ],
}

LABELS = {
    "en": {
        "heading": "What Visitors Say",
        "google": "Google",
        "tripadvisor": "TripAdvisor",
        "stars": "5 out of 5 stars",
        "prev": "Previous review",
        "next": "Next review",
        "read_google": "More on Google",
        "read_tripadvisor": "More on TripAdvisor",
    },
    "hr": {
        "heading": "Što kažu posjetitelji",
        "lead": "Recenzije s 5 zvjezdica s Googlea i TripAdvisora",
        "google": "Google",
        "tripadvisor": "TripAdvisor",
        "stars": "5 od 5 zvjezdica",
        "prev": "Prethodna recenzija",
        "next": "Sljedeća recenzija",
        "read_google": "Više na Googleu",
        "read_tripadvisor": "Više na TripAdvisoru",
    },
}


def _source_badge(source: str, labels: dict) -> str:
    mod = "google" if source == "google" else "tripadvisor"
    name = labels["google"] if source == "google" else labels["tripadvisor"]
    return f'<span class="review-card__source review-card__source--{mod}">{name}</span>'


def render_reviews_section(lang: str) -> str:
    labels = LABELS[lang]
    reviews = REVIEWS[lang]
    cards = []
    for review in reviews:
        cards.append(
            f"""<article class="review-card">
          {_source_badge(review["source"], labels)}
          <div class="review-card__stars" aria-label="{labels['stars']}">★★★★★</div>
          <blockquote class="review-card__quote"><p>{review['quote']}</p></blockquote>
          <cite class="review-card__author">— {review['author']}</cite>
        </article>"""
        )
    cards_html = "\n        ".join(cards)
    return f"""<section class="section section--wide section--theme-reviews" id="reviews" aria-labelledby="reviews-heading">
      <div class="section__inner">
        <div class="section__heading">
          <h2 id="reviews-heading">{labels['heading']}</h2>
        </div>
        <div class="reviews-carousel" data-reviews-carousel>
          <button type="button" class="reviews-carousel__nav reviews-carousel__nav--prev" aria-label="{labels['prev']}" data-reviews-prev>‹</button>
          <div class="reviews-carousel__track" tabindex="0" data-reviews-track>
            {cards_html}
          </div>
          <button type="button" class="reviews-carousel__nav reviews-carousel__nav--next" aria-label="{labels['next']}" data-reviews-next>›</button>
        </div>
        <p class="reviews-carousel__links">
          <a href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener noreferrer">{labels['read_google']}</a>
          <span aria-hidden="true">·</span>
          <a href="{TRIPADVISOR_URL}" target="_blank" rel="noopener noreferrer">{labels['read_tripadvisor']}</a>
        </p>
      </div>
    </section>"""
