#!/usr/bin/env python3
"""CFA Level I çalışma sayfasını üretir.
Kullanım: python3 scripts/cfa/build.py
Kullanım: python3 scripts/cfa/build.py [qm|econ|corp|fsa|eq|fi|der|alt|pm|eth]. İçerik: scripts/cfa/<konu>/r*.py (her dosyada R listesi). Görsel stil MASAK Modül 2 sayfasından alınır."""
import json, re, sys, pathlib, importlib.util, collections

KOK = pathlib.Path(__file__).resolve().parents[2]
BURASI = pathlib.Path(__file__).resolve().parent

def yukle(yol):
    spec = importlib.util.spec_from_file_location(yol.stem, yol)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.R

KONULAR = {
    "qm": dict(slug="quantitative-methods", ad="Quantitative Methods", sayi="Eleven", pay="11–14%", dengele=True),
    "econ": dict(slug="economics", ad="Economics", sayi="Eight", pay="6–9%", dengele=True),
    "corp": dict(slug="corporate-issuers", ad="Corporate Finance", sayi="Seven", pay="6–9%", dengele=True),
    "fsa": dict(slug="financial-statement-analysis", ad="Financial Statement Analysis", sayi="Twelve", pay="11–14%", dengele=True),
    "eq": dict(slug="equity-investments", ad="Equities", sayi="Eight", pay="11–14%", dengele=True),
    "fi": dict(slug="fixed-income", ad="Fixed Income", sayi="Nineteen", pay="11–14%", dengele=True),
    "der": dict(slug="derivatives", ad="Derivatives and Risk Management", sayi="Ten", pay="6–9%", dengele=True),
    "alt": dict(slug="alternative-investments", ad="Alternative Investments", sayi="Seven", pay="6–9%", dengele=True),
    "pm": dict(slug="portfolio-management", ad="Portfolio Construction", sayi="Six", pay="8–12%", dengele=True),
    "eth": dict(slug="ethical-and-professional-standards", ad="Ethical and Professional Standards", sayi="Ten", pay="10–15%", dengele=True, birim="sections"),
    # Sınav İngilizcesi: müfredat konusu değil; anlatım Türkçe, örnekler İngilizce
    "eng": dict(slug="english-for-the-exam", ad="English for the Exam", sayi="Twelve", pay="", dengele=True, birim="units", etiket="Unit",
        title="CFA Level I · English for the Exam (Sınava Yönelik İngilizce)",
        desc="CFA Level I sınav sorularını doğru okumak için İngilizce hazırlık: soru kökleri, yön ve miktar ifadeleri, bağlaçlar, olumsuzluk tuzakları, karıştırılan kelimeler; Türkçe açıklamalı.",
        lede="İngilizcesi yeterli gelmeyenler için sınava yönelik hazırlık. Konu bilgisi değil, sınav sorularının dili: soru kökleri, yön ve miktar ifadeleri, bağlaçlar, olumsuzluk tuzakları ve en çok karıştırılan kelimeler. 12 ünite; her birinde Türkçe açıklamalı ifadeler, kısa notlar ve sınav formatında alıştırma soruları var.",
        tip="<b>Nasıl çalışılır</b>Konulara başlamadan önce bu bölümü bir kez bitirin, sonra takıldıkça dönün. Sınavda soru başına yaklaşık <span class=\"n\">90</span> saniye var; sorunun ne istediğini ilk okuyuşta anlamak, bilgiyi bilmek kadar önemli. Açıklamalar Türkçe, örnek cümleler sınavdaki gibi İngilizce."),
}
ANAHTAR = sys.argv[1] if len(sys.argv) > 1 else "qm"
KONU = KONULAR[ANAHTAR]

S = []
for f in sorted((BURASI / ANAHTAR).glob("r*.py")):
    S += yukle(f)

# --- ek dosyalar (ek*.py): mevcut okumalara terim, not ve soru ekler ---
for f in sorted((BURASI / ANAHTAR).glob("ek*.py")):
    spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for sid, e in m.EK.items():
        s_ = next(x for x in S if x["id"] == sid)
        s_["terms"] += e.get("terms", [])
        s_["notes"] += e.get("notes", "")
        s_["qs"] += e.get("qs", [])

