/**
 * Glavani Park gift voucher checkout — posts to legacy glavanipark.com/payment.
 */
(function () {
  const root = document.getElementById('gift-voucher-checkout');
  if (!root) return;

  const configEl = document.getElementById('gift-voucher-config');
  if (!configEl) return;

  let config;
  try {
    config = JSON.parse(configEl.textContent);
  } catch (e) {
    return;
  }

  const copy = config.copy;
  const lang = config.lang === 'hr' ? 'hr' : 'en';
  const maxQty = 99;
  const quantities = {};
  config.vouchers.forEach(function (v) {
    quantities[v.id] = 0;
  });

  const params = new URLSearchParams(window.location.search);
  const preselect = params.get('v');
  if (preselect && Object.prototype.hasOwnProperty.call(quantities, preselect)) {
    quantities[preselect] = 1;
  }

  function todayIso() {
    const d = new Date();
    const m = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return d.getFullYear() + '-' + m + '-' + day;
  }

  function formatMoney(amount) {
    const n = Number(amount);
    if (Number.isNaN(n)) return lang === 'hr' ? '0 €' : '€0';
    const fixed = n.toFixed(2);
    return lang === 'hr' ? fixed.replace('.00', '') + ' €' : '€' + fixed.replace(/\.00$/, '');
  }

  function lineTotal(voucher) {
    return voucher.price * quantities[voucher.id];
  }

  function subtotal() {
    return config.vouchers.reduce(function (sum, v) {
      return sum + lineTotal(v);
    }, 0);
  }

  function activeItems() {
    return config.vouchers.filter(function (v) {
      return quantities[v.id] > 0;
    });
  }

  function legacyQuantities() {
    const byField = {};
    config.legacySlots.forEach(function (slot) {
      byField[slot.field] = 0;
    });
    config.vouchers.forEach(function (v) {
      byField[v.legacyField] = quantities[v.id];
    });
    return byField;
  }

  function serializeQuantity() {
    let out = '';
    config.legacySlots.forEach(function (slot) {
      const qty = legacyQuantities()[slot.field] || 0;
      if (qty > 0) {
        out += slot.pk + ':' + qty + ';';
      }
    });
    return out;
  }

  function buildCalculateBody(totalAmount) {
    const parts = ['date=' + encodeURIComponent(todayIso())];
    let i = 0;
    config.legacySlots.forEach(function (slot) {
      const qty = legacyQuantities()[slot.field] || 0;
      if (qty > 0) {
        parts.push('params[' + i + '][pk]=' + encodeURIComponent(slot.pk));
        parts.push('params[' + i + '][value]=' + encodeURIComponent(String(qty)));
        i += 1;
      }
    });
    const email = root.querySelector('[name="bEmail"]');
    if (email && email.value.trim()) {
      parts.push('customer[0][fieldName]=bEmail');
      parts.push('customer[0][value]=' + encodeURIComponent(email.value.trim()));
    }
    return parts.join('&');
  }

  let displayedTotal = 0;
  let calculating = false;

  function fallbackTotal() {
    return subtotal();
  }

  function updateTotals() {
    const totalEl = root.querySelector('[data-total]');
    const sub = subtotal();
    if (sub === 0) {
      displayedTotal = 0;
      if (totalEl) totalEl.textContent = formatMoney(0);
      root.querySelectorAll('[data-line-total]').forEach(function (el) {
        const id = el.getAttribute('data-line-total');
        const voucher = config.vouchers.find(function (v) { return v.id === id; });
        if (voucher) el.textContent = formatMoney(0);
      });
      return;
    }

    displayedTotal = fallbackTotal();
    if (totalEl) totalEl.textContent = formatMoney(displayedTotal);

    config.vouchers.forEach(function (voucher) {
      const el = root.querySelector('[data-line-total="' + voucher.id + '"]');
      if (el) el.textContent = formatMoney(lineTotal(voucher));
    });

    if (calculating) return;
    calculating = true;
    fetch(config.calculateUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: buildCalculateBody(sub),
    })
      .then(function (res) {
        if (!res.ok) throw new Error('calculate failed');
        return res.json();
      })
      .then(function (data) {
        if (data && data.type === 'success' && data.total != null) {
          displayedTotal = parseFloat(data.total, 10);
          if (totalEl) totalEl.textContent = formatMoney(displayedTotal);
        }
      })
      .catch(function () {
        /* keep client-side fallback */
      })
      .finally(function () {
        calculating = false;
      });
  }

  function setQty(id, next) {
    const clamped = Math.max(0, Math.min(maxQty, next));
    quantities[id] = clamped;
    const input = root.querySelector('[data-qty-input="' + id + '"]');
    if (input) input.value = String(clamped);
    const minus = root.querySelector('[data-qty-minus="' + id + '"]');
    if (minus) minus.disabled = clamped <= 0;
    updateTotals();
  }

  function render() {
    const voucherRows = config.vouchers.map(function (voucher) {
      const qty = quantities[voucher.id];
      return (
        '<article class="voucher-checkout-item" data-voucher="' + voucher.id + '">' +
          '<img class="voucher-checkout-item__thumb" src="' + voucher.image + '" alt="" width="80" height="56" loading="lazy">' +
          '<div class="voucher-checkout-item__info">' +
            '<h3 class="voucher-checkout-item__name">' + voucher.name + '</h3>' +
            '<p class="voucher-checkout-item__package">' + voucher.package + '</p>' +
            '<p class="voucher-checkout-item__unit">' + copy.each.replace('{price}', String(voucher.price)) + '</p>' +
          '</div>' +
          '<div class="voucher-checkout-item__qty">' +
            '<button type="button" class="qty-btn" data-qty-minus="' + voucher.id + '" aria-label="−"' + (qty <= 0 ? ' disabled' : '') + '>−</button>' +
            '<input type="number" class="qty-input" data-qty-input="' + voucher.id + '" value="' + qty + '" min="0" max="' + maxQty + '" inputmode="numeric" aria-label="' + voucher.name + '">' +
            '<button type="button" class="qty-btn" data-qty-plus="' + voucher.id + '" aria-label="+">+</button>' +
          '</div>' +
          '<p class="voucher-checkout-item__total" data-line-total="' + voucher.id + '">' + formatMoney(lineTotal(voucher)) + '</p>' +
        '</article>'
      );
    }).join('');

    root.innerHTML =
      '<form class="voucher-checkout-form booking-form" action="' + config.paymentUrl + '" method="post" novalidate>' +
        '<input type="hidden" name="omb" value="-1">' +
        '<input type="hidden" name="validator" value="0">' +
        '<input type="hidden" name="selectedLanguage" value="' + lang + '">' +
        '<input type="hidden" name="bTotalWithDiscount" value="0">' +
        '<input type="hidden" name="quantity" value="">' +
        config.legacySlots.map(function (slot) {
          return '<input type="hidden" name="' + slot.field + '" data-legacy-field="' + slot.field + '" value="0">';
        }).join('') +
        '<section class="voucher-checkout-section">' +
          '<h2 class="voucher-checkout-section__title">' + copy.packages_heading + '</h2>' +
          '<div class="voucher-checkout-list">' + voucherRows + '</div>' +
        '</section>' +
        '<section class="voucher-checkout-section">' +
          '<h2 class="voucher-checkout-section__title">' + copy.details_heading + '</h2>' +
          '<div class="booking-form__row">' +
            '<div><label for="bFirstName">' + copy.first_name + ' *</label><input id="bFirstName" name="bFirstName" type="text" required autocomplete="given-name"></div>' +
            '<div><label for="bLastName">' + copy.last_name + ' *</label><input id="bLastName" name="bLastName" type="text" required autocomplete="family-name"></div>' +
          '</div>' +
          '<div><label for="bAddress">' + copy.address + ' *</label><input id="bAddress" name="bAddress" type="text" required autocomplete="street-address"></div>' +
          '<div class="booking-form__row">' +
            '<div><label for="bZip">' + copy.zip + ' *</label><input id="bZip" name="bZip" type="text" required autocomplete="postal-code"></div>' +
            '<div><label for="bCity">' + copy.city + ' *</label><input id="bCity" name="bCity" type="text" required autocomplete="address-level2"></div>' +
          '</div>' +
          '<div><label for="bCountry">' + copy.country + '</label><input id="bCountry" name="bCountry" type="text" autocomplete="country-name"></div>' +
          '<div class="booking-form__row">' +
            '<div><label for="bPhone">' + copy.phone + ' *</label><input id="bPhone" name="bPhone" type="tel" required autocomplete="tel"></div>' +
            '<div><label for="bEmail">' + copy.email + ' *</label><input id="bEmail" name="bEmail" type="email" required autocomplete="email"></div>' +
          '</div>' +
          '<div><label for="napomena">' + copy.comments + '</label><textarea id="napomena" name="napomena" rows="4" placeholder="' + copy.comments_ph + '"></textarea></div>' +
        '</section>' +
        '<div class="voucher-checkout-total">' +
          '<p class="voucher-checkout-total__label">' + copy.total + '</p>' +
          '<p class="voucher-checkout-total__amount" data-total>' + formatMoney(0) + '</p>' +
        '</div>' +
        '<p class="voucher-checkout-error" data-error hidden></p>' +
        '<button type="submit" class="btn-primary voucher-checkout-submit">' + copy.submit + '</button>' +
      '</form>';

    root.querySelectorAll('[data-qty-minus]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const id = btn.getAttribute('data-qty-minus');
        setQty(id, quantities[id] - 1);
      });
    });
    root.querySelectorAll('[data-qty-plus]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const id = btn.getAttribute('data-qty-plus');
        setQty(id, quantities[id] + 1);
      });
    });
    root.querySelectorAll('[data-qty-input]').forEach(function (input) {
      input.addEventListener('change', function () {
        const id = input.getAttribute('data-qty-input');
        const val = parseInt(input.value, 10);
        setQty(id, Number.isNaN(val) ? 0 : val);
      });
    });

    const form = root.querySelector('form');
    form.addEventListener('submit', function (e) {
      const errorEl = root.querySelector('[data-error]');
      function showError(msg) {
        if (errorEl) {
          errorEl.textContent = msg;
          errorEl.hidden = false;
        }
      }

      if (activeItems().length === 0) {
        e.preventDefault();
        showError(copy.select_one);
        return;
      }

      const required = ['bFirstName', 'bLastName', 'bAddress', 'bZip', 'bCity', 'bPhone', 'bEmail'];
      for (let i = 0; i < required.length; i += 1) {
        const field = form.elements[required[i]];
        if (!field || !String(field.value).trim()) {
          e.preventDefault();
          showError(copy.fill_required);
          field && field.focus();
          return;
        }
      }

      const email = String(form.elements.bEmail.value).trim();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        e.preventDefault();
        showError(copy.invalid_email);
        form.elements.bEmail.focus();
        return;
      }

      if (errorEl) errorEl.hidden = true;

      const legacy = legacyQuantities();
      config.legacySlots.forEach(function (slot) {
        const input = form.querySelector('[data-legacy-field="' + slot.field + '"]');
        if (input) input.value = String(legacy[slot.field] || 0);
      });

      form.elements.quantity.value = serializeQuantity();
      form.elements.bTotalWithDiscount.value = displayedTotal > 0 ? displayedTotal.toFixed(2) : subtotal().toFixed(2);
      form.elements.omb.value = '0';
      form.elements.validator.value = '1';
    });

    const emailInput = root.querySelector('[name="bEmail"]');
    if (emailInput) {
      emailInput.addEventListener('blur', updateTotals);
    }

    updateTotals();
  }

  render();
})();
