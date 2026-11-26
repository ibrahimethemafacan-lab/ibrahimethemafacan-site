# CFA Level I · Derivatives · readings 6–10. Original study notes and questions.
R = []

R.append(dict(id="fu", n="Pricing and Valuation of Futures Contracts", k="FUTURES", w=1, c="#2f8f5b",
terms=[
 ["Clearing house", "Takas kurumu", "The exchange's entity that acts as counterparty to all trades and guarantees performance.", "Tüm işlemlerde karşı taraf olan ve yerine getirmeyi garanti eden borsa kuruluşu."],
 ["Daily settlement", "Günlük uzlaşma", "Crediting gains and debiting losses on futures positions at the end of each day.", "Vadeli işlem pozisyonlarındaki kazanç ve kayıpların her gün sonunda hesaba yansıtılması."],
 ["Initial margin", "Başlangıç teminatı", "The deposit required to open a futures position.", "Vadeli işlem pozisyonu açmak için gereken teminat."],
 ["Maintenance margin", "Sürdürme teminatı", "The minimum balance that must be kept in the margin account.", "Teminat hesabında tutulması gereken asgari bakiye."],
 ["Variation margin", "Değişim teminatı", "The amount needed to restore the account to the initial margin after a margin call.", "Teminat çağrısından sonra hesabı başlangıç teminatına getirmek için gereken tutar."],
 ["Settlement price", "Uzlaşma fiyatı", "The official price, usually an average near the close, used for daily settlement.", "Günlük uzlaşmada kullanılan, genellikle kapanışa yakın ortalama olan resmî fiyat."],
 ["Open interest", "Açık pozisyon", "The number of futures contracts outstanding.", "Kapatılmamış vadeli işlem sözleşmesi sayısı."],
 ["Basis", "Baz", "The difference between the spot price and the futures price.", "Spot fiyat ile vadeli fiyat arasındaki fark."],
],
notes="""<h3>Futures versus forwards</h3>
<div class="tbl"><table>
<tr><th></th><th>Futures</th><th>Forwards</th></tr>
<tr><td>Trading</td><td>Exchange, standardized</td><td>Over the counter, customized</td></tr>
<tr><td>Counterparty</td><td>Clearing house</td><td>Other party</td></tr>
<tr><td>Settlement</td><td>Daily mark to market</td><td>At expiration</td></tr>
<tr><td>Credit risk</td><td>Minimal</td><td>Present</td></tr>
<tr><td>Regulation</td><td>Heavy</td><td>Lighter</td></tr>
</table></div>
<h3>Margin mechanics</h3>
<ul>
<li>Open with <b>initial margin</b>. Each day the account is credited or debited with the change in the settlement price × contract size.</li>
<li>If the balance falls below the <b>maintenance margin</b>, the trader must deposit <b>variation margin</b> to bring it back to the <b>initial</b> level.</li>
<li>After each daily settlement the futures position is effectively reset, so its value returns to zero.</li>
</ul>
<h3>Futures prices and forward prices</h3>
<ul>
<li>Without interest rate uncertainty, futures and forward prices are equal.</li>
<li>If the underlying's price is <b>positively</b> correlated with interest rates, longs receive gains when rates are high and can reinvest them at high rates, so <b>futures prices are higher</b> than forward prices. With negative correlation, futures prices are lower.</li>
<li>Interest rate futures are quoted as 100 − the annualized rate; a rate rise lowers the futures price.</li>
</ul>
<div class="trap"><b>Exam trap</b>A margin call restores the account to the initial margin, not just to the maintenance margin.</div>""",
qs=[
 ["The main difference between futures and forwards is that futures are:", ["settled daily.", "customized to each user.", "free of margin requirements."], 0, "Daily mark-to-market settlement is the defining feature of futures."],
 ["A futures account has an initial margin of $2,000 and a maintenance margin of $1,500. After a loss the balance is $1,400. The variation margin required is:", ["$100", "$500", "$600"], 2, "The account must be restored to the initial margin: 2,000 − 1,400 = $600."],
 ["A trader is long one futures contract on 100 units. The settlement price rises from $50.00 to $51.50. The trader's margin account is credited with:", ["$1.50", "$150", "$5,150"], 1, "1.50 × 100 = $150."],
 ["Immediately after daily settlement, the value of a futures contract is:", ["zero.", "the futures price.", "the initial margin."], 0, "Gains and losses have been paid, so the contract is reset to zero value."],
 ["If the price of the underlying is positively correlated with interest rates, futures prices will be:", ["lower than forward prices.", "higher than forward prices.", "equal to forward prices."], 1, "Longs receive cash when rates are high and can reinvest it at those rates, making futures more valuable."],
 ["In futures markets, the counterparty to every trade is the:", ["exchange member.", "clearing house.", "original seller."], 1, "The clearing house stands between buyers and sellers and guarantees performance."],
 ["A short-term interest rate futures contract is quoted at 96.50. The implied annualized interest rate is:", ["3.50%", "6.50%", "96.50%"], 0, "Rate = 100 − 96.50 = 3.50%."],
 ["The number of futures contracts outstanding at a given time is the:", ["volume.", "basis.", "open interest."], 2, "Open interest counts contracts that have not been closed or delivered."],
]))

