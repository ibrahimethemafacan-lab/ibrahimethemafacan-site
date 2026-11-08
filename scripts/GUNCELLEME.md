# ibrahimethemafacan.com — veri güncelleme el kitabı

Bu dosya, planlı görevlerde (yeni oturumlarda) siteyi güncelleyecek olan Claude içindir.
Depo: `ibrahimethemafacan-lab/ibrahimethemafacan-site`, dal `main`, yerel kopya `/home/claude/ibrahimethemafacan-site`
(yoksa `gh repo clone ibrahimethemafacan-lab/ibrahimethemafacan-site /home/claude/ibrahimethemafacan-site`). Her işe `git pull` ile başla.

## Genel kurallar
- Kullanıcıya Türkçe yaz; işin sonunda SendUserMessage ile kısa özet gönder (ne değişti, hangi tarih, sorun varsa ne).
- Commit: `git -c user.name=Claude -c user.email=noreply@anthropic.com commit -m "..."`; mesajın sonuna oturumun
  attribution satırları (Co-Authored-By ve Claude-Session) eklenir. Push: `git push origin main`.
  Push sonrası `R=$(git ls-remote origin refs/heads/main | cut -f1) && git update-ref refs/remotes/origin/main $R`.
- Tarihçe asla yeniden yazılmaz (force push yok).
- Yayın kontrolü: `gh run list -R ibrahimethemafacan-lab/ibrahimethemafacan-site --limit 2` → "pages build and deployment" success.
- Her değişen sayfa için Playwright testi: pageerror yok, 390 px genişlikte `document.documentElement.scrollWidth` ≤ 390.
  Yerel sunucu: `npx -y http-server -p 8766 -s . -c-1 &`; kapatırken `pkill -f` KULLANMA (kabuğu öldürür);
  `for p in $(ps -eo pid,args | awk '/http-server -p 8766/{print $1}'); do kill $p; done`.
- `style.css` değişirse tüm html'lerde `style.css?v=` sürümünü artır. `index.html` değişince `python3 scripts/gundem.py` çalıştır (gündem bloğunu ve gundem/index.html'i yeniden üretir).
- Veri kaynağı araçları: Matriks MCP `historicalData` (günlük kapanış), Fintables MCP `veri_sorgula` (fonlar, BTC), TCMB EVDS MCP `get_series_data`.
  EVDS "Too Many Requests" verirse 90 sn bekle, tek tek dene.

## 1. Haftalık piyasa güncellemesi (cuma akşamı) — `scripts/piyasa_guncelle.py`
Günceller: `araclar/getiriler.html` (2026 satırları, dipnotlar, tarihler, OG sürümü), `img/og-getiriler.png`,
ana sayfa yarış kartı, `araclar/makro.html` Dünya sekmesi (DN_, US10, notlar). Ay değişimini kendisi yapar.
1. Kapanışları çek (Matriks `historicalData`, interval daily, rawBars true, o günün tarihi):
   GLDGR, XAGTRY, USDTRY, XU100, XU030, NDX, SPX500, DJIC, DAX, UKX, PX1, NIKX, KOSPI, SHCOMP, XAUUSD, XAGUSD, BRENT, DXY,
   USTBOND10Y, EURUSD, GBPUSD, USDJPY, USDKRW, USDCNY (USDCNY günlük bazen boş → son dolu günü al).
   BTC: Fintables `SELECT zaman_utc,kapanis FROM mumlar_gunluk_gh WHERE kod='BTCUSDT' AND zaman_utc>=TIMESTAMP '<tarih-3gün>' ORDER BY zaman_utc`;
   İstanbul günü D'nin kapanışı = zaman_utc (D-1) 21:00 satırı.
   52 hafta zirvesi grafiği (`"zirve"` anahtarı): Matriks `foreignMarkets` marketType=snapshot, symbols 10'ar
   [EIDO,EWY,ARGT,TUR,EWZ,ECH,EWT,EMXC,EPHE,EZA] ve [EEM,EPU,FXI,KSA,QAT,EWM,THD] → her kod için `[price, yearHigh]`
   (lastUpdate cuma gününün ABD kapanışı olmalı; cumartesi çalıştırılırsa snapshot zaten cuma kapanışıdır).
   Mısır: `historicalData` symbol WIEGY, interval weekly, startDate 1 yıl önce → `"FTSE Mısır": [summary.lastPrice, summary.highestPrice]`.
