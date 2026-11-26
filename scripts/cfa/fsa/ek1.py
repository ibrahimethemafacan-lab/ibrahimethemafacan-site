# CFA Level I · Financial Statement Analysis · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
import re as _re
EK = {}

EK["in"] = dict(
notes="""<h3>More on sources and the analysis framework</h3>
<ul>
<li>Financial reporting is how companies show their performance and position; financial statement analysis uses that information to make economic decisions, such as whether to invest or lend. Recommending securities is a decision that relies on analysis but is not itself part of the analysis.</li>
<li>Framework: (1) state purpose and context, (2) collect data, (3) process data (adjust statements, calculate ratios, prepare common-size statements), (4) analyse and interpret, (5) develop and communicate conclusions, (6) follow up.</li>
<li>Notes are <b>audited</b> and explain accounting methods, estimates, contingencies and segments. MD&A and management commentary are <b>not audited</b>; under IFRS guidance, management commentary should address key relationships and resources.</li>
<li>Auditors give <b>reasonable assurance</b> that statements are free of material error; they do not guarantee accuracy or confirm every item. An explanatory paragraph is added for going-concern doubts or changes in accounting methods.</li>
<li>Internal controls are management's responsibility; US auditors of listed companies also report on them.</li>
<li>Proxy statements give information on board members, executive pay and matters for shareholder vote. Press releases are company sources, not objective third-party information.</li>
<li>Be suspicious of a new transaction with a material effect on earnings if management's explanation is unclear.</li>
</ul>""",
qs=[
 ["In the financial statement analysis framework, making adjustments to the statements and calculating ratios is part of:", ["processing the data.", "collecting the data.", "analysing and interpreting the data."], 0, "Processing turns raw data into comparable, usable form."],
 ["Using processed data to answer the questions posed and deciding what conclusions they support is the step of:", ["analysing and interpreting the data.", "processing the data.", "following up."], 0, "Interpretation comes after processing."],
 ["Which source most likely contains audited information?", ["Notes to the financial statements", "Management's discussion and analysis", "Press releases"], 0, "Notes are part of the audited statements."],
 ["The standard audit opinion provides:", ["reasonable assurance that the statements are free of material error.", "a guarantee that the statements are accurate.", "a review of every transaction."], 0, "Audits are based on sampling and judgment."],
 ["Which would most likely require an explanatory paragraph in the audit report?", ["Substantial doubt about the going-concern assumption", "A dividend increase", "A new chief executive"], 0, "Explanatory paragraphs cover material uncertainties and changes in accounting methods."],
 ["A firm's internal controls are primarily the responsibility of:", ["management.", "the external auditor.", "the regulator."], 0, "The auditor evaluates them; management designs and maintains them."],
 ["Information about board members' qualifications and executive compensation is best found in the:", ["proxy statement.", "statement of cash flows.", "notes on revenue recognition."], 0, "Proxy statements are sent to shareholders before votes."],
 ["Which is least likely a role of financial statement analysis?", ["Choosing the accounting standards the company must follow", "Assessing management's performance", "Evaluating a company's ability to repay debt"], 0, "Companies follow the standards required in their jurisdictions."],
 ["Which source is an analyst least likely to treat as objective information?", ["The company's press releases", "Government statistics", "Industry data from independent providers"], 0, "Press releases are prepared by management."],
 ["A company records a new type of transaction with a large effect on earnings. An analyst should be most suspicious if:", ["management's explanation of the transaction is unclear.", "the transaction is disclosed in the notes.", "the auditor gives an unqualified opinion."], 0, "Unclear explanations may hide earnings management."],
 ["Which is least likely found in the notes to the financial statements?", ["Management's forecast of next year's earnings", "Accounting policies", "Contingent liabilities"], 0, "Forecasts belong in management commentary, if anywhere."],
])

