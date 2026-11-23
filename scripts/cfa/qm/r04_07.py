# CFA Level I · Quantitative Methods · readings 4–7. Original study notes and questions.
R = []

R.append(dict(id="pt", n="Probability Trees and Conditional Expectations", k="PROBABILITY", w=2, c="#8a5cc2",
terms=[
 ["Expected value", "Beklenen değer", "The probability-weighted average of all possible outcomes of a random variable.", "Bir rassal değişkenin tüm olası sonuçlarının olasılık ağırlıklı ortalaması."],
 ["Random variable", "Rassal değişken", "A quantity whose future value is uncertain.", "Gelecekteki değeri belirsiz olan büyüklük."],
 ["Unconditional probability", "Koşulsuz olasılık", "The probability of an event regardless of any other event; also called marginal probability.", "Bir olayın, başka hiçbir olaya bağlı olmaksızın olasılığı; marjinal olasılık da denir."],
 ["Conditional probability", "Koşullu olasılık", "The probability of an event given that another event has occurred.", "Başka bir olayın gerçekleştiği bilindiğinde bir olayın olasılığı."],
 ["Joint probability", "Bileşik olasılık", "The probability that two events both occur.", "İki olayın birlikte gerçekleşme olasılığı."],
 ["Conditional expected value", "Koşullu beklenen değer", "The expected value of a random variable given a particular scenario.", "Belirli bir senaryo veri alındığında rassal değişkenin beklenen değeri."],
 ["Total probability rule", "Toplam olasılık kuralı", "Expresses an unconditional probability or expected value as the weighted sum of conditional ones over mutually exclusive and exhaustive scenarios.", "Koşulsuz bir olasılığı veya beklenen değeri, birbirini dışlayan ve tüm durumları kapsayan senaryolardaki koşullu değerlerin ağırlıklı toplamı olarak ifade eder."],
 ["Probability tree", "Olasılık ağacı", "A diagram whose branches show scenarios, their probabilities and the outcomes that follow.", "Dalları senaryoları, olasılıklarını ve izleyen sonuçları gösteren diyagram."],
 ["Prior probability", "Önsel olasılık", "The probability assigned to an event before new information arrives.", "Yeni bilgi gelmeden önce bir olaya verilen olasılık."],
 ["Posterior probability", "Sonsal olasılık", "The updated probability of an event after taking new information into account.", "Yeni bilgi hesaba katıldıktan sonra olayın güncellenmiş olasılığı."],
 ["Bayes' formula", "Bayes formülü", "A rule for reversing a conditional probability: it turns the probability of the information given the event into the probability of the event given the information.", "Koşullu olasılığı tersine çeviren kural: olay veri alındığında bilginin olasılığını, bilgi veri alındığında olayın olasılığına dönüştürür."],
],
notes="""<h3>Expected value and variance</h3>
<p class="f">E(X) = Σ P(X<sub>i</sub>) × X<sub>i</sub></p>
<p class="f">σ²(X) = Σ P(X<sub>i</sub>) × [X<sub>i</sub> − E(X)]²</p>
<ul>
<li>The expected value is a forecast, the centre of the possible outcomes. Variance and its square root, standard deviation, measure how widely the outcomes are spread around that forecast.</li>
<li>These are forward-looking, probability-weighted figures. Sample statistics in the previous reading weight every past observation equally.</li>
</ul>
<h3>Conditional expectations</h3>
<ul>
<li>A <b>conditional expected value</b> is the forecast given that a particular scenario occurs, for example expected earnings given that interest rates fall.</li>
<li>The <b>total probability rule for expected value</b> rebuilds the overall forecast from the scenario forecasts:</li>
</ul>
<p class="f">E(X) = E(X | S<sub>1</sub>) × P(S<sub>1</sub>) + E(X | S<sub>2</sub>) × P(S<sub>2</sub>) + … + E(X | S<sub>n</sub>) × P(S<sub>n</sub>)</p>
<ul>
<li>The scenarios must be <b>mutually exclusive</b> (only one can happen) and <b>exhaustive</b> (together they cover every possibility), so their probabilities sum to 1.</li>
</ul>
<h3>Reading a probability tree</h3>
<ul>
<li>The first set of branches carries unconditional probabilities of the scenarios. The second set carries conditional probabilities, given the branch they grow from.</li>
<li>Multiply along a path to get a <b>joint probability</b>. The joint probabilities at the ends of all paths sum to 1.</li>
<li>To get the unconditional probability of an outcome, add the joint probabilities of every path that leads to it.</li>
</ul>
<p class="f">P(A and B) = P(A | B) × P(B)</p>
<p class="f">P(A) = P(A | S<sub>1</sub>)P(S<sub>1</sub>) + … + P(A | S<sub>n</sub>)P(S<sub>n</sub>)</p>
<h3>Bayes' formula: updating a belief</h3>
<p class="f">P(event | information) = P(information | event) × P(event) / P(information)</p>
<ul>
<li>Start with a <b>prior</b> probability of the event. New information arrives. The formula gives the <b>posterior</b> probability.</li>
<li>The denominator, the unconditional probability of the information, comes from the total probability rule.</li>
<li>Practical method: draw the tree, compute the joint probability of each path, then divide the path you are interested in by the sum of all paths that contain the observed information.</li>
</ul>
<div class="trap"><b>Exam trap</b>P(A | B) and P(B | A) are different numbers. A question that gives "probability of a strong report given a good company" and asks for "probability of a good company given a strong report" is asking for Bayes' formula.</div>
<h3>Worked pattern</h3>
<ul>
<li>30% of companies in a sector are high quality. High-quality companies beat forecasts 80% of the time, the others 40% of the time.</li>
<li>P(beat) = 0.30 × 0.80 + 0.70 × 0.40 = 0.24 + 0.28 = 0.52.</li>
<li>P(high quality | beat) = 0.24 / 0.52 = 46.2%. One good result lifts the probability from 30% to about 46%, not to 80%.</li>
</ul>""",
qs=[
 ["A share has a 25% probability of returning 20%, a 50% probability of returning 10% and a 25% probability of returning −8%. Its expected return is closest to:", ["7.3%", "8.0%", "10.0%"], 1, "0.25 × 20 + 0.50 × 10 + 0.25 × (−8) = 5 + 5 − 2 = 8.0%. The simple average of the three outcomes is 7.3%, which ignores the probabilities."],
 ["A share has a 25% probability of returning 20%, a 50% probability of returning 10% and a 25% probability of returning −8%. The standard deviation of its return is closest to:", ["8.9%", "10.1%", "11.7%"], 1, "The expected return is 8%. Variance = 0.25 × 12² + 0.50 × 2² + 0.25 × (−16)² = 36 + 2 + 64 = 102. The square root is 10.1%."],
 ["An analyst assigns a 40% probability to a rate cut. Expected earnings per share are $5.00 if rates are cut and $3.00 if they are not. The unconditional expected earnings per share are closest to:", ["$3.80", "$4.00", "$4.20"], 0, "0.40 × 5.00 + 0.60 × 3.00 = 2.00 + 1.80 = $3.80. $4.00 treats the two scenarios as equally likely."],
 ["In a sector, 30% of companies are high quality. High-quality companies beat earnings forecasts 80% of the time and other companies 40% of the time. Given that a company beat its forecast, the probability that it is high quality is closest to:", ["30.0%", "46.2%", "80.0%"], 1, "P(beat) = 0.30 × 0.80 + 0.70 × 0.40 = 0.52. P(high quality | beat) = 0.24 / 0.52 = 46.2%. The 80% figure is the conditional probability the other way round."],
 ["Bayes' formula is most appropriately used to:", ["update a prior probability when new information arrives.", "calculate the expected value of a discrete random variable.", "determine the number of ways a set of objects can be ordered."], 0, "Bayes' formula converts a prior probability into a posterior probability using the likelihood of the new information."],
 ["The probability of a strong economy is 60%. In a strong economy, earnings per share will be $4.00 with a probability of 70% and $3.00 with a probability of 30%. The expected earnings per share conditional on a strong economy are closest to:", ["$3.30", "$3.50", "$3.70"], 2, "0.70 × 4.00 + 0.30 × 3.00 = $3.70. The 60% probability of the scenario itself is not used, because the expectation is conditional on that scenario."],
 ["The probability of a strong economy is 60%. In a strong economy, there is a 30% probability that a company's earnings fall short of forecast. The joint probability of a strong economy and an earnings shortfall is closest to:", ["0.18", "0.30", "0.42"], 0, "Multiply along the branch: 0.60 × 0.30 = 0.18."],
 ["The probability of a recession next year is 20%. A bond's probability of default is 10% in a recession and 2% otherwise. The unconditional probability of default is closest to:", ["3.6%", "6.0%", "12.0%"], 0, "0.20 × 0.10 + 0.80 × 0.02 = 0.020 + 0.016 = 3.6%."],
 ["The probability of a recession next year is 20%. A bond's probability of default is 10% in a recession and 2% otherwise. Given that the bond defaulted, the probability that a recession occurred is closest to:", ["20.0%", "44.4%", "55.6%"], 2, "P(default) = 0.036. P(recession | default) = (0.20 × 0.10) / 0.036 = 0.020 / 0.036 = 55.6%."],
 ["For the total probability rule to apply, the set of scenarios must be:", ["independent and equally likely.", "mutually exclusive and exhaustive.", "conditional and normally distributed."], 1, "The scenarios must not overlap and must cover every possibility, so that their probabilities sum to 1."],
]))

