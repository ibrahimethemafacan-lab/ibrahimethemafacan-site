# CFA Level I · Quantitative Methods · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
import re as _re
EK = {}

EK["rr"] = dict(
terms=[
 ["Gross return", "Brüt getiri", "Return before deducting management fees and other expenses.", "Yönetim ücretleri ve diğer giderler düşülmeden önceki getiri."],
 ["Real return", "Reel getiri", "Return adjusted for inflation; measures the increase in purchasing power.", "Enflasyona göre düzeltilmiş getiri; satın alma gücündeki artışı ölçer."],
],
notes="""<h3>More on returns</h3>
<p class="f">continuously compounded return = ln(P<sub>1</sub>/P<sub>0</sub>) = ln(1 + HPR) · EAR (continuous) = e<sup>r</sup> − 1</p>
<ul>
<li>For a positive return, HPR &gt; continuously compounded return; for a loss, the continuously compounded return is more negative.</li>
<li>The real risk-free rate reflects pure <b>time preference</b>. T-bill yields are nominal risk-free rates (they include expected inflation).</li>
<li>Required return ≈ real risk-free rate + inflation premium + default, liquidity and maturity premiums.</li>
<li>Arithmetic mean ≥ geometric mean ≥ harmonic mean; AM × HM = GM² for two values. Dollar-cost averaging buys shares at the harmonic mean price.</li>
<li>Gross return is before fees; net return is after fees. Real return measures purchasing power.</li>
<li><b>Money-weighted return</b> is the IRR of the investor's cash flows; it is affected by the timing of contributions. <b>Time-weighted return</b> removes that effect and is the industry standard for judging managers. If money is added before good periods, MWR exceeds TWR.</li>
</ul>""",
qs=[
 ["A share falls from $75 to $68. The continuously compounded return is closest to:", ["−10.3%", "−9.8%", "−9.3%"], 1, "ln(68/75) = −0.098."],
 ["The continuously compounded return equivalent to a one-year holding period return of −8% is closest to:", ["−8.7%", "−8.3%", "−7.7%"], 1, "ln(0.92) = −0.0834."],
 ["A stated rate of 7% compounded continuously gives an effective annual rate closest to:", ["7.00%", "7.19%", "7.25%"], 2, "e^0.07 − 1 = 7.25%."],
 ["A share is bought at $40, pays a dividend of $1.20 and is sold a year later at $46. The holding period return is:", ["15.0%", "18.0%", "21.0%"], 1, "(46 − 40 + 1.2)/40 = 18%."],
 ["A portfolio returned +2%, −30% and +25% over three years. Its geometric mean return is closest to:", ["−3.7%", "−1.0%", "+0.9%"], 0, "(1.02 × 0.70 × 1.25)^(1/3) − 1 = −3.7%."],
 ["An investor buys a share at $50, buys a second share a year later at $60, and sells both a year after that at $65. Each share pays a $2 dividend at the end of each year it is held. The money-weighted return is closest to:", ["15.7%", "17.7%", "19.7%"], 0, "IRR of −50, −58 (−60 + 2), +134 (130 + 4) is 15.7%."],
 ["For the investor above, the time-weighted return is closest to:", ["15.7%", "17.7%", "19.7%"], 1, "Year 1: 62/50 = 1.24; Year 2: 67/60 = 1.117. Geometric mean = 17.7%."],
 ["Which return measure best represents pure time preference?", ["The real risk-free rate", "The nominal risk-free rate", "The required return on equity"], 0, "It excludes inflation and risk premiums."],
 ["T-bill yields are best described as:", ["nominal risk-free rates, because they include an inflation premium.", "real risk-free rates.", "risky rates with a default premium."], 0, "They compensate for expected inflation."],
 ["A portfolio has a gross return of 8.0% and a net return of 7.2%. The difference most likely reflects:", ["fees.", "inflation.", "taxes on the investor."], 0, "Net return deducts management and other fees."],
 ["The most appropriate measure of the increase in a portfolio's purchasing power is its:", ["real return.", "gross return.", "after-tax nominal return."], 0, "Real returns adjust for inflation."],
 ["If an investor adds money just before a period of strong performance, the money-weighted return will most likely be:", ["higher than the time-weighted return.", "lower than the time-weighted return.", "equal to the time-weighted return."], 0, "More money earns the high return."],
 ["Time-weighted returns are preferred for evaluating managers because they:", ["are not affected by the timing of client cash flows.", "reflect the investor's actual wealth growth.", "are always higher."], 0, "Managers do not control contributions and withdrawals."],
 ["Computing the internal rate of return of a portfolio's inflows and outflows gives the:", ["money-weighted return.", "time-weighted return.", "geometric mean return."], 0, "MWR is an IRR."],
 ["For a set of different positive values, which ranking is correct?", ["Arithmetic mean > geometric mean > harmonic mean", "Harmonic mean > geometric mean > arithmetic mean", "Geometric mean > arithmetic mean > harmonic mean"], 0, "The means are equal only if all values are the same."],
 ["An investor buys $1,000 of a fund every month regardless of price. Her average cost per share equals the:", ["harmonic mean of the prices.", "arithmetic mean of the prices.", "geometric mean of the prices."], 0, "Dollar-cost averaging buys more shares when prices are low."],
 ["A share's price rose last year. Compared with its holding period return, its continuously compounded return is:", ["lower.", "higher.", "the same."], 0, "ln(1 + R) < R for R > 0."],
 ["Given a holding period return R, the continuously compounded return is:", ["ln(1 + R)", "e^R − 1", "ln(R)"], 0, "e^R − 1 converts the other way."],
])

