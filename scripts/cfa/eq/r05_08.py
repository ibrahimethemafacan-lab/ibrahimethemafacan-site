# CFA Level I · Equity Investments · readings 5–8. Original study notes and questions.
R = []

R.append(dict(id="ca", n="Company Analysis: Past and Present", k="COMPANY", w=4, c="#b8860b",
terms=[
 ["Company research report", "Şirket araştırma raporu", "An analyst's document describing a company, its prospects, a valuation and a recommendation.", "Bir şirketi, beklentilerini, değerlemesini ve tavsiyeyi anlatan analist raporu."],
 ["Revenue driver", "Hasılat belirleyicisi", "A measurable factor that determines revenue, such as volume, price or number of customers.", "Hacim, fiyat veya müşteri sayısı gibi hasılatı belirleyen ölçülebilir unsur."],
 ["Unit economics", "Birim ekonomisi", "Revenue and costs measured per unit sold or per customer.", "Satılan birim veya müşteri başına ölçülen hasılat ve maliyetler."],
 ["Contribution margin", "Katkı payı", "Revenue minus variable costs.", "Hasılattan değişken maliyetlerin çıkarılmasıyla bulunan tutar."],
 ["Operating leverage", "Faaliyet kaldıracı", "The sensitivity of operating profit to changes in revenue, caused by fixed costs.", "Sabit maliyetlerin yol açtığı, faaliyet kârının hasılattaki değişimlere duyarlılığı."],
 ["Degree of operating leverage (DOL)", "Faaliyet kaldıracı derecesi", "The percentage change in operating profit for a 1% change in revenue.", "Hasılattaki %1'lik değişime karşılık faaliyet kârındaki yüzde değişim."],
 ["Same-store sales", "Benzer mağaza satışları", "Sales growth from outlets open at least a year, excluding new openings.", "En az bir yıldır açık olan mağazalardan, yeni açılışlar hariç satış büyümesi."],
 ["Customer acquisition cost (CAC)", "Müşteri edinme maliyeti", "The sales and marketing cost of winning one new customer.", "Bir yeni müşteri kazanmanın satış ve pazarlama maliyeti."],
 ["Customer lifetime value (LTV)", "Müşteri yaşam boyu değeri", "The present value of the profit a customer is expected to generate over the relationship.", "Bir müşterinin ilişki süresince yaratması beklenen kârın bugünkü değeri."],
 ["Churn rate", "Müşteri kayıp oranı", "The share of customers who stop using a service in a period.", "Bir dönemde hizmeti kullanmayı bırakan müşterilerin oranı."],
 ["Key performance indicator (KPI)", "Temel performans göstergesi", "An operating metric used to track a company's performance, often specific to the industry.", "Şirket performansını izlemek için kullanılan, çoğu zaman sektöre özgü faaliyet ölçütü."],
],
notes="""<h3>What a research report contains</h3>
<ul>
<li>Key facts and a summary, the business and its environment, financial analysis, forecasts, valuation, risks, ESG considerations, and a recommendation.</li>
</ul>
<h3>Understanding the business model</h3>
<ul>
<li>Who are the customers, what is sold, how is it sold and delivered, how is it priced, and how does the company make a profit?</li>
<li>Check the company's own description against independent sources: customers, suppliers, competitors, industry data.</li>
</ul>
<h3>Analysing revenue</h3>
<ul>
<li>Break revenue into its drivers: <b>volume × price</b>, by segment, by geography, by product.</li>
<li>Separate organic growth from growth through acquisitions and currency effects.</li>
</ul>
<p class="f">revenue growth = (1 + price change) × (1 + volume change) − 1</p>
<ul>
<li>Retailers: same-store sales and sales per square metre. Subscription businesses: subscribers, revenue per user, churn. Airlines: revenue per available seat kilometre.</li>
</ul>
<h3>Analysing costs and profitability</h3>
<ul>
<li>Split costs into fixed and variable. High fixed costs mean high operating leverage: profit falls fast when revenue falls.</li>
</ul>
<p class="f">DOL = contribution margin / operating profit = %Δ operating profit / %Δ revenue</p>
<ul>
<li><b>Unit economics:</b> a business grows profitably only if customer lifetime value exceeds customer acquisition cost.</li>
<li>Compare margins over time and with peers; look for scale effects.</li>
</ul>
<h3>Capital, working capital and financial position</h3>
<ul>
<li><b>Capital investment:</b> maintenance versus growth spending; capital intensity (capital expenditure / revenue).</li>
<li><b>Working capital:</b> days of inventory, receivables and payables; the cash conversion cycle.</li>
<li><b>Return on invested capital</b> compared with the cost of capital shows whether growth creates value.</li>
<li><b>Free cash flow</b> and the conversion of profit into cash.</li>
<li><b>Balance sheet:</b> leverage, liquidity, maturity profile of debt, off-balance-sheet obligations.</li>
</ul>
<h3>ESG</h3>
<ul>
<li>Identify the ESG factors that are material for the industry and assess how the company manages them, for example emissions for a cement maker or data privacy for a technology company.</li>
</ul>
<div class="trap"><b>Exam trap</b>A company whose customers cost more to acquire than they will ever earn becomes less valuable the faster it grows.</div>""",
qs=[
 ["A company has revenue of 1,000, variable costs of 600 and fixed costs of 300. Its degree of operating leverage is closest to:", ["1.33", "2.50", "4.00"], 2, "Contribution margin is 400 and operating profit is 100. DOL = 400 / 100 = 4.0."],
 ["A company has a degree of operating leverage of 4.0. If revenue rises by 5%, operating profit is expected to rise by approximately:", ["1.25%", "5.00%", "20.00%"], 2, "Operating profit changes by DOL × revenue change = 4 × 5% = 20%."],
 ["A company raises prices by 4% but sells 2% fewer units. Its revenue growth is closest to:", ["1.92%", "2.00%", "6.08%"], 0, "(1.04 × 0.98) − 1 = 1.92%."],
 ["Same-store sales growth is most useful because it:", ["includes revenue from newly opened stores.", "excludes the effect of new store openings.", "adjusts revenue for currency movements."], 1, "By looking only at established outlets, it isolates underlying demand from expansion."],
 ["A subscription business spends $300 to acquire each customer, and each customer is expected to generate profit with a present value of $250. If the business grows its customer base rapidly, its value will most likely:", ["fall.", "rise.", "remain unchanged."], 0, "Each new customer destroys $50 of value, so faster growth means faster value destruction."],
 ["Compared with a company with mainly variable costs, a company with mainly fixed costs will see its operating profit:", ["fall less when revenue falls.", "fall more when revenue falls.", "be unaffected by changes in revenue."], 1, "High fixed costs mean high operating leverage, so profit is more sensitive to revenue in both directions."],
 ["The proportion of a subscription company's customers who cancel in a given month is its:", ["churn rate.", "renewal margin.", "contribution margin."], 0, "Churn measures customer losses and is a key indicator for subscription businesses."],
 ["A company's growth is most likely to create value if its return on invested capital is:", ["above its cost of capital.", "below its cost of capital.", "equal to its revenue growth rate."], 0, "Investing at returns above the cost of capital adds value; investing below it destroys value."],
 ["In analysing revenue growth, an analyst separates organic growth from acquisitions mainly to:", ["remove the effect of inflation.", "assess the growth of the existing business.", "measure the company's market capitalization."], 1, "Acquired revenue can disguise weak performance in the core business."],
 ["Capital intensity is best measured as:", ["capital expenditure divided by revenue.", "revenue divided by total assets.", "net income divided by equity."], 0, "It shows how much investment is needed to support each unit of revenue."],
]))

