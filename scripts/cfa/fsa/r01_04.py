# CFA Level I · Financial Statement Analysis · readings 1–4. Original study notes and questions.
R = []

R.append(dict(id="in", n="Introduction to Financial Statement Analysis", k="FRAMEWORK", w=2, c="#3b7dd8",
terms=[
 ["Financial statement analysis", "Finansal tablo analizi", "Using a company's financial reports and other information to judge its performance and financial position and to make economic decisions.", "Bir şirketin performansını ve finansal durumunu değerlendirmek ve ekonomik kararlar almak için finansal raporlarının ve diğer bilgilerin kullanılması."],
 ["Financial reporting", "Finansal raporlama", "The way a company presents its financial performance and position to investors, lenders and others.", "Şirketin finansal performansını ve durumunu yatırımcılara, kreditörlere ve diğerlerine sunma biçimi."],
 ["IFRS", "UFRS (Uluslararası Finansal Raporlama Standartları)", "Accounting standards issued by the International Accounting Standards Board and used in most countries.", "Uluslararası Muhasebe Standartları Kurulu tarafından yayımlanan ve çoğu ülkede kullanılan muhasebe standartları."],
 ["US GAAP", "ABD GAAP (ABD genel kabul görmüş muhasebe ilkeleri)", "Accounting standards issued by the Financial Accounting Standards Board and used in the United States.", "Finansal Muhasebe Standartları Kurulu tarafından yayımlanan ve ABD'de kullanılan muhasebe standartları."],
 ["Notes to the financial statements", "Finansal tablo dipnotları", "Disclosures that explain accounting policies, estimates and details behind the reported figures.", "Raporlanan rakamların arkasındaki muhasebe politikalarını, tahminleri ve ayrıntıları açıklayan bilgiler."],
 ["Management commentary (MD&A)", "Yönetimin değerlendirmesi", "Management's discussion of results, trends, risks and liquidity, published with the financial statements.", "Finansal tablolarla birlikte yayımlanan, yönetimin sonuçlar, eğilimler, riskler ve likiditeye ilişkin değerlendirmesi."],
 ["Audit report", "Denetim raporu", "The independent auditor's opinion on whether the financial statements are fairly presented.", "Finansal tabloların gerçeğe uygun sunulup sunulmadığına ilişkin bağımsız denetçi görüşü."],
 ["Unqualified opinion", "Olumlu görüş", "An audit opinion stating that the statements are free of material misstatement; also called a clean opinion.", "Tabloların önemli yanlışlık içermediğini belirten denetim görüşü; temiz görüş de denir."],
 ["Qualified opinion", "Şartlı (sınırlı olumlu) görüş", "An audit opinion noting a specific exception to otherwise fair presentation.", "Bunun dışında gerçeğe uygun olan sunuma belirli bir istisna bildiren denetim görüşü."],
 ["Adverse opinion", "Olumsuz görüş", "An audit opinion stating that the statements are not fairly presented.", "Tabloların gerçeğe uygun sunulmadığını belirten denetim görüşü."],
 ["Disclaimer of opinion", "Görüş bildirmekten kaçınma", "A statement that the auditor is unable to form an opinion.", "Denetçinin görüş oluşturamadığını bildirmesi."],
 ["Proxy statement", "Vekâlet çağrı belgesi", "A document sent to shareholders before a vote, with information on board members, pay and matters to be decided.", "Oylama öncesinde pay sahiplerine gönderilen; kurul üyeleri, ücretler ve karara bağlanacak konular hakkında bilgi içeren belge."],
],
notes="""<h3>The analysis framework</h3>
<ul>
<li>1. State the purpose and context: what question, for whom, by when.</li>
<li>2. Collect data: financial statements, industry and economic data, discussions with management.</li>
<li>3. Process data: adjust statements, compute ratios, build common-size statements and forecasts.</li>
<li>4. Analyse and interpret the processed data.</li>
<li>5. Develop and communicate conclusions and recommendations.</li>
<li>6. Follow up: update the analysis as new information arrives.</li>
</ul>
<h3>Who sets and who enforces the rules</h3>
<ul>
<li><b>Standard-setting bodies</b> write the accounting standards: the IASB issues IFRS, the FASB issues US GAAP. They are private-sector organizations.</li>
<li><b>Regulatory authorities</b> have the legal power to enforce them: for example the SEC in the United States. IOSCO is an association of securities regulators that promotes common principles; it is not itself a regulator.</li>
</ul>
<h3>Where the information comes from</h3>
<div class="tbl"><table>
<tr><th>Source</th><th>What it gives</th></tr>
<tr><td>Balance sheet, income statement, cash flow statement, statement of changes in equity</td><td>The core figures</td></tr>
<tr><td>Notes</td><td>Accounting policies, estimates, segment data, commitments, contingencies. Audited</td></tr>
<tr><td>Management commentary</td><td>Trends, risks, liquidity, critical accounting choices. Usually not audited</td></tr>
<tr><td>Audit report</td><td>Independent opinion on fair presentation</td></tr>
<tr><td>Interim reports</td><td>Quarterly or half-yearly updates. Usually not audited</td></tr>
<tr><td>Proxy statements</td><td>Board, management pay, voting matters</td></tr>
<tr><td>Other</td><td>Earnings calls, press releases, industry reports, economic data</td></tr>
</table></div>
<h3>Audit opinions</h3>
<div class="tbl"><table>
<tr><th>Opinion</th><th>Meaning</th></tr>
<tr><td>Unqualified (clean)</td><td>Fairly presented, free of material misstatement</td></tr>
<tr><td>Qualified</td><td>Fairly presented except for a specific matter</td></tr>
<tr><td>Adverse</td><td>Not fairly presented</td></tr>
<tr><td>Disclaimer</td><td>Auditor could not form an opinion</td></tr>
</table></div>
<ul>
<li>An audit gives <b>reasonable assurance</b>, not a guarantee. It is carried out on a sample.</li>
<li>The auditor also highlights the matters that required the most judgement: key audit matters under international standards, critical audit matters in the United States.</li>
<li>For listed US companies the auditor also gives an opinion on internal controls.</li>
</ul>
<h3>IFRS and US GAAP</h3>
<ul>
<li>The two sets of standards have converged in many areas but still differ, for example on inventory methods, revaluation of assets and development costs. An analyst comparing companies must adjust for these differences.</li>
</ul>
<div class="trap"><b>Exam trap</b>A qualified opinion is not a clean one. "Unqualified" is the favourable opinion.</div>""",
qs=[
 ["The first step in the financial statement analysis framework is to:", ["collect data.", "process data.", "state the purpose and context of the analysis."], 2, "The objective and the questions to be answered determine which data and techniques are needed."],
 ["Which of the following is a standard-setting body?", ["The International Accounting Standards Board", "The Securities and Exchange Commission", "The International Organization of Securities Commissions"], 0, "The IASB issues IFRS. The SEC is a regulatory authority, and IOSCO is an association of regulators."],
 ["An auditor concludes that the financial statements are fairly presented except for the treatment of one item. The auditor will most likely issue:", ["an adverse opinion.", "a qualified opinion.", "an unqualified opinion."], 1, "An exception to otherwise fair presentation leads to a qualified opinion."],
 ["An auditor who is unable to obtain sufficient evidence to form an opinion on the financial statements will issue:", ["an adverse opinion.", "a qualified opinion.", "a disclaimer of opinion."], 2, "A disclaimer states that no opinion can be given. An adverse opinion states that the statements are not fairly presented."],
 ["Information about the accounting policies and estimates a company used in preparing its financial statements is most likely found in the:", ["notes to the financial statements.", "proxy statement.", "auditor's report."], 0, "The notes disclose the basis of preparation, policies and significant estimates."],
 ["Information about the compensation of a company's senior executives is most likely found in the:", ["income statement.", "proxy statement.", "management commentary."], 1, "Proxy statements sent to shareholders before a vote describe board members, executive pay and matters to be voted on."],
 ["An audit of financial statements provides:", ["absolute assurance that the statements are free of error.", "reasonable assurance that the statements are free of material misstatement.", "a guarantee that no fraud has occurred."], 1, "Audits are based on samples and judgement, so they can give only reasonable assurance."],
 ["Management's discussion of trends, risks and liquidity that accompanies the financial statements is typically:", ["audited.", "unaudited.", "prepared by the external auditor."], 1, "Management commentary is prepared by management and is usually not audited, unlike the statements and their notes."],
 ["Computing ratios and preparing common-size financial statements belongs to which step of the analysis framework?", ["Collecting data", "Processing data", "Following up"], 1, "Turning raw statements into ratios, adjusted figures and common-size statements is the processing step."],
 ["Compared with annual financial statements, interim financial reports are typically:", ["audited and more detailed.", "unaudited and less detailed.", "audited and less detailed."], 1, "Quarterly or half-yearly reports are generally unaudited and contain condensed information."],
]))

