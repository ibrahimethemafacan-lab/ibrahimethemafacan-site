import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- ms: Firms and Market Structures ---
_s = [.35, .25, .20, .10, .10]
EK["ms"] = G(
    [("Five firms have market shares of 35%, 25%, 20%, 10% and 10%. Compute the four-firm concentration ratio and the Herfindahl–Hirschman index. What happens to each if the two smallest firms merge?",
      f"four-firm ratio = 35 + 25 + 20 + 10 = {35+25+20+10}%|HHI = 0.35<sup>2</sup> + 0.25<sup>2</sup> + 0.20<sup>2</sup> + 0.10<sup>2</sup> + 0.10<sup>2</sup> = {sum(x*x for x in _s):.4f}|after the merger: ratio = 35 + 25 + 20 + 20 = 100%; HHI = {.35**2+.25**2+.2**2+.2**2:.4f}",
      "The HHI squares the shares, so it reacts more to mergers among large firms than the simple concentration ratio does. Neither measures barriers to entry or elasticity of demand."),
     ("A firm in perfect competition faces a price of 20. Its average variable cost is 16 and its average total cost is 23. Should it produce?",
      "", "In the short run, yes: price covers variable cost and contributes 4 per unit toward fixed costs. In the long run, no: price is below average total cost, so the firm exits unless conditions improve.")],
    (["Structure", "Firms", "Product", "Pricing power"], [
        ["Perfect competition", "Many", "Identical", "None: price taker"],
        ["Monopolistic competition", "Many", "Differentiated", "Some; zero economic profit in the long run"],
        ["Oligopoly", "Few", "Similar or differentiated", "Considerable; firms are interdependent"],
        ["Monopoly", "One", "Unique, no close substitutes", "Greatest; often regulated"]]),
    "Expect a description of an industry and \"this market is best described as\", plus the shutdown and breakeven rules. Every firm maximizes profit where marginal revenue equals marginal cost; only under perfect competition does that also mean price equals marginal cost. Oligopoly models (kinked demand, Cournot, Nash equilibrium, dominant firm) are tested by recognition.")

# --- bc: Business Cycles ---
EK["bc"] = G(
    [("An analyst observes rising building permits and a rising stock index, flat industrial production, and a still-rising average duration of unemployment. What does the mix suggest?",
      "", "Building permits and stock prices are leading indicators; industrial production is coincident; the duration of unemployment is lagging. Leading indicators turning up while lagging ones still worsen is the typical picture of an economy near a trough, about to enter recovery.")],
    (["Type", "Examples"], [
        ["Leading", "Stock prices, building permits, new orders, yield curve slope, consumer expectations, initial unemployment claims"],
        ["Coincident", "Industrial production, non-farm payrolls, real personal income, manufacturing and trade sales"],
        ["Lagging", "Average duration of unemployment, inventory–sales ratio, unit labor costs, prime rate, consumer credit to income, change in services CPI"]]),
    "Questions ask you to classify an indicator or to identify the phase from a description. Recovery: output below potential but rising. Expansion: above-trend growth, falling unemployment. Slowdown: growth above zero but decelerating, inflation picking up. Contraction: falling output, rising unemployment. Credit cycles are longer than business cycles and amplify them.")

# --- fp: Fiscal Policy ---
EK["fp"] = G(
    [("The marginal propensity to consume is 0.8 and the tax rate is 25%. What is the fiscal multiplier, and what is the effect of a 100 increase in government spending?",
      f"multiplier = 1 / [1 − MPC × (1 − t)] = 1 / (1 − 0.8 × 0.75) = {1/(1-.8*.75):.1f}|change in output = 100 × 2.5 = {100/(1-.8*.75):.0f}",
      "A higher tax rate or a lower propensity to consume makes the multiplier smaller. A tax cut of the same size has a smaller effect than spending, because part of it is saved.")],
    (["Pair", "Difference"], [
        ["Automatic stabilizers vs discretionary policy", "Taxes and transfers that respond to the cycle by themselves vs deliberate changes in spending or tax law"],
        ["Recognition, action, impact lags", "Time to see the problem, to legislate, and for the measure to affect the economy"],
        ["Crowding out", "Government borrowing raises interest rates and reduces private investment"],
        ["Ricardian equivalence", "Households save a tax cut in anticipation of higher future taxes, so demand does not rise"],
        ["Direct vs indirect taxes", "On income and wealth vs on spending; indirect taxes can be changed and take effect quickly"]]),
    "Know which tools are expansionary (more spending, lower taxes, a larger deficit) and the arguments about why fiscal policy may not work as intended: lags, crowding out, and limited room when debt is already high. The balanced-budget multiplier is positive: equal rises in spending and taxes still raise output.")

# --- mp: Monetary Policy ---
EK["mp"] = G(
    [("The required reserve ratio is 10%. What is the money multiplier? A central bank estimates trend real growth of 2% and targets inflation of 2%; its policy rate is 2.5%. Is policy expansionary or contractionary?",
      f"money multiplier = 1 / 0.10 = {1/.1:.0f}|neutral rate = trend real growth + inflation target = 2% + 2% = 4%|policy rate of 2.5% is below neutral: expansionary", "")],
    (["Fiscal", "Monetary", "Likely result"], [
        ["Easy", "Easy", "Strong demand; public and private sectors both grow; inflation risk"],
        ["Easy", "Tight", "Higher interest rates; the public sector's share of output rises"],
        ["Tight", "Easy", "Lower interest rates; the private sector's share rises"],
        ["Tight", "Tight", "Weaker demand; both sectors shrink"]]),
    "Typical items: the three tools (policy rate, reserve requirements, open market operations), the three qualities of an effective central bank (independence, credibility, transparency), and the limits of policy. A liquidity trap, where demand for money is unlimited at very low rates, and bond markets that distrust the bank both weaken transmission. Quantitative easing buys assets to lower long-term rates when the policy rate is near zero.")

