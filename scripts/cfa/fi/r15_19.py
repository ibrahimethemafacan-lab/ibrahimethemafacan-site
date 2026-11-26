# CFA Level I · Fixed Income · readings 15–19. Original study notes and questions.
R = []

R.append(dict(id="cg", n="Credit Analysis for Government Issuers", k="SOVEREIGN", w=1, c="#1f7a8c",
terms=[
 ["Sovereign credit risk", "Ülke (egemen) kredi riski", "The risk that a national government fails to pay its debt in full and on time.", "Merkezi hükümetin borcunu tam ve zamanında ödeyememesi riski."],
 ["Local currency rating", "Yerel para notu", "A rating of a sovereign's debt denominated in its own currency.", "Bir devletin kendi para birimi cinsinden borcunun notu."],
 ["Foreign currency rating", "Yabancı para notu", "A rating of a sovereign's debt denominated in other currencies; usually lower than the local currency rating.", "Bir devletin başka para birimleri cinsinden borcunun notu; genellikle yerel para notundan düşüktür."],
 ["Reserve currency", "Rezerv para", "A currency widely held by central banks as reserves, which eases the issuing country's borrowing.", "Merkez bankalarınca rezerv olarak yaygın tutulan ve ihraççı ülkenin borçlanmasını kolaylaştıran para."],
 ["Debt-to-GDP ratio", "Borç/GSYH oranı", "Government debt as a share of gross domestic product; a measure of fiscal burden.", "Kamu borcunun gayrisafi yurt içi hasılaya oranı; mali yükün ölçüsü."],
 ["Fiscal flexibility", "Mali esneklik", "A government's ability to raise revenue or cut spending to service its debt.", "Hükümetin borcunu ödemek için gelir artırma veya harcama kısma kabiliyeti."],
 ["Non-sovereign government", "Alt yönetim (yerel yönetim)", "A regional or local government, which cannot create money and so carries more credit risk than the sovereign.", "Para basamadığı için merkezi hükümetten daha fazla kredi riski taşıyan bölgesel veya yerel yönetim."],
],
notes="""<h3>What sovereign analysts look at</h3>
<div class="tbl"><table>
<tr><th>Area</th><th>Questions</th></tr>
<tr><td>Institutional</td><td>Rule of law, stable and effective policy-making, low corruption, history of honouring debts</td></tr>
<tr><td>Economic</td><td>Income per head, growth prospects, diversification of the economy</td></tr>
<tr><td>External</td><td>Status of the currency (reserve currency?), current account, foreign exchange reserves, external debt</td></tr>
<tr><td>Fiscal</td><td>Debt-to-GDP, interest burden relative to revenue, ability to raise taxes or cut spending</td></tr>
<tr><td>Monetary</td><td>Independence of the central bank, credibility, exchange rate regime</td></tr>
</table></div>
<ul>
<li>A freely floating currency and a credible, independent central bank give more room to absorb shocks. A fixed exchange rate removes monetary flexibility.</li>
</ul>
<h3>Local and foreign currency</h3>
<ul>
<li>A government can, in the last resort, create its own currency, so default on <b>local currency</b> debt is less likely. It must earn or borrow <b>foreign currency</b>, so foreign currency debt is riskier and is usually rated <b>lower</b>.</li>
</ul>
<h3>Non-sovereign government debt</h3>
<ul>
<li><b>General obligation bonds:</b> backed by the taxing power of a regional or local government. Analysis resembles sovereign analysis, but these issuers cannot create money and are often bound by balanced-budget rules.</li>
<li><b>Revenue bonds:</b> backed by a specific project. Analysis resembles corporate analysis, with focus on the <b>debt service coverage ratio</b> (project revenue / debt service).</li>
<li>Agencies and government-sponsored entities depend on the strength and reliability of state support.</li>
</ul>
<div class="trap"><b>Exam trap</b>Having a reserve currency is a major strength: it lets a country borrow in its own currency from the rest of the world.</div>""",
qs=[
 ["A sovereign's rating on its foreign-currency debt is most likely:", ["lower than its local-currency rating.", "higher than its local-currency rating.", "the same as its local-currency rating."], 0, "A government can create its own currency but not foreign currency, so foreign-currency debt carries more default risk."],
 ["Which of the following most likely strengthens a sovereign's credit quality?", ["A fixed exchange rate", "A high ratio of debt to GDP", "A currency used as an international reserve currency"], 2, "Reserve-currency status allows borrowing abroad in the country's own currency, reducing external risk."],
 ["In analysing a revenue bond issued by a city to fund a toll road, the most important ratio is likely the:", ["debt-to-GDP ratio.", "debt service coverage ratio.", "current account balance."], 1, "Repayment depends on the project's revenue relative to its debt service."],
 ["Compared with a national government, a regional government is most likely to have higher credit risk because it:", ["cannot create money.", "has no power to tax.", "always borrows in foreign currency."], 0, "Without the ability to create money, a regional government depends entirely on its revenues and transfers."],
 ["Which of the following is an institutional factor in sovereign credit analysis?", ["GDP per capita", "Foreign exchange reserves", "The effectiveness of policy-making"], 2, "Institutional factors cover governance, rule of law and policy effectiveness."],
 ["A high ratio of interest payments to government revenue most directly indicates weak:", ["fiscal flexibility.", "external status.", "monetary independence."], 0, "A large share of revenue going to interest leaves little room to respond to shocks."],
 ["A sovereign with a credible, independent central bank and a freely floating exchange rate most likely has:", ["less monetary flexibility.", "more monetary flexibility.", "no need for foreign exchange reserves."], 1, "It can adjust interest rates and allow the currency to absorb shocks."],
 ["General obligation bonds issued by a local government are backed by the:", ["revenue of a specific project.", "taxing power of the issuer.", "guarantee of the national government."], 1, "General obligation bonds are secured by the issuer's broad ability to raise taxes."],
]))