EK["tv"] = dict(
notes="""<h3>More on time value</h3>
<ul>
<li>An annuity due pays at the start of each period: PV(due) = PV(ordinary) × (1 + r).</li>
<li>A deferred perpetuity's value at t = n − 1 is PMT / r; discount it back n − 1 periods.</li>
<li>Negative yields mean the zero-coupon bond's price is <b>above</b> face value.</li>
<li>If a bond's price rises, its yield falls. Price of a perpetual bond = coupon / yield.</li>
<li>Gordon model: P<sub>0</sub> = D<sub>1</sub>/(r − g); implied return r = D<sub>1</sub>/P<sub>0</sub> + g, the dividend yield plus growth.</li>
<li>Cash flow additivity: investing for two years at the two-year spot rate should equal investing for one year and rolling over at the implied forward rate. It also gives no-arbitrage forward exchange rates.</li>
</ul>
<p class="f">(1 + S<sub>2</sub>)² = (1 + S<sub>1</sub>)(1 + F<sub>1,1</sub>)</p>""",
qs=[
 ["An annuity pays $250 at the end of each year for 10 years. At 8%, its present value is closest to:", ["$1,678", "$1,812", "$2,500"], 0, "250 × 6.7101 = 1,677.52."],
 ["If the annuity above paid at the start of each year, its present value would be closest to:", ["$1,678", "$1,812", "$1,950"], 1, "Annuity due = 1,677.52 × 1.08 = 1,811.72."],
 ["A 15-year zero-coupon bond yields 2.5% with annual compounding. Its price per 100 of face value is closest to:", ["69.05", "71.42", "96.30"], 0, "100 / 1.025^15 = 69.05."],
 ["A 10-year zero-coupon bond has a yield of −1.0%. Its price per 100 of face value is closest to:", ["90.44", "100.00", "110.57"], 2, "100 / 0.99^10 = 110.57: a negative yield means a price above par."],
 ["A perpetual bond pays $5,000 a year and similar bonds yield 6%. Its price is closest to:", ["$30,000", "$83,333", "$90,000"], 1, "5,000 / 0.06."],
 ["A perpetuity pays $120 a year with the first payment in five years. At 8%, its value today is closest to:", ["$1,103", "$1,191", "$1,500"], 0, "Value at Year 4 = 1,500; discounted four years = 1,102.54."],
 ["A $20,000 loan is repaid with 48 monthly payments at 6% annual interest. Each payment is closest to:", ["$417", "$470", "$520"], 1, "PMT with i = 0.5%, n = 48 = 469.70."],
 ["A zero-coupon bond costs $600 and pays $1,000 in 12 years. Its annual yield is closest to:", ["4.3%", "4.8%", "5.6%"], 0, "(1000/600)^(1/12) − 1 = 4.35%."],
 ["An 8-year bond pays an annual coupon of 45 on 1,000 face value. Its yield to maturity is 5.5%. Its price is closest to:", ["936.65", "1,000.00", "1,066.40"], 0, "PV of coupons and face value at 5.5%."],
 ["A share has just paid a dividend of $1.80, which grows at 5% a year. Investors require 11%. Its value is:", ["$30.00", "$31.50", "$36.00"], 1, "1.80 × 1.05 / 0.06 = 31.50."],
 ["The one-year spot rate is 2% and the two-year spot rate is 3%. The implied one-year rate one year from now is closest to:", ["3.0%", "4.0%", "5.0%"], 1, "1.03² / 1.02 − 1 = 4.01%."],
 ["Under a constant growth model, a share's required return can be estimated as the:", ["dividend yield plus the growth rate.", "growth rate minus the dividend yield.", "dividend yield minus the growth rate."], 0, "r = D1/P0 + g."],
 ["A bond's price rises from 942.50. Its yield to maturity will:", ["fall.", "rise.", "stay the same."], 0, "Prices and yields move inversely."],
 ["To apply the Gordon growth model, the required return must be:", ["greater than the dividend growth rate.", "equal to the growth rate.", "less than the growth rate."], 0, "Otherwise the formula gives no meaningful value."],
 ["Two investments have identical cash flows in all states, but one is priced slightly below the other. An investor should most likely:", ["buy the cheaper one and sell the dearer one.", "buy both.", "ignore the difference."], 0, "This exploits a violation of the law of one price."],
 ["The one-year interest rates are 3.5% in USD and 4.0% in GBP, and spot is 1.25 USD/GBP. The one-year no-arbitrage forward rate is closest to:", ["1.2440 USD/GBP", "1.2500 USD/GBP", "1.2560 USD/GBP"], 0, "1.25 × 1.035/1.04 = 1.2440."],
])

