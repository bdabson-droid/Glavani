(function () {
  var body = document.body;
  if (!body.classList.contains("home-landing")) return;

  var chrome = document.querySelectorAll(".visit-cta-bar, .quick-actions");
  if (!chrome.length) return;

  function scrollThreshold() {
    return Math.min(96, Math.max(40, Math.round(window.innerHeight * 0.06)));
  }

  function setPastHero(pastHero) {
    body.classList.toggle("home-past-hero", pastHero);
    chrome.forEach(function (el) {
      el.setAttribute("aria-hidden", pastHero ? "false" : "true");
    });
  }

  function update() {
    setPastHero(window.scrollY > scrollThreshold());
  }

  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update, { passive: true });
  update();
})();
