# CFA Level I · Portfolio Management · readings 1–6. Original study notes and questions.
R = []

R.append(dict(id="r1", n="Portfolio Risk and Return: Part I", k="RISK & RETURN", w=3, c="#3b7dd8",
terms=[
 ["Risk aversion", "Riskten kaçınma", "Preferring a certain outcome to a risky one with the same expected value.", "Aynı beklenen değere sahip riskli bir sonuç yerine kesin bir sonucu tercih etme."],
 ["Utility function", "Fayda fonksiyonu", "A measure of an investor's satisfaction from a portfolio, combining expected return and risk.", "Beklenen getiri ve riski birleştirerek yatırımcının bir portföyden aldığı tatmini ölçen fonksiyon."],
 ["Indifference curve", "Kayıtsızlık eğrisi", "Combinations of risk and return that give an investor the same utility.", "Yatırımcıya aynı faydayı sağlayan risk ve getiri bileşimleri."],
 ["Efficient frontier", "Etkin sınır", "The set of portfolios offering the highest expected return for each level of risk.", "Her risk düzeyi için en yüksek beklenen getiriyi sunan portföyler kümesi."],
 ["Global minimum-variance portfolio", "Küresel en düşük varyanslı portföy", "The risky portfolio with the lowest possible variance.", "Mümkün olan en düşük varyansa sahip riskli portföy."],
 ["Capital allocation line (CAL)", "Sermaye tahsis doğrusu", "The combinations of the risk-free asset and a risky portfolio available to an investor.", "Yatırımcının erişebildiği, risksiz varlık ile riskli portföy bileşimleri."],
 ["Optimal risky portfolio", "Optimal riskli portföy", "The risky portfolio where the capital allocation line is tangent to the efficient frontier.", "Sermaye tahsis doğrusunun etkin sınıra teğet olduğu riskli portföy."],
 ["Optimal investor portfolio", "Optimal yatırımcı portföyü", "The point on the capital allocation line that touches the investor's highest indifference curve.", "Sermaye tahsis doğrusunun yatırımcının en yüksek kayıtsızlık eğrisine değdiği nokta."],
 ["Correlation", "Korelasyon", "A measure from −1 to +1 of how two assets' returns move together.", "İki varlığın getirilerinin birlikte nasıl hareket ettiğini −1 ile +1 arasında ölçen gösterge."],
],
notes="""<h3>Historical record</h3>
<ul>
<li>Over long periods: small-company shares &gt; large-company shares &gt; long-term bonds &gt; bills, both in return and in volatility. Higher risk has been rewarded with higher return.</li>
<li>Asset returns are often not normal: they are skewed and fat-tailed.</li>
</ul>
<h3>Risk aversion and utility</h3>
<p class="f">U = E(R) − ½ × A × σ²</p>
<ul>
<li>A &gt; 0: risk-averse; A = 0: risk-neutral; A &lt; 0: risk-seeking. Use returns and variance as decimals.</li>
<li>Indifference curves slope upward; a more risk-averse investor has <b>steeper</b> curves, needing more return for each extra unit of risk.</li>
</ul>
<h3>Two-asset portfolio</h3>
<p class="f">σ<sub>p</sub>² = w<sub>1</sub>²σ<sub>1</sub>² + w<sub>2</sub>²σ<sub>2</sub>² + 2w<sub>1</sub>w<sub>2</sub>ρσ<sub>1</sub>σ<sub>2</sub></p>
<ul>
<li>The lower the correlation, the greater the risk reduction. At ρ = +1 there is no diversification benefit.</li>
<li>As the number of assets grows, portfolio variance approaches the average covariance; individual variances matter less.</li>
</ul>
<h3>From frontier to choice</h3>
<ul>
<li>The <b>minimum-variance frontier</b> traces the lowest risk for each return. The upper part, above the global minimum-variance portfolio, is the <b>efficient frontier</b>.</li>
<li>Adding a risk-free asset creates the <b>capital allocation line</b>: E(R<sub>p</sub>) = R<sub>f</sub> + [(E(R<sub>i</sub>) − R<sub>f</sub>)/σ<sub>i</sub>] × σ<sub>p</sub>. The best CAL is tangent to the efficient frontier at the <b>optimal risky portfolio</b>.</li>
<li><b>Two-fund separation:</b> all investors hold the same optimal risky portfolio; their risk aversion only determines how much they put in it versus the risk-free asset.</li>
<li>The <b>optimal investor portfolio</b> is where the investor's highest attainable indifference curve touches the CAL.</li>
</ul>
<div class="trap"><b>Exam trap</b>In the utility formula, enter 20% as 0.20, so σ² = 0.04. Mixing percentages and decimals gives absurd results.</div>""",
qs=[
 ["An investor with a risk aversion coefficient of 4 considers a portfolio with an expected return of 10% and a standard deviation of 20%. Its utility is closest to:", ["2.0%", "6.0%", "8.0%"], 0, "U = 0.10 − 0.5 × 4 × 0.20² = 0.10 − 0.08 = 0.02."],
 ["An investor with a risk aversion coefficient of zero is best described as:", ["risk-averse.", "risk-neutral.", "risk-seeking."], 1, "With A = 0, risk does not affect utility; only expected return matters."],
 ["Compared with a less risk-averse investor, a more risk-averse investor has indifference curves that are:", ["flatter.", "steeper.", "downward sloping."], 1, "Each additional unit of risk requires more extra return to keep utility unchanged."],
 ["A portfolio holds equal weights in two assets with standard deviations of 10% and 20% and a correlation of zero. Its standard deviation is closest to:", ["11.18%", "15.00%", "22.36%"], 0, "σ² = 0.25 × 0.01 + 0.25 × 0.04 = 0.0125; σ = 11.18%."],
 ["The efficient frontier is the set of portfolios that:", ["have the lowest correlation.", "offer the highest expected return for each level of risk.", "contain only risk-free assets."], 1, "Portfolios on the efficient frontier cannot be improved without taking more risk."],
 ["The slope of the capital allocation line equals the risky portfolio's:", ["beta.", "Sharpe ratio.", "expected return."], 1, "Slope = (E(R) − Rf) / σ, the reward per unit of total risk."],
 ["Under two-fund separation, investors with different risk tolerances will hold:", ["different optimal risky portfolios.", "the same optimal risky portfolio in different proportions with the risk-free asset.", "only the global minimum-variance portfolio."], 1, "The risky portfolio is the same for everyone; only the mix with the risk-free asset differs."],
 ["An investor's optimal portfolio is found where the capital allocation line:", ["crosses the vertical axis.", "is tangent to the investor's highest attainable indifference curve.", "meets the global minimum-variance portfolio."], 1, "That point maximizes the investor's utility given the available opportunities."],
]))

