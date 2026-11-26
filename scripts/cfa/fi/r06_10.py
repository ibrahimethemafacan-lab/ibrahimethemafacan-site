# CFA Level I · Fixed Income · readings 6–10. Original study notes and questions.
R = []

R.append(dict(id="bv", n="Fixed-Income Bond Valuation: Prices and Yields", k="PRICING", w=2, c="#2f8f5b",
terms=[
 ["Market discount rate", "Piyasa iskonto oranı", "The rate investors require on a bond given its risk; used to discount its cash flows.", "Yatırımcıların tahvilin riski karşılığında istediği oran; nakit akışlarını iskontolamakta kullanılır."],
 ["Yield to maturity (YTM)", "Vadeye kadar getiri", "The single discount rate that makes the present value of a bond's cash flows equal to its price.", "Tahvilin nakit akışlarının bugünkü değerini fiyatına eşitleyen tek iskonto oranı."],
 ["Premium bond", "Primli tahvil", "A bond priced above par because its coupon rate exceeds the market discount rate.", "Kupon oranı piyasa iskonto oranından yüksek olduğu için nominalin üzerinde fiyatlanan tahvil."],
 ["Discount bond", "İskontolu tahvil", "A bond priced below par because its coupon rate is below the market discount rate.", "Kupon oranı piyasa iskonto oranından düşük olduğu için nominalin altında fiyatlanan tahvil."],
 ["Accrued interest", "İşlemiş faiz", "The part of the next coupon earned by the seller since the last coupon date.", "Son kupon tarihinden bu yana satıcının hak ettiği, bir sonraki kuponun kısmı."],
 ["Flat price", "Temiz fiyat", "The quoted bond price, excluding accrued interest.", "İşlemiş faiz hariç kote edilen tahvil fiyatı."],
 ["Full price", "Kirli fiyat", "The price actually paid: flat price plus accrued interest.", "Fiilen ödenen fiyat: temiz fiyat artı işlemiş faiz."],
 ["Matrix pricing", "Matris fiyatlama", "Estimating the price of an illiquid bond from the yields of comparable bonds.", "Likit olmayan bir tahvilin fiyatını benzer tahvillerin getirilerinden tahmin etme."],
 ["Pull to par", "Nominale yakınsama", "The movement of a bond's price toward par as it approaches maturity, if the yield is unchanged.", "Getiri değişmezse tahvil fiyatının vadeye yaklaştıkça nominale doğru hareketi."],
],
notes="""<h3>Price as present value</h3>
<p class="f">P = C/(1+r) + C/(1+r)<sup>2</sup> + … + (C + FV)/(1+r)<sup>N</sup></p>
<ul>
<li>If coupon rate = market discount rate, price = par. Coupon above the discount rate: premium. Below: discount.</li>
<li>With semi-annual coupons, use half the coupon and half the annual rate, and twice the number of periods.</li>
</ul>
<h3>Five price-yield relationships (option-free bonds)</h3>
<ul>
<li>1. <b>Inverse:</b> price falls when yield rises.</li>
<li>2. <b>Convexity:</b> for the same change in yield, the price rise is larger than the price fall.</li>
<li>3. <b>Coupon effect:</b> lower coupon means greater price sensitivity.</li>
<li>4. <b>Maturity effect:</b> longer maturity generally means greater sensitivity.</li>
<li>5. <b>Constant-yield path:</b> premium and discount bonds move toward par as maturity approaches.</li>
</ul>
<h3>Prices between coupon dates</h3>
<p class="f">accrued interest = coupon × (days since last coupon / days in coupon period)</p>
<p class="f">full price = flat price + accrued interest</p>
<ul>
<li>Corporate bonds commonly use a 30/360 day count; government bonds actual/actual.</li>
<li>The full price can also be found by moving the price at the last coupon date forward: PV<sub>full</sub> = PV × (1 + r)<sup>t/T</sup>.</li>
<li>Quotes use the flat price so that the price does not jump on coupon dates.</li>
</ul>
<h3>Matrix pricing</h3>
<ul>
<li>For a bond with no recent trades, take yields of comparable bonds (similar rating, maturity, coupon), interpolate a yield for the bond, and price it with that yield.</li>
<li>Also used to set the coupon on a new issue: benchmark yield + estimated spread.</li>
</ul>
<div class="trap"><b>Exam trap</b>A zero-coupon bond is more sensitive to rate changes than a coupon bond with the same maturity, because all its value is at the end.</div>""",
qs=[
 ["A three-year bond with a par value of 100 pays an annual coupon of 5%. If the market discount rate is 4%, its price is closest to:", ["97.33", "100.00", "102.78"], 2, "5/1.04 + 5/1.04² + 105/1.04³ = 4.81 + 4.62 + 93.34 = 102.78. A coupon above the discount rate gives a premium."],
 ["A five-year zero-coupon bond with a par value of 100 has a yield of 5%, stated on a semi-annual basis. Its price is closest to:", ["78.12", "78.35", "95.24"], 0, "100 / 1.025^10 = 78.12. Using annual compounding gives 78.35."],
 ["A bond pays an annual coupon of 6% on a par value of 100 and uses a 30/360 day count. If 90 days have passed since the last coupon, the accrued interest is:", ["0.75", "1.50", "6.00"], 1, "6 × 90/360 = 1.50."],
 ["A bond has a flat price of 99.20 and accrued interest of 1.50. Its full price is:", ["97.70", "99.20", "100.70"], 2, "Full price = flat price + accrued interest = 100.70."],
 ["Holding other features constant, which bond's price is most sensitive to a change in its yield?", ["A 2-year bond with an 8% coupon", "A 10-year bond with an 8% coupon", "A 10-year bond with a 2% coupon"], 2, "Longer maturity and lower coupon both increase price sensitivity."],
 ["For an option-free bond, compared with the price change from a 50 bp increase in yield, the price change from a 50 bp decrease is:", ["smaller.", "larger.", "the same."], 1, "Convexity makes price gains from falling yields larger than losses from equal rises."],
 ["A premium bond's yield stays unchanged until maturity. Its price will:", ["rise above its current price.", "fall toward par.", "stay constant."], 1, "As maturity approaches, the price converges on par, so a premium price declines."],
 ["An analyst estimates the price of a corporate bond that has not traded for several weeks using yields on bonds with similar ratings and maturities. This method is:", ["matrix pricing.", "bootstrapping.", "duration matching."], 0, "Matrix pricing infers a yield for an illiquid bond from comparable bonds."],
]))

