/**
 * Homepage review carousel — swipe, arrows, dots, and keyboard.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var SWIPE_THRESHOLD = 48;

  document.querySelectorAll('[data-review-carousel]').forEach(function (root) {
    var viewport = root.querySelector('.review-carousel__viewport');
    var track = root.querySelector('[data-review-track]');
    var prev = root.querySelector('[data-review-prev]');
    var next = root.querySelector('[data-review-next]');
    var dotsRoot = root.querySelector('[data-review-dots]');
    if (!viewport || !track || !prev || !next || !dotsRoot) return;

    var slides = Array.from(track.querySelectorAll('.review-carousel__slide'));
    if (!slides.length) return;

    var index = 0;
    var autoplayTimer = null;
    var pointerStartX = 0;
    var pointerStartY = 0;
    var pointerActive = false;

    slides.forEach(function (_, i) {
      var dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'review-carousel__dot';
      dot.setAttribute('role', 'tab');
      dot.setAttribute('aria-label', 'Review ' + (i + 1));
      dot.addEventListener('click', function () {
        goTo(i);
        restartAutoplay();
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

    function stopAutoplay() {
      if (autoplayTimer) {
        window.clearInterval(autoplayTimer);
        autoplayTimer = null;
      }
    }

    function startAutoplay() {
      if (prefersReducedMotion || slides.length < 2) return;
      stopAutoplay();
      autoplayTimer = window.setInterval(function () {
        goTo(index + 1);
      }, 8000);
    }

    function restartAutoplay() {
      stopAutoplay();
      startAutoplay();
    }

    prev.addEventListener('click', function () {
      goTo(index - 1);
      restartAutoplay();
    });
    next.addEventListener('click', function () {
      goTo(index + 1);
      restartAutoplay();
    });

    root.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        goTo(index - 1);
        restartAutoplay();
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        goTo(index + 1);
        restartAutoplay();
      }
    });

    function onPointerDown(e) {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      pointerActive = true;
      pointerStartX = e.clientX;
      pointerStartY = e.clientY;
      viewport.classList.add('is-dragging');
      if (viewport.setPointerCapture) {
        viewport.setPointerCapture(e.pointerId);
      }
      stopAutoplay();
    }

    function onPointerUp(e) {
      if (!pointerActive) return;
      pointerActive = false;
      viewport.classList.remove('is-dragging');
      if (viewport.releasePointerCapture) {
        try {
          viewport.releasePointerCapture(e.pointerId);
        } catch (err) {
          /* ignore if capture was already released */
        }
      }

      var deltaX = e.clientX - pointerStartX;
      var deltaY = e.clientY - pointerStartY;
      if (Math.abs(deltaX) >= SWIPE_THRESHOLD && Math.abs(deltaX) > Math.abs(deltaY)) {
        goTo(deltaX < 0 ? index + 1 : index - 1);
      }
      restartAutoplay();
    }

    viewport.addEventListener('pointerdown', onPointerDown);
    viewport.addEventListener('pointerup', onPointerUp);
    viewport.addEventListener('pointercancel', onPointerUp);

    goTo(0);
    startAutoplay();
  });
})();