R.append(dict(id="cc", n="Credit Analysis for Corporate Issuers", k="CORPORATE CREDIT", w=2, c="#3b7dd8",
terms=[
 ["Leverage ratio", "Kaldıraç oranı", "A measure of debt relative to earnings or capital, such as debt/EBITDA.", "Borcun kâra veya sermayeye göre ölçüsü; örneğin borç/FAVÖK."],
 ["Coverage ratio", "Karşılama oranı", "A measure of earnings relative to interest, such as EBITDA/interest.", "Kârın faize göre ölçüsü; örneğin FAVÖK/faiz."],
 ["Funds from operations (FFO)", "Faaliyetlerden sağlanan fonlar", "Net income plus depreciation, amortization and other non-cash items.", "Net kâr artı amortisman ve diğer nakit dışı kalemler."],
 ["Seniority ranking", "Alacak sıralaması", "The order in which creditors are paid in bankruptcy.", "İflasta alacaklılara ödeme yapılma sırası."],
 ["First lien", "Birinci derece rehin", "A secured claim with first priority on specific assets.", "Belirli varlıklar üzerinde ilk sırada önceliği olan teminatlı alacak."],
 ["Subordinated debt", "Sermaye benzeri (ikincil) borç", "Debt that ranks behind senior debt in a liquidation.", "Tasfiyede kıdemli borcun arkasında sıralanan borç."],
 ["Pari passu", "Eşit sırada", "Ranking equally with other claims of the same class.", "Aynı sınıftaki diğer alacaklarla eşit sırada yer alma."],
 ["Structural subordination", "Yapısal ikincillik", "The weaker position of a holding company's creditors relative to creditors of its operating subsidiaries.", "Holding şirketi alacaklılarının, faaliyet gösteren bağlı ortaklıkların alacaklılarına göre zayıf konumu."],
 ["Absolute priority rule", "Mutlak öncelik kuralı", "The principle that senior claims are paid in full before junior claims receive anything.", "Kıdemli alacaklar tamamen ödenmeden alt sıradakilerin hiçbir şey alamaması ilkesi."],
],
notes="""<h3>What to analyse</h3>
<ul>
<li><b>Capacity:</b> the industry's structure and cyclicality, the company's competitive position, track record, management and strategy.</li>
<li><b>Capital:</b> leverage, liquidity and access to funding.</li>
<li><b>Collateral:</b> quality and value of assets that secure the debt.</li>
<li><b>Covenants:</b> protections in the bond and loan agreements.</li>
</ul>
<h3>Key ratios</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>Ratio</th><th>Better when</th></tr>
<tr><td>Profitability and cash flow</td><td>EBITDA, FFO, free cash flow</td><td>Higher and stable</td></tr>
<tr><td>Leverage</td><td>Debt / EBITDA, debt / capital, FFO / debt</td><td>Debt ratios lower; FFO/debt higher</td></tr>
<tr><td>Coverage</td><td>EBITDA / interest, EBIT / interest</td><td>Higher</td></tr>
</table></div>
<ul>
<li>Adjust reported debt for leases, pension deficits and other debt-like obligations.</li>
<li>Look at the trend and at peers, and consider the business cycle: margins of cyclical companies collapse in recessions.</li>
</ul>
<h3>Seniority and recovery</h3>
<p class="f">first lien &gt; second lien &gt; senior unsecured &gt; senior subordinated &gt; subordinated &gt; junior subordinated</p>
<ul>
<li>Higher ranking means higher expected recovery and a lower spread. Claims of the same class rank <b>pari passu</b>.</li>
<li>In practice negotiated settlements sometimes give junior creditors something before seniors are paid in full, despite the <b>absolute priority rule</b>.</li>
<li><b>Structural subordination:</b> a holding company's creditors are paid from dividends of its subsidiaries only after the subsidiaries' own creditors.</li>
</ul>
<h3>High-yield and investment-grade analysis</h3>
<ul>
<li>For high-yield issuers, focus more on liquidity, refinancing needs, the debt structure, covenants and recovery values; consider an equity-like view of the company.</li>
<li>Companies with strong free cash flow, low leverage and good access to markets merit the tightest spreads.</li>
</ul>
<div class="trap"><b>Exam trap</b>For FFO/debt, higher is better; for debt/EBITDA, lower is better. Check the direction before comparing companies.</div>""",
qs=[
 ["A company has total debt of 400 and EBITDA of 100. Its debt-to-EBITDA ratio is:", ["0.25", "4.00", "5.00"], 1, "400 / 100 = 4.0 times."],
 ["A company has EBITDA of 100 and interest expense of 20. Its EBITDA-to-interest coverage is:", ["0.20", "4.00", "5.00"], 2, "100 / 20 = 5.0 times."],
 ["Which of the following claims ranks highest in a liquidation?", ["Senior unsecured debt", "Subordinated debt", "First lien debt"], 2, "Debt secured by a first lien on assets has the highest priority."],
 ["Creditors of a holding company are paid from its subsidiaries' cash flows only after the subsidiaries' own creditors. This is known as:", ["notching.", "pari passu ranking.", "structural subordination."], 2, "Structural subordination arises from the corporate structure, not from the terms of the debt."],
 ["Two bonds of the same issuer with the same seniority rank:", ["senior to each other.", "pari passu.", "according to their issue dates."], 1, "Claims of the same class share equally in any recovery."],
 ["For a credit analyst, which change most likely indicates improving credit quality?", ["A higher debt-to-capital ratio", "A lower EBITDA-to-interest ratio", "A higher FFO-to-debt ratio"], 2, "More funds from operations relative to debt means greater capacity to repay."],
 ["Compared with analysis of investment-grade issuers, analysis of high-yield issuers places more emphasis on:", ["liquidity and refinancing needs.", "the issuer's dividend policy.", "short-term changes in the credit rating."], 0, "High-yield issuers are more vulnerable to running out of cash, so liquidity and the debt structure are central."],
 ["The principle that senior creditors must be paid in full before junior creditors receive anything is the:", ["negative pledge.", "absolute priority rule.", "cross-default clause."], 1, "The absolute priority rule sets the order of payment in bankruptcy, although it is not always followed in practice."],
]))

