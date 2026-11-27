import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- df: Derivative Instrument and Market Features ---
EK["df"] = G(
    [("A trader is long one futures contract. Initial margin is 5,000 and maintenance margin is 4,000. The position loses 1,200 in a day. Is there a margin call, and for how much?",
      f"balance = 5,000 − 1,200 = {n(5000-1200,0)}|{n(3800,0)} is below the maintenance margin of 4,000: margin call|deposit required = 5,000 − 3,800 = {n(1200,0)}",
      "The account must be brought back to the initial margin, not just to the maintenance level.")],
    (["Feature", "Exchange-traded", "Over the counter"], [
        ["Terms", "Standardized", "Customized"],
        ["Counterparty", "Clearinghouse stands between the parties", "The other party, unless centrally cleared"],
        ["Credit risk", "Very low: daily margining", "Higher: depends on collateral agreements"],
        ["Liquidity and transparency", "High", "Lower"],
        ["Typical instruments", "Futures, listed options", "Forwards, swaps, OTC options"]]),
    "Questions describe a contract and ask whether it is exchange-traded or OTC, or what central clearing changes: it replaces bilateral counterparty risk with exposure to the central counterparty, but it does not remove market risk. The margin-call calculation above is the classic numerical item.")

# --- fc: Forward Commitments and Contingent Claims ---
EK["fc"] = G(
    [("A call has an exercise price of 50 and cost 4. A put has an exercise price of 50 and cost 3. At expiration the underlying is 58 in one scenario and 44 in another. What are the buyer's payoffs and profits?",
      f"call at 58: payoff = 58 − 50 = {58-50}; profit = 8 − 4 = {8-4}|call at 44: payoff = 0; profit = −4|put at 44: payoff = 50 − 44 = {50-44}; profit = 6 − 3 = {6-3}|put at 58: payoff = 0; profit = −3|break-even: call 50 + 4 = 54; put 50 − 3 = 47",
      "The seller's profit is the mirror image. The buyer's loss is limited to the premium.")],
    (["Pair", "Difference"], [
        ["Forward commitment vs contingent claim", "Both parties are obliged (forward, futures, swap) vs one party has a right and pays a premium for it (option)"],
        ["Payoff vs profit", "Payoff ignores the premium; profit subtracts it"],
        ["Long call vs short put", "Both gain when prices rise, but the long call has a right and the short put has an obligation with limited gain"],
        ["Forward vs futures", "Private, customized, settled at the end vs standardized, cleared, marked to market daily"],
        ["CDS buyer vs seller", "The buyer pays a periodic premium for protection; the seller is long the credit risk"]]),
    "Expect a payoff or profit at a given price, a break-even price, or a maximum loss. Maximum loss for a call seller is unlimited; for a put seller it is the exercise price minus the premium. Read carefully whether the question asks for payoff or profit, and for the buyer or the seller.")

# --- du: Benefits, Risks, Uses ---
EK["du"] = G(
    [("A futures contract has a notional value of 100,000 and requires margin of 5,000. The futures price falls by 2%. What is the loss as a percentage of the margin posted?",
      f"leverage = 100,000 / 5,000 = {100000/5000:.0f}×|loss = 2% × 100,000 = {n(2000,0)}|loss on margin = 2,000 / 5,000 = {2000/5000*100:.0f}%",
      "Small cash outlay, large exposure: this implicit leverage is both the main benefit and the main risk of derivatives.")],
    (["Hedge accounting type", "What is hedged", "Example"], [
        ["Cash flow hedge", "Variability of a future cash flow", "Swapping floating-rate debt to fixed; hedging a forecast purchase with futures"],
        ["Fair value hedge", "Change in the value of an existing asset or liability", "Swapping fixed-rate debt to floating; hedging inventory"],
        ["Net investment hedge", "Currency exposure of a foreign subsidiary", "Selling the subsidiary's currency forward"]]),
    "Questions name a company's exposure and ask for the hedge type, or list a risk and ask which it is. Basis risk is the mismatch between the hedge and the exposure; counterparty risk belongs mainly to OTC contracts; liquidity risk arises from margin calls. Benefits to remember: price discovery, risk transfer, lower transaction costs, operational efficiency.")

