# CFA Level I · Alternative Investments · readings 1–7. Original study notes and questions.
R = []

R.append(dict(id="af", n="Alternative Investment Features, Methods, and Structures", k="STRUCTURES", w=2, c="#3b7dd8",
terms=[
 ["Alternative investment", "Alternatif yatırım", "An investment outside traditional long-only stocks, bonds and cash, such as private capital, real assets or hedge funds.", "Geleneksel uzun pozisyonlu hisse, tahvil ve nakit dışındaki yatırım; örneğin özel sermaye, reel varlıklar veya serbest fonlar."],
 ["Fund investing", "Fon aracılığıyla yatırım", "Investing through a pooled vehicle run by a manager.", "Bir yöneticinin işlettiği ortak yatırım aracı üzerinden yatırım yapma."],
 ["Co-investing", "Ortak yatırım", "Investing directly in a deal alongside a fund in which the investor is already a limited partner.", "Yatırımcının zaten sınırlı ortağı olduğu bir fonla birlikte bir işleme doğrudan yatırım yapması."],
 ["Direct investing", "Doğrudan yatırım", "Buying assets or companies directly, without a fund intermediary.", "Varlıkları veya şirketleri fon aracısı olmadan doğrudan satın alma."],
 ["General partner (GP)", "Komandite (yönetici) ortak", "The manager of a limited partnership fund, with unlimited liability.", "Komandit ortaklık fonunun sınırsız sorumlu yöneticisi."],
 ["Limited partner (LP)", "Komanditer (sınırlı sorumlu) ortak", "An investor in a limited partnership whose liability is limited to the capital committed.", "Sorumluluğu taahhüt ettiği sermayeyle sınırlı olan komandit ortaklık yatırımcısı."],
 ["Management fee", "Yönetim ücreti", "An annual fee charged as a percentage of assets or committed capital.", "Varlıkların veya taahhüt edilen sermayenin yüzdesi olarak alınan yıllık ücret."],
 ["Carried interest", "Performans payı (carried interest)", "The general partner's share of fund profits, typically about 20%.", "Genel ortağın fon kârından aldığı pay; tipik olarak yaklaşık %20."],
 ["Hurdle rate", "Engel getiri oranı", "The minimum return investors must receive before the manager earns an incentive fee.", "Yöneticinin performans ücreti alabilmesi için yatırımcıların elde etmesi gereken asgari getiri."],
 ["Clawback", "Geri alma hükmü", "A provision requiring the general partner to return excess carried interest received earlier.", "Genel ortağın daha önce aldığı fazla performans payını iade etmesini gerektiren hüküm."],
 ["Lockup period", "Kilit dönemi", "A period during which investors may not redeem their investment.", "Yatırımcıların yatırımlarını geri çekemediği dönem."],
],
notes="""<h3>Features</h3>
<ul>
<li>Specialized knowledge required, relatively low correlation with traditional assets, illiquidity, less regulation and transparency, high fees, limited and often unreliable historical data.</li>
<li>Returns may come from an illiquidity premium, manager skill, or access to opportunities not available in public markets.</li>
</ul>
<h3>Three ways to invest</h3>
<div class="tbl"><table>
<tr><th></th><th>Fund investing</th><th>Co-investing</th><th>Direct investing</th></tr>
<tr><td>Control over assets</td><td>Lowest</td><td>Middle</td><td>Highest</td></tr>
<tr><td>Fees</td><td>Highest (management and incentive)</td><td>Lower on the co-investment</td><td>No external manager fees</td></tr>
<tr><td>Expertise needed</td><td>Lowest; must select managers</td><td>Middle</td><td>Highest</td></tr>
<tr><td>Diversification</td><td>Highest</td><td>Middle</td><td>Lowest</td></tr>
</table></div>
<ul>
<li>Co-investors face adverse selection: the manager may offer the less attractive deals for co-investment.</li>
</ul>
<h3>Structures</h3>
<ul>
<li>Most funds are <b>limited partnerships</b>: the GP manages and has unlimited liability; LPs provide capital with limited liability. The <b>limited partnership agreement</b> and side letters set terms.</li>
<li>LPs commit capital that is <b>called</b> over time as investments are found.</li>
<li><b>Master-feeder</b> structures let investors in different tax jurisdictions invest through separate feeder funds into one master fund.</li>
<li><b>Separately managed accounts</b> give investors ownership, transparency and control, at higher cost and with larger minimums.</li>
</ul>
<h3>Fees and distribution waterfalls</h3>
<ul>
<li>Typical "2 and 20": 2% management fee, 20% incentive fee (carried interest).</li>
<li><b>Hurdle rate:</b> no incentive fee until investors earn a minimum return. <b>Hard hurdle:</b> fee only on returns above the hurdle. <b>Soft hurdle:</b> once the hurdle is cleared, fee on the whole return (often through a catch-up).</li>
<li><b>High-water mark:</b> no incentive fee until losses are recovered and the fund exceeds its previous peak value.</li>
<li><b>European (whole-of-fund) waterfall:</b> the GP receives carry only after LPs get back all contributed capital plus the hurdle. Favours LPs.</li>
<li><b>American (deal-by-deal) waterfall:</b> carry is paid deal by deal. Favours the GP; a <b>clawback</b> protects LPs if later deals lose money.</li>
<li><b>Lockups</b>, <b>notice periods</b> and <b>gates</b> limit how fast investors can redeem.</li>
</ul>
<div class="trap"><b>Exam trap</b>The European waterfall is the one that favours investors, because the manager waits for the whole fund to return capital.</div>""",
qs=[
 ["Compared with fund investing, direct investing in alternatives typically offers:", ["lower fees and more control.", "higher fees and more diversification.", "lower fees and less required expertise."], 0, "Direct investors avoid external manager fees and control the assets, but need the most expertise."],
 ["An investor who is a limited partner in a private equity fund invests directly in one of the fund's deals alongside it. This is:", ["fund investing.", "co-investing.", "a fund of funds."], 1, "Co-investing means investing in a deal next to the fund, usually at reduced fees."],
 ["A distribution waterfall in which the general partner receives carried interest only after limited partners have received all their contributed capital plus the hurdle return is a:", ["deal-by-deal waterfall.", "whole-of-fund waterfall.", "high-water mark waterfall."], 1, "The European, whole-of-fund approach favours investors by deferring carry."],
 ["A clawback provision requires the:", ["limited partners to contribute more capital.", "general partner to return excess carried interest.", "fund to sell assets before the end of its life."], 1, "If later losses mean the GP received too much carry earlier, it must give some back."],
 ["A hedge fund that lost money last year does not charge an incentive fee this year until its value exceeds its previous peak. This is due to a:", ["hurdle rate.", "lockup period.", "high-water mark."], 2, "A high-water mark prevents managers being paid twice for the same performance."],
 ["A period during which investors in a fund cannot redeem their shares is a:", ["gate.", "lockup period.", "notice period."], 1, "Lockup periods are common in hedge funds and private funds. A gate limits redemptions once allowed."],
 ["Which of the following is a typical characteristic of alternative investments?", ["High liquidity", "Extensive public disclosure", "Relatively low correlation with traditional assets"], 2, "Diversification through low correlation is a key reason to hold alternatives."],
 ["A master-feeder fund structure is used mainly to:", ["raise the fund's leverage.", "accommodate investors with different tax situations.", "avoid paying management fees."], 1, "Separate feeder funds for different jurisdictions invest in one master portfolio."],
]))

