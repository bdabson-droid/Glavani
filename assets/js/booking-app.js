/**
 * Glavani Park Booking App — activity packages, up to 6 guests, adult pricing.
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
        { id: 'training-2', icon: '🌲', name: 'Training route + 2 games', desc: 'High ropes training route plus two park games', price: 30 },
        { id: 'all-no-catapult', icon: '🎫', name: 'All games (without catapult)', desc: 'Every attraction except the human catapult', price: 50 },
        { id: 'catapult-swing', icon: '🚀', name: 'Human catapult + 12.5 m swing', desc: 'Human catapult and high swing — ages 10+', price: 50 },
        { id: 'all-incl-catapult', icon: '⭐', name: 'All games incl. human catapult', desc: 'Full park: ziplines, swing, catapult, Quick Jump & more', price: 70 },
      ],
      months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
      days: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      pickActivity: 'Choose your package',
      pickActivityLead: 'All prices shown are adult rates per person · max 6 people online',
      priceEach: '€{price} per person',
      pickDate: 'Pick your visit date',
      pickDateLead: 'Open daily 9 AM–5 PM · last entry 3 PM',
      yourDetails: 'Your details',
      confirmTitle: 'Confirm booking',
      confirmLead: 'Send your request via WhatsApp or SMS — no email needed',
      name: 'Your name',
      phone: 'Your phone number',
      guests: 'Number of guests (max 6)',
      guestsHint: 'Groups of 7 or more must call to book.',
      arrival: 'Preferred arrival',
      arrivalOpts: ['Morning (9:00–10:30)', 'Late morning (10:30–12:00)', 'Afternoon (12:00–14:00)'],
      notes: 'Notes (optional)',
      notesPh: 'Any special requests…',
      next: 'Next',
      back: 'Back',
      summary: 'Booking summary',
      package: 'Package',
      date: 'Date',
      pricePerPerson: 'Price per person',
      estimatedTotal: 'Estimated total',
      whatsapp: 'Send via WhatsApp',
      sms: 'Send SMS',
      call: 'Call to confirm',
      copy: 'Copy details',
      copied: 'Copied to clipboard!',
      selectActivity: 'Please select a package.',
      selectDate: 'Please select a visit date.',
      fillRequired: 'Please enter your name and phone number.',
      tooManyGuests: 'Online booking is for up to 6 people only. Please call to book larger groups:',
      myDiary: 'My booking diary',
      myDiaryLead: 'Saved on this device',
      emptyDiary: 'No saved bookings yet.',
      tabBook: 'Book',
      tabDiary: 'My diary',
      parkHours: 'Prices are adult rates · confirm on arrival · park open 9 AM – 5 PM',
      msgHeader: 'Glavani Park booking request',
      callGroups: 'Call for groups of 7+',
    },
    hr: {
      steps: ['Paket', 'Datum', 'Podaci', 'Potvrda'],
      activities: [
        { id: 'training-2', icon: '🌲', name: 'Trening ruta + 2 igre', desc: 'Trening ruta na visokim stazama plus dvije atrakcije', price: 30 },
        { id: 'all-no-catapult', icon: '🎫', name: 'Sve igre (bez katapulata)', desc: 'Sve atrakcije osim ljudske katapulata', price: 50 },
        { id: 'catapult-swing', icon: '🚀', name: 'Ljudska katapulta + ljuljačka 12,5 m', desc: 'Katapulta i visoka ljuljačka — 10+ godina', price: 50 },
        { id: 'all-incl-catapult', icon: '⭐', name: 'Sve igre uklj. ljudsku katapultu', desc: 'Cijeli park: zipline, ljuljačka, katapulta, Quick Jump i više', price: 70 },
      ],
      months: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
      days: ['Pon','Uto','Sri','Čet','Pet','Sub','Ned'],
      pickActivity: 'Odaberite paket',
      pickActivityLead: 'Sve cijene su odrasla ulaznica po osobi · max 6 osoba online',
      priceEach: '€{price} po osobi',
      pickDate: 'Odaberite datum posjeta',
      pickDateLead: 'Otvoreno 9–17 h · zadnji ulaz 15 h',
      yourDetails: 'Vaši podaci',
      confirmTitle: 'Potvrdite rezervaciju',
      confirmLead: 'Pošaljite WhatsAppom ili SMS-om — bez e-maila',
      name: 'Ime i prezime',
      phone: 'Broj telefona',
      guests: 'Broj gostiju (max 6)',
      guestsHint: 'Grupe od 7 i više osoba moraju rezervirati telefonom.',
      arrival: 'Preferirani dolazak',
      arrivalOpts: ['Jutro (9:00–10:30)', 'Kasno jutro (10:30–12:00)', 'Poslijepodne (12:00–14:00)'],
      notes: 'Napomena (opcionalno)',
      notesPh: 'Posebni zahtjevi…',
      next: 'Dalje',
      back: 'Natrag',
      summary: 'Sažetak rezervacije',
      package: 'Paket',
      date: 'Datum',
      pricePerPerson: 'Cijena po osobi',
      estimatedTotal: 'Procijenjen ukupno',
      whatsapp: 'Pošalji WhatsApp',
      sms: 'Pošalji SMS',
      call: 'Pozovi za potvrdu',
      copy: 'Kopiraj detalje',
      copied: 'Kopirano!',
      selectActivity: 'Odaberite paket.',
      selectDate: 'Odaberite datum posjeta.',
      fillRequired: 'Unesite ime i telefon.',
      tooManyGuests: 'Online rezervacija je za najviše 6 osoba. Za veće grupe nazovite:',
      myDiary: 'Moj dnevnik rezervacija',
      myDiaryLead: 'Spremljeno na ovom uređaju',
      emptyDiary: 'Još nema spremljenih rezervacija.',
      tabBook: 'Rezerviraj',
      tabDiary: 'Dnevnik',
      parkHours: 'Cijene su za odrasle · potvrda na ulazu · park 9–17 h',
      msgHeader: 'Zahtjev za rezervaciju Glavani Park',
      callGroups: 'Pozovite za grupe 7+',
    },
  };
  const t = i18n[lang];
  const phone = lang === 'hr' ? PHONE_HR : PHONE_EN;

  let step = 0;
  let selectedActivityId = null;
  let selectedDate = null;
  let viewYear, viewMonth;
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const state = { name: '', phone: '', guests: 2, arrival: 0, notes: '' };

  function pad(n) { return String(n).padStart(2, '0'); }
  function isoDate(d) { return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; }

  function selectedActivity() {
    return t.activities.find(a => a.id === selectedActivityId) || null;
  }

  function estimatedTotal() {
    const a = selectedActivity();
    if (!a) return 0;
    return a.price * parseInt(state.guests, 10);
  }

  function buildMessage() {
    const a = selectedActivity();
    const total = estimatedTotal();
    return [
      t.msgHeader,
      '---',
      `${t.package}: ${a ? a.name : '—'}`,
      `${t.pricePerPerson}: €${a ? a.price : 0} (${lang === 'hr' ? 'odrasla cijena' : 'adult rate'})`,
      `${t.guests}: ${state.guests}`,
      `${t.estimatedTotal}: €${total}`,
      `${t.date}: ${selectedDate}`,
      `${t.name}: ${state.name}`,
      `${t.phone}: ${state.phone}`,
      `${t.arrival}: ${t.arrivalOpts[state.arrival]}`,
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
      guests: state.guests,
      total: estimatedTotal(),
      arrival: t.arrivalOpts[state.arrival],
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

  function renderActivities() {
    return `<section class="book-panel">
      <h2>${t.pickActivity}</h2>
      <p class="book-panel__lead">${t.pickActivityLead}</p>
      <div class="activity-grid">
        ${t.activities.map(a => {
          const on = selectedActivityId === a.id;
          const priceLabel = t.priceEach.replace('{price}', a.price);
          return `<button type="button" class="activity-pick${on ? ' activity-pick--on' : ''}" data-id="${a.id}" aria-pressed="${on}">
            <span class="activity-pick__icon">${a.icon}</span>
            <span class="activity-pick__name">${a.name}</span>
            <span class="activity-pick__price">${priceLabel}</span>
            <span class="activity-pick__desc">${a.desc}</span>
          </button>`;
        }).join('')}
      </div>
      <p class="book-groups-notice">${t.guestsHint} <a href="tel:+${phone}">${t.callGroups}</a></p>
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
    return `<section class="book-panel">
      <h2>${t.pickDate}</h2>
      <p class="book-panel__lead">${t.pickDateLead}</p>
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
    const preview = a ? `<p class="book-package-preview">${a.name} · ${t.priceEach.replace('{price}', a.price)}</p>` : '';
    return `<section class="book-panel">
      <h2>${t.yourDetails}</h2>
      ${preview}
      <div class="booking-form">
        <div class="booking-form__row">
          <div><label for="app-name">${t.name}</label><input id="app-name" type="text" value="${state.name}" required autocomplete="name"></div>
          <div><label for="app-phone">${t.phone}</label><input id="app-phone" type="tel" value="${state.phone}" required autocomplete="tel"></div>
        </div>
        <div class="booking-form__row">
          <div>
            <label for="app-guests">${t.guests}</label>
            <input id="app-guests" type="number" min="1" max="${MAX_GUESTS}" value="${state.guests}">
            <p class="field-hint">${t.guestsHint}</p>
          </div>
          <div><label for="app-arrival">${t.arrival}</label>
            <select id="app-arrival">${t.arrivalOpts.map((o, i) => `<option value="${i}"${i === state.arrival ? ' selected' : ''}>${o}</option>`).join('')}</select>
          </div>
        </div>
        <div><label for="app-notes">${t.notes}</label><textarea id="app-notes" placeholder="${t.notesPh}">${state.notes}</textarea></div>
        ${a ? `<p class="book-total-preview"><strong>${t.estimatedTotal}:</strong> €${a.price * parseInt(state.guests, 10)}</p>` : ''}
      </div>
    </section>`;
  }

  function renderConfirm() {
    const a = selectedActivity();
    const msg = buildMessage();
    const total = estimatedTotal();
    return `<section class="book-panel">
      <h2>${t.confirmTitle}</h2>
      <p class="book-panel__lead">${t.confirmLead}</p>
      <div class="book-summary">
        <h3>${t.summary}</h3>
        <dl>
          <dt>${t.package}</dt><dd>${a ? a.name : '—'}</dd>
          <dt>${t.pricePerPerson}</dt><dd>€${a ? a.price : 0}</dd>
          <dt>${t.guests}</dt><dd>${state.guests}</dd>
          <dt>${t.estimatedTotal}</dt><dd><strong>€${total}</strong></dd>
          <dt>${t.date}</dt><dd>${selectedDate}</dd>
          <dt>${t.name}</dt><dd>${state.name}</dd>
          <dt>${t.phone}</dt><dd>${state.phone}</dd>
          <dt>${t.arrival}</dt><dd>${t.arrivalOpts[state.arrival]}</dd>
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

    const panels = [renderActivities(), renderCalendar(), renderDetails(), renderConfirm()];
    root.innerHTML = `
      <div class="book-tabs">
        <button type="button" class="book-tabs__btn book-tabs__btn--active" data-tab="book">${t.tabBook}</button>
        <button type="button" class="book-tabs__btn" data-tab="diary">${t.tabDiary}</button>
      </div>
      ${renderProgress()}
      ${panels[step]}
      <div class="book-nav">
        ${step > 0 ? `<button type="button" class="btn-secondary" id="book-back">${t.back}</button>` : '<span></span>'}
        ${step < 3 ? `<button type="button" class="btn-primary" id="book-next">${t.next}</button>` : ''}
      </div>`;

    bindTabs();
    bindStepEvents();
  }

  function bindTabs() {
    root.querySelectorAll('.book-tabs__btn').forEach(btn => {
      btn.addEventListener('click', () => {
        activeTab = btn.dataset.tab;
        render();
      });
    });
  }

  function validateGuests(guests) {
    const n = parseInt(guests, 10);
    if (n > MAX_GUESTS) {
      alert(`${t.tooManyGuests}\n+${phone}`);
      return false;
    }
    return true;
  }

  function bindStepEvents() {
    root.querySelectorAll('.activity-pick').forEach(btn => {
      btn.addEventListener('click', () => {
        selectedActivityId = btn.dataset.id;
        render();
      });
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

    document.getElementById('app-guests')?.addEventListener('input', (e) => {
      const val = parseInt(e.target.value, 10);
      if (val > MAX_GUESTS) {
        e.target.value = MAX_GUESTS;
        state.guests = MAX_GUESTS;
      } else {
        state.guests = val || 1;
      }
    });

    document.getElementById('book-back')?.addEventListener('click', () => { step--; render(); });

    document.getElementById('book-next')?.addEventListener('click', () => {
      if (step === 0 && !selectedActivityId) { alert(t.selectActivity); return; }
      if (step === 1 && !selectedDate) { alert(t.selectDate); return; }
      if (step === 2) {
        state.name = document.getElementById('app-name')?.value.trim() || '';
        state.phone = document.getElementById('app-phone')?.value.trim() || '';
        state.guests = parseInt(document.getElementById('app-guests')?.value || '1', 10);
        state.arrival = parseInt(document.getElementById('app-arrival')?.value || '0', 10);
        state.notes = document.getElementById('app-notes')?.value.trim() || '';
        if (!state.name || !state.phone) { alert(t.fillRequired); return; }
        if (!validateGuests(state.guests)) return;
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