R.append(dict(id="r2", n="Portfolio Risk and Return: Part II", k="CAPM", w=4, c="#2e9e8f",
terms=[
 ["Capital market line (CML)", "Sermaye piyasası doğrusu", "The capital allocation line that uses the market portfolio as the risky portfolio.", "Riskli portföy olarak piyasa portföyünü kullanan sermaye tahsis doğrusu."],
 ["Market portfolio", "Piyasa portföyü", "A portfolio of all risky assets weighted by market value.", "Tüm riskli varlıkların piyasa değerine göre ağırlıklandırıldığı portföy."],
 ["Systematic risk", "Sistematik risk", "Risk that affects the whole market and cannot be diversified away.", "Tüm piyasayı etkileyen ve çeşitlendirmeyle giderilemeyen risk."],
 ["Nonsystematic risk", "Sistematik olmayan risk", "Risk specific to a company or industry that can be removed by diversification.", "Şirkete veya sektöre özgü, çeşitlendirmeyle giderilebilen risk."],
 ["Beta", "Beta", "A measure of an asset's systematic risk: its sensitivity to market returns.", "Bir varlığın sistematik riskinin ölçüsü: piyasa getirilerine duyarlılığı."],
 ["Capital asset pricing model (CAPM)", "Finansal varlık fiyatlama modeli", "A model in which expected return equals the risk-free rate plus beta times the market risk premium.", "Beklenen getirinin risksiz faiz artı beta çarpı piyasa risk primine eşit olduğu model."],
 ["Security market line (SML)", "Menkul kıymet piyasası doğrusu", "The graph of the CAPM: expected return against beta.", "Finansal varlık fiyatlama modelinin grafiği: beklenen getiri ile beta ilişkisi."],
 ["Sharpe ratio", "Sharpe oranı", "Excess return divided by total risk (standard deviation).", "Fazla getirinin toplam riske (standart sapmaya) bölümü."],
 ["Treynor ratio", "Treynor oranı", "Excess return divided by beta.", "Fazla getirinin betaya bölümü."],
 ["Jensen's alpha", "Jensen alfası", "Actual return minus the return predicted by the CAPM.", "Gerçekleşen getiriden finansal varlık fiyatlama modelinin öngördüğü getirinin çıkarılması."],
 ["M-squared", "M-kare", "A portfolio's return adjusted to the market's total risk, minus the market return.", "Portföy getirisinin piyasanın toplam riskine göre düzeltilip piyasa getirisinden çıkarılması."],
],
notes="""<h3>Capital market line</h3>
<p class="f">E(R<sub>p</sub>) = R<sub>f</sub> + [(E(R<sub>m</sub>) − R<sub>f</sub>) / σ<sub>m</sub>] × σ<sub>p</sub></p>
<ul>
<li>If all investors share the same expectations, the optimal risky portfolio is the <b>market portfolio</b>.</li>
<li>Points left of the market portfolio are lending portfolios; points to the right involve borrowing.</li>
</ul>
<h3>Systematic and nonsystematic risk</h3>
<ul>
<li>Total risk = systematic + nonsystematic. Diversification removes nonsystematic risk, so only <b>systematic risk is rewarded</b>.</li>
<li>Multifactor models (macro factors, or fundamental factors such as size and value) extend the idea to several sources of systematic risk.</li>
</ul>
<p class="f">β<sub>i</sub> = Cov(R<sub>i</sub>, R<sub>m</sub>) / σ<sub>m</sub>² = ρ<sub>i,m</sub> × σ<sub>i</sub> / σ<sub>m</sub></p>
<h3>CAPM and the SML</h3>
<p class="f">E(R<sub>i</sub>) = R<sub>f</sub> + β<sub>i</sub> × [E(R<sub>m</sub>) − R<sub>f</sub>]</p>
<ul>
<li>Assumptions: risk-averse, return-maximizing investors; frictionless markets; one-period horizon; homogeneous expectations; infinitely divisible assets; price takers.</li>
<li>A security plotting <b>above</b> the SML offers more return than its beta requires: <b>undervalued</b>. Below: overvalued.</li>
<li>The CML uses total risk and applies only to efficient portfolios; the SML uses beta and applies to any asset.</li>
</ul>
<h3>Performance measures</h3>
<div class="tbl"><table>
<tr><th>Measure</th><th>Formula</th><th>Risk used</th></tr>
<tr><td>Sharpe ratio</td><td>(R<sub>p</sub> − R<sub>f</sub>) / σ<sub>p</sub></td><td>Total</td></tr>
<tr><td>M-squared</td><td>(R<sub>p</sub> − R<sub>f</sub>) × σ<sub>m</sub>/σ<sub>p</sub> − (R<sub>m</sub> − R<sub>f</sub>)</td><td>Total, in percentage terms</td></tr>
<tr><td>Treynor ratio</td><td>(R<sub>p</sub> − R<sub>f</sub>) / β<sub>p</sub></td><td>Systematic</td></tr>
<tr><td>Jensen's alpha</td><td>R<sub>p</sub> − [R<sub>f</sub> + β<sub>p</sub>(R<sub>m</sub> − R<sub>f</sub>)]</td><td>Systematic</td></tr>
</table></div>
<ul>
<li>Use Sharpe or M-squared for a portfolio that is the investor's whole wealth; Treynor or alpha for a well-diversified part of a larger portfolio.</li>
</ul>
<div class="trap"><b>Exam trap</b>Beta is not σ<sub>i</sub>/σ<sub>m</sub>; that ratio must be multiplied by the correlation.</div>""",
qs=[
 ["The risk-free rate is 3%, the expected market return is 9% and a share's beta is 1.2. Its required return under the CAPM is:", ["9.0%", "10.2%", "13.8%"], 1, "3% + 1.2 × (9% − 3%) = 10.2%."],
 ["A share has a standard deviation of 30% and a correlation with the market of 0.6. The market's standard deviation is 20%. The share's beta is:", ["0.4", "0.9", "1.5"], 1, "β = 0.6 × 30 / 20 = 0.9. The ratio of standard deviations alone gives 1.5."],
 ["According to the CAPM, investors are rewarded for bearing:", ["total risk.", "systematic risk only.", "nonsystematic risk only."], 1, "Nonsystematic risk can be diversified away at no cost, so it earns no premium."],
 ["A portfolio returned 12% with a standard deviation of 18%. The risk-free rate is 3%. Its Sharpe ratio is:", ["0.50", "0.67", "4.00"], 0, "(12 − 3) / 18 = 0.50."],
 ["A portfolio returned 12% with a beta of 1.5. The risk-free rate is 3%. Its Treynor ratio is:", ["6.0", "8.0", "9.0"], 0, "(12 − 3) / 1.5 = 6.0."],
 ["A portfolio with a beta of 1.5 returned 12%. The risk-free rate is 3% and the market returned 8%. Jensen's alpha is:", ["1.5%", "4.0%", "9.0%"], 0, "Required = 3% + 1.5 × 5% = 10.5%. Alpha = 12% − 10.5% = 1.5%."],
 ["A security whose expected return plots above the security market line is:", ["overvalued.", "undervalued.", "correctly valued."], 1, "It offers more return than its systematic risk requires, so its price should rise."],
 ["Compared with the security market line, the capital market line:", ["uses beta as its measure of risk.", "applies to individual securities.", "uses total risk and applies to efficient portfolios."], 2, "The CML plots return against standard deviation for combinations of the market portfolio and the risk-free asset."],
]))

