# CFA Level I · Fixed Income · readings 11–14. Original study notes and questions.
R = []

R.append(dict(id="dm", n="Yield-Based Bond Duration Measures and Properties", k="DURATION", w=2, c="#c0563f",
terms=[
 ["Modified duration", "Düzeltilmiş süre", "The approximate percentage change in a bond's price for a 1% change in its yield.", "Getirideki %1'lik değişime karşılık tahvil fiyatındaki yaklaşık yüzde değişim."],
 ["Approximate modified duration", "Yaklaşık düzeltilmiş süre", "Modified duration estimated by repricing the bond for a small rise and fall in yield.", "Tahvilin getirideki küçük artış ve azalış için yeniden fiyatlanmasıyla tahmin edilen düzeltilmiş süre."],
 ["Money duration", "Parasal süre", "Modified duration multiplied by the full price of the position; the change in value for a 1% change in yield.", "Düzeltilmiş sürenin pozisyonun kirli fiyatıyla çarpımı; getirideki %1'lik değişime karşılık değer değişimi."],
 ["Price value of a basis point (PVBP)", "Baz puan değeri", "The change in a bond's value for a one basis point change in yield.", "Getirideki bir baz puanlık değişime karşılık tahvil değerindeki değişim."],
 ["Effective duration", "Efektif süre", "A duration measure based on shifts in the benchmark curve; needed for bonds with embedded options.", "Gösterge eğrideki kaymalara dayanan süre ölçüsü; gömülü opsiyonlu tahviller için gereklidir."],
 ["Interest rate risk", "Faiz oranı riski", "The risk that changes in interest rates change the value of a bond.", "Faiz oranlarındaki değişimlerin tahvilin değerini değiştirmesi riski."],
 ["Basis point", "Baz puan", "One hundredth of a percentage point (0.01%).", "Yüzde birin yüzde biri (%0,01)."],
],
notes="""<h3>Measures</h3>
<p class="f">modified duration = Macaulay duration / (1 + r), with r the yield per period</p>
<p class="f">%ΔP ≈ −modified duration × Δyield</p>
<p class="f">approximate modified duration = (PV<sub>−</sub> − PV<sub>+</sub>) / (2 × Δyield × PV<sub>0</sub>)</p>
<ul>
<li>With semi-annual payments, divide Macaulay duration (in periods) by (1 + yield/2), then by 2 to annualize.</li>
<li>Macaulay duration is measured in years; modified duration is a sensitivity (percent per percent).</li>
</ul>
<p class="f">money duration = modified duration × full price of the position</p>
<p class="f">PVBP = (PV<sub>−</sub> − PV<sub>+</sub>) / 2, for a 1 bp shift; or money duration × 0.0001</p>
<h3>What makes duration higher</h3>
<div class="tbl"><table>
<tr><th>Feature</th><th>Effect on duration</th></tr>
<tr><td>Longer maturity</td><td>Higher (almost always)</td></tr>
<tr><td>Lower coupon</td><td>Higher</td></tr>
<tr><td>Lower yield</td><td>Higher</td></tr>
<tr><td>Zero coupon</td><td>Macaulay duration = maturity</td></tr>
<tr><td>Floating-rate note</td><td>Close to the time to the next reset</td></tr>
<tr><td>Call option</td><td>Lower, especially when rates are low</td></tr>
<tr><td>Put option</td><td>Lower, especially when rates are high</td></tr>
</table></div>
<ul>
<li>For long-dated discount bonds, duration can fall slightly as maturity lengthens, but this is rare in practice.</li>
<li>Yield duration measures assume the bond's cash flows do not change when rates change. For bonds with options, use <b>effective duration</b>.</li>
</ul>
<div class="trap"><b>Exam trap</b>Duration is a linear estimate. For large yield changes it understates price rises and overstates price falls; convexity corrects this.</div>""",
qs=[
 ["A bond has a Macaulay duration of 5.0 and an annual yield to maturity of 4%. Its modified duration is closest to:", ["4.81", "5.00", "5.20"], 0, "5.0 / 1.04 = 4.81."],
 ["A bond is priced at 100. Its price would be 102.5 if its yield fell by 50 bp and 97.6 if its yield rose by 50 bp. Its approximate modified duration is closest to:", ["2.45", "4.90", "9.80"], 1, "(102.5 − 97.6) / (2 × 0.005 × 100) = 4.9 / 1.0 = 4.90."],
 ["A bond has a modified duration of 6.0. If its yield rises by 50 bp, its price will change by approximately:", ["−6.00%", "−3.00%", "−0.50%"], 1, "%ΔP ≈ −6.0 × 0.005 = −3.0%."],
 ["The Macaulay duration of a seven-year zero-coupon bond is:", ["less than 7 years.", "exactly 7 years.", "more than 7 years."], 1, "All of the bond's value is received at maturity, so its weighted average time is the maturity."],
 ["All else equal, a bond with a lower coupon rate has:", ["a lower duration.", "a higher duration.", "the same duration."], 1, "Less of its value comes early, so the weighted average time to cash flows is longer."],
 ["A bond position has a money duration of $10,000,000. Its price value of a basis point is closest to:", ["$100", "$1,000", "$10,000"], 1, "PVBP = money duration × 0.0001 = $1,000."],
 ["All else equal, when a bond's yield rises, its duration:", ["falls.", "rises.", "is unchanged."], 0, "Higher yields reduce the weight of distant cash flows in present value terms."],
 ["The duration of a floating-rate note is approximately equal to the:", ["time to maturity.", "time to the next coupon reset.", "duration of a fixed-rate bond with the same maturity."], 1, "At each reset the coupon adjusts to market rates, so price sensitivity extends only to the next reset."],
]))