2. `scripts/data/piyasa_bazlar.json` içindeki `mevduat_ytd`'yi gerekirse yenile (bkz. §3), TÜFE değiştiyse `tufe_ratio` ve `tufe_ay` (bkz. §4).
3. JSON yaz (örnek üstbilgide, dosyadaki docstring) ve `python3 scripts/piyasa_guncelle.py kapanis.json` çalıştır.
   Çıktıdaki ytd değerlerini sağduyuyla kontrol et (bir haftada %20'den fazla sıçrama varsa veri hatasıdır).
4. OG görselini `img/og-getiriler.png` olarak Read ile aç, bak. Test, commit ("Verileri <tarih> kapanışına güncelle"), push.

## 2. Fonlar sayfası — `scripts/fonlar_build.py` (cuma)
Veri Fintables'tan; betiğin içindeki sabitleri elle güncelle, sonra `python3 scripts/fonlar_build.py`.
- `M` listesi: aylık `("YYYY-MM", yatırım fonu büyüklüğü mlr TL, yatırımcı sayısı, emeklilik fonu büyüklüğü mlr TL)`; ay içindeyken son satır "ay içi" değeriyle güncellenir, yeni ayda satır eklenir.
  Sorgu: `SELECT g.tarih_europe_istanbul t, f.fon_tipi, ROUND((SUM(g.fon_buyuklugu)/1e9)::numeric,1) b, SUM(g.yatirimci_sayisi) inv, ROUND((SUM(g.gunluk_nakit_giris_cikisi)/1e9)::numeric,2) fl FROM gunluk_fon_degerleri g JOIN fonlar f ON f.fon_kodu=g.fon_kodu WHERE g.tarih_europe_istanbul IN ('<günler>') AND f.fon_tipi IN ('mutual','pension') GROUP BY 1,2 ORDER BY 1,2`
- Aylık net akım dizileri (yatırım `-1423.8,-288.0,...` ve emeklilik `16.2,3.9,...` ile biten): ay içi toplam = günlük `fl` toplamı (mlr TL).
- `SEM` tablosu: şemsiye türüne göre (ad, adet, büyüklük mlr, yatırımcı, 2025 sonu büyüklük, yılbaşından akım). Sorgu:
  `WITH a AS (SELECT COALESCE(f.semsiye_fon,'-') s, COUNT(*) n, ROUND((SUM(g.fon_buyuklugu)/1e9)::numeric,1) b, SUM(g.yatirimci_sayisi) inv FROM gunluk_fon_degerleri g JOIN fonlar f ON f.fon_kodu=g.fon_kodu WHERE g.tarih_europe_istanbul='<tarih>' AND f.fon_tipi='mutual' GROUP BY 1), y AS (SELECT COALESCE(f.semsiye_fon,'-') s, ROUND((SUM(g.gunluk_nakit_giris_cikisi)/1e9)::numeric,1) fy FROM gunluk_fon_degerleri g JOIN fonlar f ON f.fon_kodu=g.fon_kodu WHERE g.tarih_europe_istanbul>='2026-01-01' AND g.tarih_europe_istanbul<='<tarih>' AND f.fon_tipi='mutual' GROUP BY 1) SELECT a.s,a.n,a.b,a.inv,y.fy FROM a LEFT JOIN y ON y.s=a.s ORDER BY a.b DESC`
  2025 sonu sütunu sabittir (Serbest 5047.6, Para piyasası 1466.5, Katılım 331.4, Borçlanma 174.1, Kıymetli madenler 180.6, Hisse 169.3, Fon sepeti 111.0, Değişken 84.6, Karma 4.6, Diğer 1.3).
- Betikteki "<gün> <Ay> 2026" tarih metinlerini ve "Kasım 2026 için ... değeri ve 1–N Kasım akımları" notunu güncelle.
- BES/OKS kartları `scripts/data/egm_ozet.json`'dan üretilir (EGM BES Özet ve OKS Özet ekranları; EGM'ye buradan erişim yok). Kullanıcı ekran görüntüsü gönderdiğinde bes/oks dizilerine yeni tarihli bir kayıt ekle (alanlar dosyada), betiği çalıştır; kartlar, haftalık fark satırı ve tarih metinleri kendiliğinden güncellenir.
  (Göndermediyse dokunma, özet mesajında "BES verisi <tarih>te kaldı, EGM görüntüsü gönderirsen işlerim" de.)
