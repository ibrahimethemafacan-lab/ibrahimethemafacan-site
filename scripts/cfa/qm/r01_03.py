# CFA Level I · Quantitative Methods · readings 1–3. Original study notes and questions.
R = []

R.append(dict(id="rr", n="Rates and Returns", k="RETURNS", w=3, c="#3b7dd8",
terms=[
 ["Required rate of return", "Gerekli getiri oranı", "The minimum return an investor needs to accept an investment, given its risk.", "Yatırımcının, riskini göz önüne alarak bir yatırımı kabul etmek için istediği en düşük getiri."],
 ["Real risk-free rate", "Reel risksiz faiz oranı", "The return on a riskless security when no inflation is expected; it reflects time preference only.", "Enflasyon beklenmediği durumda risksiz bir menkul kıymetin getirisi; yalnızca zaman tercihini yansıtır."],
 ["Inflation premium", "Enflasyon primi", "Compensation for expected loss of purchasing power over the life of the investment.", "Yatırım süresince beklenen satın alma gücü kaybının karşılığı."],
 ["Default risk premium", "Temerrüt riski primi", "Extra return for the possibility that the borrower fails to pay as promised.", "Borçlunun ödemeyi vaat ettiği gibi yapamama olasılığı için istenen ek getiri."],
 ["Liquidity premium", "Likidite primi", "Extra return for an asset that cannot be sold quickly at close to fair value.", "Gerçeğe uygun değerine yakın bir fiyattan hızla satılamayan varlık için istenen ek getiri."],
 ["Holding period return (HPR)", "Elde tutma dönemi getirisi", "Total return over one period: price change plus income, divided by the beginning price.", "Tek bir dönemin toplam getirisi: fiyat değişimi ile gelirin toplamının dönem başı fiyata oranı."],
 ["Geometric mean return", "Geometrik ortalama getiri", "The constant per-period rate that produces the same ending wealth as the actual sequence of returns.", "Gerçekleşen getiri dizisiyle aynı dönem sonu servete ulaştıran sabit dönemlik oran."],
 ["Harmonic mean", "Harmonik ortalama", "The reciprocal of the average of reciprocals; it gives the average cost per share when equal money amounts are invested each period.", "Terslerin ortalamasının tersi; her dönem eşit tutar yatırıldığında pay başına ortalama maliyeti verir."],
 ["Money-weighted return (MWR)", "Para ağırlıklı getiri", "The internal rate of return on all cash flows into and out of the portfolio; it depends on the timing and size of flows.", "Portföye giren ve çıkan tüm nakit akışlarının iç verim oranı; akışların zamanına ve büyüklüğüne bağlıdır."],
 ["Time-weighted return (TWR)", "Zaman ağırlıklı getiri", "The compound growth rate of one unit of money over the period, unaffected by external cash flows.", "Bir birim paranın dönem boyunca bileşik büyüme oranı; dış nakit akışlarından etkilenmez."],
 ["Continuously compounded return", "Sürekli bileşik getiri", "The natural logarithm of one plus the holding period return.", "Bir artı elde tutma dönemi getirisinin doğal logaritması."],
],
notes="""<h3>What an interest rate measures</h3>
<ul>
<li>An interest rate can be read three ways: a <b>required rate of return</b>, a <b>discount rate</b>, or an <b>opportunity cost</b> of spending money today.</li>
<li>A quoted (nominal) rate is built from layers of compensation:</li>
</ul>
<p class="f">nominal rate ≈ real risk-free rate + inflation premium + default risk premium + liquidity premium + maturity premium</p>
<ul>
<li>The <b>nominal risk-free rate</b> is the first two layers only: real risk-free rate plus expected inflation. Short-term government bills are the usual proxy.</li>
<li>Each extra premium answers one question: might the borrower not pay (default), can I sell quickly at a fair price (liquidity), how sensitive is the price to rate changes over a long life (maturity)?</li>
</ul>
<h3>Holding period return</h3>
<p class="f">HPR = (P<sub>1</sub> − P<sub>0</sub> + I<sub>1</sub>) / P<sub>0</sub></p>
<ul>
<li>Returns over several periods link by multiplication, not addition: (1 + R<sub>1</sub>)(1 + R<sub>2</sub>)…(1 + R<sub>n</sub>) − 1.</li>
</ul>
<h3>Three averages</h3>
<div class="tbl"><table>
<tr><th>Mean</th><th>How it is computed</th><th>When it is the right one</th></tr>
<tr><td>Arithmetic</td><td>Sum of returns ÷ n</td><td>Best estimate of the return in a single future period</td></tr>
<tr><td>Geometric</td><td>[(1+R<sub>1</sub>)…(1+R<sub>n</sub>)]<sup>1/n</sup> − 1</td><td>Compound growth of wealth over several past periods</td></tr>
<tr><td>Harmonic</td><td>n ÷ Σ(1/X<sub>i</sub>)</td><td>Average price paid when the same money amount is invested each period</td></tr>
</table></div>
<ul>
<li>For any set of values that are not all equal: <b>arithmetic &gt; geometric &gt; harmonic</b>. The gap widens as the values become more dispersed.</li>
</ul>
<div class="trap"><b>Exam trap</b>If a question asks how much wealth actually grew per year, use the geometric mean. The arithmetic mean overstates compound growth whenever returns vary.</div>
<h3>Money-weighted and time-weighted returns</h3>
<ul>
<li><b>Money-weighted return</b> is the IRR of the investor's cash flows. Deposits are outflows from the investor, withdrawals and the ending value are inflows. Periods in which more money was invested count for more.</li>
<li><b>Time-weighted return</b> breaks the horizon at every external cash flow, computes each sub-period HPR, links them and takes the geometric mean if the horizon is longer than a year.</li>
<li>Use TWR to judge a manager who does not control when clients add or withdraw money. Use MWR to describe what a particular investor actually earned.</li>
<li>If money is added just before a weak period, MWR falls below TWR; if added just before a strong period, MWR rises above TWR.</li>
</ul>
<h3>Annualizing and compounding</h3>
<p class="f">annualized return = (1 + R<sub>period</sub>)<sup>periods per year</sup> − 1</p>
<p class="f">continuously compounded return = ln(1 + HPR) = ln(P<sub>1</sub>/P<sub>0</sub>)</p>
<ul>
<li>Continuously compounded returns are additive across time, which is why they are used in modelling.</li>
<li>For a given stated annual rate, more frequent compounding gives a higher effective annual rate; continuous compounding is the upper limit.</li>
</ul>
<h3>Other return labels</h3>
<ul>
<li><b>Gross return</b> is before management and administrative fees, but after trading costs. <b>Net return</b> is after those fees.</li>
<li><b>Real return</b>: (1 + nominal) / (1 + inflation) − 1. Subtracting inflation is only an approximation.</li>
<li><b>Leveraged return</b>: gain or loss on the full position, less borrowing cost, divided by the investor's own capital. Leverage magnifies both gains and losses.</li>
</ul>""",
qs=[
 ["The nominal risk-free rate is best described as the real risk-free rate plus:", ["a maturity premium.", "a default risk premium.", "an expected inflation premium."], 2, "The nominal risk-free rate adds only expected inflation to the real risk-free rate. Default, liquidity and maturity premiums apply to securities that carry those risks."],
 ["An investor buys a share for $50.00, receives a dividend of $1.50 and sells the share one year later for $54.00. The holding period return is closest to:", ["8.0%", "10.2%", "11.0%"], 2, "HPR = (54.00 − 50.00 + 1.50) / 50.00 = 5.50 / 50.00 = 11.0%. The 8.0% figure ignores the dividend."],
 ["A fund returned +20%, −10% and +5% in three consecutive years. The geometric mean annual return is closest to:", ["4.3%", "5.0%", "5.3%"], 0, "(1.20 × 0.90 × 1.05)^(1/3) − 1 = 1.134^(1/3) − 1 ≈ 4.3%. The arithmetic mean is 5.0%, which overstates compound growth."],
 ["An investor puts $1,000 into the same share in each of three months, at prices of $10.00, $12.50 and $20.00. The average cost per share is closest to:", ["$13.04", "$13.57", "$14.17"], 0, "Shares bought: 100 + 80 + 50 = 230. Average cost = 3,000 / 230 = $13.04, the harmonic mean of the prices. $14.17 is the arithmetic mean and $13.57 the geometric mean."],
 ["For a series of returns that are not all equal, which ordering of the means is correct?", ["Harmonic > geometric > arithmetic", "Geometric > arithmetic > harmonic", "Arithmetic > geometric > harmonic"], 2, "With any dispersion in the data, the arithmetic mean is the largest and the harmonic mean the smallest; the geometric mean lies between them."],
 ["A portfolio is worth $100 at the start of Year 1 and earns 20%. The client then adds $100. In Year 2 the portfolio loses 10%. The annual time-weighted return is closest to:", ["−0.7%", "3.9%", "5.0%"], 1, "TWR links the sub-period returns: (1.20 × 0.90)^(1/2) − 1 ≈ 3.9%. The money-weighted return is about −0.7% because more money was invested during the losing year."],
 ["Which return measure is most appropriate for evaluating a manager who has no control over the timing of client deposits and withdrawals?", ["Time-weighted return", "Money-weighted return", "Arithmetic mean of money-weighted returns"], 0, "The time-weighted return removes the effect of external cash flows, so it reflects the manager's investment decisions rather than the client's timing."],
 ["A share price rises from $100 to $110 over a year. The continuously compounded return is closest to:", ["9.53%", "10.00%", "10.52%"], 0, "ln(110 / 100) = ln(1.10) ≈ 9.53%. The continuously compounded return is always below the holding period return when the return is positive."],
 ["An investment earns 3.0% over 90 days. Using a 365-day year, the annualized return is closest to:", ["12.00%", "12.17%", "12.74%"], 2, "(1.03)^(365/90) − 1 ≈ 12.74%. The figure 12.17% scales the return without compounding."],
 ["A bond fund earns a nominal return of 8.0% in a year when inflation is 3.0%. The real return is closest to:", ["4.85%", "5.00%", "5.15%"], 0, "(1.08 / 1.03) − 1 ≈ 4.85%. Subtracting inflation from the nominal return gives 5.00%, which is only an approximation."],
]))