R.append(dict(id="sc", n="Fixed-Income Securitization", k="SECURITIZATION", w=1, c="#2e9e8f",
terms=[
 ["Securitization", "Menkul kıymetleştirme", "Pooling loans or receivables and issuing securities backed by their cash flows.", "Kredileri veya alacakları bir havuzda toplayıp bunların nakit akışlarına dayalı menkul kıymet ihraç etme."],
 ["Originator", "Kaynak kuruluş", "The lender that makes the loans and sells them into the securitization.", "Kredileri veren ve onları menkul kıymetleştirmeye satan kuruluş."],
 ["Special purpose entity (SPE)", "Özel amaçlı kuruluş", "A legally separate entity that buys the assets and issues the securities, shielding investors from the originator's bankruptcy.", "Varlıkları satın alan ve menkul kıymetleri ihraç eden, yatırımcıları kaynak kuruluşun iflasından koruyan ayrı tüzel kişilik."],
 ["Servicer", "Hizmet sağlayıcı", "The party that collects payments from borrowers and manages the loans.", "Borçlulardan ödemeleri tahsil eden ve kredileri yöneten taraf."],
 ["Tranche", "Dilim", "One of several classes of securities in a securitization with different priority or timing of payments.", "Menkul kıymetleştirmede farklı ödeme önceliği veya zamanlamasına sahip sınıflardan biri."],
 ["Credit tranching", "Kredi riskine göre dilimleme", "A structure in which junior tranches absorb losses before senior ones.", "Alt dilimlerin kayıpları üst dilimlerden önce üstlendiği yapı."],
 ["Waterfall", "Ödeme şelalesi", "The rules that set the order in which cash flows are paid to the tranches.", "Nakit akışlarının dilimlere hangi sırayla ödeneceğini belirleyen kurallar."],
 ["Covered bond", "Teminatlı (ipotekli) tahvil", "A bond issued by a bank and backed by a pool of assets that stays on its balance sheet, with recourse to both the pool and the bank.", "Bir bankanın ihraç ettiği, bilançosunda kalan varlık havuzuyla desteklenen ve hem havuza hem bankaya rücu imkânı veren tahvil."],
],
notes="""<h3>Why securitize</h3>
<ul>
<li>For originators: frees capital, funds new lending, can lower funding costs, and moves risk off the balance sheet.</li>
<li>For investors: access to asset pools they could not otherwise buy, with a choice of risk and timing through tranches.</li>
<li>For the economy: more lending and more efficient capital markets. The risks are poor underwriting standards and complexity, as seen in 2007–2008.</li>
</ul>
<h3>Parties</h3>
<div class="tbl"><table>
<tr><th>Party</th><th>Role</th></tr>
<tr><td>Originator / seller</td><td>Makes the loans, sells them to the SPE</td></tr>
<tr><td>Special purpose entity</td><td>Buys the assets, issues the securities; bankruptcy-remote from the seller</td></tr>
<tr><td>Servicer</td><td>Collects payments, deals with delinquencies</td></tr>
<tr><td>Trustee</td><td>Protects investors' interests</td></tr>
</table></div>
<ul>
<li>Because the assets are sold to a separate SPE, investors are exposed to the pool, not to the originator's credit.</li>
</ul>
<h3>Structures</h3>
<ul>
<li><b>Credit tranching:</b> losses hit the equity or residual tranche first, then subordinated tranches, then senior. Subordination is internal credit enhancement.</li>
<li><b>Time tranching:</b> tranches receive principal in sequence, redistributing prepayment risk.</li>
<li>The <b>waterfall</b> sets payment priority: senior tranches first.</li>
</ul>
<h3>Covered bonds</h3>
<ul>
<li>Issued by banks; the cover pool stays on the bank's balance sheet. Investors have <b>dual recourse</b>: to the bank and to the pool.</li>
<li>The pool is <b>dynamic</b>: non-performing assets must be replaced. These features make covered bonds lower-risk and lower-yielding than comparable asset-backed securities.</li>
</ul>
<div class="trap"><b>Exam trap</b>A covered bond stays on the issuer's balance sheet and gives dual recourse; an asset-backed security is issued by a separate SPE and investors have recourse only to the pool.</div>""",
qs=[
 ["The main reason a securitization uses a special purpose entity is to:", ["increase the originator's leverage.", "protect investors from the originator's bankruptcy.", "avoid the need for a servicer."], 1, "The SPE owns the assets separately, so the originator's creditors cannot claim them."],
 ["The party that collects loan payments from borrowers in a securitization is the:", ["trustee.", "servicer.", "originator."], 1, "The servicer manages collections and delinquencies; it is often the originator but performs a separate role."],
 ["In a structure with credit tranching, the first losses on the underlying pool are absorbed by the:", ["senior tranche.", "mezzanine tranche.", "subordinated or equity tranche."], 2, "Junior tranches protect the senior ones by taking losses first."],
 ["Compared with an asset-backed security, a covered bond most likely offers investors:", ["recourse only to the collateral pool.", "recourse to both the issuing bank and the collateral pool.", "no recourse to the collateral pool."], 1, "Covered bonds give dual recourse, which lowers their risk."],
 ["In a covered bond programme, a loan in the cover pool that stops performing is most likely:", ["left in the pool.", "replaced with a performing asset.", "transferred to the bondholders."], 1, "Cover pools are dynamic and must be kept at the required quality."],
 ["Time tranching in a securitization is designed mainly to redistribute:", ["credit risk.", "currency risk.", "prepayment risk."], 2, "Tranches that receive principal at different times face different exposure to early repayment."],
 ["Which of the following is a benefit of securitization for the originating bank?", ["It increases the bank's credit risk.", "It frees capital to make new loans.", "It eliminates the need for borrowers to repay."], 1, "Selling loans converts them to cash and reduces the capital the bank must hold."],
 ["The set of rules that determines the order in which a securitization's cash flows are paid to tranches is the:", ["waterfall.", "cover pool.", "indenture covenant."], 0, "The waterfall specifies payment priority among tranches."],
]))