# --- doğru şık dengesi: yalnızca sözel ve benzer uzunluktaki şıklarda, en sık kullanılan doğru şıkkı en az kullanılanla yer değiştir ---
def _sayisal(o): return bool(re.search(r"\d", o))
if KONU.get("dengele"):
    say = collections.Counter(q[2] for s in S for q in s["qs"])
    esik = sum(len(t["qs"]) for t in S) / 3 + 1
    for s in S:
        for q in s["qs"]:
            o = q[1]; i = q[2]
            if say[i] <= esik or say[i] != max(say[k] for k in (0, 1, 2)): continue
            if any(_sayisal(x) for x in o) or max(map(len, o)) - min(map(len, o)) > 14: continue
            j = min((k for k in (0, 1, 2) if k != i), key=lambda k: say[k])
            o[i], o[j] = o[j], o[i]; q[2] = j; say[i] -= 1; say[j] += 1

# --- denetimler ---
def sayi(o):
    m = re.fullmatch(r"[−-]?\$?([\d,]+(?:\.\d+)?)%?", o.strip())
    if not m: return None
    v = float(m.group(1).replace(",", ""))
    return -v if o.strip()[0] in "−-" else v
dag = collections.Counter(); uyari = []
for s in S:
    assert len(s["qs"]) >= s["w"], s["id"]
    for i, q in enumerate(s["qs"]):
        assert len(q) == 4 and len(q[1]) == 3 and q[2] in (0, 1, 2), (s["id"], i)
        dag[q[2]] += 1
        ns = [sayi(o) for o in q[1]]
        if all(n is not None for n in ns) and ns != sorted(ns): uyari.append(f"{s['id']} q{i+1}: sayısal şıklar artan sırada değil {q[1]}")
        low = " ".join(q[1]).lower()
        if "all of the above" in low or "none of the above" in low: uyari.append(f"{s['id']} q{i+1}: yasak şık")
print("okuma:", len(S), "| soru:", sum(len(s["qs"]) for s in S), "| terim:", sum(len(s["terms"]) for s in S), "| doğru şık dağılımı A/B/C:", [dag[k] for k in (0, 1, 2)])
for u in uyari: print("UYARI", u)

masak = (KOK / "calisma-masasi/masak-modul-2/index.html").read_text(encoding="utf-8")
_i = masak.index("<style>\n/* Layout")
css = "body{margin:0}" + masak[_i + 7: masak.index("</style>", _i)]

EK_CSS = """
.notes p.f{font:500 13.5px/1.7 var(--f-mono);background:var(--sunk);border-radius:6px;padding:8px 12px;margin:10px 0;overflow-wrap:anywhere;color:var(--ink)}
.notes p.f sub,.notes p.f sup{font-size:.72em}
.terms{display:grid;gap:10px}
.term{background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:12px 14px}
.term .th{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline;margin-bottom:6px}
.term .en{font:600 15.5px/1.3 var(--f-body)}
.term .tr{font:500 13.5px/1.3 var(--f-body);color:var(--accent)}
.term p{margin:0;max-width:74ch}
.term p+p{margin-top:6px;color:var(--muted)}
.term .lg{font:600 10.5px/1 var(--f-mono);color:var(--muted);border:1px solid var(--line);border-radius:4px;padding:2px 4px;margin-right:7px;vertical-align:1px}
.tsearch{width:100%;font:15px var(--f-body);padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);margin-bottom:14px}
.tsearch:focus{outline:2px solid var(--accent);outline-offset:-1px}
.tgroup{font:600 13px/1.3 var(--f-body);color:var(--muted);margin:18px 0 8px}
.timer{font:600 14px var(--f-mono);color:var(--num);background:var(--num-soft);border-radius:6px;padding:5px 9px}
"""

