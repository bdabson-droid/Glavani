/**
 * Glavani Park Booking App — pick activity + date, confirm via WhatsApp, SMS, or call.
 * Saves entries to your phone's local diary (localStorage). No email required.
 */
(function () {
  const root = document.getElementById('booking-app');
  if (!root) return;

  const lang = document.documentElement.lang?.startsWith('hr') ? 'hr' : 'en';
  const PHONE_EN = '385918964525';
  const PHONE_HR = '38598224314';
  const STORAGE_KEY = 'glavani-park-bookings';

  const i18n = {
    en: {
      steps: ['Activity', 'Date', 'Details', 'Confirm'],
      activities: [
        { id: 'full-day', icon: '🎫', name: 'Full day pass', desc: 'All attractions & high ropes routes' },
        { id: 'high-ropes', icon: '🌲', name: 'High ropes courses', desc: 'Yellow, blue & black routes' },
        { id: 'zipline', icon: '🪂', name: 'Ziplines', desc: 'Up to 120 m through the treetops' },
        { id: 'high-swing', icon: '🎢', name: '12.5 m high swing', desc: 'Soar above the Istrian forest' },
        { id: 'catapult', icon: '🚀', name: 'Human catapult', desc: '0 to 100 km/h in one second' },
        { id: 'quick-jump', icon: '⬇️', name: 'Quick Jump', desc: '20 m controlled free fall' },
        { id: 'climbing', icon: '🧗', name: 'Climbing wall', desc: 'Outdoor wall, all skill levels' },
        { id: 'team-building', icon: '🤝', name: 'Team building', desc: 'Corporate & group packages' },
        { id: 'birthday', icon: '🎂', name: 'Birthday party', desc: 'Priority access & party area' },
        { id: 'school', icon: '🎒', name: 'School trip', desc: 'Educational outdoor programme' },
      ],
      months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
      days: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      pickActivity: 'Choose your activity',
      pickActivityLead: 'Tap one or more activities you want to book',
      pickDate: 'Pick your visit date',
      pickDateLead: 'Open daily 9 AM–5 PM · last entry 3 PM',
      yourDetails: 'Your details',
      confirmTitle: 'Confirm booking',
      confirmLead: 'Send your request instantly — no email needed',
      name: 'Your name',
      phone: 'Your phone number',
      guests: 'Number of guests',
      arrival: 'Preferred arrival',
      arrivalOpts: ['Morning (9:00–10:30)', 'Late morning (10:30–12:00)', 'Afternoon (12:00–14:00)'],
      notes: 'Notes (optional)',
      notesPh: "Children's ages, group name…",
      next: 'Next',
      back: 'Back',
      confirm: 'Confirm & send',
      summary: 'Booking summary',
      activity: 'Activity',
      date: 'Date',
      whatsapp: 'Send via WhatsApp',
      sms: 'Send SMS',
      call: 'Call to confirm',
      copy: 'Copy details',
      copied: 'Copied to clipboard!',
      selectActivity: 'Please select at least one activity.',
      selectDate: 'Please select a visit date.',
      fillRequired: 'Please enter your name and phone number.',
      myDiary: 'My booking diary',
      myDiaryLead: 'Saved on this device — tap to view or send again',
      emptyDiary: 'No saved bookings yet. Complete a booking to see it here.',
      saved: 'Booking saved to your diary!',
      tabBook: 'Book',
      tabDiary: 'My diary',
      parkHours: 'Park open 9 AM – 5 PM',
      msgHeader: 'Glavani Park booking request',
    },
    hr: {
      steps: ['Aktivnost', 'Datum', 'Podaci', 'Potvrda'],
      activities: [
        { id: 'full-day', icon: '🎫', name: 'Cjelodnevna ulaznica', desc: 'Sve atrakcije i visoke staze' },
        { id: 'high-ropes', icon: '🌲', name: 'Visoke užadne staze', desc: 'Žuta, plava i crna staza' },
        { id: 'zipline', icon: '🪂', name: 'Zipline', desc: 'Do 120 m kroz krošnje' },
        { id: 'high-swing', icon: '🎢', name: 'Ljuljačka 12,5 m', desc: 'Let iznad istarske šume' },
        { id: 'catapult', icon: '🚀', name: 'Ljudska katapulta', desc: '0 do 100 km/h u sekundi' },
        { id: 'quick-jump', icon: '⬇️', name: 'Quick Jump', desc: '20 m kontrolirani slobodni pad' },
        { id: 'climbing', icon: '🧗', name: 'Penjački zid', desc: 'Na otvorenom, svi nivoi' },
        { id: 'team-building', icon: '🤝', name: 'Team building', desc: 'Korporativni i grupni paketi' },
        { id: 'birthday', icon: '🎂', name: 'Rođendanska zabava', desc: 'Prioritetni pristup' },
        { id: 'school', icon: '🎒', name: 'Školski izlet', desc: 'Edukativni program na otvorenom' },
      ],
      months: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
      days: ['Pon','Uto','Sri','Čet','Pet','Sub','Ned'],
      pickActivity: 'Odaberite aktivnost',
      pickActivityLead: 'Dodirnite jednu ili više aktivnosti',
      pickDate: 'Odaberite datum posjeta',
      pickDateLead: 'Otvoreno 9–17 h · zadnji ulaz 15 h',
      yourDetails: 'Vaši podaci',
      confirmTitle: 'Potvrdite rezervaciju',
      confirmLead: 'Pošaljite zahtjev odmah — bez e-maila',
      name: 'Ime i prezime',
      phone: 'Broj telefona',
      guests: 'Broj gostiju',
      arrival: 'Preferirani dolazak',
      arrivalOpts: ['Jutro (9:00–10:30)', 'Kasno jutro (10:30–12:00)', 'Poslijepodne (12:00–14:00)'],
      notes: 'Napomena (opcionalno)',
      notesPh: 'Dob djece, naziv grupe…',
      next: 'Dalje',
      back: 'Natrag',
      confirm: 'Potvrdi i pošalji',
      summary: 'Sažetak rezervacije',
      activity: 'Aktivnost',
      date: 'Datum',
      whatsapp: 'Pošalji WhatsApp',
      sms: 'Pošalji SMS',
      call: 'Pozovi za potvrdu',
      copy: 'Kopiraj detalje',
      copied: 'Kopirano!',
      selectActivity: 'Odaberite barem jednu aktivnost.',
      selectDate: 'Odaberite datum posjeta.',
      fillRequired: 'Unesite ime i telefon.',
      myDiary: 'Moj dnevnik rezervacija',
      myDiaryLead: 'Spremljeno na ovom uređaju',
      emptyDiary: 'Još nema spremljenih rezervacija.',
      saved: 'Rezervacija spremljena u dnevnik!',
      tabBook: 'Rezerviraj',
      tabDiary: 'Dnevnik',
      parkHours: 'Park otvoren 9–17 h',
      msgHeader: 'Zahtjev za rezervaciju Glavani Park',
    },
  };
  const t = i18n[lang];
  const phone = lang === 'hr' ? PHONE_HR : PHONE_EN;

  let step = 0;
  let selectedActivities = new Set();
  let selectedDate = null;
  let viewYear, viewMonth;
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const state = { name: '', phone: '', guests: 2, arrival: 0, notes: '' };

  function pad(n) { return String(n).padStart(2, '0'); }
  function isoDate(d) { return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; }

  function activityNames() {
    return t.activities.filter(a => selectedActivities.has(a.id)).map(a => a.name).join(', ');
  }

  function buildMessage() {
    return [
      t.msgHeader,
      '---',
      `${t.activity}: ${activityNames()}`,
      `${t.date}: ${selectedDate}`,
      `${t.name}: ${state.name}`,
      `${t.phone}: ${state.phone}`,
      `${t.guests}: ${state.guests}`,
      `${t.arrival}: ${t.arrivalOpts[state.arrival]}`,
      `${t.notes}: ${state.notes || '—'}`,
      '---',
      t.pickDateLead,
      'Glavani Park · Glavani 10, Barban, Istria',
    ].join('\n');
  }

  function saveToDiary() {
    const bookings = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    bookings.unshift({
      id: Date.now(),
      activities: activityNames(),
      date: selectedDate,
      name: state.name,
      phone: state.phone,
      guests: state.guests,
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
          const on = selectedActivities.has(a.id);
          return `<button type="button" class="activity-pick${on ? ' activity-pick--on' : ''}" data-id="${a.id}" aria-pressed="${on}">
            <span class="activity-pick__icon">${a.icon}</span>
            <span class="activity-pick__name">${a.name}</span>
            <span class="activity-pick__desc">${a.desc}</span>
          </button>`;
        }).join('')}
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
    return `<section class="book-panel">
      <h2>${t.yourDetails}</h2>
      <div class="booking-form">
        <div class="booking-form__row">
          <div><label for="app-name">${t.name}</label><input id="app-name" type="text" value="${state.name}" required autocomplete="name"></div>
          <div><label for="app-phone">${t.phone}</label><input id="app-phone" type="tel" value="${state.phone}" required autocomplete="tel"></div>
        </div>
        <div class="booking-form__row">
          <div><label for="app-guests">${t.guests}</label><input id="app-guests" type="number" min="1" max="99" value="${state.guests}"></div>
          <div><label for="app-arrival">${t.arrival}</label>
            <select id="app-arrival">${t.arrivalOpts.map((o, i) => `<option value="${i}"${i === state.arrival ? ' selected' : ''}>${o}</option>`).join('')}</select>
          </div>
        </div>
        <div><label for="app-notes">${t.notes}</label><textarea id="app-notes" placeholder="${t.notesPh}">${state.notes}</textarea></div>
      </div>
    </section>`;
  }

  function renderConfirm() {
    const msg = buildMessage();
    return `<section class="book-panel">
      <h2>${t.confirmTitle}</h2>
      <p class="book-panel__lead">${t.confirmLead}</p>
      <div class="book-summary">
        <h3>${t.summary}</h3>
        <dl>
          <dt>${t.activity}</dt><dd>${activityNames()}</dd>
          <dt>${t.date}</dt><dd>${selectedDate}</dd>
          <dt>${t.name}</dt><dd>${state.name}</dd>
          <dt>${t.phone}</dt><dd>${state.phone}</dd>
          <dt>${t.guests}</dt><dd>${state.guests}</dd>
          <dt>${t.arrival}</dt><dd>${t.arrivalOpts[state.arrival]}</dd>
        </dl>
      </div>
      <div class="book-send-grid">
        <a class="btn-whatsapp" id="btn-whatsapp" href="https://wa.me/${phone}?text=${encodeURIComponent(msg)}" target="_blank" rel="noopener">${t.whatsapp}</a>
        <a class="btn-sms" id="btn-sms" href="sms:+${phone}?body=${encodeURIComponent(msg)}">${t.sms}</a>
        <a class="btn-secondary" id="btn-call" href="tel:+${phone}">${t.call}</a>
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
          <span>${b.name} · ${b.guests} ${lang === 'hr' ? 'gostiju' : 'guests'}</span>
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

  function bindStepEvents() {
    root.querySelectorAll('.activity-pick').forEach(btn => {
      btn.addEventListener('click', () => {
        const id = btn.dataset.id;
        if (selectedActivities.has(id)) selectedActivities.delete(id);
        else selectedActivities.add(id);
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

    document.getElementById('book-back')?.addEventListener('click', () => { step--; render(); });

    document.getElementById('book-next')?.addEventListener('click', () => {
      if (step === 0 && selectedActivities.size === 0) { alert(t.selectActivity); return; }
      if (step === 1 && !selectedDate) { alert(t.selectDate); return; }
      if (step === 2) {
        state.name = document.getElementById('app-name')?.value.trim() || '';
        state.phone = document.getElementById('app-phone')?.value.trim() || '';
        state.guests = document.getElementById('app-guests')?.value || 2;
        state.arrival = parseInt(document.getElementById('app-arrival')?.value || '0', 10);
        state.notes = document.getElementById('app-notes')?.value.trim() || '';
        if (!state.name || !state.phone) { alert(t.fillRequired); return; }
      }
      if (step === 2) {
        saveToDiary();
      }
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
