"""Formspree enquiry form for general contact (not the booking wizard)."""

from __future__ import annotations

import html

from activities import ACTIVITIES
from site_config import FORMSPREE_FORM_ID

LABELS = {
    "en": {
        "name": "Your name",
        "email": "Email address",
        "phone": "Phone number",
        "activity": "Activity (optional)",
        "activity_default": "General enquiry",
        "date": "Preferred visit date (optional)",
        "adults": "Number of adults",
        "children": "Number of children",
        "message": "Message",
        "submit": "Send enquiry",
        "submitting": "Sending…",
        "success_title": "Message sent",
        "success_lead": "Thank you — we have received your enquiry and aim to reply within 48 hours.",
        "success_spam": (
            "If you do not hear back, check spam for email from info@glavanipark.com or "
            "office@glavanipark.com, or call us to confirm."
        ),
        "error": "Sorry, we could not send your message. Please call us instead.",
        "required_hint": "Fields marked * are required.",
        "not_configured": (
            "The contact form is not yet configured. Please call or email "
            "info@glavanipark.com for now."
        ),
    },
    "hr": {
        "name": "Ime i prezime",
        "email": "E-mail adresa",
        "phone": "Broj telefona",
        "activity": "Aktivnost (opcionalno)",
        "activity_default": "Opći upit",
        "date": "Željeni datum posjeta (opcionalno)",
        "adults": "Broj odraslih",
        "children": "Broj djece",
        "message": "Poruka",
        "submit": "Pošaljite upit",
        "submitting": "Šaljem…",
        "success_title": "Poruka poslana",
        "success_lead": "Hvala — primili smo vaš upit i nastojimo odgovoriti u roku od 48 sati.",
        "success_spam": (
            "Ako ne dobijete odgovor, provjerite neželjenu poštu za info@glavanipark.com ili "
            "office@glavanipark.com, ili nas nazovite."
        ),
        "error": "Nažalost nismo mogli poslati poruku. Molimo nazovite nas.",
        "required_hint": "Polja označena * su obavezna.",
        "not_configured": (
            "Obrazac još nije konfiguriran. Za sada nazovite ili pišite na info@glavanipark.com."
        ),
    },
}


def _activity_options(lang: str) -> str:
    quote_key = "hr" if lang == "hr" else "en"
    default = LABELS[lang]["activity_default"]
    opts = [f'<option value="">{html.escape(default)}</option>']
    for activity in ACTIVITIES:
        name = activity[quote_key]["h1"]
        opts.append(f'<option value="{html.escape(name)}">{html.escape(name)}</option>')
    return "".join(opts)


def render_contact_form(lang: str) -> str:
    labels = LABELS[lang]
    if not FORMSPREE_FORM_ID:
        return f'<p class="contact-form__notice" role="status">{labels["not_configured"]}</p>'

    action = f"https://formspree.io/f/{html.escape(FORMSPREE_FORM_ID)}"
    return f"""<form class="contact-form" id="contact-form" action="{action}" method="POST" novalidate>
      <p class="contact-form__hint">{labels['required_hint']}</p>
      <div class="contact-form__row">
        <div>
          <label for="contact-name">{labels['name']} *</label>
          <input id="contact-name" name="name" type="text" required autocomplete="name">
        </div>
        <div>
          <label for="contact-email">{labels['email']} *</label>
          <input id="contact-email" name="email" type="email" required autocomplete="email">
        </div>
      </div>
      <div class="contact-form__row">
        <div>
          <label for="contact-phone">{labels['phone']} *</label>
          <input id="contact-phone" name="phone" type="tel" required autocomplete="tel">
        </div>
        <div>
          <label for="contact-activity">{labels['activity']}</label>
          <select id="contact-activity" name="activity">{_activity_options(lang)}</select>
        </div>
      </div>
      <div class="contact-form__row">
        <div>
          <label for="contact-date">{labels['date']}</label>
          <input id="contact-date" name="date" type="date">
        </div>
        <div>
          <label for="contact-adults">{labels['adults']}</label>
          <input id="contact-adults" name="adults" type="number" min="0" max="99" value="1">
        </div>
        <div>
          <label for="contact-children">{labels['children']}</label>
          <input id="contact-children" name="children" type="number" min="0" max="99" value="0">
        </div>
      </div>
      <div>
        <label for="contact-message">{labels['message']} *</label>
        <textarea id="contact-message" name="message" rows="5" required></textarea>
      </div>
      <input type="hidden" name="_subject" value="Glavani Park enquiry">
      <input type="text" name="_gotcha" class="contact-form__honeypot" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button type="submit" class="btn-primary" id="contact-submit">{labels['submit']}</button>
      <div class="contact-form__feedback" id="contact-feedback" role="status" aria-live="polite" hidden></div>
    </form>"""
