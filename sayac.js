/* Sayfa görüntülenme sayacı (GoatCounter). Ana sayfada çalışmaz; 300'ün altındaki sayıları göstermez. */
(function () {
  var ESIK = 300;
  var yol = location.pathname.replace(/\/index\.html$/, '/').replace(/\/$/, '');
  if (yol === '/cevrimdisi.html') return;
  if (!yol) { toplam(); return; }
  var h1 = document.querySelector('main h1, header.top h1, h1');
  if (!h1) return;
  var ts = '?start=2026-10-24&_=' + Math.floor(Date.now() / 600000);
  var url = 'https://ibrahimethemafacan.goatcounter.com/counter/' + encodeURIComponent(yol).replace(/%2F/g, '/') + '.json' + ts;
  fetch(url, { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
    if (!d || !d.count) return;
    var n = parseInt(String(d.count).replace(/\D/g, ''), 10);
    if (!(n >= ESIK)) return;
    var p = document.createElement('p');
    p.className = 'gc-sayac';
    p.style.cssText = 'font-family:var(--sans,system-ui,sans-serif);font-size:.78rem;color:var(--muted,#6b7280);margin:' + (h1.closest('header.top') ? '-.2rem 0 .8rem' : '-.6rem 0 1.2rem') + ';font-variant-numeric:tabular-nums;letter-spacing:.01em';
    p.setAttribute('title', 'Bu sayfanın yayına girdiği günden bu yana toplam ziyaret (aynı kişinin aynı gün içindeki tekrar açmaları tek sayılır)');
    p.textContent = n.toLocaleString('tr-TR') + ' ziyaret';
    h1.insertAdjacentElement('afterend', p);
  }).catch(function () {});

  /* Ana sayfa: altbilgide sitenin toplam görüntülenmesi */
  function toplam() {
    var tel = document.querySelector('.site-foot .wrap');
    if (!tel) return;
    fetch('https://ibrahimethemafacan.goatcounter.com/counter/TOTAL.json?start=2026-10-24&_=' + Math.floor(Date.now() / 600000), { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d || !d.count) return;
      var n = parseInt(String(d.count).replace(/\D/g, ''), 10);
      if (!(n > 0)) return;
      var p = document.createElement('p');
      p.className = 'gc-toplam';
      p.style.cssText = 'font-size:.8rem;color:var(--muted,#6b7280);margin:.2rem 0 .6rem;font-variant-numeric:tabular-nums';
      p.innerHTML = '24 Ekim 2026\'da yayına girdiğinden bu yana <b style="color:var(--ink,#111);font-weight:700">' + n.toLocaleString('tr-TR') + '</b> ziyaret.';
      var son = tel.querySelector('p:last-of-type');
      if (son) tel.insertBefore(p, son); else tel.appendChild(p);
    }).catch(function () {});
  }
})();
