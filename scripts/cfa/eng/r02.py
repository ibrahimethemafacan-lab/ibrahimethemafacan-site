# CFA Level I · English for the Exam, üniteler 9–12. Özgün içerik.
R = []

# ---------------------------------------------------------------- 9
R.append(dict(id="u9", n="Uzun cümleyi çözmek", k="LONG SENTENCES", w=3, c="#0F766E",
terms=[
 ["noun phrase", "isim öbeği", "a 10-year, 5% semiannual-pay, option-free corporate bond", "İngilizcede asıl isim en sondadır; önündeki her şey onu niteler. Burada asıl isim “bond”dur."],
 ["passive voice", "edilgen yapı", "The bonds were issued at a discount by the company.", "İşi yapan “by” ile sonda verilir ya da hiç verilmez. Etken hali: The company issued the bonds."],
 ["which / that clause", "ilgi cümleciği", "The fund, which was launched in 2019, charges a 2% fee.", "Virgüller arasındaki kısım ek bilgidir. Çıkarınca ana cümle kalır: The fund charges a 2% fee."],
 ["-ing phrase", "ulaç / sıfat-fiil öbeği", "An investor holding a callable bond is short a call option.", "“Holding a callable bond” yatırımcıyı niteler: geri çağrılabilir tahvil tutan yatırımcı."],
 ["of-chain", "“of” zinciri", "the present value of the expected future cash flows of the project", "Sondan başa doğru çevrilir: projenin beklenen gelecekteki nakit akışlarının bugünkü değeri."],
 ["compared with / relative to", "… ile karşılaştırıldığında; … e göre", "Relative to a straight bond, a callable bond offers a higher yield.", "Karşılaştırmanın hangi şeye göre yapıldığını söyler; cümlenin başında da sonunda da olabilir."],
 ["as a result of / due to", "… sonucunda; … nedeniyle", "Margins declined due to higher input costs.", "Nedeni gösterir. “Because of”, “owing to” ve “driven by” aynı işi görür."],
 ["the extent to which", "ne ölçüde", "Duration measures the extent to which a bond's price responds to yield changes.", "Bir şeyin derecesini anlatır: fiyatın getiri değişimine ne ölçüde tepki verdiği."],
 ["whether", "… olup olmadığı", "The analyst must decide whether the information is material.", "İki olasılık arasında karar: bilginin önemli olup olmadığı."],
 ["such as / including", "örneğin; … gibi; … dahil", "Costs of carry, such as storage and insurance, raise the forward price.", "Örnek verir; liste tam değildir. “i.e.” ise “yani” demektir ve tam tanım verir; “e.g.” örnektir."],
],
notes="""<h3>Asıl ismi bulun</h3>
<ul>
<li>İngilizcede niteleyenler ismin önüne dizilir ve asıl isim <b>en sonda</b> durur.</li>
</ul>
<p class="f">a 10-year, 5% semiannual-pay, option-free corporate <b>bond</b><br>→ 10 yıl vadeli, %5 kuponlu, altı ayda bir ödemeli, opsiyonsuz şirket <b>tahvili</b></p>
<p class="f">the company's weighted average after-tax <b>cost</b> of capital<br>→ şirketin ağırlıklı ortalama vergi sonrası sermaye <b>maliyeti</b></p>
<h3>Cümleyi üç adımda sadeleştirin</h3>
<ul>
<li><b>1.</b> Virgüller arasındaki ek bilgiyi ve parantezleri geçici olarak atın.</li>
<li><b>2.</b> Özneyi ve ana fiili bulun.</li>
<li><b>3.</b> Rakamları ve koşulları (if, unless, assuming) geri ekleyin.</li>
</ul>
<p class="f">An analyst, who covers the retail sector for a mid-sized broker, notes that a company that recently changed its inventory method from LIFO to FIFO reported higher gross margins.<br><br>Özü: A company changed from LIFO to FIFO and reported higher gross margins.</p>
<div class="trap"><b>Sınav tuzağı</b>Uzun gövdede gereksiz bilgi bilerek verilir. Rakamların hepsini kullanmak zorunda değilsiniz; önce sorunun istediğini okuyun, sonra yalnızca gereken veriyi alın.</div>
<h3>Edilgen cümle</h3>
<div class="tbl"><table>
<tr><th>Edilgen</th><th>Etken</th></tr>
<tr><td>Revenue is recognized when control is transferred.</td><td>The company recognizes revenue when it transfers control.</td></tr>
<tr><td>The loss was offset by a gain on the hedge.</td><td>A gain on the hedge offset the loss.</td></tr>
<tr><td>The client was not informed of the conflict.</td><td>The manager did not inform the client of the conflict.</td></tr>
</table></div>
<p>Edilgen cümlede işi kimin yaptığı gizlenebilir. Ethics sorularında “kim yaptı, kim yapmalıydı” sorusunu kendiniz sorun.</p>""",
qs=[
 ["“a three-year, 4% annual-pay, callable corporate bond” ifadesinde asıl isim hangisidir?", ["bond", "corporate", "callable"], 0, "İngilizce isim öbeğinde asıl isim en sondadır: bond. Önündeki kelimelerin hepsi tahvili niteler."],
 ["“The portfolio, which had been fully hedged until March, lost 8% in April.” The main statement of the sentence is that the portfolio:", ["was fully hedged in April", "was launched in March", "lost 8% in April"], 2, "Virgüller arasındaki kısım ek bilgidir. Ana cümle: The portfolio lost 8% in April. Korunma mart ayına kadar geçerliydi."],
 ["“The loss on the bond position was more than offset by the gain on the futures.” The combined result was:", ["a net gain", "a net loss", "exactly zero"], 0, "Edilgen yapı: tahvil zararı futures kazancıyla fazlasıyla dengelendi. “More than offset” kazancın zarardan büyük olduğunu söyler; net sonuç kazançtır."],
 ["“An investor holding a putable bond is long a put option.” Who is long the put option?", ["The issuer of the bond", "The investor who holds the bond", "The dealer who sold the bond"], 1, "“Holding a putable bond” yatırımcıyı niteler. Geri satılabilir tahvili elinde tutan yatırımcı put opsiyonunda uzun pozisyondadır."],
 ["“the present value of the lease payments of the lessee” ifadesinin doğru Türkçesi hangisidir?", ["kiracının bugünkü kira ödemelerinin değeri", "kiracının kira ödemelerinin bugünkü değeri", "bugünkü değerin kira ödemelerinin kiracısı"], 1, "“Of” zinciri sondan başa çevrilir: kiracının → kira ödemelerinin → bugünkü değeri."],
 ["“Relative to FIFO, LIFO results in lower reported income when prices are rising.” Which method gives the higher reported income when prices rise?", ["LIFO", "FIFO", "Both give the same income"], 1, "“Relative to FIFO”: FIFO'ya göre. LIFO daha düşük kâr veriyorsa yüksek kârı veren FIFO'dur."],
 ["“Benefits of carry, e.g. dividends, lower the forward price.” The abbreviation “e.g.” tells us that dividends are:", ["the only benefit of carry", "one example of a benefit of carry", "not a benefit of carry"], 1, "“e.g.” örneğin demektir; liste tam değildir. Tam tanım veren kısaltma “i.e.”dir (yani)."],
 ["“The supervisor must determine whether the employee's outside activity was disclosed.” The supervisor must find out:", ["why the activity was disclosed", "when the activity will be disclosed", "if the activity was disclosed or not"], 2, "“Whether”: … olup olmadığı. Yönetici, faaliyetin açıklanıp açıklanmadığını belirlemelidir."],
]))