R.append(dict(id="ic", n="Industry and Competitive Analysis", k="INDUSTRY", w=3, c="#2f8f5b",
terms=[
 ["Industry classification system", "Sektör sınıflandırma sistemi", "A framework that groups companies by their main business activity.", "Şirketleri ana faaliyetlerine göre gruplayan çerçeve."],
 ["Peer group", "Emsal grubu", "Companies with similar business activities, competitive factors and economic drivers.", "Benzer faaliyetlere, rekabet unsurlarına ve ekonomik belirleyicilere sahip şirketler."],
 ["Cyclical industry", "Döngüsel sektör", "An industry whose results rise and fall strongly with the business cycle.", "Sonuçları iş çevrimiyle güçlü biçimde yükselip düşen sektör."],
 ["Defensive industry", "Defansif sektör", "An industry whose results are relatively unaffected by the business cycle.", "Sonuçları iş çevriminden görece az etkilenen sektör."],
 ["Industry life cycle", "Sektör yaşam döngüsü", "The stages an industry passes through: embryonic, growth, shakeout, mature and decline.", "Bir sektörün geçtiği evreler: doğuş, büyüme, ayıklanma, olgunluk ve gerileme."],
 ["Barriers to entry", "Giriş engelleri", "Obstacles that make it hard for new firms to enter an industry.", "Yeni firmaların bir sektöre girmesini zorlaştıran engeller."],
 ["Pricing power", "Fiyatlama gücü", "The ability to raise prices without losing much demand.", "Talebi fazla kaybetmeden fiyatları artırabilme gücü."],
 ["Industry concentration", "Sektör yoğunlaşması", "The extent to which a few firms account for most of the industry's sales.", "Sektör satışlarının ne ölçüde birkaç firmada toplandığı."],
 ["Cost leadership", "Maliyet liderliği", "A strategy of being the lowest-cost producer in the industry.", "Sektörün en düşük maliyetli üreticisi olma stratejisi."],
 ["Differentiation", "Farklılaştırma", "A strategy of offering products that customers see as unique and will pay more for.", "Müşterilerin benzersiz gördüğü ve daha fazla ödemeye razı olduğu ürünler sunma stratejisi."],
 ["PESTLE analysis", "PESTLE analizi", "A review of political, economic, social, technological, legal and environmental influences.", "Siyasi, ekonomik, sosyal, teknolojik, hukuki ve çevresel etkilerin incelenmesi."],
],
notes="""<h3>Why industry analysis matters</h3>
<ul>
<li>Industry conditions explain much of a company's performance and set the limits of what it can achieve. They also help identify active opportunities and risks.</li>
</ul>
<h3>Grouping companies</h3>
<ul>
<li>By <b>products and services</b>, using commercial classification systems (sector, industry group, industry, sub-industry) or government systems. Classification follows the main source of revenue.</li>
<li>By <b>business-cycle sensitivity:</b> cyclical (cars, durable goods, materials, travel) or non-cyclical. Non-cyclical splits into <b>defensive</b> (utilities, food, basic consumer goods) and <b>growth</b> (demand rises regardless of the cycle).</li>
<li>Statistical grouping by return correlations is possible but unstable over time.</li>
<li>A <b>peer group</b> should share similar drivers; a company with several businesses may need several peer groups.</li>
</ul>
<h3>Industry life cycle</h3>
<div class="tbl"><table>
<tr><th>Stage</th><th>Growth</th><th>Features</th></tr>
<tr><td>Embryonic</td><td>Slow</td><td>High prices, high risk of failure, large investment</td></tr>
<tr><td>Growth</td><td>Rapid</td><td>New customers, falling prices, profits rising, limited competition</td></tr>
<tr><td>Shakeout</td><td>Slowing</td><td>Overcapacity, intense competition, price cuts, failures and consolidation</td></tr>
<tr><td>Mature</td><td>Slow or none</td><td>Replacement demand, consolidated, stable prices, strong cash flow</td></tr>
<tr><td>Decline</td><td>Negative</td><td>Substitutes or changing tastes, excess capacity, price wars</td></tr>
</table></div>
<h3>Competitive forces</h3>
<ul>
<li>Porter's five forces: rivalry among existing firms, threat of new entrants, threat of substitutes, bargaining power of suppliers, bargaining power of buyers.</li>
<li>High barriers to entry, high concentration and stable market shares support pricing power, but none guarantees it: a concentrated industry selling an undifferentiated product can still compete hard on price.</li>
<li><b>Capacity:</b> tight capacity gives producers pricing power; overcapacity drives prices down. Capacity that takes years to build can cause long cycles.</li>
</ul>
<h3>External influences</h3>
<ul>
<li>Political, economic, social, technological, legal and environmental (PESTLE). Examples: regulation, interest rates, demographics, new technology, climate policy.</li>
</ul>
<h3>Company strategy within the industry</h3>
<ul>
<li><b>Cost leadership</b>, <b>differentiation</b>, or a <b>focus</b> on a narrow segment with either approach.</li>
<li>Assess the company's competitive position: market share trends, unit costs relative to peers, brand strength, switching costs.</li>
</ul>
<div class="trap"><b>Exam trap</b>A mature industry can be very profitable. Slow growth does not mean weak returns; strong incumbents often generate the most cash.</div>""",
qs=[
 ["An industry with rapidly expanding demand, falling prices and limited competition is most likely in the:", ["growth stage.", "mature stage.", "shakeout stage."], 0, "In the growth stage new customers keep arriving, so firms can grow without taking share from each other."],
 ["An industry with slowing growth, excess capacity, price cutting and an increasing number of failures is most likely in the:", ["growth stage.", "mature stage.", "shakeout stage."], 2, "The shakeout stage is marked by overcapacity and consolidation as weaker firms exit."],
 ["Which industry is most likely classified as defensive?", ["Automobiles", "Food retailing", "Hotels and leisure"], 1, "Demand for basic food is relatively stable through the business cycle."],
 ["Which of the following most likely gives the existing firms in an industry greater pricing power?", ["High barriers to entry", "Many substitute products", "Strong bargaining power of buyers"], 0, "Barriers to entry protect incumbents from new competition. Substitutes and powerful buyers reduce pricing power."],
 ["An industry dominated by a few firms that sell an undifferentiated product most likely has:", ["no price competition.", "pricing power guaranteed by concentration.", "the possibility of intense price competition."], 2, "Concentration helps pricing power, but if products are identical, firms may still compete aggressively on price."],
 ["When an industry is operating close to full capacity, producers most likely have:", ["weak pricing power.", "strong pricing power.", "no incentive to add capacity."], 1, "Tight capacity limits supply, which allows higher prices until new capacity is added."],
 ["A company that aims to be the lowest-cost producer in its industry is following a strategy of:", ["focus.", "differentiation.", "cost leadership."], 2, "Cost leadership aims at the lowest cost so the company can compete on price and still earn a return."],
 ["Changes in population age structure are best classified in a PESTLE analysis as:", ["social factors.", "political factors.", "economic factors."], 0, "Demographics are a social influence on demand."],
 ["A company that earns most of its revenue from manufacturing chemicals and a smaller part from consulting will be classified, under commercial classification systems, mainly according to its:", ["largest source of revenue.", "largest number of employees.", "headquarters location."], 0, "Classification follows the company's principal business activity, usually measured by revenue."],
 ["Grouping companies by the statistical correlation of their share returns has the disadvantage that:", ["it cannot be done for large companies.", "it ignores past returns.", "the groups may change over time."], 2, "Correlations shift between periods, so the resulting groups are unstable and may not reflect real economic links."],
]))

