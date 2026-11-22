#!/usr/bin/env python3
"""Makro sayfasındaki kart harcamaları verisini üretir (var KK ve var KA).

Girdi: scripts/data/kart_haftalik.json (EVDS bie_kkhartut, cuma tarihli haftalık, bin TL; dates + KT1..KT51)
       scripts/data/tufe.json (TP.TUKFIY2025.GENEL, "YYYY-AA": endeks)
Çıktı: araclar/makro.html içindeki `var KK=...;` (son 4 hafta, nominal yıllık değişim) ve
       `var KA=...;` (son 12 tam ay, aylık reel yıllık değişim) satırları.
Aylık tahmin: haftalık tutar o haftanın yedi gününe eşit dağıtılır, takvim ayına göre toplanır.
"""
import json, re, datetime as D, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = json.load(open(R + '/scripts/data/kart_haftalik.json'))
TU = json.load(open(R + '/scripts/data/tufe.json'))
AY = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
N = {2: "Araba kiralama", 3: "Araç satış, servis, yedek parça", 4: "Akaryakıt", 5: "Çeşitli gıda", 6: "Doğrudan pazarlama",
     7: "Eğitim, kırtasiye", 8: "Elektronik, bilgisayar", 9: "Giyim ve aksesuar", 10: "Havayolları", 11: "Hizmet sektörleri",
     12: "Konaklama", 13: "Kulüp, dernek", 14: "İçkili yerler", 15: "Kuyumcular", 16: "Market ve AVM", 17: "Mobilya, dekorasyon",
     18: "Müteahhit işleri", 19: "Sağlık, kozmetik", 20: "Seyahat, taşımacılık", 21: "Sigorta", 22: "Telekomünikasyon",
     23: "Yapı malzemeleri", 24: "Yemek", 25: "Kamu, vergi ödemeleri", 26: "Bireysel emeklilik", 49: "Diğer"}
dates = [D.date.fromisoformat(d) for d in H['dates']]
tr = lambda d: f"{d.day} {AY[d.month - 1]} {d.year}"
tr2 = lambda a, b: (f"{a.day} {AY[a.month - 1]}" + (f" {a.year}" if a.year != b.year else "") + f"–{tr(b)}")

# --- KK: son 4 hafta / 52 hafta önceki 4 hafta
def son4(k):
    v = H['KT%d' % k]
    return sum(v[-4:]) / 1e6, sum(v[-56:-52]) / 1e6
assert (dates[-1] - dates[-53]).days == 364
rows = [[N[k], round(son4(k)[0], 2), round(son4(k)[1], 2), ""] for k in N]
rows.append(["Toplam", round(son4(1)[0], 2), round(son4(1)[1], 2), "t"])
rows.append(["İnternetten alışveriş", round(son4(50)[0], 2), round(son4(50)[1], 2), "i"])
aylar = sorted(TU)
son_ay = aylar[-1]; y, m = map(int, son_ay.split('-'))
enf = (TU[son_ay] / TU[f"{y - 1}-{m:02d}"] - 1) * 100
KK = {"d": tr(dates[-1]), "a": tr2(dates[-4] - D.timedelta(6), dates[-1]),
      "o": tr2(dates[-56] - D.timedelta(6), dates[-53]), "enf": round(enf, 1), "enfAy": f"{AY[m - 1]} {y}", "r": rows}

# --- KA: aylık reel yıllık değişim, son 12 tam ay
def aylik(k):
    out = {}
    for d, v in zip(dates, H['KT%d' % k]):
        if v is None: continue
        for i in range(7):
            g = d - D.timedelta(i); out[g.strftime('%Y-%m')] = out.get(g.strftime('%Y-%m'), 0) + v / 7
    return out
ilk, son = dates[0] - D.timedelta(6), dates[-1]
def tam(a):
    y, m = map(int, a.split('-')); b = D.date(y, m, 1); e = (D.date(y + (m == 12), m % 12 + 1, 1) - D.timedelta(1))
    return b >= ilk and e <= son
A1 = aylik(1); tamlar = [a for a in sorted(A1) if tam(a) and a in TU]
hedef = [a for a in tamlar if f"{int(a[:4]) - 1}{a[4:]}" in tamlar][-12:]
assert len(hedef) == 12, hedef
def reel(k):
    A = aylik(k); o = []
    for a in hedef:
        p = f"{int(a[:4]) - 1}{a[4:]}"
        o.append(round(((A[a] / A[p]) / (TU[a] / TU[p]) - 1) * 100, 1))
    return o
tot = son4(1)[0]
KA = {"m": hedef, "t": reel(1),
      "s": sorted([[N[k], round(son4(k)[0] / tot * 100, 1), reel(k)] for k in N], key=lambda r: -r[1])}
p = R + '/araclar/makro.html'; s = open(p, encoding='utf-8').read()
js = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
for nm, o in (('KK', KK), ('KA', KA)):
    s, n = re.subn(r'var %s=\{.*?\};\n' % nm, lambda _: 'var %s=%s;\n' % (nm, js(o)), s, count=1, flags=re.S)
    assert n == 1, nm + ' satırı bulunamadı'
open(p, 'w', encoding='utf-8').write(s)
print('KK', KK['d'], 'enf', KK['enf'], '| KA', hedef[0], '→', hedef[-1], 'toplam reel', KA['t'])
for r in KA['s']: print(f"  {r[0]:32s} pay {r[1]:5.1f}  {min(r[2]):6.1f} … {max(r[2]):6.1f}  son {r[2][-1]:6.1f}")