R.append(dict(id="ap", n="Alternative Investment Performance and Returns", k="PERFORMANCE", w=2, c="#2e9e8f",
terms=[
 ["Hard hurdle", "Katı engel oranı", "An incentive fee charged only on returns above the hurdle rate.", "Yalnızca engel oranının üzerindeki getiriye uygulanan performans ücreti."],
 ["Soft hurdle", "Esnek engel oranı", "An incentive fee charged on the whole return once the hurdle is exceeded.", "Engel oranı aşıldığında tüm getiriye uygulanan performans ücreti."],
 ["Catch-up clause", "Yakalama hükmü", "A provision giving the manager a large share of returns just above the hurdle until it has its full incentive fee.", "Engelin hemen üzerindeki getiriden, tam performans ücretini alana kadar yöneticiye büyük pay veren hüküm."],
 ["Multiple of invested capital (MOIC)", "Yatırılan sermaye katsayısı", "Total value (distributions plus remaining value) divided by capital invested.", "Toplam değerin (dağıtımlar artı kalan değer) yatırılan sermayeye bölümü."],
 ["Internal rate of return (IRR)", "İç verim oranı", "The discount rate that sets the net present value of a fund's cash flows to zero; the standard return measure for private funds.", "Fonun nakit akışlarının net bugünkü değerini sıfırlayan iskonto oranı; özel fonlarda standart getiri ölçüsü."],
 ["Appraisal smoothing", "Ekspertiz düzleştirmesi", "The understatement of volatility caused by valuing assets with infrequent appraisals.", "Varlıkların seyrek ekspertizlerle değerlenmesinin oynaklığı olduğundan düşük göstermesi."],
 ["Backfill bias", "Geriye doldurma yanlılığı", "The upward bias from adding a fund's earlier good returns when it joins a database.", "Bir fon veri tabanına katıldığında önceki iyi getirilerinin eklenmesinden doğan yukarı yönlü yanlılık."],
 ["Sortino ratio", "Sortino oranı", "Excess return divided by downside deviation.", "Fazla getirinin aşağı yönlü sapmaya bölümü."],
],
notes="""<h3>Calculating fees</h3>
<ul>
<li>Order matters: the management fee is usually charged first, and the incentive fee on the gain net of the management fee.</li>
<li>Example: capital 100 grows to 120. Management fee 2% of ending value = 2.4. Gain net of management fee = 120 − 100 − 2.4 = 17.6. Incentive fee 20% = 3.52. Total fees = 5.92. Investor's net return = (120 − 5.92 − 100) / 100 = 14.08%.</li>
<li>With a hard hurdle of 5%: incentive on 17.6 − 5 = 12.6. With a soft hurdle: on the full 17.6 once 5 is exceeded.</li>
<li>With a high-water mark, no incentive fee is paid until the fund's value exceeds its previous high.</li>
</ul>
<h3>Measuring returns</h3>
<ul>
<li><b>IRR</b> captures the timing of capital calls and distributions; it is the standard for private equity and real estate funds.</li>
<li><b>MOIC</b> = (realized + unrealized value) / invested capital. Simple, but ignores time.</li>
<li>Use time-weighted returns for hedge funds and other open-ended funds where the manager does not control cash flows.</li>
</ul>
<h3>Pitfalls in the data</h3>
<ul>
<li><b>Appraisal-based valuations</b> are infrequent and smoothed, so reported volatility and correlations with public markets are too low.</li>
<li><b>Survivorship bias</b> (failed funds drop out) and <b>backfill bias</b> (funds add their good history when they start reporting) both overstate returns.</li>
<li>Returns are often not normal: skewed and fat-tailed, so the Sharpe ratio can mislead. The Sortino ratio and drawdown measures help.</li>
<li>Leverage, illiquidity and fees must all be considered when comparing alternatives with traditional assets.</li>
</ul>
<div class="trap"><b>Exam trap</b>Check whether the management fee is based on beginning or ending value, and whether the incentive fee is calculated before or after it.</div>""",
qs=[
 ["A fund starts the year with $100 million and ends with $120 million before fees. It charges a 2% management fee on ending value and a 20% incentive fee on gains net of the management fee. Total fees are closest to:", ["$4.00 million", "$5.92 million", "$6.40 million"], 1, "Management fee = 2.4. Incentive fee = 20% × (20 − 2.4) = 3.52. Total = $5.92 million."],
 ["Using the same fund and fees, the investors' net return is closest to:", ["13.60%", "14.08%", "16.00%"], 1, "(120 − 5.92 − 100) / 100 = 14.08%."],
 ["A fund's value is below its high-water mark at year-end, although it earned a positive return during the year. The incentive fee for the year is:", ["zero.", "based on the year's return.", "based on the return above the hurdle rate."], 0, "No incentive fee is paid until the fund exceeds its previous peak."],
 ["Under a soft hurdle, once the fund's return exceeds the hurdle rate, the incentive fee is charged on:", ["the return above the hurdle only.", "the entire return.", "the management fee only."], 1, "A soft hurdle makes the whole return eligible once the hurdle is cleared."],
 ["A private equity fund called $10 million, has distributed $15 million and holds investments valued at $5 million. Its MOIC is:", ["1.5x", "2.0x", "5.0x"], 1, "(15 + 5) / 10 = 2.0x."],
 ["Volatility calculated from appraisal-based real estate returns is most likely:", ["overstated.", "understated.", "accurate."], 1, "Infrequent appraisals smooth valuations, hiding true price variability."],
 ["When a hedge fund joins a database and its earlier strong returns are added to the database's history, the result is:", ["backfill bias.", "survivorship bias.", "appraisal smoothing."], 0, "Only funds with good records choose to start reporting, so adding their history inflates returns."],
 ["The most appropriate return measure for a private equity fund whose manager controls the timing of capital calls and distributions is the:", ["IRR.", "arithmetic mean return.", "time-weighted return."], 0, "IRR reflects the timing and size of cash flows the manager decides."],
]))

