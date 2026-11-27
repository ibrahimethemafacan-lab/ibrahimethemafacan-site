import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- mo: Market Organization and Structure ---
EK["mo"] = G(
    [("An investor buys 100 shares at 50 with an initial margin of 40%. The maintenance margin is 25%. What is the return on equity if the price rises to 60 (ignore interest and commissions), and at what price is there a margin call?",
      f"equity = 40% × 5,000 = {n(2000,0)}; loan = {n(3000,0)}; leverage = 1 / 0.40 = {1/.4:.1f}×|gain = (60 − 50) × 100 = {n(1000,0)}; return on equity = 1,000 / 2,000 = {1000/2000*100:.0f}%|margin call price = 50 × (1 − 0.40) / (1 − 0.25) = {50*.6/.75:.2f}",
      "The share rose 20% and the leveraged return is 2.5 times that. Losses are magnified in the same way.")],
    (["Order or market", "Meaning"], [
        ["Market order", "Execute now at the best available price: certain execution, uncertain price"],
        ["Limit order", "Execute only at the limit price or better: certain price, uncertain execution"],
        ["Stop order", "Becomes a market order once the stop price is touched; a stop-sell limits losses on a long position"],
        ["Quote-driven (dealer) market", "Investors trade with dealers at posted bid and ask prices; most bonds and currencies"],
        ["Order-driven market", "Orders are matched by rules of price and time priority; most stock exchanges"],
        ["Brokered market", "Brokers find a counterparty for unique or illiquid items"]]),
    "Margin calculations and order types are the routine items. Read stop orders carefully: a stop-buy is placed above the market, a stop-sell below it. Also know the three types of market efficiency the system should deliver: informational, operational (low trading costs) and allocational, and the difference between primary offerings (IPO, seasoned, private placement, rights) and secondary trading.")

# --- ix: Security Market Indexes ---
_p0 = [10, 20, 50]; _p1 = [11, 18, 55]; _sh = [300, 50, 10]
_pw = sum(_p1) / sum(_p0) - 1
_ew = sum(b / a - 1 for a, b in zip(_p0, _p1)) / 3
_cw = sum(b * s for b, s in zip(_p1, _sh)) / sum(a * s for a, s in zip(_p0, _sh)) - 1
EK["ix"] = G(
    [("Three stocks move from 10, 20 and 50 to 11, 18 and 55. Shares outstanding are 300, 50 and 10. Compute the return of a price-weighted, an equal-weighted and a market-capitalization-weighted index.",
      f"price-weighted: (11 + 18 + 55) / (10 + 20 + 50) − 1 = {_pw*100:.2f}%|equal-weighted: (10% − 10% + 10%) / 3 = {_ew*100:.2f}%|cap-weighted: (3,300 + 900 + 550) / (3,000 + 1,000 + 500) − 1 = {_cw*100:.2f}%",
      "Same stocks, same price moves, different index returns: the weighting method decides which stock matters most.")],
    (["Weighting", "Bias or drawback"], [
        ["Price", "Highest-priced stock dominates; a stock split changes the weights"],
        ["Market capitalization", "Overweights stocks that have risen, possibly overvalued ones; a momentum tilt"],
        ["Float-adjusted capitalization", "Counts only shares available to the public; the usual choice for investable indexes"],
        ["Equal", "Small-company tilt; needs frequent rebalancing"],
        ["Fundamental", "Value tilt; weights by sales, earnings, book value or dividends"]]),
    "Expect the three index returns from a small table. Know the difference between a price return index and a total return index (which adds income), and between rebalancing (adjusting weights) and reconstitution (changing the constituents). A cap-weighted index rebalances itself as prices move.")