# --- ar: Arbitrage, Replication, Cost of Carry ---
EK["ar"] = G(
    [("A stock trades at 100, the risk-free rate is 5% and the forward expires in one year. What is the forward price with no dividends, and with a dividend whose present value is 2?",
      f"no income: F<sub>0</sub> = 100 × 1.05 = {100*1.05:.2f}|with income: F<sub>0</sub> = (100 − 2) × 1.05 = {(100-2)*1.05:.2f}", ""),
     ("With no dividends, a dealer quotes the forward at 107. What is the arbitrage?",
      f"borrow 100 at 5%, buy the stock, sell forward at 107|at expiration: deliver the stock for 107, repay {100*1.05:.0f}|riskless profit = 107 − 105 = {107-105}",
      "The forward is too expensive, so sell it and carry the asset: cash-and-carry arbitrage.")],
    (["Item", "Effect on forward price", "Examples"], [
        ["Costs of carry", "Raise it", "Financing, storage, insurance"],
        ["Benefits of carry", "Lower it", "Dividends, coupons, foreign interest"],
        ["Convenience yield", "Lowers it", "Non-cash benefit of holding a physical commodity that is in short supply"]]),
    "Besides computing a forward price, expect \"which strategy earns the arbitrage profit\". Forward too high: buy spot, sell forward. Forward too low: short spot, lend the proceeds, buy forward. Replication questions use the same logic: asset plus short forward equals a risk-free bond.")

# --- fw: Forwards ---
_v = 108 - 105 / 1.05 ** .5
EK["fw"] = G(
    [("An investor went long a one-year forward at 105. Six months later the underlying trades at 108 and the risk-free rate is 5%. The asset pays no income. What is the value of the long position?",
      f"V<sub>t</sub> = S<sub>t</sub> − F<sub>0</sub> / (1 + r)<sup>T−t</sup> = 108 − 105 / 1.05<sup>0.5</sup>|= 108 − {105/1.05**.5:.2f} = {_v:.2f}",
      "The short position is worth the negative of this. At expiration the value is simply S<sub>T</sub> − F<sub>0</sub>.")],
    (["Pair", "Difference"], [
        ["Forward price vs forward value", "The price is fixed at initiation and written in the contract; the value changes as the spot price and time change"],
        ["Value at initiation", "Zero for both parties: no money changes hands"],
        ["Long vs short", "The long gains when the spot price rises above the present value of the forward price"],
        ["FRA long vs short", "The long (fixed-rate payer) gains when the reference rate ends above the FRA rate"]]),
    "The value-during-life formula is the most tested item: spot minus the present value of the forward price. A forward rate agreement is a forward on an interest rate; its fixed rate is the implied forward rate from the spot curve, so borrowers use a long FRA to lock in a borrowing cost.")

# --- fu: Futures ---
EK["fu"] = G(
    [("A trader is long one gold futures contract of 100 ounces at 2,000. The settlement price is 2,010 on day 1 and 1,995 on day 2. What are the daily gains and losses?",
      f"day 1: (2,010 − 2,000) × 100 = +{n(1000,0)}|day 2: (1,995 − 2,010) × 100 = {n(-1500,0)}|cumulative: {n(-500,0)}",
      "Gains and losses are settled in cash every day, so the value of a futures contract is reset to zero after each settlement.")],
    (["Correlation of futures prices with interest rates", "Result"], [
        ["Positive", "Futures price above forward price: gains are reinvested when rates are high"],
        ["Negative", "Futures price below forward price"],
        ["Zero, or constant interest rates", "Futures and forward prices are equal"]]),
    "Expect the mark-to-market calculation and the forward-versus-futures price comparison in the table. Interest rate futures are quoted as 100 minus the yield, so their price moves one for one with the rate, while a bond's price is convex; this difference is the convexity bias and matters for long-dated contracts.")

# --- sw: Swaps ---
_d1 = 1 / 1.03; _d2 = 1 / 1.04 ** 2; _s = (1 - _d2) / (_d1 + _d2)
EK["sw"] = G(
    [("The one-year spot rate is 3% and the two-year spot rate is 4%. What is the fixed rate on a two-year annual-pay interest rate swap?",
      f"discount factors: 1/1.03 = {_d1:.4f}; 1/1.04<sup>2</sup> = {_d2:.4f}|swap rate = (1 − final discount factor) / sum of discount factors|= (1 − {_d2:.4f}) / ({_d1:.4f} + {_d2:.4f}) = {_s*100:.2f}%",
      "The swap rate is the par rate: it makes the present value of the fixed payments equal to that of the expected floating payments, so the swap is worth zero at initiation.")],
    (["Pair", "Difference"], [
        ["Swap price vs swap value", "The price is the fixed rate set at initiation; the value starts at zero and changes as rates move"],
        ["Pay-fixed vs receive-fixed", "The fixed payer gains when rates rise; the fixed receiver gains when rates fall"],
        ["Swap vs series of forwards", "A swap equals a series of forward rate agreements at one common fixed rate, so the individual forwards are off-market"],
        ["Notional vs payments", "Notional is not exchanged in an interest rate swap; only the net interest difference is paid"]]),
    "Questions ask who gains after a rate move, or ask you to recognise the swap as a portfolio of FRAs. A pay-fixed swap is like being long a floating-rate bond and short a fixed-rate bond; that framing answers most valuation questions without a formula.")

