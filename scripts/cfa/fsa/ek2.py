import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- in: Introduction ---
EK["in"] = G(
    [("An analyst needs three things: the company's inventory accounting method, management's own view of liquidity and capital resources, and the pay of the chief executive. Where does each appear?",
      "", "The accounting method is in the notes to the financial statements. Management's view of liquidity is in the management commentary (MD&A), which is not audited. Executive pay is in the proxy statement.")],
    (["Audit opinion", "Meaning"], [
        ["Unqualified (unmodified, clean)", "Statements are fairly presented"],
        ["Qualified", "Fairly presented except for a specific matter"],
        ["Adverse", "Not fairly presented: material departures from the standards"],
        ["Disclaimer", "The auditor could not form an opinion"],
        ["Key audit matters", "Areas of significant judgment the auditor highlights; not a qualification"]]),
    "Questions name a piece of information and ask where it is found, or describe an auditor's conclusion and ask for the opinion type. The framework for analysis is also tested by its order: state the purpose, collect data, process data, analyze, conclude and communicate, follow up. An audit gives reasonable assurance, not a guarantee.")

# --- is: Income Statements ---
_new = 100 - 100 * 20 / 25
EK["is"] = G(
    [("Net income is 1,000 and preferred dividends are 100. There are 400 weighted average common shares and 100 options with an exercise price of 20; the average share price was 25. Compute basic and diluted EPS.",
      f"basic EPS = (1,000 − 100) / 400 = {900/400:.2f}|treasury stock method: shares issued 100; shares bought back = 100 × 20 / 25 = {100*20/25:.0f}; net new shares = {_new:.0f}|diluted EPS = 900 / (400 + 20) = {900/420:.2f}",
      "Options are dilutive only when the average market price is above the exercise price. If a security would raise EPS it is antidilutive and is left out.")],
    (["Pair", "Difference"], [
        ["Basic vs diluted EPS", "Actual shares outstanding vs as if all dilutive securities had been converted"],
        ["Principal vs agent", "A principal reports revenue gross; an agent reports only its fee or commission"],
        ["Change in accounting policy vs estimate", "Policy: applied retrospectively, prior periods restated. Estimate: applied prospectively"],
        ["Operating vs non-operating items", "From the core business vs from investing and financing, such as interest for a non-financial firm"],
        ["Discontinued operations", "Reported separately, net of tax, below income from continuing operations"]]),
    "Diluted EPS is the staple calculation: use the if-converted method for convertible bonds and preferred, and the treasury stock method for options and warrants. Revenue questions follow the five steps: identify the contract, identify the performance obligations, determine the price, allocate it, and recognise revenue as each obligation is satisfied.")

# --- bs: Balance Sheets ---
EK["bs"] = G(
    [("Current assets consist of cash 80, marketable securities 40, receivables 130 and inventory 250. Current liabilities are 250. Compute the current, quick and cash ratios.",
      f"current ratio = 500 / 250 = {500/250:.2f}|quick ratio = (80 + 40 + 130) / 250 = {250/250:.2f}|cash ratio = (80 + 40) / 250 = {120/250:.2f}",
      "Half of the current assets are inventory, so the quick ratio is far lower than the current ratio: liquidity depends on selling that inventory.")],
    (["Financial asset category", "Carried at", "Unrealized gains and losses"], [
        ["Amortized cost", "Amortized cost", "Not recognized"],
        ["Fair value through OCI", "Fair value", "In other comprehensive income"],
        ["Fair value through profit or loss", "Fair value", "In the income statement"]]),
    "Expect liquidity and solvency ratios from a short balance sheet, and classification items: which securities' gains go through income and which through OCI. Goodwill is the excess of purchase price over the fair value of identifiable net assets; it is not amortized but tested for impairment. Internally generated goodwill is never recognized.")

