#!/usr/bin/env python3
"""CFA Level I tam deneme (mock exam) sayfasını üretir.
Kullanım: python3 scripts/cfa/mock.py
Sorular, on konu sayfasının (build.py çıktısı) içindeki S verisinden okunur; önce konu sayfalarını üretin.
İki oturum, 90'ar soru, 135'er dakika. Konu başına soru sayısı resmi ağırlık aralıklarının içindedir."""
import json, pathlib

KOK = pathlib.Path(__file__).resolve().parents[2]
CFA = KOK / "calisma-masasi/cfa-level-1"

# (anahtar, slug, ad, oturum, soru sayısı, renk, resmi ağırlık)
KONULAR = [  # Şubat 2027'den itibaren geçerli adlar, oturumlar ve ağırlıklar (CFA Institute)
    ("eth", "ethical-and-professional-standards", "Ethical and Professional Standards", 1, 23, "#003894", "10–15%"),
    ("qm", "quantitative-methods", "Quantitative Methods", 1, 22, "#0E7C86", "11–14%"),
    ("econ", "economics", "Economics", 1, 12, "#B45309", "6–9%"),
    ("fsa", "financial-statement-analysis", "Financial Statement Analysis", 1, 21, "#6D28D9", "11–14%"),
    ("corp", "corporate-issuers", "Corporate Finance", 1, 12, "#BE185D", "6–9%"),
    ("eq", "equity-investments", "Equities", 2, 22, "#15803D", "11–14%"),
    ("fi", "fixed-income", "Fixed Income", 2, 22, "#1D4ED8", "11–14%"),
    ("der", "derivatives", "Derivatives and Risk Management", 2, 13, "#C2410C", "6–9%"),
    ("alt", "alternative-investments", "Alternative Investments", 2, 14, "#0F766E", "6–9%"),
    ("pm", "portfolio-management", "Portfolio Construction", 2, 19, "#7C3AED", "8–12%"),
]
for o in (1, 2):
    assert sum(k[4] for k in KONULAR if k[3] == o) == 90

def oku(slug):
    h = (CFA / slug / "index.html").read_text(encoding="utf-8")
    i = h.index("const S = ") + 10
    return json.JSONDecoder().raw_decode(h, i)[0], h

T = []; ornek = None
for key, slug, ad, otr, n, renk, pay in KONULAR:
    S, h = oku(slug); ornek = ornek or h
    qs = [[q[0], q[1], q[2], q[3], s["n"]] for s in S for q in s["qs"]]
    assert len(qs) >= n * 3, key
    T.append(dict(id=key, n=ad, o=otr, w=n, c=renk, p=pay, u=f"/calisma-masasi/cfa-level-1/{slug}/", qs=qs))
TOPLAM = sum(len(t["qs"]) for t in T)

URL = "https://ibrahimethemafacan.com/calisma-masasi/cfa-level-1/mock-exam/"
TITLE = "CFA Level I · Full Mock Exam"
DESC = "A full-length CFA Level I mock exam: 180 three-choice questions in two timed sessions of 135 minutes, weighted by topic as in the exam."

# Baş kısım (stil, üst şerit) konu sayfasından alınır; başlık, açıklama ve adres değiştirilir.
bas = ornek[: ornek.index('<div class="wrap">')]
import re
bas = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", bas)
bas = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + DESC, bas)
bas = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + TITLE, bas)
bas = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + DESC, bas)
bas = re.sub(r'(<link rel="canonical" href=")[^"]*', r"\g<1>" + URL, bas)
bas = re.sub(r'(<meta property="og:url" content=")[^"]*', r"\g<1>" + URL, bas)
EK = """<style>
.sess{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin:16px 0}
.scard{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:16px}
.scard h3{font:700 19px/1.25 var(--f-display,var(--f-body));margin:0 0 4px}
.scard .sub{color:var(--muted);font:500 13.5px/1.5 var(--f-body);margin:0 0 10px}
.scard ul{list-style:none;margin:0 0 14px;padding:0;font:500 14px/1.5 var(--f-body)}
.scard li{display:flex;justify-content:space-between;gap:10px;padding:4px 0;border-bottom:1px solid var(--line)}
.scard li span:last-child{font-family:var(--f-mono);color:var(--muted)}
.scard .last{font:600 13.5px/1.4 var(--f-mono);color:var(--num);margin:0 0 12px}
.stick{position:sticky;top:0;z-index:5;background:var(--bg,var(--surface));padding:8px 0;border-bottom:1px solid var(--line)}
.bar a{color:inherit}
</style>
"""
bas = bas.replace("</head>", EK + "</head>")