R.append(dict(id="pk", n="Investments in Private Capital: Equity and Debt", k="PRIVATE CAPITAL", w=2, c="#c0563f",
terms=[
 ["Private equity", "Özel sermaye", "Equity investment in companies that are not publicly traded.", "Halka açık işlem görmeyen şirketlere özkaynak yatırımı."],
 ["Leveraged buyout (LBO)", "Kaldıraçlı satın alma", "Acquisition of a company financed largely with debt.", "Büyük ölçüde borçla finanse edilen şirket satın alması."],
 ["Venture capital", "Girişim sermayesi", "Equity investment in early-stage companies with high growth potential.", "Yüksek büyüme potansiyeli olan erken aşamadaki şirketlere özkaynak yatırımı."],
 ["Growth equity", "Büyüme sermayesi", "Minority investments in established, growing companies that need capital to expand.", "Büyümek için sermayeye ihtiyaç duyan, yerleşik ve büyüyen şirketlere azınlık yatırımı."],
 ["Private debt", "Özel borç", "Loans and debt instruments provided by non-bank lenders and not traded publicly.", "Banka dışı kredi verenlerin sağladığı ve halka açık işlem görmeyen kredi ve borçlanma araçları."],
 ["Direct lending", "Doğrudan kredi", "Senior loans made by private funds directly to companies, often middle-market firms.", "Özel fonların, çoğu zaman orta ölçekli şirketlere doğrudan verdiği kıdemli krediler."],
 ["Mezzanine debt", "Mezanin borç", "Subordinated debt, often with warrants or conversion features, ranking between senior debt and equity.", "Kıdemli borç ile özkaynak arasında yer alan, çoğu zaman varant veya dönüşüm hakkı içeren ikincil borç."],
 ["Distressed debt", "Sorunlu borç", "Debt of companies in or near default, bought at a deep discount.", "Temerrüt içindeki veya ona yakın şirketlerin, büyük iskontoyla alınan borcu."],
 ["Trade sale", "Stratejik satış", "Exiting an investment by selling the company to another company.", "Yatırımdan, şirketi başka bir şirkete satarak çıkma."],
 ["Secondary sale", "İkincil satış", "Exiting by selling the investment to another private equity firm or investor.", "Yatırımı başka bir özel sermaye şirketine veya yatırımcıya satarak çıkma."],
],
notes="""<h3>Private equity strategies</h3>
<div class="tbl"><table>
<tr><th>Strategy</th><th>Target</th><th>Main source of return</th></tr>
<tr><td>Leveraged buyout</td><td>Mature companies with stable cash flow</td><td>Leverage, operating improvement, multiple expansion</td></tr>
<tr><td>Venture capital</td><td>Start-ups: pre-seed, seed, early stage, later stage</td><td>A few big winners among many failures</td></tr>
<tr><td>Growth equity</td><td>Established, profitable, growing companies</td><td>Expansion; usually minority stakes and little leverage</td></tr>
</table></div>
<ul>
<li>A <b>management buyout</b> is an LBO led by the existing managers; a <b>management buy-in</b> brings in external managers.</li>
<li><b>Exit routes:</b> trade sale, IPO, secondary sale to another fund, recapitalization (adding debt to pay a dividend), and write-off.</li>
<li>Private equity returns are correlated with public equity; appraisal-based reporting understates the link.</li>
</ul>
<h3>Private debt strategies</h3>
<div class="tbl"><table>
<tr><th>Strategy</th><th>Features</th><th>Risk and return</th></tr>
<tr><td>Direct lending</td><td>Senior, secured, floating-rate, covenants</td><td>Lowest in private debt</td></tr>
<tr><td>Unitranche</td><td>Senior and subordinated combined into one loan</td><td>Middle</td></tr>
<tr><td>Mezzanine</td><td>Subordinated; equity kickers such as warrants</td><td>Higher</td></tr>
<tr><td>Venture debt</td><td>Loans to start-ups, often with warrants</td><td>High</td></tr>
<tr><td>Distressed debt</td><td>Bought cheaply; returns from restructuring</td><td>Highest</td></tr>
</table></div>
<ul>
<li>Private debt has grown as banks have pulled back from lending to riskier and mid-sized companies.</li>
<li>Investors earn an illiquidity premium over public credit, but face less liquidity, concentration and valuation uncertainty.</li>
</ul>
<h3>Role in a portfolio</h3>
<ul>
<li>Private equity: higher expected return than public equity, with illiquidity and high manager dispersion (manager selection matters a great deal).</li>
<li>Private debt: income with floating rates, some diversification from public bonds.</li>
</ul>
<div class="trap"><b>Exam trap</b>Mezzanine debt ranks below senior debt but above equity; the warrants give it some equity-like upside.</div>""",
qs=[
 ["An acquisition of a mature company with stable cash flows, financed mostly with borrowed money, is a:", ["venture capital deal.", "leveraged buyout.", "growth equity investment."], 1, "LBOs use high leverage, supported by the target's predictable cash flows."],
 ["Venture capital returns typically come from:", ["steady dividends from many companies.", "a small number of very successful investments.", "high leverage on mature companies."], 1, "Most start-ups fail or return little; a few large successes drive overall performance."],
 ["Subordinated debt that includes warrants and ranks between senior debt and equity is:", ["mezzanine debt.", "direct lending.", "unitranche debt."], 0, "Mezzanine debt combines subordination with equity participation."],
 ["Among private debt strategies, the lowest risk is typically associated with:", ["direct lending.", "distressed debt.", "venture debt."], 0, "Direct lending is usually senior and secured with covenants."],
 ["A private equity firm exits an investment by selling the company to a competitor in the same industry. This exit is a:", ["trade sale.", "secondary sale.", "recapitalization."], 0, "A sale to a strategic buyer is a trade sale."],
 ["A private equity firm exits an investment by selling it to another private equity firm. This exit is a:", ["trade sale.", "secondary sale.", "write-off."], 1, "Selling to another financial investor is a secondary sale."],
 ["Distressed debt investors aim to profit mainly from:", ["regular coupon payments.", "the restructuring or recovery of the issuer.", "short-term trading of investment-grade bonds."], 1, "They buy at deep discounts and gain if the company recovers or the restructuring delivers more than the price paid."],
 ["Growth equity investments are typically:", ["majority stakes using heavy leverage.", "minority stakes with little or no leverage.", "loans secured on the company's assets."], 1, "Growth equity provides capital to expanding companies, usually without taking control."],
]))

