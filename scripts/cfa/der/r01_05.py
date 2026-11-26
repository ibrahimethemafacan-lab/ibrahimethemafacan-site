# CFA Level I · Derivatives · readings 1–5. Original study notes and questions.
R = []

R.append(dict(id="df", n="Derivative Instrument and Derivative Market Features", k="MARKETS", w=2, c="#3b7dd8",
terms=[
 ["Derivative", "Türev araç", "A contract whose value depends on the value of an underlying asset, rate or index.", "Değeri dayanak bir varlığın, oranın veya endeksin değerine bağlı olan sözleşme."],
 ["Underlying", "Dayanak varlık", "The asset, rate or index on which a derivative's value is based.", "Türev aracın değerinin dayandığı varlık, oran veya endeks."],
 ["Forward commitment", "Vadeli yükümlülük", "A contract obliging both parties to transact at a future date on agreed terms.", "Her iki tarafı gelecekteki bir tarihte kararlaştırılan koşullarla işlem yapmakla yükümlü kılan sözleşme."],
 ["Contingent claim", "Koşullu hak", "A derivative whose payoff depends on a future event, such as an option.", "Getirisi opsiyon gibi gelecekteki bir olaya bağlı olan türev araç."],
 ["Exchange-traded derivative", "Borsada işlem gören türev", "A standardized derivative traded on an exchange and cleared through a clearing house.", "Borsada işlem gören ve takas kurumu aracılığıyla takas edilen standart türev araç."],
 ["Over-the-counter (OTC) derivative", "Tezgâhüstü türev", "A customized derivative negotiated directly between two parties.", "İki taraf arasında doğrudan pazarlıkla oluşturulan özelleştirilmiş türev araç."],
 ["Central counterparty (CCP)", "Merkezi karşı taraf", "An entity that becomes the buyer to every seller and the seller to every buyer, guaranteeing performance.", "Her satıcıya alıcı, her alıcıya satıcı olarak işlemlerin yerine getirilmesini garanti eden kuruluş."],
 ["Counterparty credit risk", "Karşı taraf kredi riski", "The risk that the other side of a contract fails to pay what it owes.", "Sözleşmenin karşı tarafının borcunu ödememesi riski."],
 ["Notional amount", "Nominal (hayali) tutar", "The amount used to calculate a derivative's payments; often not exchanged.", "Türev aracın ödemelerini hesaplamakta kullanılan, çoğu zaman el değiştirmeyen tutar."],
 ["Margin", "Teminat", "Collateral posted to cover potential losses on a derivative position.", "Türev pozisyondaki olası kayıpları karşılamak için yatırılan teminat."],
],
notes="""<h3>What a derivative is</h3>
<ul>
<li>A contract between two parties whose value comes from an <b>underlying</b>: equities, bonds and interest rates, currencies, commodities, credit, or other variables such as weather or volatility indexes.</li>
<li>Derivatives let investors take on or shed exposure with little capital, so they are leveraged.</li>
</ul>
<h3>Two families</h3>
<div class="tbl"><table>
<tr><th>Forward commitments</th><th>Contingent claims</th></tr>
<tr><td>Both parties must perform</td><td>One party has a right, the other an obligation</td></tr>
<tr><td>Forwards, futures, swaps</td><td>Options, credit default swaps</td></tr>
<tr><td>Payoff is linear in the underlying</td><td>Payoff is non-linear; the buyer pays a premium</td></tr>
</table></div>
<h3>Where derivatives trade</h3>
<div class="tbl"><table>
<tr><th></th><th>Exchange-traded</th><th>Over the counter</th></tr>
<tr><td>Terms</td><td>Standardized</td><td>Customized</td></tr>
<tr><td>Counterparty</td><td>Clearing house</td><td>The dealer or other party</td></tr>
<tr><td>Credit risk</td><td>Very low: margin and daily settlement</td><td>Higher, though reduced by collateral and central clearing</td></tr>
<tr><td>Transparency and liquidity</td><td>High</td><td>Lower</td></tr>
<tr><td>Flexibility</td><td>Low</td><td>High</td></tr>
</table></div>
<ul>
<li>OTC trades are typically documented under a master agreement that sets standard terms, netting and collateral rules.</li>
<li>After the 2008 crisis, regulators required many standardized OTC swaps to be <b>centrally cleared</b> through a CCP and reported to trade repositories.</li>
<li>A CCP takes on counterparty risk and protects itself with <b>initial margin</b>, daily <b>variation margin</b> and a default fund.</li>
</ul>
<div class="trap"><b>Exam trap</b>A credit default swap is a contingent claim, not a forward commitment: the protection seller pays only if a credit event occurs.</div>""",
qs=[
 ["Compared with over-the-counter derivatives, exchange-traded derivatives are:", ["more customized.", "more standardized.", "subject to more counterparty risk."], 1, "Exchange-traded contracts have standard terms and are cleared through a clearing house."],
 ["The main benefit of central clearing of derivatives is a reduction in:", ["market risk.", "counterparty credit risk.", "the notional amount."], 1, "The central counterparty guarantees performance and collects margin, reducing the risk that one side defaults."],
 ["Which of the following is a contingent claim?", ["A swap", "A forward contract", "A call option"], 2, "An option gives a right without an obligation, so its payoff depends on whether it is exercised."],
 ["Which of the following is a forward commitment?", ["An interest rate swap", "A put option", "A credit default swap"], 0, "Both parties to a swap are obliged to make payments. Options and CDS are contingent claims."],
 ["The amount used to calculate the payments on an interest rate swap, which is usually not exchanged, is the:", ["premium.", "margin.", "notional amount."], 2, "The notional amount scales the interest payments but is not itself paid in an interest rate swap."],
 ["Compared with exchange-traded derivatives, over-the-counter derivatives typically offer:", ["less flexibility.", "greater flexibility.", "greater transparency."], 1, "OTC contracts can be tailored to the user's exact needs, at the cost of less transparency and liquidity."],
 ["Which of the following can serve as the underlying of a derivative?", ["Only financial assets", "Only commodities", "A weather index"], 2, "Underlyings include equities, rates, currencies, commodities, credit and other variables such as weather."],
 ["Daily payments made to reflect gains and losses on a cleared derivative position are called:", ["initial margin.", "variation margin.", "the premium."], 1, "Variation margin settles the change in value each day; initial margin is posted at the start."],
]))

