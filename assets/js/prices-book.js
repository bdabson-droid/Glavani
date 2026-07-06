/**
 * Prices page — guest stepper (1–10) updates book links for the booking app.
 */
(function () {
  const MAX_GUESTS = 10;
  const DEFAULT_GUESTS = 2;

  document.querySelectorAll('.price-list__item[data-package-id]').forEach((item) => {
    const packageId = item.dataset.packageId;
    const price = Number(item.dataset.price) || 0;
    const minus = item.querySelector('[data-qty-minus]');
    const plus = item.querySelector('[data-qty-plus]');
    const valueEl = item.querySelector('[data-qty-value]');
    const link = item.querySelector('[data-book-link]');
    const totalEl = item.querySelector('[data-price-total]');
    if (!minus || !plus || !valueEl || !link || !packageId) return;

    let guests = DEFAULT_GUESTS;

    function update() {
      valueEl.textContent = String(guests);
      minus.disabled = guests <= 1;
      plus.disabled = guests >= MAX_GUESTS;

      const url = new URL(link.getAttribute('href'), window.location.href);
      url.searchParams.set('package', packageId);
      url.searchParams.set('guests', String(guests));
      link.href = url.pathname + url.search;

      if (totalEl && price) {
        totalEl.textContent = '€' + price * guests;
      }
    }

    minus.addEventListener('click', () => {
      if (guests > 1) {
        guests -= 1;
        update();
      }
    });

    plus.addEventListener('click', () => {
      if (guests < MAX_GUESTS) {
        guests += 1;
        update();
      }
    });

    update();
  });
})();