# --- me: Market Efficiency ---
EK["me"] = G(
    [("A company announces earnings far above expectations. Its share price jumps 8% within minutes and shows no further abnormal movement in the following weeks. With which form of efficiency is this consistent?",
      "", "With semi-strong efficiency: public information is reflected in the price immediately, so trading after the announcement earns no abnormal return. Had the price kept drifting upward for weeks, that would be evidence against it (post-earnings-announcement drift).")],
    (["Form", "Prices reflect", "What cannot earn abnormal returns"], [
        ["Weak", "Past prices and volume", "Technical analysis"],
        ["Semi-strong", "All public information", "Technical and fundamental analysis"],
        ["Strong", "All public and private information", "Anything, including inside information"]]),
    "Questions ask which strategy should fail under a given form, or which form an observation contradicts. Anomalies are grouped as time-series (January effect, momentum, overreaction), cross-sectional (size, value) and other (closed-end fund discounts, earnings surprises, IPOs). Most shrink or vanish after transaction costs. Limits to arbitrage: costs of trading and of information, and restrictions on short selling.")

# --- eq: Overview of Equity Securities ---
EK["eq"] = G(
    [("A company has cumulative preferred shares with a par value of 100 and a 5% dividend. It paid no preferred dividend in the last two years. How much must it pay per preferred share this year before any common dividend?",
      f"arrears = 2 × 5 = {2*5}|current year = 5|total = {2*5+5} per share",
      "With non-cumulative preferred shares the missed dividends would be lost and only 5 would be due."),
     ("Net income is 150 and average book value of equity is 1,000. The market value of equity is 2,400. Compute ROE and the price-to-book ratio.",
      f"ROE = 150 / 1,000 = {150/1000*100:.0f}%|P/B = 2,400 / 1,000 = {2400/1000:.1f}",
      "A price-to-book ratio above 1 says investors expect the company to earn more than its cost of equity on future investments.")],
    (["Pair", "Difference"], [
        ["Common vs preferred shares", "Residual claim with votes vs fixed dividend, priority over common, usually no vote"],
        ["Cumulative vs non-cumulative preferred", "Missed dividends accumulate and must be paid first vs they are lost"],
        ["Participating preferred", "Receives extra dividends when profits exceed a set level"],
        ["Callable vs putable shares", "Issuer may buy back at a set price (favors the issuer) vs holder may sell back (favors the holder)"],
        ["Sponsored vs unsponsored depository receipt", "Issuer is involved and holders vote vs the depository bank keeps the voting rights"],
        ["Book value vs market value of equity", "Accounting net assets from the past vs investors' view of the future"]]),
    "Expect risk rankings (putable is less risky than callable; cumulative less risky than non-cumulative; preferred less risky than common) and return on equity interpretations. A rising ROE is not always good: it can come from a shrinking equity base after losses or buybacks financed with debt.")

# --- ca: Company Analysis: Past and Present ---
EK["ca"] = G(
    [("A company has revenue of 1,000, variable costs of 600 and fixed operating costs of 300. What is its degree of operating leverage, and what happens to operating income if revenue rises 10%?",
      f"contribution margin = 1,000 − 600 = {1000-600}|operating income = 400 − 300 = {400-300}|degree of operating leverage = 400 / 100 = {400/100:.0f}|operating income change ≈ 4 × 10% = {4*10}%",
      "Check: new contribution is 440, less 300 of fixed cost gives 140, which is 40% higher.")],
    (["Pair", "Difference"], [
        ["Operating vs financial leverage", "Fixed operating costs magnify the effect of sales on operating income vs fixed interest costs magnify the effect on net income"],
        ["Top-down vs bottom-up revenue analysis", "From market size and share vs from products, prices, volumes and segments"],
        ["Fixed vs variable costs", "Do not change with volume in the short run vs move with volume"],
        ["Pricing power", "Ability to raise prices without losing volume; shows in stable or rising gross margins"],
        ["Sources vs uses of capital", "Operating cash flow, debt, equity vs capital expenditure, acquisitions, dividends, buybacks"]]),
    "Questions give a small income statement and ask for a leverage measure, or describe a company and ask what explains its margins. High operating leverage means profits are very sensitive to volume, which is good in expansions and dangerous in downturns. A company research report should separate facts from the analyst's opinion.")