N_EXAM = sum(s["w"] for s in S)
N_TERM = sum(len(s["terms"]) for s in S)
LEDE = KONU.get("lede") or f"""{KONU["sayi"]} {KONU.get("birim", "readings")}, in curriculum order. Each opens with its key terms, explained in English and Turkish, followed by concise notes and three-choice practice questions. A {N_EXAM}-question timed mock exam is at the end."""
TIP = KONU.get("tip") or f"""<b>Exam format</b>Level I has <span class="n">180</span> multiple-choice questions in two sessions of <span class="n">135</span> minutes, about <span class="n">90</span> seconds per question. Every question has three choices, A, B and C, and there is no penalty for a wrong answer. {KONU["ad"]} carries roughly <span class="n">{KONU["pay"]}</span> of the exam (weights in effect from February 2027)."""
URL = f"https://ibrahimethemafacan.com/calisma-masasi/cfa-level-1/{KONU['slug']}/"
TITLE = KONU.get("title") or f"CFA Level I · {KONU['ad']} Study Desk"
DESC = KONU.get("desc") or f"Study notes, key terms in English and Turkish, three-choice practice questions and a timed mock exam for CFA Level I {KONU['ad']}."

HEAD = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{URL}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/img/favicon-192.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="İbrahim Ethem Afacan">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="https://ibrahimethemafacan.com/img/og-calisma-masasi.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@ibrahim___ethem">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,700&display=swap">
<style>{css}{EK_CSS}</style>
<style id="nosel">body{{-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}}input,textarea,select{{-webkit-user-select:text;user-select:text}}</style>
<link rel="manifest" href="/manifest.webmanifest">
<script defer src="/sayac.js?v=2"></script>
<meta name="theme-color" content="#F5F8FC">
<script src="/pwa.js" defer></script>
</head><body>
<div class="iea-bar" style="margin:0 calc(-1 * max(16px,env(safe-area-inset-right,0px))) 0 calc(-1 * max(16px,env(safe-area-inset-left,0px)));background:#003894;color:#D6E6FB;font:500 13px/1.45 Manrope,system-ui,-apple-system,'Segoe UI',sans-serif;padding:10px max(16px,env(safe-area-inset-left,0px));padding-top:max(10px,env(safe-area-inset-top,0px))">
  <div style="max-width:1180px;margin:0 auto;display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;justify-content:space-between">
    <nav style="display:flex;gap:14px;flex-wrap:wrap;align-items:center"><a href="/" style="color:#fff;font-weight:800;text-decoration:none">İbrahim Ethem Afacan</a><a href="/calisma-masasi/" style="color:#6BE3FF;font-weight:700;text-decoration:none">← Çalışma Masası</a></nav>
    <span>Independent study material. Not affiliated with or endorsed by CFA Institute.</span>
  </div>
</div>
<div class="wrap">
  <header class="top">
    <div class="eyebrow">CFA Program · Level I</div>
    <h1>{KONU["ad"]}</h1>
    <p class="lede">{LEDE}</p>
    <div class="tip">{TIP}</div>
    <div class="weights" id="weights" aria-label="Mock exam questions per reading"></div>
    <div class="wlegend"><span>Bar width = questions drawn from the reading in the mock exam</span><span>{sum(len(s["qs"]) for s in S)} practice questions · {N_TERM} key terms</span></div>
  </header>
  <div class="layout">
    <nav class="tabs" id="tabs" aria-label="Readings"></nav>
    <main id="main"></main>
  </div>
