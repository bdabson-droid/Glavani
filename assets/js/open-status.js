(function () {
  var OPEN = 9;
  var CLOSE = 17;
  var LAST_ENTRY = 15;
  var OFF_SEASON_MONTHS = { 1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 10: true, 11: true, 12: true };

  var labels = {
    en: {
      open: "Open now",
      closed: "Closed now",
      opens_tomorrow: "Opens tomorrow at 9 AM",
      opens_at: "Opens at 9 AM",
      last_entry_soon: "Last entry in {minutes} min",
      last_entry: "Last entry 3 PM",
      pre_booking_only: "Pre-booking only",
    },
    hr: {
      open: "Otvoreno sada",
      closed: "Zatvoreno sada",
      opens_tomorrow: "Otvara se sutra u 9 h",
      opens_at: "Otvara se u 9 h",
      last_entry_soon: "Zadnji ulaz za {minutes} min",
      last_entry: "Zadnji ulaz u 15 h",
      pre_booking_only: "Samo unaprijedna rezervacija",
    },
  };

  function zagrebParts() {
    var parts = new Intl.DateTimeFormat("en-GB", {
      timeZone: "Europe/Zagreb",
      hour: "numeric",
      minute: "numeric",
      month: "numeric",
      hour12: false,
    }).formatToParts(new Date());
    var hour = 0;
    var minute = 0;
    var month = 0;
    parts.forEach(function (part) {
      if (part.type === "hour") hour = parseInt(part.value, 10);
      if (part.type === "minute") minute = parseInt(part.value, 10);
      if (part.type === "month") month = parseInt(part.value, 10);
    });
    return { hour: hour, minute: minute, month: month };
  }

  function statusFor(lang) {
    var copy = labels[lang] || labels.en;
    var time = zagrebParts();

    if (OFF_SEASON_MONTHS[time.month]) {
      return { state: "closed", message: copy.pre_booking_only };
    }

    var minutes = time.hour * 60 + time.minute;
    var openAt = OPEN * 60;
    var closeAt = CLOSE * 60;
    var lastEntryAt = LAST_ENTRY * 60;

    if (minutes >= openAt && minutes < lastEntryAt) {
      var minsLeft = lastEntryAt - minutes;
      if (minsLeft <= 60) {
        return { state: "open", message: copy.last_entry_soon.replace("{minutes}", String(minsLeft)) };
      }
      return { state: "open", message: copy.open + " · " + copy.last_entry };
    }
    if (minutes >= lastEntryAt && minutes < closeAt) {
      return { state: "open", message: copy.open + " · " + copy.last_entry };
    }
    if (minutes < openAt) {
      return { state: "closed", message: copy.opens_at };
    }
    return { state: "closed", message: copy.closed + " · " + copy.opens_tomorrow };
  }

  function update() {
    document.querySelectorAll("[data-open-status]").forEach(function (el) {
      var lang = el.getAttribute("data-lang") || "en";
      var result = statusFor(lang);
      el.textContent = result.message;
      var statusEl = el.closest(".visitor-bar__status, .visit-cta-bar__status");
      if (statusEl) {
        statusEl.classList.remove("visitor-bar__status--open", "visitor-bar__status--closed");
        statusEl.classList.add("visitor-bar__status--" + result.state);
      }
      el.classList.remove("hero__open-status--open", "hero__open-status--closed");
      el.classList.add("hero__open-status--" + result.state);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", update);
  } else {
    update();
  }
  setInterval(update, 60000);
})();