R.append(dict(id="re", n="Real Estate and Infrastructure", k="REAL ASSETS", w=2, c="#8a5cc2",
terms=[
 ["Real estate investment trust (REIT)", "Gayrimenkul yatırım ortaklığı", "A listed company that owns income-producing property and distributes most of its income.", "Gelir getiren gayrimenkullere sahip olan ve gelirinin büyük kısmını dağıtan borsa şirketi."],
 ["Net operating income (NOI)", "Net faaliyet geliri", "Rental income minus operating expenses, before financing costs and taxes.", "Kira gelirinden işletme giderlerinin çıkarılmasıyla bulunan, finansman ve vergi öncesi gelir."],
 ["Capitalization rate", "Kapitalizasyon oranı", "Net operating income divided by property value.", "Net faaliyet gelirinin gayrimenkul değerine bölümü."],
 ["Core strategy", "Çekirdek strateji", "Investing in high-quality, fully let properties with low leverage and stable income.", "Tam dolu, kaliteli, düşük kaldıraçlı ve istikrarlı gelirli gayrimenkullere yatırım."],
 ["Value-add strategy", "Değer katma stratejisi", "Investing in properties that need improvement or re-letting to increase value.", "Değerini artırmak için iyileştirme veya yeniden kiralama gerektiren gayrimenkullere yatırım."],
 ["Opportunistic strategy", "Fırsatçı strateji", "High-risk real estate investing, such as development or distressed assets, often with high leverage.", "Yüksek riskli gayrimenkul yatırımı; örneğin geliştirme veya sorunlu varlıklar, çoğu zaman yüksek kaldıraçla."],
 ["Infrastructure", "Altyapı", "Long-lived assets that provide essential services, such as roads, utilities and communication networks.", "Yollar, kamu hizmetleri ve iletişim ağları gibi temel hizmet sağlayan uzun ömürlü varlıklar."],
 ["Greenfield investment", "Sıfırdan yatırım", "Investment in an infrastructure asset that has yet to be built.", "Henüz inşa edilmemiş bir altyapı varlığına yatırım."],
 ["Brownfield investment", "Mevcut varlık yatırımı", "Investment in an existing infrastructure asset with an operating history.", "Faaliyet geçmişi olan mevcut bir altyapı varlığına yatırım."],
 ["Public-private partnership", "Kamu-özel iş birliği", "An arrangement in which a private investor finances and operates public infrastructure.", "Özel bir yatırımcının kamu altyapısını finanse edip işlettiği düzenleme."],
],
notes="""<h3>Real estate</h3>
<ul>
<li>Types: residential, commercial (office, retail, industrial and logistics, hotels), and others such as data centres.</li>
<li>Returns: rental income plus capital appreciation. Leases give stable cash flow; property values move with the economy and interest rates.</li>
</ul>
<div class="tbl"><table>
<tr><th>Form</th><th>Debt</th><th>Equity</th></tr>
<tr><td>Private</td><td>Mortgage loans, construction loans</td><td>Direct ownership, private real estate funds</td></tr>
<tr><td>Public</td><td>Mortgage-backed securities</td><td>REITs, real estate company shares</td></tr>
</table></div>
<ul>
<li>Direct ownership: control and tax benefits, but large lot sizes, illiquidity, concentration and management effort.</li>
<li>REITs: liquid and diversified, but their returns behave partly like equities.</li>
</ul>
<h3>Valuation</h3>
<p class="f">capitalization rate = NOI / property value &nbsp;&nbsp;&nbsp; value = NOI / cap rate</p>
<ul>
<li>Approaches: income (direct capitalization or discounted cash flow), comparable sales, and cost (replacement cost).</li>
<li>Lower cap rates mean higher values; cap rates tend to rise with interest rates.</li>
</ul>
<h3>Strategies by risk</h3>
<p class="f">core &lt; core-plus &lt; value-add &lt; opportunistic</p>
<h3>Infrastructure</h3>
<ul>
<li><b>Economic</b> infrastructure: transport, energy, utilities, communications. <b>Social</b> infrastructure: schools, hospitals, prisons.</li>
<li><b>Brownfield</b> assets have operating histories and steady cash flows. <b>Greenfield</b> projects carry construction and demand risk, with higher expected return.</li>
<li>Revenue may come from user fees, regulated tariffs, or availability payments from the government (as in many public-private partnerships).</li>
<li>Attractions: long-lived, often monopoly-like, inflation-linked cash flows. Risks: regulation, politics, construction, illiquidity.</li>
</ul>
<div class="trap"><b>Exam trap</b>Brownfield is the lower-risk infrastructure investment, because the asset already exists and has a record of cash flow.</div>""",
qs=[
 ["A property produces net operating income of $500,000. Comparable properties sell at a capitalization rate of 5%. The estimated value is:", ["$2.5 million", "$10.0 million", "$25.0 million"], 1, "Value = 500,000 / 0.05 = $10.0 million."],
 ["A property worth $10 million produces net operating income of $600,000. Its capitalization rate is:", ["5.0%", "6.0%", "6.7%"], 1, "600,000 / 10,000,000 = 6.0%."],
 ["A real estate strategy that focuses on high-quality, fully let properties with low leverage is:", ["core.", "value-add.", "opportunistic."], 0, "Core strategies aim for stable income with the lowest risk."],
 ["Among real estate strategies, the highest expected risk and return is associated with:", ["core.", "value-add.", "opportunistic."], 2, "Opportunistic strategies include development and distressed assets, often with high leverage."],
 ["Compared with direct ownership of property, investing through REITs provides:", ["more control over the properties.", "greater liquidity.", "lower correlation with equities."], 1, "REIT shares trade on exchanges, but their prices move partly with the stock market."],
 ["An investment in a toll road that has operated for ten years is best described as a:", ["greenfield investment.", "brownfield investment.", "social infrastructure investment."], 1, "Brownfield investments are in existing assets with operating histories."],
 ["Compared with brownfield infrastructure investments, greenfield investments typically have:", ["lower risk.", "higher risk.", "more stable cash flows."], 1, "Greenfield projects face construction and demand uncertainty."],
 ["A hospital financed and run by a private company under a long-term contract with the government is an example of:", ["social infrastructure.", "economic infrastructure.", "a core real estate investment."], 0, "Hospitals, schools and similar public facilities are social infrastructure."],
]))

