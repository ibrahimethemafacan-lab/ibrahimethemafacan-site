import json
import os
SITE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'
import json as _json
_EGM=_json.load(open(SITE+'scripts/data/egm_ozet.json'))
_AY=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
def _trh(t): y,m,d=t.split('-'); return '%d %s'%(int(d),_AY[int(m)-1])
def _tl(x,nd=1): return ('{:,.%df}'%nd).format(x).replace(',','X').replace('.',',').replace('X','.')
def _mn(x): return _tl(x/1e6,2)+' mn'
def _fark(seri,anah):
    """Son kesin veri ile bir önceki kesin veri arasındaki fark metni."""
    kesin=[r for r in seri if not r.get('yaklasik') and anah in r]
    if len(kesin)<2: return ''
    a,b=kesin[-2],kesin[-1]; d=b[anah]-a[anah]
    if abs(d)>=1e6: txt=('+' if d>=0 else '−')+_tl(abs(d)/1e6,2)+' mn'
    elif abs(d)>=1000: txt=('+' if d>=0 else '−')+_tl(abs(d)/1000,1)+' bin'
    else: txt=('+' if d>=0 else '−')+str(int(abs(d)))
    return txt+' ('+_trh(a['tarih'])+' → '+_trh(b['tarih'])+')'
def _kart(k):
    L=_EGM[k][-1]; kisi='katilimci' if k=='bes' else 'calisan'; belge='sozlesme' if k=='bes' else 'sertifika'
    top=(L['fon']+L['dk'])/1e6
    d={'t':'Gönüllü BES' if k=='bes' else 'Otomatik katılım (OKS)',
       'big':_tl(top,2) if top>=1 else _tl(top*1000,1),'unit':'trilyon TL' if top>=1 else 'milyar TL',
       'facts':[['Katılımcı' if k=='bes' else 'Çalışan',_mn(L[kisi]),_fark(_EGM[k],kisi)],
                ['Sözleşme' if k=='bes' else 'Sertifika',_mn(L[belge]),_fark(_EGM[k],belge)],
                ['Devlet katkısı',_tl(L['dk']/1000,1)+' mlr TL','']],
       'rows':[{'n':'Katılımcıların fonu' if k=='bes' else 'Çalışanların fonu','a':round(L['fon_faizli']/1000,4),'b':round(L['fon_faizsiz']/1000,4)},
               {'n':'Devlet katkısı fonu','a':round(L['dk_faizli']/1000,4),'b':round(L['dk_faizsiz']/1000,4)}]}
    return _json.dumps(d,ensure_ascii=False)
EGM_BES=_kart('bes'); EGM_OKS=_kart('oks')
_b,_o=_EGM['bes'][-1],_EGM['oks'][-1]
EGM_OZET=("EGM'nin %s özetine göre sistemde %s milyon katılımcı ve %s trilyon TL fon var: gönüllü BES %s milyon kişi ve %s trilyon TL, otomatik katılım %s milyon kişi ve %s milyar TL." % (
    _trh(_b['tarih'])+' '+_b['tarih'][:4], _tl((_b['katilimci']+_o['calisan'])/1e6,2), _tl((_b['fon']+_b['dk']+_o['fon']+_o['dk'])/1e6,2),
    _tl(_b['katilimci']/1e6,2), _tl((_b['fon']+_b['dk'])/1e6,2), _tl(_o['calisan']/1e6,2), _tl((_o['fon']+_o['dk'])/1e3,1))); EGM_TARIH=_trh(_EGM['bes'][-1]['tarih'])+' '+_EGM['bes'][-1]['tarih'][:4]

L=open(SITE+'araclar/makro.html').read().split('\n')
def lines(a,b): return '\n'.join(L[a-1:b])
def find(m,start=0):
    for i in range(start,len(L)):
        if m in L[i]: return i+1
    raise Exception(m)
iS=find('</style>'); iM=find('<main'); iMe=find('</main>'); iSc=find('<script>',iMe)
iD=find('var D = '); iF=find('function fill'); iG=find('/* ---- grafikler'); iT=find('function tk'); iR=find('var rt;window'); iTb=find('/* ---- sekmeler'); iE=len(L)
head=lines(1,iS)
import re
DESC="TEFAS ve EGM verileriyle Türkiye'de yatırım fonları ve bireysel emeklilik: fon büyüklükleri, yatırımcı ve katılımcı sayıları, fon türlerine göre dağılım ve aylık para girişleri."
for old,new in [("Makro Göstergeler — İbrahim Ethem Afacan","Yatırım ve Emeklilik Fonları — İbrahim Ethem Afacan"),
                 ('content="Makro Göstergeler"','content="Yatırım ve Emeklilik Fonları"'),
                 ("araclar/makro.html","araclar/fonlar.html"),("og-makro.png?v=1","og-fonlar.png?v=2")]:
    assert old in head,old; head=head.replace(old,new)
