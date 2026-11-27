import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- r1: Portfolio Risk and Return I ---
_var = .6**2*.2**2 + .4**2*.1**2 + 2*.6*.4*.25*.2*.1
EK["r1"] = G(
    [("A portfolio holds 60% in asset A (standard deviation 20%) and 40% in asset B (standard deviation 10%). The correlation is 0.25. What is the portfolio's standard deviation?",
      f"variance = 0.6<sup>2</sup> × 0.20<sup>2</sup> + 0.4<sup>2</sup> × 0.10<sup>2</sup> + 2 × 0.6 × 0.4 × 0.25 × 0.20 × 0.10|= {.36*.04:.4f} + {.16*.01:.4f} + {2*.6*.4*.25*.2*.1:.4f} = {_var:.4f}|standard deviation = {_var**.5*100:.2f}%",
      f"The weighted average of the two standard deviations is {.6*20+.4*10:.0f}%. The portfolio's risk is lower because the correlation is below 1."),
     ("An investor with risk aversion A = 4 considers a portfolio with an expected return of 10% and a standard deviation of 20%. What is its utility?",
      f"U = E(r) − ½ × A × σ<sup>2</sup> = 0.10 − 0.5 × 4 × 0.20<sup>2</sup> = {.10-.5*4*.04:.2f}",
      "Use decimals. A risk-free asset yielding more than 2% would give this investor higher utility.")],
    (["Term", "Meaning"], [
        ["Minimum-variance frontier", "All portfolios with the lowest risk for each level of return"],
        ["Efficient frontier", "Only the upper part of that curve, above the global minimum-variance portfolio"],
        ["Capital allocation line", "Combinations of the risk-free asset and one risky portfolio; a straight line"],
        ["Optimal risky portfolio", "Where the capital allocation line is tangent to the efficient frontier; the same for all investors"],
        ["Optimal investor portfolio", "Where the investor's highest indifference curve touches the line; depends on risk aversion"]]),
    "The two-asset standard deviation is the calculation to master; do not forget the 2 in the covariance term or to take the square root. Conceptually: correlation of +1 gives no diversification benefit, lower correlation gives more, and risk aversion changes where an investor sits on the line, not which risky portfolio is best.")

# --- r2: Portfolio Risk and Return II ---
EK["r2"] = G(
    [("The risk-free rate is 3% and the market risk premium is 6%. A stock has a beta of 1.2 and analysts forecast a return of 12%. Is it overvalued or undervalued?",
      f"required return = 3% + 1.2 × 6% = {3+1.2*6:.1f}%|forecast − required = 12.0% − 10.2% = +{12-10.2:.1f}%",
      "The stock plots above the security market line: it is undervalued, with a positive alpha of 1.8%."),
     ("A stock's correlation with the market is 0.6. Its standard deviation is 30% and the market's is 20%. What is its beta?",
      f"β = ρ × σ<sub>i</sub> / σ<sub>m</sub> = 0.6 × 30 / 20 = {.6*30/20:.1f}", "")],
    (["Measure", "Risk used", "Formula idea"], [
        ["Sharpe ratio", "Total risk (standard deviation)", "Excess return per unit of total risk"],
        ["M-squared", "Total risk", "Sharpe ratio restated as a return, by scaling the portfolio to the market's risk"],
        ["Treynor ratio", "Systematic risk (beta)", "Excess return per unit of beta"],
        ["Jensen's alpha", "Systematic risk (beta)", "Return above what the CAPM requires"]]),
    "Know the difference between the two lines: the capital market line uses total risk and holds only efficient portfolios; the security market line uses beta and prices every asset. Only systematic risk is rewarded, because unsystematic risk can be diversified away. Use Sharpe or M-squared for an investor's whole portfolio, Treynor or alpha for a part of a diversified one.")

# --- ov: Portfolio Management Overview ---
EK["ov"] = G(
    [("Two stocks each have a standard deviation of 30% and their returns are uncorrelated. What is the standard deviation of an equally weighted portfolio of the two?",
      f"variance = 0.5<sup>2</sup> × 0.30<sup>2</sup> + 0.5<sup>2</sup> × 0.30<sup>2</sup> = {2*.25*.09:.3f}|standard deviation = {(2*.25*.09)**.5*100:.1f}%",
      "Same expected return, clearly lower risk. This is the portfolio approach: judge each holding by what it adds to the whole.")],
    (["Pair", "Difference"], [
        ["Defined benefit vs defined contribution plan", "The employer promises a pension and bears investment risk vs the employee bears it"],
        ["Open-end vs closed-end fund", "Shares created and redeemed at net asset value vs a fixed number of shares that trade at a premium or discount"],
        ["Mutual fund vs ETF", "Trades once a day with the fund vs trades all day on an exchange, usually close to net asset value"],
        ["Planning, execution, feedback", "Write the IPS; allocate and select securities; monitor, rebalance and measure performance"],
        ["Endowment vs bank vs insurer", "Long horizon and high risk tolerance vs short horizon, high liquidity need and low risk tolerance"]]),
    "Questions ask which investor type has the longest horizon, the highest liquidity need or the lowest risk tolerance. Banks and non-life insurers need liquidity and safety; endowments and DB pension plans can take long-term risk. Step questions ask in which phase an activity belongs: asset allocation is execution, rebalancing is feedback.")

