(function () {
  var body = document.body;
  if (!body.classList.contains("home-landing")) return;

  var chrome = document.querySelectorAll(".visit-cta-bar, .quick-actions");
  if (!chrome.length) return;

  var visible = false;
  var ticking = false;

  function thresholds() {
    var showAt = Math.min(20, Math.max(6, Math.round(window.innerHeight * 0.015)));
    var hideAt = 0;
    return { showAt: showAt, hideAt: hideAt };
  }

  function setPastHero(pastHero) {
    if (visible === pastHero) return;
    visible = pastHero;
    body.classList.toggle("home-past-hero", pastHero);
    chrome.forEach(function (el) {
      el.setAttribute("aria-hidden", pastHero ? "false" : "true");
    });
  }

  function update() {
    var y = window.scrollY;
    var limits = thresholds();
    if (!visible && y > limits.showAt) {
      setPastHero(true);
    } else if (visible && y <= limits.hideAt) {
      setPastHero(false);
    }
  }

  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      update();
      ticking = false;
    });
  }

  var scrollLink = document.querySelector(".site-header__scroll");
  if (scrollLink) {
    scrollLink.addEventListener("click", function () {
      setPastHero(true);
    });
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  update();
})();
