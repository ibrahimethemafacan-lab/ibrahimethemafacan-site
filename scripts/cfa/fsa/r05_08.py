# CFA Level I · Financial Statement Analysis · readings 5–8. Original study notes and questions.
R = []

R.append(dict(id="c2", n="Analyzing Statements of Cash Flows II", k="FREE CASH", w=2, c="#b8860b",
terms=[
 ["Free cash flow to the firm (FCFF)", "Firmaya serbest nakit akışı", "Cash available to all providers of capital after operating costs and investment in fixed and working capital.", "Faaliyet giderleri ile sabit ve işletme sermayesi yatırımlarından sonra tüm sermaye sağlayanlara kalan nakit."],
 ["Free cash flow to equity (FCFE)", "Özkaynağa serbest nakit akışı", "Cash available to ordinary shareholders after investment and after payments to and from lenders.", "Yatırımlardan ve kreditörlerle yapılan ödemelerden sonra adi pay sahiplerine kalan nakit."],
 ["Fixed capital investment", "Sabit sermaye yatırımı", "Net spending on long-term assets such as property, plant and equipment.", "Maddi duran varlıklar gibi uzun vadeli varlıklara yapılan net harcama."],
 ["Net borrowing", "Net borçlanma", "New debt issued minus debt repaid in the period.", "Dönemde ihraç edilen yeni borçtan geri ödenen borcun çıkarılmasıyla bulunan tutar."],
 ["Common-size cash flow statement", "Dikey yüzde nakit akış tablosu", "A cash flow statement with each item shown as a percentage of revenue, or of total inflows or outflows.", "Her kalemin hasılatın ya da toplam giriş veya çıkışların yüzdesi olarak gösterildiği nakit akış tablosu."],
 ["Cash flow to revenue", "Nakit akışı/hasılat oranı", "Operating cash flow divided by revenue.", "Faaliyet nakit akışının hasılata bölümü."],
 ["Cash return on assets", "Varlıkların nakit getirisi", "Operating cash flow divided by average total assets.", "Faaliyet nakit akışının ortalama toplam varlıklara bölümü."],
 ["Debt coverage ratio", "Borç karşılama oranı", "Operating cash flow divided by total debt.", "Faaliyet nakit akışının toplam borca bölümü."],
 ["Reinvestment ratio", "Yeniden yatırım oranı", "Operating cash flow divided by cash paid for long-term assets.", "Faaliyet nakit akışının uzun vadeli varlıklar için ödenen nakde bölümü."],
 ["Quality of earnings", "Kazanç kalitesi", "The degree to which reported profit is backed by cash and is likely to continue.", "Raporlanan kârın nakitle desteklenme ve sürdürülebilir olma derecesi."],
],
notes="""<h3>Reading the cash flow statement</h3>
<ul>
<li>Start with the big picture: which of the three sections provide cash and which use it?</li>
<li>A healthy mature company funds its investment and its payments to capital providers from <b>operating</b> cash flow.</li>
<li>A growing company may have negative operating cash flow funded by financing; this is sustainable only for a time.</li>
<li>Positive cash flow from selling assets or from continual borrowing is not a lasting source.</li>
</ul>
<h3>Operating cash flow and earnings</h3>
<ul>
<li>Compare operating cash flow with net income. Profit that is persistently higher than operating cash flow suggests aggressive accruals and low <b>quality of earnings</b>.</li>
<li>Look at what drives changes: rising receivables or inventory relative to sales may signal collection or demand problems.</li>
</ul>
<h3>Common-size cash flow statements</h3>
<ul>
<li>Method 1: each item as a percentage of <b>revenue</b>. Useful for forecasting.</li>
<li>Method 2: each inflow as a percentage of total inflows and each outflow as a percentage of total outflows.</li>
</ul>
<h3>Free cash flow</h3>
<p class="f">FCFF = CFO + interest × (1 − tax rate) − fixed capital investment</p>
<p class="f">FCFF = net income + non-cash charges + interest × (1 − tax rate) − fixed capital investment − working capital investment</p>
<p class="f">FCFE = CFO − fixed capital investment + net borrowing</p>
<p class="f">FCFE = FCFF − interest × (1 − tax rate) + net borrowing</p>
<ul>
<li>Interest is added back in FCFF because it is a payment to a capital provider and was deducted in reaching CFO. It is added back after tax because interest reduced the tax bill.</li>
<li>If interest paid was classified as financing under IFRS, no add-back is needed.</li>
<li>FCFE is what could be paid to shareholders without touching the company's operations.</li>
</ul>
<h3>Cash flow ratios</h3>
<div class="tbl"><table>
<tr><th>Performance ratio</th><th>Formula</th></tr>
<tr><td>Cash flow to revenue</td><td>CFO / revenue</td></tr>
<tr><td>Cash return on assets</td><td>CFO / average total assets</td></tr>
<tr><td>Cash return on equity</td><td>CFO / average equity</td></tr>
<tr><td>Cash to income</td><td>CFO / operating income</td></tr>
<tr><td>Cash flow per share</td><td>(CFO − preferred dividends) / ordinary shares</td></tr>
</table></div>
<div class="tbl"><table>
<tr><th>Coverage ratio</th><th>Formula</th></tr>
<tr><td>Debt coverage</td><td>CFO / total debt</td></tr>
<tr><td>Interest coverage</td><td>(CFO + interest paid + taxes paid) / interest paid</td></tr>
<tr><td>Reinvestment</td><td>CFO / cash paid for long-term assets</td></tr>
<tr><td>Debt payment</td><td>CFO / cash paid for long-term debt repayment</td></tr>
<tr><td>Dividend payment</td><td>CFO / dividends paid</td></tr>
<tr><td>Investing and financing</td><td>CFO / cash outflows for investing and financing</td></tr>
</table></div>
<div class="trap"><b>Exam trap</b>FCFE adds net borrowing; FCFF does not. FCFF adds back after-tax interest; FCFE does not.</div>""",
qs=[
 ["A company reports cash flow from operations of 200, interest expense of 40 and fixed capital investment of 80. The tax rate is 25%. FCFF is:", ["120", "150", "160"], 1, "FCFF = 200 + 40 × (1 − 0.25) − 80 = 200 + 30 − 80 = 150."],
 ["A company reports cash flow from operations of 200, fixed capital investment of 80 and net borrowing of 20. FCFE is:", ["100", "120", "140"], 2, "FCFE = 200 − 80 + 20 = 140."],
 ["In calculating FCFF from cash flow from operations, after-tax interest is added back because:", ["interest is a non-cash expense.", "interest is a payment to providers of capital.", "interest is an investing cash flow."], 1, "FCFF is the cash available to all capital providers, including lenders, so their return is added back. The tax adjustment reflects the deductibility of interest."],
 ["A company has reported rising net income for three years while its cash flow from operations has been falling. This most likely indicates:", ["high quality of earnings.", "low quality of earnings.", "a reduction in financial leverage."], 1, "Profit that is not supported by cash suggests aggressive accrual accounting or working capital problems."],
 ["A mature company is most likely to be in a sound position if its main source of cash is:", ["operating activities.", "investing activities.", "financing activities."], 0, "Sustainable businesses generate enough operating cash to fund investment and returns to capital providers."],
 ["A company has cash flow from operations of 300 and total debt of 1,200. Its debt coverage ratio is closest to:", ["0.25", "0.40", "4.00"], 0, "Debt coverage = CFO / total debt = 300 / 1,200 = 0.25."],
 ["In a common-size cash flow statement prepared on a revenue basis, each line item is divided by:", ["total assets.", "revenue.", "cash flow from operations."], 1, "Expressing items as a percentage of revenue helps with comparison and forecasting."],
 ["The reinvestment ratio is calculated as cash flow from operations divided by:", ["dividends paid.", "total debt.", "cash paid for long-term assets."], 2, "It shows whether operating cash flow is sufficient to pay for capital expenditure."],
 ["FCFF is 150, interest expense is 40, the tax rate is 25% and net borrowing is 20. FCFE is:", ["100", "140", "200"], 1, "FCFE = FCFF − interest × (1 − t) + net borrowing = 150 − 30 + 20 = 140."],
 ["A company has cash flow from operations of 180 and revenue of 1,200. Its cash flow to revenue ratio is:", ["6.7%", "15.0%", "18.0%"], 1, "180 / 1,200 = 15.0%."],
]))

