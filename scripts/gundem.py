#!/usr/bin/env python3
"""Piyasa Gündemi üreticisi.

Tek veri kaynağı: gundem/akis.json (en yeni en üstte). Her öğe:
  kısa haber: {"tarih": "2026-11-03", "tur": "kisa", "etiket": "Makro", "metin": "…(HTML)"}
  yazı:       {"tarih": "2026-10-28", "tur": "yazi", "etiket": "Mevzuat", "url": "/gundem/….html",
               "baslik": "…", "ozet": "…"}

Çalıştırınca:
  1) index.html içindeki Piyasa Gündemi listesini son kısa haberler + son yazı ile yeniden yazar,
  2) gundem/index.html (takvimli gündem arşivi) sayfasını üretir.
Kullanım: python3 scripts/gundem.py
"""
import json, os, re, html, datetime

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
ANA_SAYI = 2  # ana sayfada gösterilecek en yeni kayıt sayısı
IKON = ('<svg class="brief-ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 8a5 5 0 0 0-5 5v3h10v-3a5 5 0 0 0-5-5Z" '
        'fill="#D64545"/><rect x="5" y="16.4" width="14" height="2.6" rx="1.3" fill="#A33A2E"/><path d="M12 5V2.8M5.6 7.2 4 '
        '5.6M18.4 7.2 20 5.6" stroke="#D64545" stroke-width="1.8" stroke-linecap="round"/></svg>')


def tr_tarih(d):
    y, a, g = map(int, d.split('-'))
    return f'{g} {AYLAR[a - 1]} {y}'


def li(it, ind='          '):
    if it['tur'] == 'kisa':
        return (f'{ind}<li class="brief">\n{ind}  <div class="meta">{IKON}{tr_tarih(it["tarih"])} · {html.escape(it["etiket"])} · Kısa haber</div>\n'
                f'{ind}  <p class="note-text">{it["metin"]}</p>\n{ind}</li>\n')
    return (f'{ind}<li class="post">\n{ind}  <div class="meta">{tr_tarih(it["tarih"])} · {html.escape(it["etiket"])}</div>\n'
            f'{ind}  <a href="{it["url"]}">{it["baslik"]}</a>\n'
            f'{ind}  <p class="note-summary">{it["ozet"]}</p>\n'
            f'{ind}  <a class="more" href="{it["url"]}" aria-hidden="true" tabindex="-1">Yazıyı oku →</a>\n{ind}</li>\n')


def takvim_js(akis, hedef, kok_id):
    """Takvim betiği: hedef(d) bir güne tıklanınca ne olacağını belirleyen JS ifadesi ('d' değişkeni)."""
    gunler = {}
    for x in akis:
        g = gunler.setdefault(x['tarih'], [0, 0]); g[0 if x['tur'] == 'kisa' else 1] += 1
    return ('(function(){var G=' + json.dumps(gunler) + ',AY=' + json.dumps(AYLAR, ensure_ascii=False) + ',R=document.getElementById("' + kok_id + '");'
            'var aylar=Object.keys(G).map(function(d){return d.slice(0,7);}).filter(function(v,i,a){return a.indexOf(v)===i;}).sort(),ay=aylar[aylar.length-1];'
            'function tr(d){var p=d.split("-");return (+p[2])+" "+AY[+p[1]-1]+" "+p[0];}'
            'function ciz(){var y=+ay.slice(0,4),m=+ay.slice(5,7);R.querySelector(".ct").textContent=AY[m-1]+" "+y;var i=aylar.indexOf(ay);'
            'R.querySelector(".cp").disabled=i<=0;R.querySelector(".cn").disabled=i>=aylar.length-1;'
            'var ilk=(new Date(y,m-1,1).getDay()+6)%7,n=new Date(y,m,0).getDate(),h=["Pt","Sa","Ça","Pe","Cu","Ct","Pz"].map(function(d){return \'<span class="dw">\'+d+"</span>";}).join("");'
            'for(var k=0;k<ilk;k++)h+="<span></span>";var bg=new Date(),bs=bg.getFullYear()+"-"+String(bg.getMonth()+1).padStart(2,"0")+"-"+String(bg.getDate()).padStart(2,"0");'
            'for(var g=1;g<=n;g++){var d=ay+"-"+String(g).padStart(2,"0"),x=G[d],c=(x?"var":"")+(d===bs?" bugun":"");'
            'var dots=x?"<i>"+(x[0]?"<span></span>":"")+(x[1]?\'<span class="y"></span>\':"")+"</i>":"";'
            'h+=\'<button type="button" class="\'+c+\'" data-d="\'+d+\'"\'+(x?\' aria-label="\'+tr(d)+", "+(x[0]+x[1])+\' kayıt"\':\' tabindex="-1" disabled\')+">"+g+dots+"</button>";}'
            'var Gr=R.querySelector(".cal-g");Gr.innerHTML=h;Gr.querySelectorAll("button.var").forEach(function(b){b.onclick=function(){var d=b.dataset.d;' + hedef + '};});}'
            'R.querySelector(".cp").onclick=function(){var i=aylar.indexOf(ay);if(i>0){ay=aylar[i-1];ciz();}};'
            'R.querySelector(".cn").onclick=function(){var i=aylar.indexOf(ay);if(i<aylar.length-1){ay=aylar[i+1];ciz();}};ciz();})();')


