/* Sayfa görüntülenme sayacı (GoatCounter). Ana sayfada çalışmaz; 300'ün altındaki sayıları göstermez. */
(function () {
  var ESIK = 300;
  var yol = location.pathname.replace(/\/index\.html$/, '/').replace(/\/$/, '');
  if (!yol || yol === '/cevrimdisi.html') return;
  var h1 = document.querySelector('main h1, header.top h1, h1');
  if (!h1) return;
  var url = 'https://ibrahimethemafacan.goatcounter.com/counter/' + encodeURIComponent(yol).replace(/%2F/g, '/') + '.json';
  fetch(url, { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
    if (!d || !d.count) return;
    var n = parseInt(String(d.count).replace(/\D/g, ''), 10);
    if (!(n >= ESIK)) return;
    var p = document.createElement('p');
    p.className = 'gc-sayac';
    p.style.cssText = 'font-family:var(--sans,system-ui,sans-serif);font-size:.78rem;color:var(--muted,#6b7280);margin:' + (h1.closest('header.top') ? '-.2rem 0 .8rem' : '-.6rem 0 1.2rem') + ';font-variant-numeric:tabular-nums;letter-spacing:.01em';
    p.setAttribute('title', 'Bu sayfanın yayına girdiği günden bu yana toplam görüntülenme');
    p.textContent = n.toLocaleString('tr-TR') + ' görüntülenme';
    h1.insertAdjacentElement('afterend', p);
  }).catch(function () {});
})();