R.append(dict(id="cv", n="Yield-Based Bond Convexity and Portfolio Properties", k="CONVEXITY", w=2, c="#8a5cc2",
terms=[
 ["Convexity", "Dışbükeylik", "A measure of the curvature of the price-yield relationship, the second-order effect of yield changes on price.", "Fiyat-getiri ilişkisinin eğriliğinin ölçüsü; getiri değişiminin fiyata ikinci derece etkisi."],
 ["Approximate convexity", "Yaklaşık dışbükeylik", "Convexity estimated by repricing the bond for a small rise and fall in yield.", "Tahvilin getirideki küçük artış ve azalış için yeniden fiyatlanmasıyla tahmin edilen dışbükeylik."],
 ["Positive convexity", "Pozitif dışbükeylik", "Prices rise more when yields fall than they drop when yields rise by the same amount.", "Getiriler düştüğünde fiyatların, aynı ölçüde yükseldiğinde düştüğünden daha fazla artması."],
 ["Negative convexity", "Negatif dışbükeylik", "Price gains are smaller than price losses for equal yield changes; typical of callable bonds at low yields.", "Eşit getiri değişimlerinde fiyat kazançlarının kayıplardan küçük olması; düşük getiride erken itfa edilebilir tahvillere özgüdür."],
 ["Portfolio duration", "Portföy süresi", "The market-value-weighted average of the durations of the bonds in a portfolio.", "Portföydeki tahvillerin sürelerinin piyasa değeriyle ağırlıklı ortalaması."],
 ["Parallel shift", "Paralel kayma", "A change in yields of the same size at every maturity.", "Tüm vadelerde aynı büyüklükte getiri değişimi."],
 ["Money convexity", "Parasal dışbükeylik", "Convexity multiplied by the full price of the position.", "Dışbükeyliğin pozisyonun kirli fiyatıyla çarpımı."],
],
notes="""<h3>Adding convexity to the estimate</h3>
<p class="f">%ΔP ≈ −modified duration × Δy + ½ × convexity × (Δy)<sup>2</sup></p>
<p class="f">approximate convexity = (PV<sub>−</sub> + PV<sub>+</sub> − 2 × PV<sub>0</sub>) / ((Δy)<sup>2</sup> × PV<sub>0</sub>)</p>
<ul>
<li>For an option-free bond the convexity term is always positive, so it raises the estimate whether yields rise or fall: a smaller loss, a larger gain.</li>
<li>Duration alone is a straight-line approximation of a curve; convexity accounts for the curve.</li>
</ul>
<h3>Properties</h3>
<ul>
<li>Convexity is higher for longer maturities, lower coupons and lower yields, and for portfolios with more dispersed cash flows (a barbell rather than a bullet).</li>
<li>Investors value convexity: of two bonds with the same duration and yield, the more convex one outperforms when rates move. In efficient markets it therefore has a slightly higher price and lower yield.</li>
<li><b>Callable bonds</b> show negative convexity when yields fall toward the level at which a call is likely: the price is capped near the call price.</li>
<li><b>Putable bonds</b> have more positive convexity than straight bonds when yields rise.</li>
</ul>
<h3>Portfolios</h3>
<p class="f">portfolio duration ≈ Σ w<sub>i</sub> × D<sub>i</sub>, with w<sub>i</sub> the market value weights</p>
<ul>
<li>The weighted average is easy to calculate and works for bonds with options, but assumes a <b>parallel shift</b> in the yield curve.</li>
<li>The alternative, using the portfolio's cash flow yield, is theoretically better but cannot handle embedded options.</li>
<li>Money duration and PVBP of a portfolio are the sums of those of its holdings.</li>
</ul>
<div class="trap"><b>Exam trap</b>Convexity is multiplied by (Δy)² expressed as a decimal: a 1% change gives 0.0001, not 1.</div>""",
qs=[
 ["A bond has a modified duration of 7.0 and convexity of 60. If its yield rises by 100 bp, its price will change by approximately:", ["−7.30%", "−7.00%", "−6.70%"], 2, "−7.0 × 0.01 + 0.5 × 60 × 0.0001 = −7.0% + 0.3% = −6.70%."],
 ["A bond has a modified duration of 7.0 and convexity of 60. If its yield falls by 100 bp, its price will change by approximately:", ["6.70%", "7.00%", "7.30%"], 2, "+7.0% + 0.3% = +7.30%. The convexity term adds to the gain."],
 ["A bond is priced at 100. Its price would be 102.5 if its yield fell by 50 bp and 97.6 if its yield rose by 50 bp. Its approximate convexity is closest to:", ["4", "40", "400"], 1, "(102.5 + 97.6 − 200) / (0.005² × 100) = 0.1 / 0.0025 = 40."],
 ["A portfolio holds 60% of its value in bonds with a duration of 4 and 40% in bonds with a duration of 9. Its duration is closest to:", ["5.0", "6.0", "6.5"], 1, "0.6 × 4 + 0.4 × 9 = 2.4 + 3.6 = 6.0."],
 ["Using the weighted average of individual bond durations as a portfolio's duration assumes that:", ["all bonds have the same maturity.", "the yield curve shifts in parallel.", "the portfolio contains no callable bonds."], 1, "Each bond's yield is assumed to change by the same amount."],
 ["For an option-free bond, ignoring convexity when estimating the price effect of a large decrease in yield will:", ["overstate the price increase.", "understate the price increase.", "have no effect on the estimate."], 1, "The convexity term is positive, so leaving it out underestimates the gain."],
 ["A callable bond is most likely to exhibit negative convexity when:", ["yields are well above the coupon rate.", "the call protection period is long.", "yields fall close to the level at which the bond is likely to be called."], 2, "Near the call price, further falls in yield add little to the price, so the price-yield curve bends the wrong way."],
 ["Two option-free bonds have the same duration and yield. The bond with greater convexity will most likely:", ["perform better when yields change.", "perform worse when yields change.", "perform the same when yields change."], 0, "Higher convexity means larger gains when yields fall and smaller losses when they rise."],
]))