head=re.sub(r'(name="description" content=")[^"]*"',r'\g<1>'+DESC+'"',head)
head=re.sub(r'(property="og:description" content=")[^"]*"',r'\g<1>'+DESC+'"',head)
head=re.sub(r'(name="twitter:description" content=")[^"]*"',r'\g<1>'+DESC+'"',head)
header=lines(iS+1,iM-1)
footer=lines(iMe+1,iSc-1)
helpers=lines(iD+1,iF)
chartlib=lines(iG,iT)
resize=lines(iR,iR)
tabs=lines(iTb,iE).replace("'dunya',false","'yf',false")

# --- veri ---
M=[("2021-12",260.3,4278979,239.3),("2022-01",267.4,4316722,251.2),("2022-02",280.1,4342662,260.5),("2022-03",307.7,4403982,276.1),("2022-04",322.8,4482973,283.2),("2022-05",344.3,4448665,299.9),("2022-06",352.2,4441436,300.3),("2022-07",377.7,4475383,315.2),("2022-08",425.1,4560711,340.8),("2022-09",455.9,4620358,345.1),("2022-10",508.9,4768283,367.0),("2022-11",595.8,5010107,402.7),("2022-12",670.5,5245614,428.8),
("2023-01",716.6,5435906,436.3),("2023-02",756.1,5440605,437.0),("2023-03",813.0,5504767,455.0),("2023-04",846.8,5637480,465.1),("2023-05",808.3,5643224,472.0),("2023-06",967.0,5754521,561.7),("2023-07",1163.2,6027460,628.5),("2023-08",1268.3,6400282,649.4),("2023-09",1300.1,6689080,666.1),("2023-10",1377.6,6844167,683.6),("2023-11",1459.6,6984472,721.7),("2023-12",1498.6,7065517,743.2),
("2024-01",1745.7,7332959,798.9),("2024-02",2013.5,7859765,835.2),("2024-03",2241.9,8313422,898.0),("2024-04",2415.8,8714673,963.3),("2024-05",2534.6,9145688,991.9),("2024-06",2707.3,9318860,1026.4),("2024-07",2947.6,9704767,1056.5),("2024-08",3230.8,9809727,1078.1),("2024-09",3551.1,9917716,1136.7),("2024-10",3713.5,9955117,1147.5),("2024-11",3951.5,10008508,1185.7),("2024-12",4131.1,10059766,1222.2),
("2025-01",4600.1,10219101,1283.9),("2025-02",4757.4,10289023,1335.2),("2025-03",4492.4,10106423,1380.0),("2025-04",4745.0,10062684,1442.6),("2025-05",5125.3,9999211,1481.9),("2025-06",5462.7,10022320,1535.3),("2025-07",5934.5,10108059,1629.4),("2025-08",6314.8,10207423,1703.8),("2025-09",6712.5,10247777,1825.0),("2025-10",7054.9,10281001,1931.2),("2025-11",7331.6,10278945,1994.3),("2025-12",7570.8,10312675,2148.2),
("2026-01",8182.8,10558718,2556.9),("2026-02",8245.8,10711676,2498.8),("2026-03",7799.2,10629167,2335.7),("2026-04",8407.4,10714673,2424.7),("2026-05",8403.5,10824194,2462.6),("2026-06",8958.4,10839489,2402.6),("2026-07",9351.2,10941505,2418.6),("2026-08",9949.5,11132752,2659.0),("2026-09",8183.6,10167753,2558.5),("2026-10",7875.1,10093955,2522.1),("2026-11",7891.4,10097134,2584.9)]
FM=[334.0,32.8,-416.3,139.9,187.3,138.2,244.1,173.8,170.0,153.6,177.5,-39.8,158.5,-7.1,-484.6,265.0,-148.6,214.0,126.5,223.7,-1423.8,-288.0,32.2]
FP=[12.7,13.7,16.4,12.3,7.9,11.6,13.7,15.7,31.2,24.3,31.8,37.4,25.8,23.6,19.0,15.5,11.9,11.2,8.9,14.3,16.2,3.9,8.2]
FMm=[f"{2025+i//12}-{i%12+1}" for i in range(len(FM))]
SEM=[("Serbest",1217,5177.1,888178,5047.6,-1097.1),("Para piyasası",82,1569.7,3828987,1466.5,-193.7),("Katılım",111,395.6,993493,331.4,-16.8),("Borçlanma araçları",85,224.6,1221706,174.1,-2.3),("Kıymetli madenler",28,181.0,595316,180.6,-7.3),("Hisse senedi",190,144.7,1260603,169.3,17.3),("Fon sepeti",95,100.1,618391,111.0,-12.2),("Değişken",173,88.1,507656,84.6,-20.2),("Karma",8,5.0,167687,4.6,-0.6),("Diğer",13,5.5,15117,1.3,0.6)]
BD=[('0–50 bin',6500000,76),('50–100 bin',1200000,85),('100–250 bin',1200000,183),('250–500 bin',624000,222),('500 bin–1 mn',406000,287),('1–2,5 mn',290000,445),('2,5–5 mn',94000,322),('5–10 mn',35000,236),('10 mn+',13000,268)]
D=dict(bd=[list(x) for x in BD],m=[[a,b,c,d] for a,b,c,d in M],fm=FM,fp=FP,fmm=FMm,sem=[list(x) for x in SEM])
ytd_m=round(sum(FM[12:]),1); ytd_p=round(sum(FP[12:]),1)

