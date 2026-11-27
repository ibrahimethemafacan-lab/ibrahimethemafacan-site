import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- af: Features, Methods, Structures ---
EK["af"] = G(
    [("A fund starts the year with 100 million and earns a gross return of 10%. It charges a 2% management fee on beginning assets and a 20% incentive fee on gains net of the management fee, with no hurdle. What is the investor's net return?",
      f"gross gain = 10.0|management fee = 2% × 100 = {.02*100:.1f}|incentive fee = 20% × (10.0 − 2.0) = {.2*8:.1f}|total fees = {2+1.6:.1f}; net return = (10.0 − 3.6) / 100 = {10-3.6:.1f}%",
      "Read the fee basis carefully: the management fee may be on beginning or ending assets, and the incentive fee may be calculated before or after the management fee.")],
    (["Pair", "Difference"], [
        ["Fund investing vs co-investing vs direct investing", "From least control and lowest due-diligence burden to most control, lowest fees and highest required expertise"],
        ["General partner vs limited partner", "The GP manages the fund and has unlimited liability; LPs supply capital and are liable only for what they committed"],
        ["Committed vs invested capital", "Committed is the total pledged; invested is what has been drawn down so far"],
        ["Deal-by-deal (American) vs whole-of-fund (European) waterfall", "Deal-by-deal pays the GP earlier and favors the GP; whole-of-fund pays the GP only after LPs recover all capital plus the hurdle"],
        ["Clawback", "LPs can recover incentive fees already paid if later losses make them excessive"]]),
    "Fee calculations dominate. Check three things before computing: the management fee base, whether the incentive fee is net of the management fee, and whether a hurdle or high-water mark applies. Structure questions ask which waterfall or which investment method is better for the investor.")

# --- ap: Performance and Returns ---
EK["ap"] = G(
    [("A private equity fund has called 50 million from an investor, has distributed 30 million and reports a remaining net asset value of 45 million. Compute DPI, RVPI and TVPI.",
      f"DPI = distributions / paid-in = 30 / 50 = {30/50:.1f}×|RVPI = residual value / paid-in = 45 / 50 = {45/50:.1f}×|TVPI = DPI + RVPI = {75/50:.1f}×",
      "TVPI is the multiple of invested capital. Only DPI is cash already received; RVPI depends on the manager's valuations."),
     ("A fund gains 12 on 100 of capital. The incentive fee is 20% and the hurdle rate is 8%. What is the fee with a soft hurdle and with a hard hurdle?",
      f"soft hurdle (hurdle cleared, fee on the whole gain): 20% × 12 = {.2*12:.1f}|hard hurdle (fee only on the excess): 20% × (12 − 8) = {.2*4:.1f}", "")],
    (["Pair", "Difference"], [
        ["IRR vs multiple (MOIC)", "IRR accounts for the timing of cash flows; the multiple ignores time"],
        ["J-curve", "Early negative returns from fees and investment costs, turning positive as investments mature and exit"],
        ["Appraisal-based returns", "Smoothed valuations understate volatility and correlation with other assets, so diversification benefits look larger than they are"],
        ["Survivorship vs backfill bias", "Failed funds drop out of the index; new funds add only their good past record. Both overstate index returns"]]),
    "Expect a fee or multiple calculation and a bias question. Because alternative returns are smoothed and indices are biased upward, reported Sharpe ratios are overstated. For private funds, IRR is the standard measure because the manager controls the timing of cash flows.")

# --- pk: Private Capital ---
EK["pk"] = G(
    [("A buyout fund acquires a company for 1,000, financed with 700 of debt and 300 of equity. Five years later it sells the company for 1,400, when debt has been paid down to 500. What are the equity multiple and the annualized return?",
      f"equity at exit = 1,400 − 500 = {1400-500}|multiple = 900 / 300 = {900/300:.1f}×|annualized return = 3.0<sup>1/5</sup> − 1 = {(3**.2-1)*100:.1f}%",
      "The company's value rose 40%, but equity tripled: leverage and debt paydown did most of the work.")],
    (["Category", "Types"], [
        ["Venture capital stages", "Pre-seed and seed (idea), early stage (start of operations), later stage (expansion), mezzanine stage (preparing for an IPO)"],
        ["Growth equity vs buyout", "Minority stake in an established, growing firm vs controlling stake, usually with leverage"],
        ["Private debt", "Direct lending, mezzanine debt, venture debt, distressed debt, unitranche"],
        ["Exit routes", "Trade sale, IPO, secondary sale to another fund, recapitalization, write-off"]]),
    "Questions describe a company and ask for the financing stage, or describe a loan and ask for the type of private debt. Mezzanine debt is subordinated and often comes with warrants; mezzanine-stage venture capital is something else: financing before going public. A recapitalization is not a true exit, since the fund keeps control.")

