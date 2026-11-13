"""araclar/fon-tarama.html üretir. Veri: funds.json (ajan çıktısı).
Türetilmiş metrikler burada hesaplanır; veri sayfaya gömülür."""
import json, math, re

import os
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
SC = SITE + 'scripts/data/'
D = json.load(open(SC + 'fontar_funds.json'))
ASOF = '13 Kasım 2026'


KEEP = {'BES','OKS','TL','ABD','FTSE','S&P','MSCI','ESG','BIST','ETF','BYF','GYF','GSYF','USD','EUR','AI','IT','A.Ş','T.C'}
LOWW = {'ve','ile'}
def trlow(x):
    return x.replace('I','ı').replace('İ','i').lower()
def tcap(ad):
    if ad != ad.upper():
        return ad
    ad = ad.replace('A.Ş.', 'A.Ş. ').replace('  ', ' ')
    out = []
    for w in ad.split():
        pre = suf = ''
        core = w
        while core and core[0] == '(':
            pre += core[0]; core = core[1:]
        while core and core[-1] in ').,':
            suf = core[-1] + suf; core = core[:-1]
        if not core:
            out.append(w); continue
        if core in KEEP or (core.isalpha() and len(core) <= 4 and not any(c in 'AEIİOÖUÜ' for c in core[1:])):
            out.append(pre + core + suf); continue
        low = trlow(core)
        if low in LOWW and not pre:
            out.append(low + suf); continue
        first = {'i': 'İ', 'ı': 'I'}.get(low[0], low[0].upper())
        out.append(pre + first + low[1:] + suf)
    r = ' '.join(out)
    for a, b in (('Allıanz','Allianz'),('Metlıfe','MetLife'),('Cıgna','Cigna'),('Unıted','United'),('Fıba','Fiba'),('Bnp Parıbas','BNP Paribas'),('Bnp','BNP'),('Hdı','HDI')):
        r = r.replace(a, b)
    return r

# --- türetilmiş metrikler ---
rows = []
pp_ann = []  # para piyasası fonlarının yıllıklandırılmış getirileri (rf için)
for r in D['rows']:
    p1, p0, py, m1, m3 = r.get('p1'), r.get('p0'), r.get('py'), r.get('m1'), r.get('m3')
    n, s1, s2, dd = r.get('n'), r.get('s1'), r.get('s2'), r.get('dd')
    d0 = r.get('d0') or ''
    def rt(b):
        return round((p1 / b - 1) * 100, 1) if p1 and b else None
    r1m, r3m, ry = rt(m1), rt(m3), rt(py)
    r1y = rt(p0) if p0 and d0 and d0 <= '2025-11-24' else None
    vol = sh = ann = None
    if n and n >= 60 and s1 is not None and s2 is not None and p1 and p0:
        var = (s2 - s1 * s1 / n) / (n - 1)
        if var > 0:
            vol = math.sqrt(var) * math.sqrt(252)
        ann = (p1 / p0) ** (252 / n) - 1
        if r.get('s') in ('Para Piyasası Şemsiye Fonu', 'Para Piyasası Fonu') and n >= 200:
            pp_ann.append(ann)
    rows.append((r, r1m, r3m, ry, r1y, vol, ann, dd))