</div>
<script>
"""

ENGINE = r"""
const N_EXAM=__NEXAM__,N_TERM=__NTERM__,EXAM_SEC=N_EXAM*90;
const LS="cfa-l1-__KEY__-v1";let st={};try{st=JSON.parse(localStorage.getItem(LS)||"{}")}catch(e){st={}}
function save(){try{localStorage.setItem(LS,JSON.stringify(st))}catch(e){}}
const $=s=>document.querySelector(s);const L="ABC";
let cur=null,mode="terms",exam=null,tick=null,tq="";
const esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function sectionStats(s){const a=st[s.id]||{};let d=0,ok=0;s.qs.forEach((q,i)=>{if(a[i]!==undefined){d++;if(a[i]===q[2])ok++}});return{d,ok,t:s.qs.length}}
function scoreText(t){return `${t.ok} correct · ${t.d-t.ok} wrong · ${t.t-t.d} unanswered`}
function renderWeights(){$("#weights").innerHTML=S.map(s=>`<button style="flex:${s.w};background:${s.c}" title="${s.n}: ${s.w}" data-go="${s.id}">${s.w}</button>`).join("")}
function renderTabs(){
  const items=S.map(s=>{const t=sectionStats(s);return `<button style="--c:${s.c}" data-go="${s.id}" aria-current="${cur===s.id}"><span class="dot"></span><span>${s.n}</span><span class="cnt">${t.d}/${t.t}</span></button>`}).join("");
  $("#tabs").innerHTML=`<button style="--c:var(--num)" data-go="terms" aria-current="${cur==="terms"}"><span class="dot"></span><span>Key Terms</span><span class="cnt">${N_TERM}</span></button><div class="sep"></div>`+items+`<div class="sep"></div>`+
  `<button style="--c:var(--ink)" data-go="mock" aria-current="${cur==="mock"}"><span class="dot"></span><span>Mock Exam</span><span class="cnt">${N_EXAM}</span></button>`;
}
function go(id){cur=id;if(id!=="mock"){exam=null;stopTick()}render();try{history.replaceState(null,"","#"+id)}catch(e){}
  const m=$("#main");if(m.getBoundingClientRect().top<0)m.scrollIntoView({block:"start"})}
function qCard(q,idx,label,chosen,reveal,attrs,tag){
  const opts=q[1].map((o,j)=>{let cls="";if(chosen===j)cls="sel";if(reveal){if(j===q[2])cls="right";else if(chosen===j)cls="wrong"}
    return `<button ${attrs} data-o="${j}" class="${cls}" ${reveal?"disabled":""}><span class="l">${L[j]}</span><span>${o}</span></button>`}).join("");
  const exp=reveal?`<div class="exp"><strong>${chosen===q[2]?"Correct.":(chosen===undefined?"Not answered. ":"")+"The answer is "+L[q[2]]+"."}</strong> ${q[3]}</div>`:"";
  return `<div class="q"><div class="qt"><span class="qn">${label}</span><span>${q[0]}</span></div>${tag?`<div class="tag">${tag}</div>`:""}<div class="opts" data-q="${idx}">${opts}</div>${exp}</div>`;
}
function termCard(t){return `<div class="term"><div class="th"><span class="en">${t[0]}</span><span class="tr">${t[1]}</span></div><p><span class="lg">EN</span>${t[2]}</p><p lang="tr"><span class="lg">TR</span>${t[3]}</p></div>`}
function termList(){const f=tq.trim().toLocaleLowerCase("tr");let h="",n=0;
  S.forEach((s,i)=>{const ts=s.terms.filter(t=>!f||t.join(" ").toLocaleLowerCase("tr").includes(f));if(!ts.length)return;n+=ts.length;
    h+=`<div class="tgroup">__ETIKET__ ${i+1} · ${s.n}</div><div class="terms">${ts.map(termCard).join("")}</div>`});
  return h||`<p style="color:var(--muted)">No term matches “${esc(tq)}”.</p>`}