R.append(dict(id="nr", n="Natural Resources", k="RESOURCES", w=2, c="#b8860b",
terms=[
 ["Farmland", "Tarım arazisi", "Land used to grow crops or raise livestock, earning income from harvests or leases.", "Ürün yetiştirmek veya hayvancılık için kullanılan, hasattan veya kiradan gelir sağlayan arazi."],
 ["Timberland", "Orman arazisi", "Land used to grow trees for harvest.", "Hasat için ağaç yetiştirilen arazi."],
 ["Commodity", "Emtia", "A physical good such as energy, metals or agricultural products.", "Enerji, metal veya tarım ürünü gibi fiziksel mal."],
 ["Contango", "Contango", "A market in which futures prices are above the spot price.", "Vadeli fiyatların spot fiyatın üzerinde olduğu piyasa."],
 ["Backwardation", "Backwardation", "A market in which futures prices are below the spot price.", "Vadeli fiyatların spot fiyatın altında olduğu piyasa."],
 ["Roll yield", "Devir getirisi", "The return from replacing expiring futures with longer-dated ones; positive in backwardation.", "Vadesi dolan vadeli sözleşmeleri daha uzun vadelilerle değiştirmekten gelen getiri; backwardation'da pozitiftir."],
 ["Collateral yield", "Teminat getirisi", "The interest earned on the cash held as collateral for futures positions.", "Vadeli pozisyonlar için teminat olarak tutulan nakdin faiz getirisi."],
 ["Spot price return", "Spot fiyat getirisi", "The change in the price of the physical commodity.", "Fiziksel emtianın fiyatındaki değişim."],
],
notes="""<h3>Land: farmland and timberland</h3>
<ul>
<li>Return sources: income from harvests or leases, and changes in land value.</li>
<li><b>Timberland</b> has a production flexibility that farmland lacks: if prices are low, the owner can delay harvesting and let the trees keep growing.</li>
<li>Both offer inflation protection and low correlation with financial assets, but are illiquid and exposed to weather, disease and regulation.</li>
<li>ESG considerations: water use, deforestation, biodiversity, carbon capture by forests.</li>
</ul>
<h3>Commodities</h3>
<ul>
<li>Sectors: energy, industrial metals, precious metals, grains, livestock, softs.</li>
<li>Most investors use <b>futures</b>, commodity funds and ETFs, or shares of producers. Direct physical holdings involve storage costs.</li>
</ul>
<p class="f">total return on a futures position = spot price return + roll yield + collateral yield</p>
<div class="tbl"><table>
<tr><th>Curve</th><th>Futures vs spot</th><th>Roll yield for a long investor</th></tr>
<tr><td>Contango</td><td>Futures above spot</td><td>Negative</td></tr>
<tr><td>Backwardation</td><td>Futures below spot</td><td>Positive</td></tr>
</table></div>
<ul>
<li>Backwardation often reflects a high <b>convenience yield</b>: users value having the physical commodity now. Contango reflects storage and financing costs.</li>
<li>Commodities tend to do well in periods of unexpected inflation and supply shocks, and provide diversification, but they produce no income and are volatile.</li>
</ul>
<div class="trap"><b>Exam trap</b>Even if spot prices are flat, a long futures investor loses in contango through negative roll yield.</div>""",
qs=[
 ["When futures prices are above the spot price, the market is in:", ["contango.", "backwardation.", "equilibrium."], 0, "Contango means an upward-sloping futures curve, usually reflecting storage and financing costs."],
 ["For an investor holding long commodity futures, roll yield is positive when the market is in:", ["contango.", "backwardation.", "either contango or backwardation."], 1, "Rolling into cheaper longer-dated contracts that converge upward produces a gain."],
 ["A commodity futures position has a spot price return of 3%, a roll yield of −2% and a collateral yield of 4%. Its total return is closest to:", ["1%", "5%", "9%"], 1, "3% − 2% + 4% = 5%."],
 ["Compared with farmland, timberland offers greater flexibility because:", ["it produces income every season.", "harvesting can be delayed when prices are low.", "it is unaffected by weather."], 1, "Trees keep growing, so owners can wait for better prices."],
 ["A high convenience yield for a commodity is most likely associated with:", ["contango.", "backwardation.", "low spot prices."], 1, "When holding the physical good is valuable, spot prices rise relative to futures."],
 ["Which of the following is a typical benefit of adding commodities to a portfolio?", ["Regular income payments", "Protection against unexpected inflation", "Low volatility"], 1, "Commodity prices often rise with inflation shocks, but they pay no income and are volatile."],
 ["The interest earned on cash held as margin for a commodity futures position is the:", ["roll yield.", "spot return.", "collateral yield."], 2, "Collateral yield is the return on the cash backing the futures exposure."],
 ["Most institutional investors gain commodity exposure mainly through:", ["physical storage of commodities.", "commodity futures and related funds.", "farmland only."], 1, "Futures avoid the costs of storing physical goods."],
]))