R.append(dict(id="tv", n="The Time Value of Money in Finance", k="TVM", w=3, c="#2e9e8f",
terms=[
 ["Present value (PV)", "Bugünkü değer", "The value today of a future cash flow, found by discounting at an appropriate rate.", "Gelecekteki bir nakit akışının uygun bir oranla iskonto edilerek bulunan bugünkü değeri."],
 ["Discount rate", "İskonto oranı", "The rate used to convert future cash flows to present value; it reflects the required return.", "Gelecekteki nakit akışlarını bugünkü değere çevirmekte kullanılan oran; gerekli getiriyi yansıtır."],
 ["Zero-coupon bond", "Kuponsuz tahvil", "A bond that makes a single payment at maturity and is sold at a discount to that payment.", "Yalnızca vadede tek ödeme yapan ve bu ödemenin altında bir fiyatla satılan tahvil."],
 ["Yield to maturity (YTM)", "Vadeye kadar getiri", "The single discount rate that makes the present value of a bond's promised payments equal to its price.", "Tahvilin vaat edilen ödemelerinin bugünkü değerini fiyatına eşitleyen tek iskonto oranı."],
 ["Perpetuity", "Sonsuz vadeli nakit akışı", "A stream of equal payments that continues forever; its value is the payment divided by the discount rate.", "Sonsuza kadar süren eşit ödemeler dizisi; değeri ödemenin iskonto oranına bölümüdür."],
 ["Annuity", "Anüite", "A finite stream of equal payments made at regular intervals.", "Düzenli aralıklarla yapılan, sınırlı sayıda eşit ödemeden oluşan dizi."],
 ["Amortizing loan", "İtfa edilen kredi", "A loan repaid through equal periodic payments that each contain interest and principal.", "Her biri faiz ve anapara içeren eşit dönemsel ödemelerle geri ödenen kredi."],
 ["Constant growth (Gordon) model", "Sabit büyüme (Gordon) modeli", "Values a share as next year's dividend divided by the required return minus the constant dividend growth rate.", "Payı, gelecek yılın temettüsünün gerekli getiri ile sabit temettü büyüme oranı farkına bölümü olarak değerler."],
 ["Implied return", "Zımni getiri", "The discount rate that equates an asset's observed price with its expected cash flows.", "Varlığın gözlenen fiyatını beklenen nakit akışlarına eşitleyen iskonto oranı."],
 ["Cash flow additivity principle", "Nakit akışı toplanabilirliği ilkesi", "The present value of a set of cash flows equals the sum of the present values of each; two strategies with identical cash flows must have the same price.", "Bir nakit akışı dizisinin bugünkü değeri, her birinin bugünkü değerlerinin toplamıdır; aynı nakit akışlarını üreten iki stratejinin fiyatı aynı olmalıdır."],
 ["Forward rate", "Vadeli faiz oranı", "An interest rate for a loan that begins at a future date, implied by today's spot rates.", "Gelecek bir tarihte başlayacak borçlanma için bugünkü spot oranların ima ettiği faiz oranı."],
],
notes="""<h3>One idea, many instruments</h3>
<ul>
<li>The price of any financial asset is the present value of the cash flows it is expected to pay. Fixed income, equity and derivatives differ only in the pattern and certainty of those cash flows.</li>
</ul>
<p class="f">PV = FV / (1 + r)<sup>t</sup> &nbsp;&nbsp;&nbsp; FV = PV × (1 + r)<sup>t</sup></p>
<h3>Fixed-income instruments</h3>
<div class="tbl"><table>
<tr><th>Pattern</th><th>Cash flows</th><th>Price</th></tr>
<tr><td>Discount (zero-coupon)</td><td>One payment of face value at maturity</td><td>FV / (1 + r)<sup>t</sup></td></tr>
<tr><td>Coupon bond</td><td>Level coupons, then coupon plus principal</td><td>Sum of each payment discounted at the yield to maturity</td></tr>
<tr><td>Perpetual bond</td><td>Coupons forever, no principal</td><td>PMT / r</td></tr>
<tr><td>Level annuity (amortizing loan)</td><td>Equal payments of interest and principal</td><td>PMT × [1 − (1 + r)<sup>−t</sup>] / r</td></tr>
</table></div>
<ul>
<li><b>Coupon rate vs yield:</b> if the coupon rate equals the yield the bond trades at par; a coupon below the yield means a discount, above the yield a premium.</li>
<li>Price and yield move in opposite directions.</li>
<li>With a <b>negative yield</b>, a zero-coupon bond is priced above its face value.</li>
<li>In an amortizing loan the payment is constant, but the interest portion shrinks and the principal portion grows with each payment, because interest is charged on a falling balance.</li>
</ul>
<h3>Equity instruments</h3>
<p class="f">Preferred share (level dividend forever): PV = D / r</p>
<p class="f">Constant growth: PV<sub>0</sub> = D<sub>1</sub> / (r − g), &nbsp; where D<sub>1</sub> = D<sub>0</sub>(1 + g) and r &gt; g</p>
<ul>
<li>For a company with a temporary high-growth phase, value the dividends of that phase one by one, compute a terminal value with the constant growth formula at the start of the stable phase, and discount everything to today.</li>
</ul>
<div class="trap"><b>Exam trap</b>The constant growth formula needs next year's dividend in the numerator. If the question gives the dividend just paid, grow it by one year first.</div>
<h3>Implied return and implied growth</h3>
<ul>
<li>Rearranging a pricing formula for the discount rate gives the return the market price implies.</li>
</ul>
<p class="f">Discount bond: r = (FV / PV)<sup>1/t</sup> − 1</p>
<p class="f">Equity: r = D<sub>1</sub> / P<sub>0</sub> + g &nbsp;&nbsp;&nbsp; g = r − D<sub>1</sub> / P<sub>0</sub></p>
<ul>
<li>The implied return on a share is its expected dividend yield plus the growth rate. Given a required return, the same formula shows what growth rate the current price assumes.</li>
<li>A price-to-earnings ratio can be read the same way: a higher ratio implies higher expected growth or a lower required return.</li>
</ul>
<h3>Cash flow additivity and no arbitrage</h3>
<ul>
<li>If two strategies deliver the same cash flows on the same dates, they must cost the same today. Otherwise an investor could buy the cheap one, sell the expensive one and earn a riskless profit.</li>
<li><b>Forward interest rates:</b> investing for two years at the two-year spot rate must equal investing for one year and rolling over at the one-year rate one year forward.</li>
</ul>
<p class="f">(1 + z<sub>2</sub>)<sup>2</sup> = (1 + z<sub>1</sub>)(1 + f<sub>1,1</sub>)</p>
<ul>
<li><b>Forward exchange rates:</b> converting and investing abroad, with the future proceeds sold forward, must earn the same as investing at home. The forward rate is therefore set by the interest rate difference between the two currencies.</li>
<li><b>Option pricing:</b> in a one-period two-outcome model, a portfolio of the underlying asset and the option can be built to pay the same in both outcomes. That riskless portfolio must earn the risk-free rate, which fixes the option's price without needing the real probabilities of the up and down moves.</li>
</ul>""",
qs=[
 ["A zero-coupon bond pays $1,000 in five years. If the annual discount rate is 4%, its price is closest to:", ["$783.53", "$821.93", "$833.33"], 1, "1,000 / 1.04^5 = $821.93. $783.53 uses 5% and $833.33 uses simple interest (1,000 / 1.20)."],
 ["If the yield on a zero-coupon government bond is negative, the bond's price is:", ["below its face value.", "equal to its face value.", "above its face value."], 2, "Discounting at a negative rate makes the present value larger than the future payment, so the bond trades above face value."],
 ["A three-year bond with a face value of 100 pays an annual coupon of 5%. If the yield to maturity is 6%, the price is closest to:", ["97.33", "100.00", "102.78"], 0, "5/1.06 + 5/1.06² + 105/1.06³ = 4.72 + 4.45 + 88.16 = 97.33. A coupon below the yield means the bond trades at a discount."],
 ["A preferred share pays a fixed annual dividend of $4.00 forever. If the required return is 8%, its value is closest to:", ["$32.00", "$46.30", "$50.00"], 2, "A level perpetuity is worth D / r = 4.00 / 0.08 = $50.00."],
 ["A company has just paid a dividend of $2.00 per share. Dividends are expected to grow at 5% forever and the required return is 9%. The value of the share is closest to:", ["$23.33", "$50.00", "$52.50"], 2, "D₁ = 2.00 × 1.05 = 2.10. Value = 2.10 / (0.09 − 0.05) = $52.50. Using the dividend just paid gives $50.00, which is the common error."],
 ["A share trades at $40.00. Next year's dividend is expected to be $2.00 and dividends are expected to grow at 4% indefinitely. The required return implied by the price is closest to:", ["5.0%", "8.8%", "9.0%"], 2, "r = D₁ / P₀ + g = 2.00 / 40.00 + 0.04 = 9.0%."],
 ["A share trades at $25.00 and is expected to pay a dividend of $1.50 next year. If investors require a 10% return, the constant dividend growth rate implied by the price is closest to:", ["4.0%", "6.0%", "16.0%"], 0, "g = r − D₁ / P₀ = 0.10 − 1.50 / 25.00 = 0.10 − 0.06 = 4.0%."],
 ["A $100,000 loan is repaid in five equal annual payments at an interest rate of 6%. The annual payment is closest to:", ["$21,200", "$23,740", "$26,000"], 1, "PMT = 100,000 × 0.06 / (1 − 1.06^−5) = 6,000 / 0.25274 ≈ $23,740."],
 ["The one-year spot rate is 3% and the two-year spot rate is 4%. The one-year rate, one year forward, is closest to:", ["3.50%", "4.00%", "5.01%"], 2, "(1.04)² / 1.03 − 1 = 1.0816 / 1.03 − 1 ≈ 5.01%. Investing for two years must equal investing for one year and rolling over at the forward rate."],
 ["For a fully amortizing loan with level payments, as the loan approaches maturity the interest portion of each payment:", ["decreases.", "increases.", "stays the same."], 0, "Interest is charged on the outstanding balance, which falls with every payment, so each payment contains less interest and more principal."],
]))

