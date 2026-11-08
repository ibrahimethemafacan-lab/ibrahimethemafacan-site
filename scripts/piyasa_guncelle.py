#!/usr/bin/env python3
"""Piyasa kapanışlarıyla getiriler.html, ana sayfa yarış kartı, OG görseli ve makro Dünya sekmesini günceller.

Kullanım:
  python3 scripts/piyasa_guncelle.py kapanis.json
kapanis.json örneği (hepsi gün sonu kapanışı; Matriks kodları):
{
  "tarih": "13 Kasım 2026",
  "GLDGR": 6563.27, "XAGTRY": 2605.11, "USDTRY": 50.149, "XU100": 11482.6, "XU030": 14290.2,
  "NDX": 26989.99, "BTC": 75882,
  "SPX500": 7381.27, "DJIC": 51285.73, "DAX": 25820.36, "UKX": 10673.94, "PX1": 8139.0,
  "NIKX": 57434.77, "KOSPI": 5059.69, "SHCOMP": 3649.18, "XAUUSD": 4070.73, "XAGUSD": 51.95,
  "BRENT": 96.77, "DXY": 102.3, "USTBOND10Y": 4.87,
  "EURUSD": 1.11369, "GBPUSD": 1.33501, "USDJPY": 158.534, "USDKRW": 1364.03, "USDCNY": 6.6765,
  "mevduat_ytd": 45.3,                 # isteğe bağlı: TCMB faiz verisiyle yeniden hesaplanan yılbaşından getiri
  "mevduat_not": "faiz verisi ... haftasına kadar",   # isteğe bağlı
  "tufe_ratio": 1.27507, "tufe_ay": "Ekim 2026"       # isteğe bağlı: yeni TÜFE geldiğinde
}
Ay değişimi otomatiktir: tarihin ayı bir önceki çalıştırmadan farklıysa, önceki çalıştırmanın kapanışları
(bazlar dosyasındaki son_kapanis) yeni ayın bazı (m0) olur; "X ayı" etiketleri de değişir.
"""
import json, os, re, sys, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAZ = os.path.join(ROOT, 'scripts', 'data', 'piyasa_bazlar.json')
GET = os.path.join(ROOT, 'araclar', 'getiriler.html')
MAK = os.path.join(ROOT, 'araclar', 'makro.html')
IDX = os.path.join(ROOT, 'index.html')
OGD = os.path.join(ROOT, 'scripts', 'og')
FXK = {'EUR': 'EURUSD', 'GBP': 'GBPUSD', 'JPY': 'USDJPY', 'KRW': 'USDKRW', 'CNY': 'USDCNY', 'TRY': 'USDTRY'}
KOD = {'S&P 500|ABD': 'SPX500', 'Dow Jones|ABD': 'DJIC', 'Nasdaq-100|ABD': 'NDX', 'DAX|Almanya': 'DAX', 'FTSE 100|İngiltere': 'UKX',
       'CAC 40|Fransa': 'PX1', 'Nikkei 225|Japonya': 'NIKX', 'KOSPI|Güney Kore': 'KOSPI', 'Şanghay|Çin': 'SHCOMP', 'BIST 100|Türkiye': 'XU100',
       'Altın|ons': 'XAUUSD', 'Gümüş|ons': 'XAGUSD', 'Brent petrol|varil': 'BRENT', 'Dolar endeksi|DXY': 'DXY'}
AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
EK_A = {'Ocak': 'a', 'Şubat': 'a', 'Mart': 'a', 'Nisan': 'a', 'Mayıs': 'a', 'Haziran': 'a', 'Temmuz': 'a', 'Ağustos': 'a', 'Eylül': 'e', 'Ekim': 'e', 'Kasım': 'a', 'Aralık': 'a'}


def tl(x, nd=0):
    s = ('{:,.%df}' % nd).format(x)
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')


def pct1(v):
    return ('+' if v >= 0 else '−') + tl(abs(v), 1)