R.append(dict(id="pm", n="Portfolio Mathematics", k="PORTFOLIO", w=2, c="#b8860b",
terms=[
 ["Portfolio weight", "Portföy ağırlığı", "The share of total portfolio value invested in a particular asset.", "Toplam portföy değerinin belirli bir varlığa yatırılan payı."],
 ["Portfolio expected return", "Portföyün beklenen getirisi", "The weighted average of the expected returns of the assets in the portfolio.", "Portföydeki varlıkların beklenen getirilerinin ağırlıklı ortalaması."],
 ["Covariance", "Kovaryans", "A measure of how two random variables move together; positive when they tend to move in the same direction.", "İki rassal değişkenin birlikte nasıl hareket ettiğinin ölçüsü; aynı yönde hareket etme eğilimindeyseler pozitiftir."],
 ["Covariance matrix", "Kovaryans matrisi", "A table of the covariances between every pair of assets, with variances on the diagonal.", "Her varlık çifti arasındaki kovaryansları gösteren tablo; köşegeninde varyanslar yer alır."],
 ["Correlation", "Korelasyon", "Covariance scaled by the two standard deviations; a unit-free measure of linear co-movement between −1 and +1.", "Kovaryansın iki standart sapmayla ölçeklenmiş hali; −1 ile +1 arasında, birimsiz bir doğrusal birlikte hareket ölçüsü."],
 ["Diversification", "Çeşitlendirme", "Reducing portfolio risk by combining assets that are less than perfectly correlated.", "Tam korelasyonlu olmayan varlıkları bir araya getirerek portföy riskini azaltma."],
 ["Joint probability function", "Bileşik olasılık fonksiyonu", "A table giving the probability of each combination of outcomes for two random variables.", "İki rassal değişkenin her sonuç bileşiminin olasılığını veren tablo."],
 ["Independence", "Bağımsızlık", "Two random variables are independent if knowing one tells nothing about the other; independent variables have zero covariance.", "Birini bilmek diğeri hakkında bilgi vermiyorsa iki rassal değişken bağımsızdır; bağımsız değişkenlerin kovaryansı sıfırdır."],
 ["Shortfall risk", "Hedefin altında kalma riski", "The probability that a portfolio's return or value falls below a stated minimum level.", "Portföy getirisinin veya değerinin belirlenen asgari düzeyin altına düşme olasılığı."],
 ["Safety-first ratio", "Önce güvenlik oranı", "Expected portfolio return minus the threshold return, divided by the portfolio's standard deviation.", "Portföyün beklenen getirisi ile eşik getiri arasındaki farkın portföyün standart sapmasına bölümü."],
],
notes="""<h3>Portfolio expected return</h3>
<p class="f">E(R<sub>p</sub>) = w<sub>1</sub>E(R<sub>1</sub>) + w<sub>2</sub>E(R<sub>2</sub>) + … + w<sub>n</sub>E(R<sub>n</sub>)</p>
<ul>
<li>Weights are market value proportions and sum to 1. The expected return is always a straight weighted average.</li>
</ul>
<h3>Portfolio variance</h3>
<p class="f">Two assets: σ²<sub>p</sub> = w<sub>1</sub>²σ<sub>1</sub>² + w<sub>2</sub>²σ<sub>2</sub>² + 2w<sub>1</sub>w<sub>2</sub>Cov(R<sub>1</sub>,R<sub>2</sub>)</p>
<p class="f">Cov(R<sub>1</sub>,R<sub>2</sub>) = ρ<sub>1,2</sub> × σ<sub>1</sub> × σ<sub>2</sub></p>
<ul>
<li>Risk is <b>not</b> a weighted average. It depends on how the assets move together.</li>
<li>If the correlation is +1, portfolio standard deviation equals the weighted average of the two standard deviations. For any correlation below +1 it is lower. That shortfall is the benefit of diversification.</li>
<li>The lower the correlation, the larger the risk reduction. At −1, a suitable choice of weights can remove risk entirely.</li>
</ul>
<h3>How many inputs?</h3>
<ul>
<li>A portfolio of n assets needs n expected returns, n variances and <b>n(n − 1)/2</b> distinct covariances.</li>
<li>The covariance matrix has n² cells: n variances on the diagonal and n(n − 1) off-diagonal covariances, each appearing twice because Cov(A,B) = Cov(B,A).</li>
<li>As n grows, the covariances come to dominate portfolio risk.</li>
</ul>
<h3>Covariance from a joint probability function</h3>
<p class="f">Cov(R<sub>A</sub>,R<sub>B</sub>) = Σ P(scenario) × [R<sub>A</sub> − E(R<sub>A</sub>)] × [R<sub>B</sub> − E(R<sub>B</sub>)]</p>
<ul>
<li>Compute each asset's expected return first, then weight the products of the deviations by the scenario probabilities.</li>
<li>If two variables are independent, their covariance and correlation are zero. The reverse does not always hold: zero correlation only rules out a linear relationship.</li>
</ul>
<h3>Shortfall risk and Roy's safety-first criterion</h3>
<p class="f">SFRatio = [E(R<sub>p</sub>) − R<sub>L</sub>] / σ<sub>p</sub></p>
<ul>
<li>R<sub>L</sub> is the minimum acceptable (threshold) return. The ratio counts how many standard deviations the expected return lies above the threshold.</li>
<li>The best portfolio under this rule is the one with the <b>highest</b> ratio, because it has the lowest probability of falling below the threshold.</li>
<li>If returns are normally distributed, the probability of shortfall is N(−SFRatio): the area in the left tail below that many standard deviations.</li>
<li>If the threshold is the risk-free rate, the safety-first ratio is the same as the Sharpe ratio.</li>
</ul>
<div class="trap"><b>Exam trap</b>Choosing the portfolio with the highest expected return or the lowest standard deviation alone is not the safety-first answer. Compute the ratio for each candidate.</div>""",
qs=[
 ["A portfolio has 60% in Asset A, with an expected return of 10%, and 40% in Asset B, with an expected return of 5%. The portfolio's expected return is closest to:", ["7.0%", "7.5%", "8.0%"], 2, "0.60 × 10 + 0.40 × 5 = 8.0%. The figure 7.5% is the simple average, which ignores the weights."],
 ["A portfolio has 60% in Asset A (standard deviation 20%) and 40% in Asset B (standard deviation 10%). The correlation between them is 0.3. The portfolio standard deviation is closest to:", ["12.65%", "13.74%", "16.00%"], 1, "Variance = 0.36 × 0.04 + 0.16 × 0.01 + 2 × 0.6 × 0.4 × 0.3 × 0.20 × 0.10 = 0.01888. The square root is 13.74%. The other figures correspond to correlations of 0 and +1."],
 ["The number of distinct covariances needed to compute the variance of a portfolio of 10 assets is:", ["45", "90", "100"], 0, "n(n − 1)/2 = 10 × 9 / 2 = 45. The matrix has 100 cells, of which 10 are variances and 90 are covariances that come in identical pairs."],
 ["Two assets have standard deviations of 20% and 30% and a correlation of 0.5. Their covariance is closest to:", ["0.015", "0.030", "0.060"], 1, "Covariance = 0.5 × 0.20 × 0.30 = 0.030."],
 ["An investor requires a minimum return of 3%. Portfolio A has an expected return of 8% and a standard deviation of 10%. Portfolio B has 10% and 16%. Portfolio C has 12% and 20%. Under Roy's safety-first criterion, the best choice is:", ["Portfolio A.", "Portfolio B.", "Portfolio C."], 0, "Safety-first ratios: A = (8 − 3)/10 = 0.50, B = (10 − 3)/16 = 0.44, C = (12 − 3)/20 = 0.45. The highest ratio, Portfolio A, has the lowest probability of falling below 3%."],
 ["When two assets with a correlation of less than +1 are combined, the portfolio's standard deviation is:", ["less than the weighted average of the two standard deviations.", "equal to the weighted average of the two standard deviations.", "greater than the weighted average of the two standard deviations."], 0, "Only at a correlation of exactly +1 does portfolio standard deviation equal the weighted average. Below +1, diversification reduces it."],
 ["There are two equally likely scenarios. In the first, Asset A returns 20% and Asset B returns 10%. In the second, Asset A returns 0% and Asset B returns 2%. The covariance of the two returns is closest to:", ["0.0020", "0.0040", "0.0080"], 1, "Expected returns are 10% and 6%. Covariance = 0.5 × (0.10)(0.04) + 0.5 × (−0.10)(−0.04) = 0.0040."],
 ["Shortfall risk is best described as the probability that a portfolio's return will:", ["be negative.", "fall below a specified minimum level.", "be lower than its expected return."], 1, "Shortfall risk is defined relative to a chosen threshold, which need not be zero or the expected return."],
 ["Two assets have the same standard deviation and a correlation of −1. An equally weighted portfolio of the two has a standard deviation:", ["of zero.", "equal to that of each asset.", "equal to half that of each asset."], 0, "With perfect negative correlation and equal volatility, equal weights make the movements offset exactly: σp = |0.5σ − 0.5σ| = 0."],
 ["A portfolio's returns are normally distributed and its safety-first ratio is 1.0. The probability that its return falls below the threshold is closest to:", ["15.9%", "34.1%", "84.1%"], 0, "The threshold lies one standard deviation below the mean. About 68.3% of a normal distribution lies within one standard deviation, leaving roughly 15.9% in the left tail."],
]))