R.append(dict(id="yf", n="Yield and Yield Spread Measures for Fixed-Rate Bonds", k="YIELDS", w=2, c="#c2417a",
terms=[
 ["Periodicity", "Faiz ödeme sıklığı", "The number of periods per year assumed in stating an annual rate.", "Yıllık bir oranı ifade ederken varsayılan yıllık dönem sayısı."],
 ["Effective annual yield", "Efektif yıllık getiri", "A yield restated with annual compounding, allowing comparison across periodicities.", "Yıllık bileşik faize çevrilmiş getiri; farklı sıklıklar arasında karşılaştırmaya olanak verir."],
 ["Current yield", "Cari getiri", "The annual coupon divided by the flat price.", "Yıllık kuponun temiz fiyata bölümü."],
 ["Yield to call", "Erken itfaya kadar getiri", "The yield assuming the bond is called at a specified call date and price.", "Tahvilin belirli bir tarihte ve fiyattan erken itfa edildiği varsayımıyla getiri."],
 ["Yield to worst", "En kötü getiri", "The lowest of the yield to maturity and the yields to each call date.", "Vadeye kadar getiri ile her erken itfa tarihine kadar getirilerin en düşüğü."],
 ["G-spread", "Devlet tahviline göre fark", "The yield spread over an interpolated government bond yield of the same maturity.", "Aynı vadeli devlet tahvili getirisine göre getiri farkı."],
 ["I-spread", "Swap oranına göre fark", "The yield spread over the swap rate of the same maturity.", "Aynı vadeli swap oranına göre getiri farkı."],
 ["Z-spread", "Sıfır oynaklık farkı (Z-spread)", "The constant spread added to each spot rate that makes the present value of cash flows equal to the price.", "Nakit akışlarının bugünkü değerini fiyata eşitlemek için her spot orana eklenen sabit fark."],
 ["Option-adjusted spread (OAS)", "Opsiyondan arındırılmış fark", "The spread after removing the value of any embedded option.", "Gömülü opsiyonun değeri çıkarıldıktan sonra kalan fark."],
],
notes="""<h3>Comparing yields</h3>
<ul>
<li>Yields with different compounding frequencies are not directly comparable. Convert them to the same periodicity.</li>
</ul>
<p class="f">(1 + APR<sub>m</sub>/m)<sup>m</sup> = (1 + APR<sub>n</sub>/n)<sup>n</sup></p>
<p class="f">effective annual yield = (1 + APR/m)<sup>m</sup> − 1</p>
<ul>
<li>A semi-annual yield of 6% equals an effective annual 6.09% and a quarterly-compounded 5.96%. More frequent compounding means a lower stated rate for the same effective return.</li>
<li><b>Street convention</b> assumes payments on the scheduled dates, ignoring weekends and holidays; the <b>true yield</b> uses actual payment dates and is slightly lower.</li>
</ul>
<h3>Other yield measures</h3>
<ul>
<li><b>Current yield</b> = annual coupon / flat price. Ignores gains or losses to maturity and reinvestment.</li>
<li><b>Simple yield</b> adds straight-line amortization of the discount or premium to the coupon.</li>
<li><b>Yield to call</b> uses the call date and call price. <b>Yield to worst</b> is the lowest of YTM and all yields to call.</li>
<li><b>Option-adjusted yield</b> removes the value of the call option.</li>
</ul>
<h3>Spreads</h3>
<div class="tbl"><table>
<tr><th>Spread</th><th>Over what</th></tr>
<tr><td>Benchmark spread</td><td>Yield of the on-the-run government bond of similar maturity</td></tr>
<tr><td>G-spread</td><td>Government yield interpolated to the bond's exact maturity</td></tr>
<tr><td>I-spread</td><td>Swap rate of the same maturity</td></tr>
<tr><td>Z-spread</td><td>Each point of the government spot curve</td></tr>
<tr><td>OAS</td><td>Z-spread minus the option's value in spread terms</td></tr>
</table></div>
<ul>
<li>The spread compensates for credit risk, liquidity risk and tax differences. The benchmark yield reflects macro factors such as expected inflation and real rates.</li>
<li>For a <b>callable</b> bond, OAS &lt; Z-spread, because part of the spread pays for the call option the investor has sold. For a putable bond, OAS &gt; Z-spread.</li>
</ul>
<div class="trap"><b>Exam trap</b>Yield to worst is the lowest yield, not the highest; it is the conservative estimate for a callable bond trading at a premium.</div>""",
qs=[
 ["A bond's yield to maturity is 6% stated on a semi-annual basis. Its effective annual yield is closest to:", ["6.00%", "6.09%", "6.18%"], 1, "(1 + 0.06/2)² − 1 = 6.09%."],
 ["A yield of 6% stated on a semi-annual basis, restated on a quarterly basis, is closest to:", ["5.96%", "6.00%", "6.09%"], 0, "Quarterly rate = 4 × [(1.03)^(1/2) − 1] = 5.96%. More frequent compounding means a lower stated rate."],
 ["A bond pays an annual coupon of 5 on a par value of 100 and has a flat price of 95. Its current yield is closest to:", ["4.75%", "5.00%", "5.26%"], 2, "Current yield = 5 / 95 = 5.26%."],
 ["The yield to worst on a callable bond is the:", ["highest of its yield to maturity and its yields to call.", "lowest of its yield to maturity and its yields to call.", "average of its yield to maturity and its yields to call."], 1, "Yield to worst gives the most conservative yield across all possible redemption dates."],
 ["A corporate bond's yield spread over the swap rate of the same maturity is its:", ["G-spread.", "I-spread.", "Z-spread."], 1, "The I-spread uses the swap curve as the benchmark; the G-spread uses government yields."],
 ["The constant spread that, added to each government spot rate, makes the present value of a bond's cash flows equal to its price is the:", ["Z-spread.", "G-spread.", "benchmark spread."], 0, "The Z-spread applies one spread across the whole spot curve, not a single yield."],
 ["For a callable bond, the option-adjusted spread is:", ["greater than the Z-spread.", "less than the Z-spread.", "equal to the Z-spread."], 1, "Part of the Z-spread compensates for the call option sold to the issuer; removing it leaves a smaller OAS."],
 ["Compared with a yield calculated under the street convention, the true yield that uses actual payment dates is:", ["slightly higher.", "slightly lower.", "identical."], 1, "Payments delayed by weekends and holidays arrive later, which slightly reduces the true yield."],
]))

