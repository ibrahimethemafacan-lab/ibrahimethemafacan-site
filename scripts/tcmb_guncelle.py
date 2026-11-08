#!/usr/bin/env python3
"""TCMB haftalık verilerini EVDS'den çekip araclar/makro.html içindeki D verisini günceller.

Kullanım:
  EVDS_KEY=... python3 scripts/tcmb_guncelle.py            # gerçek çekim
  python3 scripts/tcmb_guncelle.py --mock dosya.json        # test: seriler dosyadan
Çıkış kodu 0; stdout'ta 'DEGISTI' ya da 'GUNCEL' satırı basılır (iş akışı buna bakar).

Güncellenenler: D.wk (son 12 hafta), D.yf 2026* kümülatifi, D.stok, D.res, D.nres.d/.b,
D.m3yoy, D.para son satırının m3/m3v/res değerleri, KPI ve notlardaki hafta tarihi,
'Veriler ... itibarıyla' tarihi. Net ve swap hariç net rezerv EVDS'de yok; onlar
D.nres.n/.s olarak elle (ya da planlı Claude görevinde) girilir; script yalnızca
D.nres.nd ile bu değerlerin hangi haftaya ait olduğunu işaretler."""
import json, os, re, sys, urllib.request, datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, 'araclar', 'makro.html')
SERIES = {
    'h': 'TP.MKNETHAR.M7', 'b': 'TP.MKNETHAR.M8', 't': 'TP.MKNETHAR.M20',
    'sh': 'TP.MKNETHAR.M1', 'sb': 'TP.MKNETHAR.M2',
    'rt': 'TP.AB.TOPLAM', 'rg': 'TP.AB.C1', 'rd': 'TP.AB.C2',
    'm3': 'TP.HPBITABLO1.18',
}
AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
# ay adı -> ('e/'a, 'de/'da/'ta)
EK = {'Ocak': ("'a", "'ta"), 'Şubat': ("'a", "'ta"), 'Mart': ("'a", "'ta"), 'Nisan': ("'a", "'da"), 'Mayıs': ("'a", "'ta"),
      'Haziran': ("'a", "'da"), 'Temmuz': ("'a", "'da"), 'Ağustos': ("'a", "'ta"), 'Eylül': ("'e", "'de"), 'Ekim': ("'e", "'de"),
      'Kasım': ("'a", "'da"), 'Aralık': ("'a", "'ta")}


def gun_ay(d):  # 'dd-mm-yyyy' -> '30 Ekim'
    g, a, _ = d.split('-')
    return '%d %s' % (int(g), AYLAR[int(a) - 1])


def tarih(d):
    return dt.datetime.strptime(d, '%d-%m-%Y').date()


def evds(code, start, end, key):
    url = 'https://evds3.tcmb.gov.tr/igmevdsms-dis/series=%s&startDate=%s&endDate=%s&type=json' % (code, start, end)
    req = urllib.request.Request(url, headers={'key': key, 'User-Agent': 'ibrahimethemafacan.com guncelleme'})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    col = code.replace('.', '_')
    out = []
    for it in d.get('items', []):
        v = it.get(col)
        if v in (None, ''):
            continue
        out.append((it['Tarih'], float(v)))
    return out


