(function () {
  var OPEN = 9;
  var CLOSE = 17;
  var LAST_ENTRY = 15;

  var labels = {
    en: {
      open: "Open now",
      closed: "Closed today",
      opens_at: "Opens at 9 AM",
      last_entry_soon: "Last entry in {minutes} min",
      last_entry: "Last entry 3 PM",
    },
    hr: {
      open: "Otvoreno sada",
      closed: "Zatvoreno danas",
      opens_at: "Otvara se u 9 h",
      last_entry_soon: "Zadnji ulaz za {minutes} min",
      last_entry: "Zadnji ulaz u 15 h",
    },
  };

  function zagrebParts() {
    var parts = new Intl.DateTimeFormat("en-GB", {
      timeZone: "Europe/Zagreb",
      hour: "numeric",
      minute: "numeric",
      hour12: false,
    }).formatToParts(new Date());
    var hour = 0;
    var minute = 0;
    parts.forEach(function (part) {
      if (part.type === "hour") hour = parseInt(part.value, 10);
      if (part.type === "minute") minute = parseInt(part.value, 10);
    });
    return { hour: hour, minute: minute };
  }

  function statusFor(lang) {
    var copy = labels[lang] || labels.en;
    var time = zagrebParts();
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
    return { state: "closed", message: copy.closed };
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