R.append(dict(id="ab", n="Asset-Backed Security (ABS) Instrument and Market Features", k="ABS", w=1, c="#c0563f",
terms=[
 ["Asset-backed security (ABS)", "Varlığa dayalı menkul kıymet", "A security backed by a pool of non-mortgage assets such as auto loans or credit card receivables.", "Taşıt kredileri veya kredi kartı alacakları gibi ipotek dışı varlık havuzuna dayalı menkul kıymet."],
 ["Amortizing ABS", "İtfalı varlığa dayalı menkul kıymet", "An ABS backed by loans with scheduled principal repayments, such as auto loans.", "Taşıt kredileri gibi planlı anapara ödemeli kredilere dayalı varlığa dayalı menkul kıymet."],
 ["Non-amortizing ABS", "İtfasız (döner) varlığa dayalı menkul kıymet", "An ABS backed by revolving receivables, such as credit card balances, with no scheduled principal payments.", "Kredi kartı bakiyeleri gibi planlı anapara ödemesi olmayan döner alacaklara dayalı menkul kıymet."],
 ["Lockout period", "Kilit (yeniden yatırım) dönemi", "The period in which principal collections are used to buy new receivables instead of being paid to investors.", "Anapara tahsilatlarının yatırımcılara ödenmek yerine yeni alacak alımında kullanıldığı dönem."],
 ["Early amortization", "Erken itfa", "A trigger that ends the lockout period and starts paying principal to investors if the pool performs poorly.", "Havuz kötü performans gösterirse kilit dönemini bitirip yatırımcılara anapara ödemeye başlayan tetikleyici."],
 ["Excess spread", "Fazla getiri marjı", "The difference between the interest earned on the pool and the interest paid to investors plus fees; a first line of loss protection.", "Havuzdan elde edilen faiz ile yatırımcılara ödenen faiz ve ücretler arasındaki fark; ilk kayıp koruması."],
 ["Collateralized debt obligation (CDO)", "Teminatlandırılmış borç yükümlülüğü", "A structured security backed by a diversified pool of debt instruments.", "Çeşitlendirilmiş bir borçlanma araçları havuzuna dayalı yapılandırılmış menkul kıymet."],
 ["Collateralized loan obligation (CLO)", "Teminatlandırılmış kredi yükümlülüğü", "A CDO backed mainly by leveraged corporate loans and run by a collateral manager.", "Esas olarak kaldıraçlı şirket kredilerine dayalı ve bir teminat yöneticisince yönetilen teminatlandırılmış borç yükümlülüğü."],
],
notes="""<h3>Auto loan ABS</h3>
<ul>
<li>Backed by amortizing car loans and leases. Cash flows include interest, scheduled principal and prepayments (from early payoff, sale of the car, or accidents).</li>
<li>Credit enhancement: subordination, reserve accounts, overcollateralization and excess spread.</li>
</ul>
<h3>Credit card ABS</h3>
<ul>
<li>Backed by revolving receivables with no fixed repayment schedule, so the structure is <b>non-amortizing</b>.</li>
<li>During the <b>lockout (revolving) period</b> principal collections buy new receivables, and investors receive only interest. After that, principal is paid out.</li>
<li><b>Early amortization</b> triggers, such as excess spread falling below a threshold, end the revolving period early to protect investors.</li>
<li>Interest is often floating, matching the floating rates charged to cardholders.</li>
</ul>
<h3>Collateralized debt obligations</h3>
<ul>
<li>Pools of bonds or loans, split into senior, mezzanine and equity tranches. A <b>collateral manager</b> buys and sells assets.</li>
<li>The most common type today is the <b>CLO</b>, backed by leveraged corporate loans. Other types use corporate bonds, structured finance securities, or credit derivatives (synthetic CDOs).</li>
<li>The equity tranche earns the residual return after the debt tranches are paid; it profits if the pool's return exceeds the funding cost and suffers first from defaults.</li>
<li>Coverage tests (overcollateralization and interest coverage) protect senior tranches by diverting cash if breached.</li>
</ul>
<div class="trap"><b>Exam trap</b>Credit card ABS investors receive no principal during the lockout period; principal collections are reinvested in new receivables.</div>""",
qs=[
 ["During the lockout period of a credit card ABS, principal collected from cardholders is:", ["paid to investors.", "used to buy new receivables.", "returned to the originator as profit."], 1, "In the revolving period principal is reinvested, so investors receive only interest."],
 ["An early amortization provision in a credit card ABS is most likely triggered by:", ["a rise in excess spread.", "a fall in excess spread below a set level.", "the end of the scheduled lockout period."], 1, "Deteriorating pool performance, often shown by low excess spread, starts principal repayment to protect investors."],
 ["Auto loan asset-backed securities are best described as:", ["amortizing.", "non-amortizing.", "perpetual."], 0, "Car loans have scheduled principal repayments, so the ABS amortizes."],
 ["The difference between the interest earned on an ABS pool and the interest paid to bondholders and servicing fees is:", ["the haircut.", "excess spread.", "the conversion premium."], 1, "Excess spread is available to absorb losses before any tranche is affected."],
 ["A collateralized loan obligation is backed mainly by:", ["residential mortgages.", "credit card receivables.", "leveraged corporate loans."], 2, "CLOs pool loans to highly leveraged companies."],
 ["In a CDO, the party responsible for buying and selling the underlying assets is the:", ["trustee.", "originator.", "collateral manager."], 2, "The collateral manager actively manages the pool within the deal's rules."],
 ["In a CDO, the tranche that receives what is left after all debt tranches are paid is the:", ["senior tranche.", "mezzanine tranche.", "equity tranche."], 2, "The equity tranche holds the residual claim and absorbs the first losses."],
 ["Credit card receivables are suited to a non-amortizing ABS structure because:", ["cardholders pay a fixed monthly instalment.", "the receivables are revolving and have no scheduled principal.", "cardholders cannot prepay their balances."], 1, "Balances are repaid and redrawn continuously, so there is no fixed amortization schedule."],
]))

