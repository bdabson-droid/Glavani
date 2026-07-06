/**
 * Glavani Park booking — package & guest dropdowns, live pricing.
 * Groups of more than 10 must call. Bookings submit directly to the park inbox.
 * Keep activity names/prices in sync with scripts/packages.py.
 */
(function () {
  const root = document.getElementById('booking-app');
  if (!root) return;

  const configEl = document.getElementById('booking-app-config');
  if (!configEl) return;

  let config;
  try {
    config = JSON.parse(configEl.textContent);
  } catch (e) {
    return;
  }

  const MAX_GUESTS = 10;
  const lang = config.lang === 'hr' ? 'hr' : 'en';
  const PHONE_EN = '385918964525';
  const PHONE_HR = '38598224314';

  const i18n = {
    en: {
      steps: ['Package', 'Date', 'Details', 'Confirm'],
      activities: [
        { id: 'all-incl-catapult', group: 'packages', name: 'Whole park — all games incl. human catapult', price: 70, child_price: 60 },
        { id: 'catapult-swing', group: 'packages', name: 'Human catapult + 12.5 m swing', price: 50 },
        { id: 'all-no-catapult', group: 'packages', name: 'Whole park — all games (without catapult)', price: 50, child_price: 40 },
        { id: 'training-2', group: 'packages', name: 'Training route + 2 games', price: 30, child_price: 20 },
        { id: 'human-catapult', group: 'single', name: 'Human Catapult', price: 40 },
      ],
      groupPackages: 'Activity packages',
      groupSingle: 'Single activities',
      months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
      days: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      pickActivity: 'Choose your package or activity',
      pickActivityLead: 'Packages first, then single activities · max 10 people online',
      selectPackage: 'Select a package or activity…',
      selectGuests: 'Number of people',
      selectAdults: 'Adults',
      selectChildren: 'Children',
      guestsOption: '{n} person',
      guestsOptionPlural: '{n} people',
      guestsOptionCallPlus: 'More than 10 people — please call',
      callInsteadTitle: 'Groups of more than 10',
      callInsteadLead: 'Please call us so we can check availability and accommodate your party.',
      callToBook: 'Call to book your group',
      priceEach: '€{price} per person',
      priceAdultsChildren: '€{adult} adults · €{child} children',
      total: 'Total',
      pickDate: 'Pick your visit date',
      pickDateLead: 'Open daily 9 AM–5 PM · last entry 3 PM',
      yourDetails: 'Your details',
      confirmTitle: 'Confirm booking',
      confirmLead: 'Check your package and total below, then submit your booking. We will reply with an emailed invoice to confirm as soon as possible.',
      within48Title: 'Within 48 hours of your visit?',
      within48Lead: 'Please call to book so we can confirm availability in time.',
      within48Alert: 'Your selected date is within 48 hours. Please call to book instead of using the form.',
      name: 'Your name',
      email: 'Your email address',
      phone: 'Your phone number',
      guestsHint: 'Groups of more than 10 must call to book.',
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
      adults: 'Adults',
      children: 'Children',
      pricePerPerson: 'Price per person',
      sendEmail: 'Submit booking',
      submitting: 'Sending…',
      submitSuccessTitle: 'Booking sent',
      submitSuccess: 'Thank you — your booking request has been sent. We will email your invoice to confirm as soon as possible.',
      submitError: 'Sorry, we could not send your booking right now. Please call us instead.',
      newBooking: 'Make another booking',
      call: 'Call to confirm',
      copy: 'Copy details',
      copied: 'Copied to clipboard!',
      selectActivity: 'Please select a package or activity.',
      selectDate: 'Please select a visit date.',
      fillRequired: 'Please enter your name, email address, and phone number.',
      emailInvalid: 'Please enter a valid email address.',
      tooManyGuests: 'Online booking is for up to 10 people only. Please call to book larger groups:',
      parkHours: 'Confirm on arrival · park open 9 AM – 5 PM',
      msgHeader: 'Glavani Park booking request',
      callGroups: 'Call for groups of 10+',
    },
    hr: {
      steps: ['Paket', 'Datum', 'Podaci', 'Potvrda'],
      activities: [
        { id: 'all-incl-catapult', group: 'packages', name: 'Cijeli park — sve igre uklj. katapultu', price: 70, child_price: 60 },
        { id: 'catapult-swing', group: 'packages', name: 'Ljudska katapulta + ljuljačka 12,5 m', price: 50 },
        { id: 'all-no-catapult', group: 'packages', name: 'Cijeli park — sve igre (bez katapulata)', price: 50, child_price: 40 },
        { id: 'training-2', group: 'packages', name: 'Trening ruta + 2 igre', price: 30, child_price: 20 },
        { id: 'human-catapult', group: 'single', name: 'Ljudska katapulta', price: 40 },
      ],
      groupPackages: 'Paketi aktivnosti',
      groupSingle: 'Pojedinačne aktivnosti',
      months: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
      days: ['Pon','Uto','Sri','Čet','Pet','Sub','Ned'],
      pickActivity: 'Odaberite paket ili aktivnost',
      pickActivityLead: 'Prvo paketi, zatim pojedinačne aktivnosti · max 10 osoba online',
      selectPackage: 'Odaberite paket ili aktivnost…',
      selectGuests: 'Broj osoba',
      selectAdults: 'Odrasli',
      selectChildren: 'Djeca',
      guestsOption: '{n} osoba',
      guestsOptionPlural: '{n} osobe',
      guestsOptionCallPlus: 'Više od 10 osoba — nazovite',
      callInsteadTitle: 'Grupe s više od 10 osoba',
      callInsteadLead: 'Nazovite nas kako bismo provjerili dostupnost i mogli ugostiti vašu grupu.',
      callToBook: 'Pozovite za rezervaciju grupe',
      priceEach: '€{price} po osobi',
      priceAdultsChildren: '€{adult} odrasli · €{child} djeca',
      total: 'Ukupno',
      pickDate: 'Odaberite datum posjeta',
      pickDateLead: 'Otvoreno 9–17 h · zadnji ulaz 15 h',
      yourDetails: 'Vaši podaci',
      confirmTitle: 'Potvrdite rezervaciju',
      confirmLead: 'Provjerite paket i ukupnu cijenu u nastavku, zatim pošaljite rezervaciju. Odgovorit ćemo e-računom za potvrdu što je prije moguće.',
      within48Title: 'Unutar 48 sati od posjeta?',
      within48Lead: 'Molimo nazovite kako bismo na vrijeme potvrdili dostupnost.',
      within48Alert: 'Odabrani datum je unutar 48 sati. Molimo nazovite umjesto online obrasca.',
      name: 'Ime i prezime',
      email: 'Vaša e-mail adresa',
      phone: 'Broj telefona',
      guestsHint: 'Grupe s više od 10 osoba moraju rezervirati telefonom.',
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
      adults: 'Odrasli',
      children: 'Djeca',
      pricePerPerson: 'Cijena po osobi',
      sendEmail: 'Pošalji rezervaciju',
      submitting: 'Slanje…',
      submitSuccessTitle: 'Rezervacija poslana',
      submitSuccess: 'Hvala — vaš zahtjev za rezervaciju je poslan. E-račun za potvrdu poslat ćemo što je prije moguće.',
      submitError: 'Nažalost, rezervaciju trenutno nismo mogli poslati. Molimo nazovite nas.',
      newBooking: 'Nova rezervacija',
      call: 'Pozovi za potvrdu',
      copy: 'Kopiraj detalje',
      copied: 'Kopirano!',
      selectActivity: 'Odaberite paket ili aktivnost.',
      selectDate: 'Odaberite datum posjeta.',
      fillRequired: 'Unesite ime, e-mail adresu i telefon.',
      emailInvalid: 'Unesite ispravnu e-mail adresu.',
      tooManyGuests: 'Online rezervacija je za najviše 10 osoba. Za veće grupe nazovite:',
      parkHours: 'Potvrda na ulazu · park 9–17 h',
      msgHeader: 'Zahtjev za rezervaciju Glavani Park',
      callGroups: 'Pozovite za grupe 10+',
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

  const state = { name: '', email: '', phone: '', guests: 1, adults: 1, children: 0, largeGroup: false, arrival: 0, notes: '' };
  let submitted = false;

  const PREFILL_KEY = 'glavani-book-prefill';

  function readPrefillParams() {
    const params = new URLSearchParams(window.location.search);
    if (window.location.hash.length > 1) {
      const hashParams = new URLSearchParams(window.location.hash.slice(1));
      hashParams.forEach((value, key) => params.set(key, value));
    }
    try {
      const stored = sessionStorage.getItem(PREFILL_KEY);
      if (stored) {
        sessionStorage.removeItem(PREFILL_KEY);
        const data = JSON.parse(stored);
        if (data.package) params.set('package', data.package);
        if (data.guests) params.set('guests', String(data.guests));
      }
    } catch (e) {
      /* ignore */
    }
    return params;
  }

  function applyQueryPrefill() {
    const params = readPrefillParams();
    const pkg = params.get('package') || params.get('p');
    const guestsRaw = params.get('guests') || params.get('g');

    if (pkg && t.activities.some((a) => a.id === pkg)) {
      selectedActivityId = pkg;
    }

    if (guestsRaw) {
      const n = parseInt(guestsRaw, 10);
      if (n > MAX_GUESTS) {
        state.largeGroup = true;
      } else if (n >= 1) {
        state.guests = n;
        state.largeGroup = false;
      }
    }
  }

  function isoDate(d) { return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; }

  function isWithin48Hours(isoDate) {
    const visit = new Date(`${isoDate}T09:00:00`);
    const now = new Date();
    const diff = visit.getTime() - now.getTime();
    return diff >= 0 && diff < 48 * 60 * 60 * 1000;
  }

  function renderWithin48Warning() {
    return `<div class="book-within48" role="alert">
      <h3>${t.within48Title}</h3>
      <p>${t.within48Lead}</p>
      <a class="btn-call-book" href="tel:+${phone}">${t.callToBook}</a>
    </div>`;
  }

  function selectedActivity() {
    return t.activities.find(a => a.id === selectedActivityId) || null;
  }

  function activityHasChildPrice(a) {
    return !!(a && typeof a.child_price === 'number');
  }

  function guestCount() {
    if (state.largeGroup) return 0;
    const a = selectedActivity();
    if (activityHasChildPrice(a)) {
      return Math.min(MAX_GUESTS, Math.max(0, parseInt(state.adults, 10) || 0) + Math.max(0, parseInt(state.children, 10) || 0));
    }
    return Math.min(MAX_GUESTS, Math.max(1, parseInt(state.guests, 10) || 1));
  }

  function bookingTotal() {
    const a = selectedActivity();
    if (!a) return 0;
    if (activityHasChildPrice(a)) {
      const adults = Math.max(0, parseInt(state.adults, 10) || 0);
      const children = Math.max(0, parseInt(state.children, 10) || 0);
      return adults * a.price + children * a.child_price;
    }
    return a.price * guestCount();
  }

  function packageOptionLabel(a) {
    if (activityHasChildPrice(a)) {
      return `${a.name} — €${a.price} / €${a.child_price}`;
    }
    return `${a.name} — €${a.price}/pp`;
  }

  function priceSummaryLines(a) {
    if (!a) return [];
    if (activityHasChildPrice(a)) {
      const adults = Math.max(0, parseInt(state.adults, 10) || 0);
      const children = Math.max(0, parseInt(state.children, 10) || 0);
      const lines = [];
      if (adults) lines.push(`${adults} × €${a.price} (${t.adults})`);
      if (children) lines.push(`${children} × €${a.child_price} (${t.children})`);
      return lines;
    }
    return [`${guestCount()} × €${a.price}`];
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
    opts += `<option value="call"${state.largeGroup ? ' selected' : ''}>${t.guestsOptionCallPlus}</option>`;
    return opts;
  }

  function renderCountOptions(selected, max) {
    let opts = '';
    for (let n = 0; n <= max; n++) {
      opts += `<option value="${n}"${selected === n ? ' selected' : ''}>${n}</option>`;
    }
    return opts;
  }

  function renderGuestFields() {
    const a = selectedActivity();
    if (activityHasChildPrice(a)) {
      const maxAdults = Math.min(MAX_GUESTS, MAX_GUESTS - (parseInt(state.children, 10) || 0));
      const maxChildren = Math.min(MAX_GUESTS, MAX_GUESTS - (parseInt(state.adults, 10) || 0));
      return `<div class="booking-form__row">
        <div>
          <label for="app-adults">${t.selectAdults}</label>
          <select id="app-adults">${renderCountOptions(state.adults, maxAdults)}</select>
        </div>
        <div>
          <label for="app-children">${t.selectChildren}</label>
          <select id="app-children">${renderCountOptions(state.children, maxChildren)}</select>
        </div>
      </div>`;
    }
    return `<div>
      <label for="app-guests">${t.selectGuests}</label>
      <select id="app-guests" class="${state.largeGroup ? 'app-guests--call' : ''}">${renderGuestOptions()}</select>
    </div>`;
  }

  function renderPackageOptions() {
    const groups = [
      { key: 'packages', label: t.groupPackages },
      { key: 'single', label: t.groupSingle },
    ];
    return groups.map(g => {
      const items = t.activities
        .filter(a => a.group === g.key)
        .sort((a, b) => b.price - a.price);
      if (!items.length) return '';
      return `<optgroup label="${g.label}">${items.map(a =>
        `<option value="${a.id}"${selectedActivityId === a.id ? ' selected' : ''}>${packageOptionLabel(a)}</option>`
      ).join('')}</optgroup>`;
    }).join('');
  }

  function renderCallPanel() {
    return `<div class="book-call-panel" id="book-price-box" aria-live="polite">
      <p class="book-call-panel__badge">${lang === 'hr' ? '10+ osoba' : '10+ guests'}</p>
      <h3>${t.callInsteadTitle}</h3>
      <p class="book-call-panel__lead">${t.callInsteadLead}</p>
      <a class="btn-call-book btn-call-book--panel" href="tel:+${phone}">${t.callToBook}</a>
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
      <p class="book-price-box__each">${activityHasChildPrice(a)
        ? t.priceAdultsChildren.replace('{adult}', a.price).replace('{child}', a.child_price)
        : t.priceEach.replace('{price}', a.price)}</p>
      <p class="book-price-box__total"><span>${t.total}</span> <strong>€${total}</strong></p>
      <p class="book-price-box__meta">${priceSummaryLines(a).join(' · ')}</p>
    </div>`;
  }

  function updateLargeGroupUI() {
    const form = root.querySelector('.booking-form--package');
    const guests = document.getElementById('app-guests');
    if (form) form.classList.toggle('booking-form--large-group', state.largeGroup);
    if (guests) guests.classList.toggle('app-guests--call', state.largeGroup);
  }

  function updatePriceBox() {
    const box = document.getElementById('book-price-box');
    if (!box) return;
    if (state.largeGroup) {
      box.outerHTML = renderCallPanel();
    } else {
      box.outerHTML = renderPriceBox();
    }
    updateLargeGroupUI();
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
      ...(activityHasChildPrice(a)
        ? [
            `${t.adults}: ${state.adults} × €${a.price}`,
            `${t.children}: ${state.children} × €${a.child_price}`,
          ]
        : [`${t.pricePerPerson}: €${a ? a.price : 0}`, `${t.guests}: ${guestCount()}`]),
      `${t.total}: €${total}`,
      `${t.date}: ${selectedDate}`,
      `${t.arrival}: ${arrivalLabel()}`,
      `${t.name}: ${state.name}`,
      `${t.email}: ${state.email}`,
      `${t.phone}: ${state.phone}`,
      `${t.notes}: ${state.notes || '—'}`,
      '---',
      t.pickDateLead,
      'Glavani Park · Glavani 10, Barban, Istria',
    ].join('\n');
  }

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value || '').trim());
  }

  function buildSubmitPayload() {
    const a = selectedActivity();
    return {
      _subject: `${t.msgHeader} – ${selectedDate}`,
      _template: 'table',
      _captcha: 'false',
      _replyto: state.email,
      name: state.name,
      email: state.email,
      phone: state.phone,
      package: a ? a.name : '—',
      price_per_person: a ? (activityHasChildPrice(a) ? `€${a.price} adults / €${a.child_price} children` : `€${a.price}`) : '—',
      adults: activityHasChildPrice(a) ? String(state.adults) : '—',
      children: activityHasChildPrice(a) ? String(state.children) : '—',
      guests: String(guestCount()),
      total: `€${bookingTotal()}`,
      date: selectedDate,
      arrival: arrivalLabel(),
      notes: state.notes || '—',
      message: buildMessage(),
    };
  }

  async function submitBooking() {
    const btn = document.getElementById('btn-submit');
    if (btn) {
      btn.disabled = true;
      btn.textContent = t.submitting;
    }
    try {
      const res = await fetch(config.submitUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        body: JSON.stringify(buildSubmitPayload()),
      });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.success) throw new Error('submit failed');
      submitted = true;
      render();
    } catch (err) {
      alert(t.submitError);
      if (btn) {
        btn.disabled = false;
        btn.textContent = t.sendEmail;
      }
    }
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
      <div class="booking-form booking-form--package${state.largeGroup ? ' booking-form--large-group' : ''}">
        <div>
          <label for="app-package">${t.package}</label>
          <select id="app-package" required>
            <option value=""${!selectedActivityId ? ' selected' : ''} disabled>${t.selectPackage}</option>
            ${renderPackageOptions()}
          </select>
        </div>
        ${renderGuestFields()}
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
    const within48 = selectedDate && isWithin48Hours(selectedDate) ? renderWithin48Warning() : '';
    return `<section class="book-panel">
      <h2>${t.pickDate}</h2>
      <p class="book-panel__lead">${t.pickDateLead}</p>
      ${summary}
      ${within48}
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
          <div><label for="app-email">${t.email}</label><input id="app-email" type="email" value="${state.email}" required autocomplete="email"></div>
        </div>
        <div class="booking-form__row">
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

  function renderSuccess() {
    return `<section class="book-panel book-panel--success">
      <h2>${t.submitSuccessTitle}</h2>
      <p class="book-panel__lead">${t.submitSuccess}</p>
      <button type="button" class="btn-primary" id="btn-new-booking">${t.newBooking}</button>
    </section>`;
  }

  function renderConfirm() {
    const a = selectedActivity();
    const total = bookingTotal();
    return `<section class="book-panel">
      <h2>${t.confirmTitle}</h2>
      <p class="book-panel__lead">${t.confirmLead}</p>
      <div class="book-summary">
        <h3>${t.summary}</h3>
        <dl>
          <dt>${t.package}</dt><dd>${a ? a.name : '—'}</dd>
          ${activityHasChildPrice(a)
            ? `<dt>${t.adults}</dt><dd>${state.adults} × €${a.price}</dd>
          <dt>${t.children}</dt><dd>${state.children} × €${a.child_price}</dd>`
            : `<dt>${t.pricePerPerson}</dt><dd>€${a ? a.price : 0}</dd>
          <dt>${t.guests}</dt><dd>${guestCount()}</dd>`}
          <dt>${t.total}</dt><dd><strong>€${total}</strong></dd>
          <dt>${t.date}</dt><dd>${selectedDate}</dd>
          <dt>${t.arrival}</dt><dd>${arrivalLabel()}</dd>
          <dt>${t.name}</dt><dd>${state.name}</dd>
          <dt>${t.email}</dt><dd>${state.email}</dd>
          <dt>${t.phone}</dt><dd>${state.phone}</dd>
        </dl>
      </div>
      <div class="book-send-grid">
        <button type="button" class="btn-primary btn-email-book" id="btn-submit">${t.sendEmail}</button>
        <a class="btn-secondary" href="tel:+${phone}">${t.call}</a>
        <button type="button" class="btn-copy" id="btn-copy">${t.copy}</button>
      </div>
      <p class="book-hint">${t.parkHours}</p>
    </section>`;
  }

  function render() {
    if (submitted) {
      root.innerHTML = renderSuccess();
      document.getElementById('btn-new-booking')?.addEventListener('click', () => {
        submitted = false;
        step = 0;
        selectedActivityId = '';
        selectedDate = null;
        state.name = '';
        state.email = '';
        state.phone = '';
        state.notes = '';
        state.guests = 1;
        state.adults = 1;
        state.children = 0;
        state.largeGroup = false;
        render();
      });
      return;
    }

    const panels = [renderPackageStep(), renderCalendar(), renderDetails(), renderConfirm()];
    const within48Block = step === 1 && selectedDate && isWithin48Hours(selectedDate);
    root.innerHTML = `
      ${renderProgress()}
      ${panels[step]}
      <div class="book-nav">
        ${step > 0 ? `<button type="button" class="btn-secondary" id="book-back">${t.back}</button>` : '<span></span>'}
        ${step < 3 && !(step === 0 && state.largeGroup) && !within48Block ? `<button type="button" class="btn-primary" id="book-next">${t.next}</button>` : ''}
      </div>`;

    bindStepEvents();
    if (step === 0) toggleNextButton();
  }

  function bindStepEvents() {
    document.getElementById('app-package')?.addEventListener('change', (e) => {
      selectedActivityId = e.target.value;
      const a = selectedActivity();
      if (activityHasChildPrice(a)) {
        state.largeGroup = false;
        state.adults = Math.max(1, state.adults || 1);
        state.children = state.children || 0;
      } else {
        state.guests = Math.max(1, guestCount() || 1);
      }
      render();
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

    document.getElementById('app-adults')?.addEventListener('change', (e) => {
      state.adults = parseInt(e.target.value, 10) || 0;
      if (state.adults + state.children < 1) state.children = 1;
      if (state.adults + state.children > MAX_GUESTS) {
        state.children = Math.max(0, MAX_GUESTS - state.adults);
      }
      render();
    });

    document.getElementById('app-children')?.addEventListener('change', (e) => {
      state.children = parseInt(e.target.value, 10) || 0;
      if (state.adults + state.children < 1) state.adults = 1;
      if (state.adults + state.children > MAX_GUESTS) {
        state.adults = Math.max(0, MAX_GUESTS - state.children);
      }
      render();
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
        const a = selectedActivity();
        if (activityHasChildPrice(a)) {
          state.largeGroup = false;
          state.adults = parseInt(document.getElementById('app-adults')?.value || '1', 10);
          state.children = parseInt(document.getElementById('app-children')?.value || '0', 10);
          if (state.adults + state.children < 1) {
            alert(t.selectGuests);
            return;
          }
          if (state.adults + state.children > MAX_GUESTS) {
            alert(t.tooManyGuests + ' +' + phone);
            return;
          }
        } else {
          const guestVal = document.getElementById('app-guests')?.value || '1';
          if (guestVal === 'call') {
            state.largeGroup = true;
            return;
          }
          state.largeGroup = false;
          state.guests = parseInt(guestVal, 10);
        }
        if (!selectedActivityId) { alert(t.selectActivity); return; }
      }
      if (step === 1 && !selectedDate) { alert(t.selectDate); return; }
      if (step === 1 && selectedDate && isWithin48Hours(selectedDate)) {
        alert(t.within48Alert);
        return;
      }
      if (step === 2) {
        state.name = document.getElementById('app-name')?.value.trim() || '';
        state.email = document.getElementById('app-email')?.value.trim() || '';
        state.phone = document.getElementById('app-phone')?.value.trim() || '';
        state.arrival = parseInt(document.getElementById('app-arrival')?.value || '0', 10);
        state.notes = document.getElementById('app-notes')?.value.trim() || '';
        if (!state.name || !state.phone || !state.email) { alert(t.fillRequired); return; }
        if (!isValidEmail(state.email)) { alert(t.emailInvalid); return; }
      }
      step++;
      render();
    });

    document.getElementById('btn-submit')?.addEventListener('click', () => {
      submitBooking();
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
  applyQueryPrefill();
  render();
})();