EK["sm"] = dict(
terms=[
 ["Leptokurtic", "Sivri (leptokurtik)", "A distribution with fatter tails and a higher peak than the normal distribution; positive excess kurtosis.", "Normal dağılımdan daha kalın kuyruklu ve daha sivri tepeli dağılım; pozitif fazla basıklık."],
 ["Platykurtic", "Basık (platikurtik)", "A distribution with thinner tails than the normal distribution; negative excess kurtosis.", "Normal dağılımdan daha ince kuyruklu dağılım; negatif fazla basıklık."],
 ["Interquartile range", "Çeyrekler arası açıklık", "The difference between the third and first quartiles.", "Üçüncü ve birinci çeyrek arasındaki fark."],
],
notes="""<h3>More on statistical measures</h3>
<ul>
<li>Positive skew: mean &gt; median &gt; mode (long right tail). Negative skew: mean &lt; median &lt; mode.</li>
<li>Kurtosis measures tail thickness. Normal kurtosis = 3; excess kurtosis = kurtosis − 3. Leptokurtic: fat tails, more extreme outcomes, risk understated by standard deviation.</li>
<li>Position of a percentile in sorted data: L<sub>y</sub> = (n + 1) × y / 100. Quartiles, quintiles and deciles follow.</li>
<li>Sample variance divides by n − 1. CV = standard deviation / mean. Sharpe ratio = (mean − R<sub>f</sub>) / standard deviation.</li>
<li>Trimmed mean drops a percentage of extreme values (half from each end); winsorized mean replaces them with the nearest remaining values. Both reduce the effect of outliers. The median is unaffected by raising the largest value.</li>
<li>Correlation measures linear association only; −0.74 means a strong tendency to move in opposite directions.</li>
</ul>""",
qs=[
 ["Annual returns are 12%, −12%, 5% and 2%. The geometric mean return is closest to:", ["1.4%", "1.8%", "2.1%"], 0, "(1.12 × 0.88 × 1.05 × 1.02)^0.25 − 1 = 1.36%."],
 ["For the returns 12%, −12%, 5% and 2%, the arithmetic mean is:", ["1.4%", "1.75%", "2.25%"], 1, "7% / 4 = 1.75%."],
 ["A sample of returns is 8%, 2%, 11% and −1%. The sample standard deviation is closest to:", ["4.7%", "5.5%", "6.3%"], 1, "Mean 5%; squared deviations sum to 0.009; /3 = 0.003; √ = 5.48%."],
 ["Returns are 12%, 18%, 22% and 8%. The mean absolute deviation is:", ["4.0%", "5.0%", "6.0%"], 1, "Mean 15%; absolute deviations 3, 3, 7, 7; average 5%."],
 ["A distribution has a mean of 10 and a variance of 36. Its coefficient of variation is:", ["0.36", "0.60", "3.60"], 1, "Standard deviation 6 / mean 10."],
 ["For a unimodal distribution with negative skewness:", ["the median is greater than the mean.", "the mean is greater than the mode.", "the mean equals the median."], 0, "The long left tail pulls the mean down."],
 ["For a positively skewed distribution, which order from lowest to highest is correct?", ["Mode, median, mean", "Mean, median, mode", "Median, mode, mean"], 0, "The right tail pulls the mean above the median."],
 ["A distribution with a mode of 10 and a range of 2 to 25 is most likely:", ["positively skewed.", "negatively skewed.", "symmetric."], 0, "The longer tail is on the right."],
 ["A return distribution with positive excess kurtosis has, compared with a normal distribution:", ["more frequent extreme outcomes.", "fewer extreme outcomes.", "a lower peak."], 0, "Fat tails mean large deviations are more likely."],
 ["A distribution that is more peaked than the normal distribution, with fatter tails, is:", ["leptokurtic.", "platykurtic.", "mesokurtic."], 0, "Lepto means slender, referring to the tall peak."],
 ["The data 9, 4, 15, 21, 7, 12, 18, 30, 25 are sorted. Using (n + 1) × y/100, the third quartile is:", ["21.0", "23.0", "25.0"], 1, "Sorted: 4, 7, 9, 12, 15, 18, 21, 25, 30. Position 7.5: halfway between 21 and 25 = 23."],
 ["A 10% trimmed mean excludes the:", ["highest and lowest 5% of observations.", "highest and lowest 10% of observations.", "lowest 10% only."], 0, "The trim is split equally between the two ends."],
 ["A winsorized mean most likely:", ["replaces extreme values with the nearest remaining values.", "gives equal weight to all returns.", "excludes all negative returns."], 0, "This reduces the effect of outliers."],
 ["A company raises the salary of its highest-paid employee. The median salary will:", ["stay the same.", "rise.", "fall."], 0, "The middle value does not change."],
 ["A security's mean monthly return is 1.2% and its standard deviation 3.0%. The risk-free rate is 0.2% a month. Its Sharpe ratio is closest to:", ["0.33", "0.40", "2.50"], 0, "(1.2 − 0.2)/3.0 = 0.33."],
 ["The correlation between two variables is −0.74. This means that:", ["when one rises, the other tends to fall.", "a 1% rise in one causes a 0.74% fall in the other.", "the variables are unrelated."], 0, "Correlation measures association, not causation or slope."],
 ["Which statement about kurtosis is least accurate?", ["It measures how asymmetric a distribution is.", "It measures how fat the tails are.", "A normal distribution has kurtosis of 3."], 0, "Asymmetry is skewness."],
 ["A correlation of −0.065 between an asset's return and economic growth most likely indicates:", ["almost no linear relationship.", "a strong negative relationship.", "a strong positive relationship."], 0, "It is close to zero."],
 ["An analyst wants a central tendency measure that is not affected by two extremely high returns. The best choice is the:", ["median.", "arithmetic mean.", "geometric mean."], 0, "The median depends only on the middle value."],
 ["An observation at the 65th percentile means that:", ["about 65% of observations are at or below it.", "it is the 65th observation.", "65% of observations are above it."], 0, "Percentiles divide sorted data into 100 parts."],
])