R.append(dict(id="ov", n="Portfolio Management: An Overview", k="OVERVIEW", w=3, c="#c0563f",
terms=[
 ["Portfolio approach", "Portföy yaklaşımı", "Evaluating investments by their contribution to the risk and return of the whole portfolio.", "Yatırımları tüm portföyün risk ve getirisine katkılarına göre değerlendirme."],
 ["Diversification ratio", "Çeşitlendirme oranı", "The risk of an equally weighted portfolio divided by the risk of a single security in it.", "Eşit ağırlıklı portföyün riskinin içindeki tek bir menkul kıymetin riskine bölümü."],
 ["Investment policy statement (IPS)", "Yatırım politikası belgesi", "A written document setting out the client's objectives, constraints and the manager's guidelines.", "Müşterinin hedeflerini, kısıtlarını ve yöneticinin yönergelerini belirleyen yazılı belge."],
 ["Defined benefit pension plan", "Tanımlanmış fayda emeklilik planı", "A plan in which the employer promises a specified retirement benefit.", "İşverenin belirli bir emeklilik faydası taahhüt ettiği plan."],
 ["Endowment", "Vakıf fonu", "A long-term fund owned by a non-profit institution, such as a university.", "Üniversite gibi kâr amacı gütmeyen bir kuruma ait uzun vadeli fon."],
 ["Sovereign wealth fund", "Varlık fonu (devlet yatırım fonu)", "A government-owned investment fund.", "Devlete ait yatırım fonu."],
 ["Open-end fund", "Açık uçlu fon", "A fund that issues and redeems shares at net asset value.", "Payları net varlık değerinden ihraç eden ve geri alan fon."],
 ["Closed-end fund", "Kapalı uçlu fon", "A fund with a fixed number of shares that trade on an exchange, possibly at a premium or discount to net asset value.", "Sabit sayıda payı borsada işlem gören ve net varlık değerine göre primli veya iskontolu işlem görebilen fon."],
 ["Exchange-traded fund (ETF)", "Borsa yatırım fonu", "A fund whose shares trade on an exchange and stay close to net asset value through creation and redemption by authorized participants.", "Payları borsada işlem gören ve yetkili katılımcıların yaratma ve geri alma işlemleriyle net varlık değerine yakın kalan fon."],
],
notes="""<h3>The portfolio approach</h3>
<ul>
<li>Combining assets with less-than-perfect correlation reduces risk without proportionally reducing return. Diversification does not protect much in a crisis, when correlations rise.</li>
<li><b>Diversification ratio</b> = risk of the equally weighted portfolio / risk of a single security. Lower means more benefit.</li>
</ul>
<h3>The process</h3>
<ul>
<li><b>Planning:</b> understand the client, write the IPS, form capital market expectations.</li>
<li><b>Execution:</b> asset allocation, security analysis, portfolio construction and trading.</li>
<li><b>Feedback:</b> monitor and rebalance, measure and report performance.</li>
</ul>
<h3>Types of investor</h3>
<div class="tbl"><table>
<tr><th>Investor</th><th>Horizon</th><th>Risk tolerance</th><th>Liquidity needs</th></tr>
<tr><td>Individuals</td><td>Varies</td><td>Varies</td><td>Varies</td></tr>
<tr><td>Defined benefit plans</td><td>Long</td><td>High (depends on funding)</td><td>Low (rises as members retire)</td></tr>
<tr><td>Endowments and foundations</td><td>Very long</td><td>High</td><td>Low to moderate</td></tr>
<tr><td>Banks</td><td>Short</td><td>Low</td><td>High</td></tr>
<tr><td>Life insurers</td><td>Long</td><td>Low</td><td>Moderate</td></tr>
<tr><td>Property and casualty insurers</td><td>Short</td><td>Low</td><td>High</td></tr>
<tr><td>Sovereign wealth funds</td><td>Long</td><td>High</td><td>Low</td></tr>
</table></div>
<ul>
<li>In a <b>defined contribution</b> plan, the employee bears the investment risk and makes the decisions.</li>
</ul>
<h3>Pooled products</h3>
<ul>
<li><b>Open-end funds</b>: new money creates shares at net asset value; redemptions may force sales.</li>
<li><b>Closed-end funds</b>: fixed shares trade on an exchange, often at a discount or premium to net asset value.</li>
<li><b>ETFs</b>: trade all day; in-kind creation and redemption by authorized participants keeps the price close to net asset value and is tax-efficient.</li>
<li>Also: separately managed accounts, hedge funds, private equity funds, and target-date funds.</li>
</ul>
<div class="trap"><b>Exam trap</b>Property and casualty insurers have shorter horizons and higher liquidity needs than life insurers, because claims are less predictable.</div>""",
qs=[
 ["The correct order of the steps in the portfolio management process is:", ["execution, planning, feedback.", "planning, execution, feedback.", "feedback, planning, execution."], 1, "The manager first plans (IPS and expectations), then executes, then monitors and reviews."],
 ["Compared with a bank, a university endowment typically has:", ["a shorter horizon and lower risk tolerance.", "a longer horizon and higher risk tolerance.", "higher liquidity needs."], 1, "Endowments aim to support the institution in perpetuity and can take long-term risk."],
 ["Which institutional investor typically has the highest liquidity needs?", ["A sovereign wealth fund", "A university endowment", "A property and casualty insurer"], 2, "Claims can arise suddenly and are hard to predict, so liquidity needs are high."],
 ["Compared with an open-end mutual fund, a closed-end fund:", ["can trade at a premium or discount to net asset value.", "issues new shares whenever investors buy.", "always trades at net asset value."], 0, "Its fixed number of shares trades on an exchange at a market-determined price."],
 ["The price of an ETF stays close to its net asset value mainly because:", ["the manager guarantees it.", "authorized participants can create and redeem shares.", "it trades only once a day."], 1, "Arbitrage through in-kind creation and redemption closes gaps between price and NAV."],
 ["A portfolio's diversification ratio is 0.6. This means the equally weighted portfolio's risk is:", ["60% of the risk of a single security.", "60% higher than a single security.", "uncorrelated with the market."], 0, "The ratio compares portfolio risk with single-security risk; lower values indicate more diversification."],
 ["In a defined contribution pension plan, investment risk is borne by the:", ["employee.", "employer.", "pension regulator."], 0, "The employee's benefit depends on contributions and investment results."],
 ["Writing the investment policy statement belongs to which step of the portfolio management process?", ["Planning", "Execution", "Feedback"], 0, "The IPS is prepared during planning, before assets are allocated."],
]))