ART='''<svg class="gh-art" viewBox="0 0 64 64" aria-hidden="true" fill="none" stroke-linecap="round" stroke-linejoin="round">{}</svg>'''
ICON_YF=ART.format('<circle cx="24" cy="34" r="20" fill="#E6F0FE" stroke="#0E3A8C" stroke-width="2.5"/><path d="M24 34 L24 14 A20 20 0 0 1 43 40 Z" fill="#1A5FFF"/><path d="M24 34 L43 40 A20 20 0 0 1 30 53 Z" fill="#40C0FF"/><rect x="46" y="44" width="6" height="14" rx="1.5" fill="#A9C6FF"/><rect x="55" y="36" width="6" height="22" rx="1.5" fill="#1A5FFF"/>')
ICON_BES=ART.format('<path d="M10 54 H54" stroke="#A9C6FF" stroke-width="2"/><rect x="14" y="22" width="36" height="32" rx="4" fill="#fff" stroke="#0E3A8C" stroke-width="2.5"/><path d="M22 22 V16 a10 10 0 0 1 20 0 V22" stroke="#0E3A8C" stroke-width="2.5"/><circle cx="32" cy="38" r="7" fill="#1A5FFF"/><path d="M32 34 v8 M29 36.5 h6" stroke="#fff" stroke-width="2"/><polyline points="44,12 52,6 58,10" stroke="#40C0FF" stroke-width="2.5"/>')

