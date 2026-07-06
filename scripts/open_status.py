"""Park open/closed status for visitor bar (Europe/Zagreb)."""

from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Zagreb")
OPEN_HOUR = 9
CLOSE_HOUR = 17
LAST_ENTRY_HOUR = 15

# Off-season: October through June (pre-book only; no walk-ins).
OFF_SEASON_MONTHS = frozenset({10, 11, 12, 1, 2, 3, 4, 5, 6})

LABELS = {
    "en": {
        "open": "Open now",
        "closed": "Closed now",
        "opens_tomorrow": "Opens tomorrow at 9 AM",
        "opens_at": "Opens at 9 AM",
        "last_entry_soon": "Last entry in {minutes} min",
        "last_entry": "Last entry 3 PM",
        "pre_booking_only": "Pre-booking only",
    },
    "hr": {
        "open": "Otvoreno sada",
        "closed": "Zatvoreno sada",
        "opens_tomorrow": "Otvara se sutra u 9 h",
        "opens_at": "Otvara se u 9 h",
        "last_entry_soon": "Zadnji ulaz za {minutes} min",
        "last_entry": "Zadnji ulaz u 15 h",
        "pre_booking_only": "Samo unaprijedna rezervacija",
    },
}


def is_off_season(now: datetime) -> bool:
    return now.month in OFF_SEASON_MONTHS


def park_status(lang: str, now: datetime | None = None) -> dict:
    """Return status class and message for the visitor bar."""
    now = now or datetime.now(TZ)
    labels = LABELS[lang]

    if is_off_season(now):
        return {"state": "closed", "message": labels["pre_booking_only"]}

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
        return {"state": "open", "message": f"{labels['open']} · {labels['last_entry']}"}

    if minutes < open_at:
        return {"state": "closed", "message": labels["opens_at"]}

    return {
        "state": "closed",
        "message": f"{labels['closed']} · {labels['opens_tomorrow']}",
    }