TAKVIM_HTML = ('<div class="cal-h"><button type="button" class="cp" aria-label="Önceki ay">‹</button><b class="ct"></b>'
               '<button type="button" class="cn" aria-label="Sonraki ay">›</button></div><div class="cal-g"></div>'
               '<div class="cal-lg"><span>Kısa haber</span><span class="y">Yazı</span></div>')


def ana_sayfa(akis):
    p = os.path.join(KOK, 'index.html'); s = open(p, encoding='utf-8').read()
    sec = akis[:ANA_SAYI]
    yazi = next((x for x in akis if x['tur'] == 'yazi'), None)
    son_yazi = ''
    if yazi and yazi not in sec:
        son_yazi = (f'\n          <a class="gd-son-yazi" href="{yazi["url"]}"><small>Son yazı · {tr_tarih(yazi["tarih"])}</small>'
                    f'<b>{yazi["baslik"]}</b></a>')
    a = s.index('<section class="section" id="gundem">'); b = s.index('</section>', a) + len('</section>')
    blok = f'''<section class="section" id="gundem">
      <div class="wrap series gd-home">
        <div class="series-about">
          <h2>Piyasa Gündemi</h2>
          <p>Piyasaları, fonları ve sermaye piyasası mevzuatını etkileyen güncel gelişmeler ve ne anlama geldikleri.</p>
        </div>
        <div class="gd-latest">
          <ul class="notes">
{''.join(li(x, '            ') for x in sec)}          </ul>{son_yazi}
          <a class="gundem-all" href="/gundem/">Tüm gündem <span>{len(akis)} kayıt</span> →</a>
        </div>
        <aside class="cal mini" id="gd-mini" aria-label="Gündem takvimi">{TAKVIM_HTML}</aside>
      </div>
      <script>{takvim_js(akis, 'location.href="/gundem/#"+d;', 'gd-mini')}</script>
    </section>'''
    s = s[:a] + blok + s[b:]
    open(p, 'w', encoding='utf-8').write(s)
    return len(sec)


