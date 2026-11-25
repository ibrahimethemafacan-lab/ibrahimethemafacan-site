# CFA Level I · Financial Statement Analysis · readings 9–12. Original study notes and questions.
R = []

R.append(dict(id="tx", n="Analysis of Income Taxes", k="TAXES", w=2, c="#d07a2a",
terms=[
 ["Accounting profit", "Muhasebe kârı", "Pre-tax income reported in the financial statements under accounting standards.", "Muhasebe standartlarına göre finansal tablolarda raporlanan vergi öncesi kâr."],
 ["Taxable income", "Vergiye tabi kâr (mali kâr)", "Income computed under tax law, on which taxes payable are based.", "Vergi mevzuatına göre hesaplanan ve ödenecek verginin dayandığı kâr."],
 ["Taxes payable", "Ödenecek vergi", "The tax owed for the period according to the tax return.", "Vergi beyannamesine göre dönem için borçlanılan vergi."],
 ["Income tax expense", "Gelir vergisi gideri", "The tax charge in the income statement: taxes payable adjusted for changes in deferred taxes.", "Gelir tablosundaki vergi yükü: ertelenmiş vergilerdeki değişim için düzeltilmiş ödenecek vergi."],
 ["Deferred tax liability (DTL)", "Ertelenmiş vergi yükümlülüğü", "Tax that will be paid in future periods because of a temporary difference.", "Geçici bir fark nedeniyle gelecek dönemlerde ödenecek vergi."],
 ["Deferred tax asset (DTA)", "Ertelenmiş vergi varlığı", "Tax that will be recovered in future periods because of a temporary difference or a loss carried forward.", "Geçici bir fark veya devreden zarar nedeniyle gelecek dönemlerde geri kazanılacak vergi."],
 ["Temporary difference", "Geçici fark", "A difference between an item's carrying amount and its tax base that will reverse in the future.", "Bir kalemin defter değeri ile vergi matrahı arasında, gelecekte tersine dönecek fark."],
 ["Permanent difference", "Sürekli fark", "A difference between accounting profit and taxable income that will never reverse.", "Muhasebe kârı ile vergiye tabi kâr arasında hiçbir zaman tersine dönmeyecek fark."],
 ["Tax base", "Vergi matrahı (vergiye esas değer)", "The amount attributed to an asset or liability for tax purposes.", "Bir varlığa veya yükümlülüğe vergi açısından atfedilen tutar."],
 ["Valuation allowance", "Değerleme karşılığı", "Under US GAAP, a reduction of a deferred tax asset that is unlikely to be realized.", "ABD GAAP'te, gerçekleşmesi muhtemel olmayan ertelenmiş vergi varlığı için ayrılan indirim."],
 ["Effective tax rate", "Efektif vergi oranı", "Income tax expense divided by pre-tax income.", "Gelir vergisi giderinin vergi öncesi kâra bölümü."],
 ["Statutory tax rate", "Yasal vergi oranı", "The corporate income tax rate set by law in the company's home country.", "Şirketin bulunduğu ülkede yasayla belirlenen kurumlar vergisi oranı."],
],
notes="""<h3>Two sets of books</h3>
<ul>
<li>Financial statements follow accounting standards and give <b>accounting profit</b>. The tax return follows tax law and gives <b>taxable income</b>. The two differ in when, and whether, items are recognized.</li>
</ul>
<p class="f">income tax expense = taxes payable + increase in DTL − increase in DTA</p>
<h3>Temporary differences create deferred taxes</h3>
<div class="tbl"><table>
<tr><th></th><th>Deferred tax liability</th><th>Deferred tax asset</th></tr>
<tr><td>Meaning</td><td>More tax to pay later</td><td>Less tax to pay later</td></tr>
<tr><td>Arises when</td><td>Accounting profit &gt; taxable income now</td><td>Taxable income &gt; accounting profit now</td></tr>
<tr><td>Asset</td><td>Carrying amount &gt; tax base</td><td>Carrying amount &lt; tax base</td></tr>
<tr><td>Liability</td><td>Carrying amount &lt; tax base</td><td>Carrying amount &gt; tax base</td></tr>
<tr><td>Typical cause</td><td>Faster depreciation for tax than for accounting</td><td>Warranty provisions, bad debt allowances, tax losses carried forward</td></tr>
</table></div>
<p class="f">deferred tax = (carrying amount − tax base) × tax rate</p>
<ul>
<li><b>Permanent differences</b> never reverse and create no deferred tax: tax-exempt income, non-deductible fines, tax credits. They make the effective tax rate differ from the statutory rate.</li>
</ul>
<h3>When the tax rate changes</h3>
<ul>
<li>Deferred tax balances are measured at the rate expected when they reverse. A change in the rate changes both balances.</li>
<li>A rate <b>cut</b> reduces DTL and DTA. A falling DTL lowers tax expense; a falling DTA raises it. The net effect depends on which is larger.</li>
</ul>
<h3>Can the asset be used?</h3>
<ul>
<li>A deferred tax asset is worth something only if the company will have enough taxable profit in future.</li>
<li>US GAAP: a <b>valuation allowance</b> reduces the DTA if it is more likely than not that part will not be realized. Raising the allowance increases tax expense.</li>
<li>IFRS: the DTA is recognized only to the extent that realization is probable.</li>
<li>Changes in the allowance are a way to manage earnings, and an increase signals doubt about future profitability.</li>
</ul>
<h3>Three tax rates</h3>
<div class="tbl"><table>
<tr><th>Rate</th><th>Definition</th></tr>
<tr><td>Statutory</td><td>The rate set by law in the home country</td></tr>
<tr><td>Effective</td><td>Income tax expense / pre-tax income</td></tr>
<tr><td>Cash</td><td>Cash taxes paid / pre-tax income</td></tr>
</table></div>
<ul>
<li>Companies must reconcile the statutory and effective rates in the notes. The reconciling items (different rates abroad, permanent differences, tax credits, changes in rates and allowances) show how sustainable a low rate is.</li>
</ul>
<h3>For the analyst</h3>
<ul>
<li>A DTL that is expected to reverse is a real liability. One that will keep growing because the company keeps investing is, in substance, closer to equity.</li>
<li>Under both standards, deferred tax assets and liabilities are classified as non-current.</li>
</ul>
<div class="trap"><b>Exam trap</b>Faster depreciation on the tax return gives lower taxable income today, so a deferred tax liability, not an asset.</div>""",
qs=[
 ["A company reports taxes payable of 30. During the year its deferred tax liability increased by 5 and its deferred tax asset increased by 2. Income tax expense is:", ["27", "33", "37"], 1, "30 + 5 − 2 = 33."],
 ["An asset has a carrying amount of 80 and a tax base of 60. The tax rate is 25%. The company reports a deferred tax:", ["asset of 5.", "liability of 5.", "liability of 20."], 1, "The asset's carrying amount exceeds its tax base, so more tax will be paid later: (80 − 60) × 25% = 5 liability."],
 ["A company uses accelerated depreciation for tax purposes and straight-line depreciation in its financial statements. In the early years of an asset's life this creates a:", ["deferred tax asset.", "deferred tax liability.", "permanent difference."], 1, "Taxable income is lower than accounting profit now and will be higher later, so tax is deferred."],
 ["A company recognizes a warranty expense in its financial statements this year that is deductible for tax only when claims are paid. This creates a:", ["deferred tax asset.", "deferred tax liability.", "permanent difference."], 0, "Taxable income is higher than accounting profit today and will be lower when claims are paid, so future tax will be saved."],
 ["Interest received on tax-exempt bonds gives rise to:", ["a deferred tax asset.", "a temporary difference.", "a permanent difference."], 2, "The income is never taxed, so the difference does not reverse and no deferred tax is recorded."],
 ["A company has a deferred tax liability of 100 measured at a tax rate of 25%. The tax rate is reduced to 20%. As a result, the company's income tax expense will:", ["decrease by 20.", "increase by 20.", "be unaffected."], 0, "The liability is remeasured to 100 × 20/25 = 80. The reduction of 20 lowers income tax expense."],
 ["Under US GAAP, an increase in the valuation allowance against a deferred tax asset will:", ["decrease income tax expense.", "increase income tax expense.", "have no effect on net income."], 1, "A larger allowance reduces the net deferred tax asset and the reduction is charged to income tax expense."],
 ["A company has pre-tax income of 200 and income tax expense of 44. The statutory rate is 25%. Its effective tax rate is:", ["22%", "25%", "44%"], 0, "Effective tax rate = 44 / 200 = 22%."],
 ["A deferred tax liability that is not expected to reverse in the foreseeable future is most appropriately treated by an analyst as:", ["a current liability.", "equity.", "an intangible asset."], 1, "If the tax is unlikely ever to be paid, the balance is in substance part of equity."],
 ["A deferred tax asset arising from tax losses carried forward has value only if the company:", ["pays dividends.", "expects sufficient future taxable income.", "has a deferred tax liability of equal size."], 1, "Losses can be used only against future taxable profit. If that is doubtful, the asset is reduced."],
]))