EK["pt"] = dict(
notes="""<h3>More on probability</h3>
<p class="f">P(A) = P(A|B)P(B) + P(A|B<sup>C</sup>)P(B<sup>C</sup>) · P(B|A) = P(A|B)P(B) / P(A)</p>
<ul>
<li>Probability trees combine scenarios: multiply along branches for joint probabilities, add across branches for totals.</li>
<li>Conditional expectations update an expected value when new information arrives.</li>
<li>An analyst who revises a forecast because of new information is applying a conditional expectation; Bayes' formula updates prior probabilities to posterior ones.</li>
</ul>""",
qs=[
 ["There is a 30% chance the economy expands. A sector outperforms with probability 80% if it expands and 30% if it does not. The unconditional probability of outperformance is:", ["24%", "45%", "55%"], 1, "0.3 × 0.8 + 0.7 × 0.3 = 0.45."],
 ["Using the data above, if the sector outperforms, the probability that the economy expanded is closest to:", ["30%", "53%", "80%"], 1, "Bayes: 0.24 / 0.45 = 0.533."],
 ["An investment earns 15% with probability 0.25, 8% with probability 0.5 and −4% with probability 0.25. Its expected return is:", ["6.00%", "6.75%", "8.00%"], 1, "0.25 × 15 + 0.5 × 8 + 0.25 × (−4) = 6.75%."],
 ["For the investment above, the standard deviation of returns is closest to:", ["4.7%", "6.8%", "9.5%"], 1, "Variance ≈ 0.00467; √ = 6.83%."],
 ["An analyst revises her earnings forecast after a central bank changes interest rates. This is an example of:", ["a conditional expectation.", "an unconditional probability.", "a joint probability."], 0, "The expectation is updated given new information."],
 ["P(A) = 0.4, P(B|A) = 0.5 and P(B|not A) = 0.2. P(B) is:", ["0.20", "0.32", "0.50"], 1, "0.4 × 0.5 + 0.6 × 0.2 = 0.32."],
 ["A conditional expectation involves:", ["refining an expected value using new information.", "calculating a joint probability only.", "ignoring scenario probabilities."], 0, "It is the expected value given a condition."],
 ["Forty per cent of cars in a car park are red. Seventy per cent of red cars and 80% of blue cars have a roof rack. The probability that a randomly chosen car has a roof rack is:", ["74%", "75%", "76%"], 2, "0.4 × 0.7 + 0.6 × 0.8 = 0.76."],
])

