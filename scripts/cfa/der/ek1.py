# CFA Level I · Derivatives · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
EK = {}

EK["df"] = dict(
terms=[
 ["Cash-settled contract", "Nakit uzlaşmalı sözleşme", "A derivative settled by paying only the net gain or loss, without delivery of the underlying.", "Dayanak varlık teslim edilmeden yalnızca net kâr veya zararın ödendiği türev."],
 ["Deliverable contract", "Teslimatlı sözleşme", "A derivative settled by delivery of the underlying asset against payment.", "Dayanak varlığın ödeme karşılığında teslim edildiği türev."],
],
notes="""<h3>More on derivative markets</h3>
<ul>
<li>Exchange-traded derivatives are standardized, <b>liquid</b>, and guaranteed by a clearinghouse, which acts as counterparty to both sides and guarantees that all obligations are honoured.</li>
<li>A long forward gains when the underlying rises; a <b>short</b> forward (agreeing to sell) gains when it falls. A hedger who owns shares and sells them forward gains on the forward when the share price falls.</li>
<li>A long interest rate forward gains when the reference rate rises.</li>
<li>At initiation, a forward contract is priced so that its <b>value is zero</b> to both parties.</li>
<li>Derivatives usually have <b>lower transaction costs</b> and less price impact than an equivalent trade in the underlying.</li>
</ul>""",
qs=[
 ["Which statement about exchange-traded derivatives is least accurate?", ["They are guaranteed by a clearinghouse.", "They are illiquid.", "They are standardized."], 1, "Standardization makes exchange-traded contracts liquid."],
 ["An investor who owns shares enters a forward contract to sell them at a fixed price. She will gain on the forward contract if the share price:", ["rises.", "falls.", "stays unchanged."], 1, "A short forward gains when the market price ends below the agreed price."],
 ["An investor is long an interest rate forward on a reference rate. At settlement the reference rate is higher than the agreed rate. The investor has:", ["a gain.", "a loss.", "neither a gain nor a loss."], 0, "The long side of an interest rate forward benefits from higher rates."],
 ["Two parties agree a six-month forward on 500 shares at $30 per share. The interest rate is 4%. At initiation, the value of the contract to the buyer is closest to:", ["$0", "$14,700", "$15,000"], 0, "Forward prices are set so that neither party pays anything at initiation."],
 ["A derivative is best defined as an instrument whose value:", ["is set in a private agreement.", "is determined outside an exchange.", "depends on the value of an underlying."], 2, "The defining feature is that value is derived from an underlying asset, rate or index."],
 ["A forward contract under which only the net gain or loss is paid at expiration is a:", ["cash-settled contract.", "deliverable contract.", "netted contract."], 0, "Cash settlement replaces delivery with a payment of the difference."],
 ["Compared with an equivalent transaction in the underlying, a derivative position typically has:", ["higher transaction costs.", "lower transaction costs.", "a greater impact on the underlying's price."], 1, "Derivatives need little capital and trade in liquid standardized markets."],
 ["The main role of a futures clearinghouse is to:", ["guarantee the obligations of both parties.", "set the prices of futures contracts.", "limit daily price movements of the underlying."], 0, "The clearinghouse is the buyer to every seller and the seller to every buyer."],
])