# --- pl: Planning and Construction ---
EK["pl"] = G(
    [("A policy portfolio sets equities at 60% with a rebalancing corridor of ±5%. After a rally the portfolio is worth 1,100, of which equities are 726. Must it be rebalanced, and how much equity is sold to return to target?",
      f"equity weight = 726 / 1,100 = {726/1100*100:.0f}% (outside 55%–65%): rebalance|target equity = 60% × 1,100 = {.6*1100:.0f}|sell 726 − 660 = {726-660}",
      "Corridors limit transaction costs: nothing is done while the weight stays inside the band.")],
    (["Pair", "Difference"], [
        ["Ability vs willingness to take risk", "Ability is objective: horizon, wealth, liquidity needs. Willingness is attitude. When they conflict, use the lower, and educate the client"],
        ["Strategic vs tactical asset allocation", "Long-term policy weights from the IPS vs deliberate short-term deviations to exploit perceived opportunities"],
        ["Tactical allocation vs security selection", "Changing asset-class weights vs choosing securities within an asset class"],
        ["Objectives vs constraints in the IPS", "Return and risk vs time horizon, taxes, liquidity, legal and regulatory, unique circumstances"],
        ["Negative screening vs best-in-class vs impact", "Excluding sectors vs picking ESG leaders in each sector vs seeking a measurable social or environmental result"]]),
    "A short client description followed by \"the client's risk tolerance is\" or \"this is which IPS constraint\" is the typical format. Liquidity is a constraint, not an objective. The IPS should be reviewed regularly and whenever the client's circumstances change materially, not when markets move.")

# --- bb: Behavioral Biases ---
EK["bb"] = G(
    [("An investor bought a stock at 80. It now trades at 50 and the company's prospects have deteriorated, but she refuses to sell \"until it gets back to 80\". She readily sells her winners. Which biases are at work?",
      "",
      "Holding losers and selling winners is the disposition effect, driven by loss aversion, an emotional bias. Fixing on the purchase price of 80 is anchoring, a cognitive error. The purchase price is irrelevant; only the stock's prospects from today matter.")],
    (["Often confused", "How to tell them apart"], [
        ["Conservatism vs anchoring", "Conservatism: slow to update a prior view after new information. Anchoring: stuck on a specific number"],
        ["Confirmation vs hindsight", "Confirmation: seeking evidence that supports a belief. Hindsight: believing afterwards that the outcome was predictable"],
        ["Representativeness vs availability", "Classifying by stereotype or a small sample vs judging by what comes most easily to mind"],
        ["Status quo vs endowment", "Preferring to do nothing vs valuing something more simply because you own it"],
        ["Loss aversion vs regret aversion", "Feeling losses more than equal gains vs avoiding decisions for fear of being wrong"],
        ["Cognitive error vs emotional bias", "Faulty reasoning, which can be corrected with information vs feeling, which usually has to be accommodated"]]),
    "Every question is a short story and \"this behavior is most likely\". Identify first whether the cause is reasoning or feeling. Cognitive errors split into belief perseverance (conservatism, confirmation, representativeness, illusion of control, hindsight) and processing errors (anchoring, mental accounting, framing, availability). Overconfidence leads to excessive trading and under-diversification.")

# --- rm: Risk Management ---
EK["rm"] = G(
    [("A bond portfolio worth 10 million has a modified duration of 5. A risk manager stresses it with a 1% rise in yields. Separately, the portfolio's 5% one-day VaR is 150,000. Interpret both numbers.",
      f"stress loss ≈ 5 × 1% × 10,000,000 = {n(5*.01*10_000_000,0)}",
      "The stress test says what is lost in one defined scenario, with no probability attached. The VaR says there is a 5% chance of losing at least 150,000 in a day; it says nothing about how large the loss can be beyond that.")],
    (["Pair", "Difference"], [
        ["Risk tolerance vs risk budgeting", "How much risk the organization accepts overall vs how that risk is allocated across units or strategies"],
        ["VaR vs CVaR (expected shortfall)", "The minimum loss in the worst x% of cases vs the average loss in those cases"],
        ["Stress test vs scenario analysis", "A shock to one or a few variables vs a complete, coherent set of changes"],
        ["Risk transfer vs risk shifting", "Paying an insurer to take the risk vs using derivatives to change the distribution of outcomes"],
        ["Financial vs non-financial risk", "Market, credit, liquidity vs operational, legal, model, solvency, regulatory"]]),
    "Risk management is not about minimising risk but about taking the risks the organization intends to take, in the amount it intends. Questions ask you to classify a risk or a response: avoid, accept (self-insure), transfer or shift. The VaR interpretation item appears often; \"at least\", not \"at most\", is the correct wording.")