R.append(dict(id="rq", n="Financial Reporting Quality", k="QUALITY", w=2, c="#6b7a8f",
terms=[
 ["Financial reporting quality", "Finansal raporlama kalitesi", "How well the reports follow accounting standards and faithfully show the company's economic reality.", "Raporların muhasebe standartlarına ne ölçüde uyduğu ve şirketin ekonomik gerçekliğini ne kadar doğru yansıttığı."],
 ["Earnings quality", "Kazanç kalitesi", "How sustainable the earnings are and whether they give an adequate return.", "Kazançların ne kadar sürdürülebilir olduğu ve yeterli getiri sağlayıp sağlamadığı."],
 ["Aggressive accounting", "Agresif muhasebe", "Choices that increase reported performance or position in the current period.", "Cari dönemde raporlanan performansı veya finansal durumu yükselten tercihler."],
 ["Conservative accounting", "İhtiyatlı muhasebe", "Choices that decrease reported performance or position in the current period.", "Cari dönemde raporlanan performansı veya finansal durumu düşüren tercihler."],
 ["Earnings smoothing", "Kâr düzleştirme", "Reducing the volatility of reported earnings by shifting profit between periods.", "Kârı dönemler arasında kaydırarak raporlanan kazancın oynaklığını azaltma."],
 ["Earnings management", "Kâr yönetimi", "Deliberate use of accounting choices or real actions to reach a desired earnings figure.", "İstenen kâr rakamına ulaşmak için muhasebe tercihlerinin veya gerçek işlemlerin bilinçli kullanımı."],
 ["Non-GAAP measure", "GAAP dışı ölçüt", "A performance figure defined by management and not by accounting standards, such as adjusted earnings.", "Düzeltilmiş kâr gibi, muhasebe standartlarınca değil yönetimce tanımlanan performans rakamı."],
 ["Channel stuffing", "Kanal doldurma", "Shipping more goods to distributors than they can sell in order to record revenue early.", "Erken hasılat kaydetmek için dağıtıcılara satabileceklerinden fazla mal sevk etme."],
 ["Bill-and-hold sale", "Faturala ve beklet satışı", "Recording a sale before the goods are delivered to the customer.", "Mallar müşteriye teslim edilmeden satışın kaydedilmesi."],
 ["Big bath", "Büyük temizlik (big bath)", "Taking very large write-offs in one bad period to make later periods look better.", "Sonraki dönemlerin daha iyi görünmesi için kötü bir dönemde çok büyük değer düşüklükleri kaydetme."],
 ["Cookie jar reserves", "Kumbara karşılıkları", "Excess provisions built up in good periods and released into profit in weaker ones.", "İyi dönemlerde ayrılan ve zayıf dönemlerde kâra aktarılan fazla karşılıklar."],
 ["Fraud triangle", "Hile üçgeni", "The three conditions that favour misreporting: opportunity, motivation and rationalization.", "Yanlış raporlamayı kolaylaştıran üç koşul: fırsat, güdü ve haklı gösterme."],
],
notes="""<h3>Two different qualities</h3>
<ul>
<li><b>Reporting quality</b> is about the information: does it follow the standards and is it useful for decisions (relevant, complete, neutral, free from error)?</li>
<li><b>Earnings quality</b> is about the results: are the earnings sustainable and adequate?</li>
<li>High earnings quality cannot be assessed without high reporting quality. A company can report low-quality earnings very accurately.</li>
</ul>
<h3>The quality spectrum, best to worst</h3>
<ul>
<li>1. Compliant with standards, decision-useful, and earnings are sustainable and adequate.</li>
<li>2. Compliant and decision-useful, but earnings quality is low.</li>
<li>3. Compliant, but choices are biased: aggressive, conservative, or smoothing.</li>
<li>4. Compliant, but earnings are actively managed, through real actions (such as cutting research spending) or accounting choices.</li>
<li>5. Not compliant with standards.</li>
<li>6. Fictitious transactions: fraud.</li>
</ul>
<h3>Biased choices</h3>
<ul>
<li><b>Aggressive</b> choices bring profit forward; later periods pay for it. <b>Conservative</b> choices delay profit.</li>
<li>Both are bias. Conservative accounting in good times can build <b>cookie jar reserves</b> that are released later to <b>smooth</b> earnings. A <b>big bath</b> loads all the bad news into one period.</li>
<li>Standards themselves contain some conservatism: losses are often recognized earlier than gains.</li>
</ul>
<h3>Why and when managers misreport</h3>
<ul>
<li><b>Motivation:</b> meeting analysts' forecasts, bonuses and share-based pay, career concerns, staying within debt covenants.</li>
<li><b>Opportunity:</b> weak internal controls, an ineffective board, standards that allow wide discretion.</li>
<li><b>Rationalization:</b> convincing oneself the choice is justified.</li>
</ul>
<h3>What keeps reporting honest</h3>
<ul>
<li>Regulators: registration, disclosure and audit requirements, enforcement.</li>
<li>Auditors: an independent opinion, though based on samples and paid for by the company.</li>
<li>Private contracts: lenders and investors write covenants and monitor compliance.</li>
</ul>
<h3>Non-GAAP measures</h3>
<ul>
<li>Management may present "adjusted" earnings that exclude items it considers unusual. Companies must show the closest standard measure with equal prominence and reconcile the two.</li>
<li>Be wary when the same "non-recurring" charges recur every year.</li>
</ul>
<h3>Accounting choices and warning signs</h3>
<div class="tbl"><table>
<tr><th>Area</th><th>What to watch</th></tr>
<tr><td>Revenue</td><td>Revenue growing faster than peers or than cash collected; rising receivables; <b>channel stuffing</b>; <b>bill-and-hold</b> sales; changes in recognition policy</td></tr>
<tr><td>Inventory</td><td>Inventory growing faster than sales; falling turnover; LIFO liquidations</td></tr>
<tr><td>Expenses</td><td>Capitalizing costs that peers expense; long useful lives; low provisions</td></tr>
<tr><td>Cash flow</td><td>Net income persistently above operating cash flow; stretching payables; classifying operating outflows as investing</td></tr>
<tr><td>Other</td><td>Frequent "one-off" items; related-party transactions; fourth-quarter surprises; a change of auditor</td></tr>
</table></div>
<div class="trap"><b>Exam trap</b>Conservative accounting is not automatically "high quality". Unbiased reporting is the ideal; conservative choices can be used to shift profit into later periods.</div>""",
qs=[
 ["Financial reports that comply with accounting standards and are decision-useful, but show earnings that are not sustainable, are best described as having:", ["low reporting quality and low earnings quality.", "high reporting quality and low earnings quality.", "low reporting quality and high earnings quality."], 1, "The information is faithful, so reporting quality is high. The results themselves are poor, so earnings quality is low."],
 ["A company ships more products to its distributors than they can sell and records the shipments as revenue. This practice is known as:", ["a big bath.", "channel stuffing.", "a bill-and-hold sale."], 1, "Channel stuffing pulls future sales into the current period and is usually followed by returns or weak later sales."],
 ["A company records unusually large provisions in a profitable year and reduces them in a later, weaker year. This is an example of:", ["cookie jar reserves.", "channel stuffing.", "aggressive revenue recognition."], 0, "Reserves built in good times and released in bad times smooth reported earnings."],
 ["The three conditions that are typically present when low-quality financial reports are issued are:", ["opportunity, motivation and rationalization.", "leverage, liquidity and profitability.", "relevance, neutrality and completeness."], 0, "These are the conditions of the fraud triangle."],
 ["Which of the following is most likely a warning sign of aggressive revenue recognition?", ["Receivables growing more slowly than revenue", "Receivables growing much faster than revenue", "Operating cash flow exceeding net income"], 1, "If revenue is recorded but not collected, receivables rise relative to sales."],
 ["When a company presents an adjusted earnings figure that is not defined by accounting standards, it is generally required to:", ["have the figure audited.", "omit the standard figure.", "reconcile it to the most comparable standard measure."], 2, "Non-GAAP measures must be accompanied by the closest standard measure and a reconciliation."],
 ["A new chief executive writes off large amounts of assets in the first year, which makes profits in following years look stronger. This is best described as:", ["a big bath.", "earnings smoothing.", "channel stuffing."], 0, "A big bath concentrates losses in one period so that later periods benefit from lower expenses."],
 ["Cutting research spending in the final quarter in order to meet an earnings target is an example of earnings management through:", ["accounting choices.", "real actions.", "fictitious transactions."], 1, "The decision changes the business itself, so it is real earnings management, and it may harm long-term results."],
 ["Compared with unbiased accounting, conservative accounting choices in the current period will most likely:", ["increase reported earnings in later periods.", "decrease reported earnings in later periods.", "have no effect on reported earnings in later periods."], 0, "Profit deferred now appears later, which is why conservative accounting can be used for smoothing."],
 ["Which of the following is least likely a mechanism that disciplines financial reporting quality?", ["Securities regulators", "External auditors", "Management bonus plans tied to earnings"], 2, "Earnings-linked pay is a motivation to misreport. Regulators, auditors and private contracts act as constraints."],
]))