R.append(dict(id="sw", n="Pricing and Valuation of Interest Rate and Other Swaps", k="SWAPS", w=2, c="#c2417a",
terms=[
 ["Interest rate swap", "Faiz swabı", "An agreement to exchange fixed-rate interest payments for floating-rate payments on a notional amount.", "Nominal tutar üzerinden sabit faiz ödemelerini değişken faiz ödemeleriyle değiştirme anlaşması."],
 ["Fixed-rate payer", "Sabit faiz ödeyen", "The party that pays the fixed rate and receives the floating rate.", "Sabit faiz ödeyip değişken faiz alan taraf."],
 ["Floating-rate payer", "Değişken faiz ödeyen", "The party that pays the floating rate and receives the fixed rate.", "Değişken faiz ödeyip sabit faiz alan taraf."],
 ["Swap rate", "Swap oranı", "The fixed rate that gives a swap zero value at initiation.", "Swaba başlangıçta sıfır değer veren sabit oran."],
 ["Net settlement", "Net uzlaşma", "Paying only the difference between the two parties' obligations.", "Tarafların yükümlülükleri arasındaki farkın ödenmesi."],
 ["Currency swap", "Döviz swabı", "An exchange of interest payments, and usually notional amounts, in two currencies.", "İki para birimindeki faiz ödemelerinin ve genellikle nominal tutarların değişimi."],
 ["Equity swap", "Hisse senedi swabı", "A swap in which at least one leg is based on the return of a share or index.", "En az bir bacağı bir payın veya endeksin getirisine dayanan swap."],
],
notes="""<h3>Interest rate swaps</h3>
<ul>
<li>Payments are netted: on each settlement date only the difference changes hands.</li>
</ul>
<p class="f">net payment by fixed-rate payer = (fixed rate − floating rate) × notional × period</p>
<ul>
<li>A swap is equivalent to a <b>series of forward rate agreements</b>, or to a long position in one bond and a short position in another (fixed-rate bond vs floating-rate note).</li>
<li>The <b>swap rate</b> is set so that the present values of the fixed and the expected floating payments are equal: the swap starts with zero value. It is, in effect, a par rate.</li>
</ul>
<h3>Value after initiation</h3>
<ul>
<li>If market swap rates <b>rise</b> after the swap is agreed, the <b>fixed-rate payer</b> gains: it pays below-market fixed. Value = PV of (new swap rate − old fixed rate) on the remaining payments.</li>
<li>If rates fall, the floating-rate payer gains.</li>
</ul>
<h3>Uses</h3>
<div class="tbl"><table>
<tr><th>Situation</th><th>Swap</th></tr>
<tr><td>Floating-rate borrower wants certainty</td><td>Pay fixed, receive floating</td></tr>
<tr><td>Fixed-rate borrower expects rates to fall</td><td>Pay floating, receive fixed</td></tr>
<tr><td>Investor wants to add duration</td><td>Receive fixed</td></tr>
</table></div>
<h3>Other swaps</h3>
<ul>
<li><b>Currency swaps</b> usually exchange notional amounts at the start and end, plus interest in two currencies.</li>
<li><b>Equity swaps</b> exchange the return on a share or index for a fixed or floating rate.</li>
</ul>
<div class="trap"><b>Exam trap</b>A pay-fixed swap has negative duration: its value rises when rates rise.</div>""",
qs=[
 ["A swap has a notional amount of $10 million. The fixed rate is 4% and the floating rate for the period is 3.5%, with annual settlement. The net payment is:", ["$25,000", "$50,000", "$350,000"], 1, "(4.0% − 3.5%) × 10,000,000 = $50,000, paid by the fixed-rate payer."],
 ["At initiation, the value of a plain interest rate swap is:", ["zero.", "the notional amount.", "the present value of the fixed payments."], 0, "The fixed rate is chosen so that both legs have equal present value."],
 ["After an interest rate swap is agreed, market interest rates rise. The value of the swap to the fixed-rate payer:", ["falls.", "rises.", "is unchanged."], 1, "The fixed-rate payer now pays less than the current market fixed rate."],
 ["An interest rate swap is economically equivalent to:", ["a single option.", "a series of forward rate agreements.", "a series of credit default swaps."], 1, "Each settlement is like an FRA on the floating rate for that period."],
 ["A company with floating-rate debt that wants to lock in its interest cost should enter a swap to:", ["pay fixed and receive floating.", "pay floating and receive fixed.", "pay floating and receive floating."], 0, "Receiving floating offsets the debt's floating payments, leaving a net fixed cost."],
 ["The fixed rate in a newly agreed interest rate swap is best described as a:", ["spot rate.", "par rate.", "forward rate."], 1, "It is the coupon at which a fixed-rate bond matching the swap would trade at par."],
 ["Compared with an interest rate swap, a currency swap typically involves:", ["no interest payments.", "an exchange of notional amounts.", "payments in a single currency."], 1, "Notional amounts in two currencies are usually exchanged at the start and returned at the end."],
 ["To the fixed-rate payer, a swap position behaves like:", ["a long fixed-rate bond and a short floating-rate note.", "a short fixed-rate bond and a long floating-rate note.", "a long position in both a fixed-rate bond and a floating-rate note."], 1, "The payer owes fixed payments (like an issuer) and receives floating payments (like an investor)."],
]))