main=f'''  <main class="wrap narrow">
    <article class="prose wide">
      <h1>Yatırım ve emeklilik fonları</h1>
      <p>Türkiye'de yatırım fonlarına ve bireysel emeklilik sistemine (BES) ne kadar para girdi, kaç kişi yatırım yapıyor, para hangi tür fonlarda? TEFAS'ta işlem gören fonların büyüklükleri, yatırımcı sayıları ve aylık para girişleri ile Emeklilik Gözetim Merkezi'nin (EGM) katılımcı verileri. Veriler 11 Kasım 2026 itibarıyladır.</p>
    </article>

    <div class="kpi" id="kpi"></div>

    <nav class="tabs" role="tablist" aria-label="Bölümler"><button type="button" role="tab" data-t="yf" aria-selected="false">Yatırım fonları</button><button type="button" role="tab" data-t="bes" aria-selected="false">Emeklilik fonları ve BES</button></nav>

    <section class="grp" id="yf">
      <div class="gh-row">{ICON_YF}<h2 class="gh">Yatırım fonları</h2></div>
      <article class="prose wide"><p>Portföy yönetim şirketlerinin kurduğu yatırım fonlarının toplam büyüklüğü (serbest fonlar dahil, borsa yatırım fonları ve gayrimenkul/girişim sermayesi fonları hariç). Ay sonu değerleri, milyar TL.</p></article>
      <figure class="chart" id="c-yb"><figcaption>Yatırım fonlarının toplam büyüklüğü, ay sonu, milyar TL</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <figure class="chart" id="c-yt"><figcaption id="yt-cap"></figcaption>
        <div class="seg" role="group" aria-label="Görünüm"><button type="button" data-p="b" aria-pressed="true">Büyüklük</button><button type="button" data-p="d" aria-pressed="false">2026 değişimi</button><button type="button" data-p="a" aria-pressed="false">2026 net akım</button></div>
        <p class="yt-not" id="yt-not"></p>
        <div class="lg"></div><div class="rk"></div></figure>
      <figure class="chart" id="c-ya"><figcaption>Aylık net para girişi ve çıkışı, milyar TL</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <article class="prose wide"><p>Net akım, yatırımcıların fona yatırdığı paradan çektikleri paranın düşülmesiyle bulunur; fiyat değişimini içermez. Eylül 2026'da yatırım fonlarından yaklaşık 1,4 trilyon TL net çıkış oldu; bunun büyük bölümü serbest fonlar ve para piyasası fonlarındandı.</p></article>
      <figure class="chart" id="c-yy"><figcaption>Yatırımcı sayısı, ay sonu, milyon</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <details class="tbl"><summary>Tablo olarak göster</summary>
      <div class="twrap"><table class="kt" id="t-sem"><thead><tr><th>Fon türü</th><th>Fon sayısı</th><th>Büyüklük (milyar TL)</th><th>Yatırımcı</th><th>2026'da değişim</th></tr></thead><tbody></tbody></table></div>
      </details>
      <p class="calc-note">Yatırımcı sayısı, fonların açıkladığı yatırımcı sayılarının toplamıdır; birden fazla fonda yatırımı olan kişi her fonda ayrı sayılır, bu yüzden tekil yatırımcı sayısından yüksektir. Fon türleri SPK'nın şemsiye fon sınıflandırmasına göredir.</p>
    </section>

    <section class="grp" id="bes">
      <div class="gh-row">{ICON_BES}<h2 class="gh">Emeklilik fonları ve BES</h2></div>
      <article class="prose wide"><p>Bireysel emeklilik sisteminde katılımcıların birikimleri emeklilik yatırım fonlarında değerlendirilir. Gönüllü BES'te katılımcı sözleşmeyi kendisi açar; otomatik katılımda (OKS) işveren çalışanı sisteme dahil eder ve çalışan iki ay içinde cayabilir. Devlet, gönüllü BES'te ödenen katkı payının yüzde 20'si oranında devlet katkısı verir.</p></article>
      <h3 class="bd-h">Gönüllü BES ve OKS özet verileri, {EGM_TARIH}</h3>
      <p class="calc-note" style="margin-top:0">{EGM_OZET}</p>
      <div class="oz-grid">
        <article class="oz-card" id="oz-bes"></article>
        <article class="oz-card" id="oz-oks"></article>
      </div>
      <details class="tbl"><summary>Tablo olarak göster</summary>
      <article class="prose wide"><h3>Gönüllü BES</h3></article>
      <div class="twrap"><table class="kt" id="t-oz"><thead><tr><th>Kalem</th><th>Milyar TL</th><th>Pay</th></tr></thead><tbody></tbody></table></div>
      <article class="prose wide"><h3>Otomatik katılım (OKS)</h3></article>
      <div class="twrap"><table class="kt" id="t-oks"><thead><tr><th>Kalem</th><th>Milyar TL</th><th>Pay</th></tr></thead><tbody></tbody></table></div>
      </details>
      <p class="calc-note">Kaynak: EGM, BES ve OKS Özet Verileri, {EGM_TARIH}. Bir katılımcının birden fazla sözleşmesi, bir çalışanın birden fazla işveren üzerinden sertifikası olabilir; bu yüzden sözleşme ve sertifika sayıları kişi sayısından yüksektir. Faizsiz tutarlar, katılım esaslı (faizsiz) emeklilik fonlarındaki birikimdir. Devlet katkısı, katılımcının kendi birikiminden ayrı hesapta tutulur. Gönüllü BES'te birikimin yaklaşık üçte ikisi faizli fonlardayken, OKS'te birikimin yüzde 60'ı faizsiz fonlardadır.</p>
      <h3 class="bd-h">Birikim büyüklüğüne göre katılımcılar</h3>
      <article class="prose wide"><p>Gönüllü BES'te katılımcıların çoğunun birikimi küçük; fonların büyük kısmı ise az sayıda katılımcıda toplanıyor. EGM'nin 30 Eylül 2026 verileri.</p></article>
      <div class="kpi" id="kpi-bd"></div>
      <figure class="chart" id="c-bd"><figcaption>Birikim aralığına göre katılımcı sayısı, bin kişi</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <figure class="chart" id="c-bt"><figcaption>Birikim aralığına göre toplam fon tutarı, milyar TL (yaklaşık)</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <details class="tbl"><summary>Tablo olarak göster</summary>
      <div class="twrap"><table class="kt" id="t-bd"><thead><tr><th>Birikim aralığı (TL)</th><th>Katılımcı</th><th>Katılımcı payı</th><th>Fon tutarı (≈ milyar TL)</th><th>Fon payı</th></tr></thead><tbody></tbody></table></div>
      </details>
      <p class="calc-note">Kaynak: EGM, Fon Büyüklüğünün ve Katılımcı Adedinin Birikim Tutarı Aralıklarına Göre Dağılımı (GR-01-048), 30.09.2026. Katılımcı sayıları EGM'nin açıkladığı değerlerdir; aralık bazındaki fon tutarları EGM grafiğinden okunmuş yaklaşık değerlerdir. EGM'ye göre katılımcı başına ortalama birikim 204.451 TL.</p>
      <h3 class="bd-h">Fon büyüklüğü ve para girişleri</h3>
      <figure class="chart" id="c-pb"><figcaption>Emeklilik fonlarının toplam büyüklüğü, ay sonu, milyar TL</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <figure class="chart" id="c-pa"><figcaption>Emeklilik fonlarına aylık net para girişi, milyar TL</figcaption><div class="lg"></div><div class="plot"></div></figure>
      <p class="calc-note">Katılımcı ve çalışan sayıları ile fon tutarları EGM'nin {EGM_TARIH} tarihli BES ve OKS özet verileridir. Emeklilik fonlarının büyüklüğü ve para girişleri TEFAS fon verilerinden hesaplanmıştır; devlet katkısı fonları dahildir.</p>
    </section>

    <article class="prose">
      <h2>Notlar</h2>
      <p>Kaynak: Yatırım ve emeklilik fonlarının günlük büyüklük, yatırımcı sayısı ve para akımı verileri TEFAS'tan, Fintables üzerinden alınmıştır; BES katılımcı ve fon tutarları Emeklilik Gözetim Merkezi'nin (egm.org.tr) özet verileridir. Ay sonu değeri, ayın son işlem günündeki değerdir; Kasım 2026 için 11 Kasım değeri ve 1–11 Kasım akımları kullanılmıştır. 2024 Temmuz sonunda emeklilik fonu verisinde eksik gün olduğu için o ay 29 Temmuz değeri kullanılmıştır. Aylık net akım, günlük net akımların toplamıdır. Tablolar ve hesaplamalar yapay zekâ destekli araçlarla hazırlanmıştır; yatırım kararı vermeden önce verileri kaynağından teyit edin.</p>
    </article>
  </main>'''

