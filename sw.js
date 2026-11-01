/* ibrahimethemafacan.com servis çalışanı
   - Sayfalar (HTML): önce ağ, ağ yoksa önbellek; yoksa çevrimdışı sayfası.
   - Stil, betik, görsel, yazı tipi: önbellek öncelikli, arka planda tazele.
   - Podcast mp3: dinlenince önbelleğe alınır, sonra çevrimdışı da çalar.
   Sürüm değişince eski önbellekler silinir. */
var SURUM = 'iea-v1';
var SAYFA = SURUM + '-sayfa', VARLIK = SURUM + '-varlik', SES = SURUM + '-ses';
var ONYUKLE = ['/', '/index.html', '/style.css', '/tema.js', '/pwa.js', '/cevrimdisi.html',
  '/img/logo.png', '/img/logo-dark.png', '/img/pwa-192.png', '/calisma-masasi/'];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(SAYFA).then(function (c) {
    return Promise.all(ONYUKLE.map(function (u) { return c.add(new Request(u, { cache: 'reload' })).catch(function () {}); }));
  }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.filter(function (k) { return k.indexOf('iea-') === 0 && k.indexOf(SURUM) !== 0; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function ayniKaynak(url) { return url.origin === self.location.origin; }

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);
  if (!ayniKaynak(url)) return;                      // Google Fonts, GoatCounter vb. dokunma
  if (url.pathname === '/sw.js') return;

  // Sayfalar: ağ öncelikli
  if (req.mode === 'navigate' || (req.headers.get('accept') || '').indexOf('text/html') > -1) {
    e.respondWith(fetch(req).then(function (r) {
      if (r && r.ok) { var kopya = r.clone(); caches.open(SAYFA).then(function (c) { c.put(stripQuery(req), kopya); }); }
      return r;
    }).catch(function () {
      return caches.match(stripQuery(req)).then(function (r) { return r || caches.match('/cevrimdisi.html'); });
    }));
    return;
  }

  // Ses: önbellek öncelikli, yoksa ağdan al ve sakla (Range isteklerinde tam dosyayı sakla)
  if (/\.(mp3|m4a|ogg)$/.test(url.pathname)) {
    e.respondWith(caches.open(SES).then(function (c) {
      return c.match(url.pathname).then(function (r) {
        if (r) return rangeCevap(r, req);
        return fetch(new Request(url.pathname)).then(function (net) {
          if (net && net.ok && net.status === 200) c.put(url.pathname, net.clone());
          return rangeCevap(net, req);
        });
      });
    }));
    return;
  }

  // Diğer varlıklar: önbellekten ver, arka planda tazele
  e.respondWith(caches.open(VARLIK).then(function (c) {
    return c.match(req).then(function (r) {
      var ag = fetch(req).then(function (net) { if (net && net.ok) c.put(req, net.clone()); return net; }).catch(function () { return r; });
      return r || ag;
    });
  }));
});

function stripQuery(req) { var u = new URL(req.url); u.search = ''; return u.toString(); }

/* Önbellekteki tam ses dosyasından Range (kısmi içerik) yanıtı üret: iOS Safari sarma için buna ihtiyaç duyar */
function rangeCevap(res, req) {
  var range = req.headers.get('range');
  if (!range || !res || res.status !== 200) return res;
  return res.arrayBuffer().then(function (buf) {
    var m = /bytes=(\d+)-(\d*)/.exec(range); var start = +m[1], end = m[2] ? +m[2] : buf.byteLength - 1;
    if (start >= buf.byteLength) return new Response(null, { status: 416, headers: { 'Content-Range': 'bytes */' + buf.byteLength } });
    var parca = buf.slice(start, end + 1);
    return new Response(parca, { status: 206, statusText: 'Partial Content', headers: {
      'Content-Type': res.headers.get('Content-Type') || 'audio/mpeg', 'Content-Length': parca.byteLength,
      'Content-Range': 'bytes ' + start + '-' + end + '/' + buf.byteLength, 'Accept-Ranges': 'bytes' } });
  });
}

/* Sayfadan gelen "bu dersi çevrimdışı indir" isteği */
self.addEventListener('message', function (e) {
  var d = e.data || {};
  if (d.tip === 'indir' && Array.isArray(d.urller)) {
    e.waitUntil(caches.open(SES).then(function (c) {
      var n = 0;
      return Promise.all(d.urller.map(function (u) {
        return c.match(u).then(function (r) { if (r) return; return fetch(u).then(function (net) { if (net.ok) { n++; return c.put(u, net); } }); });
      })).then(function () { if (e.source) e.source.postMessage({ tip: 'indirildi', yeni: n, toplam: d.urller.length }); });
    }));
  }
});