R.append(dict(id="yr", n="Yield and Yield Spread Measures for Floating-Rate Instruments", k="FLOATERS", w=1, c="#1f7a8c",
terms=[
 ["Reference rate", "Referans faiz", "The market rate to which a floating coupon is linked, such as an overnight or term benchmark rate.", "Değişken kuponun bağlı olduğu piyasa faizi; örneğin gecelik veya vadeli gösterge faiz."],
 ["Quoted margin", "Kote edilen marj", "The fixed spread over the reference rate that the issuer pays.", "İhraççının referans faizin üzerine ödediği sabit fark."],
 ["Required margin", "Gerekli marj", "The spread over the reference rate that investors currently require; also called discount margin.", "Yatırımcıların şu anda referans faizin üzerine istediği fark; iskonto marjı da denir."],
 ["Discount rate basis", "İskonto esası", "A money market quotation that expresses the discount from face value as an annual rate on face value.", "Nominal değerden iskontoyu, nominal değer üzerinden yıllık oran olarak ifade eden para piyasası kotasyonu."],
 ["Add-on rate basis", "Basit faiz esası", "A money market quotation in which interest is added to the amount invested.", "Faizin yatırılan tutara eklendiği para piyasası kotasyonu."],
 ["Bond equivalent yield", "Tahvil eşdeğer getiri", "A money market rate stated on an add-on basis with a 365-day year.", "365 günlük yıl esasıyla basit faiz şeklinde ifade edilen para piyasası getirisi."],
 ["Money market instrument", "Para piyasası aracı", "A debt instrument with a maturity of one year or less.", "Vadesi bir yıl veya daha kısa olan borçlanma aracı."],
],
notes="""<h3>Floating-rate notes</h3>
<ul>
<li>Coupon = reference rate + <b>quoted margin</b>, reset each period. Because the coupon follows market rates, the price stays close to par at reset dates.</li>
<li>If the <b>required margin</b> rises above the quoted margin (for example after a downgrade), the note trades <b>below par</b>. If it falls below the quoted margin, the note trades <b>above par</b>.</li>
<li>Pricing: discount each projected coupon (reference rate + quoted margin) at the reference rate + required margin.</li>
</ul>
<h3>Money market quotations</h3>
<div class="tbl"><table>
<tr><th>Basis</th><th>Price formula</th><th>Used for</th></tr>
<tr><td>Discount rate</td><td>PV = FV × (1 − Days/Year × DR)</td><td>Treasury bills, commercial paper</td></tr>
<tr><td>Add-on rate</td><td>PV = FV / (1 + Days/Year × AOR)</td><td>Bank deposits, repos, certificates of deposit</td></tr>
</table></div>
<p class="f">AOR = (Year / Days) × (FV − PV) / PV</p>
<ul>
<li>A discount rate understates the investor's return: it divides the interest by face value, not by the amount invested, and usually uses a 360-day year.</li>
<li>To compare, convert all rates to the same basis: the <b>bond equivalent yield</b> is an add-on rate with a 365-day year.</li>
<li>Periodicity of money market rates = 365 / days to maturity; convert to a common periodicity before comparing with bond yields.</li>
</ul>
<div class="trap"><b>Exam trap</b>On the same instrument, the add-on rate is always higher than the discount rate.</div>""",
qs=[
 ["A floating-rate note has a quoted margin of 50 bp. Investors now require a margin of 70 bp. On a reset date the note will most likely trade:", ["below par.", "at par.", "above par."], 0, "The note pays less over the reference rate than investors require, so its price falls below par."],
 ["On a reset date, a floating-rate note trades at par when its:", ["quoted margin is zero.", "quoted margin equals the required margin.", "reference rate equals its coupon rate."], 1, "When the coupon spread matches the required spread, the note is priced at par."],
 ["A 90-day Treasury bill with a face value of 100 is quoted at a discount rate of 4% on a 360-day basis. Its price is:", ["96.00", "99.00", "99.01"], 1, "100 × (1 − 0.04 × 90/360) = 99.00."],
 ["A 90-day money market instrument has a face value of 100 and a price of 99. Its add-on rate on a 365-day basis is closest to:", ["4.00%", "4.06%", "4.10%"], 2, "AOR = (365/90) × (1/99) = 4.10%. Dividing by face value instead of price gives 4.06%."],
 ["Compared with the add-on rate for the same instrument, a discount rate is:", ["lower.", "higher.", "the same."], 0, "The discount rate uses face value as the base and so understates the return on the amount invested."],
 ["The bond equivalent yield of a money market instrument is an:", ["add-on rate on a 360-day year.", "add-on rate on a 365-day year.", "discount rate on a 365-day year."], 1, "It restates the return as an add-on rate with a 365-day year, comparable to bond yields."],
 ["The issuer of a floating-rate note is downgraded. The note's price will most likely:", ["rise above par.", "fall below par.", "remain at par because the coupon resets."], 1, "The coupon resets with the reference rate, not with credit risk. A higher required margin lowers the price."],
 ["Floating-rate notes have less interest rate risk than fixed-rate bonds because:", ["they have no credit risk.", "their coupons adjust to market rates.", "they always trade at par."], 1, "Coupon resets keep the note's yield close to market rates; credit risk remains."],
]))