EK["pm"] = dict(
notes="""<h3>More on portfolio mathematics</h3>
<p class="f">σ<sub>p</sub>² = w<sub>1</sub>²σ<sub>1</sub>² + w<sub>2</sub>²σ<sub>2</sub>² + 2w<sub>1</sub>w<sub>2</sub>ρσ<sub>1</sub>σ<sub>2</sub> · ρ = Cov / (σ<sub>1</sub>σ<sub>2</sub>)</p>
<ul>
<li>Covariance from a joint distribution: Σ p × (X − E[X])(Y − E[Y]).</li>
<li>With perfectly negative correlation, a zero-risk portfolio uses w<sub>A</sub> = σ<sub>B</sub> / (σ<sub>A</sub> + σ<sub>B</sub>).</li>
<li>Roy's safety-first ratio = (E[R] − R<sub>L</sub>) / σ. Choose the highest ratio to minimize the probability of falling below the threshold.</li>
<li>Variance of a discrete variable: Σ p × (x − E[x])².</li>
</ul>""",
qs=[
 ["A portfolio has 40% in an asset with a standard deviation of 20% and 60% in one with 30%. The correlation is 0.25. The portfolio standard deviation is closest to:", ["19.2%", "21.4%", "26.0%"], 1, "Variance = 0.0064 + 0.0324 + 0.0072 = 0.046; √ = 21.4%."],
 ["The covariance between two assets is 0.012 and their standard deviations are 15% and 20%. Their correlation is:", ["0.04", "0.40", "0.80"], 1, "0.012 / (0.15 × 0.20) = 0.40."],
 ["Two assets are perfectly negatively correlated, with standard deviations of 12% (A) and 18% (B). The weight in A that gives a zero-risk portfolio is:", ["40%", "50%", "60%"], 2, "w_A = 18 / (12 + 18) = 0.6."],
 ["An investor's threshold return is 4%. Portfolio X has E[R] = 11% and σ = 14%; Y has 9% and 9%; Z has 13% and 18%. Using Roy's safety-first criterion, she should choose:", ["Portfolio X.", "Portfolio Y.", "Portfolio Z."], 1, "Ratios: X 0.50, Y 0.56, Z 0.50."],
 ["X takes the values 2, 3 and 4 with probabilities 0.25, 0.5 and 0.25. The variance of X is:", ["0.25", "0.50", "1.00"], 1, "Mean 3; variance = 0.25 × 1 + 0.5 × 0 + 0.25 × 1 = 0.5."],
 ["To calculate the standard deviation of a two-asset portfolio, an analyst needs the assets' standard deviations, their correlation and the:", ["portfolio weights.", "risk-free rate.", "expected returns."], 0, "Weights enter every term of the variance formula."],
 ["The covariance of two investments is 0.009. Their variances are 0.020 and 0.016. Their correlation is closest to:", ["0.28", "0.50", "0.56"], 1, "0.009 / (0.1414 × 0.1265) = 0.50."],
 ["A boom (probability 0.3) gives a 15% return and a bust (0.7) gives 3%. The expected return is:", ["6.6%", "9.0%", "11.4%"], 0, "0.3 × 15 + 0.7 × 3 = 6.6%."],
])

EK["si"] = dict(
notes="""<h3>More on simulation</h3>
<ul>
<li>If ln(Y) is normally distributed, Y is <b>lognormal</b>: bounded below by zero and positively skewed, so it suits asset prices. Continuously compounded returns are normal.</li>
<li>Monte Carlo simulation approximates solutions to complex problems such as valuing options with complex features. Limitations: results are only as good as the inputs and model; it is statistical, not analytic, so it gives less insight into cause and effect.</li>
<li>Resampling draws repeated samples from the observed sample to estimate population parameters. In bootstrap resampling, each sample is the same size as the original and drawn <b>with replacement</b>, so an observation can appear many times.</li>
</ul>""",
qs=[
 ["If a random variable Y is lognormally distributed, ln(Y) is:", ["normally distributed.", "lognormally distributed.", "uniformly distributed."], 0, "This is the definition of lognormal."],
 ["A lognormal distribution is least likely to be:", ["negatively skewed.", "bounded below by zero.", "used to model share prices."], 0, "It is positively skewed."],
 ["Lognormal distributions are used for asset prices mainly because they:", ["cannot take negative values.", "are symmetric.", "have thin tails."], 0, "Prices cannot fall below zero."],
 ["A limitation of Monte Carlo simulation is that:", ["results are only as accurate as the inputs and assumptions.", "it cannot handle complex securities.", "it requires no computing power."], 0, "Garbage in, garbage out."],
 ["Monte Carlo simulation is most useful to:", ["approximate solutions to complex problems.", "compute continuously compounded returns.", "eliminate sampling error."], 0, "It handles problems without closed-form answers."],
 ["In bootstrap resampling, a single observation from the original sample:", ["may appear more than once in a resample.", "appears exactly once in each resample.", "is never reused."], 0, "Sampling is with replacement."],
 ["In bootstrap resampling, each resample is:", ["the same size as the original sample.", "smaller each time.", "larger each time."], 0, "Many resamples of equal size are drawn."],
 ["The aim of resampling is to estimate parameters of the:", ["overall population.", "individual subsamples.", "original sample only."], 0, "Subsamples are a tool for inference."],
 ["Compared with analytic methods, a limitation of Monte Carlo simulation is that it:", ["gives less insight into cause and effect.", "cannot use probability distributions.", "only works with normal variables."], 0, "It produces statistical estimates rather than formulas."],
])