R.append(dict(id="op", n="Pricing and Valuation of Options", k="OPTIONS", w=2, c="#1f7a8c",
terms=[
 ["Exercise value", "Kullanım değeri", "The value of an option if exercised now; zero if out of the money. Also called intrinsic value.", "Opsiyon şimdi kullanılsaydı sahip olacağı değer; zararda ise sıfır. İçsel değer de denir."],
 ["Time value", "Zaman değeri", "Option premium minus exercise value.", "Opsiyon priminden kullanım değerinin çıkarılmasıyla bulunan tutar."],
 ["Moneyness", "Opsiyonun kârda/zararda olma durumu", "The relationship between the underlying price and the exercise price.", "Dayanak fiyat ile kullanım fiyatı arasındaki ilişki."],
 ["European option", "Avrupa tipi opsiyon", "An option that can be exercised only at expiration.", "Yalnızca vade sonunda kullanılabilen opsiyon."],
 ["American option", "Amerikan tipi opsiyon", "An option that can be exercised at any time up to expiration.", "Vade sonuna kadar herhangi bir zamanda kullanılabilen opsiyon."],
 ["Volatility", "Oynaklık", "The variability of the underlying's returns; the key driver of option time value.", "Dayanağın getirilerinin değişkenliği; opsiyon zaman değerinin temel belirleyicisi."],
 ["Lower bound", "Alt sınır", "The minimum value an option can have without permitting arbitrage.", "Arbitraja izin vermeden bir opsiyonun sahip olabileceği en düşük değer."],
],
notes="""<h3>Exercise value and time value</h3>
<p class="f">call exercise value = max(0, S − X) &nbsp;&nbsp;&nbsp; put exercise value = max(0, X − S)</p>
<p class="f">option value = exercise value + time value</p>
<ul>
<li>Time value reflects the chance that the option will become more valuable before expiration. It falls to zero at expiration.</li>
<li>An out-of-the-money option has only time value.</li>
</ul>
<h3>No-arbitrage bounds for European options</h3>
<p class="f">call: max(0, S<sub>0</sub> − X/(1+r)<sup>T</sup>) ≤ c ≤ S<sub>0</sub></p>
<p class="f">put: max(0, X/(1+r)<sup>T</sup> − S<sub>0</sub>) ≤ p ≤ X/(1+r)<sup>T</sup></p>
<h3>What moves option values</h3>
<div class="tbl"><table>
<tr><th>Increase in</th><th>Call</th><th>Put</th></tr>
<tr><td>Price of the underlying</td><td>Up</td><td>Down</td></tr>
<tr><td>Exercise price</td><td>Down</td><td>Up</td></tr>
<tr><td>Risk-free rate</td><td>Up</td><td>Down</td></tr>
<tr><td>Volatility</td><td>Up</td><td>Up</td></tr>
<tr><td>Time to expiration</td><td>Up</td><td>Usually up (a deep in-the-money European put can fall)</td></tr>
<tr><td>Income on the underlying (dividends)</td><td>Down</td><td>Up</td></tr>
<tr><td>Carrying costs</td><td>Up</td><td>Down</td></tr>
</table></div>
<h3>American and European options</h3>
<ul>
<li>An American option is worth at least as much as the equivalent European option.</li>
<li>An American <b>call</b> on a non-dividend-paying asset should never be exercised early, so it is worth the same as a European call.</li>
<li>An American put may be worth exercising early when deep in the money, so it can be worth more than a European put.</li>
</ul>
<div class="trap"><b>Exam trap</b>Higher volatility raises the value of both calls and puts: the downside is limited to the premium while the upside grows.</div>""",
qs=[
 ["A call has an exercise price of $50 and the share trades at $55. The call's exercise value is:", ["$0", "$5", "$55"], 1, "max(0, 55 − 50) = $5."],
 ["A call with an exercise value of $5 trades at a premium of $7. Its time value is:", ["$2", "$5", "$7"], 0, "Time value = 7 − 5 = $2."],
 ["An increase in the volatility of the underlying will most likely:", ["increase call values and decrease put values.", "decrease call values and increase put values.", "increase both call and put values."], 2, "Greater volatility raises the chance of large favourable moves for both, while losses are capped at the premium."],
 ["An increase in the risk-free rate will most likely:", ["increase call values and decrease put values.", "decrease call values and increase put values.", "increase both call and put values."], 0, "A higher rate lowers the present value of the exercise price, which helps calls and hurts puts."],
 ["A one-year European call has an exercise price of $50. The share trades at $55 and the risk-free rate is 5%. The lower bound on the call's value is closest to:", ["$0.00", "$5.00", "$7.38"], 2, "55 − 50 / 1.05 = 55 − 47.62 = $7.38."],
 ["An American call on a share that pays no dividends is worth:", ["less than an equivalent European call.", "the same as an equivalent European call.", "more than an equivalent European call."], 1, "Early exercise would give up time value, so the right to exercise early is worthless."],
 ["An out-of-the-money option's value consists of:", ["exercise value only.", "time value only.", "both exercise value and time value."], 1, "Its exercise value is zero, so all its value is time value."],
 ["An increase in the expected dividends on the underlying share will most likely:", ["increase call values.", "decrease call values.", "have no effect on call values."], 1, "Dividends lower the share price when paid, which reduces the value of the right to buy it."],
]))