R.append(dict(id="fc", n="Forward Commitment and Contingent Claim Features and Instruments", k="INSTRUMENTS", w=2, c="#2e9e8f",
terms=[
 ["Forward contract", "Forward sözleşmesi", "An OTC agreement to buy or sell an asset at a set price on a future date.", "Bir varlığı gelecekteki bir tarihte belirli fiyattan alıp satmaya ilişkin tezgâhüstü anlaşma."],
 ["Futures contract", "Vadeli işlem (futures) sözleşmesi", "A standardized, exchange-traded forward with daily settlement of gains and losses.", "Kazanç ve kayıpları günlük olarak uzlaştırılan, borsada işlem gören standart forward."],
 ["Swap", "Swap", "An agreement to exchange a series of cash flows over a period.", "Belirli bir süre boyunca bir dizi nakit akışını değiş tokuş etme anlaşması."],
 ["Call option", "Alım opsiyonu", "The right to buy the underlying at the exercise price.", "Dayanak varlığı kullanım fiyatından satın alma hakkı."],
 ["Put option", "Satım opsiyonu", "The right to sell the underlying at the exercise price.", "Dayanak varlığı kullanım fiyatından satma hakkı."],
 ["Exercise price", "Kullanım fiyatı", "The price at which an option holder may buy or sell the underlying; also called strike price.", "Opsiyon sahibinin dayanak varlığı alabileceği veya satabileceği fiyat; strike fiyatı da denir."],
 ["Option premium", "Opsiyon primi", "The price the buyer pays the seller for an option.", "Alıcının opsiyon için satıcıya ödediği fiyat."],
 ["In the money", "Kârda (içinde) opsiyon", "An option that would have positive value if exercised now.", "Şimdi kullanılsaydı pozitif değeri olacak opsiyon."],
 ["Credit default swap (CDS)", "Kredi temerrüt swabı", "A contract in which the protection buyer pays periodic premiums and is compensated if a credit event occurs.", "Korunma alıcısının dönemsel prim ödediği ve kredi olayı gerçekleşirse tazmin edildiği sözleşme."],
 ["Breakeven price", "Başabaş fiyatı", "The underlying price at expiration at which an option position has zero profit.", "Vade sonunda opsiyon pozisyonunun kârının sıfır olduğu dayanak fiyatı."],
],
notes="""<h3>Forwards and futures</h3>
<p class="f">long forward payoff at expiration = S<sub>T</sub> − F<sub>0</sub> &nbsp;&nbsp;&nbsp; short = F<sub>0</sub> − S<sub>T</sub></p>
<ul>
<li>The long agrees to buy, the short to sell. No money changes hands at the start; the forward price is set so that the contract's value is zero.</li>
<li>Settlement can be by delivery or in cash.</li>
<li><b>Futures</b> are standardized, traded on exchanges and settled daily, so gains and losses are realized as they occur.</li>
<li><b>Swaps</b> are a series of forwards: for example, fixed interest payments exchanged for floating ones on a notional amount.</li>
</ul>
<h3>Options</h3>
<p class="f">call payoff = max(0, S<sub>T</sub> − X) &nbsp;&nbsp;&nbsp; put payoff = max(0, X − S<sub>T</sub>)</p>
<p class="f">profit = payoff − premium (buyer); premium − payoff (seller)</p>
<div class="tbl"><table>
<tr><th>Position</th><th>Maximum gain</th><th>Maximum loss</th><th>Breakeven</th></tr>
<tr><td>Long call</td><td>Unlimited</td><td>Premium</td><td>X + premium</td></tr>
<tr><td>Short call</td><td>Premium</td><td>Unlimited</td><td>X + premium</td></tr>
<tr><td>Long put</td><td>X − premium</td><td>Premium</td><td>X − premium</td></tr>
<tr><td>Short put</td><td>Premium</td><td>X − premium</td><td>X − premium</td></tr>
</table></div>
<ul>
<li><b>Moneyness:</b> a call is in the money when S &gt; X, a put when S &lt; X; at the money when S = X.</li>
<li><b>European</b> options can be exercised only at expiration; <b>American</b> options at any time up to expiration.</li>
</ul>
<h3>Credit default swaps</h3>
<ul>
<li>The protection buyer pays a periodic premium; the seller pays the loss if the reference entity has a credit event (bankruptcy, failure to pay, sometimes restructuring).</li>
<li>Used to hedge credit exposure or to take a view on credit without owning the bond.</li>
</ul>
<div class="trap"><b>Exam trap</b>Payoff ignores the premium; profit subtracts it. Read which one the question asks for.</div>""",
qs=[
 ["An investor enters a long forward contract at a forward price of $50. At expiration the underlying is $58. The payoff to the investor is:", ["−$8", "$0", "$8"], 2, "Long forward payoff = S(T) − F(0) = 58 − 50 = $8."],
 ["An investor buys a call with an exercise price of $40 for a premium of $3. At expiration the share is $45. Her profit is:", ["$2", "$3", "$5"], 0, "Payoff = 45 − 40 = 5; profit = 5 − 3 = $2."],
 ["An investor buys a put with an exercise price of $40 for a premium of $2. At expiration the share is $35. Her profit is:", ["$2", "$3", "$5"], 1, "Payoff = 40 − 35 = 5; profit = 5 − 2 = $3."],
 ["The breakeven price at expiration for the buyer of a call with an exercise price of $40 and a premium of $3 is:", ["$37", "$40", "$43"], 2, "The share must rise above the exercise price by the premium: 40 + 3 = $43."],
 ["The maximum loss for the buyer of a call option is:", ["the premium paid.", "the exercise price.", "unlimited."], 0, "The buyer can simply let the option expire, losing only the premium."],
 ["An investor writes a put with an exercise price of $40 for a premium of $2. Her maximum possible loss is:", ["$2", "$38", "$40"], 1, "If the share falls to zero she pays 40 and keeps the premium: 40 − 2 = $38."],
 ["The buyer of protection in a credit default swap:", ["receives periodic premiums.", "pays periodic premiums.", "must deliver the reference bond at the start."], 1, "The protection buyer pays premiums in exchange for compensation if a credit event occurs."],
 ["A put option is in the money when the price of the underlying is:", ["below the exercise price.", "equal to the exercise price.", "above the exercise price."], 0, "The right to sell at X is valuable when the market price is below X."],
]))