EK["ei"] = dict(
notes="""<h3>More on sampling</h3>
<ul>
<li><b>Simple random</b>: every member has an equal chance. <b>Stratified</b>: divide into strata, sample from each in proportion; used to build bond index portfolios. <b>Cluster</b>: sample whole groups. <b>Convenience</b>: easy to reach. <b>Judgmental</b>: the researcher hand-picks, as an auditor might.</li>
<li>Central limit theorem: for large samples (n ≥ 30), the distribution of sample means is approximately normal with mean μ and variance σ²/n, whatever the population's distribution.</li>
<li>Standard error of the mean = σ/√n (or s/√n).</li>
<li>Jackknife: repeat the mean leaving out one observation at a time. Bootstrap: resample with replacement; useful when no analytic formula exists for the standard error.</li>
</ul>""",
qs=[
 ["A population has a standard deviation of 20. The standard error of the mean for a sample of 100 is:", ["0.2", "2.0", "20.0"], 1, "20 / √100 = 2."],
 ["An auditor who hand-picks transactions to examine for fraud is using:", ["judgmental sampling.", "cluster sampling.", "convenience sampling."], 0, "Selection relies on the auditor's judgment."],
 ["According to the central limit theorem, the distribution of sample means is approximately normal if:", ["the sample size is large.", "the population is normal only.", "the population variance is known."], 0, "This holds for any population distribution."],
 ["The central limit theorem concerns the sampling distribution of the:", ["sample mean.", "sample standard deviation.", "population mean."], 0, "It describes how sample means are distributed."],
 ["If the population mean is 16.62, the mean of the distribution of all sample means of size 40 is:", ["16.62", "16.62 / √40", "unknown"], 0, "The sample mean is an unbiased estimator."],
 ["Which statement about the central limit theorem is least accurate?", ["It requires a normal population.", "The variance of sample means is σ²/n.", "It applies to large samples."], 0, "The population can have any distribution with finite variance."],
 ["A technique that calculates many means from the same sample, each time leaving out one observation, is the:", ["jackknife.", "bootstrap.", "stratified sample."], 0, "The bootstrap resamples with replacement."],
 ["An analyst sorts stocks into 10 groups by size and draws a random sample from each group. This is:", ["stratified random sampling.", "cluster sampling.", "simple random sampling."], 0, "Each stratum is represented."],
 ["Stratified random sampling is most often used to build portfolios that track indexes of:", ["bonds.", "small-cap shares.", "commodities."], 0, "Bond indexes have many issues with distinct risk factors."],
 ["An advantage of the bootstrap over a formula-based standard error is that it:", ["can be used when no analytic formula is available.", "is always more accurate.", "needs less computation."], 0, "It works for complex statistics."],
 ["A population of bank debt-to-equity ratios has a mean of 20 and a variance of 25. For samples of 100 banks, the standard error of the sample mean is:", ["0.25", "0.50", "2.50"], 1, "σ = 5; 5/√100 = 0.5."],
])

EK["ht"] = dict(
notes="""<h3>More on hypothesis testing</h3>
<ul>
<li>Type I error: rejecting a true null (probability = significance level α). Type II error: failing to reject a false null (probability β). Power = 1 − β.</li>
<li>Lowering α raises the chance of a Type II error, other things equal. A larger sample raises power.</li>
<li>Put what you hope to prove in the <b>alternative</b>; a 'greater than or equal' claim becomes H<sub>0</sub>: μ ≤ μ<sub>0</sub> versus H<sub>a</sub>: μ &gt; μ<sub>0</sub> for a one-tailed test.</li>
<li>Two-tailed 5% test: critical z = ±1.96; one-tailed 5%: 1.645. Reject if the statistic is beyond the critical value or if the p-value &lt; α.</li>
<li>Tests: t-test for a mean with unknown variance; chi-square for a single variance; F-test for equality of two variances; paired comparisons for dependent samples.</li>
<li>Parametric tests rely on assumptions about population distributions; non-parametric tests need fewer assumptions and suit ranked data or outliers.</li>
</ul>
<p class="f">t = (x̄ − μ<sub>0</sub>) / (s/√n)</p>""",
qs=[
 ["A Type I error is made when a researcher:", ["rejects a true null hypothesis.", "fails to reject a false null hypothesis.", "rejects a false null hypothesis."], 0, "Its probability is the significance level."],
 ["A Type II error:", ["fails to reject a false null hypothesis.", "rejects a true null hypothesis.", "rejects a false null hypothesis."], 0, "Its probability is β."],
 ["The power of a test is the probability of:", ["rejecting a false null hypothesis.", "rejecting a true null hypothesis.", "failing to reject a false null."], 0, "Power = 1 − probability of a Type II error."],
 ["If the probability of a Type I error is reduced, other things equal, the probability of a Type II error:", ["rises.", "falls.", "is unchanged."], 0, "A stricter test is less likely to detect a false null."],
 ["To increase the power of a test without changing the significance level, a researcher should:", ["increase the sample size.", "use a smaller sample.", "switch to a two-tailed test."], 0, "More data reduces the standard error."],
 ["A researcher wants to show that average salaries exceed $60,000. The appropriate hypotheses are:", ["H0: μ ≤ 60,000; Ha: μ > 60,000.", "H0: μ > 60,000; Ha: μ ≤ 60,000.", "H0: μ = 60,000; Ha: μ ≠ 60,000."], 0, "The claim to be supported goes in the alternative."],
 ["A sample of 36 has a mean of 5.4 and a standard deviation of 1.8. The t-statistic for H0: μ = 5 is closest to:", ["0.22", "1.33", "8.00"], 1, "(5.4 − 5) / (1.8/6) = 1.33."],
 ["For a two-tailed z-test at 5% significance, a z-statistic of 1.85 leads the researcher to:", ["fail to reject the null.", "reject the null.", "accept the alternative."], 0, "1.85 is inside ±1.96."],
 ["A one-tailed z-test at 5% significance will reject a true null hypothesis:", ["5% of the time.", "95% of the time.", "never."], 0, "That is the meaning of the significance level."],
 ["An analyst wants to test whether a population variance equals a given value. She should use a:", ["chi-square test.", "t-test.", "F-test."], 0, "The F-test compares two variances."],
 ["To test whether two populations have equal variances, the appropriate statistic is the:", ["F-statistic.", "chi-square statistic.", "z-statistic."], 0, "It is the ratio of the two sample variances."],
 ["Which statement about parametric and non-parametric tests is least accurate?", ["Non-parametric tests rely on population parameters.", "Parametric tests make assumptions about distributions.", "Non-parametric tests suit ranked data."], 0, "Non-parametric tests need fewer assumptions."],
 ["A test of whether a fund's performance rank in one period predicts its rank in the next is most likely a:", ["non-parametric test.", "parametric t-test of means.", "chi-square test of variance."], 0, "Ranks call for non-parametric methods."],
 ["If the p-value of a test is 0.03 and the significance level is 5%, the researcher should:", ["reject the null hypothesis.", "fail to reject the null hypothesis.", "increase the significance level."], 0, "The p-value is below α."],
 ["To test whether the mean of differences between paired observations is zero, the appropriate test is a:", ["paired comparisons t-test.", "difference in means test for independent samples.", "chi-square test."], 0, "The samples are dependent."],
 ["If a two-tailed test has a 5% probability of rejecting the null when it is true, then:", ["the significance level is 5%.", "the power of the test is 95%.", "the probability of a Type II error is 5%."], 0, "Power depends on β, not α."],
])

