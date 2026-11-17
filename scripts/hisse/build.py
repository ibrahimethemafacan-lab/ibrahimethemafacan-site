#!/usr/bin/env python3
"""Hisse tarama sayfasını Rasathane verisi ve kodundan üretir (geliştirme sürümü)."""
import json, re, sys
REPO = '/home/claude/ibrahimethemafacan-site'
W = '/home/claude/onizleme'
D = json.load(open(W + '/rasathane_data.json'))
IHR = json.load(open(W + '/ihracat.json'))
meta = open(W + '/rasathane_meta.txt').read()
L = open(W + '/rasathane_222_.txt').read().split('\n')
ln = lambda a, b: '\n'.join(L[a - 222:b - 222 + 1])

# --- veri dosyası
js = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
open(REPO + '/araclar/hisse-tarama-veri.js', 'w', encoding='utf-8').write(
    '// Hisse tarama verisi (geliştirme). Kaynak: Matriks, Fintables.\n'
    'const RAW=%s;\n%s\nconst DET=%s;\nconst SCR=%s;\nconst MACD=%s;\nconst IHR=%s;\n' % (
        js(D['RAW']), meta, js(D['DET']), js(D['SCR']), js(D['MACD']), js(IHR)))

# --- Rasathane kodundan alınan parçalar
core = '\n'.join([ln(225, 232), ln(289, 361), ln(362, 431), ln(437, 520)])
core = core.replace('const $=id=>document.getElementById(id);', '')
for a, b in [('class="sub"', 'class="hsub"'), (':"sub"}', ':"hsub"}'), ('class="note"', 'class="hnote"'),
             ('class="more"', 'class="hmore"'), ('className="more"', 'className="hmore"'),
             ('class="chart"', 'class="hchart"'), ('class="mini"', 'class="hmini"'),
             ('“Güncel” satırı 16 Ekim kapanışı ile', '“Güncel” satırı son kapanış ile'),
             ('sp.m==="scr"&&sp.s', 'sp.m==="scr"&&sp.s')]:
    core = core.replace(a, b)
assert 'class="sub' not in core and 'class="note' not in core, 'kalan sınıf'

page = open(W + '/hisse_sablon.html', encoding='utf-8').read()
src = open(REPO + '/araclar/fon-tarama.html', encoding='utf-8').read()
ver = re.search(r'style\.css\?v=([0-9a-z]+)', src).group(1)
head_nav = src[src.index('<body>'):src.index('<main')]
foot = src[src.index('<footer'):src.index('</footer>') + 9]
page = (page.replace('%%VER%%', ver).replace('%%HEADER%%', head_nav).replace('%%FOOTER%%', foot)
        .replace('%%CORE%%', core))
open(REPO + '/araclar/hisse-tarama.html', 'w', encoding='utf-8').write(page)
print('ok', len(page))
