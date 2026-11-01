/* PWA: servis çalışanı kaydı + "uygulama olarak kur" yardımcısı */
(function () {
  if (!('serviceWorker' in navigator)) return;
  window.addEventListener('load', function () { navigator.serviceWorker.register('/sw.js').catch(function () {}); });

  var standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
  if (standalone) { document.documentElement.classList.add('pwa'); return; }
  var ios = /iphone|ipad|ipod/i.test(navigator.userAgent) && !window.MSStream;
  var mobil = ios || /android/i.test(navigator.userAgent);
  var KEY = 'pwa-kur-kapat';
  try { if (localStorage.getItem(KEY)) return; } catch (e) {}
  if (!mobil) return;

  var deferred = null;
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); deferred = e; goster(); });
  if (ios) document.addEventListener('DOMContentLoaded', goster);

  function goster() {
    if (document.getElementById('pwa-bar') || !document.body) return;
    var css = document.createElement('style');
    css.textContent = '#pwa-bar{position:fixed;left:.75rem;right:.75rem;bottom:.75rem;z-index:60;display:flex;align-items:center;gap:.7rem;background:var(--panel,#fff);color:var(--ink,#0E1C36);border:1px solid var(--rule,#D7E0EC);border-radius:.9rem;padding:.65rem .8rem;box-shadow:0 8px 28px rgba(14,28,54,.18);font-family:var(--sans,system-ui);font-size:.85rem;line-height:1.35}#pwa-bar img{width:40px;height:40px;border-radius:10px;flex:none}#pwa-bar b{display:block;font-size:.9rem}#pwa-bar .pwa-x{all:unset;cursor:pointer;color:var(--muted,#56657E);font-size:1.2rem;padding:0 .2rem;margin-left:auto}#pwa-bar .pwa-go{all:unset;cursor:pointer;background:var(--accent,#1A5FFF);color:#fff;font-weight:700;border-radius:999px;padding:.4rem .85rem;white-space:nowrap}#pwa-sheet{position:fixed;inset:0;z-index:61;background:rgba(14,28,54,.45);display:flex;align-items:flex-end}#pwa-sheet div{background:var(--panel,#fff);color:var(--ink,#0E1C36);width:100%;border-radius:1.1rem 1.1rem 0 0;padding:1.1rem 1.2rem 1.6rem;font-family:var(--sans,system-ui);font-size:.95rem;line-height:1.55}#pwa-sheet h3{margin:0 0 .5rem;font-size:1.05rem}#pwa-sheet ol{margin:.4rem 0 0;padding-left:1.2rem}#pwa-sheet button{all:unset;cursor:pointer;display:block;margin:1rem auto 0;color:var(--accent,#1A5FFF);font-weight:700}';
    document.head.appendChild(css);
    var bar = document.createElement('div'); bar.id = 'pwa-bar';
    bar.innerHTML = '<img src="/img/pwa-192.png" alt=""><span><b>Uygulama olarak kur</b>Ana ekrandan tek dokunuşla aç; notlar ve podcastler çevrimdışı da çalışır.</span><button type="button" class="pwa-go">Kur</button><button type="button" class="pwa-x" aria-label="Kapat">×</button>';
    document.body.appendChild(bar);
    bar.querySelector('.pwa-x').onclick = function () { bar.remove(); try { localStorage.setItem(KEY, '1'); } catch (e) {} };
    bar.querySelector('.pwa-go').onclick = function () {
      if (deferred) { deferred.prompt(); deferred.userChoice.then(function () { bar.remove(); deferred = null; }); return; }
      var sh = document.createElement('div'); sh.id = 'pwa-sheet';
      sh.innerHTML = '<div><h3>iPhone\'a kurmak için</h3>Safari\'de alttaki <b>Paylaş</b> düğmesine (kare ve yukarı ok) dokun, listeden <b>Ana Ekrana Ekle</b>\'yi seç, sağ üstten <b>Ekle</b>\'ye bas.<ol><li>Paylaş düğmesi</li><li>Ana Ekrana Ekle</li><li>Ekle</li></ol>Site, ana ekranda kendi simgesiyle, tam ekran bir uygulama olarak açılır.<button type="button">Tamam</button></div>';
      document.body.appendChild(sh);
      sh.onclick = function (e) { if (e.target === sh || e.target.tagName === 'BUTTON') { sh.remove(); bar.remove(); try { localStorage.setItem(KEY, '1'); } catch (e2) {} } };
    };
  }
})();