R.append(dict(id="hf", n="Hedge Funds", k="HEDGE FUNDS", w=2, c="#2f8f5b",
terms=[
 ["Hedge fund", "Serbest fon", "A lightly regulated pooled fund that can use leverage, short selling and derivatives.", "Kaldıraç, açığa satış ve türev araç kullanabilen, sınırlı düzenlemeye tabi ortak fon."],
 ["Long/short equity", "Uzun/kısa hisse stratejisi", "Buying undervalued shares and shorting overvalued ones, usually with net long exposure.", "Değeri düşük payları alıp yüksek olanları açığa satma; genellikle net uzun pozisyonla."],
 ["Equity market neutral", "Piyasa nötr hisse stratejisi", "Long and short equity positions balanced to remove market exposure.", "Piyasa riskini ortadan kaldıracak şekilde dengelenmiş uzun ve kısa hisse pozisyonları."],
 ["Merger arbitrage", "Birleşme arbitrajı", "Buying the target of an announced acquisition and, in share deals, shorting the acquirer.", "Açıklanan bir satın almanın hedef şirketini alıp, pay takası işlemlerinde alıcıyı açığa satma."],
 ["Convertible bond arbitrage", "Dönüştürülebilir tahvil arbitrajı", "Buying underpriced convertible bonds and shorting the issuer's shares.", "Ucuz dönüştürülebilir tahvilleri alıp ihraççının paylarını açığa satma."],
 ["Global macro", "Global makro", "Taking positions across markets based on views of economic trends, interest rates and currencies.", "Ekonomik eğilimler, faizler ve kurlar hakkındaki görüşlere dayanarak piyasalar arasında pozisyon alma."],
 ["Fund of funds", "Fon sepeti fonu", "A fund that invests in several hedge funds.", "Birden fazla serbest fona yatırım yapan fon."],
 ["Gate", "Çıkış sınırı", "A limit on the share of a fund that can be redeemed in a period.", "Bir dönemde fonun geri ödenebilecek kısmına konan sınır."],
],
notes="""<h3>Characteristics</h3>
<ul>
<li>Aim for absolute returns; use leverage, short positions and derivatives; light regulation; high fees; lockups, notice periods and gates.</li>
<li>Access through direct investment, funds of funds (diversification and due diligence, but an extra layer of fees), or separately managed accounts.</li>
</ul>
<h3>Strategy groups</h3>
<div class="tbl"><table>
<tr><th>Group</th><th>Strategy</th><th>Idea</th></tr>
<tr><td>Equity</td><td>Long/short</td><td>Stock picking, net long</td></tr>
<tr><td></td><td>Market neutral</td><td>Beta close to zero; return from stock selection</td></tr>
<tr><td></td><td>Short-biased</td><td>Net short; looks for overvalued or fraudulent companies</td></tr>
<tr><td>Event-driven</td><td>Merger arbitrage</td><td>Long target, short acquirer in share deals; risk is deal failure</td></tr>
<tr><td></td><td>Distressed</td><td>Securities of companies in or near bankruptcy</td></tr>
<tr><td>Relative value</td><td>Convertible arbitrage</td><td>Long convertible, short shares</td></tr>
<tr><td></td><td>Fixed income arbitrage</td><td>Price differences between related bonds, often highly levered</td></tr>
<tr><td>Opportunistic</td><td>Global macro</td><td>Top-down views on rates, currencies, commodities</td></tr>
<tr><td></td><td>Managed futures</td><td>Systematic trend following in futures markets</td></tr>
<tr><td>Multi-strategy</td><td>Several of the above</td><td>Flexible allocation across strategies</td></tr>
</table></div>
<h3>Risks and analysis</h3>
<ul>
<li>Leverage magnifies losses and can force sales at bad prices; liquidity mismatches arise when assets are illiquid but investors can redeem.</li>
<li>Returns are often negatively skewed: steady gains with occasional large losses (for example, merger arbitrage when deals fail).</li>
<li>Reported returns suffer from survivorship and backfill bias; due diligence covers strategy, risk management, operations and governance.</li>
</ul>
<div class="trap"><b>Exam trap</b>In merger arbitrage the main risk is that the deal falls through, not the direction of the stock market.</div>""",
qs=[
 ["An acquisition is announced in which the acquirer will pay with its own shares. A merger arbitrage fund will most likely:", ["buy the acquirer and short the target.", "buy the target and short the acquirer.", "buy both the target and the acquirer."], 1, "The fund captures the spread between the target's price and the value of the offer."],
 ["The main risk in merger arbitrage is that:", ["the deal fails to complete.", "interest rates rise.", "the market falls slightly."], 0, "If the deal collapses, the target's price usually falls sharply."],
 ["An equity hedge fund that aims for a portfolio beta close to zero is following a:", ["short-biased strategy.", "long/short strategy with net long exposure.", "market neutral strategy."], 2, "Market neutral funds balance long and short positions to remove market exposure."],
 ["A convertible bond arbitrage strategy typically involves:", ["buying the convertible bond and shorting the issuer's shares.", "shorting the convertible bond and buying the issuer's shares.", "buying both the convertible bond and the shares."], 0, "The short share position hedges the equity exposure embedded in the convertible."],
 ["A hedge fund that takes positions in currencies, interest rates and commodities based on its view of economic trends is following a:", ["global macro strategy.", "distressed securities strategy.", "relative value strategy."], 0, "Global macro funds make top-down bets across asset classes."],
 ["Compared with investing directly in a single hedge fund, a fund of funds offers:", ["lower total fees.", "more diversification but an extra layer of fees.", "daily liquidity without restrictions."], 1, "Diversification and manager selection come at the cost of additional fees."],
 ["A fund provision limiting redemptions to 10% of the fund's assets in any quarter is a:", ["gate.", "lockup.", "high-water mark."], 0, "A gate caps how much can be withdrawn in a period."],
 ["Many hedge fund strategies produce returns that are:", ["normally distributed.", "positively skewed.", "negatively skewed."], 2, "They earn steady small gains with occasional large losses, which standard measures may understate."],
]))