EK["ti"] = dict(
notes="""<h3>More on tests of independence</h3>
<p class="f">t = r√(n − 2) / √(1 − r²), df = n − 2 · χ² = Σ (O − E)² / E, df = (rows − 1)(columns − 1)</p>
<ul>
<li>To test whether a correlation is zero, use a t-statistic with n − 2 degrees of freedom (parametric, Pearson) or the Spearman rank correlation (non-parametric).</li>
<li>A test of independence of two categorical variables uses a contingency table and a <b>chi-square</b> statistic; it is non-parametric.</li>
<li>Expected frequency of a cell = row total × column total / grand total.</li>
</ul>""",
qs=[
 ["A test of independence based on contingency table data uses a(n):", ["chi-square statistic.", "F-statistic.", "t-statistic."], 0, "It compares observed and expected frequencies."],
 ["In a test of independence with a contingency table of 3 rows and 4 columns, the degrees of freedom are:", ["6", "7", "12"], 0, "(3 − 1) × (4 − 1) = 6."],
 ["A sample of 24 pairs has a correlation of 0.42. The t-statistic for testing zero correlation is closest to:", ["1.97", "2.17", "2.40"], 1, "0.42 × √22 / √(1 − 0.1764) = 2.17."],
 ["To test whether weekly returns on two shares are correlated, the test statistic follows a:", ["t-distribution.", "chi-square distribution.", "F-distribution."], 0, "With n − 2 degrees of freedom."],
 ["A test of whether two categorical variables are independent is most likely:", ["non-parametric.", "parametric.", "based on population variances."], 0, "It makes no distributional assumptions."],
 ["The expected frequency for a cell in a contingency table equals:", ["row total × column total / grand total.", "row total / column total.", "observed frequency squared."], 0, "This is the frequency implied by independence."],
])

