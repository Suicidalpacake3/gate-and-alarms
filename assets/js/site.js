(function () {
  var doc = document.documentElement;

  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var scrim = document.querySelector('.nav-scrim');
  function setNav(open) {
    doc.classList.toggle('nav-open', open);
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (toggle) toggle.addEventListener('click', function () { setNav(!doc.classList.contains('nav-open')); });
  if (scrim) scrim.addEventListener('click', function () { setNav(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });
  document.querySelectorAll('.nav a').forEach(function (a) { a.addEventListener('click', function () { setNav(false); }); });

  // Header shadow and mobile call bar
  var header = document.querySelector('.site-header');
  var floatBar = document.querySelector('.float-call');
  function onScroll() {
    var y = window.scrollY || 0;
    if (header) header.classList.toggle('scrolled', y > 8);
    if (floatBar) floatBar.classList.toggle('show', y > 520);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Services: open the right detail when arriving from a link
  function openFromHash() {
    var id = decodeURIComponent(location.hash.replace('#', ''));
    if (!id) return;
    var el = document.getElementById(id);
    if (el && el.tagName === 'DETAILS') {
      el.open = true;
      setTimeout(function () { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 60);
    }
  }
  openFromHash();
  window.addEventListener('hashchange', openFromHash);

  // Services: highlight the side index
  var indexLinks = document.querySelectorAll('.svc-index a[href^="#"]');
  if (indexLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    indexLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          indexLinks.forEach(function (a) { a.classList.remove('active'); });
          var a = map[en.target.id];
          if (a) a.classList.add('active');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) so.observe(s); });
  }

  // Contact: build an enquiry for WhatsApp or email
  var form = document.getElementById('enquiry');
  if (form) {
    var msg = form.querySelector('.form-msg');
    function compose() {
      var f = form.elements;
      var name = f.namedItem('name').value.trim();
      var phone = f.namedItem('phone').value.trim();
      var area = f.namedItem('area').value.trim();
      var details = f.namedItem('details').value.trim();
      var picked = Array.prototype.map.call(form.querySelectorAll('input[name="service"]:checked'), function (i) { return i.value; });
      if (!name || !phone) {
        msg.textContent = 'Please add your name and a number Brian can call you back on.';
        return null;
      }
      msg.textContent = '';
      var lines = ['Hi Brian, I would like some help from Gate and Alarms.', ''];
      lines.push('Name: ' + name);
      lines.push('Phone: ' + phone);
      if (area) lines.push('Area: ' + area);
      if (picked.length) lines.push('Service: ' + picked.join(', '));
      if (details) { lines.push(''); lines.push(details); }
      return lines.join('\n');
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var text = compose();
      if (!text) return;
      window.open('https://wa.me/27817182920?text=' + encodeURIComponent(text), '_blank', 'noopener');
    });
    var mailBtn = form.querySelector('[data-send="email"]');
    if (mailBtn) mailBtn.addEventListener('click', function () {
      var text = compose();
      if (!text) return;
      location.href = 'mailto:brian@gateandalarms.co.za?subject=' + encodeURIComponent('Website enquiry') + '&body=' + encodeURIComponent(text);
    });
  }

  // Footer year
  var yr = document.querySelector('[data-year]');
  if (yr) yr.textContent = new Date().getFullYear();
})();