R.append(dict(id="da", n="Introduction to Digital Assets", k="DIGITAL", w=2, c="#c2417a",
terms=[
 ["Digital asset", "Dijital varlık", "An asset created, stored and transferred electronically, usually recorded on a distributed ledger.", "Elektronik olarak oluşturulan, saklanan ve devredilen, genellikle dağıtık defterde kayıtlı varlık."],
 ["Distributed ledger", "Dağıtık defter", "A database shared and kept in sync across many participants.", "Birçok katılımcı arasında paylaşılan ve eşzamanlı tutulan veri tabanı."],
 ["Blockchain", "Blokzincir", "A distributed ledger that records transactions in blocks linked cryptographically.", "İşlemleri şifreleme yoluyla birbirine bağlı bloklar halinde kaydeden dağıtık defter."],
 ["Permissionless network", "İzinsiz ağ", "A network that anyone can join and validate.", "Herkesin katılabildiği ve doğrulama yapabildiği ağ."],
 ["Permissioned network", "İzinli ağ", "A network restricted to approved participants.", "Yalnızca onaylı katılımcılara açık ağ."],
 ["Proof of work", "İş ispatı", "A consensus method in which miners solve computing puzzles to add blocks.", "Madencilerin blok eklemek için hesaplama problemleri çözdüğü uzlaşı yöntemi."],
 ["Proof of stake", "Hisse ispatı", "A consensus method in which validators are chosen according to the coins they stake.", "Doğrulayıcıların kilitledikleri coin miktarına göre seçildiği uzlaşı yöntemi."],
 ["Stablecoin", "Sabit değerli coin", "A cryptocurrency designed to hold a stable value against a reference such as a currency.", "Bir para birimi gibi bir referansa karşı sabit değer korumak üzere tasarlanmış kripto para."],
 ["Non-fungible token (NFT)", "Değiştirilemez token", "A unique digital token representing ownership of a specific item.", "Belirli bir varlığın sahipliğini temsil eden benzersiz dijital token."],
 ["Smart contract", "Akıllı sözleşme", "Code on a blockchain that executes automatically when conditions are met.", "Koşullar sağlandığında otomatik olarak çalışan blokzincir üzerindeki kod."],
 ["Decentralized finance (DeFi)", "Merkeziyetsiz finans", "Financial services provided through smart contracts without traditional intermediaries.", "Geleneksel aracılar olmadan akıllı sözleşmeler aracılığıyla sunulan finansal hizmetler."],
],
notes="""<h3>The technology</h3>
<ul>
<li>A <b>distributed ledger</b> keeps a shared record across a network. A <b>blockchain</b> groups transactions into blocks; each block contains a cryptographic link to the previous one, so altering history is very hard.</li>
<li><b>Consensus mechanisms</b> decide who adds the next block. <b>Proof of work</b>: miners spend computing power; secure but energy-intensive. <b>Proof of stake</b>: validators lock up coins and risk losing them if they cheat; far less energy.</li>
<li><b>Permissionless</b> networks are open to anyone; <b>permissioned</b> networks restrict participation, as used by some institutions.</li>
</ul>
<h3>Types of digital asset</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>Description</th></tr>
<tr><td>Cryptocurrencies</td><td>Native coins of a blockchain, used for payment or network fees</td></tr>
<tr><td>Stablecoins</td><td>Pegged to a reference asset, backed by reserves or managed by algorithms</td></tr>
<tr><td>Tokens</td><td>Utility tokens (access to a service), governance tokens (voting), security tokens (ownership of an asset)</td></tr>
<tr><td>NFTs</td><td>Unique tokens for specific items such as art or collectibles</td></tr>
<tr><td>Central bank digital currencies</td><td>Digital money issued by a central bank</td></tr>
</table></div>
<ul>
<li><b>Smart contracts</b> run automatically on the blockchain and power decentralized finance: lending, exchanges and derivatives without intermediaries.</li>
</ul>
<h3>Investing</h3>
<ul>
<li>Ways in: direct holdings through exchanges or self-custody wallets, funds and exchange-traded products, futures, and shares of companies in the sector.</li>
<li>Risks: extreme volatility, uncertain and changing regulation, custody and hacking risk, fraud, operational failures of exchanges, and the lack of cash flows on which to base a valuation.</li>
<li>Correlation with equities has varied and has tended to rise in periods of stress.</li>
</ul>
<div class="trap"><b>Exam trap</b>Proof of stake does not require miners to solve puzzles; validators are chosen according to the coins they lock up.</div>""",
qs=[
 ["A blockchain network that anyone can join and help validate is:", ["permissioned.", "permissionless.", "centralized."], 1, "Permissionless networks are open to all participants."],
 ["In a proof-of-stake system, the right to validate transactions depends mainly on:", ["computing power.", "the coins a participant locks up.", "approval by a central authority."], 1, "Validators stake coins, which they can lose if they act dishonestly."],
 ["Compared with proof of stake, proof of work:", ["uses much more energy.", "uses much less energy.", "does not require consensus."], 0, "Miners compete by performing large amounts of computation."],
 ["A cryptocurrency designed to maintain a constant value against the US dollar is a:", ["stablecoin.", "governance token.", "non-fungible token."], 0, "Stablecoins aim to hold a fixed value relative to a reference asset."],
 ["A unique digital token representing ownership of a specific artwork is a:", ["utility token.", "stablecoin.", "non-fungible token."], 2, "Each NFT is unique and cannot be exchanged one-for-one with another."],
 ["Code on a blockchain that executes automatically when agreed conditions are met is a:", ["smart contract.", "distributed ledger.", "proof of work."], 0, "Smart contracts underpin decentralized finance applications."],
 ["Which of the following is a major risk of investing in digital assets?", ["Guaranteed regulatory protection", "Stable and predictable prices", "Custody and hacking risk"], 2, "Assets held on exchanges or in wallets can be stolen or lost, and investor protections are limited."],
 ["A token that gives its holders voting rights over changes to a protocol is a:", ["utility token.", "governance token.", "security token."], 1, "Governance tokens let holders vote on how a network or application is run."],
]))
