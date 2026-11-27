"""Not güçlendirme yardımcıları (ek2.py dosyaları kullanır).
G(ex, cf, ask): her okumaya eklenen üç bölümün HTML'ini üretir.
  ex  : [(soru, hesap, yorum)]  hesap: satırlar '|' ile ayrılır (boş olabilir); yorum düz metin (boş olabilir)
  cf  : (başlıklar, satırlar)   "Often confused" tablosu
  ask : "How the exam asks it" paragrafı
Sayılar ek dosyalarında Python ile hesaplanır; elle yazılmaz."""

import re

def G(ex, cf, ask):
    h = "<h3>Worked example" + ("s" if len(ex) > 1 else "") + "</h3>"
    for q, calc, note in ex:
        h += f"<p><b>Question.</b> {q}</p>"
        if calc:
            calc = re.sub(r"(?<![\w.>])-(?=\d)", "−", calc)  # ASCII eksi yerine gerçek eksi işareti
            h += '<p class="f">' + "<br>".join(x.strip() for x in calc.split("|")) + "</p>"
        if note:
            h += f"<p><b>Answer.</b> {note}</p>"
    hdr, rows = cf
    h += "<h3>Often confused</h3><div class=\"tbl\"><table><tr>" + "".join(f"<th>{x}</th>" for x in hdr) + "</tr>"
    for r in rows:
        assert len(r) == len(hdr), r
        h += "<tr>" + "".join(f"<td>{x}</td>" for x in r) + "</tr>"
    h += "</table></div>"
    h += f"<h3>How the exam asks it</h3><p>{ask}</p>"
    return dict(notes=h)

def n(x, d=2):
    """Binlik ayraçlı sayı."""
    return f"{x:,.{d}f}"