R.append(dict(id="is", n="Analyzing Income Statements", k="INCOME", w=3, c="#2e9e8f",
terms=[
 ["Revenue recognition", "Hasılatın muhasebeleştirilmesi", "The rules that decide when and how much revenue is recorded.", "Hasılatın ne zaman ve hangi tutarda kaydedileceğini belirleyen kurallar."],
 ["Performance obligation", "Edim yükümlülüğü", "A promise in a contract to transfer a distinct good or service to the customer.", "Sözleşmede müşteriye ayrı bir mal veya hizmet devretme taahhüdü."],
 ["Matching principle", "Dönemsellik (eşleştirme) ilkesi", "Expenses are recognized in the same period as the revenues they helped to earn.", "Giderlerin, elde edilmesine katkıda bulundukları hasılatla aynı dönemde muhasebeleştirilmesi."],
 ["Period cost", "Dönem gideri", "A cost expensed in the period in which it is incurred, because it cannot be tied to specific revenue.", "Belirli bir hasılatla ilişkilendirilemediği için oluştuğu dönemde gider yazılan maliyet."],
 ["Capitalization", "Aktifleştirme", "Recording a cost as an asset on the balance sheet and expensing it over future periods.", "Bir maliyetin bilançoda varlık olarak kaydedilip gelecek dönemlere yayılarak giderleştirilmesi."],
 ["Discontinued operations", "Durdurulan faaliyetler", "A component of the business that has been or will be disposed of, reported separately net of tax.", "Elden çıkarılmış veya çıkarılacak olan, vergi sonrası ayrı raporlanan işletme bölümü."],
 ["Change in accounting estimate", "Muhasebe tahmininde değişiklik", "A revision of an estimate, such as an asset's useful life, applied to current and future periods.", "Bir varlığın faydalı ömrü gibi bir tahminin, cari ve gelecek dönemlere uygulanan revizyonu."],
 ["Retrospective application", "Geriye dönük uygulama", "Restating prior periods as if a new accounting policy had always been used.", "Yeni muhasebe politikası hep kullanılmış gibi önceki dönemlerin yeniden düzenlenmesi."],
 ["Basic earnings per share", "Temel pay başına kazanç", "Net income available to ordinary shareholders divided by the weighted average number of ordinary shares.", "Adi pay sahiplerine ait net kârın ağırlıklı ortalama adi pay sayısına bölümü."],
 ["Diluted earnings per share", "Sulandırılmış pay başına kazanç", "Earnings per share assuming all dilutive securities are converted into ordinary shares.", "Sulandırıcı etkisi olan tüm menkul kıymetlerin adi paya dönüştürüldüğü varsayımıyla hesaplanan pay başına kazanç."],
 ["Treasury stock method", "Geri alınan pay yöntemi", "A method for options and warrants that assumes exercise proceeds are used to buy back shares at the average market price.", "Opsiyon ve varantlar için, kullanım bedelinin ortalama piyasa fiyatından pay geri almakta kullanıldığını varsayan yöntem."],
 ["Common-size income statement", "Dikey yüzde gelir tablosu", "An income statement with every line expressed as a percentage of revenue.", "Her kalemin hasılatın yüzdesi olarak ifade edildiği gelir tablosu."],
],
notes="""<h3>Revenue recognition: five steps</h3>
<ul>
<li>1. Identify the contract with the customer.</li>
<li>2. Identify the separate performance obligations.</li>
<li>3. Determine the transaction price.</li>
<li>4. Allocate the price to the performance obligations.</li>
<li>5. Recognize revenue when, or as, each obligation is satisfied.</li>
</ul>
<ul>
<li>Revenue is recognized when control of the good or service passes to the customer, which may be at a point in time or over time. For long-term contracts, revenue is recognized in line with progress.</li>
<li>An agent that arranges a sale for another party reports only its commission as revenue, not the gross amount.</li>
</ul>
<h3>Expense recognition</h3>
<ul>
<li><b>Matching:</b> costs directly linked to revenue, such as cost of goods sold, are expensed when the revenue is recognized.</li>
<li><b>Period costs:</b> administrative costs and the like are expensed as incurred.</li>
<li><b>Capitalize or expense?</b> A cost that will bring benefits in future periods is capitalized and then depreciated or amortized.</li>
</ul>
<div class="tbl"><table>
<tr><th>In the first year</th><th>Capitalizing</th><th>Expensing</th></tr>
<tr><td>Net income</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Total assets and equity</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Cash flow from operations</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Cash flow from investing</td><td>Lower</td><td>Higher</td></tr>
</table></div>
<ul>
<li>In later years the pattern in net income reverses, because the capitalized cost is depreciated. Total cash flow is the same either way.</li>
</ul>
<h3>Non-recurring items and accounting changes</h3>
<ul>
<li><b>Discontinued operations</b> are shown separately, net of tax, below income from continuing operations.</li>
<li><b>Unusual or infrequent items</b>, such as restructuring charges, are part of continuing operations and shown before tax. Analysts usually exclude them when forecasting.</li>
</ul>
<div class="tbl"><table>
<tr><th>Change</th><th>Treatment</th></tr>
<tr><td>Accounting policy</td><td>Retrospective: prior periods restated</td></tr>
<tr><td>Accounting estimate</td><td>Prospective: current and future periods only</td></tr>
<tr><td>Correction of a prior-period error</td><td>Prior periods restated</td></tr>
</table></div>
<h3>Earnings per share</h3>
<p class="f">basic EPS = (net income − preferred dividends) / weighted average number of ordinary shares</p>
<ul>
<li>Shares issued or repurchased during the year are weighted by the fraction of the year they were outstanding. Stock dividends and splits are applied to the whole year.</li>
<li><b>Diluted EPS</b> adds the effect of securities that could become ordinary shares, but only if they are <b>dilutive</b>, that is, if they lower EPS.</li>
<li><b>Convertible preferred:</b> add back the preferred dividend to the numerator; add the new shares to the denominator.</li>
<li><b>Convertible debt:</b> add back after-tax interest to the numerator; add the new shares to the denominator.</li>
<li><b>Options and warrants (treasury stock method):</b> they are dilutive only if the average share price exceeds the exercise price.</li>
</ul>
<p class="f">net new shares = options × (1 − exercise price / average market price)</p>
<h3>Common-size analysis</h3>
<ul>
<li>Dividing every line by revenue shows margins directly: gross margin, operating margin, net margin. It allows comparison across companies of different sizes and across years.</li>
</ul>
<div class="trap"><b>Exam trap</b>If including a convertible security raises EPS, it is antidilutive and is left out of diluted EPS. Diluted EPS can never be higher than basic EPS.</div>""",
qs=[
 ["Under the five-step revenue recognition model, revenue is recognized when:", ["cash is received from the customer.", "the contract is signed.", "a performance obligation is satisfied."], 2, "Revenue is recognized when or as the company transfers control of the promised good or service."],
 ["A company has net income of 1,000 and pays preferred dividends of 100. Its weighted average number of ordinary shares is 300. Basic EPS is closest to:", ["3.00", "3.33", "3.67"], 0, "(1,000 − 100) / 300 = 3.00. Preferred dividends are deducted because they do not belong to ordinary shareholders."],
 ["A company had 1,000 shares outstanding on 1 January and issued 200 new shares on 1 July. The weighted average number of shares for the year is:", ["1,000", "1,100", "1,200"], 1, "The new shares were outstanding for half the year: 1,000 + 200 × 6/12 = 1,100."],
 ["A company has 100 options outstanding with an exercise price of 20. The average share price during the year was 25. Under the treasury stock method, the number of shares added to the denominator of diluted EPS is:", ["20", "80", "100"], 0, "Exercise raises 2,000, which buys back 2,000 / 25 = 80 shares. Net new shares = 100 − 80 = 20."],
 ["In the year an expenditure is made, capitalizing it instead of expensing it results in:", ["lower net income and lower total assets.", "higher net income and higher cash flow from operations.", "higher net income and lower cash flow from operations."], 1, "Capitalizing spreads the cost over later years, so first-year income is higher. The outflow is classified as investing, so operating cash flow is higher too."],
 ["A change in the estimated useful life of a machine is accounted for:", ["prospectively.", "retrospectively.", "as a correction of an error."], 0, "A change in estimate affects only the current and future periods. A change in accounting policy is applied retrospectively."],
 ["On the income statement, the results of discontinued operations are reported:", ["within operating income, before tax.", "separately, net of tax.", "directly in equity."], 1, "Discontinued operations are shown separately from continuing operations, net of income tax."],
 ["Options are dilutive under the treasury stock method only if the:", ["exercise price exceeds the average market price.", "average market price exceeds the exercise price.", "options were granted during the current year."], 1, "When the market price is above the exercise price, the proceeds buy back fewer shares than are issued, so the share count rises."],
 ["A company has net income of 1,000, preferred dividends of 100 and 300 weighted average ordinary shares. The preferred shares are convertible into 200 ordinary shares. Diluted EPS is closest to:", ["1.80", "2.00", "3.00"], 1, "Add back the preferred dividend and add the new shares: 1,000 / (300 + 200) = 2.00, which is below basic EPS of 3.00, so the security is dilutive."],
 ["In a common-size income statement, each item is expressed as a percentage of:", ["revenue.", "net income.", "total assets."], 0, "Dividing by revenue shows margins and cost ratios and allows comparison across firms and years."],
]))