script=f'''  <script>
    var D={json.dumps(D,ensure_ascii=False)};
{helpers}
{chartlib}
    var last=D.m[D.m.length-1],dec=D.m.filter(function(r){{return r[0]==='2025-12';}})[0],peak=D.m.reduce(function(a,r){{return r[1]>a[1]?r:a;}});
    document.getElementById('kpi').innerHTML=[
      ['Yatırım fonlarının büyüklüğü, trilyon TL',n2.format(last[1]/1000)],
      ['Emeklilik fonlarının büyüklüğü, trilyon TL',n2.format(last[3]/1000)],
      ['BES ve OKS katılımcı sayısı, milyon (EGM, 5 Kasım)','18,37'],
      ['Yatırım fonlarına 2026\\'da net akım, milyar TL',sg({ytd_m},n0)],
      ['Yatırım fonu büyüklüğü, Ağustos zirvesinden değişim',pc((last[1]/peak[1]-1)*100)],
      ['Emeklilik fonlarına 2026\\'da net akım, milyar TL',sg({ytd_p},n0)]
    ].map(function(x){{return '<div><b>'+x[1]+'</b><span>'+x[0]+'</span></div>';}}).join('');
    fill('t-sem',D.sem.map(function(r){{return '<tr><td>'+r[0]+'</td><td>'+n0.format(r[1])+'</td><td>'+n1.format(r[2])+'</td><td>'+n0.format(r[3])+'</td><td>'+(r[4]>2?pc((r[2]/r[4]-1)*100):'–')+'</td></tr>';}}).join(''));
    /* tür sıralaması: büyüklük / 2026 değişimi / 2026 net akım */
    var ytP='b';
    function ytDraw(){{
      var rows=D.sem.map(function(r){{return {{n:r[0],b:r[2],d:r[4]>2?(r[2]/r[4]-1)*100:null,t:r[2]-r[4],a:r[5]}};}});
      if(ytP==='d')rows=rows.filter(function(r){{return r.d!=null;}});
      var k=ytP;rows.sort(function(a,b){{return b[k]-a[k];}});
      var C={{b:'Fon türüne göre büyüklük, 11 Kasım 2026, milyar TL',d:'Fon türüne göre büyüklüğün 2026 başından bu yana değişimi',a:'Fon türüne göre 2026 net para girişi ve çıkışı, milyar TL'}};
      var N={{b:'',d:'Büyüklükteki değişim; yatırımcıların yatırdığı ve çektiği paranın yanında fonların getirisini ve yeni kurulan ya da kapanan fonları da içerir. Yüzdenin altında tutar (milyar TL) yazar.',a:'Net akım: yatırımcıların fonlara yatırdığı paradan çektikleri paranın düşülmesi. Fiyat değişimini içermez. 1 Ocak – 11 Kasım 2026.'}};
      document.getElementById('yt-cap').textContent=C[ytP];var nt=document.getElementById('yt-not');nt.textContent=N[ytP];nt.hidden=!N[ytP];
      var vs=rows.map(function(r){{return r[k];}}),lo=Math.min(0,Math.min.apply(null,vs)),hi=Math.max(0,Math.max.apply(null,vs)),span=hi-lo||1,z=(0-lo)/span*100,sgn=ytP!=='b';
      var sb=function(v,f){{return (v<0?'−':'+')+f(Math.abs(v));}};
      document.querySelector('#c-yt .rk').innerHTML=rows.map(function(r){{var v=r[k],p=(v-lo)/span*100,cl=sgn?(v<0?'neg':'pos'):'',txt;
        if(ytP==='b')txt=n0.format(v);
        else if(ytP==='d')txt=sb(v,function(x){{return '%'+n1.format(x);}})+'<small class="'+(r.t<0?'neg':'pos')+'">'+sb(r.t,function(x){{return n1.format(x);}})+' mlr TL</small>';
        else txt=sb(v,function(x){{return n1.format(x);}});
        return '<div class="rk-row"><span class="nm">'+r.n+'</span><span class="tr">'+(sgn?'<i class="z" style="left:'+z+'%"></i>':'')+'<i class="b" style="left:'+Math.min(p,z)+'%;width:'+Math.max(.6,Math.abs(p-z))+'%;background:'+(sgn?(v<0?DN:UP):C1)+'"></i></span><span class="vl '+cl+'">'+txt+'</span></div>';}}).join('');
    }}
    document.querySelectorAll('#c-yt .seg button').forEach(function(b){{b.addEventListener('click',function(){{ytP=b.dataset.p;document.querySelectorAll('#c-yt .seg button').forEach(function(x){{x.setAttribute('aria-pressed',x===b);}});ytDraw();}});}});
    ytDraw();
    (function(){{
      function card(el,d){{var rows=d.rows.map(function(r){{var t=r.a+r.b,p1=r.a/t*100,p2=100-p1;
        return '<div class="oz-row"><div class="oz-lab"><span>'+r.n+'</span><b>'+n1.format(t)+' milyar TL</b></div>'+
        '<div class="oz-bar"><i style="width:'+p1.toFixed(1)+'%;background:'+C1+'"></i><i style="width:'+p2.toFixed(1)+'%;background:'+C3+'"></i></div>'+
        '<div class="oz-pct"><span><i class="d" style="background:'+C1+'"></i>%'+n1.format(p1)+' faizli</span><span>%'+n1.format(p2)+' faizsiz (katılım)<i class="d" style="background:'+C3+'"></i></span></div></div>';}}).join('');
        document.getElementById(el).innerHTML='<h4>'+d.t+'</h4><p class="oz-big">'+d.big+' <small>'+d.unit+'</small></p><p class="oz-sub">toplam birikim, devlet katkısı dahil</p>'+
        '<dl class="oz-facts">'+d.facts.map(function(f){{return '<div><dt>'+f[0]+'</dt><dd>'+f[1]+(f[2]?'<small class="oz-dlt">'+f[2]+'</small>':'')+'</dd></div>';}}).join('')+'</dl>'+rows;}}
      card('oz-bes',{EGM_BES});
      card('oz-oks',{EGM_OKS});
      function tbl(id,OZ,T){{var base=0;fill(id,OZ.map(function(r){{if(r[2]===1)base=r[1];var sh=r[2]===1?r[1]/T*100:r[1]/base*100;return '<tr><td'+(r[2]===2?' style="padding-left:1.6rem;color:var(--muted)"':'')+'>'+(r[2]===1?'<b>'+r[0]+'</b>':r[0])+'</td><td>'+n1.format(r[1])+'</td><td>%'+n1.format(sh)+'</td></tr>';}}).join(''));}}
      tbl('t-oz',[['Katılımcıların fon tutarı',2089.6943,1],['Faizli',1345.7005,2],['Faizsiz (katılım)',743.9938,2],['Devlet katkısı fon tutarı',273.4677,1],['Faizli',239.9327,2],['Faizsiz (katılım)',33.5350,2]],2089.6943+273.4677);
      tbl('t-oks',[['Çalışanların fon tutarı',151.0791,1],['Faizli',60.1580,2],['Faizsiz (katılım)',90.9211,2],['Devlet katkısı fon tutarı',10.0603,1],['Faizli',3.9179,2],['Faizsiz (katılım)',6.1424,2]],151.0791+10.0603);
    }})();
    (function(){{var tc=D.bd.reduce(function(a,r){{return a+r[1];}},0),tt=D.bd.reduce(function(a,r){{return a+r[2];}},0);
      var small=D.bd[0][1]/tc*100,big=D.bd.slice(5),bc=big.reduce(function(a,r){{return a+r[1];}},0),bt=big.reduce(function(a,r){{return a+r[2];}},0);
      document.getElementById('kpi-bd').innerHTML=[['Birikimi 50 bin TL altında olan katılımcı payı','%'+n0.format(small)],['Birikimi 1 milyon TL üstü katılımcı, bin kişi',n0.format(bc/1000)],['Bu katılımcıların fonlardaki payı (yaklaşık)','%'+n0.format(bt/tt*100)],['Katılımcı başına ortalama birikim, TL','204.451']].map(function(x){{return '<div><b>'+x[1]+'</b><span>'+x[0]+'</span></div>';}}).join('');
      fill('t-bd',D.bd.map(function(r){{return '<tr><td>'+r[0]+'</td><td>'+n0.format(r[1])+'</td><td>%'+n1.format(r[1]/tc*100)+'</td><td>'+n0.format(r[2])+'</td><td>%'+n1.format(r[2]/tt*100)+'</td></tr>';}}).join(''));
      var lb=D.bd.map(function(r){{return r[0];}});
      chart('c-bd',{{type:'bar',labels:lb,fmt:function(v){{return n0.format(v)+' bin kişi';}},fmtAxis:function(v){{return n0.format(v);}},lw:60,series:[{{name:'Katılımcı',color:C1,values:D.bd.map(function(r){{return r[1]/1000;}})}}]}});
      chart('c-bt',{{type:'bar',labels:lb,fmt:function(v){{return '≈ '+n0.format(v)+' milyar TL';}},fmtAxis:function(v){{return n0.format(v);}},lw:60,series:[{{name:'Fon tutarı',color:C2,values:D.bd.map(function(r){{return r[2];}})}}]}});
    }})();
    var ms=D.m.map(function(r){{return r[0];}});
    var fT=function(v){{return n0.format(v)+' milyar TL';}},fTa=function(v){{return n0.format(v);}};
    chart('c-yb',{{type:'line',labels:ms,short:ayk,tipLabel:ay,fmt:fT,fmtAxis:fTa,lw:46,min:0,series:[{{name:'Yatırım fonları',color:C1,values:D.m.map(function(r){{return r[1];}})}}]}});
    chart('c-ya',{{type:'bar',sign:true,labels:D.fmm,short:ayk,tipLabel:ay,fmt:function(v){{return fB(v)+' milyar TL';}},fmtAxis:fTa,lw:46,series:[{{name:'Net akım',color:UP,values:D.fm}}]}});
    chart('c-yy',{{type:'line',labels:ms,short:ayk,tipLabel:ay,fmt:function(v){{return n2.format(v)+' milyon';}},fmtAxis:function(v){{return n0.format(v);}},lw:46,series:[{{name:'Yatırımcı sayısı',color:C3,values:D.m.map(function(r){{return r[2]/1e6;}})}}]}});
    chart('c-pb',{{type:'line',labels:ms,short:ayk,tipLabel:ay,fmt:fT,fmtAxis:fTa,lw:46,min:0,series:[{{name:'Emeklilik fonları',color:C2,values:D.m.map(function(r){{return r[3];}})}}]}});
    chart('c-pa',{{type:'bar',sign:true,labels:D.fmm,short:ayk,tipLabel:ay,fmt:function(v){{return fB(v)+' milyar TL';}},fmtAxis:fTa,lw:46,series:[{{name:'Net akım',color:UP,values:D.fp}}]}});
{resize}
{tabs}'''