EK["lr"] = dict(
notes="""<h3>More on simple linear regression</h3>
<ul>
<li>OLS minimizes the sum of squared differences between actual and predicted values of the dependent variable.</li>
<li>Assumptions: linear relationship, constant error variance (homoskedasticity), independent errors, normally distributed errors. Heteroskedasticity means the error variance is not constant.</li>
<li>R² = RSS/SST = 1 − SSE/SST. SEE = √(SSE / (n − 2)). F = MSR/MSE with 1 and n − 2 df.</li>
<li>Confidence and prediction intervals use n − 2 degrees of freedom.</li>
<li>Functional forms: log-lin (ln Y on X) when X relates to the relative change in Y; lin-log (Y on ln X); log-log (both logs; slope is an elasticity).</li>
<li>The slope is the change in Y for a one-unit change in X.</li>
</ul>""",
qs=[
 ["The regression equation is Y = 1.5 + 0.9X. When X = 4, the predicted value of Y is:", ["3.6", "5.1", "6.0"], 1, "1.5 + 0.9 × 4 = 5.1."],
 ["A regression has a regression sum of squares of 600 and a total sum of squares of 800. Its R² is:", ["0.25", "0.75", "1.33"], 1, "600 / 800."],
 ["A regression on 50 observations has a sum of squared errors of 200. The standard error of the estimate is closest to:", ["2.00", "2.04", "4.17"], 1, "√(200 / 48) = 2.04."],
 ["A simple linear regression exhibits heteroskedasticity if its residuals:", ["do not have a constant variance.", "are not normally distributed.", "are correlated with each other."], 0, "Correlated residuals indicate serial correlation."],
 ["For a confidence interval around a predicted value in simple regression with n observations, the degrees of freedom are:", ["n − 2.", "n − 1.", "n."], 0, "Two parameters are estimated."],
 ["When an independent variable has a linear relationship with the relative change in the dependent variable, the most appropriate model is:", ["log-lin.", "lin-log.", "log-log."], 0, "Take the log of the dependent variable."],
 ["The least squares criterion minimizes the sum of squared differences between:", ["actual and predicted values of the dependent variable.", "actual and predicted values of the independent variable.", "the intercept and the slope."], 0, "These differences are the residuals."],
 ["Which is least likely an assumption of the linear regression model?", ["The independent variable is normally distributed.", "The error variance is constant.", "The errors are independent."], 0, "The assumption concerns the residuals."],
 ["A simple linear regression models the relationship between:", ["one dependent and one independent variable.", "one dependent and several independent variables.", "two dependent variables."], 0, "Multiple regression has more than one independent variable."],
 ["The slope coefficient in a simple linear regression is the:", ["change in the dependent variable for a one-unit change in the independent variable.", "value of Y when X is zero.", "correlation between X and Y."], 0, "The intercept is Y when X = 0."],
])

EK["bd"] = dict(
terms=[
 ["Underfitting", "Eksik uyum", "When a model is too simple and treats real relationships as noise, performing poorly even on training data.", "Modelin fazla basit olması ve gerçek ilişkileri gürültü sayması; eğitim verisinde bile kötü sonuç verir."],
 ["Data curation", "Veri düzenleme", "Ensuring data quality and accuracy, for example by cleaning errors and adjusting for missing values.", "Hataları temizleme ve eksik değerleri düzeltme gibi işlemlerle veri kalitesini ve doğruluğunu sağlama."],
 ["Text analytics", "Metin analizi", "Using computers to analyse unstructured text, such as counting words in filings.", "Bilgisayarla yapılandırılmamış metni analiz etme; örneğin raporlarda kelime saymak."],
],
notes="""<h3>More on Big Data</h3>
<ul>
<li>The Vs of Big Data: <b>volume</b> (terabytes), <b>velocity</b> (low latency, real time), <b>variety</b> (structured and unstructured) and veracity (reliability).</li>
<li>A main driver of fintech is the growing amount of <b>unstructured</b> data.</li>
<li>Data processing: capture (collecting and moving data), curation (quality and cleaning), storage, search, transfer.</li>
<li>Machine learning: supervised (learns from labelled inputs and outputs), unsupervised (finds structure without labels), deep learning (neural networks with many layers).</li>
<li>Overfitting: the model treats noise as true parameters. Underfitting: it treats true parameters as noise.</li>
<li>Applications include text analytics, natural language processing, algorithmic trading and risk management.</li>
</ul>""",
qs=[
 ["A machine learning model is said to be underfit when it:", ["treats true parameters as noise.", "treats noise as true parameters.", "has too many variables."], 0, "Overfitting is the reverse."],
 ["An executive mentions 'low latency' and 'multiple terabytes' when describing her data needs. These refer to Big Data's:", ["velocity and volume.", "variety and veracity.", "volume and variety."], 0, "Latency is about speed; terabytes about size."],
 ["Counting how often words like 'risk' appear in companies' annual reports is an example of:", ["text analytics.", "deep learning.", "algorithmic trading."], 0, "It analyses unstructured text."],
 ["A primary driver of fintech is the:", ["increasing amount of unstructured data.", "decline in computing power.", "shift to fully structured data."], 0, "New tools process text, images and other unstructured data."],
 ["An analyst adjusts two countries' daily index data for different public holidays. This is an example of data:", ["curation.", "capture.", "storage."], 0, "Curation ensures data are accurate and comparable."],
 ["A machine learns to model outputs from a given set of labelled inputs. This is:", ["supervised learning.", "unsupervised learning.", "deep learning."], 0, "Labelled data guide the model."],
 ["Artificial intelligence is best described as:", ["computer systems that perform tasks that normally need human intelligence.", "networks of smart devices.", "a method of storing data."], 0, "Networks of devices are the Internet of Things."],
])

# Sayı içermeyen sorularda doğru şıkları sırayla A/B/C'ye dağıt.
_n = 0
for _e in EK.values():
    for _q in _e.get("qs", []):
        if any(_re.search(r"\d", _x) for _x in _q[1]): continue
        _j = _n % 3; _o = _q[1]; _i = _q[2]
        _o[_i], _o[_j] = _o[_j], _o[_i]; _q[2] = _j; _n += 1