R.append(dict(id="bs", n="Analyzing Balance Sheets", k="BALANCE", w=3, c="#c0563f",
terms=[
 ["Current assets", "Dönen varlıklar", "Assets expected to be turned into cash or used up within one year or one operating cycle.", "Bir yıl veya bir faaliyet döngüsü içinde nakde çevrilmesi veya tüketilmesi beklenen varlıklar."],
 ["Identifiable intangible asset", "Tanımlanabilir maddi olmayan varlık", "A non-physical asset that can be separated from the company or arises from legal rights, such as a patent.", "Patent gibi, şirketten ayrılabilen veya yasal haklardan doğan fiziksel olmayan varlık."],
 ["Goodwill", "Şerefiye", "The amount paid in an acquisition above the fair value of the identifiable net assets acquired.", "Bir satın almada, edinilen tanımlanabilir net varlıkların gerçeğe uygun değerinin üzerinde ödenen tutar."],
 ["Impairment", "Değer düşüklüğü", "A write-down of an asset whose carrying amount can no longer be recovered.", "Defter değeri artık geri kazanılamayan bir varlığın değerinin düşürülmesi."],
 ["Amortized cost", "İtfa edilmiş maliyet", "A measurement basis for financial assets held to collect contractual cash flows; changes in market value are not recognized.", "Sözleşmeye bağlı nakit akışlarını tahsil etmek için tutulan finansal varlıklarda kullanılan ölçüm esası; piyasa değeri değişimleri kaydedilmez."],
 ["Fair value through profit or loss (FVPL)", "Gerçeğe uygun değer farkı kâr/zarara yansıtılan", "A measurement basis under which changes in fair value go to the income statement.", "Gerçeğe uygun değer değişimlerinin gelir tablosuna yansıtıldığı ölçüm esası."],
 ["Fair value through other comprehensive income (FVOCI)", "Gerçeğe uygun değer farkı diğer kapsamlı gelire yansıtılan", "A measurement basis under which changes in fair value bypass net income and go to equity.", "Gerçeğe uygun değer değişimlerinin net kâra uğramadan özkaynağa yansıtıldığı ölçüm esası."],
 ["Deferred revenue", "Ertelenmiş gelir", "Cash received from customers for goods or services not yet delivered; a liability.", "Henüz teslim edilmemiş mal veya hizmetler için müşterilerden alınan nakit; bir yükümlülüktür."],
 ["Accumulated other comprehensive income", "Birikmiş diğer kapsamlı gelir", "The part of equity that collects gains and losses not included in net income.", "Net kâra dahil edilmeyen kazanç ve kayıpların toplandığı özkaynak kalemi."],
 ["Treasury shares", "Geri alınan paylar", "A company's own shares that it has bought back; they reduce equity.", "Şirketin geri satın aldığı kendi payları; özkaynağı azaltır."],
 ["Common-size balance sheet", "Dikey yüzde bilanço", "A balance sheet with every item expressed as a percentage of total assets.", "Her kalemin toplam varlıkların yüzdesi olarak ifade edildiği bilanço."],
 ["Solvency ratio", "Borç ödeme gücü oranı", "A ratio that measures a company's ability to meet its long-term obligations.", "Şirketin uzun vadeli yükümlülüklerini karşılama gücünü ölçen oran."],
],
notes="""<h3>What the balance sheet shows</h3>
<p class="f">assets = liabilities + equity</p>
<ul>
<li>It is a snapshot at one date. Many items are measured at historical cost, others at fair value, and some assets, such as internally created brands, do not appear at all. Book equity is therefore not the market value of the company.</li>
<li>Most companies separate <b>current</b> and <b>non-current</b> items. A liquidity-based presentation, ordered by liquidity without that split, is allowed under IFRS when it is more relevant, as for banks.</li>
</ul>
<h3>Intangible assets</h3>
<div class="tbl"><table>
<tr><th>Item</th><th>IFRS</th><th>US GAAP</th></tr>
<tr><td>Purchased intangibles</td><td>Capitalized</td><td>Capitalized</td></tr>
<tr><td>Research costs</td><td>Expensed</td><td>Expensed</td></tr>
<tr><td>Development costs</td><td>Capitalized if criteria are met</td><td>Generally expensed</td></tr>
<tr><td>Internally generated brands, customer lists</td><td>Expensed</td><td>Expensed</td></tr>
</table></div>
<ul>
<li>Intangibles with a finite life are amortized. Those with an indefinite life are not amortized but are tested for impairment at least yearly.</li>
</ul>
<h3>Goodwill</h3>
<p class="f">goodwill = purchase price − fair value of identifiable net assets acquired</p>
<ul>
<li>Arises only in an acquisition. It is not amortized; it is tested for impairment at least annually, and an impairment loss reduces net income but not cash flow.</li>
<li>Analysts often remove goodwill from assets and equity when computing ratios, and exclude impairment charges from recurring earnings.</li>
</ul>
<h3>Financial instruments</h3>
<div class="tbl"><table>
<tr><th>Category (IFRS)</th><th>Typical holding</th><th>Balance sheet value</th><th>Unrealized gains and losses</th></tr>
<tr><td>Amortized cost</td><td>Debt held to collect interest and principal</td><td>Amortized cost</td><td>Not recognized</td></tr>
<tr><td>FVOCI</td><td>Debt held both to collect and to sell; equity by election</td><td>Fair value</td><td>Other comprehensive income</td></tr>
<tr><td>FVPL</td><td>Trading securities, derivatives, most equity</td><td>Fair value</td><td>Income statement</td></tr>
</table></div>
<ul>
<li>US GAAP uses similar treatment for debt securities under the names held-to-maturity, available-for-sale and trading.</li>
</ul>
<h3>Liabilities and equity</h3>
<ul>
<li>Current liabilities: payables, short-term debt, accrued expenses, <b>deferred revenue</b>. Non-current: long-term debt, deferred tax liabilities.</li>
<li>Equity: contributed capital, retained earnings, treasury shares (a deduction), accumulated other comprehensive income, non-controlling interest.</li>
</ul>
<h3>Analysing the balance sheet</h3>
<ul>
<li>A <b>common-size balance sheet</b> divides each item by total assets.</li>
</ul>
<div class="tbl"><table>
<tr><th>Ratio</th><th>Formula</th></tr>
<tr><td>Current</td><td>Current assets / current liabilities</td></tr>
<tr><td>Quick</td><td>(Cash + marketable securities + receivables) / current liabilities</td></tr>
<tr><td>Cash</td><td>(Cash + marketable securities) / current liabilities</td></tr>
<tr><td>Long-term debt to equity</td><td>Long-term debt / total equity</td></tr>
<tr><td>Debt to equity</td><td>Total debt / total equity</td></tr>
<tr><td>Total debt (debt to assets)</td><td>Total debt / total assets</td></tr>
<tr><td>Financial leverage</td><td>Total assets / total equity</td></tr>
</table></div>
<div class="trap"><b>Exam trap</b>Deferred revenue is a liability, not income. The company has been paid but still owes the customer the product or service.</div>""",
qs=[
 ["A company acquires another for 500. The fair value of the identifiable assets acquired is 600 and the fair value of the liabilities assumed is 200. Goodwill recognized is:", ["100", "300", "400"], 0, "Identifiable net assets are 600 − 200 = 400. Goodwill = 500 − 400 = 100."],
 ["Under IFRS, goodwill is:", ["amortized over its useful life.", "tested for impairment at least annually.", "revalued upward when its fair value increases."], 1, "Goodwill is not amortized. It is tested for impairment and written down if impaired, and it is never written up."],
 ["Under IFRS, costs incurred in the development phase of an internal project are:", ["always expensed.", "always capitalized.", "capitalized if certain criteria are met."], 2, "Research costs are expensed. Development costs are capitalized once technical feasibility and other criteria are demonstrated."],
 ["A company receives payment from a customer for a service it will provide next year. On the balance sheet this is reported as:", ["revenue.", "an asset.", "a liability."], 2, "Cash received before delivery is deferred revenue, a liability that is released to income as the service is provided."],
 ["Unrealized gains and losses on a debt security measured at fair value through other comprehensive income are reported:", ["in equity, without passing through net income.", "in the income statement.", "nowhere until the security is sold."], 0, "Fair value changes on FVOCI assets are recorded in other comprehensive income and accumulate in equity."],
 ["Unrealized gains and losses on securities held for trading are reported:", ["in the income statement.", "in other comprehensive income.", "only in the notes."], 0, "Trading securities are measured at fair value through profit or loss."],
 ["Treasury shares are reported on the balance sheet as:", ["an investment asset.", "a current liability.", "a reduction of equity."], 2, "Shares the company has bought back reduce shareholders' equity and carry no voting rights or dividends."],
 ["In a common-size balance sheet, each item is expressed as a percentage of:", ["revenue.", "total equity.", "total assets."], 2, "Dividing by total assets shows the composition of assets and of financing."],
 ["A company has total assets of 1,000, total debt of 400 and total equity of 500. Its financial leverage ratio is closest to:", ["0.4", "0.8", "2.0"], 2, "Financial leverage = total assets / total equity = 1,000 / 500 = 2.0. Debt to equity is 0.8 and debt to assets is 0.4."],
 ["Which of the following assets is most likely absent from a company's balance sheet?", ["A patent purchased from another company", "Goodwill from an acquisition", "A brand the company developed itself"], 2, "Internally generated brands are expensed as incurred and not recognized as assets."],
]))