R.append(dict(id="cr", n="Curve-Based and Empirical Fixed-Income Risk Measures", k="EFFECTIVE", w=1, c="#b8860b",
terms=[
 ["Effective duration", "Efektif süre", "Price sensitivity to a parallel shift in the benchmark yield curve, allowing cash flows to change.", "Nakit akışlarının değişmesine izin vererek gösterge getiri eğrisindeki paralel kaymaya fiyat duyarlılığı."],
 ["Effective convexity", "Efektif dışbükeylik", "Second-order price sensitivity to shifts in the benchmark curve, for bonds whose cash flows depend on rates.", "Nakit akışları faize bağlı tahvillerde gösterge eğrideki kaymalara ikinci derece fiyat duyarlılığı."],
 ["Key rate duration", "Anahtar vade süresi", "Price sensitivity to a change in the benchmark rate at one maturity only.", "Yalnızca bir vadedeki gösterge faiz değişimine fiyat duyarlılığı."],
 ["Shaping risk", "Eğri biçimi riski", "The risk from non-parallel changes in the yield curve, such as steepening or flattening.", "Getiri eğrisindeki dikleşme veya yassılaşma gibi paralel olmayan değişimlerden kaynaklanan risk."],
 ["Empirical duration", "Ampirik süre", "Duration estimated from the observed relationship between bond prices and benchmark yields.", "Tahvil fiyatları ile gösterge getiriler arasındaki gözlenen ilişkiden tahmin edilen süre."],
 ["Analytical duration", "Analitik süre", "Duration calculated from a formula or pricing model.", "Bir formül veya fiyatlama modeliyle hesaplanan süre."],
],
notes="""<h3>Why curve-based measures</h3>
<ul>
<li>Yield duration assumes fixed cash flows. When a bond has an embedded option, or is a mortgage security with prepayments, cash flows change with rates and the bond has no stable yield to maturity.</li>
<li>Effective measures shift the <b>benchmark curve</b> up and down and reprice the bond with a model.</li>
</ul>
<p class="f">effective duration = (PV<sub>−</sub> − PV<sub>+</sub>) / (2 × ΔCurve × PV<sub>0</sub>)</p>
<p class="f">effective convexity = (PV<sub>−</sub> + PV<sub>+</sub> − 2 × PV<sub>0</sub>) / ((ΔCurve)<sup>2</sup> × PV<sub>0</sub>)</p>
<h3>Bonds with options</h3>
<div class="tbl"><table>
<tr><th></th><th>Callable</th><th>Putable</th></tr>
<tr><td>Effective duration vs straight bond</td><td>Lower, especially when rates fall</td><td>Lower, especially when rates rise</td></tr>
<tr><td>Effective convexity</td><td>Can be negative at low rates</td><td>Always positive</td></tr>
</table></div>
<h3>Key rate durations</h3>
<ul>
<li>Shift the curve at one maturity, keeping the others fixed. The sum of key rate durations equals effective duration.</li>
<li>They show exposure to <b>shaping risk</b>: two portfolios with the same effective duration can react very differently if the curve steepens or flattens.</li>
</ul>
<h3>Empirical duration</h3>
<ul>
<li>Estimated by regressing bond price changes on benchmark yield changes.</li>
<li>For high-yield bonds, empirical duration is usually <b>lower</b> than analytical duration: when benchmark yields rise in a strong economy, credit spreads often narrow, partly offsetting the effect. For government bonds the two measures are similar.</li>
</ul>
<div class="trap"><b>Exam trap</b>Effective duration is required for bonds with embedded options. Modified duration ignores that cash flows change when rates change.</div>""",
qs=[
 ["A callable bond is priced at 100. A model gives prices of 101.5 if the benchmark curve shifts down by 25 bp and 98.0 if it shifts up by 25 bp. The effective duration is closest to:", ["3.5", "7.0", "14.0"], 1, "(101.5 − 98.0) / (2 × 0.0025 × 100) = 3.5 / 0.5 = 7.0."],
 ["The most appropriate measure of interest rate risk for a bond with an embedded call option is:", ["Macaulay duration.", "modified duration.", "effective duration."], 2, "Effective duration allows for the change in cash flows when rates change."],
 ["The sum of a bond's key rate durations equals its:", ["effective duration.", "Macaulay duration.", "empirical duration."], 0, "Key rate durations break effective duration down by maturity."],
 ["Key rate durations are most useful for measuring a portfolio's exposure to:", ["credit risk.", "shaping risk.", "liquidity risk."], 1, "They show how the portfolio reacts to non-parallel changes in the curve."],
 ["Compared with its analytical duration, the empirical duration of a high-yield bond is most likely:", ["lower.", "higher.", "the same."], 0, "Credit spreads tend to narrow when benchmark rates rise in a strong economy, damping the price reaction."],
 ["When interest rates fall toward the call price, the effective convexity of a callable bond is most likely:", ["zero.", "positive.", "negative."], 2, "The call caps price gains, producing negative convexity."],
 ["Compared with an otherwise identical option-free bond, a putable bond's effective duration when rates rise sharply is:", ["lower.", "higher.", "the same."], 0, "The put limits the price fall, so the bond behaves like a shorter bond."],
 ["Effective duration is calculated using shifts in the:", ["bond's own yield to maturity.", "benchmark yield curve.", "issuer's credit spread."], 1, "Bonds with options lack a stable YTM, so the benchmark curve is shifted and the bond repriced with a model."],
]))