# --- gp: Geopolitics ---
EK["gp"] = G(
    [("Country A is highly integrated into world trade and works through international institutions and common rules. Country B is equally open to trade but uses its dominant position to set terms for others. Country C restricts trade and capital and aims at self-sufficiency. Classify them.",
      "", "A is multilateralism (cooperative and globalized). B is hegemony (non-cooperative and globalized). C is autarky (non-cooperative and nationalist). The fourth type, bilateralism, is cooperation between two countries or regions without broad openness.")],
    (["Risk type", "Nature", "Example"], [
        ["Event risk", "Tied to a known date", "Elections, referendums, scheduled summits"],
        ["Exogenous risk", "Sudden and unexpected", "Uprisings, invasions, natural disasters"],
        ["Thematic risk", "Known and evolving over a long period", "Climate change, cyber threats, migration"]]),
    "Expect a scenario and a classification. Tools of geopolitics come in three groups: national security (alliances, armed conflict), economic (trade agreements, tariffs, nationalization) and financial (sanctions, capital controls, currency arrangements). When judging a risk for a portfolio, weigh its likelihood, its velocity (how fast it hits markets) and the size and nature of its impact.")

# --- it: International Trade ---
EK["it"] = G(
    [("With one day of labor, country A can make 10 units of cloth or 5 of wine. Country B can make 4 of cloth or 4 of wine. Who should produce what?",
      f"opportunity cost of 1 wine: A gives up 10/5 = {10/5:.0f} cloth; B gives up 4/4 = {4/4:.0f} cloth|opportunity cost of 1 cloth: A gives up {5/10:.1f} wine; B gives up {4/4:.0f} wine",
      "A has an absolute advantage in both goods, but B has the lower opportunity cost in wine and A in cloth. A exports cloth and B exports wine; both gain at any price between 1 and 2 cloth per wine.")],
    (["Arrangement", "Adds"], [
        ["Free trade area", "No barriers among members; each keeps its own external tariffs"],
        ["Customs union", "A common external tariff"],
        ["Common market", "Free movement of labor and capital"],
        ["Economic union", "Common institutions and coordinated economic policy"],
        ["Monetary union", "A single currency"]]),
    "Comparative advantage is about opportunity cost, not about who is more productive. For trade restrictions, know who gains: with a tariff the government collects revenue; with a quota the rent goes to whoever holds the licences; with a voluntary export restraint it goes to the foreign exporters. All of them raise the domestic price, help domestic producers and hurt consumers.")

# --- fx: Capital Flows and the FX Market ---
EK["fx"] = G(
    [("The USD/EUR rate moves from 1.1000 to 1.1550. By how much did the euro appreciate, and the dollar depreciate?",
      f"euro (base currency): 1.1550 / 1.1000 − 1 = +{(1.155/1.1-1)*100:.2f}%|dollar: 1.1000 / 1.1550 − 1 = {(1.1/1.155-1)*100:.2f}%",
      "The two percentages are not equal and opposite. In a quote of A/B, the rate is the price of one unit of B, the base currency, in units of A.")],
    (["Regime", "Feature"], [
        ["Dollarization / monetary union", "No own currency; no independent monetary policy"],
        ["Currency board", "Domestic currency fully backed by foreign reserves at a fixed rate"],
        ["Fixed peg / target zone", "Rate held within a narrow band; reserves are used to defend it"],
        ["Crawling peg", "Peg adjusted periodically, often for inflation"],
        ["Managed float", "Market-determined, with intervention at the authorities' discretion"],
        ["Independent float", "Market-determined; monetary policy is free to target domestic goals"]]),
    "Quotation mechanics catch many candidates: always identify the base currency first. Other common items: the real exchange rate adjusts the nominal rate for relative price levels; a country with a trade deficit must have a matching capital inflow; and capital controls are used to protect a fixed rate or to keep monetary policy independent.")

# --- ec: Exchange Rate Calculations ---
_f = 1.10 * 1.05 / 1.03
EK["ec"] = G(
    [("USD/EUR is 1.1000 and JPY/USD is 150.00. What is the JPY/EUR cross rate?",
      f"JPY/EUR = JPY/USD × USD/EUR = 150.00 × 1.1000 = {150*1.1:.2f}", ""),
     ("Spot USD/EUR is 1.1000. One-year interest rates are 5% in dollars and 3% in euros. What is the one-year forward rate, and how is it quoted in points?",
      f"F = S × (1 + r<sub>USD</sub>) / (1 + r<sub>EUR</sub>) = 1.1000 × 1.05 / 1.03 = {_f:.4f}|forward points = ({_f:.4f} − 1.1000) × 10,000 = {(_f-1.1)*10000:.0f}",
      "The price currency's rate goes in the numerator. The euro, with the lower interest rate, trades at a forward premium of about 1.9%, which offsets the interest difference.")],
    (["Pair", "Difference"], [
        ["Forward premium vs discount", "The currency with the lower interest rate trades at a forward premium; the higher-rate currency at a discount"],
        ["Forward rate vs forecast", "The forward comes from interest rates by arbitrage; it is not a prediction of the future spot rate"],
        ["Forward points", "Forward minus spot, scaled by 10,000 for most pairs (100 for yen quotes)"],
        ["Cross rate", "Multiply two quotes so that the common currency cancels; invert one first if needed"]]),
    "Cross rates and the covered interest parity forward are standard calculations. Write the currencies as fractions and check that the units cancel. If a quoted forward differs from the parity value, an arbitrage exists: borrow the currency that is cheap to borrow, convert at spot, lend, and sell the proceeds forward.")
