"""Shared brand messaging — hours, phones, and voice for Glavani Park."""

BOOKING_EMAIL = "info@glavanipark.com"
ONLINE_BOOKING_MAX = 10
CALL_FOR_GROUPS_ABOVE = 10

PHONES = (
    {
        "name": "Nigel Simpson",
        "display": "+385 91 896 4525",
        "tel": "+385918964525",
        "image": "nigel-simpson-glavanipark.webp",
    },
    {
        "name": "Nevenko Bulić",
        "display": "+385 98 224 314",
        "tel": "+38598224314",
        "image": "nevenko-bulic-glavanipark.webp",
    },
)

NIGEL_PHONE = PHONES[0]


def limits_call_link() -> str:
    """Clickable tel link for Nigel — used for height/weight limit questions."""
    p = NIGEL_PHONE
    return f'<a href="tel:{p["tel"]}">{p["display"]}</a>'


def limits_call_plain() -> str:
    return NIGEL_PHONE["display"]


def limits_call_cta(lang: str, *, unsure: bool = True) -> str:
    link = limits_call_link()
    if lang == "hr":
        tail = " ako niste sigurni." if unsure else "."
        return f"Nazovite nas na {link}{tail}"
    tail = " if you are unsure." if unsure else "."
    return f"Call us on {link}{tail}"


def limits_call_prompt(lang: str, continuation: str) -> str:
    """Call CTA where more text follows the phone link."""
    link = limits_call_link()
    if lang == "hr":
        return f"Nazovite nas na {link} {continuation}"
    return f"Call us on {link} {continuation}"

VISITOR = {
    "en": {
        "hours_label": "Open daily",
        "hours": "9 AM – 5 PM",
        "tagline": "Croatia's Number 1 Adventure Park · Istria · A Great Place to Be",
        "number_one": "Croatia's Number 1 Adventure Park",
        "welcome": "A Great Place to Be",
        "hero_subtitle": (
            "We're a family-run adventure park in the Istrian countryside — friendly, qualified staff, "
            "forest ziplines, and memories you'll talk about for years. Drop in for a chat before you clip in."
        ),
        "visitor_bar_aria": "Visitor information",
        "logo_alt": "Glavani Park — A Great Place to Be",
    },
    "hr": {
        "hours_label": "Otvoreno svaki dan",
        "hours": "9–17 h",
        "tagline": "Broj 1 avanturistički park u Hrvatskoj · Istria · odlično mjesto za avanturu",
        "number_one": "Broj 1 avanturistički park u Hrvatskoj",
        "welcome": "Odlično mjesto za avanturu",
        "hero_subtitle": (
            "Obiteljski avanturistički park u istarskom krajoliku — profesionalna i srdačna ekipa, "
            "zipline u šumi i uspomene o kojima ćete pričati godinama. Svratite na kavu prije nego krenete u avanturu."
        ),
        "visitor_bar_aria": "Informacije za posjetitelje",
        "logo_alt": "Glavani Park — odlično mjesto za avanturu",
    },
}