R.append(dict(id="du", n="Derivative Benefits, Risks, and Issuer and Investor Uses", k="USES", w=1, c="#c0563f",
terms=[
 ["Hedging", "Riskten korunma", "Using a position to reduce an existing exposure.", "Mevcut bir riski azaltmak için pozisyon kullanma."],
 ["Speculation", "Spekülasyon", "Taking on exposure in the hope of profiting from price changes.", "Fiyat değişimlerinden kâr umuduyla risk üstlenme."],
 ["Basis risk", "Baz riski", "The risk that the hedging instrument and the exposure being hedged do not move exactly together.", "Korunma aracı ile korunan risk kaleminin tam olarak birlikte hareket etmemesi riski."],
 ["Price discovery", "Fiyat keşfi", "The process by which markets reveal information about expected future prices.", "Piyasaların beklenen gelecek fiyatlar hakkındaki bilgiyi ortaya koyma süreci."],
 ["Fair value hedge", "Gerçeğe uygun değer riskinden korunma", "A hedge of changes in the value of an asset or liability.", "Bir varlığın veya yükümlülüğün değerindeki değişimlerden korunma."],
 ["Cash flow hedge", "Nakit akış riskinden korunma", "A hedge of the variability of future cash flows.", "Gelecekteki nakit akışlarının değişkenliğinden korunma."],
 ["Net investment hedge", "Net yatırım riskinden korunma", "A hedge of the currency exposure of an investment in a foreign subsidiary.", "Yurt dışı bağlı ortaklıktaki yatırımın kur riskinden korunma."],
 ["Systemic risk", "Sistemik risk", "The risk that failures at some institutions spread to the whole financial system.", "Bazı kurumlardaki başarısızlıkların tüm finansal sisteme yayılması riski."],
],
notes="""<h3>Benefits</h3>
<ul>
<li><b>Risk transfer:</b> those who want less risk pass it to those willing to bear it.</li>
<li><b>Price discovery:</b> futures and options prices reveal expectations of future prices and volatility.</li>
<li><b>Lower costs and greater efficiency:</b> derivatives let investors change exposure cheaply and quickly, often with high liquidity, and allow short exposure that is hard to get in cash markets.</li>
</ul>
<h3>Risks</h3>
<ul>
<li><b>Leverage:</b> small price moves can cause large losses relative to the capital committed.</li>
<li><b>Basis risk:</b> the hedge does not track the exposure exactly.</li>
<li><b>Liquidity risk:</b> margin calls require cash at short notice, even when the hedged position has not produced cash.</li>
<li><b>Counterparty credit risk</b>, especially in OTC contracts.</li>
<li><b>Systemic risk:</b> concentrated, interconnected exposures can spread losses across the system.</li>
<li>Complexity and model risk.</li>
</ul>
<h3>Issuers' uses and hedge accounting</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>What is hedged</th><th>Example</th></tr>
<tr><td>Fair value hedge</td><td>Value of an asset or liability</td><td>Fixed-rate debt swapped to floating</td></tr>
<tr><td>Cash flow hedge</td><td>Variable future cash flows</td><td>Floating-rate debt swapped to fixed; forward purchase of a commodity input</td></tr>
<tr><td>Net investment hedge</td><td>Currency value of a foreign subsidiary</td><td>Currency forward or foreign-currency debt</td></tr>
</table></div>
<ul>
<li>Hedge accounting lets the gains and losses on the derivative be matched with those on the hedged item, reducing earnings volatility.</li>
</ul>
<h3>Investors' uses</h3>
<ul>
<li>Change exposure quickly (for example, reduce equity risk with index futures), replicate a cash position cheaply, gain short exposure, express a view on volatility, or protect against falls with puts.</li>
</ul>
<div class="trap"><b>Exam trap</b>Swapping fixed-rate debt to floating hedges the debt's value: a fair value hedge. Swapping floating to fixed hedges cash flows.</div>""",
qs=[
 ["A company hedges jet fuel purchases with crude oil futures. The risk that the two prices do not move together is:", ["basis risk.", "systemic risk.", "counterparty risk."], 0, "The hedge instrument's underlying differs from the exposure, leaving basis risk."],
 ["A company with floating-rate debt enters a swap to pay fixed and receive floating. For accounting purposes this is most likely a:", ["fair value hedge.", "cash flow hedge.", "net investment hedge."], 1, "The swap removes variability in future interest payments."],
 ["A company with fixed-rate debt enters a swap to pay floating and receive fixed. For accounting purposes this is most likely a:", ["fair value hedge.", "cash flow hedge.", "net investment hedge."], 0, "The swap offsets changes in the fair value of the fixed-rate debt."],
 ["A company hedges the currency exposure of its investment in a foreign subsidiary. This is a:", ["fair value hedge.", "cash flow hedge.", "net investment hedge."], 2, "Net investment hedges protect the home-currency value of a foreign operation."],
 ["Which of the following is a benefit that derivatives provide to markets?", ["Price discovery", "Elimination of systemic risk", "Elimination of the need for collateral"], 0, "Derivatives prices reveal information about expected prices and volatility."],
 ["A hedger using futures may face a liquidity problem because:", ["futures cannot be sold before expiration.", "margin calls must be met in cash before the hedged item produces cash.", "futures have no counterparty."], 1, "Daily settlement can require cash even when the offsetting gain on the hedged item has not yet been realized."],
 ["An investor who wants to reduce the equity exposure of a portfolio quickly and cheaply, without selling shares, would most likely:", ["buy equity index futures.", "sell equity index futures.", "buy call options on the index."], 1, "A short futures position offsets part of the portfolio's market exposure."],
 ["The use of derivatives can increase systemic risk mainly through:", ["price discovery.", "lower transaction costs.", "concentrated and interconnected exposures."], 2, "If large exposures are concentrated in a few institutions, losses can spread across the system."],
]))

