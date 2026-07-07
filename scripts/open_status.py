"""Park open/closed status for visitor bar (Europe/Zagreb)."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

from brand_voice import PHONES

TZ = ZoneInfo("Europe/Zagreb")
OPEN_HOUR = 9
CLOSE_HOUR = 17
LAST_ENTRY_HOUR = 15

LABELS = {
    "en": {
        "open": "Open now",
        "closed": "Closed now",
        "opens_tomorrow": "Opens tomorrow at 9 AM",
        "opens_at": "Opens at 9 AM",
        "last_entry_soon": "Last entry in {minutes} min",
        "last_entry": "Last entry 3 PM",
        "no_new_entries": "No new entries today unless pre-arranged",
        "call_to_book": "Call to book",
    },
    "hr": {
        "open": "Otvoreno sada",
        "closed": "Zatvoreno sada",
        "opens_tomorrow": "Otvara se sutra u 9 h",
        "opens_at": "Otvara se u 9 h",
        "last_entry_soon": "Zadnji ulaz za {minutes} min",
        "last_entry": "Zadnji ulaz u 15 h",
        "no_new_entries": "Nema novih ulaza danas osim po prethodnom dogovoru",
        "call_to_book": "Pozovite za rezervaciju",
    },
}


def amber_status_message(lang: str) -> str:
    labels = LABELS[lang]
    phone = PHONES[1] if lang == "hr" else PHONES[0]
    return (
        f'{labels["no_new_entries"]} · '
        f'<a class="open-status__call" href="tel:{phone["tel"]}">{labels["call_to_book"]}</a>'
    )


def park_status(lang: str, now: datetime | None = None) -> dict:
    """Return status class and message for the visitor bar."""
    now = now or datetime.now(TZ)
    labels = LABELS[lang]
    minutes = now.hour * 60 + now.minute
    open_at = OPEN_HOUR * 60
    close_at = CLOSE_HOUR * 60
    last_entry_at = LAST_ENTRY_HOUR * 60

    if open_at <= minutes < last_entry_at:
        mins_left = last_entry_at - minutes
        if mins_left <= 60:
            message = labels["last_entry_soon"].format(minutes=mins_left)
        else:
            message = f"{labels['open']} · {labels['last_entry']}"
        return {"state": "open", "message": message}

    if last_entry_at <= minutes < close_at:
        return {"state": "amber", "message": amber_status_message(lang), "html": True}

    if minutes < open_at:
        return {"state": "closed", "message": labels["opens_at"]}

    return {
        "state": "closed",
        "message": f"{labels['closed']} · {labels['opens_tomorrow']}",
    }