EK["fc"] = dict(
terms=[
 ["Contingent claim", "Koşullu hak", "A derivative whose payoff depends on a specified event occurring, such as an option or a credit default swap.", "Getirisi belirli bir olayın gerçekleşmesine bağlı türev; örneğin opsiyon veya kredi temerrüt swabı."],
 ["Writer", "Opsiyon satıcısı (yazan)", "The party that sells an option, receives the premium and has the obligation if the option is exercised.", "Opsiyonu satan, primi alan ve opsiyon kullanılırsa yükümlülük taşıyan taraf."],
],
notes="""<h3>Option payoffs and margin</h3>
<ul>
<li>Call value at expiration = max(0, S<sub>T</sub> − X). Put value = max(0, X − S<sub>T</sub>). Option values are <b>never negative</b> for the holder.</li>
<li>Profit = value at expiration − premium for the buyer; the writer's profit is the opposite.</li>
<li>Breakeven: call X + premium; put X − premium, for both buyer and writer.</li>
<li>Put moneyness: in the money when S &lt; X, by X − S.</li>
<li>A put holder has the right to <b>sell</b>; a put writer must <b>buy</b> if exercised. A call holder has the right to buy; a call writer must sell.</li>
<li>If the margin balance falls below the <b>maintenance margin</b>, the trader must deposit enough to restore it to the <b>initial margin</b>.</li>
<li>The settlement price is an <b>average of trade prices</b> at the end of the session, not the last trade.</li>
<li>A credit default swap is a contingent claim similar to insurance, not a forward commitment. The protection buyer makes periodic payments to the seller.</li>
<li>Forward commitments are legally binding.</li>
</ul>""",
qs=[
 ["Which statement about a forward commitment is least accurate?", ["It can be based on a stock index.", "It is a contractual promise.", "It is not legally binding."], 2, "Forwards, futures and swaps legally oblige both parties to perform."],
 ["A European call has an exercise price of 55. At expiration the share trades at 51. The option's value is:", ["negative.", "zero.", "positive."], 1, "The holder will not exercise, so the value is zero, never negative."],
 ["A trader's futures account falls below the maintenance margin. To keep the position open, she must deposit enough to bring the account back to the:", ["maintenance margin.", "variation margin.", "initial margin."], 2, "A margin call restores the balance to the initial margin level."],
 ["A contract giving the holder the right, but not the obligation, to sell an asset at a set price on a set date is a:", ["call option.", "put option.", "forward contract."], 1, "The right to sell is a put."],
 ["The daily settlement price of a futures contract is typically:", ["the last trade price of the day.", "an average of trade prices near the close.", "the opening price of the next day."], 1, "Averaging prices over the closing period makes the settlement price harder to manipulate."],
 ["Which statement about options is most accurate?", ["The holder of a put has the right to sell to the writer.", "The writer of a put must sell the asset if the option is exercised.", "The holder of a call must sell if the price rises above the strike."], 0, "The put writer must buy, and the call holder has a right, not an obligation."],
 ["A derivative whose payoff depends on a specified event occurring is best described as:", ["a contingent claim.", "a forward commitment.", "a swap."], 0, "Options and credit default swaps are contingent claims."],
 ["An investor pays a premium of $3 for a call with an exercise price of $30. At expiration the share is at $31.50. Her profit is closest to:", ["−$3.00", "−$1.50", "+$1.50"], 1, "Exercise value 1.50 minus the 3.00 premium gives −1.50."],
 ["A trader writes a put with an exercise price of $50 for a premium of $2.60. At expiration the share is at $62. Her profit is:", ["$2.60", "$9.40", "$14.60"], 0, "The put expires worthless, so the writer keeps the whole premium."],
 ["An investor pays $2.20 for a put with an exercise price of $90. At expiration the share is at $76. His profit is:", ["$2.20", "$11.80", "$16.20"], 1, "Exercise value 14.00 minus the 2.20 premium."],
 ["Which statement about call options is most accurate?", ["The buyer's breakeven price is the exercise price plus the premium.", "The seller's breakeven price is the exercise price minus the premium.", "The holder exercises when the exercise price is above the share price."], 0, "Buyer and seller share the same breakeven: X + premium."],
 ["A share trades at $36. A put on it with an exercise price of $42 costs $8. The put is:", ["out of the money by $2.", "in the money by $6.", "in the money by $8."], 1, "A put is in the money by X − S = 42 − 36. The premium does not affect moneyness."],
 ["At expiration, the value of a European call option is equal to its:", ["intrinsic value.", "time value.", "premium paid."], 0, "No time is left, so only the exercise value remains."],
 ["A credit default swap is least accurately described as:", ["a contingent claim.", "a form of insurance.", "a forward commitment."], 2, "Payment by the seller depends on a credit event, so it is a contingent claim."],
 ["A call has an exercise price of $45. At expiration the share trades at $52. The call's value is:", ["$0", "$7", "$52"], 1, "max(0, 52 − 45) = 7."],
 ["A put has an exercise price of $70. At expiration the share trades at $58. The put's value is:", ["$0", "$12", "$58"], 1, "max(0, 70 − 58) = 12."],
 ["An investor holds a European put. At expiration the share price is above the exercise price. The put's value to the investor is:", ["negative.", "zero.", "positive."], 1, "The put will not be exercised; its value cannot be negative."],
])