EK["is"] = dict(
terms=[
 ["Simple capital structure", "Basit sermaye yapısı", "A capital structure with no potentially dilutive securities; only basic EPS is reported.", "Potansiyel olarak sulandırıcı menkul kıymet içermeyen sermaye yapısı; yalnızca temel hisse başına kâr raporlanır."],
 ["Complex capital structure", "Karmaşık sermaye yapısı", "A capital structure with potentially dilutive securities such as convertibles, options and warrants.", "Dönüştürülebilir menkul kıymet, opsiyon ve varant gibi potansiyel olarak sulandırıcı menkul kıymetler içeren sermaye yapısı."],
 ["Antidilutive security", "Sulandırma karşıtı menkul kıymet", "A security whose conversion would raise EPS; it is excluded from diluted EPS.", "Dönüşümü hisse başına kârı artıracak menkul kıymet; sulandırılmış hisse başına kâr hesabına katılmaz."],
 ["If-converted method", "Dönüştürülmüş varsayımı yöntemi", "The method that assumes convertible securities were converted at the start of the year (or at issue).", "Dönüştürülebilir menkul kıymetlerin yıl başında (veya ihraçta) dönüştürüldüğünü varsayan yöntem."],
],
notes="""<h3>EPS mechanics</h3>
<p class="f">basic EPS = (net income − preferred dividends) / weighted average common shares</p>
<p class="f">diluted EPS = (NI − pref. div. + convertible pref. div. + convertible debt interest × (1 − t)) / (WASO + shares from conversion + treasury stock shares)</p>
<ul>
<li>Weight new issues and repurchases by the fraction of the year outstanding. Stock dividends and splits are applied <b>retroactively</b> to all shares outstanding before them, as if they happened at the start of the year.</li>
<li>Treasury stock method for options and warrants: new shares = N × (1 − exercise price / average market price). Only in-the-money options (exercise below average price) are dilutive.</li>
<li>A security is <b>antidilutive</b> if including it would raise EPS; it is excluded. Diluted EPS is always ≤ basic EPS.</li>
<li>Simple capital structure: no convertibles, options or warrants. Callable or putable bonds and non-convertible preferred are fine.</li>
<li>Changes in accounting <b>estimates</b> (useful lives, residual values) are applied prospectively; changes in accounting <b>principles</b> are applied retrospectively; correction of an error requires restatement.</li>
<li>Revenue standards (IFRS 15, ASC 606) are principles-based, with five steps around contracts and <b>performance obligations</b>.</li>
<li>Indefinite-life intangibles are not amortized but tested for impairment. Interest on self-constructed assets is capitalized under both IFRS and US GAAP.</li>
</ul>""",
qs=[
 ["A company has 1,000,000 shares at the start of the year, issues 300,000 on 1 April and buys back 100,000 on 1 October. Its weighted average shares outstanding are:", ["1,125,000", "1,200,000", "1,225,000"], 1, "1,000,000 + 300,000 × 9/12 − 100,000 × 3/12 = 1,200,000."],
 ["A company has 500,000 shares at the start of the year, pays a 10% stock dividend on 1 June and issues 60,000 new shares on 1 September. Its weighted average shares are:", ["540,000", "570,000", "610,000"], 1, "The stock dividend is applied from the start: 550,000. Add 60,000 × 4/12 = 20,000."],
 ["A company has 400,000 shares, splits 2-for-1 on 1 July and issues 100,000 post-split shares on 1 October. Its weighted average shares are:", ["625,000", "800,000", "825,000"], 2, "The split is retroactive: 800,000 + 100,000 × 3/12 = 825,000."],
 ["Net income is $2.4 million, preferred dividends are $0.4 million and weighted average common shares are 1 million. Basic EPS is:", ["$2.00", "$2.40", "$2.80"], 0, "(2.4 − 0.4)/1.0 = 2.00."],
 ["A company has 50,000 options with an exercise price of $30. The average share price is $40. Under the treasury stock method, the options add how many shares to the diluted share count?", ["12,500", "37,500", "50,000"], 0, "Proceeds 1.5 million buy back 37,500 shares at $40, so 50,000 − 37,500 = 12,500."],
 ["A company has net income of $1.5 million, 1 million common shares and 100,000 convertible preferred shares paying $2 each, convertible into 300,000 common shares. Its diluted EPS is closest to:", ["$1.15", "$1.30", "$1.50"], 0, "Basic = (1.5 − 0.2)/1.0 = 1.30. Diluted = 1.5/1.3 = 1.15, which is dilutive."],
 ["Net income is $5 million and there are 2 million shares. The company has $10 million of 6% bonds convertible into 400,000 shares; the tax rate is 25%. Diluted EPS is closest to:", ["$2.08", "$2.27", "$2.50"], 1, "Add back interest of 600,000 × 0.75 = 450,000: 5.45/2.4 = 2.27."],
 ["Options with an exercise price above the average market price during the year are:", ["antidilutive and excluded from diluted EPS.", "dilutive and included in diluted EPS.", "included in basic EPS."], 0, "They would not be exercised."],
 ["In calculating diluted EPS, the interest on convertible debt is:", ["added back to net income after tax.", "added back before tax.", "subtracted from net income."], 0, "If converted, the company would not pay the interest, net of the tax saving."],
 ["In calculating diluted EPS, dividends on dilutive convertible preferred shares are:", ["added back to earnings available to common shareholders.", "subtracted again.", "ignored."], 0, "If converted, no preferred dividends would be paid."],
 ["A company with a simple capital structure is least likely to have:", ["convertible bonds.", "callable bonds.", "non-convertible preferred shares."], 0, "Convertibles are potentially dilutive."],
 ["Which is not a potentially dilutive security?", ["Non-convertible preferred shares", "Warrants", "Stock options"], 0, "Only securities that could become common shares can dilute EPS."],
 ["Changes in the useful lives and residual values of assets are changes in accounting:", ["estimates and are applied prospectively.", "principles and are applied retrospectively.", "estimates and are applied retrospectively."], 0, "Estimates change future periods only."],
 ["A company changes from an incorrect accounting method to an acceptable one. This:", ["requires restatement of prior periods as a correction of an error.", "is a change in estimate applied prospectively.", "needs no disclosure."], 0, "Using an unacceptable method is an error."],
 ["The approach to revenue recognition in the converged IFRS and US GAAP standards is best described as:", ["principles-based.", "rules-based.", "objectives-based."], 0, "The standards set principles applied through five steps."],
 ["Under the revenue standards, a promise to transfer a distinct good or service is a:", ["performance obligation.", "contract.", "transaction price."], 0, "Revenue is recognized as each obligation is satisfied."],
 ["Intangible assets with indefinite lives are:", ["tested for impairment but not amortized.", "amortized over 40 years.", "expensed when acquired."], 0, "Goodwill is an example."],
 ["Capitalizing interest on assets a company constructs for its own use is required under:", ["both IFRS and US GAAP.", "IFRS only.", "US GAAP only."], 0, "Interest during construction is part of the asset's cost."],
 ["Under accrual accounting, expenses are recognized in the same period as the:", ["revenues they help generate.", "cash payment.", "invoice from the supplier."], 0, "This is the matching principle."],
 ["A firm records revenue and expenses on a sale before collecting cash. Ignoring taxes, the effect is:", ["higher assets with no change in liabilities.", "higher liabilities and lower assets.", "no effect on assets."], 0, "Receivables rise by the profit plus cost relieved; equity rises."],
 ["Diluted EPS is always:", ["less than or equal to basic EPS.", "greater than basic EPS.", "equal to basic EPS."], 0, "Antidilutive securities are excluded, so EPS cannot rise."],
 ["The first-in, first-out method best matches the physical flow of goods when customers usually take:", ["the oldest units first.", "the newest units first.", "units at random."], 0, "Perishable goods are a typical example."],
 ["Retrospective application is least likely required for:", ["a change to LIFO under US GAAP.", "a change from LIFO to FIFO.", "a change from average cost to FIFO."], 0, "Changes to LIFO are applied prospectively, because past LIFO layers cannot be reconstructed."],
])