R.append(dict(id="sm", n="Statistical Measures of Asset Returns", k="STATISTICS", w=3, c="#c0563f",
terms=[
 ["Measure of central tendency", "Merkezi eğilim ölçüsü", "A single value that locates the centre of a data set, such as the mean, median or mode.", "Bir veri setinin merkezini gösteren tek değer; ortalama, medyan veya mod gibi."],
 ["Median", "Medyan (ortanca)", "The middle observation when data are sorted; half the observations lie above it and half below.", "Veriler sıralandığında ortada kalan gözlem; gözlemlerin yarısı üstünde, yarısı altındadır."],
 ["Outlier", "Aykırı değer", "An observation that lies far from the rest of the data.", "Verilerin geri kalanından çok uzakta bulunan gözlem."],
 ["Trimmed mean", "Budanmış ortalama", "A mean computed after removing a stated percentage of the lowest and highest observations.", "En düşük ve en yüksek gözlemlerin belirli bir yüzdesi çıkarıldıktan sonra hesaplanan ortalama."],
 ["Winsorized mean", "Winsorize edilmiş ortalama", "A mean computed after replacing extreme observations with the values at chosen percentiles.", "Uç gözlemler, seçilen yüzdeliklerdeki değerlerle değiştirildikten sonra hesaplanan ortalama."],
 ["Quantile", "Kantil", "A value at or below which a stated fraction of the data lies; quartiles, quintiles, deciles and percentiles are examples.", "Verinin belirli bir kesrinin altında veya ona eşit kaldığı değer; çeyreklik, beşte birlik, ondalık ve yüzdelik örnekleridir."],
 ["Mean absolute deviation (MAD)", "Ortalama mutlak sapma", "The average of the absolute distances of observations from their mean.", "Gözlemlerin ortalamadan mutlak uzaklıklarının ortalaması."],
 ["Standard deviation", "Standart sapma", "The square root of the variance; it measures dispersion in the same units as the data.", "Varyansın karekökü; dağılımı veriyle aynı birimde ölçer."],
 ["Target downside deviation", "Hedef aşağı yönlü sapma", "Dispersion measured using only the observations that fall below a chosen target return.", "Yalnızca seçilen hedef getirinin altında kalan gözlemler kullanılarak ölçülen dağılım."],
 ["Coefficient of variation (CV)", "Değişim katsayısı", "Standard deviation divided by the mean; risk per unit of return.", "Standart sapmanın ortalamaya bölümü; birim getiri başına risk."],
 ["Skewness", "Çarpıklık", "A measure of how asymmetric a distribution is around its mean.", "Bir dağılımın ortalaması etrafında ne kadar asimetrik olduğunun ölçüsü."],
 ["Kurtosis", "Basıklık", "A measure of how much of a distribution's weight sits in its tails compared with a normal distribution.", "Normal dağılıma kıyasla, dağılımın ağırlığının ne kadarının kuyruklarda olduğunun ölçüsü."],
 ["Correlation coefficient", "Korelasyon katsayısı", "Covariance divided by the product of the two standard deviations; it ranges from −1 to +1.", "Kovaryansın iki standart sapmanın çarpımına bölümü; −1 ile +1 arasında değer alır."],
],
notes="""<h3>Locating the centre</h3>
<ul>
<li><b>Arithmetic mean:</b> uses every observation, so a single extreme value can pull it a long way.</li>
<li><b>Median:</b> the middle value of the sorted data. With an even number of observations it is the average of the two middle values. It is not affected by how extreme the outliers are.</li>
<li><b>Mode:</b> the most frequent value. A distribution can have one mode, several, or none.</li>
</ul>
<h3>Dealing with outliers</h3>
<ul>
<li>First ask whether the outlier is an error. If it is, correct or remove it. If it is a genuine observation, either keep it or reduce its influence:</li>
<li><b>Trimmed mean:</b> drop the most extreme observations at each end. A 5% trimmed mean removes the lowest 2.5% and the highest 2.5%.</li>
<li><b>Winsorized mean:</b> keep the number of observations but replace the extremes with the nearest retained value. A 90% winsorized mean sets everything below the 5th percentile equal to the 5th percentile, and everything above the 95th equal to the 95th.</li>
</ul>
<h3>Quantiles</h3>
<p class="f">position of the y-th percentile: L<sub>y</sub> = (n + 1) × y / 100</p>
<ul>
<li>Quartiles split sorted data into four parts, quintiles into five, deciles into ten, percentiles into a hundred.</li>
<li>The <b>interquartile range</b> is Q3 − Q1 and contains the middle 50% of observations. A box-and-whisker plot draws it as the box.</li>
</ul>
<h3>Dispersion</h3>
<p class="f">sample variance: s² = Σ(X<sub>i</sub> − X̄)² / (n − 1) &nbsp;&nbsp;&nbsp; sample standard deviation: s = √s²</p>
<p class="f">MAD = Σ|X<sub>i</sub> − X̄| / n</p>
<ul>
<li><b>Range</b> is maximum minus minimum; it uses only two observations.</li>
<li>Dividing by n − 1 instead of n makes the sample variance an unbiased estimate of the population variance.</li>
<li><b>Target downside deviation</b> counts only shortfalls below a target B: square the shortfalls, sum them, divide by n − 1 (all observations, not just the shortfalls) and take the square root.</li>
<li><b>Coefficient of variation</b> = s / X̄. It has no units, so it compares dispersion across data sets with different means or scales. Lower means less risk per unit of return.</li>
</ul>
<h3>Shape: skewness and kurtosis</h3>
<div class="tbl"><table>
<tr><th>Shape</th><th>Tail</th><th>Typical ordering</th></tr>
<tr><td>Positively skewed</td><td>Long right tail, a few large gains</td><td>mode &lt; median &lt; mean</td></tr>
<tr><td>Symmetric</td><td>Both tails alike</td><td>mean = median = mode</td></tr>
<tr><td>Negatively skewed</td><td>Long left tail, a few large losses</td><td>mean &lt; median &lt; mode</td></tr>
</table></div>
<ul>
<li>A normal distribution has kurtosis of 3. <b>Excess kurtosis</b> is kurtosis minus 3.</li>
<li><b>Leptokurtic</b> (excess &gt; 0): more peaked with fatter tails, so extreme outcomes are more likely than a normal distribution suggests. <b>Platykurtic</b> (excess &lt; 0): flatter with thinner tails. <b>Mesokurtic</b>: same as normal.</li>
</ul>
<div class="trap"><b>Exam trap</b>Risk models that assume normality understate the chance of large losses when returns are negatively skewed or leptokurtic.</div>
<h3>Covariance and correlation</h3>
<p class="f">sample covariance: s<sub>XY</sub> = Σ(X<sub>i</sub> − X̄)(Y<sub>i</sub> − Ȳ) / (n − 1)</p>
<p class="f">correlation: r<sub>XY</sub> = s<sub>XY</sub> / (s<sub>X</sub> × s<sub>Y</sub>)</p>
<ul>
<li>Covariance shows direction but its size depends on the units. Correlation rescales it to between −1 and +1.</li>
<li>Correlation measures only <b>linear</b> association. Two variables can be strongly related in a non-linear way and still have a correlation near zero.</li>
<li>Correlation is sensitive to outliers and does not imply causation. <b>Spurious correlation</b> can arise by chance, from dividing two variables by a common third one, or because both depend on a third variable.</li>
</ul>""",
qs=[
 ["Which measure of central tendency is least affected by a small number of extreme observations?", ["Mean", "Median", "Range"], 1, "The median depends only on the middle of the sorted data, so the size of extreme values does not move it. The range is a measure of dispersion, not central tendency."],
 ["The sample variance of the four observations 2, 4, 6 and 8 is closest to:", ["2.58", "5.00", "6.67"], 2, "The mean is 5. Squared deviations sum to 9 + 1 + 1 + 9 = 20. Sample variance = 20 / (4 − 1) = 6.67. Dividing by 4 gives 5.00, the population variance."],
 ["The mean absolute deviation of the four observations 2, 4, 6 and 8 is closest to:", ["1.6", "2.0", "2.6"], 1, "Absolute deviations from the mean of 5 are 3, 1, 1 and 3. Their average is 8 / 4 = 2.0."],
 ["Fund A has a mean return of 8% and a standard deviation of 12%. Fund B has a mean return of 10% and a standard deviation of 18%. Which fund has less risk per unit of return?", ["Fund A, with a coefficient of variation of 1.5", "Fund B, with a coefficient of variation of 1.8", "Fund B, with a coefficient of variation of 0.6"], 0, "CV = standard deviation / mean. Fund A: 12 / 8 = 1.5. Fund B: 18 / 10 = 1.8. The lower coefficient of variation means less dispersion per unit of return."],
 ["For a positively skewed distribution with a single mode, which relationship is most likely?", ["Mean < median < mode", "Mode < median < mean", "Median < mode < mean"], 1, "The long right tail pulls the mean above the median, and the median lies above the mode."],
 ["Compared with a normal distribution, a return distribution with positive excess kurtosis has:", ["thinner tails.", "fatter tails.", "a longer right tail."], 1, "Positive excess kurtosis (leptokurtic) means more weight in both tails, so extreme outcomes occur more often than under a normal distribution."],
 ["Annual returns for four years were 5%, −3%, 1% and −7%. Using a target return of 0%, the target downside deviation is closest to:", ["3.81%", "4.40%", "5.39%"], 1, "Only the shortfalls count: (−3)² + (−7)² = 58. Divide by n − 1 = 3 to get 19.33 and take the square root: 4.40%."],
 ["The covariance between the returns of two shares is 0.0054. Their standard deviations are 8% and 9%. The correlation is closest to:", ["0.54", "0.65", "0.75"], 2, "Correlation = 0.0054 / (0.08 × 0.09) = 0.0054 / 0.0072 = 0.75."],
 ["A sorted sample contains 24 observations. Using the standard location formula, the 60th percentile is found at observation:", ["15", "16", "17"], 0, "L = (n + 1) × y / 100 = 25 × 0.60 = 15, so the 60th percentile is the 15th observation."],
 ["An analyst replaces every observation below the 5th percentile with the 5th percentile value, and every observation above the 95th percentile with the 95th percentile value, then computes the mean. This is a:", ["trimmed mean.", "harmonic mean.", "winsorized mean."], 2, "Winsorizing replaces extreme values and keeps the sample size. Trimming removes them."],
]))