R.append(dict(id="ra", n="Financial Analysis Techniques", k="RATIOS", w=3, c="#5f6fd0",
terms=[
 ["Ratio analysis", "Oran analizi", "Expressing one financial quantity relative to another to compare companies and periods.", "Şirketleri ve dönemleri karşılaştırmak için bir finansal büyüklüğün diğerine oranlanması."],
 ["Activity ratio", "Faaliyet (verimlilik) oranı", "A ratio that measures how efficiently a company uses its assets.", "Şirketin varlıklarını ne kadar verimli kullandığını ölçen oran."],
 ["Total asset turnover", "Toplam varlık devir hızı", "Revenue divided by average total assets.", "Hasılatın ortalama toplam varlıklara bölümü."],
 ["Profitability ratio", "Kârlılık oranı", "A ratio that measures the return a company earns on its sales, assets or capital.", "Şirketin satışlarından, varlıklarından veya sermayesinden elde ettiği getiriyi ölçen oran."],
 ["Operating profit margin", "Faaliyet kâr marjı", "Operating income divided by revenue.", "Faaliyet kârının hasılata bölümü."],
 ["Return on assets (ROA)", "Aktif kârlılığı", "Net income divided by average total assets.", "Net kârın ortalama toplam varlıklara bölümü."],
 ["Return on equity (ROE)", "Özkaynak kârlılığı", "Net income divided by average shareholders' equity.", "Net kârın ortalama özkaynağa bölümü."],
 ["DuPont analysis", "DuPont analizi", "Breaking return on equity into margin, turnover and leverage.", "Özkaynak kârlılığının marj, devir hızı ve kaldıraç bileşenlerine ayrılması."],
 ["Interest coverage ratio", "Faiz karşılama oranı", "Operating income divided by interest payments.", "Faaliyet kârının faiz ödemelerine bölümü."],
 ["Tax burden", "Vergi yükü", "Net income divided by pre-tax income; the share of pre-tax profit kept after tax.", "Net kârın vergi öncesi kâra bölümü; vergi öncesi kârın vergiden sonra kalan kısmı."],
 ["Interest burden", "Faiz yükü", "Pre-tax income divided by operating income; the share of operating profit kept after interest.", "Vergi öncesi kârın faaliyet kârına bölümü; faaliyet kârının faizden sonra kalan kısmı."],
 ["Price-to-earnings ratio (P/E)", "Fiyat/kazanç oranı", "Share price divided by earnings per share.", "Pay fiyatının pay başına kazanca bölümü."],
],
notes="""<h3>Tools</h3>
<ul>
<li><b>Ratios</b> relate one figure to another. <b>Common-size statements</b> express every line as a share of revenue or of total assets. <b>Trend analysis</b> follows figures over time, and <b>cross-sectional analysis</b> compares companies.</li>
<li>A ratio means little alone. Compare it with the company's history, its peers and its own goals.</li>
<li>Limits: different accounting methods, companies with several lines of business, no single "right" value, and ratios that give conflicting signals.</li>
</ul>
<h3>Activity ratios</h3>
<div class="tbl"><table>
<tr><th>Ratio</th><th>Formula</th></tr>
<tr><td>Inventory turnover</td><td>Cost of goods sold / average inventory</td></tr>
<tr><td>Receivables turnover</td><td>Revenue / average receivables</td></tr>
<tr><td>Payables turnover</td><td>Purchases / average payables</td></tr>
<tr><td>Days of inventory, sales outstanding, payables</td><td>365 / the matching turnover</td></tr>
<tr><td>Working capital turnover</td><td>Revenue / average working capital</td></tr>
<tr><td>Fixed asset turnover</td><td>Revenue / average net fixed assets</td></tr>
<tr><td>Total asset turnover</td><td>Revenue / average total assets</td></tr>
</table></div>
<h3>Liquidity ratios</h3>
<ul>
<li>Current, quick and cash ratios; the defensive interval = (cash + marketable securities + receivables) / daily cash expenditures; the cash conversion cycle = days of inventory + days sales outstanding − days payables.</li>
</ul>
<h3>Solvency ratios</h3>
<div class="tbl"><table>
<tr><th>Ratio</th><th>Formula</th></tr>
<tr><td>Debt to assets</td><td>Total debt / total assets</td></tr>
<tr><td>Debt to capital</td><td>Total debt / (total debt + total equity)</td></tr>
<tr><td>Debt to equity</td><td>Total debt / total equity</td></tr>
<tr><td>Financial leverage</td><td>Average total assets / average total equity</td></tr>
<tr><td>Interest coverage</td><td>EBIT / interest payments</td></tr>
<tr><td>Fixed charge coverage</td><td>(EBIT + lease payments) / (interest payments + lease payments)</td></tr>
<tr><td>Debt to EBITDA</td><td>Total or net debt / EBITDA</td></tr>
</table></div>
<h3>Profitability ratios</h3>
<div class="tbl"><table>
<tr><th>Ratio</th><th>Formula</th></tr>
<tr><td>Gross profit margin</td><td>Gross profit / revenue</td></tr>
<tr><td>Operating profit margin</td><td>Operating income / revenue</td></tr>
<tr><td>Pre-tax margin</td><td>Earnings before tax / revenue</td></tr>
<tr><td>Net profit margin</td><td>Net income / revenue</td></tr>
<tr><td>Return on assets</td><td>Net income / average total assets</td></tr>
<tr><td>Return on equity</td><td>Net income / average total equity</td></tr>
<tr><td>Return on invested capital</td><td>After-tax operating profit / average invested capital</td></tr>
</table></div>
<h3>DuPont analysis</h3>
<p class="f">ROE = net profit margin × total asset turnover × financial leverage</p>
<p class="f">ROE = (net income / revenue) × (revenue / average assets) × (average assets / average equity)</p>
<p class="f">five-part: ROE = tax burden × interest burden × EBIT margin × total asset turnover × financial leverage</p>
<p class="f">tax burden = net income / EBT &nbsp;&nbsp; interest burden = EBT / EBIT &nbsp;&nbsp; EBIT margin = EBIT / revenue</p>
<ul>
<li>The decomposition shows where a change in ROE comes from: operations, efficiency, or borrowing. A rise in ROE driven only by leverage is of lower quality.</li>
<li>More debt raises leverage but lowers the interest burden ratio, so its net effect on ROE depends on what the borrowed money earns.</li>
</ul>
<h3>Valuation and other uses</h3>
<ul>
<li>Valuation ratios: price to earnings, price to cash flow, price to sales, price to book value; dividend payout = dividends / net income; retention rate = 1 − payout; sustainable growth = retention rate × ROE.</li>
<li>Industry-specific measures: same-store sales for retailers, capital adequacy for banks, average revenue per user for subscription businesses.</li>
<li>Credit analysis focuses on coverage, leverage and the stability of cash flow.</li>
<li>Segment reporting lets the analyst compute margins and turnover for each line of business.</li>
</ul>
<div class="trap"><b>Exam trap</b>In the five-part DuPont formula a higher tax burden ratio means the company keeps more of its pre-tax profit, that is, it pays less tax.</div>""",
qs=[
 ["A company has a net profit margin of 5%, total asset turnover of 1.5 and financial leverage of 2.0. Its return on equity is:", ["7.5%", "10.0%", "15.0%"], 2, "ROE = 5% × 1.5 × 2.0 = 15.0%. The figure 7.5% is the return on assets."],
 ["A company's return on equity rose from 12% to 15% while its net profit margin and total asset turnover were unchanged. The increase is most likely due to:", ["higher financial leverage.", "lower tax rates.", "improved operating efficiency."], 0, "With margin and turnover constant, the only remaining DuPont component is leverage."],
 ["A company has revenue of 2,000 and average total assets of 800. Its total asset turnover is:", ["0.4", "2.5", "4.0"], 1, "2,000 / 800 = 2.5."],
 ["A company has operating income (EBIT) of 300 and interest payments of 60. Its interest coverage ratio is:", ["0.2", "4.0", "5.0"], 2, "EBIT / interest = 300 / 60 = 5.0."],
 ["In the five-part DuPont decomposition, the interest burden is calculated as:", ["EBT / EBIT.", "EBIT / revenue.", "net income / EBT."], 0, "Interest burden is the share of operating profit that remains after interest. Net income / EBT is the tax burden and EBIT / revenue is the EBIT margin."],
 ["A company has revenue of 730 and average receivables of 60. Its days sales outstanding is closest to:", ["12 days", "30 days", "60 days"], 1, "Receivables turnover = 730 / 60 = 12.17. Days sales outstanding = 365 / 12.17 = 30 days."],
 ["Which of the following is a solvency ratio?", ["Quick ratio", "Debt-to-equity ratio", "Inventory turnover"], 1, "Solvency ratios measure long-term debt-paying ability. The quick ratio is a liquidity ratio and inventory turnover is an activity ratio."],
 ["A company has a return on equity of 12% and pays out 40% of its earnings as dividends. Its sustainable growth rate is:", ["4.8%", "7.2%", "12.0%"], 1, "Retention rate = 1 − 0.40 = 0.60. Sustainable growth = 0.60 × 12% = 7.2%."],
 ["A limitation of ratio analysis is that:", ["ratios cannot be compared over time.", "companies may use different accounting methods.", "ratios ignore the size of the company."], 1, "Differences in accounting choices reduce comparability. Removing the effect of size is a strength of ratios, not a weakness."],
 ["A company has total debt of 400 and total equity of 600. Its debt-to-capital ratio is:", ["0.40", "0.67", "1.50"], 0, "Debt to capital = 400 / (400 + 600) = 0.40. Debt to equity is 0.67."],
]))

