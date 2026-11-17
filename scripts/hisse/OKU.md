# Hisse tarama (geliştirme dalı: hisse-tarama)

Yayında değil; ana sayfadaki kart "yakında" durumunda. Borsa İstanbul gün sonu veri lisansı gelince ana dala alınacak.

- `araclar/hisse-tarama.html`: sayfa (hızlı taramalar + sektör haritası + detaylı tarama + hisse sayfası).
- `araclar/hisse-tarama-veri.js`: veri (RAW, META, DET, SCR, MACD, IHR). **Depoya konmaz** (lisans); Rasathane
  sayfasındaki (claude.ai/artifact/YSxF6NuM5N994Yj11kMXs7) aynı adlı sabitlerden `build.py` ile üretilir.
- `sablon.html` + `build.py`: sayfayı üretir. `ihracat.json`: Fintables, son 12 ay yurt dışı satış / satış (%), >= %20.
  Sorgu: gelir tablosu kalemleri `Satış Gelirleri` ve `Yurt Dışı Satışlar`, `try_ttm`, şirketin son dönemi.
- Hızlı taramalar BIST: ihr (>= %50), macd (günlük, son 5 gün), zirve (52h haftalık kapanış zirvesine %5),
  dip (PD/DD dibine %10 + 3 çeyrek kârlı), nakit (net nakit/PD >= %20), favok ($ FAVÖK 2 çeyrek yıllık artış).
  ABD/Çin taramaları geçici; piyasa bazında ayrıca çalışılacak.