R.append(dict(id="mb", n="Mortgage-Backed Security (MBS) Instrument and Market Features", k="MBS", w=2, c="#8a5cc2",
terms=[
 ["Mortgage pass-through security", "İpoteğe dayalı aktarımlı menkul kıymet", "A security that passes the cash flows of a mortgage pool to investors pro rata, minus fees.", "İpotek havuzunun nakit akışlarını, ücretler düşüldükten sonra yatırımcılara oransal olarak aktaran menkul kıymet."],
 ["Prepayment risk", "Erken ödeme riski", "The uncertainty in cash flows caused by borrowers repaying their mortgages early.", "Borçluların ipoteklerini erken ödemesinden kaynaklanan nakit akışı belirsizliği."],
 ["Contraction risk", "Daralma riski", "The risk that falling rates speed up prepayments and shorten the security's life.", "Düşen faizlerin erken ödemeleri hızlandırması ve menkul kıymetin ömrünü kısaltması riski."],
 ["Extension risk", "Uzama riski", "The risk that rising rates slow prepayments and lengthen the security's life.", "Yükselen faizlerin erken ödemeleri yavaşlatması ve menkul kıymetin ömrünü uzatması riski."],
 ["Single monthly mortality rate (SMM)", "Aylık erken ödeme oranı", "The share of the outstanding balance prepaid in a month.", "Bir ayda erken ödenen kalan bakiye oranı."],
 ["Conditional prepayment rate (CPR)", "Yıllık erken ödeme oranı", "The annualized equivalent of the monthly prepayment rate.", "Aylık erken ödeme oranının yıllık karşılığı."],
 ["Collateralized mortgage obligation (CMO)", "Teminatlandırılmış ipotek yükümlülüğü", "A security that splits mortgage cash flows into tranches with different exposure to prepayment risk.", "İpotek nakit akışlarını erken ödeme riskine farklı maruz kalan dilimlere bölen menkul kıymet."],
 ["Planned amortization class (PAC)", "Planlı itfa sınıfı", "A CMO tranche with a principal schedule protected within a range of prepayment speeds.", "Belirli erken ödeme hızları aralığında korunan anapara takvimine sahip dilim."],
 ["Support tranche", "Destek dilimi", "A CMO tranche that absorbs prepayment variability to protect the PAC tranche.", "Planlı itfa dilimini korumak için erken ödeme değişkenliğini üstlenen dilim."],
 ["Loan-to-value ratio (LTV)", "Kredi/değer oranı", "The loan amount divided by the value of the property.", "Kredi tutarının gayrimenkulün değerine bölümü."],
 ["Debt service coverage ratio (DSCR)", "Borç servis karşılama oranı", "Net operating income divided by debt service.", "Net faaliyet gelirinin borç servisine bölümü."],
],
notes="""<h3>Residential mortgages</h3>
<ul>
<li>Features: maturity, fixed or adjustable rate, amortization schedule, prepayment penalties, recourse or non-recourse (whether the lender can claim more than the property).</li>
<li>Lower <b>LTV</b> means more borrower equity and lower default risk.</li>
<li><b>Agency</b> residential MBS are guaranteed by government agencies or government-sponsored entities and meet their underwriting standards. <b>Non-agency</b> MBS carry credit risk and need credit enhancement.</li>
</ul>
<h3>Prepayments</h3>
<p class="f">SMM = 1 − (1 − CPR)<sup>1/12</sup></p>
<ul>
<li>Prepayments rise when rates fall (refinancing), and also reflect home sales, defaults and curtailments.</li>
<li><b>Contraction risk:</b> falling rates, faster prepayments, cash returned when reinvestment rates are low. Gives MBS negative convexity.</li>
<li><b>Extension risk:</b> rising rates, slower prepayments, investors locked in at below-market rates.</li>
<li><b>Weighted average life</b> summarizes the expected timing of principal and shortens as prepayment speeds rise.</li>
</ul>
<h3>Collateralized mortgage obligations</h3>
<ul>
<li>CMOs do not remove prepayment risk; they redistribute it among tranches.</li>
<li><b>Sequential-pay:</b> each tranche receives all principal in turn; the first tranche has the shortest life and least extension risk.</li>
<li><b>PAC and support tranches:</b> the PAC receives a scheduled principal amount within a band of prepayment speeds; the support tranche absorbs the variability and has the most prepayment risk.</li>
<li>Floating-rate and inverse floating-rate tranches can be created from a fixed-rate tranche.</li>
</ul>
<h3>Commercial MBS</h3>
<ul>
<li>Backed by loans on income-producing property (offices, shopping centres, apartments). Credit risk depends on the property's income: <b>DSCR</b> and <b>LTV</b> are the key ratios.</li>
<li>Strong <b>call protection</b>: prepayment lockouts, defeasance, prepayment penalty points, yield maintenance charges.</li>
<li>Many loans have <b>balloon</b> payments at maturity, creating <b>balloon risk</b>: if the borrower cannot refinance, the loan may extend.</li>
</ul>
<div class="trap"><b>Exam trap</b>SMM is not CPR divided by 12. Use the compounding formula.</div>""",
qs=[
 ["A mortgage pool has a conditional prepayment rate of 6%. Its single monthly mortality rate is closest to:", ["0.50%", "0.51%", "6.00%"], 1, "SMM = 1 − (0.94)^(1/12) = 0.51%. Dividing by 12 gives 0.50%, which ignores compounding."],
 ["When interest rates fall sharply, holders of mortgage pass-through securities are most exposed to:", ["extension risk.", "contraction risk.", "balloon risk."], 1, "Borrowers refinance and prepay, returning principal when reinvestment rates are low."],
 ["When interest rates rise, holders of mortgage pass-through securities are most exposed to:", ["extension risk.", "contraction risk.", "early amortization risk."], 0, "Prepayments slow, lengthening the security's life at a below-market rate."],
 ["In a CMO with a planned amortization class and a support tranche, prepayment risk is mainly absorbed by the:", ["PAC tranche.", "support tranche.", "senior tranche."], 1, "The support tranche takes faster or slower principal so that the PAC can follow its schedule."],
 ["In a sequential-pay CMO, the tranche with the shortest weighted average life is the:", ["first tranche.", "middle tranche.", "last tranche."], 0, "The first tranche receives all principal payments until it is retired."],
 ["A property worth 500 is financed with a loan of 400. The loan-to-value ratio is:", ["20%", "80%", "125%"], 1, "LTV = 400 / 500 = 80%."],
 ["A commercial property generates net operating income of 120 and its annual debt service is 100. The debt service coverage ratio is:", ["0.83", "1.20", "2.20"], 1, "DSCR = 120 / 100 = 1.20. Values above 1 mean income covers the debt payments."],
 ["Compared with residential MBS, commercial MBS typically offer investors:", ["less call protection.", "more call protection.", "no protection against prepayment."], 1, "Commercial loans commonly include lockouts, defeasance, penalties or yield maintenance charges."],
]))