# --- op: Options ---
_lb = 54 - 50 / 1.04
EK["op"] = G(
    [("A one-year European call with an exercise price of 50 trades at 6.50 when the underlying is 54. The risk-free rate is 4%. What are the exercise value, the time value and the lower bound of the call?",
      f"exercise value = max(0, 54 − 50) = {54-50}|time value = 6.50 − 4.00 = {6.5-4:.2f}|lower bound = max(0, S − X/(1 + r)<sup>T</sup>) = 54 − {50/1.04:.2f} = {_lb:.2f}",
      "The premium of 6.50 is above the lower bound of 5.92, as it must be.")],
    (["An increase in", "Call value", "Put value"], [
        ["Underlying price", "Rises", "Falls"],
        ["Exercise price", "Falls", "Rises"],
        ["Risk-free rate", "Rises", "Falls"],
        ["Volatility", "Rises", "Rises"],
        ["Time to expiration", "Rises", "Usually rises (a deep in-the-money European put can fall)"],
        ["Income on the underlying", "Falls", "Rises"]]),
    "The factor table is tested directly: \"which change raises the value of a put\". Also know moneyness for both option types, that time value is highest at the money and falls to zero at expiration, and that an option's value can never be below its exercise value for American options or its lower bound for European ones.")

# --- pc: Put–Call Parity ---
_pv = 50 / 1.04
EK["pc"] = G(
    [("A one-year European call with an exercise price of 50 costs 6. The underlying trades at 52 and the risk-free rate is 4%. What should the put with the same terms cost?",
      f"S + p = c + X/(1 + r)<sup>T</sup>|p = 6 + {_pv:.2f} − 52 = {6+_pv-52:.2f}",
      "If the put traded at a different price, buying the cheap side and selling the expensive side would lock in a riskless profit.")],
    (["Position", "Built from", "Equivalent to"], [
        ["Protective put", "Long stock + long put", "Fiduciary call"],
        ["Fiduciary call", "Long call + risk-free bond paying X", "Protective put"],
        ["Synthetic long stock", "Long call + short put + bond", "Stock"],
        ["Synthetic long call", "Long stock + long put − bond", "Call"],
        ["Covered call", "Long stock + short call", "Risk-free bond + short put"]]),
    "Rearranging the parity equation to build a synthetic position is the standard item: move a term across the equals sign and its sign flips from long to short. In put–call forward parity, replace the stock with the present value of the forward price. The same logic values a firm: equity is a call on the firm's assets, and risky debt is a risk-free bond minus a put.")

# --- bi: Binomial ---
_pi = (1.05 - .8) / (1.2 - .8); _c = (_pi * 20) / 1.05
EK["bi"] = G(
    [("A stock at 100 will be 120 or 80 in one year. The risk-free rate is 5%. Value a one-year call with an exercise price of 100, and find the hedge ratio.",
      f"risk-neutral probability of an up move = (1 + r − d) / (u − d) = (1.05 − 0.80) / (1.20 − 0.80) = {_pi:.3f}|call payoffs: 20 (up), 0 (down)|c = ({_pi:.3f} × 20 + {1-_pi:.3f} × 0) / 1.05 = {_c:.2f}|hedge ratio = (20 − 0) / (120 − 80) = {20/40:.2f}",
      "Holding 0.5 share for each call sold gives the same value in both states, so the hedged portfolio must earn the risk-free rate.")],
    (["Pair", "Difference"], [
        ["Risk-neutral vs actual probability", "Risk-neutral probabilities come from u, d and the risk-free rate. The real-world probability of an up move is not needed"],
        ["Expected return of the stock", "Does not enter the option price: the option is priced by replication, not by forecasting"],
        ["Hedge ratio", "Shares per option that make the portfolio riskless; equals the option's delta in this model"],
        ["Higher volatility", "A wider gap between u and d, which raises both call and put values"]]),
    "You will be asked for the risk-neutral probability, the option value or the hedge ratio. The conceptual trap is the actual probability: a question may give it to mislead you. Discount the risk-neutral expected payoff at the risk-free rate, never at the stock's expected return.")