# ---------------------------------------------------------------- 10
R.append(dict(id="u10", n="Formüllerin ve sayıların dili", k="MATH IN WORDS", w=3, c="#C2410C",
terms=[
 ["divided by", "bölü", "Return on equity is net income divided by average equity.", "“A divided by B” = A / B. “Over” da aynı anlamdadır: net income over equity."],
 ["multiplied by / times", "çarpı", "Money duration is modified duration times the full price.", "“Times” ayrıca kat anlamına gelir: “interest coverage of 4 times” (4×)."],
 ["the product of / the sum of", "… in çarpımı / … in toplamı", "ROE is the product of margin, turnover and leverage.", "“Product” burada ürün değil, çarpım demektir. “The difference between A and B” = A − B."],
 ["to the power of / squared", "üssü / karesi", "The future value is 100 times 1.05 to the power of 10.", "“Squared” karesi, “cubed” küpü, “square root of” karekökü."],
 ["percent / percentage point", "yüzde / yüzde puan", "The rate rose from 4% to 5%: one percentage point, or 25 percent.", "Yüzde puan iki oranın farkıdır; yüzde ise oransal değişimdir."],
 ["weighted average", "ağırlıklı ortalama", "Portfolio duration is the weighted average of the bonds' durations.", "Her değer kendi ağırlığıyla çarpılıp toplanır. “Simple average” ağırlıksız ortalamadır."],
 ["compound / discount", "bileşik faizle büyütmek / iskonto etmek", "Cash flows are discounted at the required rate of return.", "“Compound” bugünden geleceğe, “discount” gelecekten bugüne götürür."],
 ["per", "başına", "Earnings per share is 2.50. The fee is 2% per annum.", "“Per share” pay başına, “per annum” yıllık, “per period” dönem başına."],
 ["inversely / directly related", "ters / doğru orantılı", "Bond prices are inversely related to yields.", "“Inversely”: biri artınca diğeri azalır. “Positively related” aynı yönde, “negatively related” zıt yönde."],
 ["approximately / roughly", "yaklaşık olarak", "The price change is approximately −3.4%.", "Yaklaşık sonuç. “≈” işaretinin sözle söylenişidir; “closest to” köküyle birlikte kullanılır."],
 ["rounded to", "… e yuvarlanmış", "The result is 12.47, rounded to two decimal places.", "“Decimal places” ondalık basamak. “To the nearest whole number”: en yakın tam sayıya."],
 ["annualized", "yıllıklandırılmış", "A monthly return of 1% is an annualized return of about 12.7%.", "Daha kısa bir dönemin getirisinin yıllık karşılığı. “Semiannual” altı aylık, “quarterly” üç aylık."],
],
notes="""<h3>Dört işlem ve ötesi</h3>
<div class="tbl"><table>
<tr><th>İşlem</th><th>İngilizce</th><th>Örnek</th></tr>
<tr><td>+</td><td>plus, the sum of, added to</td><td>the risk-free rate plus a risk premium</td></tr>
<tr><td>−</td><td>minus, less, net of, the difference between</td><td>revenue less cost of goods sold</td></tr>
<tr><td>×</td><td>times, multiplied by, the product of</td><td>beta times the market risk premium</td></tr>
<tr><td>÷</td><td>divided by, over, per, the ratio of … to …</td><td>debt divided by equity</td></tr>
<tr><td>x²</td><td>squared, to the power of 2</td><td>the standard deviation squared</td></tr>
<tr><td>√</td><td>the square root of</td><td>the square root of the variance</td></tr>
</table></div>
<p>“Less” çıkarma anlamındadır: “price less accrued interest” fiyattan birikmiş faizin düşülmesidir.</p>
<h3>Bir formülü cümleden kurmak</h3>
<p class="f">“The required return equals the risk-free rate plus beta times the market risk premium.”<br>→ r = R<sub>f</sub> + β × (R<sub>m</sub> − R<sub>f</sub>)</p>
<p class="f">“Modified duration is Macaulay duration divided by one plus the yield per period.”<br>→ ModDur = MacDur / (1 + r)</p>
<div class="trap"><b>Sınav tuzağı</b>“The ratio of A to B” her zaman A / B'dir. “Debt-to-equity” borç bölü özkaynak, “price-to-earnings” fiyat bölü kârdır. Sırayı ters çevirmek tam tersi sonucu verir.</div>
<h3>Yüzde mi, yüzde puan mı?</h3>
<ul>
<li>Marj %10'dan %12'ye çıkarsa: <b>2 percentage points</b> artmıştır; oransal olarak <b>20 percent</b>.</li>
<li>100 <b>basis points</b> = 1 percentage point.</li>
<li>“Doubled” iki katına çıktı (+%100), “halved” yarıya indi (−%50), “tripled” üç katına çıktı (+%200).</li>
</ul>
<h3>İlişki bildiren ifadeler</h3>
<ul>
<li><b>inversely related / negatively related</b>: ters yönlü</li>
<li><b>directly related / positively related</b>: aynı yönlü</li>
<li><b>proportional to</b>: … ile orantılı. <b>A function of</b>: … e bağlı.</li>
<li><b>the higher the coupon, the lower the duration</b>: kupon ne kadar yüksekse durasyon o kadar düşük.</li>
</ul>""",
qs=[
 ["“The current ratio is current assets divided by current liabilities.” Current assets are 500 and current liabilities are 250. The current ratio is:", ["0.5", "2.0", "250.0"], 1, "“A divided by B” = A / B: 500 / 250 = 2,0. 0,5 şıkkı bölmenin ters yapılmış halidir."],
 ["A company's operating margin rises from 10% to 12%. The margin has increased by:", ["2 percent", "2 percentage points", "12 percentage points"], 1, "İki oranın farkı yüzde puandır: 12 − 10 = 2 yüzde puan. Oransal artış ise %20'dir."],
 ["“ROE is the product of net profit margin, asset turnover and financial leverage.” With values of 6%, 1.25 and 2.0, ROE is closest to:", ["9.25%", "15.00%", "16.25%"], 1, "“The product of” çarpımı demektir: 0,06 × 1,25 × 2,0 = %15. 9,25 şıkkı üçünün toplamından gelir."],
 ["“Gross profit is revenue less cost of goods sold.” Revenue is 800 and cost of goods sold is 500. Gross profit is:", ["300", "500", "1,300"], 0, "“Less” çıkarma demektir: 800 − 500 = 300."],
 ["“Bond prices are inversely related to market yields.” If yields fall, bond prices:", ["fall", "rise", "do not change"], 1, "“Inversely related”: ters yönlü. Getiri düşerse fiyat yükselir."],
 ["“The debt-to-equity ratio is 0.5.” Equity is 400. Debt is:", ["200", "400", "800"], 0, "“Debt-to-equity” borç bölü özkaynaktır: borç / 400 = 0,5, borç 200. 800 şıkkı oranı ters okumaktan gelir."],
 ["“The higher the coupon rate, the lower the duration.” Which bond has the highest duration, all else equal?", ["The bond with an 8% coupon", "The bond with a 5% coupon", "The bond with a 2% coupon"], 2, "“The higher …, the lower …”: kupon ne kadar yüksekse durasyon o kadar düşük. En yüksek durasyon en düşük kuponlu tahvildedir."],
 ["“Variance is the standard deviation squared.” The standard deviation is 20%. The variance, in decimals, is:", ["0.04", "0.20", "0.40"], 0, "“Squared” karesi demektir: 0,20² = 0,04."],
]))