R.append(dict(id="ck", n="Credit Risk", k="CREDIT", w=2, c="#c2417a",
terms=[
 ["Default risk", "Temerrüt riski", "The risk that the borrower fails to pay interest or principal in full and on time.", "Borçlunun faiz veya anaparayı tam ve zamanında ödeyememesi riski."],
 ["Probability of default (POD)", "Temerrüt olasılığı", "The likelihood that the borrower defaults within a given period.", "Borçlunun belirli bir dönemde temerrüde düşme olasılığı."],
 ["Loss given default (LGD)", "Temerrüt halinde kayıp", "The share of the exposure lost if default occurs; one minus the recovery rate.", "Temerrüt olursa kaybedilen pay; bir eksi geri kazanım oranı."],
 ["Recovery rate", "Geri kazanım oranı", "The share of the exposure recovered after default.", "Temerrütten sonra geri kazanılan pay."],
 ["Expected loss", "Beklenen kayıp", "Probability of default multiplied by loss given default.", "Temerrüt olasılığı ile temerrüt halinde kaybın çarpımı."],
 ["Credit spread", "Kredi risk primi (spread)", "The yield on a risky bond minus the yield on a comparable government bond.", "Riskli bir tahvilin getirisinden benzer devlet tahvili getirisinin çıkarılmasıyla bulunan fark."],
 ["Downgrade risk", "Not düşürme riski", "The risk that a lower credit rating raises the bond's spread and lowers its price.", "Kredi notunun düşürülmesinin tahvilin primini artırıp fiyatını düşürmesi riski."],
 ["Notching", "Kademeli not farkı", "Rating individual issues above or below the issuer rating according to their seniority and security.", "Tek tek ihraçlara, sıralama ve teminatlarına göre ihraççı notunun üstünde veya altında not verilmesi."],
 ["Spread risk", "Prim riski", "The risk that changes in credit spreads change the bond's price.", "Kredi primlerindeki değişimlerin tahvilin fiyatını değiştirmesi riski."],
],
notes="""<h3>Measuring credit risk</h3>
<p class="f">expected loss = probability of default × loss given default</p>
<p class="f">loss given default = 1 − recovery rate</p>
<ul>
<li>Recovery depends on seniority and collateral, and is lower when many companies default at the same time, as in recessions.</li>
<li><b>Credit spread</b> compensates for expected loss and for the uncertainty of losses, plus a liquidity premium.</li>
</ul>
<h3>Credit ratings</h3>
<ul>
<li>Investment grade: AAA to BBB− (Baa3). High yield (speculative): BB+ (Ba1) and below.</li>
<li><b>Issuer ratings</b> refer to senior unsecured debt; <b>issue ratings</b> are notched up for secured debt and down for subordinated debt, more so for lower-rated issuers.</li>
<li>Limitations: ratings change slowly and may lag the market; agencies can make mistakes; some risks (fraud, litigation, event risk) are hard to rate.</li>
</ul>
<h3>Spread risk</h3>
<ul>
<li>Spreads widen when the economy weakens, when an issuer is downgraded, and when liquidity dries up. Lower-rated bonds have wider and more volatile spreads.</li>
<li>Price effect of a spread change:</li>
</ul>
<p class="f">%ΔP ≈ −modified duration × Δspread + ½ × convexity × (Δspread)<sup>2</sup></p>
<ul>
<li>A liquidity component appears in wider bid-ask spreads for smaller, less frequently traded issues.</li>
</ul>
<h3>Assessing credit</h3>
<ul>
<li>Traditional framework: <b>capacity</b> to repay, <b>capital</b> (financial resources and leverage), <b>collateral</b>, <b>covenants</b>; some also add <b>character</b> (management quality and integrity).</li>
<li>Sources of repayment: operating cash flow, refinancing, sale of collateral, and guarantees.</li>
</ul>
<div class="trap"><b>Exam trap</b>The recovery rate is not the loss. A 40% recovery means a 60% loss given default.</div>""",
qs=[
 ["A bond has a 2% probability of default and an expected recovery rate of 40%. Its expected loss is closest to:", ["0.80%", "1.20%", "2.00%"], 1, "LGD = 60%. Expected loss = 2% × 60% = 1.20%."],
 ["A bond has a modified duration of 5 and convexity of 40. If its credit spread widens by 100 bp, its price will change by approximately:", ["−5.20%", "−5.00%", "−4.80%"], 2, "−5 × 0.01 + 0.5 × 40 × 0.0001 = −5.0% + 0.2% = −4.80%."],
 ["The lowest credit rating considered investment grade is:", ["BB+", "BBB−", "BBB+"], 1, "BBB− (or Baa3) is the lowest investment-grade rating."],
 ["A subordinated bond of an issuer with a BB senior unsecured rating will most likely be rated:", ["above BB.", "BB.", "below BB."], 2, "Subordinated issues are notched below the issuer rating because their expected recovery is lower."],
 ["Credit spreads typically widen most during:", ["economic expansions.", "economic contractions.", "periods of rising credit ratings."], 1, "Default expectations rise and investors demand more compensation for risk in downturns."],
 ["A limitation of credit ratings as a measure of credit risk is that they:", ["are always identical across rating agencies.", "change more slowly than market prices.", "include liquidity risk."], 1, "Ratings tend to lag changes in an issuer's situation, while spreads react immediately."],
 ["Compared with investment-grade bonds, high-yield bonds' credit spreads are most likely:", ["narrower and less volatile.", "wider and more volatile.", "wider and less volatile."], 1, "Higher default risk produces larger spreads that react more strongly to the economy."],
 ["Which of the following is least likely one of the traditional factors in credit analysis?", ["Capacity", "Collateral", "Convexity"], 2, "The traditional factors include capacity, capital, collateral and covenants. Convexity is an interest rate risk measure."],
]))