R.append(dict(id="si", n="Simulation Methods", k="SIMULATION", w=1, c="#2f8f5b",
terms=[
 ["Lognormal distribution", "Lognormal dağılım", "The distribution of a variable whose natural logarithm is normally distributed; it cannot be negative and is skewed to the right.", "Doğal logaritması normal dağılan bir değişkenin dağılımı; negatif olamaz ve sağa çarpıktır."],
 ["Continuously compounded return", "Sürekli bileşik getiri", "The natural logarithm of the ratio of ending price to beginning price.", "Dönem sonu fiyatın dönem başı fiyata oranının doğal logaritması."],
 ["Independently and identically distributed (i.i.d.)", "Bağımsız ve özdeş dağılımlı", "Describes returns that do not depend on one another and are all drawn from the same distribution.", "Birbirine bağlı olmayan ve hepsi aynı dağılımdan gelen getirileri tanımlar."],
 ["Volatility", "Oynaklık (volatilite)", "The standard deviation of continuously compounded returns, usually stated on an annual basis.", "Sürekli bileşik getirilerin standart sapması; genellikle yıllık olarak ifade edilir."],
 ["Monte Carlo simulation", "Monte Carlo simülasyonu", "Generating many random outcomes from assumed probability distributions to estimate the distribution of a result.", "Varsayılan olasılık dağılımlarından çok sayıda rassal sonuç üreterek bir sonucun dağılımını tahmin etme."],
 ["Risk factor", "Risk faktörü", "An underlying variable, such as a share price or interest rate, whose uncertainty drives the value being studied.", "Belirsizliği incelenen değeri belirleyen, pay fiyatı veya faiz oranı gibi temel değişken."],
 ["Random number generator", "Rassal sayı üreteci", "An algorithm that produces numbers used to draw outcomes from a probability distribution.", "Bir olasılık dağılımından sonuç çekmek için kullanılan sayıları üreten algoritma."],
 ["Resampling", "Yeniden örnekleme", "Repeatedly drawing samples from the observed data set to learn about a statistic.", "Bir istatistik hakkında bilgi edinmek için gözlenen veri setinden tekrar tekrar örnek çekme."],
 ["Bootstrap", "Bootstrap (özyükleme)", "A resampling method that draws samples of the same size from the observed data with replacement.", "Gözlenen veriden aynı büyüklükte örnekleri yerine koyarak çeken yeniden örnekleme yöntemi."],
 ["Sampling with replacement", "Yerine koyarak örnekleme", "After an observation is drawn it is returned to the pool, so it can be drawn again.", "Çekilen gözlem havuza geri konur; böylece yeniden çekilebilir."],
],
notes="""<h3>Why the lognormal distribution</h3>
<ul>
<li>A share price cannot fall below zero, and it can rise without limit. A normal distribution allows negative values, so it is a poor model for prices.</li>
<li>If the continuously compounded return is normally distributed, the future price is <b>lognormally</b> distributed.</li>
<li>The lognormal distribution is bounded below by zero and skewed to the right.</li>
</ul>
<p class="f">P<sub>T</sub> = P<sub>0</sub> × e<sup>r</sup> &nbsp;&nbsp;&nbsp; r = ln(P<sub>T</sub> / P<sub>0</sub>)</p>
<h3>Continuously compounded returns over time</h3>
<ul>
<li>They add up: the return over a year is the sum of the daily continuously compounded returns.</li>
<li>If the periodic returns are independently and identically distributed, the mean scales with time and the standard deviation scales with the <b>square root</b> of time.</li>
</ul>
<p class="f">E(r<sub>T</sub>) = μ × T &nbsp;&nbsp;&nbsp; σ(r<sub>T</sub>) = σ × √T</p>
<ul>
<li>Example: a daily volatility of 1% with 250 trading days gives an annual volatility of 1% × √250 ≈ 15.8%.</li>
</ul>
<h3>Monte Carlo simulation</h3>
<ul>
<li>Use it when there is no formula for the answer: complex securities, path-dependent payoffs, portfolios with many interacting risks, retirement planning.</li>
<li>Steps:</li>
</ul>
<ul>
<li>1. State the quantity of interest in terms of its underlying risk factors.</li>
<li>2. Choose a probability distribution and parameters for each risk factor.</li>
<li>3. Draw random values for the risk factors.</li>
<li>4. Compute the quantity of interest for that draw.</li>
<li>5. Repeat many times; the mean of the results is the estimate, and their spread shows the range of outcomes.</li>
</ul>
<ul>
<li><b>Strength:</b> flexible, handles any distribution and any payoff, good for asking "what if" questions about assumptions.</li>
<li><b>Limits:</b> the answer is only as good as the assumed distributions and model. It gives a statistical estimate, not an exact result, and offers less insight into cause and effect than an analytical formula.</li>
</ul>
<h3>Bootstrap resampling</h3>
<ul>
<li>Instead of assuming a distribution, treat the observed sample as if it were the population.</li>
<li>Draw many resamples of the same size <b>with replacement</b>, compute the statistic for each, and study the distribution of those results.</li>
<li>Useful when no analytical formula for the statistic's standard error exists, or when the data do not follow a convenient distribution.</li>
<li>Limit: it can only reproduce what is in the observed sample. Events that never occurred in the data cannot appear in the resamples.</li>
</ul>
<div class="tbl"><table>
<tr><th></th><th>Monte Carlo</th><th>Bootstrap</th></tr>
<tr><td>Source of random draws</td><td>An assumed probability distribution</td><td>The observed data</td></tr>
<tr><td>Needs a distribution assumption</td><td>Yes</td><td>No</td></tr>
<tr><td>Main weakness</td><td>Wrong assumptions give wrong answers</td><td>Limited to history in the sample</td></tr>
</table></div>""",
qs=[
 ["Compared with a normal distribution, a lognormal distribution is:", ["symmetric and unbounded.", "skewed to the left and bounded above by zero.", "skewed to the right and bounded below by zero."], 2, "A lognormal variable cannot be negative and has a long right tail, which is why it suits asset prices."],
 ["If a share's continuously compounded return is normally distributed, the share's future price is best described as:", ["normally distributed.", "uniformly distributed.", "lognormally distributed."], 2, "The price is the exponential of a normal variable, and the exponential of a normal variable is lognormal."],
 ["A share priced at $50.00 earns a continuously compounded return of 10% a year for two years. Its price after two years is closest to:", ["$60.00", "$60.50", "$61.07"], 2, "50 × e^(0.10 × 2) = 50 × 1.2214 = $61.07. $60.50 uses annual compounding and $60.00 simple interest."],
 ["A limitation of Monte Carlo simulation is that it:", ["cannot be used for securities with complex payoffs.", "requires that all risk factors be normally distributed.", "provides statistical estimates rather than exact results."], 2, "Simulation is flexible about payoffs and distributions, but its output is an estimate whose quality depends on the assumptions and the number of trials."],
 ["In bootstrap resampling, each resample is drawn from the:", ["observed sample, with replacement.", "observed sample, without replacement.", "assumed probability distribution of the population."], 0, "Bootstrap treats the observed sample as the population and draws from it with replacement. Drawing from an assumed distribution describes Monte Carlo simulation."],
 ["The main difference between Monte Carlo simulation and bootstrap resampling is that Monte Carlo simulation:", ["uses only historical observations.", "produces a single outcome rather than a distribution.", "draws random values from a specified probability distribution."], 2, "Monte Carlo needs the analyst to specify distributions for the risk factors; bootstrap draws from the data itself."],
 ["Daily continuously compounded returns are independently and identically distributed with a standard deviation of 1%. Assuming 250 trading days, the annualized standard deviation is closest to:", ["5.0%", "15.8%", "25.0%"], 1, "Standard deviation scales with the square root of time: 1% × √250 ≈ 15.8%."],
 ["A share's continuously compounded returns in three consecutive weeks are 1.0%, 2.0% and −0.5%. The continuously compounded return for the three weeks is closest to:", ["2.49%", "2.50%", "2.53%"], 1, "Continuously compounded returns are additive: 1.0 + 2.0 − 0.5 = 2.50%."],
 ["The first step in a Monte Carlo simulation is to:", ["generate random numbers for each risk factor.", "calculate the mean of the simulated outcomes.", "specify the quantity of interest in terms of underlying risk factors."], 2, "The problem must be defined before any distributions are chosen or random numbers drawn."],
 ["A weakness of bootstrap resampling is that it:", ["requires the population to be normally distributed.", "cannot generate outcomes that are absent from the observed sample.", "can be applied only when an analytical formula for the statistic exists."], 1, "Because every resample is built from the observed data, outcomes that never appeared in the sample cannot be produced."],
]))