R.append(dict(id="ts", n="The Term Structure of Interest Rates: Spot, Par, and Forward Curves", k="CURVES", w=2, c="#3b7dd8",
terms=[
 ["Spot rate", "Spot faiz", "The yield on a zero-coupon bond for a given maturity.", "Belirli bir vadedeki kuponsuz tahvilin getirisi."],
 ["Spot curve", "Spot getiri eğrisi", "The set of spot rates for different maturities; also called the zero curve.", "Farklı vadeler için spot faizlerin oluşturduğu eğri; sıfır eğrisi de denir."],
 ["Par curve", "Nominal (par) eğrisi", "The coupon rates at which bonds of each maturity would be priced at par.", "Her vadedeki tahvilin nominalden fiyatlanmasını sağlayacak kupon oranları."],
 ["Forward rate", "Vadeli faiz", "An interest rate for a loan starting at a future date, implied by today's spot rates.", "Bugünkü spot faizlerin ima ettiği, gelecekteki bir tarihte başlayacak borçlanma faizi."],
 ["Bootstrapping", "Ardışık türetme (bootstrapping)", "Deriving spot rates one maturity at a time from the prices or par rates of coupon bonds.", "Kuponlu tahvillerin fiyatlarından veya par oranlarından spot faizleri vade vade türetme."],
 ["Upward-sloping yield curve", "Pozitif eğimli getiri eğrisi", "A curve in which longer maturities have higher yields.", "Uzun vadelerin daha yüksek getirili olduğu eğri."],
 ["Inverted yield curve", "Ters getiri eğrisi", "A curve in which short maturities have higher yields than long ones.", "Kısa vadelerin uzun vadelerden daha yüksek getirili olduğu eğri."],
 ["Riding the yield curve", "Getiri eğrisinde ilerleme stratejisi", "Buying bonds longer than the horizon and selling before maturity to benefit from a stable upward-sloping curve.", "Ufuktan uzun vadeli tahvil alıp vadeden önce satarak sabit ve pozitif eğimli eğriden yararlanma."],
],
notes="""<h3>Three curves</h3>
<ul>
<li><b>Spot curve:</b> zero-coupon yields. Pricing a bond with spot rates discounts each cash flow at its own rate, which is the no-arbitrage price.</li>
<li><b>Par curve:</b> coupon rates that price each maturity at par. Obtained from spot rates; spot rates can be <b>bootstrapped</b> from par rates.</li>
<li><b>Forward curve:</b> rates for future periods implied by spot rates.</li>
</ul>
<p class="f">P = C/(1+z<sub>1</sub>) + C/(1+z<sub>2</sub>)<sup>2</sup> + … + (C + FV)/(1+z<sub>N</sub>)<sup>N</sup></p>
<h3>Forward rates</h3>
<p class="f">(1 + z<sub>A+B</sub>)<sup>A+B</sup> = (1 + z<sub>A</sub>)<sup>A</sup> × (1 + f<sub>A,B</sub>)<sup>B</sup></p>
<ul>
<li>A forward rate is a <b>break-even</b> rate: an investor is indifferent between a long bond and a short bond rolled over at the forward rate.</li>
<li>If the spot curve is upward sloping, forward rates lie above spot rates; if it is inverted, they lie below.</li>
<li>If future spot rates turn out exactly as today's forwards imply, every bond, whatever its maturity, earns the current short-term spot rate over the next period.</li>
</ul>
<h3>Shapes</h3>
<div class="tbl"><table>
<tr><th>Shape</th><th>Typical reading</th></tr>
<tr><td>Upward sloping</td><td>Normal; compensation for duration risk, or expected rate rises</td></tr>
<tr><td>Flat</td><td>Transition; uncertain direction</td></tr>
<tr><td>Inverted</td><td>Expected rate cuts; often precedes recessions</td></tr>
</table></div>
<h3>Riding the yield curve</h3>
<ul>
<li>With an upward-sloping curve that stays unchanged, a bond bought with a maturity longer than the investment horizon will "roll down" to a lower yield as time passes, and can be sold at a gain. The return exceeds that of a bond matching the horizon.</li>
</ul>
<div class="trap"><b>Exam trap</b>The par rate for a maturity is a blend of the spot rates up to that maturity, so on an upward-sloping curve it lies slightly below the spot rate.</div>""",
qs=[
 ["The one-year spot rate is 2% and the two-year spot rate is 3%. The one-year rate one year forward is closest to:", ["2.50%", "3.00%", "4.01%"], 2, "1.03² / 1.02 − 1 = 4.01%."],
 ["The one-year spot rate is 2% and the two-year spot rate is 3%. The price of a two-year bond with a par value of 100 and a 5% annual coupon is closest to:", ["100.00", "103.83", "103.88"], 2, "5/1.02 + 105/1.03² = 4.90 + 98.97 = 103.88."],
 ["The one-year spot rate is 2% and the two-year spot rate is 3%. The two-year par rate is closest to:", ["2.50%", "2.99%", "3.00%"], 1, "Solve c/1.02 + (1 + c)/1.0609 = 1, giving c ≈ 2.99%, just below the two-year spot rate."],
 ["When the spot curve is upward sloping, forward rates are most likely:", ["below spot rates.", "above spot rates.", "equal to spot rates."], 1, "Longer spot rates are averages of shorter rates and forward rates, so forwards must be higher."],
 ["Deriving spot rates step by step from the prices of coupon-paying bonds is called:", ["bootstrapping.", "matrix pricing.", "riding the yield curve."], 0, "Bootstrapping solves for each spot rate in turn using the rates already found."],
 ["If future spot rates turn out to be equal to today's forward rates, an investor who buys a three-year bond and sells it after one year earns:", ["the one-year spot rate.", "the three-year spot rate.", "the one-year rate two years forward."], 0, "Under that assumption, all bonds earn the same one-period return: the current short-term spot rate."],
 ["An investor with a two-year horizon buys a five-year bond, expecting a stable upward-sloping yield curve, and plans to sell it after two years. This strategy is:", ["bootstrapping.", "duration matching.", "riding the yield curve."], 2, "The bond rolls down the curve to a lower yield and higher price, adding to return."],
 ["A yield curve on which short-term yields are higher than long-term yields is:", ["flat.", "inverted.", "upward sloping."], 1, "An inverted curve often reflects expectations that interest rates will fall."],
]))