R.append(dict(id="pl", n="Basics of Portfolio Planning and Construction", k="PLANNING", w=3, c="#8a5cc2",
terms=[
 ["Return objective", "Getiri hedefi", "The return the investor needs or wants, stated in absolute or relative terms.", "Yatırımcının ihtiyaç duyduğu veya istediği, mutlak ya da göreli olarak ifade edilen getiri."],
 ["Ability to take risk", "Risk alma kapasitesi", "The investor's financial capacity to bear losses, based on horizon, wealth and income.", "Ufuk, servet ve gelire dayalı olarak yatırımcının kayıplara katlanma finansal kapasitesi."],
 ["Willingness to take risk", "Risk alma isteği", "The investor's attitude to risk.", "Yatırımcının riske karşı tutumu."],
 ["Investment constraints", "Yatırım kısıtları", "Limits on investment choices: liquidity, time horizon, tax, legal and regulatory, and unique circumstances.", "Yatırım tercihlerine konan sınırlar: likidite, zaman ufku, vergi, hukuki ve düzenleyici unsurlar, özel durumlar."],
 ["Strategic asset allocation", "Stratejik varlık dağılımı", "The long-term target weights of asset classes set to meet the investor's objectives.", "Yatırımcının hedeflerini karşılamak için belirlenen uzun vadeli varlık sınıfı ağırlıkları."],
 ["Tactical asset allocation", "Taktik varlık dağılımı", "Short-term deviations from strategic weights to exploit expected opportunities.", "Beklenen fırsatlardan yararlanmak için stratejik ağırlıklardan kısa süreli sapmalar."],
 ["Rebalancing", "Yeniden dengeleme", "Trading to return a portfolio to its target weights.", "Portföyü hedef ağırlıklarına döndürmek için işlem yapma."],
 ["Core-satellite", "Çekirdek-uydu yaklaşımı", "A passive or low-risk core portfolio combined with active satellite positions.", "Pasif veya düşük riskli bir çekirdek portföyün aktif uydu pozisyonlarla birleştirilmesi."],
 ["Exclusionary screening", "Dışlayıcı tarama", "Removing companies or sectors from the investable universe for ethical or ESG reasons.", "Etik veya ÇSY gerekçeleriyle şirketleri ya da sektörleri yatırım evreninden çıkarma."],
],
notes="""<h3>Investment policy statement</h3>
<ul>
<li>Typical contents: client description, purpose, duties of the parties, objectives and constraints, review schedule, performance measures and benchmarks, rebalancing policy, and any ESG preferences.</li>
<li>Reviewed at least annually, and whenever the client's circumstances change.</li>
</ul>
<h3>Objectives</h3>
<ul>
<li><b>Return:</b> absolute (for example 7% a year) or relative to a benchmark; must be consistent with risk.</li>
<li><b>Risk:</b> ability and willingness. When they conflict, the adviser generally follows the <b>lower</b> of the two, and may educate the client if willingness is unrealistically low.</li>
</ul>
<h3>Constraints</h3>
<ul>
<li><b>Liquidity:</b> expected and unexpected cash needs.</li>
<li><b>Time horizon:</b> may have several stages.</li>
<li><b>Tax:</b> affects asset location and choice of investments.</li>
<li><b>Legal and regulatory:</b> for example, restrictions on pension funds or insider holdings.</li>
<li><b>Unique circumstances:</b> personal or ethical preferences, concentrated holdings.</li>
</ul>
<h3>Asset allocation</h3>
<ul>
<li>Asset classes should be internally similar (high correlations within) and distinct from each other (low correlations between).</li>
<li><b>Strategic</b> allocation sets long-term weights and largely determines the variability of returns. <b>Tactical</b> allocation deviates temporarily. <b>Security selection</b> deviates within an asset class.</li>
<li>Rebalancing back to targets can be calendar-based or within permitted ranges.</li>
<li><b>Risk budgeting</b> allocates the total risk the investor can bear among active strategies.</li>
<li><b>Core-satellite:</b> an indexed core with active satellites.</li>
</ul>
<h3>ESG integration</h3>
<ul>
<li>Approaches: negative (exclusionary) screening, positive (best-in-class) screening, ESG integration into analysis, thematic investing, impact investing, and active ownership (engagement and proxy voting).</li>
</ul>
<div class="trap"><b>Exam trap</b>The return objective is an objective, not a constraint. The five constraints are liquidity, horizon, tax, legal and regulatory, and unique circumstances.</div>""",
qs=[
 ["A young, wealthy client with a long horizon and stable income says she is very uncomfortable with any loss. Her overall risk tolerance should most likely be considered:", ["high, based on her ability.", "below average, based on her willingness.", "the average of the two."], 1, "When ability and willingness differ, the adviser generally follows the lower and discusses it with the client."],
 ["Which of the following is an investment constraint, not an objective?", ["Return requirement", "Risk tolerance", "Time horizon"], 2, "Return and risk are objectives; horizon is one of the constraints."],
 ["Long-term target weights for each asset class set to meet a client's objectives are the:", ["tactical asset allocation.", "strategic asset allocation.", "security selection policy."], 1, "Strategic allocation reflects long-term goals and capital market expectations."],
 ["A manager temporarily overweights equities because she expects them to outperform over the next six months. This is:", ["rebalancing.", "tactical asset allocation.", "strategic asset allocation."], 1, "Short-term deviations from strategic weights are tactical decisions."],
 ["Asset classes used in strategic allocation should ideally have:", ["high correlations between classes.", "low correlations within each class.", "high correlations within each class and low correlations between classes."], 2, "Each class should be internally similar and distinct from the others."],
 ["A portfolio that combines a low-cost index fund with several actively managed specialist funds follows a:", ["core-satellite approach.", "tactical approach.", "liability-driven approach."], 0, "The passive core is supplemented by active satellites."],
 ["Excluding tobacco and weapons manufacturers from a portfolio is an example of:", ["impact investing.", "thematic investing.", "exclusionary screening."], 2, "Negative or exclusionary screening removes companies or sectors from the universe."],
 ["An investment policy statement should be reviewed:", ["only when markets fall.", "only at the client's request.", "at least annually and when circumstances change."], 2, "Regular review keeps the IPS aligned with the client's situation."],
]))