EK["du"] = dict(
notes="""<h3>More on uses of derivatives</h3>
<ul>
<li><b>Liquidity</b> is both an advantage (low cash requirement for large positions) and a disadvantage (the implied leverage creates more risk).</li>
<li>Hedge accounting: a <b>fair value hedge</b> offsets changes in the value of an asset or liability, such as a fixed-rate bond or inventory; a <b>cash flow hedge</b> offsets variable cash flows; a <b>net investment hedge</b> offsets changes in the value of a foreign subsidiary.</li>
<li>To protect a share holding while keeping upside, <b>buy a put</b>. To gain upside with limited loss without owning the asset, <b>buy a call</b>.</li>
<li>Companies can hedge the currency risk of expected receipts and payments with forwards.</li>
<li>In option pricing, the volatility of the underlying is the only input that cannot be observed directly.</li>
</ul>""",
qs=[
 ["Compared with cash markets, which feature of derivatives is both an advantage and a disadvantage?", ["Liquidity", "Short selling", "Market efficiency"], 0, "Low cash needs make large positions easy, but the leverage involved adds risk."],
 ["A company uses an interest rate swap to offset changes in the value of its fixed-rate bonds. Under hedge accounting, this is a:", ["fair value hedge.", "cash flow hedge.", "net investment hedge."], 0, "It hedges the value of a liability, not a stream of variable cash flows."],
 ["Which input to an option pricing model is not directly observable?", ["Exercise price", "Risk-free rate", "Volatility of the underlying"], 2, "Volatility must be estimated."],
 ["A company uses derivatives to reduce changes in the value of its inventory. Under hedge accounting, this is most likely a:", ["fair value hedge.", "cash flow hedge.", "net investment hedge."], 0, "Hedging the value of an asset is a fair value hedge."],
 ["A shareholder wants to protect against a fall in the share price while keeping the potential gains. The most appropriate action is to:", ["sell calls.", "buy calls.", "buy puts."], 2, "A protective put sets a floor and leaves the upside open."],
 ["Which statement about the use of derivatives is most accurate?", ["A manufacturer can hedge the currency risk of expected foreign receipts.", "A portfolio manager cannot reduce exposure to a market index.", "Converting fixed-rate debt to floating always reduces risk."], 0, "Currency forwards lock in the rate for future receipts or payments."],
 ["An investor wants to profit from a rise in an asset's price, with limited loss, without owning the asset. She should:", ["buy a call.", "buy a put.", "buy a call and a put."], 0, "A long call gives the upside; the maximum loss is the premium."],
])