def arsiv(akis):
    # şablon: ana sayfanın head + header + footer'ı
    s = open(os.path.join(KOK, 'index.html'), encoding='utf-8').read()
    head = s[:s.index('</head>')]
    head = re.sub(r'<title>.*?</title>', '<title>Piyasa Gündemi — İbrahim Ethem Afacan</title>', head, flags=re.S)
    desc = 'Piyasaları, fonları ve sermaye piyasası mevzuatını etkileyen gelişmeler: kısa haberler ve yazılar, takvim üzerinde gün gün.'
    for k in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        head = re.sub(r'(<meta %s content=")[^"]*"' % k, r'\g<1>' + desc + '"', head)
    for k in ('property="og:title"', 'name="twitter:title"'):
        head = re.sub(r'(<meta %s content=")[^"]*"' % k, r'\g<1>Piyasa Gündemi — İbrahim Ethem Afacan"', head)
    head = head.replace('content="https://ibrahimethemafacan.com/"', 'content="https://ibrahimethemafacan.com/gundem/"')
    head = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://ibrahimethemafacan.com/gundem/">', head)
    hs = s.index('<header class="site-head">'); he = s.index('</header>', hs) + len('</header>')
    header = s[hs:he].replace('href="#', 'href="/#').replace('<a href="/#gundem">', '<a href="/#gundem" aria-current="page">')
    fs = s.index('<footer class="site-foot">'); fe = s.index('</footer>', fs) + len('</footer>')
    footer = s[fs:fe]
    tail = s[fe:]
    data = json.dumps(akis, ensure_ascii=False).replace('</', '<\\/')
    css = '''<style>
    .gd-wrap{display:grid;grid-template-columns:19rem minmax(0,1fr);gap:2.5rem;align-items:start;margin-top:1.5rem}
    @media (max-width:860px){.gd-wrap{grid-template-columns:1fr;gap:1.25rem}}
    .gd-bar{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center;margin-bottom:.4rem;font-family:var(--sans)}
    .gd-bar button{all:unset;cursor:pointer;font-size:.8rem;font-weight:700;padding:.35rem .85rem;border-radius:999px;border:1.5px solid var(--rule);color:var(--ink);background:var(--panel)}
    .gd-bar button[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:#fff}
    .gd-bar .gd-sec{margin-left:auto;font-size:.8rem;color:var(--muted)}
    .gd-bar .gd-sec a{color:var(--accent);font-weight:700;cursor:pointer;margin-left:.4rem}
    .gd-day{font-family:var(--sans);font-size:.78rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);margin:1.6rem 0 0;padding-bottom:.35rem;border-bottom:1px solid var(--rule)}
    .gd-day:first-child{margin-top:.6rem}
    .gd-list .notes{margin:0}
    .gd-bos{font-family:var(--sans);color:var(--muted);padding:1rem 0}
  </style>
'''
    body = f'''
<body>
  {header}

  <main class="wrap">
    <article class="prose wide" style="margin-bottom:0">
      <h1>Piyasa Gündemi</h1>
      <p>Piyasaları, fonları ve sermaye piyasası mevzuatını etkileyen gelişmeler. Takvimden bir güne dokunarak o günün haberlerini görebilirsin.</p>
    </article>
    <div class="gd-wrap">
      <aside class="cal" aria-label="Gündem takvimi">
        <div class="cal-h"><button type="button" id="cal-p" aria-label="Önceki ay">‹</button><b id="cal-t"></b><button type="button" id="cal-n" aria-label="Sonraki ay">›</button></div>
        <div class="cal-g" id="cal-g"></div>
        <div class="cal-lg"><span>Kısa haber</span><span class="y">Yazı</span></div>
      </aside>
      <section>
        <div class="gd-bar" role="group" aria-label="Tür">
          <button type="button" data-t="" aria-pressed="true">Tümü</button>
          <button type="button" data-t="yazi" aria-pressed="false">Yazılar</button>
          <button type="button" data-t="kisa" aria-pressed="false">Kısa haberler</button>
          <span class="gd-sec" id="gd-sec" hidden></span>
        </div>
        <div class="gd-list" id="gd-list"></div>
      </section>
    </div>
  </main>

  {footer}
<script>
(function(){{
var A={data};
var AY={json.dumps(AYLAR, ensure_ascii=False)},GUN=["Pazar","Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi"];
var IC='{IKON}';
var tur='',gun=null,by={{}};A.forEach(function(x){{(by[x.tarih]=by[x.tarih]||[]).push(x);}});
var aylar=Object.keys(by).map(function(d){{return d.slice(0,7);}}).filter(function(v,i,a){{return a.indexOf(v)===i;}}).sort();
var ay=aylar[aylar.length-1];
function esc(t){{return String(t).replace(/[&<>"]/g,function(c){{return {{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}}[c];}});}}
function trT(d){{var p=d.split('-');return (+p[2])+' '+AY[+p[1]-1]+' '+p[0];}}
function li(x){{
  if(x.tur==='kisa')return '<li class="brief"><div class="meta">'+IC+trT(x.tarih)+' · '+esc(x.etiket)+' · Kısa haber</div><p class="note-text">'+x.metin+'</p></li>';
  return '<li class="post"><div class="meta">'+trT(x.tarih)+' · '+esc(x.etiket)+'</div><a href="'+x.url+'">'+x.baslik+'</a><p class="note-summary">'+x.ozet+'</p><a class="more" href="'+x.url+'" aria-hidden="true" tabindex="-1">Yazıyı oku →</a></li>';
}}
function liste(){{
  var L=A.filter(function(x){{return (!tur||x.tur===tur)&&(!gun||x.tarih===gun);}}),h='',son='';
  L.forEach(function(x){{
    if(x.tarih!==son){{if(son)h+='</ul>';var dt=new Date(x.tarih+'T12:00:00');h+='<h2 class="gd-day">'+trT(x.tarih)+', '+GUN[dt.getDay()]+'</h2><ul class="notes">';son=x.tarih;}}
    h+=li(x);
  }});
  if(son)h+='</ul>';
  document.getElementById('gd-list').innerHTML=h||'<p class="gd-bos">Bu seçimde kayıt yok.</p>';
  var s=document.getElementById('gd-sec');
  if(gun){{s.hidden=false;s.innerHTML=trT(gun)+'<a id="gd-x">Tümünü göster</a>';document.getElementById('gd-x').onclick=function(){{gun=null;takvim();liste();}};}}else s.hidden=true;
}}
function takvim(){{
  var y=+ay.slice(0,4),m=+ay.slice(5,7);document.getElementById('cal-t').textContent=AY[m-1]+' '+y;
  var i=aylar.indexOf(ay);document.getElementById('cal-p').disabled=i<=0;document.getElementById('cal-n').disabled=i>=aylar.length-1;
  var ilk=(new Date(y,m-1,1).getDay()+6)%7,n=new Date(y,m,0).getDate(),h=['Pt','Sa','Ça','Pe','Cu','Ct','Pz'].map(function(d){{return '<span class="dw">'+d+'</span>';}}).join('');
  for(var k=0;k<ilk;k++)h+='<span></span>';
  var bg=new Date(),bs=bg.getFullYear()+'-'+String(bg.getMonth()+1).padStart(2,'0')+'-'+String(bg.getDate()).padStart(2,'0');
  for(var g=1;g<=n;g++){{
    var d=ay+'-'+String(g).padStart(2,'0'),x=by[d],c=(x?'var':'')+(d===bs?' bugun':'')+(d===gun?' sec':'');
    var dots=x?'<i>'+(x.some(function(z){{return z.tur==='kisa';}})?'<span></span>':'')+(x.some(function(z){{return z.tur==='yazi';}})?'<span class="y"></span>':'')+'</i>':'';
    h+='<button type="button" class="'+c+'" data-d="'+d+'"'+(x?' aria-label="'+trT(d)+', '+x.length+' kayıt"':' tabindex="-1" disabled')+'>'+g+dots+'</button>';
  }}
  var G=document.getElementById('cal-g');G.innerHTML=h;
  G.querySelectorAll('button.var').forEach(function(b){{b.onclick=function(){{gun=gun===b.dataset.d?null:b.dataset.d;takvim();liste();
    if(window.innerWidth<860)document.getElementById('gd-list').scrollIntoView({{behavior:'smooth',block:'start'}});}};}});
}}
document.getElementById('cal-p').onclick=function(){{var i=aylar.indexOf(ay);if(i>0){{ay=aylar[i-1];takvim();}}}};
document.getElementById('cal-n').onclick=function(){{var i=aylar.indexOf(ay);if(i<aylar.length-1){{ay=aylar[i+1];takvim();}}}};
document.querySelectorAll('.gd-bar button').forEach(function(b){{b.onclick=function(){{tur=b.dataset.t;document.querySelectorAll('.gd-bar button').forEach(function(x){{x.setAttribute('aria-pressed',x===b);}});liste();}};}});
var q=location.hash.slice(1);if(by[q]){{gun=q;ay=q.slice(0,7);}}
takvim();liste();
}})();
</script>'''
    out = head + css + '</head>' + body + tail
    os.makedirs(os.path.join(KOK, 'gundem'), exist_ok=True)
    open(os.path.join(KOK, 'gundem', 'index.html'), 'w', encoding='utf-8').write(out)


if __name__ == '__main__':
    akis = json.load(open(os.path.join(KOK, 'gundem', 'akis.json'), encoding='utf-8'))
    akis.sort(key=lambda x: x['tarih'], reverse=True)  # kararlı sıralama: aynı gün içindeki sıra korunur
    n = ana_sayfa(akis)
    arsiv(akis)
    print(f'ana sayfa: {n} kayıt · arşiv: {len(akis)} kayıt')
