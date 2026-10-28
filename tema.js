/* Aydınlık / karanlık tema. <head> içinde, stil dosyasından önce yüklenir ki sayfa yanlış renkte yanıp sönmesin. */
(function () {
  var d = document.documentElement, KEY = 'tema';
  var mq = window.matchMedia ? matchMedia('(prefers-color-scheme: dark)') : null;
  function saved() { try { var t = localStorage.getItem(KEY); return t === 'light' || t === 'dark' ? t : null; } catch (e) { return null; } }
  function apply(t) { d.setAttribute('data-theme', t); sync(); }
  function sync() {
    var b = document.querySelector('.theme-toggle'); if (!b) return;
    var lbl = d.getAttribute('data-theme') === 'dark' ? 'Aydınlık moda geç' : 'Karanlık moda geç';
    b.setAttribute('aria-label', lbl); b.title = lbl;
  }
  apply(saved() || (mq && mq.matches ? 'dark' : 'light'));
  document.addEventListener('DOMContentLoaded', sync);
  document.addEventListener('click', function (e) {
    if (!e.target.closest || !e.target.closest('.theme-toggle')) return;
    var t = d.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem(KEY, t); } catch (err) {}
    apply(t);
  });
  if (mq && mq.addEventListener) mq.addEventListener('change', function (m) { if (!saved()) apply(m.matches ? 'dark' : 'light'); });
})();