R.append(dict(id="cf", n="Company Analysis: Forecasting", k="FORECASTING", w=3, c="#c2417a",
terms=[
 ["Forecast horizon", "Tahmin ufku", "The period over which detailed forecasts are made.", "Ayrıntılı tahminlerin yapıldığı dönem."],
 ["Driver-based forecast", "Belirleyici tabanlı tahmin", "A forecast built from the underlying drivers of revenue and cost, such as volume and price.", "Hacim ve fiyat gibi hasılat ve maliyetin temel belirleyicilerinden kurulan tahmin."],
 ["Mean reversion", "Ortalamaya dönüş", "The tendency of unusually high or low results to move back toward a long-run average.", "Olağandışı yüksek veya düşük sonuçların uzun dönem ortalamasına geri dönme eğilimi."],
 ["Normalized earnings", "Normalleştirilmiş kâr", "Earnings adjusted to remove one-off items and the effects of the business cycle.", "Tek seferlik kalemlerden ve iş çevrimi etkilerinden arındırılmış kâr."],
 ["Base case", "Temel senaryo", "The most likely set of forecast assumptions.", "En olası tahmin varsayımları seti."],
 ["Scenario analysis", "Senaryo analizi", "Valuing the company under several internally consistent sets of assumptions.", "Şirketi kendi içinde tutarlı birkaç varsayım seti altında değerleme."],
 ["Sensitivity analysis", "Duyarlılık analizi", "Changing one input at a time to see its effect on the forecast or value.", "Her seferinde tek bir girdiyi değiştirerek tahmine veya değere etkisini görme."],
 ["Terminal value", "Devam (uç) değeri", "The value of all cash flows beyond the explicit forecast period.", "Açık tahmin döneminin ötesindeki tüm nakit akışlarının değeri."],
 ["Maintenance capital expenditure", "Bakım yatırımı", "Spending needed to keep existing capacity working.", "Mevcut kapasiteyi çalışır durumda tutmak için gereken harcama."],
 ["Growth capital expenditure", "Büyüme yatırımı", "Spending that adds new capacity.", "Yeni kapasite ekleyen harcama."],
],
notes="""<h3>Principles</h3>
<ul>
<li>Forecast what matters for value: the main revenue drivers, margins, capital needs. Not every line deserves the same effort.</li>
<li>Use the company's history, management guidance, industry data and the economic outlook, but form an independent view.</li>
<li>Results far from normal tend to <b>revert to the mean</b> as competition and the cycle play out. A margin far above peers needs a durable reason to persist.</li>
<li>The horizon depends on the investment's holding period and the industry. Cyclical companies need a horizon that reaches mid-cycle conditions.</li>
</ul>
<h3>Approaches to revenue</h3>
<ul>
<li><b>Top-down:</b> economy, then industry, then market share.</li>
<li><b>Bottom-up:</b> drivers specific to the company, such as units × price, stores × sales per store, or the order backlog.</li>
<li><b>Hybrid:</b> combine both and reconcile the differences.</li>
</ul>
<h3>Costs and margins</h3>
<ul>
<li>Variable costs move with revenue; fixed costs step up only when capacity is added. Model operating leverage explicitly.</li>
<li>Consider input price changes, competitive pressure and the scope to pass on costs.</li>
</ul>
<h3>Balance sheet and cash flow</h3>
<ul>
<li>Working capital from days of inventory, receivables and payables.</li>
<li>Capital expenditure: maintenance spending tends to be close to depreciation over time; growth spending depends on expected volume.</li>
<li>Debt and interest from the financing plan; share count from buybacks, issuance and dilution.</li>
<li>Effective tax rate rather than statutory rate, adjusted for known changes.</li>
</ul>
<h3>Handling uncertainty</h3>
<div class="tbl"><table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td>Sensitivity analysis</td><td>Varies one input at a time to show which assumptions matter most</td></tr>
<tr><td>Scenario analysis</td><td>Varies several linked inputs together: bull, base and bear cases</td></tr>
<tr><td>Simulation</td><td>Draws inputs from distributions to give a range of values</td></tr>
</table></div>
<ul>
<li>Beyond the explicit horizon, a <b>terminal value</b> captures the rest of the company's life, usually with a long-run growth rate close to nominal economic growth or with a valuation multiple.</li>
<li>Avoid overconfidence and anchoring on past forecasts; review assumptions as new information arrives.</li>
</ul>
<div class="trap"><b>Exam trap</b>Sensitivity analysis changes one input at a time. Changing several related inputs together is scenario analysis.</div>""",
qs=[
 ["An analyst values a company under a bull case, a base case and a bear case, each with a consistent set of assumptions for growth, margins and capital spending. This approach is:", ["scenario analysis.", "sensitivity analysis.", "regression analysis."], 0, "Scenario analysis changes several linked assumptions together. Sensitivity analysis changes one at a time."],
 ["An analyst changes only the assumed long-term growth rate to see how much the estimated value changes. This approach is:", ["scenario analysis.", "sensitivity analysis.", "simulation."], 1, "Varying a single input in isolation is sensitivity analysis."],
 ["A company's operating margin is far above that of its competitors without any lasting competitive advantage. An analyst should most likely forecast that the margin will:", ["rise further.", "remain unchanged indefinitely.", "move back toward the industry level."], 2, "Without a durable advantage, competition tends to erode exceptional margins, so they revert toward the mean."],
 ["Over long periods, a company's maintenance capital expenditure is most likely to be close to its:", ["revenue.", "depreciation expense.", "net income."], 1, "Spending to replace worn-out assets roughly matches the rate at which assets are depreciated, adjusted for inflation."],
 ["The forecast horizon for a company in a cyclical industry should most likely be long enough to:", ["cover one quarter.", "reach the next cyclical peak.", "include mid-cycle conditions."], 2, "Forecasting only to a peak or trough would give a misleading picture of normal earnings."],
 ["Earnings adjusted to remove one-off items and the effects of the business cycle are called:", ["normalized earnings.", "trailing earnings.", "diluted earnings."], 0, "Normalized earnings estimate what the company earns in typical conditions."],
 ["In a long-term forecast, the terminal growth rate of a mature company should most likely be:", ["above nominal economic growth.", "close to or below nominal economic growth.", "equal to the company's recent growth rate."], 1, "No company can grow faster than the economy forever, so long-run growth should be at or below nominal GDP growth."],
 ["An analyst who forecasts revenue by multiplying the expected number of units sold by the expected average price is using a:", ["top-down approach.", "driver-based approach.", "market-share approach."], 1, "Building revenue from volume and price is a driver-based, bottom-up method."],
 ["In forecasting a company's working capital, an analyst is most likely to use:", ["days of inventory, receivables and payables.", "the dividend payout ratio.", "the price-to-earnings ratio."], 0, "Working capital items are usually projected from turnover or days ratios linked to revenue and costs."],
 ["Forecasting income tax with the company's effective tax rate instead of the statutory rate is preferable because the effective rate:", ["is always lower.", "is set by law.", "reflects the company's actual tax position."], 2, "The effective rate captures foreign rates, tax credits and other items that affect the tax actually charged."],
]))

