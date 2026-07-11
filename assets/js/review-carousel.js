/**
 * Homepage review carousel — one guest quote at a time.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('[data-review-carousel]').forEach(function (root) {
    var track = root.querySelector('[data-review-track]');
    var prev = root.querySelector('[data-review-prev]');
    var next = root.querySelector('[data-review-next]');
    var dotsRoot = root.querySelector('[data-review-dots]');
    if (!track || !prev || !next || !dotsRoot) return;

    var slides = Array.from(track.querySelectorAll('.review-carousel__slide'));
    if (!slides.length) return;

    var index = 0;

    slides.forEach(function (_, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'review-carousel__dot';
      dot.setAttribute('role', 'tab');
      dot.setAttribute('aria-label', 'Review ' + (i + 1));
      dot.addEventListener('click', function () {
        goTo(i);
      });
      dotsRoot.appendChild(dot);
    });

    function updateDots() {
      var dots = dotsRoot.querySelectorAll('.review-carousel__dot');
      dots.forEach(function (dot, i) {
        var active = i === index;
        dot.classList.toggle('is-active', active);
        dot.setAttribute('aria-selected', active ? 'true' : 'false');
        dot.setAttribute('tabindex', active ? '0' : '-1');
      });
    }

    function goTo(target) {
      index = (target + slides.length) % slides.length;
      track.style.transform = 'translateX(-' + index * 100 + '%)';
      updateDots();
    }

    prev.addEventListener('click', function () {
      goTo(index - 1);
    });
    next.addEventListener('click', function () {
      goTo(index + 1);
    });

    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        goTo(index - 1);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        goTo(index + 1);
      }
    });

    goTo(0);

    if (!prefersReducedMotion) {
      window.setInterval(function () {
        goTo(index + 1);
      }, 8000);
    }
  });
})();