- Sosyal paylaşım görseli: `scripts/og/fonlar.html` içindeki değerleri güncelleyip `cd scripts/og && node render.js "$PWD" fonlar && cp og-fonlar.png ../../img/`.

## 3. Mevduat faizi (getiriler "TL mevduat" satırı)
Yöntem (sayfanın dipnotu): 3 aya kadar vadeli TL mevduat her vade sonunda yenilenir; faiz, vade başındaki haftanın TCMB ağırlıklı
ortalama akım faizidir (EVDS `TP.TRY.MT02`, grup `bie_mt100h`, haftalık cuma). `piyasa_bazlar.json` → `getiriler.mevduat`
{vade_basi, faiz, baz_carpan}; §1 betiği her çalıştırmada ytd'yi kendisi hesaplar, elle bir şey gerekmez.
Yalnızca vade yenilenince (yılın ilk cuması, Nisan/Temmuz/Ekim'in ilk cuması: 2027 için 1 Ocak tatil → ilk veri haftası) kapanış JSON'una
`"mevduat_vade": {"vade_basi": "YYYY-MM-DD", "faiz": <o haftanın TP.TRY.MT02 değeri>}` eklenir; betik baz çarpanı taşır.
Yıl başında ayrıca c25 tabanları ve 2026* satırları 2027'ye devredilir (elle, ocak başında; kullanıcıyla birlikte).

## 4. TÜFE (her ayın 3'ü, TÜİK 10:00)
- Aylık TÜFE % → `piyasa_bazlar.json`: `tufe_ratio *= (1 + aylık/100)`, `tufe_ay = "<Ay> 2026"`; sonra §1 betiği (son kapanışlarla) çalıştırılır.
- `araclar/makro.html` → `D.para` son satırı: `tf` = yıllık TÜFE (%), `rf` = reel politika faizi ≈ ((1+pf/100)/(1+tf/100)−1)×100; KPI ve notlardaki ay adları.
- Gündeme kısa haber eklenmez (kullanıcı isterse ekler).

## 5. TCMB haftalık (perşembe 14:30) — otomatik: `.github/workflows/tcmb-haftalik.yml` → `scripts/tcmb_guncelle.py`
GitHub Actions 14:50 ve 15:40'ta çalışır; yeni hafta geldiyse makro.html'i günceller ve kendi commit'iyle yayınlar.
Planlı Claude görevi (perşembe 15:50) şunları yapar:
1. `git pull`; `git log -3` ile botun commit'i var mı bak. Yoksa `python3 scripts/tcmb_guncelle.py` ile (EVDS MCP değil, API anahtarı GitHub'da; bu oturumda
   anahtar yoksa) EVDS MCP'den serileri çekip aynı mantıkla elle güncelle (seriler: TP.MKNETHAR.M7/M8/M20 akım, M1/M2 stok; TP.AB.TOPLAM/C1/C2 rezerv; TP.HPBITABLO1.18 M3).
2. Net rezerv ve swap hariç net rezerv EVDS'de yok. Bloomberg HT / AA Finans haberinden ("TCMB rezervleri" haberi, perşembe 14:30 sonrası) al:
   `D.nres.n = [yeni, önceki]`, `D.nres.s = [yeni, önceki]`, `D.nres.nd`'yi sil (ya da `d` ile eşitle). Kaynağı kullanıcıya bildir.
3. Test, commit, push, özet mesajı.