R.append(dict(id="ev", n="Equity Valuation: Concepts and Basic Tools", k="VALUATION", w=4, c="#1f7a8c",
terms=[
 ["Intrinsic value", "İçsel değer", "The value of an asset based on an analysis of its fundamentals, which may differ from its market price.", "Temel göstergelerin analizine dayanan ve piyasa fiyatından farklı olabilen değer."],
 ["Dividend discount model (DDM)", "Temettü indirgeme modeli", "A model that values a share as the present value of its expected future dividends.", "Payı beklenen gelecek temettülerinin bugünkü değeri olarak değerleyen model."],
 ["Gordon growth model", "Gordon büyüme modeli", "A DDM that assumes dividends grow at a constant rate forever.", "Temettülerin sonsuza dek sabit oranda büyüdüğünü varsayan temettü indirgeme modeli."],
 ["Free cash flow to equity (FCFE)", "Özkaynağa serbest nakit akışı", "Cash available to shareholders after operating costs, investment and net borrowing.", "Faaliyet giderleri, yatırımlar ve net borçlanmadan sonra pay sahiplerine kalan nakit."],
 ["Multiplier model", "Çarpan modeli", "A valuation based on a ratio of price, or enterprise value, to a fundamental such as earnings.", "Fiyatın veya firma değerinin kâr gibi bir temel göstergeye oranına dayanan değerleme."],
 ["Justified P/E", "Gerekçelendirilmiş F/K", "The price-to-earnings ratio implied by fundamentals such as payout, required return and growth.", "Dağıtım oranı, gerekli getiri ve büyüme gibi temel göstergelerin ima ettiği fiyat/kazanç oranı."],
 ["Enterprise value (EV)", "Firma değeri", "The market value of the whole company: equity plus debt and preferred shares, minus cash.", "Şirketin tamamının piyasa değeri: özkaynak artı borç ve imtiyazlı paylar, eksi nakit."],
 ["EV/EBITDA", "FD/FAVÖK", "Enterprise value divided by earnings before interest, taxes, depreciation and amortization.", "Firma değerinin faiz, vergi ve amortisman öncesi kâra bölümü."],
 ["Asset-based valuation", "Varlık bazlı değerleme", "Valuing a company as the fair value of its assets minus its liabilities.", "Şirketi varlıklarının gerçeğe uygun değeri eksi yükümlülükleri olarak değerleme."],
 ["Ex-dividend date", "Hak kullanım (temettüsüz işlem) tarihi", "The first day a buyer of the share is not entitled to the declared dividend.", "Payı alan kişinin açıklanan temettüye hak kazanmadığı ilk gün."],
 ["Stock split", "Pay bölünmesi", "An increase in the number of shares with a proportional fall in price and no change in total value.", "Toplam değer değişmeden pay sayısının artırılması ve fiyatın orantılı düşmesi."],
 ["Share repurchase", "Pay geri alımı", "A company buying back its own shares, an alternative to paying cash dividends.", "Şirketin kendi paylarını geri satın alması; nakit temettüye bir alternatif."],
],
notes="""<h3>Value and price</h3>
<ul>
<li>If estimated intrinsic value is above the market price, the share appears undervalued; below it, overvalued. The confidence of that judgement depends on the reliability of the model and inputs.</li>
</ul>
<div class="tbl"><table>
<tr><th>Model family</th><th>Idea</th><th>Examples</th></tr>
<tr><td>Present value</td><td>Discount expected future cash flows</td><td>Dividend discount model, free cash flow to equity</td></tr>
<tr><td>Multiplier</td><td>Compare price with a fundamental</td><td>P/E, P/B, P/S, EV/EBITDA</td></tr>
<tr><td>Asset-based</td><td>Fair value of assets minus liabilities</td><td>Holding companies, natural resources, liquidation</td></tr>
</table></div>
<h3>Dividends and their mechanics</h3>
<ul>
<li>Declaration date, <b>ex-dividend date</b> (buyers from this day on do not receive the dividend; the price usually drops by about the dividend), holder-of-record date, payment date.</li>
<li><b>Stock dividends and splits</b> increase the number of shares and lower the price proportionally. No value is created; the holder's proportional ownership is unchanged. A reverse split does the opposite.</li>
<li><b>Share repurchases</b> return cash like a dividend. If financed with debt, EPS rises when the after-tax cost of debt is below the earnings yield (E/P).</li>
</ul>
<h3>Dividend discount models</h3>
<p class="f">preference share: V = D / r</p>
<p class="f">Gordon growth: V<sub>0</sub> = D<sub>1</sub> / (r − g), with D<sub>1</sub> = D<sub>0</sub>(1 + g)</p>
<ul>
<li>Appropriate for mature companies with stable payout policies. Very sensitive to the gap between r and g.</li>
<li><b>Multistage:</b> discount each dividend in the high-growth period, then add a terminal value at the start of stable growth, discounted back.</li>
<li>Sustainable growth = retention rate × ROE.</li>
<li><b>FCFE models</b> suit companies that pay little or no dividend, or whose dividends differ from their capacity to pay.</li>
</ul>
<h3>Multiples</h3>
<p class="f">justified forward P/E = payout ratio / (r − g)</p>
<ul>
<li>Higher payout or higher growth raises the justified P/E; higher required return lowers it.</li>
<li>Method of comparables: apply a peer group's multiple to the company. It shows relative, not absolute, value: if the whole sector is overvalued, so is the result.</li>
<li>P/E is widely used but fails when earnings are negative or volatile; P/B suits banks; P/S suits young companies without profits.</li>
</ul>
<p class="f">enterprise value = market value of equity + debt + preferred shares + minority interest − cash and investments</p>
<ul>
<li>EV multiples allow comparisons between companies with different capital structures.</li>
</ul>
<h3>Asset-based valuation</h3>
<ul>
<li>Works best when assets are mainly tangible and easy to value at market, or for liquidation. It misses intangibles and is hard to apply in high inflation.</li>
</ul>
<div class="trap"><b>Exam trap</b>The Gordon model needs next year's dividend. If the question gives the dividend just paid, multiply by (1 + g) first.</div>""",
qs=[
 ["A company has just paid a dividend of $2.00. Dividends are expected to grow at 4% a year indefinitely and the required return is 10%. The value of the share is closest to:", ["$33.33", "$34.67", "$52.00"], 1, "D1 = 2.00 × 1.04 = 2.08. Value = 2.08 / (0.10 − 0.04) = $34.67."],
 ["A preference share with a par value of $100 pays a 5% annual dividend forever. If the required return is 8%, its value is closest to:", ["$62.50", "$100.00", "$160.00"], 0, "Dividend is $5. Value = 5 / 0.08 = $62.50."],
 ["A company has just paid a dividend of $1.00. Dividends are expected to grow at 20% for two years and at 5% thereafter. The required return is 10%. The value of the share is closest to:", ["$26.08", "$27.27", "$30.24"], 1, "D1 = 1.20, D2 = 1.44, D3 = 1.512. P2 = 1.512 / 0.05 = 30.24. Value = 1.20/1.10 + (1.44 + 30.24)/1.21 = 1.09 + 26.18 = $27.27."],
 ["A company pays out 40% of its earnings. Its required return is 10% and its expected growth rate is 6%. The justified forward P/E is closest to:", ["4.0", "10.0", "16.0"], 1, "Justified forward P/E = 0.40 / (0.10 − 0.06) = 10.0."],
 ["A company has equity with a market value of 500, debt of 200 and cash of 50. Its enterprise value is closest to:", ["650", "700", "750"], 0, "EV = 500 + 200 − 50 = 650."],
 ["After a two-for-one stock split, the total market value of a shareholder's holding most likely:", ["halves.", "doubles.", "is unchanged."], 2, "The number of shares doubles and the price halves, so total value and proportional ownership are unchanged."],
 ["A company borrows to buy back its shares. Its earnings per share will increase if the after-tax cost of the debt is:", ["below the earnings yield.", "above the earnings yield.", "equal to the dividend yield."], 0, "If the earnings given up per share bought back exceed the after-tax interest cost, EPS rises."],
 ["An investor who buys a share on its ex-dividend date:", ["receives the declared dividend.", "does not receive the declared dividend.", "receives half of the declared dividend."], 1, "From the ex-dividend date onward, the share trades without the right to the declared dividend."],
 ["Asset-based valuation is most appropriate for a company that:", ["has mostly intangible assets.", "is a fast-growing technology company.", "holds mainly tangible assets with observable market values."], 2, "When assets can be valued reliably at market, their net value is a good guide to the company's value."],
 ["An analyst estimates a share's intrinsic value at $50. The share trades at $40. Based on this estimate, the share is:", ["overvalued.", "undervalued.", "fairly valued."], 1, "Market price below estimated intrinsic value indicates undervaluation, subject to confidence in the estimate."],
]))