R.append(dict(id="bb", n="The Behavioral Biases of Individuals", k="BEHAVIOR", w=3, c="#b8860b",
terms=[
 ["Cognitive error", "Bilişsel hata", "A bias from faulty reasoning, memory or information processing; easier to correct.", "Hatalı akıl yürütme, bellek veya bilgi işlemeden kaynaklanan yanlılık; düzeltilmesi daha kolaydır."],
 ["Emotional bias", "Duygusal yanlılık", "A bias from feelings or impulses; harder to correct and often accommodated.", "Duygu veya dürtülerden kaynaklanan yanlılık; düzeltilmesi daha zordur ve çoğu zaman uyum sağlanır."],
 ["Conservatism bias", "Tutuculuk yanlılığı", "Holding on to prior views and under-reacting to new information.", "Önceki görüşlere bağlı kalıp yeni bilgiye yetersiz tepki verme."],
 ["Confirmation bias", "Doğrulama yanlılığı", "Seeking information that supports existing beliefs.", "Mevcut inançları destekleyen bilgiyi arama."],
 ["Representativeness bias", "Temsiliyet yanlılığı", "Judging by similarity to familiar categories and ignoring base rates.", "Bilinen kategorilere benzerliğe göre yargıda bulunup temel oranları göz ardı etme."],
 ["Anchoring", "Çapalama", "Relying too much on an initial reference point, such as a purchase price.", "Alış fiyatı gibi ilk referans noktasına aşırı bağlı kalma."],
 ["Mental accounting", "Zihinsel muhasebe", "Treating money differently depending on its source or intended use.", "Parayı kaynağına veya kullanım amacına göre farklı değerlendirme."],
 ["Framing bias", "Çerçeveleme yanlılığı", "Making different decisions depending on how the same information is presented.", "Aynı bilgi farklı sunulduğunda farklı kararlar verme."],
 ["Availability bias", "Erişilebilirlik yanlılığı", "Overweighting information that is easy to recall.", "Kolay hatırlanan bilgiye aşırı ağırlık verme."],
 ["Loss aversion", "Kayıptan kaçınma", "Feeling losses more strongly than equal gains.", "Kayıpları eşit kazançlardan daha güçlü hissetme."],
 ["Overconfidence bias", "Aşırı güven yanlılığı", "Overestimating one's own knowledge and ability.", "Kendi bilgi ve yeteneğini olduğundan fazla değerlendirme."],
 ["Status quo bias", "Statüko yanlılığı", "Preferring to do nothing and keep the current situation.", "Hiçbir şey yapmamayı ve mevcut durumu korumayı tercih etme."],
 ["Endowment bias", "Sahiplik yanlılığı", "Valuing an asset more because one owns it.", "Bir varlığa sahip olunduğu için ona daha fazla değer verme."],
 ["Regret aversion", "Pişmanlıktan kaçınma", "Avoiding decisions for fear of later regret.", "Sonradan pişman olma korkusuyla karar vermekten kaçınma."],
],
notes="""<h3>Two types</h3>
<div class="tbl"><table>
<tr><th></th><th>Cognitive errors</th><th>Emotional biases</th></tr>
<tr><td>Source</td><td>Faulty reasoning or information processing</td><td>Feelings, impulses, intuition</td></tr>
<tr><td>Response</td><td>Correct with education and better information</td><td>Often accommodate; hard to change</td></tr>
</table></div>
<h3>Cognitive errors</h3>
<ul>
<li><b>Belief perseverance:</b> conservatism, confirmation, representativeness, illusion of control (believing one can influence outcomes), hindsight (believing past events were predictable).</li>
<li><b>Processing errors:</b> anchoring and adjustment, mental accounting, framing, availability.</li>
</ul>
<h3>Emotional biases</h3>
<ul>
<li><b>Loss aversion:</b> holding losers too long and selling winners too early (the disposition effect).</li>
<li><b>Overconfidence:</b> trading too much, holding concentrated portfolios, underestimating risk.</li>
<li><b>Self-control:</b> favouring spending today over saving for long-term goals.</li>
<li><b>Status quo:</b> inertia, keeping inappropriate allocations.</li>
<li><b>Endowment:</b> reluctance to sell inherited or long-held assets.</li>
<li><b>Regret aversion:</b> herding with the crowd, staying too conservative after a loss.</li>
</ul>
<h3>Effects on markets</h3>
<ul>
<li>Biases may explain momentum, bubbles and crashes, and the value effect, although many anomalies also have risk-based explanations.</li>
</ul>
<div class="trap"><b>Exam trap</b>Anchoring, mental accounting, framing and availability are cognitive errors, not emotional ones, even though they sound like feelings.</div>""",
qs=[
 ["An investor refuses to sell a share until it returns to the price she paid for it. She is most likely exhibiting:", ["anchoring.", "availability bias.", "representativeness bias."], 0, "The purchase price acts as an irrelevant reference point."],
 ["An investor keeps a separate 'fun money' account that he invests far more aggressively than the rest of his savings. This is:", ["framing bias.", "mental accounting.", "overconfidence bias."], 1, "He treats money differently depending on the label he gives it."],
 ["An investor assumes that a company with a strong brand must be a good investment, ignoring its high valuation. This is most likely:", ["anchoring.", "representativeness bias.", "regret aversion."], 1, "The investor judges by resemblance to a 'good company' stereotype and ignores other information."],
 ["Compared with cognitive errors, emotional biases are generally:", ["easier to correct.", "harder to correct.", "irrelevant to investment decisions."], 1, "Because they stem from feelings, advisers often need to accommodate them."],
 ["An investor holds on to losing positions too long and sells winners too soon. The bias most associated with this behaviour is:", ["loss aversion.", "mental accounting.", "illusion of control."], 0, "The pain of realizing losses leads to the disposition effect."],
 ["An investor who trades frequently because he believes he can consistently pick winners most likely suffers from:", ["status quo bias.", "endowment bias.", "overconfidence bias."], 2, "Overconfident investors overestimate their skill and trade too much."],
 ["An investor who inherited a portfolio from her father refuses to change it, even though it is unsuitable for her. This most likely reflects:", ["endowment bias.", "framing bias.", "hindsight bias."], 0, "She places extra value on assets she owns, especially inherited ones."],
 ["Which of the following is classified as a cognitive error?", ["Availability bias", "Self-control bias", "Regret aversion"], 0, "Availability is a processing error; the other two are emotional biases."],
]))