# --- c1: Cash Flows I ---
EK["c1"] = G(
    [("Net income is 100. Depreciation was 30 and there was a gain of 10 on the sale of equipment. Receivables rose by 15, inventory fell by 5 and payables rose by 8. What is cash flow from operations under the indirect method?",
      f"CFO = 100 + 30 − 10 − 15 + 5 + 8 = {100+30-10-15+5+8}",
      "Add back non-cash charges, remove gains that belong to investing, subtract increases in operating assets and add increases in operating liabilities.")],
    (["Item", "US GAAP", "IFRS"], [
        ["Interest received", "Operating", "Operating or investing"],
        ["Interest paid", "Operating", "Operating or financing"],
        ["Dividends received", "Operating", "Operating or investing"],
        ["Dividends paid", "Financing", "Operating or financing"],
        ["Taxes paid", "Operating", "Operating, unless tied to an investing or financing item"]]),
    "The direction of working capital adjustments is where marks are lost: an increase in an asset uses cash, an increase in a liability provides it. The classification table is tested directly. The direct and indirect methods give the same operating cash flow; only the presentation differs, and investing and financing sections are identical.")

# --- c2: Cash Flows II ---
EK["c2"] = G(
    [("Cash flow from operations is 118 after interest paid of 20. The tax rate is 25%, fixed capital investment is 40 and net borrowing is 10. Compute FCFF and FCFE.",
      f"FCFF = CFO + interest × (1 − t) − FCInv = 118 + 20 × 0.75 − 40 = {118+15-40}|FCFE = CFO − FCInv + net borrowing = 118 − 40 + 10 = {118-40+10}",
      "FCFF belongs to all providers of capital, so after-tax interest is added back. FCFE is what is left for shareholders after debt holders are paid and new debt is raised.")],
    (["Pair", "Difference"], [
        ["FCFF vs FCFE", "Available to lenders and shareholders vs to shareholders only"],
        ["Performance vs coverage ratios", "Cash flow relative to revenue, assets or equity vs cash flow relative to debt, interest or dividends"],
        ["Cash flow vs earnings", "Operating cash flow persistently below net income is a sign of low earnings quality"],
        ["Common-size cash flow statement", "Each item as a percentage of revenue, or of total inflows and outflows"]]),
    "Besides the two free cash flow formulas, questions ask you to judge a company from the pattern of its cash flows. A healthy mature company funds investing outflows from operations. A company relying on financing inflows to cover negative operating cash flow is either young or in trouble.")

# --- iv: Inventories ---
EK["iv"] = G(
    [("A company buys 10 units at 5, then 10 units at 7, and sells 12 units. Find cost of goods sold and ending inventory under FIFO, LIFO and weighted average cost.",
      f"FIFO: COGS = 10 × 5 + 2 × 7 = {10*5+2*7}; ending inventory = 8 × 7 = {8*7}|LIFO: COGS = 10 × 7 + 2 × 5 = {10*7+2*5}; ending inventory = 8 × 5 = {8*5}|average cost = 120 / 20 = 6: COGS = {12*6}; ending inventory = {8*6}",
      "COGS plus ending inventory is 120 in every case: the method only decides how the cost is split.")],
    (["When prices rise", "FIFO", "LIFO"], [
        ["Cost of goods sold", "Lower", "Higher"],
        ["Net income and taxes", "Higher", "Lower"],
        ["Ending inventory", "Higher, close to current cost", "Lower, at old costs"],
        ["Cash flow", "Lower (more tax paid)", "Higher"],
        ["Allowed under", "IFRS and US GAAP", "US GAAP only"]]),
    "Comparison questions ask for the effect of the method on a ratio: with rising prices, LIFO gives lower margins, a lower current ratio and higher inventory turnover. To compare a LIFO firm with a FIFO firm, add the LIFO reserve to inventory. Under IFRS, inventory is written down to net realizable value and the write-down can be reversed; under US GAAP it cannot.")

# --- lt: Long-Term Assets ---
EK["lt"] = G(
    [("Equipment costs 100, has a salvage value of 10 and a five-year life. Compute depreciation in years 1 and 2 under the straight-line and double-declining-balance methods.",
      f"straight-line = (100 − 10) / 5 = {(100-10)/5:.0f} each year|double-declining rate = 2 / 5 = 40%|year 1 = 40% × 100 = {.4*100:.0f}; year 2 = 40% × (100 − 40) = {.4*60:.0f}",
      "Declining-balance ignores salvage value in the calculation but stops when book value reaches it."),
     ("Under IFRS, an asset has a carrying amount of 80, fair value less costs to sell of 70 and value in use of 74. What is the impairment loss?",
      f"recoverable amount = higher of 70 and 74 = 74|loss = 80 − 74 = {80-74}", "")],
    (["Topic", "IFRS", "US GAAP"], [
        ["Impairment test", "Carrying amount vs recoverable amount", "First compare with undiscounted cash flows; if not recoverable, write down to fair value"],
        ["Reversal of impairment", "Allowed, up to the original carrying amount", "Not allowed for assets held for use"],
        ["Revaluation above cost", "Allowed (revaluation model)", "Not allowed"],
        ["Research and development", "Research expensed; development capitalized if criteria are met", "Both expensed, with limited exceptions such as software"]]),
    "Capitalizing versus expensing is the central theme: capitalizing gives higher profit, assets and operating cash flow now, and lower profit later. Expect depreciation calculations, the effect of a longer useful life on income, and the gain or loss on disposal: proceeds minus carrying amount.")