R.append(dict(id="ei", n="Estimation and Inference", k="SAMPLING", w=2, c="#d07a2a",
terms=[
 ["Population", "Ana kütle", "The complete set of items that share the characteristic being studied.", "İncelenen özelliği taşıyan tüm öğelerin oluşturduğu küme."],
 ["Parameter", "Parametre", "A numerical characteristic of a population, such as its mean.", "Ana kütlenin ortalama gibi sayısal bir özelliği."],
 ["Sample statistic", "Örneklem istatistiği", "A value computed from a sample and used to estimate a population parameter.", "Örneklemden hesaplanan ve ana kütle parametresini tahmin etmekte kullanılan değer."],
 ["Sampling error", "Örnekleme hatası", "The difference between a sample statistic and the population parameter it estimates.", "Örneklem istatistiği ile tahmin ettiği ana kütle parametresi arasındaki fark."],
 ["Simple random sampling", "Basit rassal örnekleme", "Every member of the population has the same chance of being selected.", "Ana kütlenin her üyesinin seçilme şansı eşittir."],
 ["Stratified random sampling", "Tabakalı rassal örnekleme", "The population is split into subgroups and a random sample is taken from each in proportion to its size.", "Ana kütle alt gruplara ayrılır ve her birinden büyüklüğüyle orantılı rassal örnek alınır."],
 ["Cluster sampling", "Küme örneklemesi", "The population is split into groups, some groups are chosen at random, and all or some members of those groups are sampled.", "Ana kütle gruplara ayrılır, bazı gruplar rassal seçilir ve bu grupların tüm üyeleri veya bir kısmı örneklenir."],
 ["Convenience sampling", "Kolayda örnekleme", "Selecting items because they are easy to reach; a non-probability method.", "Öğelerin kolay ulaşılabilir oldukları için seçilmesi; olasılığa dayanmayan bir yöntemdir."],
 ["Judgmental sampling", "Yargısal örnekleme", "Selecting items on the basis of the researcher's knowledge and experience; a non-probability method.", "Öğelerin araştırmacının bilgi ve deneyimine dayanarak seçilmesi; olasılığa dayanmayan bir yöntemdir."],
 ["Central limit theorem", "Merkezi limit teoremi", "For large samples, the distribution of the sample mean is approximately normal whatever the shape of the population, provided its variance is finite.", "Büyük örneklemlerde, varyansı sonlu olmak koşuluyla ana kütlenin şekli ne olursa olsun örneklem ortalamasının dağılımı yaklaşık normaldir."],
 ["Standard error of the sample mean", "Örneklem ortalamasının standart hatası", "The standard deviation of the distribution of sample means: the standard deviation divided by the square root of the sample size.", "Örneklem ortalamaları dağılımının standart sapması: standart sapmanın örneklem büyüklüğünün kareköküne bölümü."],
 ["Jackknife", "Jackknife (çakı) yöntemi", "A resampling method that recomputes a statistic leaving out one observation at a time.", "Her seferinde bir gözlemi dışarıda bırakarak istatistiği yeniden hesaplayan yeniden örnekleme yöntemi."],
],
notes="""<h3>Why sample</h3>
<ul>
<li>Examining a whole population is usually too costly or impossible. A sample statistic estimates the population parameter, and the gap between them is <b>sampling error</b>.</li>
</ul>
<h3>Sampling methods</h3>
<div class="tbl"><table>
<tr><th>Method</th><th>How it works</th><th>Note</th></tr>
<tr><td>Simple random</td><td>Every item has an equal chance of selection</td><td>Probability method</td></tr>
<tr><td>Systematic</td><td>Every k-th item is selected</td><td>Approximates simple random sampling</td></tr>
<tr><td>Stratified random</td><td>Split into strata by a characteristic, then sample randomly from <b>every</b> stratum in proportion to its size</td><td>More precise; used to build bond index portfolios</td></tr>
<tr><td>Cluster</td><td>Split into clusters, randomly pick <b>some</b> clusters, then sample all members (one-stage) or a random subset (two-stage)</td><td>Cheaper and quicker, less precise</td></tr>
<tr><td>Convenience</td><td>Take what is easy to obtain</td><td>Non-probability; may not be representative</td></tr>
<tr><td>Judgmental</td><td>Researcher hand-picks items</td><td>Non-probability; open to bias</td></tr>
</table></div>
<div class="trap"><b>Exam trap</b>Stratified sampling draws from every subgroup. Cluster sampling draws only from the subgroups that were randomly chosen.</div>
<h3>Central limit theorem</h3>
<ul>
<li>Take a population with mean μ and finite variance σ². For large samples (commonly n ≥ 30), the sample mean X̄:</li>
<li>is approximately <b>normally distributed</b>, whatever the population's own distribution,</li>
<li>has a mean equal to the population mean μ,</li>
<li>has a variance equal to σ² / n.</li>
<li>This is what allows confidence intervals and hypothesis tests about a mean even when the underlying data are not normal.</li>
</ul>
<h3>Standard error of the sample mean</h3>
<p class="f">σ<sub>X̄</sub> = σ / √n &nbsp;&nbsp;&nbsp; or, when σ is unknown, &nbsp; s<sub>X̄</sub> = s / √n</p>
<ul>
<li>It measures how much sample means vary from sample to sample. It falls as the sample grows, but only with the square root: four times the data halves the standard error.</li>
<li>Do not confuse it with the standard deviation, which measures dispersion of individual observations.</li>
</ul>
<h3>Resampling</h3>
<ul>
<li><b>Bootstrap:</b> draw many resamples of size n from the observed sample with replacement, compute the statistic each time. The standard deviation of those results estimates the statistic's standard error.</li>
</ul>
<p class="f">bootstrap standard error = √[ Σ(θ̂<sub>b</sub> − θ̄)² / (B − 1) ]</p>
<ul>
<li><b>Jackknife:</b> recompute the statistic n times, each time leaving out one observation, without replacement. It needs no random draws, so repeating it gives the same result every time. It is often used to reduce the bias of an estimator.</li>
<li>Bootstrap usually needs a computer and gives slightly different answers on each run; jackknife is simpler and deterministic.</li>
</ul>""",
qs=[
 ["An analyst divides a bond index into groups by maturity and credit rating and then randomly selects bonds from every group in proportion to its weight in the index. This method is best described as:", ["cluster sampling.", "systematic sampling.", "stratified random sampling."], 2, "Classifying the population into subgroups and sampling from every subgroup proportionally is stratified random sampling."],
 ["A sample of 100 observations has a standard deviation of 20. The standard error of the sample mean is closest to:", ["0.2", "2.0", "4.5"], 1, "Standard error = s / √n = 20 / 10 = 2.0."],
 ["According to the central limit theorem, for a large sample size the distribution of the sample mean is approximately normal:", ["only if the population is normally distributed.", "only if the population variance is known.", "regardless of the distribution of the population."], 2, "The theorem holds for any population with a finite variance, which is what makes it so useful."],
 ["A researcher divides a country into regions, randomly selects four regions and surveys every household in those four regions. This method is best described as:", ["cluster sampling.", "judgmental sampling.", "stratified random sampling."], 0, "Only the randomly chosen groups are sampled, which is cluster sampling. Stratified sampling would draw from every region."],
 ["An auditor selects the accounts to examine using her professional experience of where problems usually occur. This method is best described as:", ["judgmental sampling.", "convenience sampling.", "simple random sampling."], 0, "Selection based on the researcher's knowledge and experience is judgmental sampling, a non-probability method."],
 ["If the sample size is increased from 100 to 400, the standard error of the sample mean will:", ["fall to one-quarter of its previous value.", "fall to one-half of its previous value.", "remain unchanged."], 1, "The standard error is proportional to 1/√n. Quadrupling n doubles √n, so the standard error halves."],
 ["Which statement about the jackknife method is most accurate?", ["It draws resamples with replacement.", "It leaves out one observation at a time.", "It gives different results each time it is run."], 1, "The jackknife recomputes the statistic n times, each time omitting one observation, without replacement, so its results are repeatable."],
 ["The bootstrap estimate of the standard error of the sample mean is the:", ["mean of the resample standard deviations.", "standard deviation of the resample means.", "standard deviation of the original sample."], 1, "Each resample produces a mean; the standard deviation of those means estimates the standard error."],
 ["Sampling error is best described as the difference between:", ["two sample statistics drawn from the same population.", "a sample statistic and the population parameter it estimates.", "the standard deviation and the standard error of the sample mean."], 1, "Because a sample is only part of the population, its statistic will generally differ from the true parameter."],
 ["A population has a variance of 36. For samples of 9 observations, the variance of the sample mean is closest to:", ["2", "4", "12"], 1, "Variance of the sample mean = σ² / n = 36 / 9 = 4. Its square root, 2, is the standard error."],
]))
