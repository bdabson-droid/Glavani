/**
 * Glavani Park booking diary — client-side calendar + reservation request.
 * Submits via email (mailto) or phone; no backend required.
 */
(function () {
  const form = document.getElementById('booking-form');
  const calendarEl = document.getElementById('booking-calendar');
  const monthLabel = document.getElementById('calendar-month');
  const dateInput = document.getElementById('booking-date');
  const prevBtn = document.getElementById('cal-prev');
  const nextBtn = document.getElementById('cal-next');
  if (!form || !calendarEl) return;

  const lang = document.documentElement.lang || 'en';
  const i18n = {
    en: {
      months: ['January','February','March','April','May','June','July','August','September','October','November','December'],
      days: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
      closed: 'Past dates unavailable',
      lastEntry: 'Arrive before 3 PM for last entry',
      subject: 'Glavani Park booking request',
      types: { individual: 'Individual / family day ticket', group: 'Group visit', birthday: 'Birthday party', team: 'Team building / corporate', school: 'School trip' },
    },
    hr: {
      months: ['Siječanj','Veljača','Ožujak','Travanj','Svibanj','Lipanj','Srpanj','Kolovoz','Rujan','Listopad','Studeni','Prosinac'],
      days: ['Pon','Uto','Sri','Čet','Pet','Sub','Ned'],
      closed: 'Prošli datumi nisu dostupni',
      lastEntry: 'Dolazak do 15 h za zadnji ulaz',
      subject: 'Zahtjev za rezervaciju Glavani Park',
      types: { individual: 'Pojedinačna / obiteljska ulaznica', group: 'Grupni posjet', birthday: 'Rođendanska zabava', team: 'Team building / korporativno', school: 'Školski izlet' },
    },
  };
  const t = i18n[lang.startsWith('hr') ? 'hr' : 'en'];

  let viewYear, viewMonth, selectedDate = null;
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  function pad(n) { return String(n).padStart(2, '0'); }
  function isoDate(d) { return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`; }

  function renderCalendar() {
    const first = new Date(viewYear, viewMonth, 1);
    const startDay = (first.getDay() + 6) % 7;
    const daysInMonth = new Date(viewYear, viewMonth + 1, 0).getDate();
    monthLabel.textContent = `${t.months[viewMonth]} ${viewYear}`;

    let html = '<div class="cal-grid cal-grid--head">';
    t.days.forEach(d => { html += `<span class="cal-cell cal-cell--head">${d}</span>`; });
    html += '</div><div class="cal-grid">';

    for (let i = 0; i < startDay; i++) html += '<span class="cal-cell cal-cell--empty"></span>';

    for (let day = 1; day <= daysInMonth; day++) {
      const d = new Date(viewYear, viewMonth, day);
      const iso = isoDate(d);
      const isPast = d < today;
      const isSelected = selectedDate === iso;
      const cls = ['cal-cell', 'cal-day', isPast ? 'cal-day--past' : 'cal-day--open', isSelected ? 'cal-day--selected' : ''].filter(Boolean).join(' ');
      html += `<button type="button" class="${cls}" data-date="${iso}" ${isPast ? 'disabled' : ''} aria-label="${iso}">${day}</button>`;
    }
    html += '</div>';
    calendarEl.innerHTML = html;

    calendarEl.querySelectorAll('.cal-day--open').forEach(btn => {
      btn.addEventListener('click', () => {
        selectedDate = btn.dataset.date;
        dateInput.value = selectedDate;
        renderCalendar();
      });
    });
  }

  function initCalendar() {
    viewYear = today.getFullYear();
    viewMonth = today.getMonth();
    renderCalendar();
  }

  prevBtn?.addEventListener('click', () => {
    viewMonth--;
    if (viewMonth < 0) { viewMonth = 11; viewYear--; }
    renderCalendar();
  });

  nextBtn?.addEventListener('click', () => {
    viewMonth++;
    if (viewMonth > 11) { viewMonth = 0; viewYear++; }
    renderCalendar();
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const fd = new FormData(form);
    const date = fd.get('date') || selectedDate;
    if (!date) {
      alert(lang.startsWith('hr') ? 'Odaberite datum u kalendaru.' : 'Please select a date on the calendar.');
      return;
    }
    const typeKey = fd.get('visit_type');
    const typeLabel = t.types[typeKey] || typeKey;
    const body = [
      lang.startsWith('hr') ? 'Zahtjev za rezervaciju Glavani Park' : 'Glavani Park booking request',
      '---',
      `${lang.startsWith('hr') ? 'Datum' : 'Date'}: ${date}`,
      `${lang.startsWith('hr') ? 'Ime' : 'Name'}: ${fd.get('name')}`,
      `${lang.startsWith('hr') ? 'Telefon' : 'Phone'}: ${fd.get('phone')}`,
      `${lang.startsWith('hr') ? 'Email' : 'Email'}: ${fd.get('email') || '—'}`,
      `${lang.startsWith('hr') ? 'Broj gostiju' : 'Guests'}: ${fd.get('guests')}`,
      `${lang.startsWith('hr') ? 'Vrsta posjeta' : 'Visit type'}: ${typeLabel}`,
      `${lang.startsWith('hr') ? 'Dolazak' : 'Arrival'}: ${fd.get('arrival')}`,
      `${lang.startsWith('hr') ? 'Napomena' : 'Notes'}: ${fd.get('notes') || '—'}`,
      '---',
      t.lastEntry,
    ].join('\n');

    window.location.href = `mailto:info@glavanipark.com?subject=${encodeURIComponent(t.subject + ' – ' + date)}&body=${encodeURIComponent(body)}`;
  });

  initCalendar();
})();