def main():
    K = json.load(open(sys.argv[1]))
    B = json.load(open(BAZ, encoding='utf-8'))
    G = B['getiriler']; W = B['dunya']
    eski_tarih = B['son_tarih']; tarih = K['tarih']
    # Mevduat: 3 aylık vade, vade başındaki faizle basit birikim; yeni vade başlarsa K['mevduat_vade']={'vade_basi':'YYYY-MM-DD','faiz':r}
    import datetime as _dt
    MV = G['mevduat']
    t_gun = _dt.date(int(tarih.split()[2]), AYLAR.index(tarih.split()[1]) + 1, int(tarih.split()[0]))
    if K.get('mevduat_vade'):
        vb_eski = _dt.date.fromisoformat(MV['vade_basi']); vb_yeni = _dt.date.fromisoformat(K['mevduat_vade']['vade_basi'])
        MV['baz_carpan'] = round(MV['baz_carpan'] * (1 + MV['faiz'] / 100 * (vb_yeni - vb_eski).days / 365), 5)
        MV['vade_basi'] = K['mevduat_vade']['vade_basi']; MV['faiz'] = K['mevduat_vade']['faiz']
    vb = _dt.date.fromisoformat(MV['vade_basi'])
    G['mevduat_ytd'] = round((MV['baz_carpan'] * (1 + MV['faiz'] / 100 * (t_gun - vb).days / 365) - 1) * 100, 1)
    G['mevduat_not'] = '3 aya kadar vadeli mevduat; son vade %d %s\'%s %%%s faizle başladı' % (vb.day, AYLAR[vb.month - 1], {'Ekim':'de','Ocak':'ta','Nisan':'da','Temmuz':'da'}.get(AYLAR[vb.month - 1], 'da'), ('%.2f' % MV['faiz']).replace('.', ','))
    if 'tufe_ratio' in K: G['tufe_ratio'] = K['tufe_ratio']
    if 'tufe_ay' in K: G['tufe_ay'] = K['tufe_ay']
    # Ay değişimi otomatik: yeni ayın ilk güncellemesinde bir önceki çalıştırmanın kapanışları ay bazı (m0) olur
    yeni_ay = tarih.split()[1] != eski_tarih.split()[1]
    if yeni_ay:
        if not B.get('son_kapanis'):
            print('HATA: ay değişti ama bazlar dosyasında son_kapanis yok'); sys.exit(2)
        SK = B['son_kapanis']
        W['eski_ay'] = W['ay']; W['onceki_ay'] = eski_tarih.split()[1]; W['ay'] = tarih.split()[1]
        W['dow_notu'] = 'Dow Jones için %s %s' % (eski_tarih.split()[0], eski_tarih.split()[1])
        for v in W['varliklar']:
            v[3] = SK[KOD[v[0]]]
        for c in W['fx']:
            W['fx'][c][1] = SK[FXK[c]]
    U = K['USDTRY']; y0 = G['y0']

    # ---- getiriler.html ----
    ratios = {
        'altin': K['GLDGR'] / y0['GLDGR'], 'gumus': K['XAGTRY'] / y0['XAGTRY'], 'usd': U / y0['USDTRY'],
        'ndx': K['NDX'] * U / (y0['NDX'] * y0['USDTRY']), 'btc': K['BTC'] * U / (y0['BTC'] * y0['USDTRY']),
        'bist': G['temettu']['bist'] * K['XU100'] / y0['XU100'], 'bist30': G['temettu']['bist30'] * K['XU030'] / y0['XU030'],
        'mevduat': 1 + G['mevduat_ytd'] / 100, 'tufe': G['tufe_ratio'],
    }
    ytd = {}; cum = {}
    s = open(GET, encoding='utf-8').read()
    for k, ra in ratios.items():
        y = round((ra - 1) * 100, 1); c = (1 + G['c25'][k] / 100) * ra * 100 - 100
        c = round(c) if c >= 1000 else round(c, 1)
        ytd[k] = y; cum[k] = c
        pat = r"(\{ id: '%s'.*?\['2026\*',)[-\d.]+,[\d.]+(\]\] \})" % k
        s, n = re.subn(pat, lambda m: m.group(1) + '%s,%s' % (y, c) + m.group(2), s, count=1, flags=re.S)
        if n != 1: print('UYARI getiriler satırı bulunamadı:', k)
    gum_gr = K['XAGTRY'] / 31.1035
    R = [(r"158,80 TL → [^']+ TL", "158,80 TL → %s TL" % tl(K['GLDGR'], 2)),
         (r"2,07 TL → [^']+ TL", "2,07 TL → %s TL" % tl(gum_gr, 2)),
         (r"24\.246 TL → [\d.]+ TL", "24.246 TL → %s TL" % tl(K['NDX'] * U)),
         (r"3,79 TL → [^']+ TL", "3,79 TL → %s TL" % tl(U, 2)),
         (r"52\.961 TL → [\d.]+ TL", "52.961 TL → %s TL" % tl(K['BTC'] * U))]
    for a, b in R:
        s, n = re.subn(a, b, s, count=1)
        if n != 1: print('UYARI foot bulunamadı:', a)
    s = s.replace(eski_tarih, tarih)
    s = re.sub(r"itibarıyla \((?:faiz verisi|3 aya kadar vadeli mevduat)[^)]*\)", lambda _m: "itibarıyla (%s)" % G['mevduat_not'].replace("'", "\\'"), s)
    s = re.sub(r"\* \S+ 2026 itibarıyla \(TÜİK", "* %s itibarıyla (TÜİK" % G['tufe_ay'], s)
    B['og_v'] += 1
    s = re.sub(r'og-getiriler\.png\?v=\d+', 'og-getiriler.png?v=%d' % B['og_v'], s)
    open(GET, 'w', encoding='utf-8').write(s)

    # ---- OG görseli ----
    d = [['Bitcoin', cum['btc']], ['NASDAQ-100 (TL)', cum['ndx']], ['Gram altın', cum['altin']], ['Gram gümüş', cum['gumus']],
         ['Konut (İstanbul, kira dahil)', G['konut_cum']], ['Enflasyon (TÜFE)', cum['tufe'], 1], ['TL mevduat (brüt)', cum['mevduat'], 1],
         ['Dolar/TL', cum['usd']], ['BIST 30 (temettü dahil)', cum['bist30']], ['BIST 100 (temettü dahil)', cum['bist']]]
    d.sort(key=lambda x: -x[1])
    og = os.path.join(OGD, 'getiriler.html'); t = open(og, encoding='utf-8').read().split('\n')
    for i, line in enumerate(t):
        if line.startswith('var d='):
            t[i] = 'var d=' + json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('"', "'") + ';'
    t = '\n'.join(t).replace(eski_tarih, tarih)
    open(og, 'w', encoding='utf-8').write(t)
    subprocess.run(['node', os.path.join(OGD, 'render.js'), OGD, 'getiriler'], check=True)
    subprocess.run(['cp', os.path.join(OGD, 'og-getiriler.png'), os.path.join(ROOT, 'img', 'og-getiriler.png')], check=True)

    # ---- ana sayfa yarış kartı ----
    rows = [('TL mevduat', ytd['mevduat'], ''), ('Enflasyon', ytd['tufe'], 'ref'), ('Dolar/TL', ytd['usd'], ''),
            ('Gram altın', ytd['altin'], ''), ('BIST 100', ytd['bist'], ''), ('Gram gümüş', ytd['gumus'], '')]
    rows.sort(key=lambda r: -r[1])
    mx = max(abs(r[1]) for r in rows)
    li = []
    for n, v, cls in rows:
        c = cls or ('neg' if v < 0 else '')
        li.append('            <li%s><span class="hr-n">%s</span><span class="hr-t"><i style="width:%.1f%%"></i></span><b class="hr-v">%s</b></li>'
                  % (' class="%s"' % c if c else '', n, abs(v) / mx * 100, pct1(v)))
    gecen = [n for n, v, cls in rows if cls != 'ref' and v > ytd['tufe']]
    if not gecen: foot = 'Henüz hiçbiri enflasyonu geçemedi.'
    elif len(gecen) == 1: foot = 'Enflasyonu geçen yalnızca %s.' % gecen[0].replace('TL mevduat', 'mevduat')
    else: foot = 'Enflasyonu geçenler: %s.' % ', '.join(gecen)
    gun, ay = tarih.split()[0], tarih.split()[1]
    x = open(IDX, encoding='utf-8').read()
    x = re.sub(r'<ol class="hr-bars">.*?</ol>', '<ol class="hr-bars">\n' + '\n'.join(li) + '\n          </ol>', x, count=1, flags=re.S)
    x = re.sub(r'<span class="hr-sub">[^<]*</span>', '<span class="hr-sub">Yılbaşından %s %s\'%s, TL bazında, %%</span>' % (gun, ay, EK_A[ay]), x, count=1)
    x = re.sub(r'<div class="hr-foot"><span>[^<]*</span>', '<div class="hr-foot"><span>%s</span>' % foot, x, count=1)
    open(IDX, 'w', encoding='utf-8').write(x)

    # ---- makro Dünya sekmesi ----
    fxk = FXK; kod = KOD
    _ = {'S&P 500|ABD': 'SPX500', 'Dow Jones|ABD': 'DJIC', 'Nasdaq-100|ABD': 'NDX', 'DAX|Almanya': 'DAX', 'FTSE 100|İngiltere': 'UKX',
           'CAC 40|Fransa': 'PX1', 'Nikkei 225|Japonya': 'NIKX', 'KOSPI|Güney Kore': 'KOSPI', 'Şanghay|Çin': 'SHCOMP', 'BIST 100|Türkiye': 'XU100',
           'Altın|ons': 'XAUUSD', 'Gümüş|ons': 'XAGUSD', 'Brent petrol|varil': 'BRENT', 'Dolar endeksi|DXY': 'DXY'}
    def usd(v, c, i):
        if not c: return v
        f = W['fx'][c]; r = K[fxk[c]] if i == 2 else f[i]
        return v * r if f[2] == 'm' else v / r
    out = []
    for n, t_, a0, a_m0, c in W['varliklar']:
        l = K[kod[n]]; u = usd(l, c, 2)
        out.append([n, t_, round((u / usd(a_m0, c, 1) - 1) * 100, 1), round((u / usd(a0, c, 0) - 1) * 100, 1), round(l, 2)])
    m = open(MAK, encoding='utf-8').read()
    m, n = re.subn(r'var DN_=\[.*?\]\];', 'var DN_=' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';', m, count=1)
    if n != 1: print('UYARI DN_ bulunamadı')
    # US10: aynı ay ise son değeri değiştir, yeni ay ise ekle
    ay_idx = AYLAR.index(ay) + 1; yil = tarih.split()[2]; ay_key = '%s-%02d' % (yil, ay_idx)
    if ay_key == W['us10_son_ay']:
        m = re.sub(r'(US10=\{v:\[[^\]]*),[-\d.]+\]\};', lambda mm: mm.group(1) + ',%s]};' % K['USTBOND10Y'], m, count=1)
    else:
        m = re.sub(r'(US10=\{v:\[[^\]]*)\]\};', lambda mm: mm.group(1) + ',%s]};' % K['USTBOND10Y'], m, count=1)
        W['us10_son_ay'] = ay_key
    m = re.sub(r'Değerler \d+ \S+ 2026 itibarıyladır;', 'Değerler %s itibarıyladır;' % tarih, m, count=1)
    m = re.sub(r"ayında \(\d+ \S+'[ae] kadar\)", "ayında (%s %s'%s kadar)" % (gun, ay, EK_A[ay]), m, count=1)
    m = re.sub(r"\(\S+: \d+ \S+\), %", "(%s: %s %s), %%" % (W['ay'], gun, ay), m, count=1)
    if yeni_ay:
        ea = W['eski_ay']
        for a, b in [('>%s ayı</button>', '>%s ayı</button>'), ('<th>%s ($)</th>', '<th>%s ($)</th>'), ("'%s değişimi, dolar bazında, %%'", "'%s değişimi, dolar bazında, %%'"),
                     ("dolar endeksi %s ayında", "dolar endeksi %s ayında")]:
            m = m.replace(a % ea, b % W['ay'])
        m = re.sub(r'\S+ değişimi \S+ sonu kapanışına \([^)]*\)', '%s değişimi %s sonu kapanışına (%s)' % (W['ay'], W['onceki_ay'], W['dow_notu']), m, count=1)
    open(MAK, 'w', encoding='utf-8').write(m)

    B['son_tarih'] = tarih
    B['son_kapanis'] = {k: v for k, v in K.items() if isinstance(v, (int, float))}
    json.dump(B, open(BAZ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('tamam:', tarih, '| ytd', {k: ytd[k] for k in ('altin', 'gumus', 'usd', 'ndx', 'btc', 'bist', 'bist30', 'mevduat', 'tufe')})
    print('dünya:', [(o[0].split('|')[0], o[2], o[3]) for o in out])


if __name__ == '__main__':
    main()