def main():
    mock = None
    if '--mock' in sys.argv:
        mock = json.load(open(sys.argv[sys.argv.index('--mock') + 1]))
    key = os.environ.get('EVDS_KEY', '')
    if not mock and not key:
        print('EVDS_KEY yok'); sys.exit(2)
    bugun = dt.date.today()
    start = (bugun - dt.timedelta(days=420)).strftime('%d-%m-%Y')
    end = bugun.strftime('%d-%m-%Y')
    S = {}
    for k, code in SERIES.items():
        S[k] = [tuple(x) for x in mock[k]] if mock else evds(code, start, end, key)
        if not S[k]:
            print('seri boş:', code); sys.exit(3)

    html = open(HTML, encoding='utf-8').read()
    m = re.search(r'var D = (\{.*?\});\n', html)
    D = json.loads(m.group(1))
    eski = D['wk'][0]['d']
    son = S['t'][-1][0]
    if tarih(son) <= tarih(eski):
        print('GUNCEL', eski); return
    # yeni haftalar (eskiden yeniye)
    byd = {k: dict(S[k]) for k in ('h', 'b', 't')}
    yeni = [d for d, _ in S['t'] if tarih(d) > tarih(eski)]
    yil = D['yf'][-1]['y'].rstrip('*')
    for d in yeni:
        row = {'d': d, 'h': round(byd['h'].get(d, 0), 2), 'b': round(byd['b'].get(d, 0), 2), 't': round(byd['t'][d], 2)}
        D['wk'].insert(0, row)
        if d.endswith(yil):
            for k in ('h', 'b', 't'):
                D['yf'][-1][k] = round(D['yf'][-1][k] + row[k], 2)
    D['wk'] = D['wk'][:12]
    D['stok'] = {'h': round(S['sh'][-1][1], 2), 'b': round(S['sb'][-1][1], 2)}
    # rezerv (aynı haftaya ait son değer)
    rez_d, rez_t = S['rt'][-1]
    g = dict(S['rg']).get(rez_d); dv = dict(S['rd']).get(rez_d)
    onceki_b = D['nres']['b'][0]
    rez_yeni = round(rez_t / 1000, 1) != onceki_b or gun_ay(rez_d) + ' ' + rez_d[-4:] != D['nres']['d']
    if rez_yeni:
        D['res'] = {'t': round(rez_t, 1), 'g': round(g, 1) if g is not None else D['res']['g'], 'd': round(dv, 1) if dv is not None else D['res']['d']}
        if D['nres'].get('nd') is None:
            D['nres']['nd'] = D['nres']['d']   # net/swap hariç değerler hâlâ eski haftaya ait
        D['nres']['d'] = gun_ay(rez_d) + ' ' + rez_d[-4:]
        D['nres']['b'] = [round(rez_t / 1000, 1), onceki_b]
        D['para'][-1]['res'] = round(rez_t / 1000, 1)
    # M3 ve yıllık büyüme
    m3 = S['m3']
    m3_d, m3_v = m3[-1]
    hedef = tarih(m3_d) - dt.timedelta(days=364)
    ref = min(m3, key=lambda x: abs((tarih(x[0]) - hedef).days))
    yoy = round((m3_v / ref[1] - 1) * 100, 1)
    D['m3yoy'] = yoy
    D['para'][-1]['m3'] = yoy
    D['para'][-1]['m3v'] = round(m3_v / 1e9, 2)

    js = json.dumps(D, ensure_ascii=False, separators=(',', ':'))
    html = html[:m.start(1)] + js + html[m.end(1):]
    # metinlerdeki hafta tarihi
    e_ga, y_ga = gun_ay(eski), gun_ay(son)
    e_ay, y_ay = e_ga.split()[1], y_ga.split()[1]
    R = [
        ("rezervi, milyar $, %s'" % e_ga, "rezervi, milyar $, %s'" % y_ga),
        ("2026 satırı %s\\%s kadardır. %s itibarıyla" % (e_ga, EK[e_ay][0], e_ga), "2026 satırı %s\\%s kadardır. %s itibarıyla" % (y_ga, EK[y_ay][0], y_ga)),
        ("para arzı %s\\%s kadar" % (e_ga, EK[e_ay][0]), "para arzı %s\\%s kadar" % (y_ga, EK[y_ay][0])),
        ("rezervler %s haftası" % e_ga, "rezervler %s haftası" % y_ga),
        ("%s\\%s brüt rezervin" % (e_ga, EK[e_ay][1]), "%s\\%s brüt rezervin" % (y_ga, EK[y_ay][1])),
    ]
    eksik = []
    for a, b in R:
        if a in html:
            html = html.replace(a, b)
        else:
            eksik.append(a)
    html = re.sub(r'Veriler \d+ \S+ 20\d\d itibarıyla', 'Veriler %d %s %d itibarıyla' % (bugun.day, AYLAR[bugun.month - 1], bugun.year), html, count=1)
    open(HTML, 'w', encoding='utf-8').write(html)
    print('DEGISTI', eski, '->', son, '| yeni hafta:', len(yeni), '| rezerv:', 'yeni' if rez_yeni else 'aynı', '| m3yoy:', yoy)
    if eksik:
        print('UYARI eşleşmeyen metin:', eksik)


if __name__ == '__main__':
    main()