pp_ann.sort()
RF = pp_ann[len(pp_ann) // 2] if pp_ann else 0.40
print('rf (para piyasası medyan yıllık): %.4f  (n=%d)' % (RF, len(pp_ann)))

EXC = set('ACV AE1 AE4 AEB AEC AEG AEI AEK AEL AEP AER AET AEY AG1 AG2 AG3 AG4 AGG AGT AH0 AH2 AHJ ALZ AMF AMY ANK AO1 AO2 AVE AVH AVJ AVK AVL AVP AVU AVY AZA AZL BBH BGE BGK BKB BNK BPC BPF BPL CFB CFK CFY CGE CGG CHL CHT FEI FER FET FIE FII FIY FYL FYY GCV GDV GEF GEG GEL GHF GHI GHK GHL HEG HEL HEP HER HET HHE HHG HHN HQX IER IGE KEA KEK KEY KOE MHA MHB MHC MHG MHL MHT MHY NHB NHC NHF NHG NHH NHI NHK NHL NHO NHR NNK PRC PRS TKV VEE VEI VEL VER VEY VGP VGT VGY VKE VKJ'.split())  # BEFAS'ta işlem görmeyen emeklilik fonları

OUT = []
for r, r1m, r3m, ry, r1y, vol, ann, dd in rows:
    if r['t'] == 'pension' and r['kod'] in EXC:
        continue
    sh = None
    if vol and vol > 0.001 and ann is not None:
        sh = round((ann - RF) / vol, 2)
    al = r.get('al') or {}
    t = {'mutual': 'y', 'pension': 'e', 'exchange': 'b'}[r['t']]
    def z(v, k=1):
        return round(v, k) if isinstance(v, (int, float)) else None
    ad = tcap(r['ad'].strip())
    OUT.append([r['kod'], ad, t, r.get('s') or '', r.get('rs'), z(r.get('uc'), 4),
                z(r.get('sz')), r.get('inv'), z(r.get('fy')), z(r.get('f3')),
                r1m, r3m, ry, r1y,
                z(vol * 100 if vol else None), sh, z(dd * 100 if dd is not None else None),
                [al.get(k) or 0 for k in ('hs', 'yhs', 'kamu', 'ozelb', 'kkira', 'okira', 'kath', 'mev', 'km', 'pp', 'fonp', 'gsyf', 'gyf', 'vint', 'dgr')] if al else None])
DATA = json.dumps(OUT, ensure_ascii=False, separators=(',', ':'))
print('fon:', len(OUT), 'veri boyutu KB:', len(DATA) // 1024)

# --- makro head/header/footer'ını al ---
L = open(SITE + 'araclar/makro.html').read().split('\n')
iS = next(i for i, x in enumerate(L) if '</style>' in x)
iB = next(i for i, x in enumerate(L) if '<body>' in x)
iM = next(i for i, x in enumerate(L) if '<main' in x)
iMe = next(i for i, x in enumerate(L) if '</main>' in x)
iSc = next(i for i in range(iMe, len(L)) if '<script>' in L[i])
iH = next(i for i, x in enumerate(L) if '</head>' in x)
head = '\n'.join(L[:iH])
header = '\n'.join(L[iB:iM])
footer = '\n'.join(L[iMe + 1:iSc])
header = header.replace('<a href="/#veriler" aria-current="page">Veriler</a>', '<a href="/#veriler">Veriler</a>')
header = header.replace('<a href="/#araclar">Araçlar</a>', '<a href="/#araclar" aria-current="page">Araçlar</a>')
DESC = "TEFAS'taki yatırım fonlarını, BEFAS'taki emeklilik fonlarını ve BYF'leri şemsiye türüne, varlık dağılımına (hisse, kira sertifikası, kıymetli maden...), getiriye, Sharpe oranına, maksimum değer kaybına ve net para girişine göre tarayın."
for old, new in [("Makro Göstergeler — İbrahim Ethem Afacan", "Fon Tarama — İbrahim Ethem Afacan"),
                 ('content="Makro Göstergeler"', 'content="Fon Tarama"'),
                 ("araclar/makro.html", "araclar/fon-tarama.html"),
                 ("og-makro.png?v=1", "og-fonlar.png?v=1")]:
    assert old in head, old
    head = head.replace(old, new)
head = re.sub(r'(name="description" content=")[^"]*"', r'\g<1>' + DESC + '"', head)
head = re.sub(r'(property="og:description" content=")[^"]*"', r'\g<1>' + DESC + '"', head)
head = re.sub(r'(name="twitter:description" content=")[^"]*"', r'\g<1>' + DESC + '"', head)
head = head.replace('  </style>', '''    .flt{background:var(--panel);border:1px solid var(--rule);border-radius:.8rem;padding:1rem 1.1rem;margin:1rem 0 1.25rem;font-family:var(--sans)}
    .flt h3{margin:0 0 .5rem;font-size:.8rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
    .flt-grp{margin:0 0 .9rem}
    .chips{display:flex;flex-wrap:wrap;gap:.4rem}
    .chips label{display:inline-flex;align-items:center;gap:.35rem;border:1.5px solid var(--rule);border-radius:999px;padding:.3rem .75rem;font-size:.8rem;cursor:pointer;user-select:none;background:var(--panel);color:var(--ink)}
    .chips input{display:none}
    .chips label small{opacity:.65;font-weight:700;margin-left:.1rem}
    .sem-detail{margin-top:.6rem;padding-top:.6rem;border-top:1px dashed var(--rule)}
    #sem-tog{margin-top:.45rem}
    .chips label:has(input:checked){border-color:var(--accent);background:var(--accent);color:var(--on-accent,#fff)}
    .frow{display:flex;flex-wrap:wrap;gap:.6rem .9rem;align-items:center}
    .frow label{font-size:.8rem;color:var(--muted)}
    .fnum{width:5.2rem;padding:.35rem .45rem;border:1px solid var(--rule);border-radius:.45rem;font:inherit;font-size:.85rem;font-variant-numeric:tabular-nums;background:var(--panel);color:var(--ink)}
    .fsel{padding:.35rem .45rem;border:1px solid var(--rule);border-radius:.45rem;font:inherit;font-size:.85rem;max-width:14rem;background:var(--panel);color:var(--ink)}
    .fcond{display:flex;flex-wrap:wrap;gap:.45rem;align-items:center;margin:.35rem 0}
    .fx{all:unset;cursor:pointer;color:var(--down);font-weight:700;padding:0 .4rem;font-size:1rem}
    .fadd{all:unset;cursor:pointer;color:var(--accent);font-weight:700;font-size:.8rem;padding:.2rem 0}
    .fbar{display:flex;flex-wrap:wrap;gap:.6rem;align-items:center;justify-content:space-between;margin:.4rem 0 .5rem;font-family:var(--sans)}
    .fcount{font-size:.85rem;color:var(--muted)}
    .freset{all:unset;cursor:pointer;color:var(--accent);font-weight:700;font-size:.82rem}
    .ft{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:.82rem;font-variant-numeric:tabular-nums}
    .ft th,.ft td{padding:.45rem .5rem;border-bottom:1px solid var(--rule);text-align:right;white-space:nowrap}
    .ft th{font-weight:600;color:var(--muted);font-size:.72rem;cursor:pointer;user-select:none;position:sticky;top:0;background:var(--panel)}
    .ft th.on{color:var(--accent)}
    .ft td:nth-child(1),.ft th:nth-child(1),.ft td:nth-child(2),.ft th:nth-child(2){text-align:left}
    .ft td:nth-child(2){white-space:normal;min-width:13rem;font-size:.78rem}
    .ft .pos{color:var(--up)}.ft .neg{color:var(--down)}
    .ft .kd{font-weight:700;color:var(--navy)}
    .twrap2{overflow-x:auto;max-height:68vh;overflow-y:auto;border:1px solid var(--rule);border-radius:.6rem}
    .mini{font-size:.72rem;color:var(--muted)}
  </style>''', 1)

# --- gövde ---
body = r'''
  <main class="wrap narrow">
    <article class="prose wide">
      <h1>Fon Tarama</h1>
      <p>Yatırım fonlarını, emeklilik fonlarını ve borsa yatırım fonlarını türüne, varlık dağılımına, getirisine, Sharpe oranına, maksimum değer kaybına ve para giriş-çıkışına göre tarayın. Yatırım fonlarında yalnızca TEFAS'ta, emeklilik fonlarında yalnızca BEFAS'ta işlem gören fonlar listelenir. Veriler __ASOF__ itibarıyladır.</p>
    </article>

    <div class="flt" id="flt">
      <div class="flt-grp"><h3>Fon türü</h3><div class="chips" id="c-tip">
        <label><input type="checkbox" value="y" checked>Yatırım fonu (TEFAS)</label>
        <label><input type="checkbox" value="e" checked>Emeklilik fonu (BEFAS)</label>
        <label><input type="checkbox" value="b" checked>BYF</label>
      </div></div>
      <div class="flt-grp"><h3>Ne yatırıyor? <span class="mini">(şemsiye türleri ailelere toplandı)</span></h3><div class="chips" id="c-fam"></div>
        <button type="button" class="fadd" id="sem-tog" aria-expanded="false">Ayrıntılı şemsiye türlerini göster ▾</button>
        <div class="chips sem-detail" id="c-sem" hidden></div></div>
      <div class="flt-grp"><h3>Varlık dağılımı koşulları <span class="mini">(son bildirilen portföy dağılımı, %)</span></h3>
        <div id="c-al"></div><button type="button" class="fadd" id="al-add">+ Koşul ekle</button></div>
      <div class="flt-grp"><h3>Performans ve risk</h3><div class="frow">
        <label>Getiri <select class="fsel" id="f-gd"><option value="12">2026</option><option value="10">1 ay</option><option value="11">3 ay</option><option value="13">1 yıl</option></select>
          min % <input class="fnum" id="f-gmin" inputmode="numeric"></label>
        <label>Sharpe (1 yıl) min <input class="fnum" id="f-sh" inputmode="numeric" placeholder="örn. 0"></label>
        <label>Maks. değer kaybı en fazla % <input class="fnum" id="f-dd" inputmode="numeric" placeholder="örn. 20"></label>
      </div></div>
      <div class="flt-grp"><h3>Akım ve büyüklük</h3><div class="frow">
        <label>Net akım <select class="fsel" id="f-ad"><option value="8">2026</option><option value="9">son 3 ay</option></select>
          <select class="fsel" id="f-ay"><option value="g">en az +</option><option value="c">en az −</option></select>
          <input class="fnum" id="f-aval" inputmode="numeric" placeholder="mn TL"></label>
        <label>Büyüklük min <input class="fnum" id="f-sz" inputmode="numeric" placeholder="mn TL"></label>
        <label>Ara <input class="fnum" id="f-q" style="width:9rem" placeholder="kod veya ad"></label>
      </div></div>
    </div>

    <div class="fbar"><span class="fcount" id="cnt"></span><button type="button" class="freset" id="reset">Filtreleri sıfırla</button></div>
    <div class="twrap2"><table class="ft" id="tbl"><thead><tr>
      <th data-k="0">Kod</th><th data-k="1">Fon</th><th data-k="6">Büyüklük<br>mn TL</th>
      <th data-k="10">1 ay %</th><th data-k="12">2026 %</th><th data-k="13">1 yıl %</th>
      <th data-k="15">Sharpe</th><th data-k="16">MDK %</th><th data-k="8">Akım 2026<br>mn TL</th><th data-k="17" id="th-al">Seçili varlık %</th>
    </tr></thead><tbody></tbody></table></div>

    <article class="prose wide" style="margin-top:1.5rem">
      <h2>Yöntem</h2>
      <p>Getiriler birim pay değerinden hesaplanmıştır; 1 ay ve 3 ay getirileri sırasıyla 12 Ekim ve 12 Ağustos'tan önceki son fiyattan bu yana, 2026 getirisi yılbaşından bu yana olan değişimdir. <b>Sharpe oranı</b>, son bir yılın günlük getirilerinden yıllıklandırılmış volatilite ve bileşik getiriyle hesaplanır; risksiz getiri olarak para piyasası fonlarının medyan yıllık getirisi (%__RF__) kullanılmıştır. <b>Maksimum değer kaybı (MDK)</b>, son bir yılda zirveden dibe en derin düşüştür. <b>Net akım</b>, yatırımcıların fona yatırdığı paradan çektiklerinin farkıdır; fiyat değişimini içermez. Varlık dağılımı, fonların TEFAS'a bildirdiği son günlük dağılımdır ve benzer sınıflar gruplanmıştır (ör. kamu borçlanma = tahvil + bono + eurobond). Bir yaşını doldurmamış fonlarda 1 yıl getirisi ve Sharpe gösterilmez.</p>
      <p>Kapsam: TEFAS'ta işlem gören yatırım fonları, BEFAS'ta işlem gören emeklilik fonları ve borsa yatırım fonları — toplam __NFON__ fon. TEFAS'a açık olmayan (çoğu kurumsal ve özel) serbest fonlar ile BEFAS'ta işlem görmeyen emeklilik fonları (devlet katkısı, başlangıç ve emeklilik para piyasası fonları gibi) kapsamda değildir. Kaynak: Fintables, TEFAS fon verileri. Bu sayfa yatırım tavsiyesi değildir.</p>
    </article>
  </main>
__FOOTER__
<script>
var F=__DATA__;
var AL=[["hs","Hisse senedi"],["yhs","Yabancı hisse"],["kamu","Kamu borçlanma (tahvil/bono/eurobond)"],["ozelb","Özel sektör borçlanma"],["kkira","Kamu kira sertifikası"],["okira","Özel sektör kira sertifikası"],["kath","Katılma hesabı"],["mev","Mevduat"],["km","Kıymetli madenler"],["pp","Para piyasası (repo/TPP)"],["fonp","Fon katılma payları"],["gsyf","Girişim sermayesi YF"],["gyf","Gayrimenkul YF"],["vint","Vadeli işlem teminatı"],["dgr","Diğer"]];
var ALI={};AL.forEach(function(a,i){ALI[a[0]]=i;});
var n1=new Intl.NumberFormat('tr-TR',{minimumFractionDigits:1,maximumFractionDigits:1});
var n0=new Intl.NumberFormat('tr-TR',{maximumFractionDigits:0});
var n2=new Intl.NumberFormat('tr-TR',{minimumFractionDigits:2,maximumFractionDigits:2});
var $=function(s){return document.querySelector(s);};
var SEMS={};F.forEach(function(r){if(r[3])SEMS[r[2]]=SEMS[r[2]]||{},SEMS[r[2]][r[3]]=(SEMS[r[2]][r[3]]||0)+1;});
var sortK=6,sortD=-1,conds=[];
var FAMS=[['hisse','Hisse senedi'],['borc','Borçlanma araçları'],['pp','Para piyasası'],['kat','Katılım'],['km','Kıymetli maden'],['sepet','Fon sepeti'],['degisken','Değişken & karma'],['serbest','Serbest'],['bes','Emeklilik standart & katkı'],['diger','Diğer']];
function famOf(s){var f=[],t=(s||'').toLocaleLowerCase('tr');
  if(/hisse|endeks/.test(t))f.push('hisse');
  if(/borçlanma|kira sertifika/.test(t))f.push('borc');
  if(/para piyasası/.test(t))f.push('pp');
  if(/katılım|kira sertifika/.test(t))f.push('kat');
  if(/altın|gümüş|kıymetli maden/.test(t))f.push('km');
  if(/fon sepeti/.test(t))f.push('sepet');
  if(/değişken|karma/.test(t))f.push('degisken');
  if(/serbest/.test(t))f.push('serbest');
  if(/standart|başlangıç|katkı|yaşam döngüsü/.test(t))f.push('bes');
  if(!f.length)f.push('diger');return f;}
var FAMOF={};F.forEach(function(r){var k=r[3]||'';if(!(k in FAMOF))FAMOF[k]=famOf(k);});
var SERB='Serbest Şemsiye Fonu',SUBN={hisse:'Hisse senedi serbest',kat:'Katılım serbest',doviz:'Döviz serbest',pp:'Para piyasası / kısa vadeli serbest',km:'Kıymetli maden & emtia serbest',borc:'Borçlanma araçları serbest',diger:'Çoklu varlık / diğer serbest'};
function subOf(r){var a=(r[1]||'').toLocaleLowerCase('tr'),al=r[17]||[];
  if(/hisse/.test(a)||(al[0]||0)>=80)return 'hisse';
  if(/katılım/.test(a))return 'kat';
  if(/döviz|eurobond|dolar|yabancı/.test(a))return 'doviz';
  if(/para piyasası|kısa vadeli|nakit/.test(a)||((al[7]||0)+(al[9]||0))>=80)return 'pp';
  if(/altın|gümüş|kıymetli|emtia/.test(a)||(al[8]||0)>=50)return 'km';
  if(/borçlanma|tahvil|bono|sabit getiri/.test(a)||((al[2]||0)+(al[3]||0))>=60)return 'borc';
  return 'diger';}
var SUB={};F.forEach(function(r){if(r[3]===SERB)SUB[r[0]]=subOf(r);});
function semKey(r){return r[3]===SERB?'serbest:'+SUB[r[0]]:(r[3]||'');}
function semName(k){return k.indexOf('serbest:')===0?SUBN[k.slice(8)]:k;}
function famSel(){var v={};document.querySelectorAll('#c-fam input:checked').forEach(function(i){v[i.value]=1;});return v;}
function semChips(){var tips=tipSel(),fsel=famSel(),box=$('#c-sem'),fbox=$('#c-fam'),keep={};
  box.querySelectorAll('input:checked').forEach(function(i){keep[i.value]=1;});
  var cnt={},scnt={};F.forEach(function(r){if(tips.indexOf(r[2])<0)return;var k=r[3]||'';FAMOF[k].forEach(function(f){cnt[f]=(cnt[f]||0)+1;});if(k){var sk=semKey(r);scnt[sk]=(scnt[sk]||0)+1;}});
  fbox.innerHTML=FAMS.filter(function(f){return cnt[f[0]];}).map(function(f){return '<label><input type="checkbox" value="'+f[0]+'"'+(fsel[f[0]]?' checked':'')+'>'+f[1]+' <small>'+cnt[f[0]]+'</small></label>';}).join('');
  fbox.querySelectorAll('input').forEach(function(i){i.addEventListener('change',function(){semChips();apply();});});
  var anyF=Object.keys(fsel).length,list=Object.keys(scnt).filter(function(k){var base=k.indexOf('serbest:')===0?SERB:k;return !anyF||FAMOF[base].some(function(f){return fsel[f];});});
  list.sort(function(a,b){return semName(a).localeCompare(semName(b),'tr');});
  box.innerHTML=list.map(function(k){return '<label><input type="checkbox" value="'+k.replace(/"/g,'&quot;')+'"'+(keep[k]?' checked':'')+'>'+semName(k)+' <small>'+scnt[k]+'</small></label>';}).join('');
  box.querySelectorAll('input').forEach(function(i){i.addEventListener('change',apply);});}
$('#sem-tog').addEventListener('click',function(){var b=$('#c-sem'),o=b.hidden;b.hidden=!o;this.setAttribute('aria-expanded',o?'true':'false');this.textContent=o?'Ayrıntılı şemsiye türlerini gizle ▴':'Ayrıntılı şemsiye türlerini göster ▾';});
function tipSel(){var v=[];document.querySelectorAll('#c-tip input:checked').forEach(function(i){v.push(i.value);});return v;}
function addCond(k,mn,mx){var d=document.createElement('div');d.className='fcond';
  d.innerHTML='<select class="fsel">'+AL.map(function(a){return '<option value="'+a[0]+'"'+(a[0]===k?' selected':'')+'>'+a[1]+'</option>';}).join('')+'</select> en az <input class="fnum mn" inputmode="numeric" value="'+(mn||'')+'"> en fazla <input class="fnum mx" inputmode="numeric" value="'+(mx||'')+'"> % <button type="button" class="fx" title="Kaldır">×</button>';
  d.querySelector('.fx').onclick=function(){d.remove();apply();};
  d.querySelectorAll('select,input').forEach(function(i){i.addEventListener('change',apply);i.addEventListener('input',deb);});
  $('#c-al').appendChild(d);}
var dt;function deb(){clearTimeout(dt);dt=setTimeout(apply,350);}
function num(id){var v=document.getElementById(id).value.replace(',','.').trim();if(v==='')return null;var f=parseFloat(v);return isNaN(f)?null:f;}
function apply(){
  var tips=tipSel(),sems={},anySem=false,fsel=famSel(),anyFam=Object.keys(fsel).length>0;
  document.querySelectorAll('#c-sem input:checked').forEach(function(i){sems[i.value]=1;anySem=true;});
  var cs=[];document.querySelectorAll('#c-al .fcond').forEach(function(d){var k=d.querySelector('select').value,mn=d.querySelector('.mn').value,mx=d.querySelector('.mx').value;
    mn=mn===''?null:parseFloat(mn.replace(',','.'));mx=mx===''?null:parseFloat(mx.replace(',','.'));
    if(mn!=null||mx!=null)cs.push([ALI[k],mn,mx]);});
  var gd=+$('#f-gd').value,gmin=num('f-gmin'),sh=num('f-sh'),ddv=num('f-dd');
  var ad=+$('#f-ad').value,ay=$('#f-ay').value,aval=num('f-aval'),szv=num('f-sz');
  var q=$('#f-q').value.trim().toLocaleLowerCase('tr');
  var out=F.filter(function(r){
    if(tips.indexOf(r[2])<0)return false;
    if(anySem&&!sems[semKey(r)])return false;
    if(!anySem&&anyFam&&!FAMOF[r[3]||''].some(function(f){return fsel[f];}))return false;
    for(var i=0;i<cs.length;i++){var a=r[17];if(!a)return false;var w=a[cs[i][0]];
      if(cs[i][1]!=null&&w<cs[i][1])return false;if(cs[i][2]!=null&&w>cs[i][2])return false;}
    if(gmin!=null&&(r[gd]==null||r[gd]<gmin))return false;
    if(sh!=null&&(r[15]==null||r[15]<sh))return false;
    if(ddv!=null&&(r[16]==null||r[16]<-Math.abs(ddv)))return false;
    if(aval!=null){var f=r[ad];if(f==null)return false;if(ay==='g'&&f<aval)return false;if(ay==='c'&&f>-aval)return false;}
    if(szv!=null&&(r[6]==null||r[6]<szv))return false;
    if(q&&r[0].toLocaleLowerCase('tr').indexOf(q)<0&&r[1].toLocaleLowerCase('tr').indexOf(q)<0)return false;
    return true;});
  var alk=cs.length?cs[0][0]:null;
  $('#th-al').style.display=alk==null?'none':'';
  out.sort(function(a,b){var x=sortK===17?(a[17]?a[17][alk]:null):a[sortK],y=sortK===17?(b[17]?b[17][alk]:null):b[sortK];
    if(x==null)return 1;if(y==null)return -1;if(typeof x==='string')return sortD*x.localeCompare(y,'tr');return sortD*(x-y);});
  var MAX=300,sh2=out.slice(0,MAX);
  $('#cnt').textContent=n0.format(out.length)+' fon'+(out.length>MAX?' (ilk '+MAX+' gösteriliyor)':'');
  var tb=$('#tbl tbody');
  tb.innerHTML=sh2.map(function(r){
    function pc(v,k){return v==null?'<td>–</td>':'<td class="'+(v>0.049?'pos':v<-0.049?'neg':'')+'">'+(v>0?'+':v<0?'−':'')+ (k===2?n2:n1).format(Math.abs(v))+'</td>';}
    var alv=alk==null?'':(r[17]?'<td>'+n1.format(r[17][alk])+'</td>':'<td>–</td>');
    return '<tr><td class="kd">'+r[0]+'</td><td>'+r[1]+'<br><span class="mini">'+(r[2]==='e'?'Emeklilik':r[2]==='b'?'BYF':'Yatırım')+(r[3]?' · '+r[3].replace(' Şemsiye Fonu','').replace(' Fonu',''):'')+'</span></td>'+
      '<td>'+(r[6]==null?'–':n0.format(r[6]))+'</td>'+pc(r[10])+pc(r[12])+pc(r[13])+pc(r[15],2)+pc(r[16])+pc(r[8])+alv+'</tr>';}).join('');
  document.querySelectorAll('#tbl th').forEach(function(h){h.classList.toggle('on',+h.dataset.k===sortK);});
}
document.querySelectorAll('#c-tip input').forEach(function(i){i.addEventListener('change',function(){semChips();apply();});});
['f-gd','f-sh','f-dd','f-ad','f-ay','f-aval','f-sz','f-gmin','f-q'].forEach(function(id){var e=document.getElementById(id);e.addEventListener('change',apply);e.addEventListener('input',deb);});
document.querySelectorAll('#tbl th').forEach(function(h){h.addEventListener('click',function(){var k=+h.dataset.k;if(sortK===k)sortD=-sortD;else{sortK=k;sortD=(k<=3)?1:-1;}apply();});});
$('#al-add').onclick=function(){addCond('hs');};
$('#reset').onclick=function(){document.querySelectorAll('#c-tip input').forEach(function(i){i.checked=true;});document.querySelectorAll('#c-fam input,#c-sem input').forEach(function(i){i.checked=false;});
  $('#c-al').innerHTML='';['f-gmin','f-sh','f-dd','f-aval','f-sz','f-q'].forEach(function(id){document.getElementById(id).value='';});
  sortK=6;sortD=-1;semChips();apply();};
semChips();apply();
</script>
<script data-goatcounter="https://ibrahimethemafacan.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''
body = body.replace('__ASOF__', ASOF).replace('__RF__', str(round(RF * 100, 1)).replace('.', ',')).replace('__NFON__', str(len(OUT))).replace('__DATA__', DATA)
body = body.replace('__FOOTER__', footer)
open(SITE + 'araclar/fon-tarama.html', 'w').write(head + '\n</head>\n' + header + body)
print('yazıldı: araclar/fon-tarama.html')