R.append(dict(id="pc", n="Option Replication Using Put–Call Parity", k="PARITY", w=1, c="#3b7dd8",
terms=[
 ["Put–call parity", "Alım-satım opsiyonu paritesi", "The no-arbitrage relationship linking European call and put prices with the same exercise price and expiration.", "Aynı kullanım fiyatı ve vadeye sahip Avrupa tipi alım ve satım opsiyonu fiyatlarını bağlayan arbitrajsızlık ilişkisi."],
 ["Fiduciary call", "Güvenceli alım", "A long call plus a risk-free bond that pays the exercise price at expiration.", "Uzun alım opsiyonu artı vade sonunda kullanım fiyatını ödeyen risksiz tahvil."],
 ["Protective put", "Koruyucu satım", "A long share plus a long put on it.", "Uzun pay pozisyonu artı o pay üzerine uzun satım opsiyonu."],
 ["Covered call", "Örtülü alım", "A long share plus a short call on it.", "Uzun pay pozisyonu artı o pay üzerine kısa alım opsiyonu."],
 ["Synthetic call", "Sentetik alım", "A position replicating a call: long share, long put, borrowing the present value of the exercise price.", "Alım opsiyonunu kopyalayan pozisyon: uzun pay, uzun satım, kullanım fiyatının bugünkü değeri kadar borçlanma."],
 ["Synthetic put", "Sentetik satım", "A position replicating a put: long call, short share, lending the present value of the exercise price.", "Satım opsiyonunu kopyalayan pozisyon: uzun alım, kısa pay, kullanım fiyatının bugünkü değeri kadar borç verme."],
 ["Put–call forward parity", "Alım-satım-forward paritesi", "Put–call parity with a forward contract in place of the underlying.", "Dayanak yerine forward sözleşmesi kullanılan alım-satım paritesi."],
],
notes="""<h3>The relationship</h3>
<p class="f">S<sub>0</sub> + p<sub>0</sub> = c<sub>0</sub> + X / (1 + r)<sup>T</sup></p>
<ul>
<li>Left: a <b>protective put</b>. Right: a <b>fiduciary call</b>. At expiration both are worth max(S<sub>T</sub>, X), so they must cost the same today.</li>
<li>Holds for European options with the same underlying, exercise price and expiration.</li>
</ul>
<h3>Rearranging to create synthetics</h3>
<div class="tbl"><table>
<tr><th>Synthetic</th><th>Formula</th></tr>
<tr><td>Call</td><td>c = S + p − X/(1+r)<sup>T</sup></td></tr>
<tr><td>Put</td><td>p = c − S + X/(1+r)<sup>T</sup></td></tr>
<tr><td>Share</td><td>S = c − p + X/(1+r)<sup>T</sup></td></tr>
<tr><td>Risk-free bond</td><td>X/(1+r)<sup>T</sup> = S + p − c</td></tr>
</table></div>
<ul>
<li>A plus sign means a long position, a minus sign a short one (for the bond, minus means borrowing).</li>
<li>A <b>covered call</b> (S − c) equals a risk-free bond minus a put: PV(X) − p.</li>
</ul>
<h3>Arbitrage when parity fails</h3>
<ul>
<li>If the call is too expensive relative to parity, sell the call and buy the synthetic call; and vice versa.</li>
</ul>
<h3>Put–call forward parity</h3>
<p class="f">F<sub>0</sub> / (1 + r)<sup>T</sup> + p<sub>0</sub> = c<sub>0</sub> + X / (1 + r)<sup>T</sup></p>
<ul>
<li>A long forward can be replicated with a long call and a short put at the same exercise price.</li>
</ul>
<div class="trap"><b>Exam trap</b>The bond in put–call parity pays the exercise price at expiration, so use its present value, not X itself.</div>""",
qs=[
 ["A share trades at $50. A one-year European call with an exercise price of $50 costs $6, and the risk-free rate is 4%. According to put–call parity, the matching put is worth closest to:", ["$2.00", "$4.08", "$6.00"], 1, "p = c + X/(1 + r) − S = 6 + 48.08 − 50 = $4.08."],
 ["A protective put has the same payoff at expiration as a:", ["covered call.", "fiduciary call.", "short forward."], 1, "Both are worth max(S, X) at expiration."],
 ["A synthetic call can be created by:", ["buying the share, buying a put and borrowing the present value of the exercise price.", "selling the share, buying a put and lending the present value of the exercise price.", "buying the share, selling a put and lending the present value of the exercise price."], 0, "c = S + p − PV(X)."],
 ["A synthetic put can be created by:", ["buying a call, buying the share and borrowing.", "buying a call, selling the share and lending.", "selling a call, buying the share and lending."], 1, "p = c − S + PV(X)."],
 ["A covered call position is equivalent to:", ["a long put plus a risk-free bond.", "a risk-free bond minus a put.", "a long call minus a risk-free bond."], 1, "S − c = PV(X) − p."],
 ["If a call is priced above the value implied by put–call parity, an arbitrageur should:", ["buy the call and sell the synthetic call.", "sell the call and buy the synthetic call.", "buy both the call and the put."], 1, "Sell the overpriced instrument and buy its cheaper replica."],
 ["Put–call parity in its basic form applies to:", ["American options only.", "European options only.", "any option regardless of exercise style."], 1, "Early exercise of American options can break the exact relationship."],
 ["A long call and a short put with the same exercise price and expiration replicate a:", ["long forward.", "short forward.", "risk-free bond."], 0, "This is put–call forward parity: c − p equals a long forward position in present value terms."],
]))