# --- ic: Industry and Competitive Analysis ---
EK["ic"] = G(
    [("An industry's growth has slowed sharply. Capacity exceeds demand, prices are being cut, and weaker companies are failing or being acquired. Which life-cycle stage is this, and what follows?",
      "", "This is the shakeout stage. It follows the growth stage and leads to maturity, where a smaller number of firms compete with stable shares, little growth and often high barriers to entry.")],
    (["Force (Porter)", "Stronger when"], [
        ["Threat of new entrants", "Barriers to entry are low"],
        ["Bargaining power of suppliers", "Few suppliers, no substitutes for the input"],
        ["Bargaining power of buyers", "Few large buyers, low switching costs"],
        ["Threat of substitutes", "Close alternatives exist at a similar price"],
        ["Rivalry among competitors", "Many similar firms, slow growth, high fixed costs, high exit barriers"]]),
    "A short industry description followed by \"which force is most significant\" or \"which stage\" is the typical item. Life-cycle order: embryonic, growth, shakeout, mature, decline. Generic strategies are cost leadership, differentiation and focus. Classification by sensitivity to the business cycle separates cyclical industries (autos, housing, industrials) from defensive ones (utilities, staples, health care).")

# --- cf: Company Analysis: Forecasting ---
EK["cf"] = G(
    [("A company's sales volume is expected to grow 5% and its average price 2%. Revenue this year is 800. Forecast next year's revenue. If the operating margin stays at 15%, what is operating income?",
      f"revenue growth = 1.05 × 1.02 − 1 = {(1.05*1.02-1)*100:.1f}%|revenue = 800 × 1.071 = {800*1.05*1.02:.1f}|operating income = 15% × {800*1.05*1.02:.1f} = {.15*800*1.05*1.02:.1f}",
      "Price and volume effects multiply; they are not simply added.")],
    (["Forecast approach", "When it fits"], [
        ["Historical results", "Stable, mature businesses where the past is a fair guide"],
        ["Historical base rates and convergence", "Assume the company moves toward industry averages over time"],
        ["Management guidance", "When management has a credible record; check for bias"],
        ["Analyst's discretionary forecast", "When the past is not representative: new products, restructuring, cyclical turning points"]]),
    "Questions ask which approach suits a company, or what should drive the choice of forecast horizon: the cyclicality of the industry, the company's own cycle, and the investor's holding period. Forecast objects can be drivers (price, volume), individual line items, or summary measures such as free cash flow. Scenario analysis shows the range of outcomes, not a single point.")

# --- ev: Equity Valuation ---
EK["ev"] = G(
    [("A company just paid a dividend of 2.00, which is expected to grow at 5% forever. Investors require 10%. What is the share worth, and what is the justified forward P/E if the payout ratio is 40%?",
      f"D<sub>1</sub> = 2.00 × 1.05 = {2*1.05:.2f}|V<sub>0</sub> = 2.10 / (0.10 − 0.05) = {2.1/.05:.2f}|justified forward P/E = payout / (r − g) = 0.40 / 0.05 = {.4/.05:.0f}", ""),
     ("Market capitalization is 800, debt is 300 and cash is 100. EBITDA is 125. Compute EV/EBITDA.",
      f"enterprise value = 800 + 300 − 100 = {800+300-100:,}|EV/EBITDA = 1,000 / 125 = {1000/125:.0f}×",
      "Enterprise value multiples allow comparison of companies with different capital structures.")],
    (["Model", "Best suited to"], [
        ["Dividend discount (Gordon growth)", "Mature, stable companies that pay dividends"],
        ["Multistage dividend discount", "Companies moving from high growth to stable growth"],
        ["Free cash flow to equity", "Companies that pay no dividends or pay much less than they could"],
        ["Price multiples", "Quick comparison with peers or with the company's own history"],
        ["Asset-based", "Firms with mostly tangible or financial assets, or in liquidation; poor for intangibles"]]),
    "Gordon growth items test whether you used next year's dividend and whether growth is below the required return. Know the effect of each input: value rises with dividends and growth and falls with the required return. Dividend chronology is also tested: declaration date, ex-dividend date, holder-of-record date, payment date; the price drops by about the dividend on the ex-date.")