R.append(dict(id="iv", n="Analysis of Inventories", k="INVENTORY", w=3, c="#2f8f5b",
terms=[
 ["Cost of goods sold (COGS)", "Satışların maliyeti", "The cost of the inventory that was sold during the period.", "Dönem içinde satılan stokların maliyeti."],
 ["First-in, first-out (FIFO)", "İlk giren ilk çıkar (FIFO)", "A cost flow method that assumes the oldest units are sold first.", "En eski birimlerin önce satıldığını varsayan maliyet akış yöntemi."],
 ["Last-in, first-out (LIFO)", "Son giren ilk çıkar (LIFO)", "A cost flow method that assumes the newest units are sold first; allowed under US GAAP only.", "En yeni birimlerin önce satıldığını varsayan maliyet akış yöntemi; yalnızca ABD GAAP'te izinlidir."],
 ["Weighted average cost", "Ağırlıklı ortalama maliyet", "A cost flow method that assigns the average cost of all units available to both COGS and ending inventory.", "Satışa hazır tüm birimlerin ortalama maliyetini hem satışların maliyetine hem dönem sonu stoka dağıtan yöntem."],
 ["Specific identification", "Gerçek parti maliyeti (özel tanımlama)", "A method that tracks the actual cost of each individual item.", "Her bir kalemin gerçek maliyetini izleyen yöntem."],
 ["Net realizable value (NRV)", "Net gerçekleşebilir değer", "Estimated selling price minus the estimated costs of completion and sale.", "Tahmini satış fiyatından tahmini tamamlama ve satış maliyetlerinin çıkarılmasıyla bulunan değer."],
 ["Inventory write-down", "Stok değer düşüklüğü", "A reduction of inventory to a value below its cost, recognized as an expense.", "Stokun maliyetinin altındaki bir değere indirilmesi; gider olarak kaydedilir."],
 ["LIFO reserve", "LIFO karşılığı", "The difference between inventory reported under LIFO and what it would be under FIFO.", "LIFO'ya göre raporlanan stok ile FIFO'ya göre olacak stok arasındaki fark."],
 ["LIFO liquidation", "LIFO tasfiyesi", "Selling more units than were purchased, so that old, low-cost layers flow into COGS.", "Alınandan fazla birim satılması; böylece eski ve düşük maliyetli katmanlar satışların maliyetine geçer."],
 ["Periodic inventory system", "Aralıklı envanter sistemi", "A system that determines inventory and COGS at the end of the period.", "Stokun ve satışların maliyetinin dönem sonunda belirlendiği sistem."],
 ["Perpetual inventory system", "Sürekli envanter sistemi", "A system that updates inventory and COGS after every sale.", "Stokun ve satışların maliyetinin her satıştan sonra güncellendiği sistem."],
 ["Inventory turnover", "Stok devir hızı", "Cost of goods sold divided by average inventory.", "Satışların maliyetinin ortalama stoka bölümü."],
],
notes="""<h3>The basic relationship</h3>
<p class="f">ending inventory = beginning inventory + purchases − cost of goods sold</p>
<ul>
<li>Inventory cost includes purchase price, conversion costs and costs to bring the goods to their present location and condition. Abnormal waste, storage of finished goods, selling and administrative costs are expensed.</li>
</ul>
<h3>Cost flow methods</h3>
<div class="tbl"><table>
<tr><th>Method</th><th>COGS consists of</th><th>Ending inventory consists of</th><th>Allowed under</th></tr>
<tr><td>FIFO</td><td>Oldest costs</td><td>Most recent costs</td><td>IFRS and US GAAP</td></tr>
<tr><td>LIFO</td><td>Most recent costs</td><td>Oldest costs</td><td>US GAAP only</td></tr>
<tr><td>Weighted average</td><td>Average cost</td><td>Average cost</td><td>IFRS and US GAAP</td></tr>
<tr><td>Specific identification</td><td>Actual cost of each item</td><td>Actual cost of each item</td><td>IFRS and US GAAP</td></tr>
</table></div>
<h3>When prices are rising</h3>
<div class="tbl"><table>
<tr><th></th><th>LIFO</th><th>FIFO</th></tr>
<tr><td>COGS</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Gross profit and net income</td><td>Lower</td><td>Higher</td></tr>
<tr><td>Income taxes</td><td>Lower</td><td>Higher</td></tr>
<tr><td>Cash flow</td><td>Higher, because of the tax saving</td><td>Lower</td></tr>
<tr><td>Ending inventory</td><td>Lower, at old costs</td><td>Higher, close to current cost</td></tr>
<tr><td>Inventory turnover</td><td>Higher</td><td>Lower</td></tr>
</table></div>
<ul>
<li>Weighted average lies between the two. When prices are falling, everything reverses.</li>
<li>FIFO gives the more useful balance sheet; LIFO gives the more current cost of goods sold.</li>
<li>FIFO and specific identification give the same result under periodic and perpetual systems. LIFO and weighted average may not.</li>
</ul>
<h3>LIFO reserve and conversion to FIFO</h3>
<p class="f">FIFO inventory = LIFO inventory + LIFO reserve</p>
<p class="f">FIFO COGS = LIFO COGS − increase in LIFO reserve</p>
<ul>
<li>Converting lets an analyst compare a LIFO company with FIFO companies.</li>
<li><b>LIFO liquidation:</b> when inventory quantities fall, old cheap layers go into COGS. Margins rise temporarily, the LIFO reserve falls, and the profit is not sustainable.</li>
</ul>
<h3>Measurement after purchase</h3>
<div class="tbl"><table>
<tr><th></th><th>IFRS</th><th>US GAAP</th></tr>
<tr><td>Carrying value</td><td>Lower of cost and net realizable value</td><td>Lower of cost and NRV; lower of cost or market for LIFO and retail methods</td></tr>
<tr><td>Reversal of a write-down</td><td>Allowed, up to the original cost</td><td>Not allowed</td></tr>
</table></div>
<ul>
<li>A write-down increases COGS (or is shown as a separate loss), lowers profit, assets and equity, and raises turnover in later periods.</li>
<li>Commodity producers and dealers may carry inventory at net realizable value even above cost.</li>
</ul>
<h3>Ratios and warning signs</h3>
<p class="f">inventory turnover = COGS / average inventory &nbsp;&nbsp;&nbsp; days of inventory on hand = 365 / turnover</p>
<ul>
<li>Low turnover with slow sales growth suggests obsolete stock. High turnover with slow sales growth may mean too little inventory.</li>
<li>Finished goods growing faster than sales signals weakening demand; raw materials and work-in-progress growing may signal expected demand.</li>
</ul>
<div class="trap"><b>Exam trap</b>With rising prices, LIFO reports lower profit but higher cash flow, because it lowers taxes. Lower profit does not mean lower cash.</div>""",
qs=[
 ["A company buys 10 units at 5 each and later 10 units at 6 each. It sells 12 units. Under FIFO, cost of goods sold is:", ["62", "66", "70"], 0, "FIFO sells the oldest first: 10 × 5 + 2 × 6 = 62. Weighted average gives 66 and LIFO 70."],
 ["A company buys 10 units at 5 each and later 10 units at 6 each. It sells 12 units. Under LIFO, ending inventory is:", ["40", "44", "48"], 0, "LIFO sells the newest first, leaving 8 of the oldest units: 8 × 5 = 40."],
 ["In a period of rising prices, compared with FIFO, LIFO results in:", ["higher net income and higher taxes.", "lower net income and lower taxes.", "lower net income and higher taxes."], 1, "LIFO puts the most recent, higher costs into COGS, which lowers profit and therefore the tax bill."],
 ["Which inventory cost flow method is not permitted under IFRS?", ["FIFO", "LIFO", "Weighted average cost"], 1, "LIFO is allowed under US GAAP only."],
 ["A company reports LIFO inventory of 400 and a LIFO reserve of 60. Its inventory on a FIFO basis is:", ["340", "400", "460"], 2, "FIFO inventory = LIFO inventory + LIFO reserve = 400 + 60 = 460."],
 ["A company's LIFO cost of goods sold is 900 and its LIFO reserve increased by 25 during the year. Cost of goods sold on a FIFO basis is:", ["875", "900", "925"], 0, "FIFO COGS = LIFO COGS − increase in the LIFO reserve = 900 − 25 = 875."],
 ["Under IFRS, inventory is measured at the lower of cost and:", ["market value.", "replacement cost.", "net realizable value."], 2, "Net realizable value is the estimated selling price less costs to complete and sell."],
 ["An inventory write-down recognized in a prior year may be reversed if the value recovers under:", ["IFRS only.", "US GAAP only.", "both IFRS and US GAAP."], 0, "IFRS allows reversal up to the amount of the original write-down. US GAAP does not."],
 ["A LIFO liquidation in a period of rising prices most likely results in:", ["a lower gross profit margin.", "a higher gross profit margin that is not sustainable.", "an increase in the LIFO reserve."], 1, "Old, low-cost layers enter COGS, temporarily lifting margins and reducing the LIFO reserve."],
 ["A company has cost of goods sold of 600 and average inventory of 100. Its days of inventory on hand is closest to:", ["6 days", "37 days", "61 days"], 2, "Turnover = 600 / 100 = 6. Days of inventory = 365 / 6 ≈ 61."],
]))