R.append(dict(id="rm", n="Introduction to Risk Management", k="RISK MGMT", w=2, c="#2f8f5b",
terms=[
 ["Risk management", "Risk yönetimi", "The process of identifying, measuring and controlling risks to achieve objectives.", "Hedeflere ulaşmak için riskleri belirleme, ölçme ve kontrol etme süreci."],
 ["Risk governance", "Risk yönetişimi", "The top-down process, led by the board, that sets risk policy and oversight.", "Yönetim kurulu önderliğinde risk politikasını ve gözetimini belirleyen yukarıdan aşağıya süreç."],
 ["Risk tolerance", "Risk toleransı", "The amount of risk an organization is willing and able to accept.", "Bir kurumun kabul etmeye istekli ve muktedir olduğu risk miktarı."],
 ["Risk budgeting", "Risk bütçelemesi", "Allocating the organization's total risk across activities or investments.", "Kurumun toplam riskinin faaliyetlere veya yatırımlara dağıtılması."],
 ["Financial risks", "Finansal riskler", "Risks from financial markets: market, credit and liquidity risk.", "Finansal piyasalardan kaynaklanan riskler: piyasa, kredi ve likidite riski."],
 ["Non-financial risks", "Finansal olmayan riskler", "Risks from operations, people, systems, law and the environment.", "Faaliyetlerden, insanlardan, sistemlerden, hukuktan ve çevreden kaynaklanan riskler."],
 ["Operational risk", "Operasyonel risk", "The risk of loss from failed processes, people, systems or external events.", "Başarısız süreçlerden, insanlardan, sistemlerden veya dış olaylardan kaynaklanan kayıp riski."],
 ["Model risk", "Model riski", "The risk that a model is wrong or used wrongly.", "Bir modelin yanlış olması veya yanlış kullanılması riski."],
 ["Risk transfer", "Risk transferi", "Passing risk to another party, typically through insurance.", "Riskin genellikle sigorta yoluyla başka bir tarafa aktarılması."],
 ["Risk shifting", "Risk kaydırma", "Changing the distribution of outcomes, typically with derivatives.", "Sonuçların dağılımını genellikle türev araçlarla değiştirme."],
],
notes="""<h3>The framework</h3>
<ul>
<li>Governance, identification and measurement of risks, infrastructure, policies and processes, monitoring and mitigation, communication, and strategic analysis.</li>
<li><b>Risk governance</b> starts with the board: it sets risk tolerance consistent with the organization's goals, often through a risk committee and a chief risk officer.</li>
<li>Risk management does not mean minimizing risk; it means taking the right amount of the right risks.</li>
</ul>
<h3>Risk tolerance and budgeting</h3>
<ul>
<li>Tolerance reflects both the ability to absorb losses and the appetite for risk.</li>
<li><b>Risk budgeting</b> allocates that tolerance across activities, for example by setting limits on volatility, beta or value at risk, or by allocating to risk factors.</li>
</ul>
<h3>Types of risk</h3>
<div class="tbl"><table>
<tr><th>Financial</th><th>Non-financial</th></tr>
<tr><td>Market: prices, rates, currencies</td><td>Operational, including cyber risk</td></tr>
<tr><td>Credit: default of borrowers and counterparties</td><td>Settlement, legal, compliance and regulatory</td></tr>
<tr><td>Liquidity: selling only at a large discount</td><td>Model, tail, accounting, tax, solvency</td></tr>
</table></div>
<ul>
<li>Individuals face mortality risk (dying early), longevity risk (outliving savings) and morbidity risk (illness).</li>
<li>Risks interact: a market fall can trigger credit and liquidity problems at the same time.</li>
</ul>
<h3>Measuring and responding</h3>
<ul>
<li>Measures: standard deviation, beta, duration, delta and other option sensitivities, value at risk, conditional VaR, scenario analysis and stress tests.</li>
<li>Responses: <b>accept</b> (self-insure or diversify), <b>avoid</b> (do not undertake the activity), <b>prevent or mitigate</b>, <b>transfer</b> (insurance) or <b>shift</b> (derivatives).</li>
</ul>
<div class="trap"><b>Exam trap</b>Insurance transfers risk; derivatives shift it. Choosing to self-insure is a form of risk acceptance.</div>""",
qs=[
 ["Within an organization, overall risk tolerance should be set by the:", ["board of directors.", "trading desk.", "external auditor."], 0, "Risk governance is a top-down responsibility led by the board."],
 ["Allocating an organization's total risk across its various investment activities is:", ["risk shifting.", "risk budgeting.", "risk avoidance."], 1, "Risk budgeting distributes the available risk to where it is expected to be most rewarded."],
 ["The risk that a company's computer systems are disrupted by a cyberattack is best classified as:", ["market risk.", "liquidity risk.", "operational risk."], 2, "Losses from failed systems and external events are operational risk."],
 ["Buying an insurance policy against fire damage is an example of risk:", ["transfer.", "shifting.", "acceptance."], 0, "Insurance passes the risk to the insurer."],
 ["Using put options to limit the downside of an equity portfolio is an example of risk:", ["transfer.", "shifting.", "avoidance."], 1, "Derivatives change the distribution of outcomes, which is risk shifting."],
 ["The risk that a retiree outlives her savings is:", ["mortality risk.", "longevity risk.", "morbidity risk."], 1, "Longevity risk is the risk of living longer than resources last."],
 ["The goal of risk management is best described as:", ["eliminating all risk.", "minimizing risk at any cost.", "taking the appropriate amount and type of risk."], 2, "Risk is accepted where it is expected to be rewarded and consistent with tolerance."],
 ["A company decides to keep a risk on its own balance sheet because the cost of insuring it exceeds the expected loss. This is:", ["risk acceptance.", "risk transfer.", "risk avoidance."], 0, "Self-insuring is a decision to accept the risk."],
]))