EK["bs"] = dict(
notes="""<h3>Financial assets and liabilities</h3>
<div class="tbl"><table>
<tr><th>Category</th><th>Balance sheet value</th><th>Unrealized gains and losses</th></tr>
<tr><td>Amortized cost (IFRS) / held to maturity (US GAAP)</td><td>Amortized cost</td><td>Not recognized</td></tr>
<tr><td>FVOCI (IFRS) / available for sale (US GAAP, debt)</td><td>Fair value</td><td>Other comprehensive income</td></tr>
<tr><td>FVPL (IFRS) / trading (US GAAP)</td><td>Fair value</td><td>Income statement</td></tr>
</table></div>
<ul>
<li>Interest and dividend income go to the income statement for all categories.</li>
<li>Under US GAAP, equity securities with readily determinable fair values are measured at fair value through net income. Under IFRS, any financial asset can be designated at FVPL; equity can be irrevocably elected to FVOCI.</li>
<li>Derivatives are carried at fair value; most bonds and bank loans are carried at amortized cost.</li>
<li><b>Goodwill</b> = purchase price − fair value of identifiable net assets. It arises only in acquisitions; internally generated brands create none. For comparisons, analysts often remove goodwill from assets and equity.</li>
<li>Amortization of a bond <b>premium</b> on issued debt reduces interest expense, raising net income.</li>
<li>Under IFRS, intangibles with an active market may use the revaluation model. Research costs are expensed; development costs can be capitalized under IFRS once criteria are met.</li>
</ul>""",
qs=[
 ["Under US GAAP, a debt security classified as held to maturity is carried at:", ["amortized cost.", "historical cost.", "fair value."], 0, "Amortized cost includes the amortization of any premium or discount."],
 ["The US GAAP treatment of trading securities matches the IFRS treatment of securities measured at:", ["fair value through profit or loss.", "fair value through OCI.", "amortized cost."], 0, "Both report fair value changes in net income."],
 ["Under US GAAP, unrealized gains and losses on available-for-sale debt securities are:", ["recognized in other comprehensive income.", "recognized in the income statement.", "not recognized."], 0, "They bypass net income until sold."],
 ["Under US GAAP, unrealized gains and losses on trading securities are:", ["recognized in the income statement.", "recognized in OCI.", "not recognized."], 0, "Trading securities are marked to market through income."],
 ["Under IFRS, a firm may designate at fair value through profit or loss:", ["any financial asset.", "only equity securities.", "only derivatives."], 0, "The FVPL option is available for any financial asset."],
 ["Interest income on a debt security is recognized in the income statement when the security is classified as:", ["amortized cost, FVOCI or FVPL.", "FVPL only.", "amortized cost only."], 0, "Interest is income in every category."],
 ["Which of the following is an identifiable intangible asset?", ["A trademark", "Goodwill", "A bond investment"], 0, "Goodwill is not separately identifiable; a bond is a financial asset."],
 ["Which situation will most likely result in the largest goodwill on the balance sheet?", ["Acquiring a company with a strong brand for well above the fair value of its net assets", "Building a brand internally", "Buying equipment at fair value"], 0, "Goodwill arises only on acquisitions, as the excess paid."],
 ["Which financial liability is most likely carried at fair value?", ["A derivative liability", "A bond issued at par", "A bank loan"], 0, "Bonds and loans are usually carried at amortized cost."],
 ["Non-current liabilities such as bonds are typically reported at:", ["amortized cost.", "fair value.", "face value at maturity."], 0, "Amortized cost reflects the effective interest method."],
 ["For a company that issued bonds at a premium, amortization of the premium will most likely:", ["increase net income compared with the coupon expense.", "decrease net income.", "have no effect on net income."], 0, "Interest expense is below the coupon paid."],
 ["To compare firms with different acquisition histories, an analyst is most likely to:", ["remove goodwill from assets and equity.", "add goodwill to revenue.", "double goodwill for all firms."], 0, "This puts acquisitive and non-acquisitive firms on a similar basis."],
 ["A common-size balance sheet expresses each item as a percentage of:", ["total assets.", "sales.", "equity."], 0, "A common-size income statement uses sales."],
 ["A pharmaceutical company reporting under IFRS spends money first on initial testing and later on development after the product's feasibility is shown. It should:", ["expense the testing costs and capitalize the later development costs.", "capitalize both.", "expense both."], 0, "Research is expensed; development is capitalized once criteria are met."],
 ["A company reporting under IFRS buys an intangible asset that trades in an active market. It may:", ["use the revaluation model.", "never revalue it.", "carry it at selling price less costs."], 0, "Revaluation of intangibles requires an active market."],
])

EK["c1"] = dict(
notes="""<h3>Building and converting cash flow statements</h3>
<p class="f">CFO (indirect) = NI + non-cash charges − gains + losses − increases in operating assets + increases in operating liabilities</p>
<ul>
<li>Cash collected = sales − increase in receivables (+ increase in unearned revenue). Cash paid to suppliers = COGS + increase in inventory − increase in payables.</li>
<li>Gains on asset sales are subtracted from NI in CFO; the full sale proceeds go to CFI.</li>
<li>Depreciation appears in the indirect method only; the direct method lists cash receipts and payments.</li>
<li>US GAAP: interest and dividends received and interest paid are CFO; dividends paid are CFF. IFRS: interest and dividends received are CFO or CFI; interest and dividends paid are CFO or CFF.</li>
<li>Working capital links to CFO; non-current assets to CFI; debt and equity to CFF.</li>
<li>Non-cash transactions, such as converting bonds into shares, are disclosed but do not appear in the cash flow statement.</li>
</ul>""",
qs=[
 ["Net income is 50, depreciation 10, gain on sale of equipment 4, increase in receivables 6, decrease in inventory 3 and increase in payables 5. CFO is:", ["52", "58", "66"], 1, "50 + 10 − 4 − 6 + 3 + 5 = 58."],
 ["Sales are 800 and receivables rise from 120 to 150. Cash collected from customers is:", ["770", "800", "830"], 0, "800 − 30 = 770."],
 ["Cost of goods sold is 500, inventory rises by 20 and accounts payable rise by 15. Cash paid to suppliers is:", ["465", "505", "535"], 1, "500 + 20 − 15 = 505."],
 ["A company buys equipment for 120 and sells old equipment with a book value of 25 for 30. Its CFI is:", ["−95", "−90", "−65"], 1, "−120 + 30 = −90. The gain of 5 is not added again."],
 ["Under US GAAP, a company issues bonds for 100, repays a loan of 40 and pays dividends of 20. Its CFF is:", ["40", "60", "160"], 0, "100 − 40 − 20 = 40."],
 ["If sales exceed cash collections, accounts receivable will:", ["increase.", "decrease.", "stay the same."], 0, "Uncollected sales build up receivables."],
 ["A decrease in receivables and an increase in payables will:", ["both increase CFO.", "both decrease CFO.", "offset each other."], 0, "Both free up cash."],
 ["When a gain on the sale of an asset is recognized, in the indirect method the analyst should:", ["subtract the gain from net income.", "add the gain to net income.", "include the gain in CFF."], 0, "The cash proceeds are reported in CFI."],
 ["Under US GAAP, dividends paid are classified as:", ["financing cash flows.", "operating cash flows.", "investing cash flows."], 0, "IFRS allows CFO or CFF."],
 ["Under IFRS, interest paid may be classified as:", ["operating or financing.", "investing only.", "operating only."], 0, "IFRS gives a choice; US GAAP requires operating."],
 ["Under IFRS, which classification of interest received is permitted?", ["Operating or investing", "Financing only", "Operating only"], 0, "Interest and dividends received may be CFO or CFI."],
 ["Which balance sheet accounts are most closely linked to operating cash flows?", ["Working capital accounts", "Non-current assets", "Long-term debt"], 0, "Changes in receivables, inventory and payables adjust NI to CFO."],
 ["The conversion of bonds into common shares is reported:", ["as a non-cash transaction in the notes.", "in CFF.", "in CFI."], 0, "No cash changes hands."],
 ["To convert the indirect method to the direct method for cash paid to suppliers, an analyst would:", ["add increases in inventory to COGS.", "subtract increases in inventory from COGS.", "add depreciation to COGS."], 0, "Buying more inventory uses cash."],
 ["Depreciation expense appears in the cash flow statement under:", ["the indirect method only.", "the direct method only.", "both methods."], 0, "It is added back to NI because it is non-cash."],
 ["An increase in accounts payable in the indirect method is:", ["added to net income.", "subtracted from net income.", "reported in CFF."], 0, "The company used less cash than its expenses suggest."],
 ["Prepaid insurance falls from 650 to 475 during the year. In the indirect method, this change is:", ["added to net income.", "subtracted from net income.", "ignored."], 0, "A fall in a prepaid asset means expense exceeded cash paid."],
])