# ---------------------------------------------------------------- 11
R.append(dict(id="u11", n="Kesinlik derecesi: always, generally, may", k="DEGREES OF CERTAINTY", w=3, c="#B45309",
terms=[
 ["always / never", "her zaman / asla", "A zero-coupon bond's Macaulay duration always equals its maturity.", "Mutlak ifadeler. Finansta çok az şey mutlak olduğu için şıkta görünce iki kez düşünün."],
 ["generally / typically / usually", "genellikle", "High-yield bonds typically have more restrictive covenants.", "Kural çoğu durumda geçerli, istisnası var. Sınavın en sevdiği güvenli ifadelerdir."],
 ["tend to", "eğilimindedir", "Small-cap stocks tend to be less liquid.", "Genel bir eğilimi anlatır; her durumda doğru olduğunu söylemez."],
 ["may / might / can", "olabilir; yapabilir", "A callable bond may exhibit negative convexity.", "Olasılık bildirir. Kural cümlelerinde “may” izin anlamına da gelir."],
 ["must / necessarily", "zorunlu; mutlaka", "A higher Sharpe ratio does not necessarily imply a higher return.", "“Not necessarily”: şart değil. “Must be” ise mantıksal zorunluluk bildirir."],
 ["on average", "ortalama olarak", "On average, active managers underperform after fees.", "Tek tek her örnek için değil, genel ortalama için doğru."],
 ["in most cases / in some cases", "çoğu durumda / bazı durumlarda", "In most cases, the two rules give the same decision.", "Kapsamı sınırlar. “In all cases” mutlak ifadedir."],
 ["primarily / mainly", "öncelikle; esas olarak", "An FRN's price changes primarily because of credit risk.", "Ana nedeni gösterir; başka nedenlerin de olabileceğini kabul eder."],
 ["solely / only", "yalnızca", "A revenue bond is repaid solely from the project's cash flows.", "Sınırlayıcı ifadeler. “Only” yanlış yere konunca şıkkı yanlış yapar."],
 ["to some extent / partially", "bir ölçüde; kısmen", "The currency loss was partially hedged.", "Tam değil, kısmi. “Fully” ve “entirely” tamamen demektir."],
],
notes="""<h3>Kesinlik merdiveni</h3>
<div class="tbl"><table>
<tr><th>Derece</th><th>İfadeler</th></tr>
<tr><td>Mutlak</td><td>always, never, all, none, must, only, solely, in all cases, guarantees</td></tr>
<tr><td>Güçlü</td><td>most likely, generally, typically, usually, tends to, in most cases</td></tr>
<tr><td>Orta</td><td>often, likely, may, can, on average</td></tr>
<tr><td>Zayıf</td><td>might, could, sometimes, in some cases, occasionally</td></tr>
<tr><td>Olumsuz</td><td>unlikely, rarely, seldom, least likely</td></tr>
</table></div>
<h3>Mutlak ifadelere dikkat</h3>
<ul>
<li>İçinde <b>always</b>, <b>never</b>, <b>guarantees</b>, <b>eliminates</b> ya da <b>only</b> geçen şıklar çoğu zaman yanlıştır; çünkü tek bir istisna onları çürütür.</li>
<li>Bu bir kural değil, eğilimdir. Bazı ifadeler gerçekten mutlaktır: “Convexity adjustment is always positive for an option-free bond.”</li>
<li>Çeşitlendirme riski <b>reduces</b> (azaltır); <b>eliminates</b> (yok eder) denirse şık yanlıştır, çünkü sistematik risk kalır.</li>
</ul>
<div class="trap"><b>Sınav tuzağı</b>“Only” kelimesinin yeri anlamı değiştirir. “Only systematic risk is priced” doğrudur. “Systematic risk is priced only in bear markets” yanlıştır. Kelimenin neyi sınırladığına bakın.</div>
<h3>Ethics'te kesinlik</h3>
<ul>
<li><b>guarantee</b>: garanti etmek. Getiri garantisi vermek yanlış beyandır; yalnızca yapısı gereği garantili ürünlerde kullanılabilir.</li>
<li><b>ensure / assure</b>: sağlamak; güvence vermek. “Make reasonable efforts to ensure” makul çaba göstermek demektir, sonucu garanti etmek değil.</li>
<li><b>reasonable</b>: makul. Standartlar kusursuzluk değil, makul özen ister.</li>
</ul>""",
qs=[
 ["Which statement is most accurate?", ["Diversification always eliminates risk", "Diversification never reduces risk", "Diversification generally reduces unsystematic risk"], 2, "“Always eliminates” ve “never reduces” mutlak ifadelerdir ve yanlıştır. Çeşitlendirme sistematik olmayan riski genellikle azaltır; sistematik risk kalır."],
 ["“A higher P/E does not necessarily mean the stock is overvalued.” The sentence says that a stock with a high P/E:", ["is definitely overvalued", "may or may not be overvalued", "is definitely undervalued"], 1, "“Not necessarily”: şart değil, ille de öyle değil. Yüksek F/K aşırı değerli olabilir de olmayabilir de."],
 ["“High-yield issuers typically face more restrictive covenants.” The word “typically” tells us that this is:", ["true in most cases, with exceptions", "true in every case", "rarely true"], 0, "“Typically” genellikle demektir: çoğu durumda doğru, ama istisnası olabilir."],
 ["“A revenue bond is repaid solely from the cash flows of the project.” If the project's cash flows are insufficient, bondholders can claim:", ["the issuer's general tax revenue", "nothing beyond the project's cash flows", "the assets of other projects"], 1, "“Solely”: yalnızca. Geri ödeme sadece projenin nakit akışından yapılır; tahvil sahiplerinin başka kaynağa başvurma hakkı yoktur."],
 ["“The manager told clients that the fund guarantees a return of 8%.” The fund invests in equities. The statement is:", ["acceptable, because 8% is realistic", "acceptable, if past returns were 8%", "a misrepresentation"], 2, "“Guarantee” garanti etmek demektir. Hisse senedi fonunun getirisi garanti edilemez; bu ifade yanlış beyandır (I(C) Misrepresentation)."],
 ["“The exposure was partially hedged.” After hedging, the remaining risk is:", ["zero", "smaller than before but not zero", "larger than before"], 1, "“Partially”: kısmen. Riskin bir bölümü kapatılmış, bir bölümü kalmıştır."],
 ["“Small-cap stocks tend to be less liquid than large-cap stocks.” Which conclusion is justified?", ["Every small-cap stock is less liquid than every large-cap stock", "No small-cap stock is liquid", "As a group, small-cap stocks are usually less liquid"], 2, "“Tend to” genel eğilimi anlatır. Grup olarak küçük şirket hisseleri genellikle daha az likittir; tek tek her hisse için kesin bir şey söylenmez."],
 ["“An FRN's price changes primarily because of changes in credit risk.” According to the sentence, interest rate changes are:", ["the main cause of FRN price changes", "not the main cause of FRN price changes", "the only cause of FRN price changes"], 1, "“Primarily” ana nedeni gösterir: ana neden kredi riskidir. Faiz değişimi ana neden değildir, ama hiç etkisi olmadığı da söylenmemiştir."],
]))