EK["ar"] = dict(
notes="""<h3>More on the cost of carry</h3>
<ul>
<li>Pricing models assume <b>arbitrage opportunities are exploited quickly</b> and so do not persist.</li>
<li>Costs of holding the underlying (storage, insurance) <b>raise</b> the forward price; benefits (dividends, coupons, convenience yield) <b>lower</b> it.</li>
<li>With no costs or benefits, the forward price at initiation is the <b>future value of the spot price</b>. A quoted forward price below that allows a reverse cash-and-carry arbitrage.</li>
</ul>
<p class="f">F<sub>0</sub> = [S<sub>0</sub> + PV(costs) − PV(benefits)] × (1 + R<sub>f</sub>)<sup>T</sup></p>""",
qs=[
 ["Derivatives pricing models assume that:", ["investors are risk neutral.", "arbitrage opportunities are exploited quickly.", "arbitrage never occurs in practice."], 1, "Prices are set so that no arbitrage is possible, because any opportunity would be traded away."],
 ["A net benefit from holding the underlying asset will:", ["raise the forward price at initiation.", "lower the forward price at initiation.", "not affect the forward price."], 1, "The long forward holder does not receive the benefit, so the forward price is lower."],
 ["Costs of holding the underlying that exceed the benefits will:", ["raise the forward price.", "lower the forward price.", "not affect the forward price."], 0, "The buyer avoids those net costs by waiting, so pays more forward."],
 ["Other things equal, higher storage costs for a commodity will:", ["lower its forward price.", "not affect its forward price.", "raise its forward price."], 2, "Storage is a cost of carry."],
 ["Which change is most likely to raise an asset's no-arbitrage forward price?", ["Higher dividends on a stock", "A lower convenience yield on a commodity", "Lower storage costs for a commodity"], 1, "Convenience yield is a benefit, so a lower one raises the forward price."],
 ["An asset has no costs or benefits of holding. An arbitrage profit is possible if the forward price is:", ["equal to the future value of the spot price.", "below the future value of the spot price.", "above the present value of the spot price."], 1, "The arbitrageur shorts the asset, invests the proceeds and buys forward."],
 ["Other things equal, an asset's forward price will be higher if the asset has:", ["storage costs.", "dividends.", "a convenience yield."], 0, "Storage is a cost; the other two are benefits."],
 ["For an asset with no costs or benefits of holding, the no-arbitrage forward price at initiation is:", ["zero.", "the spot price.", "the future value of the spot price."], 2, "F₀ = S₀ × (1 + Rf)^T."],
])

EK["fw"] = dict(
notes="""<h3>Value of a forward during its life</h3>
<p class="f">V<sub>t</sub> (long) = S<sub>t</sub> − F<sub>0</sub>(T) × (1 + R<sub>f</sub>)<sup>−(T−t)</sup></p>
<ul>
<li>A forward rate agreement locks in an interest rate for future borrowing or lending; it is a commitment, not an option.</li>
<li>The value of a forward or futures contract is typically zero at initiation; the price is fixed in the contract.</li>
</ul>""",
qs=[
 ["For an asset with no costs or benefits of holding, the value of a long forward during its life equals the:", ["spot price minus the present value of the forward price.", "spot price minus the forward price.", "present value of the spot price minus the forward price."], 0, "Vt = St − F₀(T)/(1 + Rf)^(T−t)."],
 ["A company most likely uses a forward rate agreement to:", ["lock in an interest rate for future borrowing.", "obtain the right, but not the obligation, to borrow at a set rate.", "swap fixed-rate debt for floating-rate debt."], 0, "An FRA fixes the rate for a future period; an option would give a right without an obligation."],
 ["The value of a forward or futures contract is:", ["fixed in the contract.", "typically zero at initiation.", "equal to the spot price at expiration."], 1, "The price is set so that no money changes hands at the start."],
 ["A one-year forward on an asset with no holding costs or benefits was agreed at 60. Six months later, the spot price is 63 and the annual risk-free rate is 4%. The value of the long position is closest to:", ["2.94", "3.00", "4.17"], 2, "63 − 60/1.04^0.5 = 63 − 58.83 = 4.17."],
])