EK["c2"] = dict(
notes="""<h3>More on cash flow analysis</h3>
<p class="f">FCFF = CFO + interest × (1 − t) − fixed capital investment · FCFE = CFO − fixed capital investment + net borrowing</p>
<ul>
<li>Common-size cash flow statements show each item as a percentage of <b>revenue</b>, or each inflow as a percentage of total inflows and each outflow as a percentage of total outflows.</li>
<li><b>Reinvestment ratio</b> = CFO / cash paid for long-term assets; <b>debt coverage</b> = CFO / total debt; <b>cash return on assets</b> = CFO / average total assets.</li>
<li>Stretching payables (a falling payables turnover) raises CFO, not CFF, and is not a sustainable source of cash.</li>
</ul>""",
qs=[
 ["CFO is 300, interest paid is 40, the tax rate is 25% and capital expenditure is 120. FCFF is:", ["180", "210", "220"], 1, "300 + 40 × 0.75 − 120 = 210."],
 ["CFO is 300, capital expenditure 120 and net borrowing 50. FCFE is:", ["130", "180", "230"], 2, "300 − 120 + 50 = 230."],
 ["A ratio that measures a firm's ability to buy long-term assets with operating cash is the:", ["reinvestment ratio.", "cash return on assets.", "debt coverage ratio."], 0, "It divides CFO by cash spent on long-term assets."],
 ["A falling accounts payable turnover most likely affects a company's cash flows by:", ["increasing CFO, which is not sustainable.", "increasing CFF, which is sustainable.", "decreasing CFO."], 0, "Delaying payments to suppliers boosts operating cash only temporarily."],
 ["A common-size cash flow statement is least likely to show each item as a percentage of:", ["total equity.", "revenue.", "total cash inflows or outflows."], 0, "The two accepted approaches use revenue or total flows."],
 ["CFO is 20 and the company buys equipment for 5 and sells equipment for 3. Its free cash flow available before financing is closest to:", ["18", "22", "25"], 0, "20 − 5 + 3 = 18."],
])

EK["iv"] = dict(
notes="""<h3>More on inventories</h3>
<ul>
<li>Rising prices and stable or rising quantities: LIFO gives higher COGS, lower inventory, lower gross profit and net income, lower taxes and so higher CFO than FIFO. Falling prices reverse this. Weighted average lies between.</li>
<li>FIFO gives the best balance sheet value (recent costs); LIFO gives the best income statement measure (current costs).</li>
<li>FIFO inventory = LIFO inventory + LIFO reserve. FIFO COGS = LIFO COGS − increase in LIFO reserve.</li>
<li>IFRS: lower of cost and <b>net realizable value</b> (selling price − completion and selling costs); write-downs can be reversed and the circumstances disclosed. US GAAP: lower of cost and NRV for FIFO and average cost; lower of cost or market for LIFO; no reversals.</li>
<li>A write-down lowers inventory and equity, raises COGS in the period, and raises later turnover ratios and ROA. It does not affect the quick ratio (inventory is excluded).</li>
<li>Changes to LIFO under US GAAP are applied prospectively. Pledged inventory must be disclosed.</li>
<li>Rising finished goods with falling raw materials may signal weak demand; rising raw materials may signal expected higher sales.</li>
</ul>""",
qs=[
 ["When prices are falling, compared with LIFO, FIFO results in:", ["higher COGS and lower gross profit.", "lower COGS and higher gross profit.", "the same COGS."], 0, "The older units sold first are the more expensive ones."],
 ["During rising prices and stable inventory levels, the inventory method that gives the most informative income statement is:", ["LIFO.", "FIFO.", "weighted average."], 0, "LIFO matches current costs with current revenue."],
 ["A company has LIFO inventory of 400 and a LIFO reserve of 60. Its FIFO inventory is:", ["340", "400", "460"], 2, "FIFO = LIFO + reserve."],
 ["LIFO COGS is 1,000 and the LIFO reserve rises from 50 to 60. FIFO COGS is:", ["940", "990", "1,010"], 1, "FIFO COGS = LIFO COGS − increase in reserve = 1,000 − 10."],
 ["Under IFRS, inventory costs 720,000, its expected selling price is 760,000 and costs to complete and sell are 70,000. The write-down is:", ["0", "30,000", "40,000"], 1, "NRV = 690,000; 720,000 − 690,000."],
 ["Which standards require a firm to disclose the circumstances of reversing an inventory write-down?", ["IFRS only", "US GAAP only", "Both"], 0, "US GAAP does not permit reversals."],
 ["In periods of rising prices and stable quantities, a LIFO firm will report, compared with a FIFO firm:", ["lower taxes and higher operating cash flow.", "higher taxes and lower operating cash flow.", "higher net income."], 0, "Higher COGS lowers taxable income."],
 ["An inventory write-down to net realizable value will most likely cause total asset turnover to:", ["increase.", "decrease.", "remain unchanged."], 0, "Assets fall while sales are unchanged."],
 ["An inventory write-down will most likely affect the quick ratio by:", ["having no effect.", "decreasing it.", "increasing it."], 0, "Inventory is excluded from the quick ratio."],
 ["The effect of an inventory write-down on return on assets is most likely:", ["lower in the current period and higher in later periods.", "higher in the current period.", "no effect in any period."], 0, "The loss hits current income; later periods have smaller assets."],
 ["A US GAAP firm changes from weighted average cost to LIFO. It must apply the change:", ["prospectively.", "retrospectively.", "only to new purchases of other products."], 0, "Earlier LIFO layers cannot be reconstructed."],
 ["During periods of rising prices and stable quantities, compared with LIFO firms, FIFO firms will have:", ["higher shareholders' equity.", "lower inventory.", "lower gross margins."], 0, "Higher inventory and higher retained earnings."],
 ["Which trend most likely indicates higher future earnings?", ["Raw materials and work in progress rising while finished goods fall", "Finished goods rising while raw materials fall", "Inventory turnover falling"], 0, "The firm is building production to meet strong demand."],
 ["A firm that pledges inventory as collateral for a loan must:", ["disclose the carrying amount pledged.", "remove the inventory from its balance sheet.", "offset it against the loan."], 0, "Disclosure is required."],
 ["If prices are rising, weighted average cost gives inventory values that are higher than under:", ["LIFO.", "FIFO.", "specific identification."], 0, "Average cost lies between LIFO and FIFO."],
 ["During declining prices, which method gives the highest net income?", ["LIFO", "FIFO", "Weighted average"], 0, "LIFO charges the newest, cheapest costs to COGS."],
])

