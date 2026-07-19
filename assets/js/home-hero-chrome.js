(function () {
  var body = document.body;
  if (!body.classList.contains("home-landing")) return;

  var chrome = document.querySelectorAll(".visit-cta-bar, .quick-actions");
  if (!chrome.length) return;

  var visible = false;
  var ticking = false;

  function scrollTop() {
    return (
      window.scrollY ||
      document.documentElement.scrollTop ||
      document.body.scrollTop ||
      0
    );
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
    var y = scrollTop();
    if (!visible && y > 0) {
      setPastHero(true);
    } else if (visible && y <= 0) {
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

  function onScrollIntent() {
    if (!visible) {
      setPastHero(true);
    }
  }

  var scrollLink = document.querySelector(".site-header__scroll");
  if (scrollLink) {
    scrollLink.addEventListener("click", function () {
      setPastHero(true);
    });
  }

  chrome.forEach(function (el) {
    el.setAttribute("aria-hidden", "true");
  });

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  window.addEventListener(
    "wheel",
    function (event) {
      if (!visible && event.deltaY !== 0) {
        onScrollIntent();
      }
    },
    { passive: true }
  );
  window.addEventListener("touchmove", onScrollIntent, { passive: true });
  update();
})();
