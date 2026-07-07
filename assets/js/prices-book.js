/**
 * Prices & activities pages — guest steppers and booking prefill.
 */
(function () {
  const STORAGE_KEY = 'glavani-book-prefill';
  const MAX_GUESTS = 6;
  const DEFAULT_GUESTS = 1;
  const WHOLE_PARK_CATAPULT_ID = 'all-incl-catapult';
  const SMALL_GROUP_BY_SIZE = {
    3: 'whole-park-group-3',
    4: 'whole-park-group-4',
    5: 'whole-park-group-5',
    6: 'whole-park-group-6',
  };
  const SMALL_GROUP_PRICES = {
    3: 180,
    4: 230,
    5: 270,
    6: 300,
  };

  function smallGroupPackageForParty(packageId, totalGuests) {
    if (packageId !== WHOLE_PARK_CATAPULT_ID || totalGuests < 3) return packageId;
    return SMALL_GROUP_BY_SIZE[totalGuests] || packageId;
  }

  function getItem(el) {
    return el.closest('.price-list__item');
  }

  function hasChildPrice(item) {
    return item.hasAttribute('data-has-child-price');
  }

  function readGuests(item) {
    const n = parseInt(item.dataset.guests || String(DEFAULT_GUESTS), 10);
    if (Number.isNaN(n)) return DEFAULT_GUESTS;
    return Math.min(MAX_GUESTS, Math.max(1, n));
  }

  function readAdults(item) {
    const n = parseInt(item.dataset.adults || '1', 10);
    if (Number.isNaN(n)) return 1;
    return Math.min(MAX_GUESTS, Math.max(0, n));
  }

  function readChildren(item) {
    const n = parseInt(item.dataset.children || '0', 10);
    if (Number.isNaN(n)) return 0;
    return Math.min(MAX_GUESTS, Math.max(0, n));
  }

  function writeGuests(item, guests) {
    const count = Math.min(MAX_GUESTS, Math.max(1, guests));
    item.dataset.guests = String(count);
    const valueEl = item.querySelector('[data-qty-value]');
    const minus = item.querySelector('[data-qty-minus]');
    const plus = item.querySelector('[data-qty-plus]');
    if (valueEl) valueEl.textContent = String(count);
    if (minus) minus.disabled = count <= 1;
    if (plus) plus.disabled = count >= MAX_GUESTS;
    updateAutoSmallGroupNote(item);
    return count;
  }

  function writeSplitGuests(item, adults, children) {
    let a = Math.max(0, adults);
    let c = Math.max(0, children);

    if (a + c > MAX_GUESTS) {
      if (c > MAX_GUESTS - a) c = Math.max(0, MAX_GUESTS - a);
      if (a + c > MAX_GUESTS) a = Math.max(0, MAX_GUESTS - c);
    }

    item.dataset.adults = String(a);
    item.dataset.children = String(c);

    const adultsVal = item.querySelector('[data-qty-adults-value]');
    const childrenVal = item.querySelector('[data-qty-children-value]');
    const adultsMinus = item.querySelector('[data-qty-adults-minus]');
    const adultsPlus = item.querySelector('[data-qty-adults-plus]');
    const childrenMinus = item.querySelector('[data-qty-children-minus]');
    const childrenPlus = item.querySelector('[data-qty-children-plus]');

    if (adultsVal) adultsVal.textContent = String(a);
    if (childrenVal) childrenVal.textContent = String(c);
    if (adultsMinus) adultsMinus.disabled = a <= 0 || (a <= 1 && c === 0);
    if (adultsPlus) adultsPlus.disabled = a + c >= MAX_GUESTS;
    if (childrenMinus) childrenMinus.disabled = c <= 0 || (c <= 1 && a === 0);
    if (childrenPlus) childrenPlus.disabled = a + c >= MAX_GUESTS;

    updateAutoSmallGroupNote(item);
    return { adults: a, children: c };
  }

  function isFlatPrice(item) {
    return item.hasAttribute('data-flat-price');
  }

  function fixedGuests(item) {
    return parseInt(item.dataset.fixedGuests || '0', 10);
  }

  function formatAutoHint(template, n, total) {
    return template.replace('{n}', String(n)).replace('{total}', String(total));
  }

  function updateAutoSmallGroupNote(item) {
    if (!item || !item.hasAttribute('data-auto-small-group')) return;
    const note = item.querySelector('[data-auto-small-group-note]');
    if (!note) return;
    const template = item.dataset.autoSmallGroupHint;
    if (!template) return;

    const totalGuests = hasChildPrice(item)
      ? readAdults(item) + readChildren(item)
      : readGuests(item);
    const groupPrice = SMALL_GROUP_PRICES[totalGuests];

    if (groupPrice) {
      note.textContent = formatAutoHint(template, totalGuests, groupPrice);
      note.hidden = false;
    } else {
      note.textContent = '';
      note.hidden = true;
    }
  }

  function initItems() {
    document.querySelectorAll('.price-list__item').forEach((item) => {
      if (!item.querySelector('[data-book-package]')) return;
      if (isFlatPrice(item)) return;
      if (hasChildPrice(item)) {
        writeSplitGuests(item, readAdults(item), readChildren(item));
      } else {
        writeGuests(item, readGuests(item));
      }
      updateAutoSmallGroupNote(item);
    });
  }

  document.addEventListener('click', (e) => {
    const minus = e.target.closest('[data-qty-minus]');
    if (minus) {
      e.preventDefault();
      const item = getItem(minus);
      if (item) writeGuests(item, readGuests(item) - 1);
      return;
    }

    const plus = e.target.closest('[data-qty-plus]');
    if (plus) {
      e.preventDefault();
      const item = getItem(plus);
      if (item) writeGuests(item, readGuests(item) + 1);
      return;
    }

    const adultsMinus = e.target.closest('[data-qty-adults-minus]');
    if (adultsMinus) {
      e.preventDefault();
      const item = getItem(adultsMinus);
      if (item) writeSplitGuests(item, readAdults(item) - 1, readChildren(item));
      return;
    }

    const adultsPlus = e.target.closest('[data-qty-adults-plus]');
    if (adultsPlus) {
      e.preventDefault();
      const item = getItem(adultsPlus);
      if (item) writeSplitGuests(item, readAdults(item) + 1, readChildren(item));
      return;
    }

    const childrenMinus = e.target.closest('[data-qty-children-minus]');
    if (childrenMinus) {
      e.preventDefault();
      const item = getItem(childrenMinus);
      if (item) writeSplitGuests(item, readAdults(item), readChildren(item) - 1);
      return;
    }

    const childrenPlus = e.target.closest('[data-qty-children-plus]');
    if (childrenPlus) {
      e.preventDefault();
      const item = getItem(childrenPlus);
      if (item) writeSplitGuests(item, readAdults(item), readChildren(item) + 1);
      return;
    }

    const book = e.target.closest('[data-book-package]');
    if (!book) return;

    const packageId = book.dataset.bookPackage;
    const item = getItem(book);
    if (!packageId || !item) return;

    try {
      let payload = { package: packageId };
      if (isFlatPrice(item)) {
        payload.guests = fixedGuests(item);
      } else if (hasChildPrice(item)) {
        const adults = readAdults(item);
        const children = readChildren(item);
        const total = adults + children;
        payload.package = smallGroupPackageForParty(packageId, total);
        if (payload.package === packageId) {
          payload.adults = adults;
          payload.children = children;
        }
      } else {
        const guests = readGuests(item);
        payload.package = smallGroupPackageForParty(packageId, guests);
        if (payload.package === packageId) {
          payload.guests = guests;
        }
      }
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
    } catch (err) {
      /* ignore */
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initItems);
  } else {
    initItems();
  }
})();