EK["lt"] = dict(
terms=[
 ["Average age of assets", "Varlıkların ortalama yaşı", "Accumulated depreciation divided by annual depreciation expense.", "Birikmiş amortismanın yıllık amortisman giderine bölünmesi."],
 ["Remaining useful life", "Kalan faydalı ömür", "Net PP&E divided by annual depreciation expense.", "Net maddi duran varlıkların yıllık amortisman giderine bölünmesi."],
],
notes="""<h3>More on long-term assets</h3>
<p class="f">average age = accumulated depreciation / depreciation expense · remaining life = net PP&E / depreciation expense · total life = gross PP&E / depreciation expense</p>
<ul>
<li>Average age helps estimate when major capital spending will be needed.</li>
<li>Capitalizing rather than expensing: higher assets and equity at first, higher income in the first year, lower income later, <b>higher CFO and lower CFI</b>, smoother earnings.</li>
<li>Internally developed intangibles (trademarks, brands) are usually expensed, so they rarely appear on the balance sheet. Acquired patents and franchise rights with finite lives are amortized; renewable trademarks may have indefinite lives.</li>
<li>Software for sale under US GAAP: costs are expensed until technological feasibility, then capitalized.</li>
<li>IFRS impairment: carrying amount above <b>recoverable amount</b> (higher of fair value less costs to sell and value in use). Impairment lowers assets and equity, raises debt-to-equity, lowers future depreciation and raises future ROA. It does not affect cash.</li>
<li>Upward revaluation (IFRS) raises assets and equity, lowers leverage, and raises later depreciation.</li>
</ul>""",
qs=[
 ["A company's accumulated depreciation is 400 and its annual depreciation expense is 50. The average age of its PP&E is:", ["8 years", "12 years", "20 years"], 0, "400 / 50 = 8."],
 ["The ratio of net PP&E to annual depreciation expense best estimates:", ["remaining useful life.", "average age.", "total useful life."], 0, "Net PP&E is the undepreciated part."],
 ["An analyst uses the average age of a firm's depreciable assets mainly to estimate its:", ["near-term capital spending needs.", "cash taxes.", "dividend capacity."], 0, "Old assets will soon need replacing."],
 ["Under IFRS, an asset has a carrying amount of 900, fair value less costs to sell of 760 and value in use of 820. The impairment loss is:", ["0", "80", "140"], 1, "Recoverable amount is the higher of 760 and 820."],
 ["An impairment write-down is least likely to decrease a company's:", ["debt-to-equity ratio.", "assets.", "future depreciation."], 0, "Lower equity raises debt-to-equity."],
 ["An impairment of long-lived assets will result in:", ["higher future return on assets.", "a lower debt-to-equity ratio.", "higher operating cash flow in the year."], 0, "Assets are smaller, and later depreciation is lower."],
 ["Compared with expensing, capitalizing an expenditure will most likely result in:", ["higher CFO and lower CFI.", "lower CFO and higher CFI.", "no difference in cash flow classification."], 0, "The outflow is classified as investing."],
 ["Which intangible asset is most likely amortized?", ["A purchased franchise right with a two-year life", "Goodwill", "A trademark renewable at little cost"], 0, "Finite-life intangibles are amortized."],
 ["The amortized cost of a trademark is least likely to appear on the balance sheet if the trademark was:", ["developed internally.", "acquired in a business combination.", "bought from another company."], 0, "Costs of internally developed trademarks are expensed."],
 ["Under US GAAP, costs of developing software for sale are:", ["expensed until technological feasibility, then capitalized.", "always capitalized.", "always expensed."], 0, "Feasibility is the trigger for capitalization."],
 ["A firm revalues its long-lived assets upward under IFRS. Which effect is least likely?", ["Higher leverage ratios", "Higher equity", "Higher depreciation in later years"], 0, "Higher equity lowers leverage."],
 ["Which item is least likely an intangible asset with an indefinite life?", ["An acquired patent", "Goodwill", "A trademark renewable indefinitely"], 0, "Patents have legal lives."],
])

EK["ll"] = dict(
notes="""<h3>More on leases and pensions</h3>
<ul>
<li>Lessees (IFRS 16 and US GAAP) record a right-of-use asset and a lease liability equal to the <b>present value of lease payments</b>, except for short-term or low-value leases. Principal repayment is a <b>financing</b> cash outflow.</li>
<li>Finance lease criteria include: ownership transfers, purchase option likely to be exercised, lease term covers most of the asset's life, PV of payments equals substantially all of fair value, or a specialized asset.</li>
<li>Lessor, finance lease: remove the asset, record a lease receivable, recognize interest income (and any selling profit). Lessor, operating lease: keep and depreciate the asset, recognize lease income.</li>
<li>Reasons to lease: less cash upfront, flexibility, lower risk of obsolescence. Benefit from appreciation is a reason to buy.</li>
<li>Defined benefit plans: the funded status (fair value of plan assets minus obligation) is recognized on the balance sheet as a net asset or liability. Defined contribution plans create no such item.</li>
<li>Share-based compensation is expensed over the <b>vesting period</b> under both IFRS and US GAAP, based on grant-date fair value.</li>
</ul>""",
qs=[
 ["A company leases equipment for five years with annual payments of $20,000 at the end of each year. The discount rate is 6%. The initial lease liability is closest to:", ["$84,250", "$94,200", "$100,000"], 0, "PV of a five-year annuity of 20,000 at 6% = 84,247."],
 ["For the lease above, the interest expense in Year 1 is closest to:", ["$5,055", "$6,000", "$14,945"], 0, "84,247 × 6% = 5,055; the rest of the payment reduces principal."],
 ["For a lessee, the principal part of a lease payment is a cash flow from:", ["financing activities.", "operating activities.", "investing activities."], 0, "It repays the lease liability."],
 ["The least likely reason for leasing rather than buying an asset is to:", ["benefit from the asset's appreciation.", "conserve cash.", "reduce the risk of obsolescence."], 0, "The owner keeps any gain in value."],
 ["A lessor that enters into a finance lease is least likely to:", ["keep the leased asset on its balance sheet.", "record a lease receivable.", "recognize interest income."], 0, "The asset is derecognized."],
 ["For an operating lease, the leased asset appears on the balance sheet of the:", ["lessor.", "lessee only.", "neither party."], 0, "The lessee records a right-of-use asset, but the physical asset stays with the lessor."],
 ["When the risks of ownership are not substantially transferred, a lessor most likely classifies the lease as:", ["an operating lease.", "a finance lease.", "a sales-type lease."], 0, "Finance leases transfer substantially all risks and rewards."],
 ["A lease is most likely a finance lease when:", ["the present value of payments equals substantially all of the asset's fair value.", "the lease term is short.", "the lessee cannot buy the asset."], 0, "This is one of the classification criteria."],
 ["The difference between a defined benefit plan's assets and its obligation is reported as:", ["a net pension asset or liability.", "an expense.", "an actuarial gain."], 0, "The funded status appears on the balance sheet."],
 ["An employer with both defined benefit and defined contribution plans is most likely to show a pension liability for the:", ["defined benefit plan only.", "defined contribution plan only.", "both plans."], 0, "DC plans have no promise beyond the contribution."],
 ["Share-based compensation is expensed over the vesting period under:", ["both IFRS and US GAAP.", "IFRS only.", "US GAAP only."], 0, "The cost is spread over the service period."],
 ["A lessee initially records a lease liability equal to:", ["the present value of the lease payments.", "the sum of the lease payments.", "the asset's fair value."], 0, "Payments are discounted."],
])