# ---------------------------------------------------------------- 12
R.append(dict(id="u12", n="Piyasa jargonu: pozisyon ve fiyat", k="MARKET JARGON", w=3, c="#1D4ED8",
terms=[
 ["long / short", "uzun (alım) / kısa (açığa satış) pozisyon", "The fund is long the stock and short the index future.", "“Long” fiyat artınca kazanır, “short” fiyat düşünce kazanır. Uzunluk ya da süreyle ilgisi yoktur."],
 ["bid / ask (offer)", "alış / satış fiyatı", "The dealer quotes 99.50 bid and 99.70 ask.", "“Bid” dealerın aldığı, “ask” sattığı fiyattır. Yatırımcı ask'ten alır, bid'den satar. Aradaki fark “spread”dir."],
 ["in / at / out of the money", "kârda / başa baş / zararda (opsiyon)", "A call with a strike of 50 is in the money when the stock trades at 54.", "Call için S > X kârda; put için S < X kârda. “At the money”: S = X."],
 ["at par / above par / below par", "nominal değerde / üstünde / altında", "The bond was issued at par and now trades below par.", "“Par” nominal (itibari) değerdir. “Above par” primli, “below par” iskontolu."],
 ["bullish / bearish", "yükseliş / düşüş beklentili", "A bearish investor buys puts.", "“Bull market” yükselen, “bear market” düşen piyasa."],
 ["upside / downside", "yukarı yönlü potansiyel / aşağı yönlü risk", "A covered call limits the upside but keeps the downside.", "“Downside risk” zarar riskidir. “Upside potential” kazanç potansiyelidir."],
 ["exposure", "(riske) açık pozisyon; maruziyet", "The firm has a large exposure to the dollar.", "Bir risk etkeninden ne kadar etkilenildiği. “Reduce exposure”: riski azaltmak."],
 ["leverage", "kaldıraç; borçla büyütme", "Leverage magnifies both gains and losses.", "“Leveraged”: kaldıraçlı. İngiliz kullanımında “gearing” de denir."],
 ["underlying", "dayanak varlık", "The option's value depends on the price of the underlying.", "Türev aracın değerini belirleyen varlık: hisse, endeks, faiz, döviz, emtia."],
 ["counterparty", "karşı taraf", "OTC contracts expose each party to counterparty risk.", "Sözleşmenin diğer tarafı. “Counterparty risk” karşı tarafın yükümlülüğünü yerine getirmeme riskidir."],
 ["notional", "itibari (sözleşme) tutarı", "The swap has a notional principal of 10 million.", "Ödemelerin hesaplandığı tutar; çoğu swapta el değiştirmez."],
 ["benchmark", "karşılaştırma ölçütü", "The fund outperformed its benchmark by 120 basis points.", "“Outperform” ölçütü geçmek, “underperform” ölçütün gerisinde kalmak. “Track” izlemek demektir."],
],
notes="""<h3>Kim kazanır?</h3>
<div class="tbl"><table>
<tr><th>Pozisyon</th><th>Fiyat artarsa</th><th>Fiyat düşerse</th></tr>
<tr><td>Long stock, long futures, long forward</td><td>Kazanır</td><td>Kaybeder</td></tr>
<tr><td>Short stock, short futures, short forward</td><td>Kaybeder</td><td>Kazanır</td></tr>
<tr><td>Long call</td><td>Kazanır</td><td>En fazla primi kaybeder</td></tr>
<tr><td>Long put</td><td>En fazla primi kaybeder</td><td>Kazanır</td></tr>
<tr><td>Short call</td><td>Kaybeder (sınırsız)</td><td>Primi kazanır</td></tr>
<tr><td>Short put</td><td>Primi kazanır</td><td>Kaybeder</td></tr>
</table></div>
<ul>
<li>Opsiyonda <b>buyer = holder = long</b>; <b>seller = writer = short</b>.</li>
<li>“Short” satmış olmak demektir; “short-term” (kısa vadeli) ile karıştırmayın.</li>
</ul>
<h3>Fiyat ifadeleri</h3>
<ul>
<li><b>trades at</b>: … fiyatından işlem görüyor. <b>Is quoted at</b>: … olarak kote ediliyor. <b>Is priced at</b>: … olarak fiyatlanmış.</li>
<li><b>at a premium to / at a discount to</b>: … in üstünde / altında. “The fund trades at a 5% discount to net asset value.”</li>
<li><b>spread</b>: fark. Alış-satış farkı (bid–ask spread) ya da getiri farkı (credit spread) olabilir; bağlama bakın.</li>
<li><b>rally</b>: yükseliş. <b>Sell-off</b>: satış dalgası. <b>Flight to quality</b>: güvenli varlıklara kaçış.</li>
</ul>
<div class="trap"><b>Sınav tuzağı</b>Döviz kotasyonunda “the dollar strengthened” ile “USD/EUR rose” aynı şey olmayabilir. USD/EUR, bir euronun dolar cinsinden fiyatıdır; oranın yükselmesi euronun değer kazandığını, doların zayıfladığını gösterir.</div>
<h3>Performans dili</h3>
<ul>
<li><b>outperform / underperform</b>: daha iyi / daha kötü getiri sağlamak</li>
<li><b>excess return</b>: ölçütün ya da risksiz oranın üzerindeki getiri. <b>Alpha</b>: riske göre düzeltilmiş fazla getiri.</li>
<li><b>drawdown</b>: zirveden dibe düşüş. <b>Volatility</b>: oynaklık.</li>
<li><b>overweight / underweight</b>: ölçüte göre fazla / eksik ağırlık vermek.</li>
</ul>""",
qs=[
 ["“The investor is short 100 shares.” The investor profits if the share price:", ["rises", "falls", "stays the same"], 1, "“Short” açığa satış pozisyonudur; fiyat düşünce kazanır. Kısa vadeyle ilgisi yoktur."],
 ["A dealer quotes a bond at 99.50 bid and 99.70 ask. An investor who wants to buy pays:", ["99.50", "99.60", "99.70"], 2, "Yatırımcı ask (satış) fiyatından alır: 99,70. Bid, dealerın alış fiyatıdır; yatırımcı o fiyattan satar."],
 ["A put option has an exercise price of 40. The underlying trades at 46. The put is:", ["in the money", "at the money", "out of the money"], 2, "Put için kârda olma koşulu S < X'tir. 46, 40'tan büyük olduğundan put zarardadır (out of the money)."],
 ["“The fund outperformed its benchmark by 120 basis points.” The benchmark returned 6.0%. The fund returned:", ["4.8%", "6.0%", "7.2%"], 2, "“Outperform”: ölçütü geçmek. 120 baz puan = %1,2; fon %6,0 + %1,2 = %7,2 getiri sağlamıştır."],
 ["“The option writer received a premium of 3.” The writer is the party that:", ["bought the option", "sold the option", "guarantees the exchange"], 1, "“Writer” opsiyonu yazan, yani satan taraftır (short). Primi alır ve yükümlülük üstlenir."],
 ["“The closed-end fund trades at a 5% discount to net asset value.” Net asset value per share is 20. The market price is:", ["19", "20", "21"], 0, "“At a discount to”: … in altında. 20'nin %5 altı 19'dur."],
 ["“The swap has a notional principal of 10 million.” In a plain interest rate swap, the 10 million is:", ["paid by the fixed-rate payer at the start", "exchanged at the start and at the end", "used only to calculate the interest payments"], 2, "“Notional” itibari tutardır: faiz ödemeleri onun üzerinden hesaplanır, ama faiz swapında bu tutar el değiştirmez."],
 ["“A bearish investor with no position in the stock wants limited risk.” The most suitable trade is to:", ["buy a put", "buy a call", "sell a put"], 0, "“Bearish”: düşüş bekleyen. Put almak fiyat düşünce kazandırır ve zarar primle sınırlıdır. Put satmak yükseliş beklentisidir."],
]))