## 6. Fon Tarama — `scripts/fontar_build.py` (cuma; veri çekimi ayrı bir alt ajanla)
1. Alt ajana Fintables sorgularını yaptır; çıktı `scripts/data/fontar_funds.json` (yapı: `{"asof","fields_note","rows":[{kod,ad,t,s,rs,uc,n,s1,s2,dd,p0,d0,p1,d1,py,m1,m3,sz,inv,fy,f3,al:{hs,yhs,kamu,ozelb,kkira,okira,kath,mev,km,pp,fonp,gsyf,gyf,vint,dgr}}]}`).
   Evren: `fonlar` tablosunda `((fon_tipi='mutual' AND tefasa_acik) OR fon_tipi IN ('pension','exchange'))`.
   Pencereler (İstanbul günü D için mumlar_gunluk_gh'de zaman_utc = (D-1) 21:00): 1 yıl: `zaman_utc >= '<D-1yıl -1gün> 21:00'`; p1: `<= '<D-1> 21:00'`;
   py: `< '2025-12-31 21:00'` son kayıt (= 31 Aralık 2025 kapanışı, zaman_utc 2025-12-30 21:00); m1: `<= '<D-1ay -1gün> 21:00'`; m3: `<= '<D-3ay -1gün> 21:00'`.
   `gunluk_fon_degerleri`: sz/inv son 10 günün son kaydı; fy 2026-01-01..D; f3 D-3ay..D. Varlık dağılımı: `gunluk_fon_varlik_sinifi_dagilimlari` son 15 günün son tarihi;
   pivot: hs=HS; yhs=YHS; kamu=DT,HB,KBA,KİBD,YBKB; ozelb=OST,FB,VDM,ÖSDB,YBOSB; kkira=KKSTL,KKSD,KKSYD; okira=OSKS,ÖKSYD; kath=KHTL,KHD,KHAU; mev=VMTL,VMD,VMAU;
   km=KM,KMBYF,KMKBA,KMKKS; pp=TR,TPP,BPP,R; fonp=YYF,BYF,YBYF; gsyf=GSYKB,GSYY; gyf=GYKB,GYY; vint=VİNT; dgr=D,BTAS,BTAA,GAS.
   Kısıtlar: yanıt ≤300 satır (fon_kodu aralıklarına böl), yasak: stddev_samp, ln, string_agg, CASE, ARRAY_AGG, FILTER, LEFT, SUBSTRING, SUBSTR, window frame.
   n/s1/s2: günlük getiri sayısı, toplamı, kareler toplamı (LAG ile); dd: pencere içi tepe noktasından en büyük düşüş.
2. `scripts/fontar_build.py` içinde `ASOF = '<gün Ay 2026>'`, r1y koşulundaki `d0 <= '<D-1yıl +11gün>'`, "1 ay ve 3 ay getirileri sırasıyla <gün Ay> ve <gün Ay>'tan" metni; sonra çalıştır.

## 7. Konut sayfası (`araclar/konut.html`) — ayın 19'u ve 27'si kontrol
Kaynaklar ve EVDS grupları: KFE `bie_kfe` (aylık, ay sonuna doğru), yeni/ikinci el `bie_ykfe`/`bie_yokfend`, birim fiyat `bie_birimfiyat` ve kira `bie_bk` (üç aylık),
ticari gayrimenkul `bie_tgfe` (üç aylık), satışlar `bie_akonutsat1..4` (TÜİK, ayın 15-20'si), inşaat `bie_inyprh2`/`bie_inypkl2` (üç aylık).
`list_datagroups(20 veya 50, keywords)` ile "Bitiş" tarihine bak; sayfadaki son dönemden yeniyse veriyi çekip sayfadaki ilgili diziyi ve açıklama metinlerini güncelle
(sayfa yapısı: üst lede, `<h2 class="gh">` bölümleri, Kaynak notunda dönem cümleleri). Yeni veri yoksa dokunma, kısa "yeni veri yok" mesajı yeterli.

## 8. Gündem kısa haberi
`gundem/akis.json` en başa `{"tarih","tur":"kisa","etiket","metin"(HTML), "ek"(isteğe bağlı HTML)}` ekle, `python3 scripts/gundem.py`, commit.
Kullanıcının metnini aynen koy; yalnızca yazım hatası düzelt.