EK["tx"] = dict(
notes="""<h3>More on income taxes</h3>
<p class="f">income tax expense = taxes payable + ΔDTL − ΔDTA</p>
<ul>
<li>Accelerated tax depreciation creates a <b>DTL</b>; expenses recognized in the accounts before they are deductible (warranties, R&D amortized for tax) and tax losses carried forward create a <b>DTA</b>.</li>
<li>Effective tax rate = income tax expense / pretax income. Cash tax rate = taxes paid / pretax income.</li>
<li>Permanent differences (non-deductible expenses, tax-exempt income, tax credits) cause effective and statutory rates to differ; they create no deferred taxes.</li>
<li>Under the liability method, a fall in the tax rate lowers both DTL and DTA.</li>
<li>A <b>valuation allowance</b> (US GAAP) reduces DTAs that are unlikely to be realized.</li>
<li>For analysis, a DTL not expected to reverse is treated as <b>equity</b>; otherwise as a liability. Some DTLs are best ignored if the timing is uncertain.</li>
<li>Under IFRS, deferred taxes are non-current.</li>
</ul>""",
qs=[
 ["A firm uses accelerated depreciation for tax and straight-line for reporting. Which result is least likely in the early years?", ["A deferred tax asset", "Taxes payable below income tax expense", "A deferred tax liability"], 0, "Tax depreciation is higher, so taxable income and taxes payable are lower, creating a DTL."],
 ["A tax loss carryforward most likely creates a:", ["deferred tax asset.", "deferred tax liability.", "permanent difference."], 0, "It will reduce future taxes."],
 ["The ratio of income tax expense to pretax income is the:", ["effective tax rate.", "cash tax rate.", "statutory tax rate."], 0, "The cash tax rate uses taxes paid."],
 ["Pretax income is $150,000, tax expense $47,000 and taxes paid $44,000. The effective tax rate is closest to:", ["29.3%", "30.0%", "31.3%"], 2, "47/150 = 31.3%; 29.3% is the cash tax rate."],
 ["Taxes payable are $2,500 and the DTL increased by $500 with no change in DTAs. Income tax expense is:", ["$2,000", "$2,500", "$3,000"], 2, "Expense = payable + ΔDTL."],
 ["Equipment costing 30,000 is depreciated over three years straight-line for reporting and 15,000 in Year 1 for tax. The tax rate is 25%. The DTL at the end of Year 1 is:", ["1,250", "2,500", "3,750"], 0, "Difference 15,000 − 10,000 = 5,000 × 25%."],
 ["A charitable donation is expensed in the accounts but is never deductible for tax. This creates:", ["a permanent difference.", "a deferred tax asset.", "a deferred tax liability."], 0, "It will never reverse."],
 ["Under the liability method, a decrease in the tax rate will:", ["decrease both DTL and DTA balances.", "increase DTL and decrease DTA.", "have no effect on deferred tax balances."], 0, "Balances are remeasured at the new rate."],
 ["A valuation allowance is created when:", ["it is likely that some deferred tax assets will not be realized.", "DTLs exceed DTAs.", "tax rates rise."], 0, "It reduces the DTA to the amount expected to be used."],
 ["If a DTL is not expected to reverse, an analyst should most appropriately treat it as:", ["equity.", "a current liability.", "an asset."], 0, "It will never be paid."],
 ["Which item is most likely to create a deferred tax asset?", ["Warranty expense recognized before it is deductible", "Accelerated tax depreciation", "Tax-exempt interest income"], 0, "Book expense ahead of tax deduction means higher taxes now."],
 ["Which is most likely to cause the effective tax rate to differ from the statutory rate?", ["Tax-exempt income", "A deferred tax liability from depreciation", "A warranty reserve"], 0, "Temporary differences change deferred taxes, not the effective rate."],
 ["A firm expenses all R&D in its accounts, but tax rules require R&D to be capitalized and amortized. In the first year, this creates a:", ["deferred tax asset.", "deferred tax liability.", "permanent difference."], 0, "Taxable income exceeds accounting profit."],
 ["Which ratio is least likely affected by whether deferred taxes are treated as a liability or as equity?", ["Gross profit margin", "Debt-to-equity ratio", "Return on equity"], 0, "Gross margin uses only sales and COGS."],
])