# --- ll: Long-Term Liabilities and Equity ---
_pv = sum(100 / 1.06 ** t for t in (1, 2, 3))
EK["ll"] = G(
    [("A company leases equipment for three years with payments of 100 at each year-end. The discount rate is 6%. What does the lessee record at inception, and how is the first payment split?",
      f"lease liability = right-of-use asset = 100/1.06 + 100/1.06<sup>2</sup> + 100/1.06<sup>3</sup> = {_pv:.2f}|interest in year 1 = {_pv:.2f} × 6% = {_pv*.06:.2f}|principal repaid = 100 − {_pv*.06:.2f} = {100-_pv*.06:.2f}",
      "Under IFRS the lessee then shows depreciation and interest as separate expenses for every lease. Under US GAAP an operating lease shows a single straight-line lease expense.")],
    (["Pair", "Difference"], [
        ["Finance vs operating lease (lessee, US GAAP)", "Both go on the balance sheet. Finance: interest plus amortization, front-loaded. Operating: one level expense, all in operating cash flow"],
        ["Defined contribution vs defined benefit", "Expense equals the contribution vs the employer owes a promised benefit and carries the investment risk"],
        ["Funded status", "Fair value of plan assets minus the pension obligation; a deficit is reported as a liability"],
        ["Stock options vs restricted stock", "Both expensed at grant-date fair value over the vesting period; options need a pricing model"]]),
    "Lease questions ask for the opening liability, the first year's interest, or the effect on ratios: recognizing a lease raises assets and liabilities, so leverage rises and asset turnover falls. For pensions at Level I, know the funded status and who bears the risk. Share-based pay reduces income but not cash.")

# --- tx: Income Taxes ---
EK["tx"] = G(
    [("An asset costing 100 is depreciated by 20 in the accounts and by 40 for tax in its first year. The tax rate is 25%. What deferred tax item arises? If taxes payable are 30, what is income tax expense?",
      f"carrying amount = 100 − 20 = {100-20}; tax base = 100 − 40 = {100-40}|temporary difference = 80 − 60 = {80-60}|deferred tax liability = 20 × 25% = {20*.25:.0f}|tax expense = taxes payable + increase in DTL = 30 + 5 = {30+5}",
      "The asset's carrying amount exceeds its tax base, so more tax will be paid later: a liability.")],
    (["Pair", "Difference"], [
        ["Deferred tax liability vs asset", "Tax to be paid later (asset carrying amount above tax base) vs tax relief to come (for example, warranty accruals, loss carryforwards)"],
        ["Temporary vs permanent difference", "Reverses over time and creates deferred tax vs never reverses and only changes the effective tax rate"],
        ["Taxable income vs accounting profit", "Computed under tax law vs under accounting standards"],
        ["Valuation allowance", "Reduces a deferred tax asset under US GAAP when it is unlikely to be used"],
        ["Statutory vs effective vs cash tax rate", "The legal rate vs tax expense over pretax income vs cash taxes paid over pretax income"]]),
    "Expect the deferred tax calculation, and the effect of a change in the tax rate: a rate cut reduces both deferred tax liabilities and assets, so a company with a net liability records a gain. A deferred tax liability that is not expected to reverse can be treated as equity in analysis.")

