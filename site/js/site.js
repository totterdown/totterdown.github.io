// Cookie consent and Google Analytics. Does nothing unless the page carries
// <meta name="ga-id">, which _build/lib.py adds when GA_ID is set.
// Analytics loads only after the visitor chooses "Allow".
(function () {
  var meta = document.querySelector('meta[name="ga-id"]');
  var KEY = 'analytics-consent';

  function stored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function store(v) {
    try { if (v) { localStorage.setItem(KEY, v); } else { localStorage.removeItem(KEY); } } catch (e) {}
  }

  function loadGA(id) {
    if (window.gtag) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', id);
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(s);
  }

  function banner(id) {
    var box = document.createElement('div');
    box.className = 'consent';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Cookie choice');
    box.innerHTML = '<p>Can we use analytics cookies to count visits? They help us see which guides are useful. ' +
      '<a href="/privacy/#analytics">Privacy</a></p>' +
      '<div class="consent-actions"><button type="button" data-v="granted">Allow</button>' +
      '<button type="button" class="secondary" data-v="denied">No thanks</button></div>';
    box.addEventListener('click', function (e) {
      var v = e.target.getAttribute && e.target.getAttribute('data-v');
      if (!v) return;
      store(v);
      box.remove();
      if (v === 'granted') loadGA(id);
    });
    document.body.appendChild(box);
  }

  // Count clicks on the "Make an offer" button as a lead, when analytics is on.
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('[data-lead]');
    if (el && window.gtag) window.gtag('event', 'generate_lead', { lead_source: el.getAttribute('data-lead') });
    if (e.target.closest && e.target.closest('[data-consent-reset]')) {
      store(null);
      location.reload();
    }
  });

  if (!meta) return;
  var id = meta.getAttribute('content');
  var choice = stored();
  if (choice === 'granted') loadGA(id);
  else if (choice !== 'denied') banner(id);
})();