EK["rq"] = dict(
notes="""<h3>More on reporting quality</h3>
<ul>
<li>Quality spectrum, from best: GAAP-compliant and decision-useful with sustainable, adequate earnings; GAAP-compliant and decision-useful but low earnings quality; GAAP-compliant but biased choices; GAAP-compliant but managed earnings; non-compliant accounting; fictitious transactions.</li>
<li>If financial reports are of low quality, users cannot assess earnings quality.</li>
<li>Earnings quality refers to <b>sustainability</b> and adequacy of returns. Reporting quality refers to compliance and decision usefulness.</li>
<li>Conditions for low quality: <b>motivation, opportunity, rationalization</b>. Motivations include meeting forecasts, debt covenants and compensation tied to results.</li>
<li>Discipline: regulators, auditors, private contracts (lenders); in the US, CEO and CFO certification.</li>
<li>Warning signs: revenue growing faster than receivables collection, CFO well below net income, capitalized operating costs (raises CFO), longer useful lives or higher salvage values, unusual rises in days payable, emphasis on non-GAAP measures.</li>
<li>A non-GAAP measure under IFRS must be reconciled to the nearest IFRS measure, explained and not given more prominence.</li>
<li>Conservative choices can also lower quality, for example 'cookie jar' reserves to smooth future earnings.</li>
</ul>""",
qs=[
 ["Which represents the highest point on the reporting quality spectrum?", ["GAAP-compliant, decision-useful reports with sustainable and adequate earnings", "GAAP-compliant reports with biased accounting choices", "GAAP-compliant reports with managed earnings"], 0, "Both reporting and earnings quality are high."],
 ["Compared with a firm that expenses recurring maintenance, a firm that capitalizes it will report higher:", ["operating cash flow.", "investing cash flow.", "financing cash flow."], 0, "The outflow moves to investing."],
 ["The conditions that make low-quality reporting likely are best described as:", ["motivation, opportunity and rationalization.", "pressure, profit and power.", "weak markets, strong auditors and regulation."], 0, "This is the fraud triangle."],
 ["A characteristic of a firm's earnings quality is:", ["sustainability.", "completeness.", "relevance."], 0, "Completeness and relevance relate to reporting quality."],
 ["An IFRS-reporting firm that presents a non-IFRS measure is least likely required to:", ["have the measure separately audited.", "reconcile it to the closest IFRS measure.", "explain why it is useful."], 0, "Reconciliation and explanation are required."],
 ["Which requirement most likely gives management an incentive to manipulate earnings?", ["Debt covenants", "Disclosure rules", "Audit requirements"], 0, "Breaching covenants can be costly."],
 ["The quality of reported earnings is low when they:", ["are not sustainable.", "are lower than last year's.", "are reported under IFRS."], 0, "Earnings quality is about whether results can continue."],
 ["A significant increase in days payable above historical levels is most likely a sign of:", ["unsustainable operating cash flow.", "higher net working capital.", "stronger earnings quality."], 0, "Stretching payables boosts CFO temporarily."],
 ["If financial reports are of low quality, users:", ["cannot reliably assess earnings quality.", "can still fully assess earnings quality.", "should rely on non-GAAP measures."], 0, "Unreliable reports hide the true performance."],
 ["To increase current earnings, management is least likely to:", ["shorten assets' useful lives.", "raise salvage values.", "lower the bad debt allowance."], 0, "Shorter lives increase depreciation."],
 ["Management is most likely to make conservative choices that reduce reporting quality when:", ["it wants to build reserves to boost future earnings.", "it needs to meet this year's analyst forecast.", "it is about to issue new shares."], 0, "This creates 'cookie jar' reserves."],
 ["A mechanism that disciplines reporting quality for US-traded securities but not typically elsewhere is:", ["certification of financial statements by the CEO and CFO.", "external audit.", "regulatory review."], 0, "US law requires this certification."],
 ["An analyst would most likely suspect deteriorating earnings quality if:", ["operating cash flow is consistently well below net income.", "receivables fall relative to sales.", "inventory turnover rises."], 0, "Earnings not backed by cash may not be sustainable."],
])

EK["ra"] = dict(
notes="""<h3>Ratio formulas</h3>
<p class="f">current = CA / CL · quick = (cash + marketable securities + receivables) / CL · cash = (cash + marketable securities) / CL</p>
<p class="f">CCC = DSO + DOH − DPO · DSO = 365 / receivables turnover · DOH = 365 / inventory turnover · DPO = 365 / payables turnover</p>
<p class="f">ROE = NI/sales × sales/assets × assets/equity = tax burden × interest burden × EBIT margin × asset turnover × equity multiplier</p>
<ul>
<li>Tax burden = NI/EBT; interest burden = EBT/EBIT; interest coverage = EBIT / interest.</li>
<li>Purchases = COGS + ending inventory − beginning inventory.</li>
<li>Paying a current liability with cash raises the current ratio when it is above 1; buying inventory with short-term debt lowers it. Collecting receivables leaves the current ratio unchanged and raises the cash ratio.</li>
<li>Higher asset turnover raises ROE only if other components do not offset it. A higher debt-to-equity ratio raises ROE only if ROA exceeds the cost of debt.</li>
<li>Industry-specific ratios: net interest margin for banks, sales per square metre for retailers.</li>
<li>Comparing with peers is <b>cross-sectional</b> analysis; over time is <b>time-series</b> analysis. Limitations: differences in accounting methods, finding comparable firms, judging target values.</li>
<li>The coefficient of variation of operating income measures business risk.</li>
</ul>""",
qs=[
 ["A company's receivables turnover is 10, inventory turnover 5 and payables turnover 12. Its cash conversion cycle is closest to:", ["79 days", "100 days", "140 days"], 0, "36.5 + 73.0 − 30.4 = 79.1."],
 ["A company's net profit margin is 5%, asset turnover 2.5 and ROE 18%. Its equity multiplier is:", ["0.69", "1.44", "2.50"], 1, "18% / (5% × 2.5) = 1.44."],
 ["A company's tax burden is 0.75, interest burden 0.80, EBIT margin 15%, asset turnover 1.2 and equity multiplier 2.0. Its ROE is:", ["10.8%", "18.0%", "21.6%"], 2, "0.75 × 0.80 × 0.15 × 1.2 × 2.0 = 21.6%."],
 ["In the five-part DuPont equation, EBT/EBIT is the:", ["interest burden.", "tax burden.", "operating margin."], 0, "It shows how much of operating profit is left after interest."],
 ["The quick ratio differs from the current ratio by excluding:", ["inventory.", "marketable securities.", "receivables."], 0, "Inventory is the least liquid current asset."],
 ["A company's operating profit is $100,000 and interest expense $25,000. Its interest coverage ratio is:", ["3.0", "4.0", "5.0"], 1, "100 / 25 = 4."],
 ["Annual sales are $250,000 and average receivables $50,000. The average collection period is closest to:", ["37 days", "73 days", "146 days"], 1, "Turnover 5; 365/5 = 73 days."],
 ["Cost of goods sold is $650,000 and average inventory $130,000. Days of inventory on hand are closest to:", ["37 days", "56 days", "73 days"], 2, "Turnover 5.0; 365/5 = 73."],
 ["A company uses short-term bank debt to buy inventory. If its current ratio was above 1, the ratio will:", ["decrease.", "increase.", "stay the same."], 0, "Equal increases to CA and CL lower a ratio above 1."],
 ["Collecting accounts receivable will most likely:", ["leave the current ratio unchanged and raise the cash ratio.", "raise both ratios.", "lower the cash ratio."], 0, "One current asset becomes another, but cash rises."],
 ["Comparing a company's ratios with those of its competitors is:", ["cross-sectional analysis.", "time-series analysis.", "horizontal analysis."], 0, "Time-series analysis compares a company with its own past."],
 ["An analyst comparing two retailers would most likely use:", ["sales per square metre.", "net interest margin.", "loss ratio."], 0, "Net interest margin is for banks; loss ratio for insurers."],
 ["An analyst is most likely to calculate net interest margin when analysing:", ["banks.", "retailers.", "manufacturers."], 0, "It measures interest income less interest expense relative to earning assets."],
 ["Which ratio is part of the original three-part DuPont equation?", ["Asset turnover", "Debt-to-equity", "Interest coverage"], 0, "ROE = net margin × asset turnover × equity multiplier."],
 ["A company's ROE is 12% and its net income $10 million. Its equity is:", ["$1.2 million", "$83.3 million", "$120 million"], 1, "10 / 0.12 = 83.3 million."],
 ["A firm's average days of receivables are 22 compared with an industry average of 29. An analyst would most likely conclude that the firm:", ["collects faster, possibly with a stricter credit policy.", "has weaker collections.", "sells more on credit."], 0, "Fewer days means faster collection."],
 ["If a firm's asset turnover rises with other factors held constant, its ROE will:", ["rise.", "fall.", "stay the same."], 0, "With other components unchanged, higher turnover raises ROE."],
 ["The coefficient of variation of operating income across two firms in the same industry most likely helps an analyst assess:", ["business risk.", "liquidity.", "valuation."], 0, "It measures the variability of operating results."],
 ["A company's quick ratio is 2.0. An equal decrease in inventory and accounts payable will:", ["increase the quick ratio.", "decrease the quick ratio.", "leave it unchanged."], 0, "Inventory is not in the numerator, but current liabilities fall."],
 ["Revenue divided by average working capital is a(n):", ["activity ratio.", "solvency ratio.", "liquidity ratio."], 0, "Working capital turnover measures efficiency."],
 ["Average total assets divided by average total equity is a:", ["solvency ratio.", "liquidity ratio.", "profitability ratio."], 0, "The financial leverage ratio measures the use of debt."],
 ["Which is least likely a valid limitation of ratio analysis?", ["Ratios can be calculated from published data.", "Different accounting methods reduce comparability.", "It is hard to find comparable companies."], 0, "Availability of data is a strength."],
 ["A company has a cash conversion cycle of 80 days. Its receivables turnover rises from 11 to 12. Its cash conversion cycle will:", ["fall.", "rise.", "stay the same."], 0, "DSO falls from 33.2 to 30.4 days."],
])