EK["fu"] = dict(
notes="""<h3>Futures versus forwards</h3>
<ul>
<li>If interest rates are <b>positively correlated</b> with the underlying price, daily settlement helps the long: gains are reinvested at higher rates. Futures are then preferred and priced <b>above</b> forwards.</li>
<li>If the correlation is <b>negative</b>, forwards are preferred by longs and futures are priced <b>below</b> forwards.</li>
<li>Daily settlement resets the futures price to the settlement price, so the contract's value returns to zero; both price and value change.</li>
<li>FRA payments are discounted at the realized rate, so FRAs show <b>convexity</b>; interest rate futures payoffs are linear.</li>
</ul>""",
qs=[
 ["A long futures position may be preferred to an equivalent forward when interest rates are:", ["positively correlated with the underlying price.", "negatively correlated with the underlying price.", "uncorrelated with the underlying price."], 0, "Gains from daily settlement are then received when rates are high and can be reinvested."],
 ["A commodity's six-month forward price is 81.40 and its six-month futures price is 81.25. This most likely indicates that:", ["futures prices are negatively correlated with interest rates.", "longs should prefer futures to forwards.", "there is an arbitrage opportunity."], 0, "Futures priced below forwards suggest negative correlation between the underlying and interest rates."],
 ["Daily settlement of a futures contract results in:", ["a change in its price but not its value.", "a change in both its price and its value.", "a change in its value but not its price."], 1, "Gains and losses are paid, the price resets to the settlement price, and the value returns to zero."],
 ["A long forward may be preferred to an equivalent futures contract when interest rates are:", ["positively correlated with the underlying price.", "negatively correlated with the underlying price.", "uncorrelated with the underlying price."], 1, "Daily settlement would then produce gains when rates are low and losses when they are high."],
 ["A forward price above an equivalent futures price is most likely explained by:", ["daily settlement of futures but not forwards.", "greater liquidity of forwards.", "difficulty of exiting a futures position."], 0, "Daily settlement, combined with the correlation of prices and rates, creates the difference."],
 ["Compared with an interest rate futures contract, an equivalent forward rate agreement:", ["has a linear payoff.", "exhibits convexity.", "pays more for a fall in rates."], 1, "FRA payoffs are discounted at the realized rate, which makes them convex."],
])

EK["sw"] = dict(
notes="""<h3>Swap pricing and replication</h3>
<ul>
<li>At initiation, a swap's <b>value</b> is zero; its <b>price</b> (the swap rate) is set at initiation and does not change.</li>
<li>A swap is equivalent to a series of forward contracts whose values at initiation <b>sum to zero</b>; individually they need not be zero.</li>
<li>The receive-fixed, pay-floating party is like someone who <b>holds a fixed-rate bond and borrows at a floating rate</b>.</li>
</ul>""",
qs=[
 ["Which of the following is typically zero when an interest rate swap is agreed?", ["Its value", "Its price", "Both its value and its price"], 0, "The swap rate is chosen so that the value is zero; the rate itself is not zero."],
 ["The position of the floating-rate payer in an interest rate swap is best replicated by:", ["borrowing at a floating rate and buying a fixed-rate bond.", "borrowing at a fixed rate and buying a floating-rate note.", "borrowing at a floating rate and entering zero-value FRAs."], 0, "The floating payer receives fixed, like a bondholder, and pays floating, like a floating-rate borrower."],
 ["The price of a fixed-for-floating interest rate swap is:", ["set when the swap is agreed.", "reset each payment period.", "directly linked to the floating rate."], 0, "The swap rate is fixed at initiation; it is the swap's value that changes."],
 ["For a series of forward contracts to replicate a swap, the forwards must have:", ["values at initiation that sum to zero.", "values at initiation that are each zero.", "values at expiration that sum to zero."], 0, "They all use the same fixed rate, so some have positive and some negative initial values."],
])

