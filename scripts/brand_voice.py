"""Shared brand messaging — hours, phones, and voice for Glavani Park."""

BOOKING_EMAIL = "info@glavanipark.com"
# FormSubmit requires activation per recipient. office@ was activated when the form launched;
# route via that endpoint and CC info@ until info@ is activated on FormSubmit (then switch endpoint).
BOOKING_FORMSUBMIT_ENDPOINT = "office@glavanipark.com"
BOOKING_FORMSUBMIT_CC = BOOKING_EMAIL
BOOKING_SUBMIT_URL = f"https://formsubmit.co/ajax/{BOOKING_FORMSUBMIT_ENDPOINT}"
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