css_extra='''    .rk{margin:.5rem 0 .25rem;font-family:var(--sans)}
    .rk-row{display:grid;grid-template-columns:10rem 1fr 4.2rem;align-items:center;gap:.6rem;padding:.28rem 0;font-size:.85rem}
    .rk-row .nm{color:var(--ink);font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
    .rk-row .tr{position:relative;height:16px}
    .rk-row .tr .b{position:absolute;top:0;height:100%;border-radius:3px}
    .rk-row .vl{text-align:right;font-weight:700;font-variant-numeric:tabular-nums}
    @media (max-width:600px){.rk-row{grid-template-columns:7.6rem 1fr 3.4rem;font-size:.78rem;gap:.4rem}}
  </style>'''
if '.rk-row{' not in head: head=head.replace('  </style>',css_extra)
head=head.replace('  </style>','    .bd-h{font-family:var(--sans);font-size:1.05rem;margin:2rem 0 .5rem;color:var(--ink)}\n    #c-yt .rk-row{grid-template-columns:10rem 1fr 6.5rem}\n    #c-yt .vl small{display:block;font-size:.72rem;font-weight:600;white-space:nowrap}\n    .yt-not{font-family:var(--sans);font-size:.78rem;color:var(--muted);margin:.4rem 0 0;max-width:46rem}\n    @media (max-width:600px){#c-yt .rk-row{grid-template-columns:7rem 1fr 5.5rem;gap:.35rem}#c-yt .seg button{padding:.35rem .6rem;font-size:.74rem}}\n    #c-yt .seg button{white-space:nowrap}\n  </style>',1)
head=head.replace('  </style>','''    .oz-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(19rem,1fr));gap:1rem;margin:.75rem 0 .75rem}
    .oz-card{background:var(--panel);border:1px solid var(--rule);border-radius:.8rem;padding:1.1rem 1.2rem;font-family:var(--sans)}
    .oz-card h4{margin:0;font-size:.8rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
    .oz-big{margin:.15rem 0 0;font-size:1.9rem;font-weight:700;color:var(--navy);font-variant-numeric:tabular-nums}
    .oz-big small{font-size:.95rem;font-weight:600;color:var(--muted)}
    .oz-sub{margin:0;font-size:.78rem;color:var(--muted)}
    .oz-facts{display:flex;gap:1.4rem;flex-wrap:wrap;margin:.8rem 0 .2rem;padding:.6rem 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
    .oz-facts div{display:grid;gap:.1rem}
    .oz-facts dt{font-size:.72rem;color:var(--muted)}
    .oz-facts dd{margin:0;font-size:.95rem;font-weight:700;font-variant-numeric:tabular-nums}
    .oz-row{margin:.95rem 0 0}
    .oz-lab{display:flex;justify-content:space-between;align-items:baseline;gap:.5rem;font-size:.82rem;margin-bottom:.35rem}
    .oz-lab b{font-variant-numeric:tabular-nums;white-space:nowrap}
    .oz-bar{display:flex;gap:2px;height:22px;border-radius:6px;overflow:hidden}
    .oz-bar i{display:block;height:100%}
    .oz-pct{display:flex;justify-content:space-between;gap:.5rem;font-size:.74rem;color:var(--muted);margin-top:.35rem;font-variant-numeric:tabular-nums}
    .oz-pct .d{display:inline-block;width:.6rem;height:.6rem;border-radius:2px;margin:0 .35rem;vertical-align:-1px}
  </style>''',1)
out='\n'.join([head,header,main,footer,script])
open(SITE+'araclar/fonlar.html','w').write(out)
print('ok',ytd_m,ytd_p)
