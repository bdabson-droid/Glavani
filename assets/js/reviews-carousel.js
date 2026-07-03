/**
 * Horizontal reviews carousel — scroll left/right with buttons and keyboard.
 */
(function () {
  document.querySelectorAll('[data-reviews-carousel]').forEach((root) => {
    const track = root.querySelector('[data-reviews-track]');
    const prev = root.querySelector('[data-reviews-prev]');
    const next = root.querySelector('[data-reviews-next]');
    if (!track || !prev || !next) return;

    function scrollStep() {
      const card = track.querySelector('.review-card');
      if (!card) return track.clientWidth * 0.85;
      const gap = parseFloat(getComputedStyle(track).gap) || 16;
      return card.offsetWidth + gap;
    }

    function scrollBy(direction) {
      track.scrollBy({ left: direction * scrollStep(), behavior: 'smooth' });
    }

    prev.addEventListener('click', () => scrollBy(-1));
    next.addEventListener('click', () => scrollBy(1));

    track.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        e.preventDefault();
        scrollBy(-1);
      } else if (e.key === 'ArrowRight') {
        e.preventDefault();
        scrollBy(1);
      }
    });
  });
})();