EK["op"] = dict(
terms=[
 ["Upper bound", "Üst sınır", "The maximum no-arbitrage value of an option: the share price for a call, the present value of the exercise price for a European put.", "Bir opsiyonun arbitrajsız azami değeri: alım opsiyonu için pay fiyatı, Avrupa tipi satım opsiyonu için kullanım fiyatının bugünkü değeri."],
],
notes="""<h3>Option value bounds and factors</h3>
<div class="tbl"><table>
<tr><th>Option</th><th>Lower bound</th><th>Upper bound</th></tr>
<tr><td>European call</td><td>max[0, S − PV(X)]</td><td>S</td></tr>
<tr><td>European put</td><td>max[0, PV(X) − S]</td><td>PV(X)</td></tr>
</table></div>
<ul>
<li>Bounds are never negative. Only options have no-arbitrage <b>upper and lower</b> bounds; forwards do not.</li>
<li>Option value = intrinsic (exercise) value + time value. An out-of-the-money option's whole premium is time value; time value falls toward zero at expiration.</li>
<li>Calls are in the money when S &gt; X, puts when S &lt; X.</li>
</ul>
<div class="tbl"><table>
<tr><th>Increase in</th><th>Call</th><th>Put</th></tr>
<tr><td>Underlying price</td><td>↑</td><td>↓</td></tr>
<tr><td>Exercise price</td><td>↓</td><td>↑</td></tr>
<tr><td>Risk-free rate</td><td>↑</td><td>↓</td></tr>
<tr><td>Volatility</td><td>↑</td><td>↑</td></tr>
<tr><td>Time to expiration</td><td>↑</td><td>↑ (usually; a European put can be an exception)</td></tr>
<tr><td>Dividends/income</td><td>↓</td><td>↑</td></tr>
</table></div>""",
qs=[
 ["The lower and upper bounds on European option values are always:", ["nonnegative.", "positive.", "based on the present value of the exercise price."], 0, "Bounds can be zero but never negative. The call's upper bound, the share price, involves no present value."],
 ["Which statement comparing forwards and options is most accurate?", ["Neither the forward buyer nor the option buyer pays cash at the start.", "Only options have upper and lower no-arbitrage price bounds.", "The option buyer's loss is unlimited."], 1, "An option buyer pays a premium and has a limited loss; forwards have no bounds."],
 ["The time value of an option:", ["equals the whole premium for an out-of-the-money option.", "rises as expiration approaches.", "is the amount by which intrinsic value exceeds the premium."], 0, "An out-of-the-money option has no intrinsic value."],
 ["When the share price is above the exercise price:", ["a call is out of the money.", "a put is out of the money.", "a put is in the money."], 1, "A put is in the money only when the price is below the exercise price."],
 ["An increase in the risk-free rate, other things equal, will:", ["increase call values and decrease put values.", "decrease call values and increase put values.", "decrease both call and put values."], 0, "A higher rate lowers the present value of the exercise price."],
 ["The value of a put is most likely to increase with:", ["a lower exercise price.", "a higher risk-free rate.", "higher volatility of the underlying."], 2, "Volatility raises the value of both calls and puts."],
 ["A holder will exercise a European put at expiration if the share price is:", ["below the exercise price.", "equal to the exercise price.", "above the exercise price."], 0, "The put then has positive exercise value."],
 ["Dividends paid on the underlying share will:", ["decrease the value of a call.", "increase the value of a call.", "not affect the value of a call."], 0, "Dividends lower the share price and are not received by the call holder."],
 ["For a European put:", ["time value equals market price minus exercise value.", "intrinsic value equals market price plus exercise value.", "exercise value equals share price minus exercise price."], 0, "Premium = exercise value + time value."],
 ["An investor holds a call with an exercise price of 40 and a put with an exercise price of 46 on the same share, which trades at 43. Which options are in the money?", ["Only the call", "Both options", "Neither option"], 1, "The call is in the money because 43 > 40; the put because 43 < 46."],
 ["Which statement about the lower bound of a European put is most accurate?", ["It is always zero.", "It can be negative for deep out-of-the-money puts.", "It is the greater of zero and PV(X) − S."], 2, "The bound cannot be negative."],
 ["A one-year European call has an exercise price of 200. Six months later the share trades at 212. The no-arbitrage upper bound on the call is:", ["200", "206", "212"], 2, "A call can never be worth more than the share itself."],
 ["An investor is long a European put and short a European call. Other things equal, a fall in the risk-free rate will increase the value of:", ["only the put position.", "both positions.", "neither position."], 1, "Lower rates raise put values and lower call values, which helps the short call."],
 ["A short put position becomes more valuable if:", ["the time to expiration increases.", "the volatility of the underlying increases.", "the price of the underlying increases."], 2, "A higher share price lowers the put's value, which benefits the writer."],
 ["At expiration, exercise value equals time value for:", ["an out-of-the-money call or an out-of-the-money put.", "an in-the-money call or an out-of-the-money put.", "an out-of-the-money call or an in-the-money put."], 0, "Both are zero for out-of-the-money options at expiration."],
 ["Which of the following will increase the value of a call option?", ["A higher exercise price", "A dividend on the underlying", "Higher volatility"], 2, "Volatility increases the chance of a large payoff."],
 ["Profits from a long call are:", ["positively related to the share price, and profits from a long put negatively related.", "negatively related to the share price, and profits from a long put positively related.", "positively related to the share price, as are profits from a long put."], 0, "Calls gain when the price rises; puts gain when it falls."],
 ["A European call with 30 days to expiration is in the money. Its time value is most likely:", ["less than its premium.", "equal to its premium.", "greater than its premium."], 0, "The premium also includes positive intrinsic value."],
 ["As the share price rises above the exercise price, a call's intrinsic value:", ["rises, while a put's intrinsic value rises as the share price falls below the exercise price.", "falls, while a put's intrinsic value rises as the share price falls.", "rises, while a put's intrinsic value falls as the share price falls."], 0, "Calls gain intrinsic value as the price rises; puts as it falls."],
 ["Compared with an otherwise identical European put with less time to expiration, a longer-dated European put:", ["must be worth more.", "must be worth at least as much.", "may be worth less."], 2, "If the share price is very low, the holder would prefer to receive X sooner, so a longer European put can be worth less."],
 ["An option's intrinsic value is the amount by which it is:", ["in the money; time value is market value minus intrinsic value.", "out of the money; time value is market value minus intrinsic value.", "in the money; time value is intrinsic value minus market value."], 0, "Time value is the part of the premium above intrinsic value."],
 ["The upper bound of a European put is the:", ["exercise price.", "present value of the exercise price.", "share price."], 1, "The most a European put can pay is X at expiration, worth PV(X) today."],
])