function render(){
  renderTabs();const m=$("#main");
  if(cur==="terms"){m.innerHTML=`<div class="sec-head"><div class="eyebrow">Glossary</div><h2>Key Terms</h2><div class="meta"><span class="chip">${N_TERM} terms</span><span class="chip">English and Turkish explanations</span></div></div>
    <input class="tsearch" id="tsearch" type="search" placeholder="Search a term in English or Turkish" value="${esc(tq)}" aria-label="Search terms"><div id="tlist">${termList()}</div>`;return}
  if(cur==="mock"){renderExam(m);return}
  const s=S.find(x=>x.id===cur);const t=sectionStats(s);
  m.innerHTML=`<div class="sec-head" style="--c:${s.c}"><div class="eyebrow">__ETIKET__ ${S.indexOf(s)+1} of ${S.length}</div><h2>${s.n}</h2>
    <div class="meta"><span class="chip strong">${s.qs.length} practice questions</span><span class="chip">${s.terms.length} key terms</span></div></div>
    <div class="switch three" role="group" aria-label="View"><button data-mode="terms" aria-pressed="${mode==="terms"}">Terms</button><button data-mode="notes" aria-pressed="${mode==="notes"}">Notes</button><button data-mode="qs" aria-pressed="${mode==="qs"}">Questions</button></div>
    <div id="body"></div>`;
  const b=$("#body");
  if(mode==="notes"){b.innerHTML=`<div class="notes">${s.notes}</div><div class="qbar" style="margin-top:16px"><button class="btn primary" data-mode="qs">Practice questions</button></div>`;return}
  if(mode==="terms"){b.innerHTML=`<div class="terms">${s.terms.map(termCard).join("")}</div><div class="qbar" style="margin-top:16px"><button class="btn primary" data-mode="notes">Read the notes</button></div>`;return}
  const a=st[s.id]||{};
  b.innerHTML=`<div class="qbar"><span class="score">${scoreText(t)}</span><button class="btn" data-reset="${s.id}">Reset</button>${t.d-t.ok>0?`<button class="btn" data-wrong="${s.id}">Retry wrong answers</button>`:""}</div>
    <div class="qlist">${s.qs.map((q,i)=>qCard(q,i,String(i+1).padStart(2,"0"),a[i],a[i]!==undefined,`data-sec="${s.id}"`)).join("")}</div>`;
}
function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function buildExam(){const qs=[];S.forEach(s=>{shuffle([...s.qs.keys()]).slice(0,s.w).forEach(i=>qs.push({s:s.id,i}))});
  exam={qs,ans:{},done:false,t0:Date.now(),used:0};stopTick();tick=setInterval(showTime,1000)}