R.append(dict(id="ar", n="Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives", k="ARBITRAGE", w=2, c="#8a5cc2",
terms=[
 ["Arbitrage", "Arbitraj", "A riskless profit made with no net investment by exploiting a price difference.", "Bir fiyat farkından yararlanarak net yatırım yapmadan elde edilen risksiz kâr."],
 ["Law of one price", "Tek fiyat kanunu", "Assets or portfolios with identical cash flows must have the same price.", "Aynı nakit akışlarına sahip varlık veya portföylerin aynı fiyatta olması gerektiği ilkesi."],
 ["Replication", "Kopyalama (replikasyon)", "Creating a position with the same payoffs as a derivative using other instruments.", "Başka araçlarla bir türev aracın getirisiyle aynı getiriye sahip pozisyon oluşturma."],
 ["Risk-neutral pricing", "Risk nötr fiyatlama", "Pricing derivatives by discounting expected payoffs at the risk-free rate, using probabilities consistent with no arbitrage.", "Türevlerin, arbitrajsızlıkla tutarlı olasılıklarla beklenen getirileri risksiz faizle iskontolayarak fiyatlanması."],
 ["Cost of carry", "Taşıma maliyeti", "The net cost of holding the underlying: financing and storage costs minus any income or benefits.", "Dayanak varlığı elde tutmanın net maliyeti: finansman ve depolama maliyetleri eksi gelir veya faydalar."],
 ["Convenience yield", "Elde tutma getirisi", "The non-monetary benefit of physically holding a commodity.", "Bir emtiayı fiziksel olarak elde tutmanın parasal olmayan faydası."],
 ["Cash-and-carry arbitrage", "Nakit ve taşıma arbitrajı", "Buying the underlying with borrowed money and selling it forward when the forward price is too high.", "Vadeli fiyat çok yüksek olduğunda dayanağı borçla alıp ileriye satma."],
 ["Reverse cash-and-carry", "Ters nakit ve taşıma arbitrajı", "Shorting the underlying, investing the proceeds and buying forward when the forward price is too low.", "Vadeli fiyat çok düşük olduğunda dayanağı açığa satıp geliri yatırma ve ileriye alma."],
],
notes="""<h3>Arbitrage and replication</h3>
<ul>
<li>If two positions produce the same future cash flows, they must cost the same today. Otherwise, buy the cheap one, sell the dear one, and lock in a riskless profit.</li>
<li>A long asset plus a short forward on it produces a certain amount at expiration: it replicates a risk-free bond. That is why the forward price depends on the risk-free rate.</li>
<li>Because a derivative can be replicated with the underlying and borrowing or lending, its price does not depend on investors' risk preferences: this is <b>risk-neutral pricing</b>.</li>
</ul>
<h3>Cost of carry model</h3>
<p class="f">F<sub>0</sub> = S<sub>0</sub> × (1 + r)<sup>T</sup> + FV(costs) − FV(benefits)</p>
<p class="f">continuous form: F<sub>0</sub> = S<sub>0</sub> × e<sup>(r + c − i)T</sup></p>
<ul>
<li><b>Costs</b> of carrying the asset (financing, storage, insurance) raise the forward price.</li>
<li><b>Benefits</b> (dividends, coupons, foreign interest, convenience yield) lower it.</li>
</ul>
<h3>When the price is wrong</h3>
<div class="tbl"><table>
<tr><th>Forward price is</th><th>Arbitrage</th></tr>
<tr><td>Too high</td><td>Cash-and-carry: borrow, buy the asset, sell forward</td></tr>
<tr><td>Too low</td><td>Reverse: short the asset, invest the proceeds, buy forward</td></tr>
</table></div>
<ul>
<li>Arbitrage is limited in practice by transaction costs, restrictions on short selling, and the difficulty of storing or borrowing some assets.</li>
</ul>
<div class="trap"><b>Exam trap</b>Income from the underlying, such as a dividend, lowers the forward price. Students often add it instead of subtracting it.</div>""",
qs=[
 ["An asset with no costs or benefits of holding trades at $100. The risk-free rate is 5%. The no-arbitrage one-year forward price is:", ["$95", "$100", "$105"], 2, "F0 = 100 × 1.05 = $105."],
 ["An asset trades at $100, the risk-free rate is 5%, and storage costs with a future value of $2 must be paid. The one-year forward price is:", ["$103", "$105", "$107"], 2, "F0 = 100 × 1.05 + 2 = $107. Costs raise the forward price."],
 ["A share trades at $100, the risk-free rate is 5%, and it will pay a dividend with a future value of $3 within the year. The one-year forward price is:", ["$102", "$105", "$108"], 0, "F0 = 100 × 1.05 − 3 = $102. Income lowers the forward price."],
 ["The no-arbitrage one-year forward price is $105, but a dealer quotes $110. An arbitrageur should:", ["buy the forward and sell the asset short.", "borrow, buy the asset and sell the forward.", "do nothing because forwards are not traded on exchanges."], 1, "The forward is too expensive. A cash-and-carry trade locks in $5 of riskless profit."],
 ["A high convenience yield on a commodity will most likely:", ["raise its forward price.", "lower its forward price.", "have no effect on its forward price."], 1, "The benefit of holding the physical commodity reduces the net cost of carry."],
 ["Holding an asset and selling it forward at the no-arbitrage price produces a position equivalent to:", ["a call option.", "a risk-free bond.", "a leveraged long position."], 1, "The future selling price is fixed, so the position earns the risk-free rate."],
 ["Under risk-neutral pricing, derivatives are valued by discounting expected payoffs at the:", ["risk-free rate.", "investor's required return.", "expected return on the underlying."], 0, "Because the derivative can be replicated, risk preferences do not enter its price."],
 ["An arbitrage opportunity requires:", ["a risky profit with a large investment.", "a riskless profit with no net investment.", "a forward price equal to the spot price."], 1, "Arbitrage locks in a gain with no risk and no capital, by trading positions with identical payoffs at different prices."],
]))