EK["pc"] = dict(
notes="""<h3>Synthetic positions from put–call parity</h3>
<p class="f">S + p = c + PV(X)</p>
<div class="tbl"><table>
<tr><th>Position</th><th>Replicated by</th></tr>
<tr><td>Synthetic call</td><td>Long share + long put − bond paying X (borrow PV(X))</td></tr>
<tr><td>Synthetic put</td><td>Long call + bond paying X − short share</td></tr>
<tr><td>Protective put (S + p)</td><td>Long call + long bond (fiduciary call)</td></tr>
<tr><td>Risk-free bond</td><td>Long share + long put − long call</td></tr>
</table></div>
<p class="f">Put–call forward parity: c + PV(X) = p + PV(F<sub>0</sub>)</p>
<ul>
<li>Since p − c = PV(X − F<sub>0</sub>), a bond paying X − F<sub>0</sub> at expiration is replicated by <b>buying the put and writing the call</b>.</li>
<li>If a put is underpriced relative to parity, buy the put and sell the synthetic put: write the call, buy the share and borrow PV(X).</li>
</ul>""",
qs=[
 ["A synthetic European call includes a short position in:", ["the underlying share.", "a risk-free bond.", "a European put."], 1, "c = S + p − PV(X): the investor borrows the present value of the exercise price."],
 ["A European put is priced below its value under put–call parity. To exploit this, an investor would most likely:", ["sell the call.", "invest PV(X) at the risk-free rate.", "sell the share short."], 0, "Buy the put and sell the synthetic put: write the call, buy the share and borrow."],
 ["A fiduciary call consists of:", ["a call and a share.", "a call and a bond that pays the exercise price at expiration.", "a call created synthetically."], 1, "Its payoff equals that of a protective put."],
 ["A synthetic European put can be created by:", ["short share, long call, long bond paying X.", "short share, long call, short bond paying X.", "long share, short call, short bond paying X."], 0, "p = c + PV(X) − S."],
 ["A synthetic European call can be created by:", ["long share, long put, short bond paying X.", "long share, short put, short bond paying X.", "long share, long put, long bond paying X."], 0, "c = S + p − PV(X)."],
 ["Under put–call forward parity, a risk-free bond paying X − F at expiration can be replicated by:", ["buying the call and writing the put.", "writing the call and buying the put.", "writing both the call and the put."], 1, "p − c = PV(X − F), so a long put and a short call give the bond's payoff."],
 ["A synthetic European put includes a short position in:", ["the underlying share.", "a risk-free bond.", "a European call."], 0, "p = c + PV(X) − S."],
 ["Which portfolio has the same payoff as a protective put?", ["Long call and long risk-free bond", "Short call and long risk-free bond", "Long call, long bond and short share"], 0, "S + p = c + PV(X)."],
 ["Which instrument is part of the put–call forward parity relationship?", ["The spot price of the underlying", "The present value of the forward price", "The future value of the forward price"], 1, "c + PV(X) = p + PV(F₀)."],
 ["Under put–call forward parity, for an asset with no holding costs or benefits, the value of a call plus PV(X) equals:", ["the forward price plus the put value.", "the put value plus the present value of the forward price.", "the share price minus the put value."], 1, "The forward price replaces the share price, discounted to today."],
])

