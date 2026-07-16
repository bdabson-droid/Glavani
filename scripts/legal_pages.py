"""Legal and contact page content."""

from __future__ import annotations

from brand_voice import BOOKING_EMAIL, PHONES, VISITOR
from site_config import COOKIE_SLUGS, CONTACT_SLUGS, PRIVACY_SLUGS, TERMS_SLUGS

OFFICE_EMAIL = "office@glavanipark.com"

LEGAL_PAGES = {
    "contact": {
        "en_slug": CONTACT_SLUGS["en"],
        "hr_slug": CONTACT_SLUGS["hr"],
        "en": {
            "title": "Contact Glavani Park | Enquiries & Group Bookings",
            "h1": "Contact Us",
            "meta_description": (
                "Contact Glavani Park in Istria — call Nigel or Nevenko, or send an enquiry. "
                "Open daily 9 AM–5 PM. info@glavanipark.com · office@glavanipark.com"
            ),
            "keywords": "contact Glavani Park, adventure park Istria phone, book Glavani Park",
            "lead": (
                "Questions about visiting, groups, or partnerships? Call us, email "
                f"{BOOKING_EMAIL}, or use the form below."
            ),
        },
        "hr": {
            "title": "Kontakt | Glavani Park Istria",
            "h1": "Kontakt",
            "meta_description": (
                "Kontaktirajte Glavani Park u Istri — nazovite Nigela ili Nevenka ili pošaljite upit. "
                "Otvoreno 9–17 h. info@glavanipark.com · office@glavanipark.com"
            ),
            "keywords": "kontakt Glavani Park, avanturistički park Istria telefon",
            "lead": (
                "Pitanja o posjetu, grupama ili partnerstvu? Nazovite nas, pišite na "
                f"{BOOKING_EMAIL} ili koristite obrazac u nastavku."
            ),
        },
    },
    "privacy": {
        "en_slug": PRIVACY_SLUGS["en"],
        "hr_slug": PRIVACY_SLUGS["hr"],
        "en": {
            "title": "Privacy Policy | Glavani Park",
            "h1": "Privacy Policy",
            "meta_description": "How Glavani Park handles your personal data when you visit our website or book activities.",
            "keywords": "Glavani Park privacy policy, GDPR Croatia",
            "sections": [
                {
                    "h2": "Who we are",
                    "paragraphs": [
                        "<p>Glavani Park is a family-run adventure park at Glavani 10, 52207 Barban, Istria, Croatia. "
                        f"Contact: {BOOKING_EMAIL}.</p>"
                    ],
                },
                {
                    "h2": "What we collect",
                    "paragraphs": [
                        "<p>When you book or contact us we may collect your name, email, phone number, visit date, "
                        "party size, and message content. We use this only to respond to enquiries and manage bookings.</p>"
                    ],
                },
                {
                    "h2": "Your rights",
                    "paragraphs": [
                        f"<p>Under GDPR you may request access, correction, or deletion of your data by emailing "
                        f"{BOOKING_EMAIL}.</p>"
                    ],
                },
            ],
        },
        "hr": {
            "title": "Pravila privatnosti | Glavani Park",
            "h1": "Pravila privatnosti",
            "meta_description": "Kako Glavani Park obrađuje vaše osobne podatke pri posjetu web stranici ili rezervaciji.",
            "keywords": "pravila privatnosti Glavani Park, GDPR Hrvatska",
            "sections": [
                {
                    "h2": "Tko smo",
                    "paragraphs": [
                        "<p>Glavani Park je obiteljski avanturistički park na adresi Glavani 10, 52207 Barban, Istra, Hrvatska. "
                        f"Kontakt: {BOOKING_EMAIL}.</p>"
                    ],
                },
                {
                    "h2": "Što prikupljamo",
                    "paragraphs": [
                        "<p>Kod rezervacije ili upita možemo prikupiti ime, e-mail, telefon, datum posjeta, broj osoba i poruku. "
                        "Podatke koristimo samo za odgovore i upravljanje rezervacijama.</p>"
                    ],
                },
                {
                    "h2": "Vaša prava",
                    "paragraphs": [
                        f"<p>Prema GDPR-u možete zatražiti pristup, ispravak ili brisanje podataka na {BOOKING_EMAIL}.</p>"
                    ],
                },
            ],
        },
    },
    "cookies": {
        "en_slug": COOKIE_SLUGS["en"],
        "hr_slug": COOKIE_SLUGS["hr"],
        "en": {
            "title": "Cookie Policy | Glavani Park",
            "h1": "Cookie Policy",
            "meta_description": "How Glavani Park uses cookies and similar technologies on this website.",
            "keywords": "Glavani Park cookies",
            "sections": [
                {
                    "h2": "Essential cookies",
                    "paragraphs": [
                        "<p>We use a small cookie to remember your analytics consent choice if you accept optional cookies.</p>"
                    ],
                },
                {
                    "h2": "Analytics",
                    "paragraphs": [
                        "<p>With your consent we may use Google Analytics 4 and/or Cloudflare Web Analytics to understand "
                        "how visitors use the site. You can decline optional cookies in the banner.</p>"
                    ],
                },
            ],
        },
        "hr": {
            "title": "Pravila o kolačićima | Glavani Park",
            "h1": "Pravila o kolačićima",
            "meta_description": "Kako Glavani Park koristi kolačiće na ovoj web stranici.",
            "keywords": "kolačići Glavani Park",
            "sections": [
                {
                    "h2": "Nužni kolačići",
                    "paragraphs": [
                        "<p>Koristimo mali kolačić za pamćenje vašeg izbora pristanka na analitiku ako prihvatite opcionalne kolačiće.</p>"
                    ],
                },
                {
                    "h2": "Analitika",
                    "paragraphs": [
                        "<p>Uz vaš pristanak možemo koristiti Google Analytics 4 i/ili Cloudflare Web Analytics. "
                        "Opcionalne kolačiće možete odbiti u banneru.</p>"
                    ],
                },
            ],
        },
    },
    "terms": {
        "en_slug": TERMS_SLUGS["en"],
        "hr_slug": TERMS_SLUGS["hr"],
        "en": {
            "title": "Terms of Use | Glavani Park",
            "h1": "Terms of Use",
            "meta_description": "Terms for using the Glavani Park website and booking adventure activities.",
            "keywords": "Glavani Park terms of use",
            "sections": [
                {
                    "h2": "Bookings",
                    "paragraphs": [
                        "<p>Online booking requests are subject to confirmation. Activity participation requires signed "
                        "waivers and compliance with safety briefings and weight/height guidance from staff.</p>"
                    ],
                },
                {
                    "h2": "Liability",
                    "paragraphs": [
                        "<p>Adventure activities involve inherent risk. Participants must follow instructor directions. "
                        "See our Safety page for equipment standards.</p>"
                    ],
                },
            ],
        },
        "hr": {
            "title": "Uvjeti korištenja | Glavani Park",
            "h1": "Uvjeti korištenja",
            "meta_description": "Uvjeti korištenja web stranice Glavani Parka i rezervacije aktivnosti.",
            "keywords": "uvjeti korištenja Glavani Park",
            "sections": [
                {
                    "h2": "Rezervacije",
                    "paragraphs": [
                        "<p>Online zahtjevi za rezervaciju podliježu potvrdi. Sudjelovanje zahtijeva potpisane izjave "
                        "i poštivanje sigurnosnih uputa osoblja.</p>"
                    ],
                },
                {
                    "h2": "Odgovornost",
                    "paragraphs": [
                        "<p>Avanturističke aktivnosti uključuju inherentni rizik. Sudionici moraju slijediti upute vodiča. "
                        "Pogledajte stranicu Sigurnost.</p>"
                    ],
                },
            ],
        },
    },
}
