import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

def _irr(cfs):
    lo, hi = 0.0, 1.0
    for _ in range(80):
        m = (lo + hi) / 2
        if sum(c / (1 + m) ** t for t, c in enumerate(cfs)) > 0: lo = m
        else: hi = m
    return m

# --- of: Organizational Forms ---
EK["of"] = G(
    [("A corporation earns pretax profit of 100 and pays corporate tax of 25%. It distributes all after-tax profit, and the shareholder pays 20% tax on dividends. What is the total effective tax rate?",
      f"after corporate tax = 100 × (1 − 25%) = {100*.75:.0f}|after personal tax = 75 × (1 − 20%) = {75*.8:.0f}|effective rate = 1 − 60 / 100 = {(1-.6)*100:.0f}%",
      "This is the double taxation of corporate profit. In a partnership the profit would be taxed once, at the owners' personal rate.")],
    (["Form", "Owner liability", "Taxation", "Access to capital"], [
        ["Sole proprietorship", "Unlimited", "Owner's personal income", "Limited to the owner"],
        ["General partnership", "Unlimited, shared", "Partners' personal income", "Limited to the partners"],
        ["Limited partnership", "GP unlimited; LPs limited to their investment", "Partners' personal income", "Wider, through LPs"],
        ["Corporation", "Limited for all owners", "Corporate tax, then tax on dividends", "Widest: equity and debt markets"]]),
    "Questions describe a business and ask for its form, or ask which form has a given feature. Know also the public–private contrast: public companies have liquid, exchange-traded shares and heavy disclosure; private ones have negotiated share transfers, fewer disclosure duties and a longer-term focus. A company goes public by IPO, direct listing or acquisition by a listed shell.")

# --- st: Investors and Other Stakeholders ---
EK["st"] = G(
    [("A company near default can invest in a safe project or in a risky one with a small chance of a very large payoff. Which do shareholders prefer, and which do bondholders prefer?",
      "", "Shareholders prefer the risky project: their loss is limited to what little equity remains, while the upside is theirs. Bondholders prefer the safe one: their best case is being repaid in full, so extra risk only lowers the chance of repayment. This conflict is why debt contracts carry covenants.")],
    (["Feature", "Debt holders", "Equity holders"], [
        ["Claim", "Contractual interest and principal", "Residual: what is left after all other claims"],
        ["Upside", "Limited to promised payments", "Unlimited"],
        ["Priority in distress", "Paid first", "Paid last"],
        ["Control", "None, except through covenants", "Voting rights"],
        ["Preference on risk and leverage", "Less", "More, up to a point"]]),
    "Stakeholder questions ask whose interests a decision favors. Shareholder theory puts shareholders first; stakeholder theory weighs customers, employees, suppliers, creditors, government and society too. ESG items ask you to sort a factor into environmental (emissions, stranded assets), social (labor practices, data privacy) or governance (board independence, pay).")

# --- cg: Corporate Governance ---
EK["cg"] = G(
    [("A shareholder owns 100 shares in a company electing three directors. How many votes can she give to one candidate under straight voting and under cumulative voting?",
      f"straight voting: 100 votes for each seat, at most 100 for any one candidate|cumulative voting: 100 × 3 = {100*3} votes, all of which may go to one candidate",
      "Cumulative voting helps minority shareholders win at least one seat.")],
    (["Board committee", "Main task"], [
        ["Audit", "Oversees financial reporting, internal control and the external auditor"],
        ["Nominating / governance", "Selects director candidates and sets governance policy"],
        ["Compensation / remuneration", "Sets executive pay and links it to performance"],
        ["Risk", "Oversees the firm's risk appetite and risk management"]]),
    "Most items are principal–agent problems: managers may prefer size, perquisites or low risk over shareholder value. Identify the mechanism that addresses each: independent directors, pay tied to long-term performance, shareholder votes, activist investors, the takeover market. Dual-class shares and staggered boards weaken shareholder control; weak governance raises the cost of capital.")

# --- wc: Working Capital and Liquidity ---
_ear = (1 + 2 / 98) ** (365 / 20) - 1
EK["wc"] = G(
    [("A supplier offers terms of 2/10 net 30. What is the effective annual cost of not taking the discount and paying on day 30?",
      f"cost = (1 + 2/98)<sup>365/20</sup> − 1 = {_ear*100:.1f}%",
      "Giving up a 2% discount to borrow for 20 extra days is very expensive. Unless the firm's borrowing cost is higher than this, it should take the discount."),
     ("Days of inventory are 50, days of receivables 40 and days of payables 35. What is the cash conversion cycle?",
      f"50 + 40 − 35 = {50+40-35} days", "")],
    (["Pair", "Difference"], [
        ["Primary vs secondary sources of liquidity", "Cash, short-term funds and cash flow management vs asset sales, renegotiating debt, bankruptcy filing; secondary sources signal distress"],
        ["Drag vs pull on liquidity", "Cash comes in too slowly (slow receivables, obsolete inventory) vs cash goes out too fast (early payments, reduced credit lines)"],
        ["Conservative vs aggressive working capital", "More current assets financed with long-term funds: safer, lower return vs lean current assets financed short term: riskier, higher return"]]),
    "The cost of trade credit and the cash conversion cycle are the calculations. Conceptual questions ask you to label an event as a drag or a pull, or a source as primary or secondary. A longer cash conversion cycle means more financing is needed; it can be shortened by collecting faster, holding less inventory or paying suppliers later.")