EK["bi"] = dict(
notes="""<h3>More on the binomial model</h3>
<ul>
<li>Inputs: current price of the underlying, its up and down moves (its volatility), the exercise price and the <b>risk-free rate</b>. Real-world probabilities and risk preferences are not needed.</li>
<li>The risk-free rate can be used because combining the option with the underlying in the right ratio creates a <b>riskless</b> portfolio.</li>
<li>Option values depend on risk-neutral (expected) probabilities, not actual ones.</li>
<li>A put priced above its model value: sell the put and buy the replicating portfolio.</li>
</ul>
<p class="f">π = (1 + R<sub>f</sub> − d) / (u − d)  ·  h = (c<sup>+</sup> − c<sup>−</sup>) / (S<sup>+</sup> − S<sup>−</sup>)</p>""",
qs=[
 ["To value an option with a one-period binomial model, an analyst needs:", ["the risk-free rate, the volatility of the underlying and its current price.", "the risk-adjusted discount rate, the volatility and the exercise price.", "the actual probability of an up move, the exercise price and the current price."], 0, "Risk-neutral pricing uses the risk-free rate and needs no real-world probabilities."],
 ["The risk-free rate can be used to value an option in a binomial model because:", ["combining the option and the underlying in the right ratio gives a riskless payoff.", "combining calls and puts gives a riskless payoff.", "option investors are risk neutral on average."], 0, "The hedged portfolio is riskless, so it must earn the risk-free rate."],
 ["A share will be worth either 36 or 20 in one year. What hedge ratio (shares per short call) makes a portfolio with a call struck at 30 riskless?", ["0.375", "0.500", "0.600"], 0, "Call payoffs are 6 and 0: h = (6 − 0)/(36 − 20) = 0.375."],
 ["A share trades at 50 and in one period will rise or fall by 20%. The risk-free rate for the period is 2%. A call with an exercise price of 52 is worth closest to:", ["3.92", "4.31", "4.40"], 1, "π = (1.02 − 0.80)/(1.20 − 0.80) = 0.55. Payoffs are 8 and 0, so c = 0.55 × 8 / 1.02 = 4.31."],
 ["One way to value a call with a one-period binomial model is to:", ["find a combination of the call and the underlying with the same value in both states.", "discount the average of the two payoffs at the risk-free rate.", "weight payoffs by actual probabilities."], 0, "The riskless hedge portfolio is valued at the risk-free rate."],
 ["An option's value depends on:", ["actual probabilities of price moves only.", "risk-neutral (expected) probabilities only.", "both actual and risk-neutral probabilities."], 1, "Real-world probabilities do not enter the pricing."],
 ["Other things equal, a fall in the risk-free rate will cause a call's no-arbitrage price to:", ["rise.", "fall.", "stay unchanged."], 1, "A lower rate raises the present value of the exercise price."],
 ["Which statement about risk-neutral pricing is most accurate?", ["It uses the expected return of the underlying.", "Its probabilities depend on investors' views on risk.", "It can be applied in models of future price moves of the underlying."], 2, "Risk-neutral probabilities come from the price moves and the risk-free rate."],
 ["A European put trades above its binomial model value. An investor can earn more than the risk-free rate by:", ["buying the put and selling the replicating portfolio.", "selling the put and buying the replicating portfolio.", "buying both the put and the underlying."], 1, "Sell what is overpriced and buy its equivalent."],
])