R.append(dict(id="rr", n="Interest Rate Risk and Return", k="RISK & RETURN", w=2, c="#2e9e8f",
terms=[
 ["Reinvestment risk", "Yeniden yatırım riski", "The risk that coupons and principal must be reinvested at lower rates.", "Kupon ve anaparanın daha düşük oranlardan yeniden yatırılması gerekmesi riski."],
 ["Market price risk", "Piyasa fiyatı riski", "The risk that rising rates lower the price at which a bond can be sold before maturity.", "Faizlerin yükselmesinin, vadeden önce satılacak tahvilin fiyatını düşürmesi riski."],
 ["Investment horizon", "Yatırım ufku", "The time until the investor needs the money.", "Yatırımcının paraya ihtiyaç duyacağı zamana kadar geçen süre."],
 ["Horizon yield", "Ufuk getirisi", "The annualized return realized over the investment horizon.", "Yatırım ufku boyunca gerçekleşen yıllıklandırılmış getiri."],
 ["Macaulay duration", "Macaulay süresi", "The weighted average time to receive a bond's cash flows, weighted by their present values.", "Tahvilin nakit akışlarının, bugünkü değerleriyle ağırlıklandırılmış ortalama alınma süresi."],
 ["Duration gap", "Süre açığı", "Macaulay duration minus the investment horizon.", "Macaulay süresinden yatırım ufkunun çıkarılmasıyla bulunan fark."],
 ["Capital gain or loss", "Sermaye kazancı veya kaybı", "The difference between the sale price and the carrying value at amortized cost.", "Satış fiyatı ile itfa edilmiş maliyetten defter değeri arasındaki fark."],
],
notes="""<h3>Three sources of return</h3>
<ul>
<li>Coupon and principal payments, <b>reinvestment income</b> on the coupons, and a <b>capital gain or loss</b> if sold before maturity.</li>
<li>An investor earns exactly the YTM only if the bond is held to maturity, all payments are made in full and on time, and coupons are reinvested at the YTM.</li>
</ul>
<h3>Two offsetting risks</h3>
<div class="tbl"><table>
<tr><th>If rates rise after purchase</th><th>Effect</th></tr>
<tr><td>Reinvestment income</td><td>Higher</td></tr>
<tr><td>Sale price before maturity</td><td>Lower</td></tr>
</table></div>
<ul>
<li>A <b>long-horizon</b> investor (holding to maturity) is exposed mainly to <b>reinvestment risk</b> and gains from rising rates.</li>
<li>A <b>short-horizon</b> investor is exposed mainly to <b>market price risk</b> and loses from rising rates.</li>
</ul>
<h3>Macaulay duration as the balance point</h3>
<ul>
<li>When the investment horizon equals the bond's <b>Macaulay duration</b>, the two effects approximately offset for a one-time parallel shift, and the realized return is close to the original YTM.</li>
</ul>
<p class="f">duration gap = Macaulay duration − investment horizon</p>
<ul>
<li><b>Positive gap</b> (duration longer than the horizon): price risk dominates; the investor is hurt by <b>rising</b> rates.</li>
<li><b>Negative gap</b>: reinvestment risk dominates; the investor is hurt by <b>falling</b> rates.</li>
<li>A zero-coupon bond held to maturity has no reinvestment risk and no price risk: its Macaulay duration equals its maturity.</li>
</ul>
<h3>Computing a horizon return</h3>
<p class="f">horizon yield = (total value at horizon / purchase price)<sup>1 / years</sup> − 1</p>
<ul>
<li>Total value at horizon = coupons compounded at the reinvestment rate + sale price (or principal at maturity).</li>
</ul>
<div class="trap"><b>Exam trap</b>A rise in rates is good news for an investor who holds to maturity: the higher reinvestment income outweighs the temporary fall in price.</div>""",
qs=[
 ["An investor buys a three-year 5% annual-coupon bond at par. Rates immediately rise to 6% and stay there. If she holds the bond to maturity and reinvests coupons at 6%, her annualized return is closest to:", ["5.00%", "5.05%", "6.00%"], 1, "Coupons grow to 5 × 1.06² + 5 × 1.06 + 5 = 15.92. Total 115.92; (1.1592)^(1/3) − 1 = 5.05%."],
 ["An investor who intends to sell a bond shortly after buying it is exposed mainly to:", ["credit risk.", "reinvestment risk.", "market price risk."], 2, "With little time to reinvest coupons, the sale price, which falls when rates rise, dominates."],
 ["An investor's horizon equals the Macaulay duration of her bond. After a one-time parallel shift in rates, her realized return will be:", ["close to the original yield to maturity.", "much higher than the original yield.", "much lower than the original yield."], 0, "At the Macaulay duration, reinvestment and price effects roughly offset."],
 ["A bond has a Macaulay duration of 6 years and the investor's horizon is 4 years. The investor is most exposed to:", ["falling rates.", "rising rates.", "no change in rates."], 1, "The duration gap is +2. Price risk dominates, so a rise in rates lowers the horizon return."],
 ["For an investor who holds a coupon bond to maturity, an increase in interest rates after purchase will most likely:", ["increase the realized return.", "decrease the realized return.", "leave the realized return unchanged."], 0, "There is no sale, so only reinvestment matters, and coupons are reinvested at higher rates."],
 ["A zero-coupon bond held to maturity has:", ["only reinvestment risk.", "only market price risk.", "neither reinvestment risk nor market price risk."], 2, "There are no coupons to reinvest and no sale before maturity, so the return is locked in at purchase."],
 ["The three sources of return on a fixed-rate bond are coupons, reinvestment income and:", ["the credit rating.", "the duration gap.", "any capital gain or loss on sale."], 2, "A sale before maturity adds a gain or loss relative to the bond's amortized value."],
 ["A negative duration gap means the investor is exposed mainly to:", ["credit risk.", "reinvestment risk.", "market price risk."], 1, "When the horizon exceeds the duration, the investor is hurt by falling rates through lower reinvestment income."],
]))