R.append(dict(id="lt", n="Analysis of Long-Term Assets", k="LONG-TERM ASSETS", w=3, c="#c2417a",
terms=[
 ["Property, plant and equipment (PP&E)", "Maddi duran varlıklar", "Tangible assets used in operations for more than one period.", "Faaliyetlerde birden fazla dönem kullanılan fiziksel varlıklar."],
 ["Depreciation", "Amortisman", "The systematic allocation of a tangible asset's cost over its useful life.", "Fiziksel bir varlığın maliyetinin faydalı ömrüne sistematik biçimde dağıtılması."],
 ["Amortization", "İtfa", "The systematic allocation of an intangible asset's cost over its useful life.", "Maddi olmayan bir varlığın maliyetinin faydalı ömrüne sistematik biçimde dağıtılması."],
 ["Carrying amount", "Defter değeri", "The value at which an asset is reported: cost minus accumulated depreciation and impairment.", "Varlığın raporlandığı değer: maliyetten birikmiş amortisman ve değer düşüklüğünün çıkarılmasıyla bulunur."],
 ["Residual value", "Kalıntı değer (hurda değer)", "The estimated amount the asset will be worth at the end of its useful life.", "Varlığın faydalı ömrü sonunda tahmin edilen değeri."],
 ["Straight-line method", "Doğrusal amortisman yöntemi", "Depreciation of an equal amount in each year of the asset's life.", "Varlığın ömrünün her yılında eşit tutarda amortisman ayrılması."],
 ["Double-declining balance method", "Çift azalan bakiyeler yöntemi", "An accelerated method that applies twice the straight-line rate to the opening carrying amount.", "Doğrusal oranın iki katını dönem başı defter değerine uygulayan hızlandırılmış yöntem."],
 ["Units-of-production method", "Üretim miktarı yöntemi", "Depreciation based on the asset's actual output or use in the period.", "Varlığın dönemdeki fiili üretimine veya kullanımına dayalı amortisman."],
 ["Recoverable amount", "Geri kazanılabilir tutar", "The higher of an asset's fair value less costs to sell and its value in use.", "Varlığın satış maliyetleri düşülmüş gerçeğe uygun değeri ile kullanım değerinden yüksek olanı."],
 ["Value in use", "Kullanım değeri", "The present value of the future cash flows expected from an asset.", "Bir varlıktan beklenen gelecekteki nakit akışlarının bugünkü değeri."],
 ["Revaluation model", "Yeniden değerleme modeli", "An IFRS option to carry long-term assets at fair value instead of cost.", "Uzun vadeli varlıkların maliyet yerine gerçeğe uygun değerle izlenmesine izin veren UFRS seçeneği."],
 ["Derecognition", "Finansal durum tablosu dışı bırakma", "Removing an asset from the balance sheet when it is sold, exchanged or abandoned.", "Varlık satıldığında, takas edildiğinde veya terk edildiğinde bilançodan çıkarılması."],
],
notes="""<h3>Getting the asset onto the balance sheet</h3>
<ul>
<li>Capitalized cost includes the purchase price and everything needed to get the asset ready for use: delivery, installation, testing.</li>
<li>Interest on borrowing during construction of an asset is capitalized as part of its cost.</li>
<li>Later spending that extends the asset's life or capacity is capitalized. Routine repairs and maintenance are expensed.</li>
<li>Intangibles: purchased ones are capitalized; research is expensed; development is capitalized under IFRS if criteria are met.</li>
</ul>
<h3>Depreciation methods</h3>
<p class="f">straight-line = (cost − residual value) / useful life</p>
<p class="f">double-declining balance = (2 / useful life) × opening carrying amount</p>
<p class="f">units of production = (cost − residual value) × units produced / total expected units</p>
<ul>
<li>Double-declining balance ignores residual value in the formula but stops when the carrying amount reaches residual value.</li>
<li>Accelerated methods give higher expense and lower profit in early years, and the reverse later.</li>
<li>A longer useful life or a higher residual value lowers annual depreciation and raises reported profit. These are estimates, so they are a way to manage earnings.</li>
<li>IFRS requires <b>component depreciation</b>: significant parts with different lives are depreciated separately.</li>
</ul>
<h3>Impairment of assets held for use</h3>
<div class="tbl"><table>
<tr><th></th><th>IFRS</th><th>US GAAP</th></tr>
<tr><td>Test</td><td>Carrying amount &gt; recoverable amount</td><td>Carrying amount &gt; undiscounted future cash flows</td></tr>
<tr><td>Loss</td><td>Carrying amount − recoverable amount</td><td>Carrying amount − fair value</td></tr>
<tr><td>Reversal</td><td>Allowed, up to what the carrying amount would have been</td><td>Not allowed</td></tr>
</table></div>
<ul>
<li>Recoverable amount = the higher of fair value less costs to sell and value in use.</li>
<li>An impairment loss lowers profit, assets and equity in the year it is recognized. It does not affect cash flow. In later years depreciation is lower, so profit and return on assets look better.</li>
</ul>
<h3>Revaluation model (IFRS only)</h3>
<ul>
<li>Assets may be carried at fair value. An increase above cost goes to equity as revaluation surplus, not to the income statement, unless it reverses an earlier loss.</li>
<li>A decrease goes to the income statement, unless it reverses an earlier surplus.</li>
<li>US GAAP allows only the cost model.</li>
</ul>
<h3>Derecognition</h3>
<p class="f">gain or loss on sale = sale proceeds − carrying amount</p>
<ul>
<li>The gain or loss is reported in the income statement. The proceeds are an investing cash inflow.</li>
<li>Assets reclassified as held for sale are no longer depreciated and are carried at the lower of carrying amount and fair value less costs to sell.</li>
</ul>
<h3>Disclosures an analyst can use</h3>
<p class="f">average age ≈ accumulated depreciation / annual depreciation expense</p>
<p class="f">remaining useful life ≈ net PP&amp;E / annual depreciation expense</p>
<p class="f">fixed asset turnover = revenue / average net PP&amp;E</p>
<ul>
<li>An old asset base suggests heavy capital spending ahead.</li>
</ul>
<div class="trap"><b>Exam trap</b>The US GAAP recoverability test uses undiscounted cash flows, but the loss itself is measured against fair value. Two different numbers are involved.</div>""",
qs=[
 ["A machine costs 100, has a residual value of 10 and a useful life of 5 years. Annual straight-line depreciation is:", ["18", "20", "22"], 0, "(100 − 10) / 5 = 18."],
 ["A machine costs 100, has a residual value of 10 and a useful life of 5 years. Depreciation in the first year under the double-declining balance method is:", ["18", "36", "40"], 2, "The rate is 2/5 = 40%, applied to the full carrying amount of 100: 40. Residual value is not deducted in the formula."],
 ["Under IFRS, an asset has a carrying amount of 100, a fair value less costs to sell of 80 and a value in use of 85. The impairment loss is:", ["0", "15", "20"], 1, "Recoverable amount is the higher of 80 and 85, which is 85. Loss = 100 − 85 = 15."],
 ["Under US GAAP, an asset held for use is tested for impairment by comparing its carrying amount with:", ["its fair value.", "its undiscounted expected future cash flows.", "the present value of its expected future cash flows."], 1, "The recoverability test uses undiscounted cash flows. If the asset fails it, the loss is measured as carrying amount less fair value."],
 ["Reversal of an impairment loss on plant and equipment held for use is permitted under:", ["IFRS only.", "US GAAP only.", "both IFRS and US GAAP."], 0, "IFRS allows reversal up to the carrying amount the asset would have had without the impairment. US GAAP prohibits it."],
 ["Equipment with a carrying amount of 40 is sold for 50. The company reports:", ["a gain of 10 in the income statement.", "a gain of 50 in the income statement.", "an increase of 10 in equity through other comprehensive income."], 0, "Gain = proceeds − carrying amount = 50 − 40 = 10, reported in profit or loss."],
 ["Compared with the straight-line method, an accelerated depreciation method in the early years of an asset's life results in:", ["higher net income.", "lower net income.", "the same net income."], 1, "Accelerated methods charge more depreciation early and less later."],
 ["A company increases its estimate of the useful life of its equipment. In the current year this change will most likely:", ["increase depreciation expense.", "decrease net income.", "increase net income."], 2, "Spreading the remaining cost over more years lowers annual depreciation and raises reported profit."],
 ["Under the IFRS revaluation model, an increase in an asset's fair value above its original cost, with no previous revaluation loss, is recognized:", ["in the income statement.", "directly in equity as a revaluation surplus.", "as a reduction of accumulated depreciation only."], 1, "The increase bypasses profit or loss and is credited to revaluation surplus within equity."],
 ["A company has accumulated depreciation of 300 and annual depreciation expense of 50. The estimated average age of its assets is:", ["3 years", "6 years", "15 years"], 1, "Average age ≈ accumulated depreciation / annual depreciation = 300 / 50 = 6 years."],
]))