R.append(dict(id="fw", n="Pricing and Valuation of Forward Contracts", k="FORWARDS", w=1, c="#b8860b",
terms=[
 ["Forward price", "Vadeli fiyat", "The price agreed at the start for exchange at expiration; set so the contract has zero value initially.", "Vade sonunda değişim için başta kararlaştırılan fiyat; sözleşmenin başlangıç değeri sıfır olacak şekilde belirlenir."],
 ["Forward value", "Forward değeri", "The current worth of an existing forward contract to one of the parties.", "Mevcut bir forward sözleşmesinin taraflardan biri için şimdiki değeri."],
 ["Forward rate agreement (FRA)", "Vadeli faiz anlaşması", "A forward contract on an interest rate for a future period.", "Gelecekteki bir dönem için faiz oranı üzerine yapılan forward sözleşmesi."],
 ["Implied forward rate", "Zımni vadeli faiz", "The interest rate for a future period implied by today's spot rates.", "Bugünkü spot faizlerin ima ettiği gelecek dönem faiz oranı."],
 ["Mark to market", "Piyasa değerine göre değerleme", "Valuing a position at current market prices.", "Bir pozisyonu güncel piyasa fiyatlarıyla değerleme."],
 ["Covered interest rate parity", "Güvenceli faiz paritesi", "The no-arbitrage link between spot and forward exchange rates and the two currencies' interest rates.", "Spot ve vadeli kurlar ile iki paranın faiz oranları arasındaki arbitrajsızlık ilişkisi."],
],
notes="""<h3>Price and value</h3>
<ul>
<li>The <b>forward price</b> is fixed at initiation. The <b>value</b> of the contract starts at zero and changes as the underlying moves.</li>
</ul>
<p class="f">value of long forward at time t = S<sub>t</sub> − PV(costs) + PV(benefits) − F<sub>0</sub> / (1 + r)<sup>T−t</sup></p>
<ul>
<li>For an asset with no costs or benefits: V<sub>t</sub> = S<sub>t</sub> − F<sub>0</sub>/(1 + r)<sup>T−t</sup>. At expiration, V<sub>T</sub> = S<sub>T</sub> − F<sub>0</sub>.</li>
<li>The short's value is the negative of the long's.</li>
</ul>
<h3>Forward price with income</h3>
<p class="f">F<sub>0</sub> = (S<sub>0</sub> − PV of income) × (1 + r)<sup>T</sup></p>
<h3>Interest rate forwards</h3>
<p class="f">(1 + z<sub>B</sub>)<sup>B</sup> = (1 + z<sub>A</sub>)<sup>A</sup> × (1 + IFR<sub>A,B−A</sub>)<sup>B−A</sup></p>
<ul>
<li>A <b>forward rate agreement</b> locks in a rate for a future period. The long (fixed-rate payer, like a future borrower) gains if the reference rate at settlement is <b>above</b> the FRA rate.</li>
<li>FRA settlement is usually paid at the start of the interest period, discounted.</li>
</ul>
<h3>Currency forwards</h3>
<p class="f">F<sub>0</sub> (price/base) = S<sub>0</sub> × (1 + r<sub>price</sub>)<sup>T</sup> / (1 + r<sub>base</sub>)<sup>T</sup></p>
<ul>
<li>The currency with the higher interest rate trades at a forward discount.</li>
</ul>
<div class="trap"><b>Exam trap</b>A contract's value is not the difference between the current spot price and the forward price; the forward price must be discounted to today.</div>""",
qs=[
 ["At initiation, the value of a forward contract to the long party is:", ["zero.", "the forward price.", "the spot price."], 0, "The forward price is chosen so that neither party pays anything at the start."],
 ["A one-year forward on a non-dividend-paying share was agreed at $105. Six months later the share trades at $104 and the risk-free rate is 5%. The value of the long position is closest to:", ["−$1.00", "$1.53", "$4.00"], 1, "104 − 105 / 1.05^0.5 = 104 − 102.47 = $1.53."],
 ["If the value of a forward contract to the long party is $3, its value to the short party is:", ["−$3", "$0", "$3"], 0, "The contract is zero-sum: one side's gain is the other's loss."],
 ["The one-year spot rate is 4% and the two-year spot rate is 5%. The one-year rate, one year forward, is closest to:", ["4.50%", "5.00%", "6.01%"], 2, "1.05² / 1.04 − 1 = 6.01%."],
 ["The long side of a forward rate agreement gains if the reference rate at settlement is:", ["above the FRA rate.", "below the FRA rate.", "equal to the FRA rate."], 0, "The long has effectively locked in a borrowing rate, which is valuable if rates turn out higher."],
 ["A share trades at $50 and will pay a dividend with a present value of $1 before expiration. The risk-free rate is 4%. The one-year forward price is closest to:", ["$50.96", "$51.00", "$52.00"], 0, "F0 = (50 − 1) × 1.04 = $50.96."],
 ["The spot USD/EUR exchange rate is 1.2000. One-year rates are 4% for the dollar and 2% for the euro. The one-year forward rate is closest to:", ["1.1769", "1.2000", "1.2235"], 2, "1.2000 × 1.04 / 1.02 = 1.2235. The dollar is the price currency."],
 ["Over the life of a forward contract, the forward price:", ["changes daily with the spot price.", "stays fixed while the contract's value changes.", "is reset to zero at each settlement."], 1, "The agreed price is fixed; what changes is the value of having agreed to it."],
]))