function stopTick(){if(tick){clearInterval(tick);tick=null}}
function fmt(x){x=Math.max(0,Math.round(x));return String(Math.floor(x/60)).padStart(2,"0")+":"+String(x%60).padStart(2,"0")}
function showTime(){if(!exam||exam.done)return;const u=(Date.now()-exam.t0)/1000;const el=$("#timer");if(el)el.textContent=u<=EXAM_SEC?fmt(EXAM_SEC-u)+" left":"over by "+fmt(u-EXAM_SEC)}
function renderExam(m){
  if(!exam){m.innerHTML=`<div class="sec-head"><div class="eyebrow">Exam practice</div><h2>Mock Exam</h2><div class="meta"><span class="chip strong">${N_EXAM} questions</span><span class="chip">${fmt(EXAM_SEC).slice(0,2)} minutes</span><span class="chip">90 seconds per question</span></div></div>
    <div class="notes"><p>Questions are drawn at random from all __NREAD__ and presented in curriculum order, as in the exam. Answers and explanations appear when you finish, together with a breakdown by reading that shows where to return.</p></div>
    <div class="qbar" style="margin-top:16px"><button class="btn primary" data-exam="start">Start the mock exam</button></div>`;return}
  const n=Object.keys(exam.ans).length;let head="";
  if(exam.done){let ok=0;const per={};exam.qs.forEach((x,k)=>{const q=S.find(s=>s.id===x.s).qs[x.i];per[x.s]=per[x.s]||{ok:0,t:0};per[x.s].t++;if(exam.ans[k]===q[2]){ok++;per[x.s].ok++}});
    head=`<div class="result"><div class="eyebrow">Result</div><div class="big">${ok} / ${N_EXAM} <span style="font-size:18px;color:var(--muted)">${Math.round(ok/N_EXAM*100)}% · ${fmt(exam.used)} used</span></div>
    <div class="bars">${S.map(s=>{const p=per[s.id]||{ok:0,t:0};const r=p.t?p.ok/p.t:0;return `<div class="bar" style="--c:${s.c}"><span class="nm">${s.n}</span><span class="track"><span class="fill" style="width:${r*100}%;display:block"></span></span><span class="v">${p.ok}/${p.t}</span></div>`}).join("")}</div>
    <div class="qbar"><button class="btn primary" data-exam="start">New mock exam</button></div></div>`}
  const fin=`<button class="btn primary" data-exam="finish">Finish and see answers</button>`;
  m.innerHTML=`<div class="sec-head"><div class="eyebrow">Exam practice</div><h2>Mock Exam</h2></div>${head}
    ${exam.done?"":`<div class="qbar"><span class="score">${n} / ${N_EXAM} answered</span><span class="timer" id="timer"></span>${fin}</div>`}
    <div class="qlist">${exam.qs.map((x,k)=>{const s=S.find(z=>z.id===x.s);return qCard(s.qs[x.i],k,String(k+1).padStart(2,"0"),exam.ans[k],exam.done,`data-ex="1"`,exam.done?s.n:"")}).join("")}</div>
    ${exam.done?"":`<div class="qbar" style="margin-top:16px">${fin}</div>`}`;showTime();
}
document.addEventListener("input",e=>{if(e.target.id==="tsearch"){tq=e.target.value;$("#tlist").innerHTML=termList()}});
document.addEventListener("click",e=>{
  const g=e.target.closest("[data-go]");if(g){if(g.dataset.go!==cur)mode="terms";go(g.dataset.go);return}
  const md=e.target.closest("[data-mode]");if(md){mode=md.dataset.mode;render();$("#main").scrollIntoView({block:"start"});return}
  const r=e.target.closest("[data-reset]");if(r){delete st[r.dataset.reset];save();render();return}
  const w=e.target.closest("[data-wrong]");if(w){const s=S.find(x=>x.id===w.dataset.wrong),a=st[s.id]||{};s.qs.forEach((q,i)=>{if(a[i]!==undefined&&a[i]!==q[2])delete a[i]});save();render();return}
  const ex=e.target.closest("[data-exam]");if(ex){if(ex.dataset.exam==="start"){buildExam();render()}else{exam.done=true;exam.used=(Date.now()-exam.t0)/1000;stopTick();render()}$("#main").scrollIntoView({block:"start"});return}
  const o=e.target.closest("[data-o]");if(!o||o.disabled)return;
  const qi=+o.parentElement.dataset.q,oi=+o.dataset.o;
  if(o.dataset.sec){const id=o.dataset.sec;st[id]=st[id]||{};st[id][qi]=oi;save();
    const s=S.find(x=>x.id===id);const card=o.closest(".q");const tmp=document.createElement("div");
    tmp.innerHTML=qCard(s.qs[qi],qi,String(qi+1).padStart(2,"0"),oi,true,`data-sec="${id}"`);card.replaceWith(tmp.firstElementChild);
    const sc=document.querySelector(".score");if(sc)sc.textContent=scoreText(sectionStats(s));renderTabs();return}
  if(o.dataset.ex&&!exam.done){exam.ans[qi]=oi;o.parentElement.querySelectorAll("button").forEach(b=>b.classList.toggle("sel",b===o));
    document.querySelectorAll(".score").forEach(el=>el.textContent=`${Object.keys(exam.ans).length} / ${N_EXAM} answered`)}
});
renderWeights();
const h=(location.hash||"").slice(1);cur=(S.some(s=>s.id===h)||h==="terms"||h==="mock")?h:S[0].id;render();
</script>
<script data-goatcounter="https://ibrahimethemafacan.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body></html>
"""

veri = [dict(id=s["id"], n=s["n"], k=s["k"], w=s["w"], c=s["c"], terms=s["terms"], notes=s["notes"], qs=s["qs"]) for s in S]
html = HEAD + "const S = " + json.dumps(veri, ensure_ascii=False).replace("</", "<\\/") + ";\n" + ENGINE.replace("__ETIKET__", KONU.get("etiket", "Reading")).replace("__NEXAM__", str(N_EXAM)).replace("__NTERM__", str(N_TERM)).replace("__KEY__", ANAHTAR).replace("__NREAD__", KONU["sayi"].lower() + " " + KONU.get("birim", "readings"))
hedef = KOK / f"calisma-masasi/cfa-level-1/{KONU['slug']}/index.html"
hedef.parent.mkdir(parents=True, exist_ok=True)
hedef.write_text(html, encoding="utf-8")
print("yazıldı:", hedef.relative_to(KOK), f"{len(html)//1024} KB")