# --- ci: Capital Investments ---
_cf = [-1000, 450, 450, 450]; _npv = sum(c / 1.10 ** t for t, c in enumerate(_cf))
EK["ci"] = G(
    [("A project costs 1,000 today and returns 450 at the end of each of the next three years. The required return is 10%. Compute the NPV and the IRR.",
      f"NPV = −1,000 + 450/1.10 + 450/1.10<sup>2</sup> + 450/1.10<sup>3</sup> = {_npv:.2f}|IRR (rate at which NPV = 0) = {_irr(_cf)*100:.1f}%",
      "NPV is positive and the IRR exceeds 10%: accept. For a single conventional project the two rules always agree."),
     ("A company earns after-tax operating profit of 120 on invested capital of 1,000. Its cost of capital is 9%. Is it creating value?",
      f"ROIC = 120 / 1,000 = {120/1000*100:.0f}%, above the 9% cost of capital: yes", "")],
    (["Pair", "Difference"], [
        ["NPV vs IRR for mutually exclusive projects", "They can rank projects differently because of size and timing; choose by NPV"],
        ["Sunk cost vs opportunity cost", "Already spent: ignore. Value of the next best use of a resource: include"],
        ["Externality / cannibalization", "Effect of the project on the firm's other cash flows: include"],
        ["Real options", "Timing (delay), sizing (expand or abandon), flexibility (change price or inputs), fundamental (payoff depends on an underlying price)"],
        ["Project types", "Going concern (maintenance), regulatory or compliance, expansion, and other (new ventures)"]]),
    "Expect an NPV or IRR decision and questions on which cash flows to include. Use after-tax incremental cash flows, ignore financing costs (they are in the discount rate), and ignore sunk costs. IRR assumes reinvestment at the IRR and can give several answers when cash flows change sign more than once.")

# --- cs: Capital Structure ---
EK["cs"] = G(
    [("A company is financed 60% with equity costing 12% and 40% with debt costing 6% before tax. The tax rate is 25%. What is its weighted average cost of capital?",
      f"WACC = 0.60 × 12% + 0.40 × 6% × (1 − 25%) = {.6*12:.1f}% + {.4*6*.75:.1f}% = {.6*12+.4*6*.75:.1f}%",
      "Use target weights at market values, and the after-tax cost of debt because interest is deductible.")],
    (["Theory", "Conclusion"], [
        ["Modigliani–Miller, no taxes", "Capital structure does not affect firm value; the cost of equity rises with leverage so WACC stays constant"],
        ["Modigliani–Miller, with taxes", "Value rises with debt because of the interest tax shield; taken alone, it implies 100% debt"],
        ["Static trade-off", "There is an optimum where the tax shield from more debt equals the added expected cost of financial distress"],
        ["Pecking order", "Managers prefer internal funds, then debt, then new equity, because each signals less bad news than the next"]]),
    "Besides the WACC calculation, expect \"according to which theory\" questions. Know what moves a firm toward more debt: stable cash flows, tangible assets, a high tax rate and a mature business. Start-ups and firms with volatile cash flows or mostly intangible assets use little debt. Issuing equity is often read as a signal that management thinks the shares are overvalued.")

# --- bm: Business Models ---
EK["bm"] = G(
    [("A subscription product sells for 50 a month. Variable cost is 30 per customer and fixed costs are 10,000 a month. How many customers are needed to break even?",
      f"contribution per customer = 50 − 30 = {50-30}|break-even = 10,000 / 20 = {10000//20} customers",
      "Unit economics come first: if the contribution per unit is negative, growth only makes the loss larger.")],
    (["Pricing or model", "How it works"], [
        ["Freemium", "Basic service free; a minority pays for premium features"],
        ["Razors and blades", "Low price on the device, profit on the consumables"],
        ["Subscription", "Recurring fee for ongoing access"],
        ["Penetration pricing", "Low price at first to win share and scale"],
        ["Bundling / tiered pricing", "Several products at one price / different prices for different volumes or features"],
        ["Platform with network effects", "The service becomes more valuable to each user as more users join"]]),
    "Questions describe a company and ask which model or pricing approach it uses. A business model explains who the customers are, what is offered, how it is delivered and how the firm earns money; it is not a financial forecast. Asset-light models, franchising and licensing shift capital needs to others and raise return on capital.")
