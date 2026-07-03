/**
 * Reviews carousel — pick a random subset on each visit, shuffle, scroll left/right.
 */
(function () {
  function shuffle(items) {
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [items[i], items[j]] = [items[j], items[i]];
    }
    return items;
  }

  function pickRandomCards(cards, count) {
    return shuffle([...cards]).slice(0, Math.min(count, cards.length));
  }

  function scrollToCard(track, card) {
    if (!card) return;
    const trackRect = track.getBoundingClientRect();
    const cardRect = card.getBoundingClientRect();
    track.scrollLeft += cardRect.left - trackRect.left;
  }

  document.querySelectorAll('[data-reviews-carousel]').forEach((root) => {
    const track = root.querySelector('[data-reviews-track]');
    const prev = root.querySelector('[data-reviews-prev]');
    const next = root.querySelector('[data-reviews-next]');
    if (!track || !prev || !next) return;

    const visibleCount = parseInt(root.dataset.reviewsVisible || '12', 10);
    const allCards = Array.from(track.querySelectorAll('.review-card'));
    const selected = pickRandomCards(allCards, visibleCount);

    allCards.forEach((card) => {
      if (!selected.includes(card)) card.remove();
    });

    shuffle(selected).forEach((card) => track.appendChild(card));
    scrollToCard(track, selected[0]);

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