# --- rq: Financial Reporting Quality ---
EK["rq"] = G(
    [("In one year a company lengthens the useful lives of its equipment, ships unusually large volumes to distributors just before year-end, and reports net income growing 20% while operating cash flow falls. What should an analyst conclude?",
      "", "Each choice raises current earnings: lower depreciation, revenue pulled forward (channel stuffing), and profit not backed by cash. The reporting may still comply with the standards, but it is aggressive and the earnings are of low quality because they are unlikely to be sustained.")],
    (["Pair", "Difference"], [
        ["Reporting quality vs earnings quality", "How faithfully the statements describe the business vs whether the earnings are sustainable and adequate"],
        ["Conservative vs aggressive accounting", "Delays income or accelerates expenses vs the opposite; both are biased"],
        ["Earnings smoothing", "Understating profit in good years to release it in bad years"],
        ["Fraud triangle", "Opportunity, motivation (pressure) and rationalization"],
        ["Compliant vs high quality", "Reports can follow the rules and still mislead through biased choices and estimates"]]),
    "Questions present a set of choices and ask whether they are conservative or aggressive, or ask which warning sign matters most. Classic warning signs: revenue growing faster than peers', receivables growing faster than revenue, operating cash flow below net income, frequent \"one-off\" items, and heavy use of non-GAAP measures. High-quality earnings require high-quality reporting first.")

# --- ra: Financial Analysis Techniques ---
EK["ra"] = G(
    [("A company has net income of 60, revenue of 1,000, average total assets of 800 and average equity of 400. Decompose its return on equity.",
      f"net profit margin = 60 / 1,000 = {60/1000*100:.1f}%|asset turnover = 1,000 / 800 = {1000/800:.2f}|financial leverage = 800 / 400 = {800/400:.1f}|ROE = 6.0% × 1.25 × 2.0 = {.06*1.25*2*100:.1f}%", ""),
     ("Days of inventory on hand are 60, days of sales outstanding 45 and days of payables 30. What is the cash conversion cycle?",
      f"60 + 45 − 30 = {60+45-30} days",
      "A shorter cycle means less cash tied up in operations.")],
    (["Ratio group", "Question it answers", "Examples"], [
        ["Activity", "How efficiently are assets used?", "Inventory turnover, receivables turnover, asset turnover"],
        ["Liquidity", "Can short-term obligations be met?", "Current, quick, cash ratios"],
        ["Solvency", "Can long-term obligations be met?", "Debt to equity, interest coverage"],
        ["Profitability", "How much profit from sales and capital?", "Margins, ROA, ROE"],
        ["Valuation", "What is the market paying?", "P/E, price to book"]]),
    "DuPont items ask which component drove a change in ROE. The five-part version splits the margin into tax burden, interest burden and EBIT margin. Other questions give two companies' ratios and ask which is more liquid or more leveraged, so know which group each ratio belongs to and in which direction it is \"better\".")

# --- fm: Financial Statement Modeling ---
EK["fm"] = G(
    [("Revenue of 1,000 is forecast to grow 10%. Gross margin is expected to be 40% and selling and administrative costs 20% of revenue. What is forecast operating income? How sensitive is it to a gross margin of 38%?",
      f"revenue = 1,000 × 1.10 = {1000*1.1:,.0f}|gross profit = 40% × 1,100 = {.4*1100:.0f}; SG&amp;A = 20% × 1,100 = {.2*1100:.0f}|operating income = {.4*1100-.2*1100:.0f}|at 38%: gross profit = {.38*1100:.0f}; operating income = {.38*1100-.2*1100:.0f} ({(198/220-1)*100:.0f}%)",
      "A two-point change in gross margin moves operating income by 10%. Sensitivity analysis shows which assumptions deserve the most work.")],
    (["Pair", "Difference"], [
        ["Top-down vs bottom-up", "Start from the economy and market share vs start from units, prices and segments"],
        ["Sensitivity vs scenario analysis", "Change one input at a time vs change several together in a coherent story"],
        ["Overconfidence vs illusion of control", "Too narrow a range of outcomes vs believing more detail or expertise makes the forecast more accurate"],
        ["Conservatism vs confirmation bias", "Slow to revise a forecast vs looking only for supporting evidence"],
        ["Cost pass-through", "Firms with pricing power can pass on higher input costs; others see margins shrink"]]),
    "Expect a simple forecast of an income statement line and a question on the analyst's behavioral biases with a remedy for each: overconfidence (record and review past forecast errors), confirmation (seek opposing views), representativeness (start from the base rate). Competitive forces matter because they cap prices and therefore margins.")