EK["fm"] = dict(
notes="""<h3>More on financial statement modelling</h3>
<ul>
<li>A sales-based pro forma model starts with the <b>revenue forecast</b>, then COGS, operating costs, working capital, capex and financing.</li>
<li>Raising the price of a product with <b>elastic</b> demand lowers revenue; with inelastic demand it raises revenue.</li>
<li>Pricing power is greatest with low threat of substitutes, low buyer and supplier power and high barriers to entry. The threat of substitutes has the largest effect on demand elasticity.</li>
<li>Behavioural biases: overconfidence (use scenarios), illusion of control (include only variables with proven explanatory power), conservatism (small updates despite large news), representativeness (consider base rates, both inside and outside views), confirmation (seek contrary evidence).</li>
<li>Forecast horizon for a cyclical company: long enough to cover a full cycle and reach a normal state. For a buy-side analyst, the horizon can match the portfolio's holding period (inverse of turnover).</li>
<li>In DCF models, terminal value assumptions (long-term growth) have the largest effect.</li>
<li>Inflection points: new technology, regulation, demographic shifts.</li>
<li>Cutting advertising to protect margins can hurt long-term sales.</li>
</ul>""",
qs=[
 ["An analyst trying to reduce representativeness bias would most likely:", ["consider both inside and outside views, including base rates.", "only use the company's own history.", "rely on a single detailed scenario."], 0, "Base rates counter the tendency to over-weight a story."],
 ["What is the most likely effect on revenue of raising the price of a product with elastic demand?", ["Revenue falls.", "Revenue rises.", "Revenue is unchanged."], 0, "Quantity falls by a larger percentage than the price rises."],
 ["An analyst creating a sales-based pro forma model will most likely begin by:", ["forecasting revenue.", "forecasting working capital.", "forecasting financing needs."], 0, "Other items are linked to revenue."],
 ["An analyst who includes only variables with known explanatory power in a model is most likely trying to avoid:", ["illusion of control bias.", "conservatism bias.", "representativeness bias."], 0, "Adding many variables gives a false sense of precision."],
 ["A company is most likely to have pricing power in an industry with high:", ["barriers to entry.", "bargaining power of customers.", "threat of substitutes."], 0, "Few competitors can enter to undercut prices."],
 ["An analyst who makes only small changes to a forecast despite information pointing to a big change most likely shows:", ["conservatism bias.", "overconfidence bias.", "illusion of control."], 0, "Beliefs are updated too slowly."],
 ["For a highly cyclical company, the most appropriate forecast horizon is one that:", ["covers a full business cycle.", "ends at the next peak.", "covers only the next year."], 0, "A full cycle shows normalized results."],
 ["In a discounted cash flow valuation, a small change in which estimate most likely has the largest effect on value?", ["Long-term growth rate", "Next year's capital spending", "Next quarter's tax rate"], 0, "Terminal value is usually most of the total."],
 ["Which element of Porter's five forces most likely has the largest effect on demand elasticity?", ["Threat of substitutes", "Threat of new entrants", "Supplier power"], 0, "Customers switch more easily when substitutes exist."],
 ["A portfolio has 25% annual turnover. A buy-side analyst would most likely forecast over a horizon of about:", ["four years.", "one year.", "ten years."], 0, "Average holding period ≈ 1 / turnover."],
 ["A firm cuts advertising to maintain margins after its input costs rise. The most likely risk is:", ["lower future sales.", "higher future tax rates.", "higher inventory turnover."], 0, "Less marketing may weaken demand."],
 ["Which is most likely to signal an inflection point in a company's forecast?", ["A major change in regulation", "A routine dividend payment", "A seasonal rise in sales"], 0, "Inflection points break past trends."],
])

# Doğru şıkların çoğu ilk sıraya yazıldığı için, sayı içermeyen sorularda yerlerini sırayla A/B/C'ye dağıt.
_n = 0
for _e in EK.values():
    for _q in _e.get("qs", []):
        if any(_re.search(r"\d", _x) for _x in _q[1]): continue
        _j = _n % 3; _o = _q[1]; _i = _q[2]
        _o[_i], _o[_j] = _o[_j], _o[_i]; _q[2] = _j; _n += 1