R.append(dict(id="c1", n="Analyzing Statements of Cash Flows I", k="CASH FLOW", w=3, c="#8a5cc2",
terms=[
 ["Cash flow from operating activities (CFO)", "Faaliyetlerden nakit akışı", "Cash generated or used by the company's day-to-day business.", "Şirketin günlük işlerinden sağlanan veya bu işlerde kullanılan nakit."],
 ["Cash flow from investing activities (CFI)", "Yatırım faaliyetlerinden nakit akışı", "Cash used to buy, or received from selling, long-term assets and investments.", "Uzun vadeli varlıkların ve yatırımların alımında kullanılan veya satışından elde edilen nakit."],
 ["Cash flow from financing activities (CFF)", "Finansman faaliyetlerinden nakit akışı", "Cash received from or paid to providers of capital: lenders and shareholders.", "Sermaye sağlayanlardan, yani kreditörlerden ve pay sahiplerinden alınan veya onlara ödenen nakit."],
 ["Direct method", "Doğrudan yöntem", "A presentation of operating cash flow that lists cash receipts and cash payments by type.", "Faaliyet nakit akışının, nakit tahsilat ve ödemelerin türlerine göre listelendiği sunumu."],
 ["Indirect method", "Dolaylı yöntem", "A presentation of operating cash flow that starts from net income and adjusts for non-cash items and working capital changes.", "Faaliyet nakit akışının net kârdan başlayıp nakit dışı kalemler ve işletme sermayesi değişimleri için düzeltildiği sunumu."],
 ["Non-cash charge", "Nakit çıkışı gerektirmeyen gider", "An expense that reduces net income but involves no cash outflow, such as depreciation.", "Amortisman gibi, net kârı azaltan ama nakit çıkışı içermeyen gider."],
 ["Accrual accounting", "Tahakkuk esaslı muhasebe", "Recording revenues when earned and expenses when incurred, whatever the timing of cash.", "Nakdin zamanlamasından bağımsız olarak hasılatın kazanıldığında, giderin oluştuğunda kaydedilmesi."],
 ["Cash collected from customers", "Müşterilerden tahsil edilen nakit", "Revenue adjusted for the change in receivables and in deferred revenue.", "Alacaklardaki ve ertelenmiş gelirdeki değişim için düzeltilmiş hasılat."],
 ["Cash paid to suppliers", "Tedarikçilere ödenen nakit", "Cost of goods sold adjusted for the changes in inventory and in payables.", "Stoklardaki ve ticari borçlardaki değişim için düzeltilmiş satışların maliyeti."],
 ["Non-cash investing and financing activity", "Nakit dışı yatırım ve finansman işlemi", "A transaction such as acquiring an asset by issuing shares; disclosed but not shown in the cash flow statement.", "Pay ihraç ederek varlık edinme gibi bir işlem; açıklanır ama nakit akış tablosunda gösterilmez."],
],
notes="""<h3>Three categories</h3>
<div class="tbl"><table>
<tr><th>Category</th><th>Examples</th></tr>
<tr><td>Operating</td><td>Cash from customers; cash paid to suppliers and employees; taxes</td></tr>
<tr><td>Investing</td><td>Purchase and sale of property, plant and equipment, intangibles, investments in other companies; loans made to others</td></tr>
<tr><td>Financing</td><td>Issuing and repaying debt; issuing and repurchasing shares; dividends paid</td></tr>
</table></div>
<h3>Interest and dividends: where they go</h3>
<div class="tbl"><table>
<tr><th>Item</th><th>US GAAP</th><th>IFRS</th></tr>
<tr><td>Interest received</td><td>Operating</td><td>Operating or investing</td></tr>
<tr><td>Dividends received</td><td>Operating</td><td>Operating or investing</td></tr>
<tr><td>Interest paid</td><td>Operating</td><td>Operating or financing</td></tr>
<tr><td>Dividends paid</td><td>Financing</td><td>Operating or financing</td></tr>
<tr><td>Taxes paid</td><td>Operating</td><td>Operating, unless tied to an investing or financing transaction</td></tr>
</table></div>
<ul>
<li>Non-cash investing and financing transactions, such as converting bonds into shares, are disclosed in a note or supplementary schedule, not in the statement itself.</li>
</ul>
<h3>Two ways to present operating cash flow</h3>
<ul>
<li><b>Direct method:</b> lists the cash receipts and payments. More informative about where cash comes from and goes. Encouraged by both sets of standards.</li>
<li><b>Indirect method:</b> starts with net income and reconciles it to operating cash flow. Shows why profit and cash differ. Used by most companies.</li>
<li>The two methods give the same total. Investing and financing sections are identical under both.</li>
</ul>
<h3>Indirect method</h3>
<p class="f">CFO = net income + non-cash charges − gains + losses − increases in operating assets + increases in operating liabilities</p>
<ul>
<li>Add back depreciation and amortization.</li>
<li>Subtract gains and add back losses on asset sales: the full proceeds belong in investing.</li>
<li>An <b>increase</b> in receivables or inventory uses cash: subtract. A <b>decrease</b> releases cash: add.</li>
<li>An <b>increase</b> in payables or accrued liabilities provides cash: add. A <b>decrease</b> uses cash: subtract.</li>
</ul>
<h3>Direct method building blocks</h3>
<p class="f">cash collected from customers = revenue − increase in receivables + increase in deferred revenue</p>
<p class="f">purchases = cost of goods sold + increase in inventory</p>
<p class="f">cash paid to suppliers = purchases − increase in payables</p>
<h3>Investing and financing</h3>
<ul>
<li>Cash received on the sale of an asset = carrying amount + gain (or − loss).</li>
<li>Dividends paid = dividends declared − increase in dividends payable.</li>
</ul>
<h3>Linking the statements</h3>
<p class="f">ending cash = beginning cash + CFO + CFI + CFF</p>
<ul>
<li>The change in cash on the balance sheet must equal the total of the three sections.</li>
</ul>
<div class="trap"><b>Exam trap</b>Under US GAAP, interest paid is operating but dividends paid are financing. Under IFRS, both can be classified as either operating or financing.</div>""",
qs=[
 ["Under US GAAP, dividends paid to shareholders are classified as:", ["operating cash flow.", "investing cash flow.", "financing cash flow."], 2, "US GAAP requires dividends paid to be reported in financing activities. IFRS allows operating or financing."],
 ["Under IFRS, interest paid may be classified as:", ["operating only.", "financing only.", "either operating or financing."], 2, "IFRS gives a choice for interest paid. US GAAP requires it to be operating."],
 ["A company reports net income of 100, depreciation of 20, a gain on the sale of equipment of 6, an increase in receivables of 10, a decrease in inventory of 5 and an increase in payables of 8. Cash flow from operations is:", ["105", "117", "129"], 1, "100 + 20 − 6 − 10 + 5 + 8 = 117. The gain is subtracted because the sale proceeds are an investing inflow."],
 ["A company reports revenue of 500 and its receivables increased by 20 during the year. Cash collected from customers is:", ["480", "500", "520"], 0, "Part of the revenue was not collected: 500 − 20 = 480."],
 ["A company has cost of goods sold of 300. During the year inventory increased by 10 and payables increased by 5. Cash paid to suppliers is:", ["295", "305", "315"], 1, "Purchases = 300 + 10 = 310. Cash paid = 310 − 5 = 305."],
 ["Compared with the direct method, the indirect method of presenting operating cash flow:", ["reports a different total.", "shows cash receipts and payments by type.", "starts with net income and reconciles it to cash flow."], 2, "Both methods give the same total. The indirect method explains the difference between net income and operating cash flow."],
 ["Purchase of a new factory building for cash is classified as:", ["an operating cash flow.", "an investing cash flow.", "a financing cash flow."], 1, "Buying and selling long-term assets are investing activities."],
 ["A company acquires land by issuing shares to the seller. This transaction is:", ["reported in investing and financing cash flows.", "reported in operating cash flow.", "disclosed but not reported in the cash flow statement."], 2, "No cash changed hands, so the transaction is a non-cash investing and financing activity that is disclosed separately."],
 ["Equipment with a carrying amount of 40 is sold at a gain of 10. The cash inflow reported in investing activities is:", ["10", "40", "50"], 2, "Proceeds = carrying amount + gain = 40 + 10 = 50. The gain is removed from operating cash flow in the indirect method."],
 ["An increase in accounts payable during the year is, in the indirect method:", ["added to net income.", "subtracted from net income.", "reported in financing activities."], 0, "The company expensed more than it paid in cash, so the increase is added back."],
]))