GOVDE = f"""<div class="wrap">
  <header class="top">
    <div class="eyebrow">CFA Program · Level I</div>
    <h1>Full Mock Exam</h1>
    <p class="lede">A full-length practice exam in the format of the real one: 180 three-choice questions in two sessions of 135 minutes. Each attempt draws a fresh set from a pool of {TOPLAM:,} questions, weighted by topic as in the exam.</p>
    <div class="tip"><b>How it works</b>Session 1 covers Ethics, Quantitative Methods, Economics, Financial Statement Analysis and Corporate Finance. Session 2 covers Equities, Fixed Income, Derivatives and Risk Management, Alternative Investments and Portfolio Construction. Topic weights are those in effect from February 2027. Answers and explanations appear when you finish a session, with a breakdown by topic. An unfinished session is kept on this device, so you can leave and come back; the clock keeps running.</div>
  </header>
  <main id="main"></main>
</div>
<script>
"""

ENGINE = r"""
const SEC=135*60,NQ=90,LS="cfa-l1-mock-v1",L="ABC";
let st={};try{st=JSON.parse(localStorage.getItem(LS)||"{}")}catch(e){st={}}
function save(){try{localStorage.setItem(LS,JSON.stringify(st))}catch(e){}}
const $=s=>document.querySelector(s);let tick=null;
const tp=id=>T.find(t=>t.id===id);
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function fmt(x){x=Math.max(0,Math.round(x));const h=Math.floor(x/3600),m=Math.floor(x%3600/60),s=x%60;return (h?h+":":"")+String(m).padStart(2,"0")+":"+String(s).padStart(2,"0")}
function start(o){const qs=[];T.filter(t=>t.o===o).forEach(t=>{shuffle([...t.qs.keys()]).slice(0,t.w).forEach(i=>qs.push([t.id,i]))});
  st.run={o,qs,ans:{},t0:Date.now(),done:false,used:0};save();render();scrollTo(0,0)}
function stopTick(){if(tick){clearInterval(tick);tick=null}}
function showTime(){const r=st.run;if(!r||r.done)return;const u=(Date.now()-r.t0)/1000,el=$("#timer");if(el)el.textContent=u<=SEC?fmt(SEC-u)+" left":"over by "+fmt(u-SEC)}
function score(r){let ok=0;const per={};r.qs.forEach((x,k)=>{const q=tp(x[0]).qs[x[1]];per[x[0]]=per[x[0]]||{ok:0,t:0};per[x[0]].t++;if(r.ans[k]===q[2]){ok++;per[x[0]].ok++}});return{ok,per}}
function finish(){const r=st.run;r.done=true;r.used=(Date.now()-r.t0)/1000;const s=score(r);st.last=st.last||{};st.last[r.o]={ok:s.ok,used:r.used,d:Date.now()};save();stopTick();render();scrollTo(0,0)}
function qCard(q,k,chosen,reveal){
  const opts=q[1].map((o,j)=>{let c="";if(chosen===j)c="sel";if(reveal){if(j===q[2])c="right";else if(chosen===j)c="wrong"}
    return `<button data-o="${j}" class="${c}" ${reveal?"disabled":""}><span class="l">${L[j]}</span><span>${o}</span></button>`}).join("");
  const exp=reveal?`<div class="exp"><strong>${chosen===q[2]?"Correct.":(chosen===undefined?"Not answered. ":"")+"The answer is "+L[q[2]]+"."}</strong> ${q[3]}</div>`:"";
  return `<div class="q"><div class="qt"><span class="qn">${String(k+1).padStart(2,"0")}</span><span>${q[0]}</span></div>${reveal?`<div class="tag">${q[4]}</div>`:""}<div class="opts" data-q="${k}">${opts}</div>${exp}</div>`}
function home(){
  const card=o=>{const ts=T.filter(t=>t.o===o),l=(st.last||{})[o],r=st.run&&!st.run.done&&st.run.o===o;
    return `<div class="scard"><h3>Session ${o}</h3><p class="sub">90 questions · 135 minutes</p>
    <ul>${ts.map(t=>`<li><span>${t.n}</span><span>${t.w}</span></li>`).join("")}</ul>
    ${l?`<p class="last">Last attempt: ${l.ok} / 90 · ${Math.round(l.ok/90*100)}%</p>`:""}
    <div class="qbar">${r?`<button class="btn primary" data-act="resume">Continue</button><button class="btn" data-act="start" data-s="${o}">Start over</button>`:`<button class="btn primary" data-act="start" data-s="${o}">Start session ${o}</button>`}</div></div>`};
  const a=(st.last||{})[1],b=(st.last||{})[2];
  const tot=a&&b?`<div class="result"><div class="eyebrow">Both sessions, last attempts</div><div class="big">${a.ok+b.ok} / 180 <span style="font-size:18px;color:var(--muted)">${Math.round((a.ok+b.ok)/180*100)}%</span></div></div>`:"";
  $("#main").innerHTML=tot+`<div class="sess">${card(1)}${card(2)}</div>
  <div class="notes"><p>Take the two sessions on the same day with a break in between for the closest match to exam conditions. CFA Institute does not publish a pass mark; many candidates aim for about 70% on practice exams. Questions here are original practice questions, not official CFA Institute questions.</p></div>`}
function exam(){const r=st.run,n=Object.keys(r.ans).length;let head="";
  if(r.done){const s=score(r);head=`<div class="result"><div class="eyebrow">Session ${r.o} result</div><div class="big">${s.ok} / ${NQ} <span style="font-size:18px;color:var(--muted)">${Math.round(s.ok/NQ*100)}% · ${fmt(r.used)} used</span></div>
    <div class="bars">${T.filter(t=>t.o===r.o).map(t=>{const p=s.per[t.id]||{ok:0,t:0};return `<div class="bar" style="--c:${t.c}"><span class="nm"><a href="${t.u}">${t.n}</a></span><span class="track"><span class="fill" style="width:${p.t?p.ok/p.t*100:0}%;display:block"></span></span><span class="v">${p.ok}/${p.t}</span></div>`}).join("")}</div>
    <div class="qbar"><button class="btn primary" data-act="home">Back to sessions</button><button class="btn" data-act="start" data-s="${r.o}">New session ${r.o}</button></div></div>`}
  const fin=`<button class="btn primary" data-act="finish">Finish and see answers</button>`;
  $("#main").innerHTML=`<div class="sec-head"><div class="eyebrow">Full mock exam</div><h2>Session ${r.o}</h2></div>${head}
    ${r.done?"":`<div class="qbar stick"><span class="score">${n} / ${NQ} answered</span><span class="timer" id="timer"></span><button class="btn" data-act="home">Pause</button></div>`}
    <div class="qlist">${r.qs.map((x,k)=>qCard(tp(x[0]).qs[x[1]],k,r.ans[k],r.done)).join("")}</div>
    ${r.done?"":`<div class="qbar" style="margin-top:16px">${fin}</div>`}`;
  if(!r.done){stopTick();tick=setInterval(showTime,1000);showTime()}}
let view="home";
function render(){if(view==="exam"&&st.run)exam();else{stopTick();home()}}
document.addEventListener("click",e=>{
  const a=e.target.closest("[data-act]");
  if(a){const k=a.dataset.act;
    if(k==="start"){const o=+a.dataset.s;if(st.run&&!st.run.done&&Object.keys(st.run.ans).length&&!a.dataset.sure){a.dataset.sure="1";a.textContent="Discard the unfinished session?";return}view="exam";start(o);return}
    if(k==="resume"){view="exam";render();scrollTo(0,0);return}
    if(k==="home"){view="home";if(st.run&&st.run.done){delete st.run;save()}render();scrollTo(0,0);return}
    if(k==="finish"){const left=NQ-Object.keys(st.run.ans).length;if(left&&!a.dataset.sure){document.querySelectorAll('[data-act="finish"]').forEach(b=>{b.dataset.sure="1";b.textContent=left+" unanswered. Finish anyway?"});return}finish();return}}
  const o=e.target.closest("[data-o]");if(!o||o.disabled||!st.run||st.run.done)return;
  const qi=+o.parentElement.dataset.q;st.run.ans[qi]=+o.dataset.o;save();
  o.parentElement.querySelectorAll("button").forEach(b=>b.classList.toggle("sel",b===o));
  const sc=$(".score");if(sc)sc.textContent=`${Object.keys(st.run.ans).length} / ${NQ} answered`;
  document.querySelectorAll('[data-act="finish"]').forEach(b=>{delete b.dataset.sure;b.textContent="Finish and see answers"})});
if(st.run&&st.run.done){delete st.run;save()}
render();
</script>
<script data-goatcounter="https://ibrahimethemafacan.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body></html>
"""

html = bas + GOVDE + "const T = " + json.dumps(T, ensure_ascii=False).replace("</", "<\\/") + ";\n" + ENGINE
hedef = CFA / "mock-exam/index.html"
hedef.parent.mkdir(parents=True, exist_ok=True)
hedef.write_text(html, encoding="utf-8")
print("havuz:", TOPLAM, "soru | yazıldı:", hedef.relative_to(KOK), f"{len(html)//1024} KB")