R.append(dict(id="ll", n="Topics in Long-Term Liabilities and Equity", k="LIABILITIES", w=3, c="#1f7a8c",
terms=[
 ["Lease", "Kiralama", "A contract giving the right to use an asset for a period in exchange for payments.", "Ödeme karşılığında bir varlığı belirli bir süre kullanma hakkı veren sözleşme."],
 ["Lessee", "Kiracı", "The party that obtains the right to use the leased asset.", "Kiralanan varlığı kullanma hakkını elde eden taraf."],
 ["Lessor", "Kiraya veren", "The owner of the asset who grants the right to use it.", "Varlığın kullanım hakkını veren sahibi."],
 ["Right-of-use asset", "Kullanım hakkı varlığı", "The asset a lessee records for its right to use the leased item over the lease term.", "Kiracının, kiralanan kalemi kira süresince kullanma hakkı için kaydettiği varlık."],
 ["Finance lease", "Finansal kiralama", "A lease that transfers substantially all the risks and rewards of ownership to the lessee.", "Sahipliğin risk ve getirilerinin esasen tamamını kiracıya devreden kiralama."],
 ["Operating lease", "Faaliyet kiralaması", "A lease that does not transfer substantially all the risks and rewards of ownership.", "Sahipliğin risk ve getirilerinin esasen tamamını devretmeyen kiralama."],
 ["Defined contribution plan", "Tanımlanmış katkı planı", "A pension plan in which the employer pays agreed contributions and the employee bears the investment risk.", "İşverenin kararlaştırılan katkıyı ödediği ve yatırım riskini çalışanın taşıdığı emeklilik planı."],
 ["Defined benefit plan", "Tanımlanmış fayda planı", "A pension plan in which the employer promises a specified benefit and bears the investment risk.", "İşverenin belirli bir fayda taahhüt ettiği ve yatırım riskini taşıdığı emeklilik planı."],
 ["Funded status", "Fonlanma durumu", "The fair value of plan assets minus the present value of the pension obligation.", "Plan varlıklarının gerçeğe uygun değerinden emeklilik yükümlülüğünün bugünkü değerinin çıkarılmasıyla bulunan tutar."],
 ["Share-based compensation", "Pay bazlı ücretlendirme", "Pay in the form of shares or options on the company's shares.", "Şirket payları veya bu paylar üzerine opsiyonlar biçiminde yapılan ücret ödemesi."],
 ["Vesting period", "Hak ediş süresi", "The time an employee must serve before a share award becomes theirs.", "Çalışanın pay ödülünü kazanması için çalışması gereken süre."],
 ["Grant date", "Verilme (tahsis) tarihi", "The date on which a share-based award is given to the employee.", "Pay bazlı ödülün çalışana verildiği tarih."],
],
notes="""<h3>Leases: the lessee</h3>
<ul>
<li>Leasing gives the use of an asset with less cash up front and often cheaper financing, since the lessor keeps a secured claim.</li>
<li>Under both IFRS and US GAAP, a lessee records a <b>right-of-use asset</b> and a <b>lease liability</b> equal to the present value of the lease payments. Short-term leases (and, under IFRS, low-value assets) may be exempted and simply expensed.</li>
</ul>
<div class="tbl"><table>
<tr><th>Lessee</th><th>IFRS: all leases; US GAAP: finance leases</th><th>US GAAP: operating leases</th></tr>
<tr><td>Balance sheet</td><td>Right-of-use asset and lease liability</td><td>Right-of-use asset and lease liability</td></tr>
<tr><td>Income statement</td><td>Amortization of the asset plus interest on the liability; total expense is higher in early years</td><td>A single, level lease expense</td></tr>
<tr><td>Cash flow</td><td>Interest: operating (or financing under IFRS); principal: financing</td><td>Whole payment: operating</td></tr>
</table></div>
<ul>
<li>A lease is a <b>finance lease</b> if it transfers ownership, contains a purchase option that is reasonably certain to be used, covers the major part of the asset's life, has payments worth substantially all of its fair value, or the asset is so specialized that only the lessee can use it.</li>
</ul>
<h3>Leases: the lessor</h3>
<ul>
<li><b>Finance lease:</b> the lessor removes the asset, records a lease receivable and earns interest income. If the lessor is a manufacturer or dealer it also records a selling profit at the start.</li>
<li><b>Operating lease:</b> the asset stays on the lessor's balance sheet and is depreciated; lease payments are rental income.</li>
</ul>
<h3>Pensions and other deferred compensation</h3>
<div class="tbl"><table>
<tr><th></th><th>Defined contribution</th><th>Defined benefit</th></tr>
<tr><td>Employer's promise</td><td>A contribution each period</td><td>A benefit in retirement</td></tr>
<tr><td>Investment risk</td><td>Employee</td><td>Employer</td></tr>
<tr><td>Employer's expense</td><td>The contribution</td><td>Service cost, net interest, and other components</td></tr>
<tr><td>Balance sheet</td><td>Nothing, apart from unpaid contributions</td><td>Net pension asset or liability</td></tr>
</table></div>
<p class="f">funded status = fair value of plan assets − present value of the defined benefit obligation</p>
<ul>
<li>A negative funded status (underfunded plan) is reported as a net pension liability; a positive one as a net pension asset.</li>
<li>Under IFRS, service cost and net interest go to the income statement, and remeasurements (actuarial gains and losses, differences in asset returns) go to other comprehensive income and are not later recycled to profit.</li>
<li>Under US GAAP, remeasurements also go first to other comprehensive income but are amortized into the income statement over time.</li>
</ul>
<h3>Share-based compensation</h3>
<ul>
<li>It aligns employees with shareholders and needs no cash, but it dilutes existing owners.</li>
<li>The expense is the <b>fair value at the grant date</b>, spread over the <b>vesting period</b>.</li>
<li><b>Share grants:</b> fair value is the market price at grant. <b>Options:</b> fair value comes from an option pricing model, which depends on assumptions such as volatility, life of the option and dividend yield. Higher volatility or a longer life means a higher expense.</li>
<li>The expense reduces net income and retained earnings and increases paid-in capital by the same amount, so total equity is unchanged.</li>
</ul>
<div class="trap"><b>Exam trap</b>Under IFRS a lessee has no "operating lease" category. Every lease other than short-term and low-value ones is treated like a finance lease.</div>""",
qs=[
 ["Under IFRS, a lessee accounts for a five-year lease of equipment by recognizing:", ["rent expense only.", "a right-of-use asset and a lease liability.", "a lease receivable."], 1, "IFRS uses a single lessee model: an asset for the right of use and a liability for the payments, except for short-term and low-value leases."],
 ["Under US GAAP, a lessee's income statement for an operating lease shows:", ["a single, level lease expense.", "separate amortization and interest expenses.", "no expense until the lease ends."], 0, "The operating lease cost is recognized on a straight-line basis as one expense. Finance leases show amortization and interest separately."],
 ["For a lessee, compared with a US GAAP operating lease, a finance lease results in total expense in the early years that is:", ["lower.", "higher.", "the same."], 1, "Interest is highest at the start when the liability is largest, so amortization plus interest exceeds the level operating lease expense early on."],
 ["A lessor classifies a lease as an operating lease. The lessor will:", ["remove the asset from its balance sheet.", "recognize a lease receivable.", "continue to depreciate the asset and report rental income."], 2, "In an operating lease the lessor keeps the asset, depreciates it and recognizes lease income."],
 ["In a defined benefit pension plan, investment risk is borne by the:", ["employee.", "employer.", "plan trustee."], 1, "The employer has promised a benefit and must make up any shortfall. In a defined contribution plan the employee bears the risk."],
 ["A defined benefit plan has plan assets with a fair value of 800 and a pension obligation with a present value of 950. The company reports a net pension:", ["asset of 150.", "liability of 150.", "liability of 950."], 1, "Funded status = 800 − 950 = −150, an underfunded plan reported as a net liability."],
 ["For a defined contribution plan, the employer's pension expense for a period equals:", ["the contribution it is required to make.", "the change in the pension obligation.", "the benefits paid to retirees."], 0, "The employer's only obligation is the agreed contribution, which is the expense."],
 ["The expense for employee share options is measured using the fair value of the options at the:", ["grant date.", "vesting date.", "exercise date."], 0, "Fair value is fixed at the grant date and expensed over the vesting period."],
 ["All else equal, an increase in the assumed volatility of the share price used to value employee options will:", ["decrease compensation expense.", "increase compensation expense.", "have no effect on compensation expense."], 1, "Higher volatility raises the fair value of an option and therefore the expense recognized."],
 ["A lease that transfers ownership of the asset to the lessee at the end of the lease term is classified by a US GAAP lessee as:", ["a finance lease.", "an operating lease.", "a short-term lease."], 0, "Transfer of ownership is one of the criteria that make a lease a finance lease."],
]))