R.append(dict(id="fm", n="Introduction to Financial Statement Modeling", k="MODELING", w=1, c="#2f8f5b",
terms=[
 ["Financial statement model", "Finansal tablo modeli", "A linked set of forecast income statements, balance sheets and cash flow statements.", "Birbirine bağlı tahmini gelir tablosu, bilanço ve nakit akış tablolarından oluşan set."],
 ["Top-down approach", "Yukarıdan aşağıya yaklaşım", "Forecasting that starts with the economy and industry and works down to the company.", "Ekonomi ve sektörden başlayıp şirkete inen tahmin yöntemi."],
 ["Bottom-up approach", "Aşağıdan yukarıya yaklaşım", "Forecasting that starts from the company's own units, such as products, shops or customers.", "Şirketin ürün, mağaza veya müşteri gibi kendi birimlerinden başlayan tahmin yöntemi."],
 ["Hybrid approach", "Karma yaklaşım", "Forecasting that combines top-down and bottom-up elements.", "Yukarıdan aşağıya ve aşağıdan yukarıya unsurları birleştiren tahmin yöntemi."],
 ["Pro forma statements", "Proforma tablolar", "Forecast financial statements built on stated assumptions.", "Belirtilen varsayımlara dayanarak hazırlanan tahmini finansal tablolar."],
 ["Overconfidence bias", "Aşırı güven yanlılığı", "Placing too much faith in one's own forecasts and abilities.", "Kişinin kendi tahminlerine ve yeteneklerine gereğinden fazla güvenmesi."],
 ["Illusion of control", "Kontrol yanılsaması", "Believing one can control or predict outcomes more than is really possible.", "Sonuçları gerçekte mümkün olandan daha fazla kontrol edebileceğine veya öngörebileceğine inanma."],
 ["Conservatism bias", "Tutuculuk yanlılığı", "Being slow to change a view when new information arrives.", "Yeni bilgi geldiğinde görüşünü değiştirmekte yavaş kalma."],
 ["Representativeness bias", "Temsiliyet yanlılığı", "Classifying new information by its resemblance to familiar cases and neglecting base rates.", "Yeni bilgiyi bilinen örneklere benzerliğine göre sınıflandırıp temel oranları ihmal etme."],
 ["Confirmation bias", "Doğrulama yanlılığı", "Looking for evidence that supports an existing view and ignoring evidence against it.", "Mevcut görüşü destekleyen kanıtı arayıp aksini gösteren kanıtı göz ardı etme."],
 ["Porter's five forces", "Porter'ın beş gücü", "A framework for judging industry competition: rivalry, new entrants, substitutes, and the bargaining power of buyers and suppliers.", "Sektör rekabetini değerlendirme çerçevesi: rekabet, yeni girişler, ikameler ile alıcıların ve tedarikçilerin pazarlık gücü."],
 ["Forecast horizon", "Tahmin ufku", "The length of time over which detailed forecasts are made.", "Ayrıntılı tahminlerin yapıldığı sürenin uzunluğu."],
],
notes="""<h3>Building a model</h3>
<ul>
<li>1. Forecast revenue.</li>
<li>2. Forecast cost of goods sold and operating expenses.</li>
<li>3. Forecast financing costs and income tax.</li>
<li>4. Forecast working capital, capital spending and the resulting balance sheet.</li>
<li>5. Use the income statement and balance sheet to build the cash flow statement.</li>
</ul>
<h3>Forecasting revenue</h3>
<ul>
<li><b>Top-down:</b> start with growth of the economy, then the market, then the company's market share.</li>
<li><b>Bottom-up:</b> start with the company's own drivers: price × volume by product, sales per shop × number of shops, customers × spending per customer.</li>
<li><b>Hybrid:</b> use both; differences between them reveal questionable assumptions.</li>
<li>Revenue growth from price and volume combines multiplicatively: (1 + price change) × (1 + volume change) − 1.</li>
</ul>
<h3>Forecasting costs</h3>
<ul>
<li><b>Cost of goods sold</b> is usually forecast as a percentage of revenue, by segment if the data allow, with attention to input prices and hedging.</li>
<li><b>Selling, general and administrative costs:</b> selling costs move with revenue; administrative costs are more fixed.</li>
<li>Companies with high fixed costs have high operating leverage: profit changes by more than revenue.</li>
<li><b>Working capital</b> items are forecast with turnover or days ratios; <b>capital spending</b> is split into maintenance, guided by depreciation, and growth.</li>
</ul>
<h3>Behavioural biases in forecasting</h3>
<div class="tbl"><table>
<tr><th>Bias</th><th>Effect</th><th>Remedy</th></tr>
<tr><td>Overconfidence</td><td>Forecast ranges that are too narrow</td><td>Review past forecast errors; use scenarios</td></tr>
<tr><td>Illusion of control</td><td>Overly complex models, false precision</td><td>Focus on the few variables that matter</td></tr>
<tr><td>Conservatism</td><td>Under-reacting to new information</td><td>Review forecasts regularly and update when evidence changes</td></tr>
<tr><td>Representativeness</td><td>Judging by resemblance, ignoring base rates</td><td>Consider how the wider group of similar companies has fared</td></tr>
<tr><td>Confirmation</td><td>Seeking only supporting evidence</td><td>Look for the opposing view; talk to sceptics</td></tr>
</table></div>
<h3>Competition and prices</h3>
<ul>
<li>Porter's five forces shape what a company can charge and what it must pay: threat of substitutes, rivalry among existing firms, bargaining power of suppliers, bargaining power of customers, and threat of new entrants.</li>
<li>Strong forces mean limited pricing power and pressure on margins, so forecasts of margin expansion need a specific justification.</li>
</ul>
<h3>Inflation and deflation</h3>
<ul>
<li>When input costs rise, the question is how much can be passed on. Raising prices protects the margin per unit but may reduce volume; the result depends on the price elasticity of demand and on what competitors do.</li>
<li>Companies with differentiated products and strong market positions can pass on more.</li>
</ul>
<h3>Forecast horizon</h3>
<ul>
<li>It depends on the investor's holding period, the industry's cyclicality and any specific events. For a cyclical company the horizon should be long enough to reach a mid-cycle level of sales and margins.</li>
<li>Beyond the explicit forecast period, value is captured in a terminal value based on a long-run growth rate or a multiple.</li>
</ul>
<div class="trap"><b>Exam trap</b>Adding many more inputs to a model does not make it more accurate. It is a symptom of the illusion of control.</div>""",
qs=[
 ["An analyst forecasts a company's revenue by estimating economic growth, then the size of the market, then the company's market share. This approach is best described as:", ["top-down.", "bottom-up.", "hybrid."], 0, "Starting from the economy and narrowing to the company is the top-down approach."],
 ["An analyst forecasts a retailer's revenue by multiplying the expected number of shops by expected sales per shop. This approach is best described as:", ["top-down.", "bottom-up.", "hybrid."], 1, "Building the forecast from company-specific units is the bottom-up approach."],
 ["A company expects to raise its prices by 3% and to increase unit sales by 2%. Its expected revenue growth is closest to:", ["5.00%", "5.06%", "6.00%"], 1, "(1.03 × 1.02) − 1 = 5.06%."],
 ["An analyst who is slow to revise a forecast after the company reports clearly weaker results is most likely showing:", ["conservatism bias.", "overconfidence bias.", "representativeness bias."], 0, "Conservatism bias is the tendency to hold on to a prior view and under-react to new information."],
 ["An analyst builds a very detailed model with hundreds of inputs and believes this makes the forecast more reliable. This is most likely an example of:", ["confirmation bias.", "illusion of control.", "conservatism bias."], 1, "Adding complexity gives a feeling of control and precision without improving accuracy."],
 ["An analyst reads only research that supports her positive view of a company. The bias she is showing is:", ["confirmation bias.", "overconfidence bias.", "illusion of control."], 0, "Confirmation bias is seeking supporting evidence and discounting contrary evidence."],
 ["Which of Porter's five forces would most directly limit a company's ability to raise its selling prices?", ["Low bargaining power of customers", "High threat of substitute products", "High barriers to entry"], 1, "If customers can easily switch to substitutes, price increases lead to lost sales. The other two conditions support pricing power."],
 ["When input costs rise, a company is most likely able to protect its margin by raising prices if:", ["demand for its product is price elastic.", "demand for its product is price inelastic.", "its competitors keep their prices unchanged."], 1, "With inelastic demand, volume falls little when prices rise, so the cost increase can be passed on."],
 ["For a company in a highly cyclical industry, the explicit forecast horizon should be:", ["limited to the next quarter.", "long enough to reach a mid-cycle level of sales and profitability.", "the same as for any other company."], 1, "Forecasting only to a peak or trough would distort the valuation, so the horizon should extend to normalized conditions."],
 ["In building a financial statement model, the cash flow statement is typically:", ["forecast first.", "forecast independently of the other statements.", "derived from the forecast income statement and balance sheet."], 2, "Once income and balance sheet items are projected, the cash flow statement follows from them."],
]))