# --- re: Real Estate and Infrastructure ---
EK["re"] = G(
    [("An office building produces net operating income of 5 million a year. Comparable buildings trade at a capitalization rate of 6.25%. What is the building worth, and what is the loan-to-value ratio with a 48 million mortgage?",
      f"value = NOI / cap rate = 5 / 0.0625 = {5/.0625:.0f} million|LTV = 48 / 80 = {48/80*100:.0f}%",
      "A lower cap rate means a higher value for the same income. NOI is before financing costs and income taxes.")],
    (["Pair", "Difference"], [
        ["Equity REIT vs mortgage REIT", "Owns and operates properties vs holds real estate loans and MBS"],
        ["Core vs value-add vs opportunistic", "Stable, income-producing properties vs redevelopment vs development and distressed assets, in rising order of risk"],
        ["Direct vs indirect investment", "Owning the property (control, illiquidity, large size) vs REITs and funds (liquidity, diversification)"],
        ["Brownfield vs greenfield", "Existing infrastructure with known cash flows vs new construction with higher risk and return"],
        ["Economic vs social infrastructure", "Transport, energy, utilities (user fees) vs schools, hospitals, prisons (availability payments from government)"]]),
    "Expect a cap-rate valuation and classification questions. REITs behave more like equities in the short run than the properties they own. Infrastructure cash flows are long-lived, often regulated and inflation-linked, which suits pension funds and insurers with long liabilities.")

# --- nr: Natural Resources ---
EK["nr"] = G(
    [("Over a year the spot price of a commodity rises 3%. The futures curve is in contango and rolling the position costs 1.5%. Collateral posted for the futures earns 4%. What is the total return on the futures position?",
      f"total return = price return + roll yield + collateral yield|= 3.0% − 1.5% + 4.0% = {3-1.5+4:.1f}%",
      "In backwardation the roll yield would be positive, since each expiring contract is replaced by a cheaper one.")],
    (["Pair", "Difference"], [
        ["Contango vs backwardation", "Futures above spot (negative roll yield for a long) vs futures below spot (positive roll yield)"],
        ["Convenience yield", "Benefit of holding the physical commodity; when it is high the market tends to be in backwardation"],
        ["Farmland vs timberland", "Crops must be harvested when ripe; timber can be left standing to grow, so the owner chooses the harvest time"],
        ["Commodity vs commodity producer equity", "Futures give direct price exposure; producer shares add company and equity market risk"]]),
    "The three-part return decomposition and the direction of the roll yield are the standard items. Commodities are valued for inflation protection and low correlation with stocks and bonds, not for income: they generate no cash flow, so their price reflects supply and demand, not discounted cash flows.")

# --- hf: Hedge Funds ---
EK["hf"] = G(
    [("A hedge fund's high-water mark is 110. It begins the year at 100 and ends at 115 before incentive fees. The incentive fee is 20%. What incentive fee is paid?",
      f"gain above the high-water mark = 115 − 110 = {115-110}|incentive fee = 20% × 5 = {.2*5:.1f}",
      "The recovery from 100 to 110 earns no incentive fee: investors do not pay twice for the same performance.")],
    (["Strategy group", "Examples", "Source of return"], [
        ["Equity hedge", "Long/short, market neutral, short-biased", "Stock selection"],
        ["Event-driven", "Merger arbitrage, distressed, activist", "Corporate events"],
        ["Relative value", "Convertible arbitrage, fixed-income arbitrage", "Pricing discrepancies between related securities"],
        ["Opportunistic", "Global macro, managed futures", "Top-down views on markets and trends"]]),
    "Questions describe what a manager does and ask for the strategy. Merger arbitrage buys the target and shorts the acquirer. Liquidity terms are also tested: a lockup is the initial period with no redemptions, a notice period is the advance warning required, and a gate limits how much can be withdrawn at once. A fund of funds adds diversification and access, but a second layer of fees.")

# --- da: Digital Assets ---
EK["da"] = G(
    [("A portfolio holds 2% in a cryptocurrency and 98% in other assets. The cryptocurrency falls 50% while the other assets are unchanged. What is the effect on the portfolio?",
      f"contribution = 2% × (−50%) = {.02*-50:.1f}%",
      "Very high volatility means even a small weight contributes noticeably to portfolio risk. Position size, not price forecasts, is the main risk control.")],
    (["Pair", "Difference"], [
        ["Coin vs token", "A coin is the native asset of its own blockchain; a token is built on another blockchain"],
        ["Permissionless vs permissioned network", "Open to anyone vs restricted to approved participants"],
        ["Proof of work vs proof of stake", "Miners compete with computing power vs validators pledge their own holdings; proof of stake uses far less energy"],
        ["Centralized vs decentralized exchange", "A company holds the assets and matches orders vs trading through smart contracts with no intermediary"],
        ["Stablecoin vs CBDC", "Privately issued token meant to track a currency vs digital money issued by a central bank"],
        ["Direct vs indirect investment", "Holding the asset in a wallet vs trusts, futures, exchange-traded products or shares of related companies"]]),
    "This reading is tested conceptually: classify the asset, the network or the form of investment. Remember that cryptocurrencies have no cash flows to discount, so their value depends on adoption and scarcity, and that historical correlations with traditional assets have been low but unstable.")
