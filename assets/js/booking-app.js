/**
 * Glavani Park Booking App — package & guest dropdowns, live pricing.
 * Groups of 7+ must call. No email — WhatsApp, SMS, or phone.
 */
(function () {
  const root = document.getElementById('booking-app');
  if (!root) return;

  const MAX_GUESTS = 6;
  const lang = document.documentElement.lang?.startsWith('hr') ? 'hr' : 'en';
  const PHONE_EN = '385918964525';
  const PHONE_HR = '38598224314';
  const STORAGE_KEY = 'glavani-park-bookings';

  const i18n = {
    en: {
      steps: ['Package', 'Date', 'Details', 'Confirm'],
      activities: [
        { id: 'training-2', group: 'packages', name: 'Training route + 2 games', price: 30 },
        { id: 'catapult-swing', group: 'packages', name: 'Human catapult + 12.5 m swing', price: 50 },
        { id: 'all-no-catapult', group: 'packages', name: 'Whole park — all games (without catapult)', price: 50 },
        { id: 'all-incl-catapult', group: 'packages', name: 'Whole park — all games incl. human catapult', price: 70 },
        { id: 'human-catapult', group: 'single', name: 'Human Catapult', price: 40 },
      ],
      groupPackages: 'Activity packages',
      groupSingle: 'Single activities',
      months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
      days: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      pickActivity: 'Choose your package or activity',
      pickActivityLead: 'Packages first, then single activities · max 6 people online',
      selectPackage: 'Select a package or activity…',
      selectGuests: 'Number of people',
      guestsOption: '{n} person',
      guestsOptionPlural: '{n} people',
      guestsOption7Plus: '7 or more people — please call',
      callInsteadTitle: 'Groups of 7 or more',
      callInsteadLead: 'Please call us so we can check availability and accommodate your party.',
      callToBook: 'Call to book your group',
      priceEach: '€{price} per person',
      total: 'Total',
      pickDate: 'Pick your visit date',
      pickDateLead: 'Open daily 9 AM–5 PM · last entry 3 PM',
      yourDetails: 'Your details',
      confirmTitle: 'Confirm booking',
      confirmLead: 'Send your request via WhatsApp or SMS — no email needed',
      name: 'Your name',
      phone: 'Your phone number',
      guestsHint: 'Groups of 7 or more must call to book.',
      arrival: 'Preferred start time',
      arrivalLead: '15-minute slots · your preferred start time · park open 9 AM–5 PM · last entry 3 PM',
      notes: 'Notes (optional)',
      notesPh: 'Any special requests…',
      next: 'Next',
      back: 'Back',
      summary: 'Booking summary',
      package: 'Package',
      date: 'Date',
      guests: 'Number of guests',
      pricePerPerson: 'Price per person',
      whatsapp: 'Send via WhatsApp',
      sms: 'Send SMS',
      call: 'Call to confirm',
      copy: 'Copy details',
      copied: 'Copied to clipboard!',
      selectActivity: 'Please select a package or activity.',
      selectDate: 'Please select a visit date.',
      fillRequired: 'Please enter your name and phone number.',
      tooManyGuests: 'Online booking is for up to 6 people only. Please call to book larger groups:',
      myDiary: 'My booking diary',
      myDiaryLead: 'Saved on this device',
      emptyDiary: 'No saved bookings yet.',
      tabBook: 'Book',
      tabDiary: 'My diary',
      parkHours: 'Confirm on arrival · park open 9 AM – 5 PM',
      msgHeader: 'Glavani Park booking request',
      callGroups: 'Call for groups of 7+',
    },
    hr: {
      steps: ['Paket', 'Datum', 'Podaci', 'Potvrda'],
      activities: [
        { id: 'training-2', group: 'packages', name: 'Trening ruta + 2 igre', price: 30 },
        { id: 'catapult-swing', group: 'packages', name: 'Ljudska katapulta + ljuljačka 12,5 m', price: 50 },
        { id: 'all-no-catapult', group: 'packages', name: 'Cijeli park — sve igre (bez katapulata)', price: 50 },
        { id: 'all-incl-catapult', group: 'packages', name: 'Cijeli park — sve igre uklj. katapultu', price: 70 },
        { id: 'human-catapult', group: 'single', name: 'Ljudska katapulta', price: 40 },
      ],
      groupPackages: 'Paketi aktivnosti',
      groupSingle: 'Pojedinačne aktivnosti',
      months: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
      days: ['Pon','Uto','Sri','Čet','Pet','Sub','Ned'],
      pickActivity: 'Odaberite paket ili aktivnost',
      pickActivityLead: 'Prvo paketi, zatim pojedinačne aktivnosti · max 6 osoba online',
      selectPackage: 'Odaberite paket ili aktivnost…',
      selectGuests: 'Broj osoba',
      guestsOption: '{n} osoba',
      guestsOptionPlural: '{n} osobe',
      guestsOption7Plus: '7 ili više osoba — nazovite',
      callInsteadTitle: 'Grupe od 7 i više osoba',
      callInsteadLead: 'Nazovite nas kako bismo provjerili dostupnost i mogli ugostiti vašu grupu.',
      callToBook: 'Pozovite za rezervaciju grupe',
      priceEach: '€{price} po osobi',
      total: 'Ukupno',
      pickDate: 'Odaberite datum posjeta',
      pickDateLead: 'Otvoreno 9–17 h · zadnji ulaz 15 h',
      yourDetails: 'Vaši podaci',
      confirmTitle: 'Potvrdite rezervaciju',
      confirmLead: 'Pošaljite WhatsAppom ili SMS-om — bez e-maila',
      name: 'Ime i prezime',
      phone: 'Broj telefona',
      guestsHint: 'Grupe od 7 i više osoba moraju rezervirati telefonom.',
      arrival: 'Preferirano vrijeme početka',
      arrivalLead: 'Termini od 15 min · željeno vrijeme početka · park 9–17 h · zadnji ulaz 15 h',
      notes: 'Napomena (opcionalno)',
      notesPh: 'Posebni zahtjevi…',
      next: 'Dalje',
      back: 'Natrag',
      summary: 'Sažetak rezervacije',
      package: 'Paket',
      date: 'Datum',
      guests: 'Broj gostiju',
      pricePerPerson: 'Cijena po osobi',
      whatsapp: 'Pošalji WhatsApp',
      sms: 'Pošalji SMS',
      call: 'Pozovi za potvrdu',
      copy: 'Kopiraj detalje',
      copied: 'Kopirano!',
      selectActivity: 'Odaberite paket ili aktivnost.',
      selectDate: 'Odaberite datum posjeta.',
      fillRequired: 'Unesite ime i telefon.',
      tooManyGuests: 'Online rezervacija je za najviše 6 osoba. Za veće grupe nazovite:',
      myDiary: 'Moj dnevnik rezervacija',
      myDiaryLead: 'Spremljeno na ovom uređaju',
      emptyDiary: 'Još nema spremljenih rezervacija.',
      tabBook: 'Rezerviraj',
      tabDiary: 'Dnevnik',
      parkHours: 'Potvrda na ulazu · park 9–17 h',
      msgHeader: 'Zahtjev za rezervaciju Glavani Park',
      callGroups: 'Pozovite za grupe 7+',
    },
  };
  const t = i18n[lang];
  const phone = lang === 'hr' ? PHONE_HR : PHONE_EN;

  const ARRIVAL_START = 9 * 60;
  const ARRIVAL_END = 15 * 60;

  function pad(n) { return String(n).padStart(2, '0'); }

  function formatArrivalLabel(h, m) {
    if (lang === 'hr') return `${pad(h)}:${pad(m)}`;
    const hour12 = h % 12 || 12;
    const ampm = h < 12 ? 'AM' : 'PM';
    return `${hour12}:${pad(m)} ${ampm}`;
  }

  function buildArrivalSlots() {
    const slots = [];
    for (let minutes = ARRIVAL_START; minutes <= ARRIVAL_END; minutes += 15) {
      const h = Math.floor(minutes / 60);
      const m = minutes % 60;
      slots.push({ minutes, label: formatArrivalLabel(h, m) });
    }
    return slots;
  }

  const arrivalSlots = buildArrivalSlots();

  function arrivalLabel() {
    return arrivalSlots[state.arrival]?.label || arrivalSlots[0].label;
  }

  function renderArrivalOptions() {
    return arrivalSlots.map((slot, i) =>
      `<option value="${i}"${i === state.arrival ? ' selected' : ''}>${slot.label}</option>`
    ).join('');
  }

  let step = 0;
  let selectedActivityId = '';
  let selectedDate = null;
  let viewYear, viewMonth;
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const state = { name: '', phone: '', guests: 2, largeGroup: false, arrival: 0, notes: '' };

  function isoDate(d) { return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; }

  function selectedActivity() {
    return t.activities.find(a => a.id === selectedActivityId) || null;
  }

  function guestCount() {
    if (state.largeGroup) return 0;
    return Math.min(MAX_GUESTS, Math.max(1, parseInt(state.guests, 10) || 1));
  }

  function bookingTotal() {
    const a = selectedActivity();
    if (!a) return 0;
    return a.price * guestCount();
  }

  function guestLabel(n) {
    if (lang === 'hr') {
      return n === 1 ? t.guestsOption.replace('{n}', n) : t.guestsOptionPlural.replace('{n}', n);
    }
    return n === 1 ? t.guestsOption.replace('{n}', n) : t.guestsOptionPlural.replace('{n}', n);
  }

  function renderGuestOptions() {
    let opts = '';
    for (let n = 1; n <= MAX_GUESTS; n++) {
      const selected = !state.largeGroup && guestCount() === n;
      opts += `<option value="${n}"${selected ? ' selected' : ''}>${guestLabel(n)}</option>`;
    }
    opts += `<option value="call"${state.largeGroup ? ' selected' : ''}>${t.guestsOption7Plus}</option>`;
    return opts;
  }

  function renderPackageOptions() {
    const groups = [
      { key: 'packages', label: t.groupPackages },
      { key: 'single', label: t.groupSingle },
    ];
    return groups.map(g => {
      const items = t.activities.filter(a => a.group === g.key);
      if (!items.length) return '';
      return `<optgroup label="${g.label}">${items.map(a =>
        `<option value="${a.id}"${selectedActivityId === a.id ? ' selected' : ''}>${a.name} — €${a.price}/pp</option>`
      ).join('')}</optgroup>`;
    }).join('');
  }

  function renderCallPanel() {
    return `<div class="book-call-panel" id="book-price-box" aria-live="polite">
      <h3>${t.callInsteadTitle}</h3>
      <p>${t.callInsteadLead}</p>
      <a class="btn-call-book" href="tel:+${phone}">${t.callToBook}</a>
      <p class="book-call-panel__number">${lang === 'hr' ? '+385 98 224 314' : '+385 91 896 4525'}</p>
    </div>`;
  }

  function renderPriceBox() {
    if (state.largeGroup) return renderCallPanel();
    const a = selectedActivity();
    const total = bookingTotal();
    if (!a) {
      return `<div class="book-price-box book-price-box--empty" id="book-price-box" aria-live="polite">
        <p>${t.selectPackage}</p>
      </div>`;
    }
    return `<div class="book-price-box" id="book-price-box" aria-live="polite">
      <p class="book-price-box__each">${t.priceEach.replace('{price}', a.price)}</p>
      <p class="book-price-box__total"><span>${t.total}</span> <strong>€${total}</strong></p>
      <p class="book-price-box__meta">${guestCount()} × €${a.price}</p>
    </div>`;
  }

  function updatePriceBox() {
    const box = document.getElementById('book-price-box');
    if (!box) return;
    if (state.largeGroup) {
      box.outerHTML = renderCallPanel();
    } else {
      box.outerHTML = renderPriceBox();
    }
    toggleNextButton();
  }

  function toggleNextButton() {
    const next = document.getElementById('book-next');
    if (!next) return;
    if (state.largeGroup) {
      next.hidden = true;
      next.disabled = true;
    } else {
      next.hidden = false;
      next.disabled = false;
    }
  }

  function buildMessage() {
    const a = selectedActivity();
    const total = bookingTotal();
    return [
      t.msgHeader,
      '---',
      `${t.package}: ${a ? a.name : '—'}`,
      `${t.pricePerPerson}: €${a ? a.price : 0}`,
      `${t.guests}: ${guestCount()}`,
      `${t.total}: €${total}`,
      `${t.date}: ${selectedDate}`,
      `${t.arrival}: ${arrivalLabel()}`,
      `${t.name}: ${state.name}`,
      `${t.phone}: ${state.phone}`,
      `${t.notes}: ${state.notes || '—'}`,
      '---',
      t.pickDateLead,
      'Glavani Park · Glavani 10, Barban, Istria',
    ].join('\n');
  }

  function saveToDiary() {
    const a = selectedActivity();
    const bookings = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    bookings.unshift({
      id: Date.now(),
      activities: a ? a.name : '',
      date: selectedDate,
      name: state.name,
      phone: state.phone,
      guests: guestCount(),
      total: bookingTotal(),
      arrival: arrivalLabel(),
      notes: state.notes,
      message: buildMessage(),
    });
    localStorage.setItem(STORAGE_KEY, JSON.stringify(bookings.slice(0, 20)));
  }

  function renderProgress() {
    return `<ol class="book-steps" aria-label="Booking steps">
      ${t.steps.map((label, i) =>
        `<li class="book-steps__item${i === step ? ' book-steps__item--active' : ''}${i < step ? ' book-steps__item--done' : ''}">${label}</li>`
      ).join('')}
    </ol>`;
  }

  function renderPackageStep() {
    return `<section class="book-panel">
      <h2>${t.pickActivity}</h2>
      <p class="book-panel__lead">${t.pickActivityLead}</p>
      <div class="booking-form booking-form--package">
        <div>
          <label for="app-package">${t.package}</label>
          <select id="app-package" required>
            <option value=""${!selectedActivityId ? ' selected' : ''} disabled>${t.selectPackage}</option>
            ${renderPackageOptions()}
          </select>
        </div>
        <div>
          <label for="app-guests">${t.selectGuests}</label>
          <select id="app-guests">${renderGuestOptions()}</select>
        </div>
        ${renderPriceBox()}
      </div>
    </section>`;
  }

  function renderCalendar() {
    const first = new Date(viewYear, viewMonth, 1);
    const startDay = (first.getDay() + 6) % 7;
    const daysInMonth = new Date(viewYear, viewMonth + 1, 0).getDate();
    let dayCells = '';
    for (let i = 0; i < startDay; i++) dayCells += '<span class="cal-cell cal-cell--empty"></span>';
    for (let day = 1; day <= daysInMonth; day++) {
      const d = new Date(viewYear, viewMonth, day);
      const iso = isoDate(d);
      const isPast = d < today;
      const isSel = selectedDate === iso;
      const cls = ['cal-cell','cal-day', isPast ? 'cal-day--past' : 'cal-day--open', isSel ? 'cal-day--selected' : ''].filter(Boolean).join(' ');
      dayCells += `<button type="button" class="${cls}" data-date="${iso}" ${isPast ? 'disabled' : ''}>${day}</button>`;
    }
    const a = selectedActivity();
    const summary = a ? `<p class="book-package-preview">${a.name} · ${guestCount()} ${lang === 'hr' ? 'osoba' : 'guests'} · <strong>€${bookingTotal()}</strong></p>` : '';
    return `<section class="book-panel">
      <h2>${t.pickDate}</h2>
      <p class="book-panel__lead">${t.pickDateLead}</p>
      ${summary}
      <div class="cal-nav">
        <button type="button" id="app-cal-prev" aria-label="Previous">‹</button>
        <span id="app-cal-month">${t.months[viewMonth]} ${viewYear}</span>
        <button type="button" id="app-cal-next" aria-label="Next">›</button>
      </div>
      <div class="cal-grid cal-grid--head">${t.days.map(d => `<span class="cal-cell cal-cell--head">${d}</span>`).join('')}</div>
      <div class="cal-grid">${dayCells}</div>
    </section>`;
  }

  function renderDetails() {
    const a = selectedActivity();
    const preview = a ? `<p class="book-package-preview">${a.name} · ${t.total}: <strong>€${bookingTotal()}</strong></p>` : '';
    return `<section class="book-panel">
      <h2>${t.yourDetails}</h2>
      ${preview}
      <div class="booking-form">
        <div class="booking-form__row">
          <div><label for="app-name">${t.name}</label><input id="app-name" type="text" value="${state.name}" required autocomplete="name"></div>
          <div><label for="app-phone">${t.phone}</label><input id="app-phone" type="tel" value="${state.phone}" required autocomplete="tel"></div>
        </div>
        <div>
          <label for="app-arrival">${t.arrival}</label>
          <select id="app-arrival">${renderArrivalOptions()}</select>
          <p class="field-hint">${t.arrivalLead}</p>
        </div>
        <div><label for="app-notes">${t.notes}</label><textarea id="app-notes" placeholder="${t.notesPh}">${state.notes}</textarea></div>
      </div>
    </section>`;
  }

  function renderConfirm() {
    const a = selectedActivity();
    const msg = buildMessage();
    const total = bookingTotal();
    return `<section class="book-panel">
      <h2>${t.confirmTitle}</h2>
      <p class="book-panel__lead">${t.confirmLead}</p>
      <div class="book-summary">
        <h3>${t.summary}</h3>
        <dl>
          <dt>${t.package}</dt><dd>${a ? a.name : '—'}</dd>
          <dt>${t.pricePerPerson}</dt><dd>€${a ? a.price : 0}</dd>
          <dt>${t.guests}</dt><dd>${guestCount()}</dd>
          <dt>${t.total}</dt><dd><strong>€${total}</strong></dd>
          <dt>${t.date}</dt><dd>${selectedDate}</dd>
          <dt>${t.arrival}</dt><dd>${arrivalLabel()}</dd>
          <dt>${t.name}</dt><dd>${state.name}</dd>
          <dt>${t.phone}</dt><dd>${state.phone}</dd>
        </dl>
      </div>
      <div class="book-send-grid">
        <a class="btn-whatsapp" href="https://wa.me/${phone}?text=${encodeURIComponent(msg)}" target="_blank" rel="noopener">${t.whatsapp}</a>
        <a class="btn-sms" href="sms:+${phone}?body=${encodeURIComponent(msg)}">${t.sms}</a>
        <a class="btn-secondary" href="tel:+${phone}">${t.call}</a>
        <button type="button" class="btn-copy" id="btn-copy">${t.copy}</button>
      </div>
      <p class="book-hint">${t.parkHours}</p>
    </section>`;
  }

  function renderDiary() {
    const bookings = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    if (!bookings.length) {
      return `<section class="book-panel"><h2>${t.myDiary}</h2><p class="book-panel__lead">${t.emptyDiary}</p></section>`;
    }
    return `<section class="book-panel">
      <h2>${t.myDiary}</h2>
      <p class="book-panel__lead">${t.myDiaryLead}</p>
      <ul class="diary-list">
        ${bookings.map(b => `<li class="diary-item">
          <strong>${b.date}</strong> — ${b.activities}
          <span>${b.name} · ${b.guests} ${lang === 'hr' ? 'osoba' : 'guests'}${b.total ? ` · €${b.total}` : ''}</span>
          <div class="diary-item__actions">
            <a href="https://wa.me/${phone}?text=${encodeURIComponent(b.message)}" class="btn-whatsapp btn-whatsapp--sm" target="_blank" rel="noopener">WhatsApp</a>
            <a href="tel:+${phone}" class="btn-secondary btn-secondary--sm">${t.call}</a>
          </div>
        </li>`).join('')}
      </ul>
    </section>`;
  }

  let activeTab = 'book';

  function render() {
    if (activeTab === 'diary') {
      root.innerHTML = `
        <div class="book-tabs">
          <button type="button" class="book-tabs__btn" data-tab="book">${t.tabBook}</button>
          <button type="button" class="book-tabs__btn book-tabs__btn--active" data-tab="diary">${t.tabDiary}</button>
        </div>
        ${renderDiary()}`;
      bindTabs();
      return;
    }

    const panels = [renderPackageStep(), renderCalendar(), renderDetails(), renderConfirm()];
    root.innerHTML = `
      <div class="book-tabs">
        <button type="button" class="book-tabs__btn book-tabs__btn--active" data-tab="book">${t.tabBook}</button>
        <button type="button" class="book-tabs__btn" data-tab="diary">${t.tabDiary}</button>
      </div>
      ${renderProgress()}
      ${panels[step]}
      <div class="book-nav">
        ${step > 0 ? `<button type="button" class="btn-secondary" id="book-back">${t.back}</button>` : '<span></span>'}
        ${step < 3 && !(step === 0 && state.largeGroup) ? `<button type="button" class="btn-primary" id="book-next">${t.next}</button>` : ''}
      </div>`;

    bindTabs();
    bindStepEvents();
    if (step === 0) toggleNextButton();
  }

  function bindTabs() {
    root.querySelectorAll('.book-tabs__btn').forEach(btn => {
      btn.addEventListener('click', () => {
        activeTab = btn.dataset.tab;
        render();
      });
    });
  }

  function bindStepEvents() {
    document.getElementById('app-package')?.addEventListener('change', (e) => {
      selectedActivityId = e.target.value;
      updatePriceBox();
    });

    document.getElementById('app-guests')?.addEventListener('change', (e) => {
      if (e.target.value === 'call') {
        state.largeGroup = true;
      } else {
        state.largeGroup = false;
        state.guests = parseInt(e.target.value, 10);
      }
      updatePriceBox();
    });

    root.querySelectorAll('.cal-day--open').forEach(btn => {
      btn.addEventListener('click', () => {
        selectedDate = btn.dataset.date;
        render();
      });
    });

    document.getElementById('app-cal-prev')?.addEventListener('click', () => {
      viewMonth--;
      if (viewMonth < 0) { viewMonth = 11; viewYear--; }
      render();
    });
    document.getElementById('app-cal-next')?.addEventListener('click', () => {
      viewMonth++;
      if (viewMonth > 11) { viewMonth = 0; viewYear++; }
      render();
    });

    document.getElementById('book-back')?.addEventListener('click', () => { step--; render(); });

    document.getElementById('book-next')?.addEventListener('click', () => {
      if (step === 0) {
        selectedActivityId = document.getElementById('app-package')?.value || '';
        const guestVal = document.getElementById('app-guests')?.value || '1';
        if (guestVal === 'call') {
          state.largeGroup = true;
          return;
        }
        state.largeGroup = false;
        state.guests = parseInt(guestVal, 10);
        if (!selectedActivityId) { alert(t.selectActivity); return; }
      }
      if (step === 1 && !selectedDate) { alert(t.selectDate); return; }
      if (step === 2) {
        state.name = document.getElementById('app-name')?.value.trim() || '';
        state.phone = document.getElementById('app-phone')?.value.trim() || '';
        state.arrival = parseInt(document.getElementById('app-arrival')?.value || '0', 10);
        state.notes = document.getElementById('app-notes')?.value.trim() || '';
        if (!state.name || !state.phone) { alert(t.fillRequired); return; }
      }
      if (step === 2) saveToDiary();
      step++;
      render();
    });

    document.getElementById('btn-copy')?.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(buildMessage());
        alert(t.copied);
      } catch {
        prompt(t.copy, buildMessage());
      }
    });
  }

  viewYear = today.getFullYear();
  viewMonth = today.getMonth();
  render();
})();
