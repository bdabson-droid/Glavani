/**
 * Reviews carousel — favour recent reviews, pick 12 at random, shuffle, scroll.
 */
(function () {
  const HALF_LIFE_DAYS = 540;
  const MIN_WEIGHT = 0.12;

  function shuffle(items) {
    for (let i = items.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [items[i], items[j]] = [items[j], items[i]];
    }
    return items;
  }

  function recencyWeight(dateStr) {
    if (!dateStr) return 1;
    const ageDays = (Date.now() - new Date(dateStr).getTime()) / (1000 * 60 * 60 * 24);
    if (ageDays <= 0) return 1;
    return Math.max(MIN_WEIGHT, Math.pow(0.5, ageDays / HALF_LIFE_DAYS));
  }

  function pickWeightedCards(cards, count) {
    const pool = [...cards];
    const picked = [];
    const limit = Math.min(count, pool.length);

    while (picked.length < limit && pool.length) {
      const weights = pool.map((card) => recencyWeight(card.dataset.reviewDate));
      const total = weights.reduce((sum, weight) => sum + weight, 0);
      let roll = Math.random() * total;
      let index = 0;

      for (let i = 0; i < pool.length; i++) {
        roll -= weights[i];
        if (roll <= 0) {
          index = i;
          break;
        }
      }

      picked.push(pool.splice(index, 1)[0]);
    }

    return picked;
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
    const selected = pickWeightedCards(allCards, visibleCount);

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