R.append(dict(id="bi", n="Valuing a Derivative Using a One-Period Binomial Model", k="BINOMIAL", w=1, c="#2e9e8f",
terms=[
 ["Binomial model", "İki terimli (binom) model", "A model in which the underlying moves to one of two prices over each period.", "Dayanağın her dönemde iki fiyattan birine hareket ettiği model."],
 ["Up factor", "Yükseliş çarpanı", "One plus the return on the underlying in the up state.", "Yükseliş durumunda dayanağın getirisi artı bir."],
 ["Down factor", "Düşüş çarpanı", "One plus the return on the underlying in the down state.", "Düşüş durumunda dayanağın getirisi artı bir."],
 ["Risk-neutral probability", "Risk nötr olasılık", "The probability of the up move that makes the expected return on the underlying equal the risk-free rate.", "Dayanağın beklenen getirisini risksiz faize eşitleyen yükseliş olasılığı."],
 ["Hedge ratio", "Korunma oranı", "The number of units of the underlying needed per option to create a riskless portfolio.", "Risksiz portföy oluşturmak için opsiyon başına gereken dayanak birim sayısı."],
 ["Riskless hedge portfolio", "Risksiz korunma portföyü", "A combination of the underlying and the option whose value is the same in both states.", "Değeri her iki durumda da aynı olan dayanak ve opsiyon bileşimi."],
],
notes="""<h3>Set-up</h3>
<ul>
<li>The underlying, now S<sub>0</sub>, moves to S<sup>+</sup> = uS<sub>0</sub> or S<sup>−</sup> = dS<sub>0</sub>. The option's value in each state is its payoff.</li>
</ul>
<p class="f">risk-neutral probability of up: π = (1 + r − d) / (u − d)</p>
<p class="f">option value = [π × V<sup>+</sup> + (1 − π) × V<sup>−</sup>] / (1 + r)</p>
<ul>
<li>The actual probabilities of up and down moves are not needed.</li>
</ul>
<h3>The hedge</h3>
<p class="f">hedge ratio = (V<sup>+</sup> − V<sup>−</sup>) / (S<sup>+</sup> − S<sup>−</sup>)</p>
<ul>
<li>Selling one call and buying hedge-ratio units of the underlying produces the same value in both states. That portfolio is riskless and must earn the risk-free rate, which pins down the option price.</li>
<li>If the market price differs from the model value, an arbitrage exists: sell the overpriced side and hedge.</li>
</ul>
<h3>Worked pattern</h3>
<ul>
<li>S<sub>0</sub> = 100, u = 1.2, d = 0.8, r = 5%, call with X = 100.</li>
<li>π = (1.05 − 0.8) / 0.4 = 0.625. Call payoffs: 20 up, 0 down.</li>
<li>Call value = 0.625 × 20 / 1.05 = 11.90. Hedge ratio = 20 / 40 = 0.5.</li>
<li>Matching put: payoffs 0 up, 20 down; value = 0.375 × 20 / 1.05 = 7.14.</li>
</ul>
<ul>
<li>A wider spread between u and d means higher volatility and a higher option value.</li>
</ul>
<div class="trap"><b>Exam trap</b>Discount with the risk-free rate, not with the expected return on the underlying.</div>""",
qs=[
 ["A share at $100 can rise to $120 or fall to $80 in one period. The risk-free rate is 5%. The risk-neutral probability of an up move is:", ["0.500", "0.625", "0.750"], 1, "π = (1.05 − 0.80) / (1.20 − 0.80) = 0.625."],
 ["A share at $100 can rise to $120 or fall to $80 in one period, and the risk-free rate is 5%. A call with an exercise price of $100 is worth closest to:", ["$10.00", "$11.90", "$12.50"], 1, "0.625 × 20 / 1.05 = $11.90."],
 ["A share at $100 can rise to $120 or fall to $80 in one period. The hedge ratio for a call with an exercise price of $100 is:", ["0.25", "0.50", "1.00"], 1, "(20 − 0) / (120 − 80) = 0.50 shares per call."],
 ["A share at $100 can rise to $120 or fall to $80 in one period, and the risk-free rate is 5%. A put with an exercise price of $100 is worth closest to:", ["$7.14", "$9.52", "$10.00"], 0, "Put payoffs are 0 and 20: 0.375 × 20 / 1.05 = $7.14."],
 ["In the binomial model, the actual probabilities of up and down moves are:", ["needed to value the option.", "not needed to value the option.", "always equal to 0.5."], 1, "The option is valued by replication, so only u, d and r matter."],
 ["All else equal, a larger difference between the up and down factors will:", ["increase the option's value.", "decrease the option's value.", "have no effect on the option's value."], 0, "A wider range means higher volatility, which raises option values."],
 ["In the binomial model, expected option payoffs are discounted at the:", ["risk-free rate.", "expected return on the share.", "investor's required return."], 0, "Under risk-neutral pricing, the riskless hedge portfolio must earn the risk-free rate."],
 ["If a call trades above its binomial model value, an arbitrageur should:", ["buy the call and sell shares.", "sell the call and buy the hedge ratio of shares.", "buy both the call and the shares."], 1, "Sell the overpriced call and hedge with the underlying to lock in the difference."],
]))
