# CFA Level I · Economics · readings 1–4. Original study notes and questions.
R = []

R.append(dict(id="ms", n="Firms and Market Structures", k="MARKETS", w=4, c="#3b7dd8",
terms=[
 ["Economic profit", "Ekonomik kâr", "Total revenue minus all costs, including the opportunity cost of the owners' capital.", "Toplam gelirden, sahiplerin sermayesinin fırsat maliyeti dahil tüm maliyetlerin çıkarılmasıyla bulunan kâr."],
 ["Marginal revenue (MR)", "Marjinal gelir", "The change in total revenue from selling one more unit.", "Bir birim daha satmanın toplam gelirde yarattığı değişim."],
 ["Marginal cost (MC)", "Marjinal maliyet", "The change in total cost from producing one more unit.", "Bir birim daha üretmenin toplam maliyette yarattığı değişim."],
 ["Average variable cost (AVC)", "Ortalama değişken maliyet", "Total variable cost divided by the quantity produced.", "Toplam değişken maliyetin üretim miktarına bölümü."],
 ["Breakeven point", "Başabaş noktası", "The output level at which total revenue equals total cost, so economic profit is zero.", "Toplam gelirin toplam maliyete eşit olduğu, ekonomik kârın sıfır olduğu üretim düzeyi."],
 ["Shutdown point", "Kapanma noktası", "The price below which a firm cannot cover its variable costs and should stop producing in the short run.", "Firmanın değişken maliyetlerini karşılayamadığı ve kısa dönemde üretimi durdurması gereken fiyat düzeyi."],
 ["Economies of scale", "Ölçek ekonomileri", "Falling long-run average cost as the scale of production increases.", "Üretim ölçeği büyüdükçe uzun dönem ortalama maliyetin düşmesi."],
 ["Perfect competition", "Tam rekabet", "A market with many firms selling identical products, no barriers to entry and no pricing power.", "Çok sayıda firmanın aynı ürünü sattığı, giriş engeli ve fiyat belirleme gücü olmayan piyasa."],
 ["Monopolistic competition", "Tekelci rekabet", "A market with many firms selling differentiated products and low barriers to entry.", "Çok sayıda firmanın farklılaştırılmış ürün sattığı ve giriş engellerinin düşük olduğu piyasa."],
 ["Oligopoly", "Oligopol", "A market dominated by a few firms whose pricing decisions depend on one another.", "Fiyat kararları birbirine bağlı olan az sayıda firmanın hâkim olduğu piyasa."],
 ["Monopoly", "Tekel (monopol)", "A market with a single seller of a product that has no close substitutes, protected by high barriers to entry.", "Yakın ikamesi olmayan bir ürünün tek satıcısının bulunduğu, yüksek giriş engelleriyle korunan piyasa."],
 ["Nash equilibrium", "Nash dengesi", "A situation in which no firm can improve its outcome by changing its own decision alone.", "Hiçbir firmanın yalnızca kendi kararını değiştirerek sonucunu iyileştiremediği durum."],
 ["Herfindahl-Hirschman Index (HHI)", "Herfindahl-Hirschman Endeksi", "The sum of the squared market shares of the firms in a market; a measure of concentration.", "Piyasadaki firmaların pazar paylarının karelerinin toplamı; bir yoğunlaşma ölçüsü."],
],
notes="""<h3>Profit, breakeven and shutdown</h3>
<ul>
<li>Every firm, in every market structure, maximizes profit where <b>marginal revenue equals marginal cost</b>.</li>
<li>Economic profit deducts opportunity costs, so zero economic profit still means the owners earn a normal return.</li>
</ul>
<div class="tbl"><table>
<tr><th>Price relative to cost</th><th>Short run</th><th>Long run</th></tr>
<tr><td>P ≥ ATC</td><td>Operate</td><td>Stay in the market</td></tr>
<tr><td>AVC ≤ P &lt; ATC</td><td>Operate: the loss is smaller than the fixed costs</td><td>Exit</td></tr>
<tr><td>P &lt; AVC</td><td>Shut down</td><td>Exit</td></tr>
</table></div>
<ul>
<li><b>Breakeven:</b> P = ATC, or total revenue = total cost.</li>
<li>Fixed costs are paid whether or not the firm produces, so in the short run only variable costs matter for the decision to keep operating.</li>
</ul>
<h3>Scale</h3>
<ul>
<li><b>Economies of scale:</b> long-run average cost falls as output grows (specialization, bulk purchasing, spreading fixed costs).</li>
<li><b>Diseconomies of scale:</b> long-run average cost rises (bureaucracy, coordination problems).</li>
<li>The lowest point of the long-run average cost curve is the <b>minimum efficient scale</b>.</li>
</ul>
<h3>Four market structures</h3>
<div class="tbl"><table>
<tr><th></th><th>Perfect competition</th><th>Monopolistic competition</th><th>Oligopoly</th><th>Monopoly</th></tr>
<tr><td>Number of sellers</td><td>Many</td><td>Many</td><td>Few</td><td>One</td></tr>
<tr><td>Product</td><td>Identical</td><td>Differentiated</td><td>Similar or differentiated</td><td>Unique</td></tr>
<tr><td>Barriers to entry</td><td>Very low</td><td>Low</td><td>High</td><td>Very high</td></tr>
<tr><td>Pricing power</td><td>None</td><td>Some</td><td>Some to significant</td><td>Significant</td></tr>
<tr><td>Non-price competition</td><td>None</td><td>Advertising, branding</td><td>Advertising, branding</td><td>Advertising</td></tr>
<tr><td>Long-run economic profit</td><td>Zero</td><td>Zero</td><td>Possible</td><td>Possible</td></tr>
</table></div>
<h3>Perfect competition</h3>
<ul>
<li>Each firm is a price taker and faces a horizontal demand curve: P = MR.</li>
<li>Long-run equilibrium: P = MR = MC = minimum ATC. Entry and exit drive economic profit to zero.</li>
</ul>
<h3>Monopolistic competition</h3>
<ul>
<li>Each firm faces a downward-sloping demand curve for its own variety, so P &gt; MR and, at the optimum, P &gt; MC.</li>
<li>Entry of new varieties shifts each firm's demand left until P = ATC and economic profit is zero. Output is below the level that minimizes average cost, which is called excess capacity.</li>
</ul>
<h3>Oligopoly</h3>
<ul>
<li><b>Kinked demand:</b> rivals match a price cut but not a price increase. Demand is elastic above the current price and less elastic below it, so prices tend to be sticky.</li>
<li><b>Cournot:</b> firms choose quantities at the same time, each taking the other's output as given. The result lies between the monopoly and competitive outcomes.</li>
<li><b>Nash equilibrium:</b> each firm's choice is the best response to the others' choices. It explains why collusive agreements are unstable: each member gains by cheating.</li>
<li><b>Stackelberg (dominant firm):</b> a leader sets its decision first and the followers react.</li>
<li>Collusion is easier with few firms, similar products, similar costs, and credible punishment of cheaters.</li>
</ul>
<h3>Monopoly</h3>
<ul>
<li>The firm's demand curve is the market demand curve. It produces where MR = MC and charges the price on the demand curve at that quantity, so P &gt; MC.</li>
<li>For a linear demand curve, marginal revenue has the same intercept and twice the slope.</li>
<li><b>Price discrimination</b> charges different customers different prices to capture more consumer surplus. It requires separable groups with different elasticities and no resale.</li>
<li>A <b>natural monopoly</b> has such large economies of scale that one firm serves the market at the lowest cost. Regulators often set its price at average cost.</li>
</ul>
<h3>Measuring concentration</h3>
<ul>
<li><b>N-firm concentration ratio:</b> the sum of the market shares of the N largest firms. Simple, but barely moves when two of the largest firms merge.</li>
<li><b>HHI:</b> the sum of the squared market shares of the largest firms. Squaring gives large firms more weight, so it reacts strongly to mergers.</li>
<li>Neither measure accounts for barriers to entry or the elasticity of demand, so high concentration does not prove pricing power.</li>
</ul>
<div class="trap"><b>Exam trap</b>A firm with price between AVC and ATC is losing money but should keep operating in the short run. Shutting down would lose the entire fixed cost.</div>""",
qs=[
 ["In the short run, a firm should shut down if the market price is below its:", ["marginal cost.", "average total cost.", "average variable cost."], 2, "If price does not cover average variable cost, each unit produced adds to the loss. Below average total cost but above average variable cost, operating still reduces the loss."],
 ["A firm's price is above its average variable cost but below its average total cost. The firm should:", ["shut down immediately.", "operate in the short run and exit in the long run.", "operate in both the short run and the long run."], 1, "Revenue covers variable costs and part of fixed costs, so operating loses less than shutting down. In the long run all costs must be covered, so the firm exits."],
 ["A monopolist faces the demand curve P = 100 − 2Q and has a constant marginal cost of 20. The profit-maximizing price is closest to:", ["$40", "$60", "$80"], 1, "Marginal revenue is 100 − 4Q. Setting it equal to 20 gives Q = 20, and the price at that quantity is 100 − 2 × 20 = $60."],
 ["In long-run equilibrium under perfect competition, price equals:", ["marginal cost but exceeds average total cost.", "average total cost but exceeds marginal cost.", "both marginal cost and minimum average total cost."], 2, "Entry and exit push price to the minimum of average total cost, where it also equals marginal cost, so economic profit is zero."],
 ["A market with many sellers, differentiated products and low barriers to entry is best described as:", ["an oligopoly.", "perfect competition.", "monopolistic competition."], 2, "Product differentiation with many firms and easy entry defines monopolistic competition."],
 ["The kinked demand curve model of oligopoly assumes that competitors will:", ["match a price cut but not a price increase.", "match a price increase but not a price cut.", "match both price increases and price cuts."], 0, "Rivals follow price cuts to protect market share but let a firm that raises its price lose customers, which creates the kink and makes prices sticky."],
 ["A market has four firms with market shares of 40%, 30%, 20% and 10%. The Herfindahl-Hirschman Index is closest to:", ["0.25", "0.30", "0.90"], 1, "0.40² + 0.30² + 0.20² + 0.10² = 0.16 + 0.09 + 0.04 + 0.01 = 0.30. The figure 0.90 is the three-firm concentration ratio."],
 ["Compared with the N-firm concentration ratio, the Herfindahl-Hirschman Index:", ["is more sensitive to mergers among large firms.", "takes barriers to entry into account.", "reflects the elasticity of demand."], 0, "Squaring market shares makes the index rise sharply when large firms combine. Neither measure reflects entry barriers or demand elasticity."],
 ["In a Nash equilibrium:", ["all firms earn zero economic profit.", "firms jointly maximize industry profit.", "no firm can gain by changing its own strategy alone."], 2, "Each firm's choice is its best response given what the others do. This is why collusion is unstable: cheating is each member's best response."],
 ["A firm whose long-run average cost falls as it increases output is experiencing:", ["economies of scale.", "diseconomies of scale.", "diminishing marginal returns."], 0, "Declining long-run average cost with larger scale is the definition of economies of scale. Diminishing marginal returns is a short-run concept with a fixed input."],
]))

R.append(dict(id="bc", n="Understanding Business Cycles", k="CYCLES", w=3, c="#2e9e8f",
terms=[
 ["Business cycle", "İş çevrimi (konjonktür dalgası)", "Recurring fluctuations in economic activity around its long-term trend.", "Ekonomik faaliyetin uzun dönem eğilimi etrafında tekrarlayan dalgalanmaları."],
 ["Recovery", "Toparlanma", "The phase after a trough in which activity is below potential but starting to increase.", "Dip noktasından sonra, faaliyetin potansiyelin altında olduğu ama artmaya başladığı evre."],
 ["Expansion", "Genişleme", "The phase in which activity grows faster than trend and rises above potential.", "Faaliyetin eğilimin üzerinde büyüdüğü ve potansiyelin üzerine çıktığı evre."],
 ["Slowdown", "Yavaşlama", "The phase near the peak in which activity is above potential but its growth is weakening.", "Zirveye yakın, faaliyetin potansiyelin üzerinde olduğu ama büyümesinin zayıfladığı evre."],
 ["Contraction", "Daralma", "The phase in which activity falls and drops below potential.", "Faaliyetin gerilediği ve potansiyelin altına indiği evre."],
 ["Output gap", "Çıktı açığı", "The difference between actual output and potential output.", "Gerçekleşen çıktı ile potansiyel çıktı arasındaki fark."],
 ["Credit cycle", "Kredi çevrimi", "Fluctuations in the availability and cost of credit over time.", "Kredinin erişilebilirliğinde ve maliyetinde zaman içinde görülen dalgalanmalar."],
 ["Inventory-to-sales ratio", "Stok/satış oranı", "Inventories divided by sales; it rises when sales slow unexpectedly.", "Stokların satışlara bölümü; satışlar beklenmedik biçimde yavaşladığında yükselir."],
 ["Leading indicator", "Öncü gösterge", "A variable that tends to change direction before the economy does.", "Ekonomiden önce yön değiştirme eğiliminde olan değişken."],
 ["Coincident indicator", "Eşzamanlı gösterge", "A variable that changes direction at about the same time as the economy.", "Ekonomiyle yaklaşık aynı zamanda yön değiştiren değişken."],
 ["Lagging indicator", "Gecikmeli gösterge", "A variable that changes direction after the economy has already turned.", "Ekonomi yön değiştirdikten sonra yön değiştiren değişken."],
 ["Diffusion index", "Yayılım endeksi", "The proportion of the components of a composite indicator that are rising.", "Bileşik bir göstergenin bileşenlerinden yükselenlerin oranı."],
],
notes="""<h3>What a cycle is</h3>
<ul>
<li>Business cycles are recurring but not regular: their length and depth vary.</li>
<li>Three ways to define the cycle:</li>
<li><b>Classical cycle:</b> the level of economic activity rises and falls.</li>
<li><b>Growth cycle:</b> activity moves above and below its long-term trend. This is the usual view of analysts.</li>
<li><b>Growth rate cycle:</b> the growth rate itself rises and falls.</li>
</ul>
<h3>Four phases</h3>
<div class="tbl"><table>
<tr><th></th><th>Recovery</th><th>Expansion</th><th>Slowdown</th><th>Contraction</th></tr>
<tr><td>Activity vs potential</td><td>Below, rising</td><td>Above, rising</td><td>Above, growth weakening</td><td>Falling below</td></tr>
<tr><td>Employment</td><td>Layoffs slow; firms use overtime before hiring</td><td>Hiring picks up, unemployment falls</td><td>Hiring slows</td><td>Hours cut first, then layoffs</td></tr>
<tr><td>Business investment</td><td>Low but turning up</td><td>Strong</td><td>Slowing</td><td>Cut back</td></tr>
<tr><td>Inflation</td><td>Moderate</td><td>Picks up modestly</td><td>Accelerates</td><td>Decelerates, with a lag</td></tr>
</table></div>
<ul>
<li>The <b>peak</b> separates slowdown from contraction; the <b>trough</b> separates contraction from recovery.</li>
</ul>
<h3>How firms and households adjust</h3>
<ul>
<li><b>Inventories:</b> when sales slow near the peak, unsold goods pile up and the inventory-to-sales ratio rises. Firms then cut production by more than the fall in sales to run inventories down. In recovery the ratio falls and production is stepped up.</li>
<li><b>Labour:</b> hiring and firing are costly, so firms first change hours and overtime, and only later change headcount. That is why unemployment lags the cycle.</li>
<li><b>Capital spending:</b> postponed quickly in a downturn; early in a recovery firms use spare capacity before ordering new equipment.</li>
<li><b>Consumers:</b> spending on durable goods is the most cyclical, services less so, and non-durables such as food the least.</li>
<li><b>Housing:</b> sensitive to mortgage rates and incomes; it often leads the cycle.</li>
<li><b>External trade:</b> imports rise with domestic income; exports depend on growth abroad and on the exchange rate.</li>
</ul>
<h3>Credit cycles</h3>
<ul>
<li>In good times lenders loosen standards and credit expands; in bad times they tighten and credit contracts.</li>
<li>Credit cycles tend to be <b>longer</b> than business cycles, and are closely tied to property prices.</li>
<li>Downturns that coincide with a credit contraction are usually deeper and last longer.</li>
</ul>
<h3>Economic indicators</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>Typical examples</th></tr>
<tr><td>Leading</td><td>Share prices, building permits, new orders, average weekly hours in manufacturing, consumer expectations, yield curve spread</td></tr>
<tr><td>Coincident</td><td>Industrial production, real personal income, non-farm payroll employment, manufacturing and trade sales</td></tr>
<tr><td>Lagging</td><td>Average duration of unemployment, inventory-to-sales ratio, unit labour costs, bank lending rates, outstanding commercial loans, consumer credit to income</td></tr>
</table></div>
<ul>
<li>A <b>diffusion index</b> shows how widespread a move is: the share of an index's components that are increasing.</li>
<li><b>Nowcasting</b> uses high-frequency data to estimate the current state of the economy before official figures are published.</li>
</ul>
<div class="trap"><b>Exam trap</b>The unemployment rate keeps rising after a recovery has begun, and the inventory-to-sales ratio is a lagging indicator, not a leading one.</div>""",
qs=[
 ["The phase of the business cycle in which economic activity is below potential but beginning to increase is the:", ["recovery.", "slowdown.", "expansion."], 0, "Recovery starts at the trough: output is still below potential but is rising. In an expansion, activity is above potential."],
 ["Which of the following is most likely a leading economic indicator?", ["Building permits", "Industrial production", "Average duration of unemployment"], 0, "Building permits change before construction activity does. Industrial production is coincident and the average duration of unemployment is lagging."],
 ["Which of the following is most likely a lagging economic indicator?", ["Share prices", "Unit labour costs", "Real personal income"], 1, "Unit labour costs turn after the economy has turned. Share prices are leading and real personal income is coincident."],
 ["Near the peak of the business cycle, when sales begin to slow unexpectedly, the inventory-to-sales ratio most likely:", ["falls.", "rises.", "is unchanged."], 1, "Unsold goods accumulate while sales weaken, so the ratio rises. Firms then cut production to bring inventories back down."],
 ["Compared with business cycles, credit cycles are typically:", ["longer.", "shorter.", "of the same length."], 0, "Credit cycles tend to last longer than business cycles and are closely linked to property markets."],
 ["At the start of a contraction, firms are most likely to respond first by:", ["laying off a large share of the workforce.", "reducing overtime and hours worked.", "selling plant and equipment."], 1, "Changing headcount is costly, so firms adjust hours first and resort to layoffs only if the downturn persists."],
 ["Which category of consumer spending is typically the most sensitive to the business cycle?", ["Services", "Durable goods", "Non-durable goods"], 1, "Purchases of durable goods such as cars and appliances can be postponed, so they fall sharply in downturns and rebound strongly in recoveries."],
 ["A diffusion index for a composite of leading indicators measures the:", ["average change in the components.", "proportion of the components that are rising.", "difference between leading and lagging components."], 1, "A diffusion index shows how broad a move is by reporting the share of components that increased."],
 ["An analyst who defines the business cycle as fluctuations of economic activity around its long-term trend is using the:", ["growth cycle concept.", "classical cycle concept.", "growth rate cycle concept."], 0, "The growth cycle measures deviations from trend. The classical cycle looks at the level of activity and the growth rate cycle at changes in the growth rate."],
 ["Early in a recovery, the unemployment rate is most likely to:", ["fall immediately as firms rehire.", "remain high because firms first increase hours of existing staff.", "rise sharply because firms cut costs to restore profits."], 1, "Firms use overtime and existing capacity before committing to new hires, so unemployment lags the turn in activity."],
]))

R.append(dict(id="fp", n="Fiscal Policy", k="FISCAL", w=3, c="#c0563f",
terms=[
 ["Fiscal policy", "Maliye politikası", "The government's use of spending and taxation to influence the economy.", "Hükümetin ekonomiyi etkilemek için harcama ve vergilendirmeyi kullanması."],
 ["Budget deficit", "Bütçe açığı", "The amount by which government spending exceeds government revenue in a period.", "Bir dönemde kamu harcamalarının kamu gelirlerini aşan tutarı."],
 ["Transfer payments", "Transfer ödemeleri", "Payments such as pensions and unemployment benefits that redistribute income without buying goods or services.", "Emekli aylığı ve işsizlik ödeneği gibi, mal veya hizmet satın almadan geliri yeniden dağıtan ödemeler."],
 ["Direct taxes", "Dolaysız vergiler", "Taxes levied on income or wealth, such as income tax and corporate tax.", "Gelir vergisi ve kurumlar vergisi gibi gelir veya servet üzerinden alınan vergiler."],
 ["Indirect taxes", "Dolaylı vergiler", "Taxes levied on goods and services, such as value added tax and excise duties.", "Katma değer vergisi ve özel tüketim vergisi gibi mal ve hizmetler üzerinden alınan vergiler."],
 ["Automatic stabilizers", "Otomatik istikrar sağlayıcılar", "Built-in features of the budget that offset swings in activity without any new decision.", "Yeni bir karar gerekmeden faaliyet dalgalanmalarını dengeleyen, bütçenin yapısında bulunan unsurlar."],
 ["Discretionary fiscal policy", "İhtiyari maliye politikası", "Deliberate changes in spending or taxes decided by the government.", "Hükümetin kararıyla harcamalarda veya vergilerde yapılan bilinçli değişiklikler."],
 ["Fiscal multiplier", "Mali çarpan", "The ratio of the change in output to the change in government spending that caused it.", "Çıktıdaki değişimin, buna yol açan kamu harcaması değişimine oranı."],
 ["Marginal propensity to consume (MPC)", "Marjinal tüketim eğilimi", "The fraction of an additional unit of disposable income that is spent on consumption.", "Ek bir birim harcanabilir gelirin tüketime harcanan kısmı."],
 ["Crowding out", "Dışlama etkisi", "Government borrowing pushes up interest rates and reduces private investment.", "Kamu borçlanmasının faizleri yükseltmesi ve özel yatırımı azaltması."],
 ["Ricardian equivalence", "Ricardo denkliği", "The idea that households save a tax cut because they expect higher taxes later, so the cut has no effect on demand.", "Hanehalklarının ileride vergilerin artacağını bekleyerek vergi indirimini tasarruf ettiği, dolayısıyla indirimin talebi etkilemediği görüşü."],
 ["Structural budget deficit", "Yapısal bütçe açığı", "The deficit that would exist if the economy were operating at full employment.", "Ekonomi tam istihdamda çalışıyor olsaydı ortaya çıkacak açık."],
],
notes="""<h3>Purpose and stance</h3>
<ul>
<li>Fiscal policy uses government spending and taxes to influence aggregate demand, redistribute income and allocate resources.</li>
<li><b>Expansionary:</b> higher spending or lower taxes; the deficit widens or the surplus shrinks. <b>Contractionary:</b> the reverse.</li>
<li>Keynesians see fiscal policy as a powerful tool when there is spare capacity. Monetarists argue its effect is temporary and prefer steady monetary policy.</li>
</ul>
<h3>Tools</h3>
<div class="tbl"><table>
<tr><th>Spending</th><th>Revenue</th></tr>
<tr><td>Transfer payments: pensions, unemployment benefits</td><td>Direct taxes: on income, profits, wealth</td></tr>
<tr><td>Current spending: goods and services used now, such as health and defence</td><td>Indirect taxes: on spending, such as value added tax and excise duties</td></tr>
<tr><td>Capital spending: infrastructure that raises future capacity</td><td></td></tr>
</table></div>
<ul>
<li>Indirect taxes can be changed quickly and raise revenue at low cost, and they can discourage harmful consumption. Direct taxes are slower to change.</li>
<li>Capital spending takes a long time to plan and carry out.</li>
<li>Good tax policy is simple, efficient, fair and raises enough revenue.</li>
</ul>
<h3>The multiplier</h3>
<p class="f">fiscal multiplier = 1 / [1 − MPC × (1 − t)]</p>
<ul>
<li>A rise in spending becomes income for someone else, who spends part of it, and so on. Taxes and saving leak out at each round.</li>
<li>A higher MPC or a lower tax rate gives a larger multiplier.</li>
<li><b>Balanced budget multiplier:</b> raising spending and taxes by the same amount is still expansionary, because the whole of the spending enters demand while part of the tax would have been saved anyway.</li>
</ul>
<h3>Why fiscal policy may disappoint</h3>
<ul>
<li><b>Lags.</b> Recognition lag: seeing that action is needed. Action lag: passing and implementing it. Impact lag: waiting for the effect.</li>
<li><b>Crowding out:</b> borrowing to fund a deficit raises interest rates and displaces private investment.</li>
<li><b>Ricardian equivalence:</b> if taxpayers save more in anticipation of future taxes, a deficit-financed tax cut does not lift demand.</li>
<li>Supply constraints: if the economy is at full employment, extra demand mostly raises prices.</li>
<li>Misjudging the size of the output gap or the multiplier.</li>
</ul>
<h3>Automatic and discretionary</h3>
<ul>
<li><b>Automatic stabilizers</b> work without a decision: in a downturn tax receipts fall and unemployment benefits rise, cushioning demand.</li>
<li><b>Discretionary</b> measures are deliberate changes in tax rates or spending programmes and suffer most from lags.</li>
</ul>
<h3>Deficits and debt</h3>
<ul>
<li>The headline deficit moves with the cycle. The <b>structural (cyclically adjusted) deficit</b> removes that effect and is the better guide to the fiscal stance.</li>
<li>Reasons to worry about a high debt-to-GDP ratio: higher future taxes that blunt incentives, crowding out of private investment, and pressure on the central bank to finance the debt by creating money.</li>
<li>Reasons not to: debt owed to citizens is partly a transfer within the country, borrowing may fund productive capital, and deficits help when the economy is far below full employment.</li>
<li>Debt becomes harder to sustain when the real interest rate on it exceeds the economy's real growth rate.</li>
</ul>
<div class="trap"><b>Exam trap</b>A larger deficit does not by itself mean policy has been loosened. In a recession the deficit widens automatically. Look at the structural balance.</div>""",
qs=[
 ["The marginal propensity to consume is 0.8 and the tax rate is 25%. The fiscal multiplier is closest to:", ["1.67", "2.50", "5.00"], 1, "1 / [1 − 0.8 × (1 − 0.25)] = 1 / (1 − 0.6) = 2.50. Ignoring taxes gives 5.00."],
 ["A government increases its spending and its tax revenue by the same amount. The effect on aggregate demand is most likely:", ["expansionary.", "contractionary.", "neutral."], 0, "All of the extra spending adds to demand, but households would have saved part of the income taken in tax, so the net effect is positive."],
 ["According to Ricardian equivalence, a tax cut financed by government borrowing will:", ["raise consumption by the full amount of the tax cut.", "have no effect on aggregate demand because households save the tax cut.", "reduce aggregate demand because interest rates rise."], 1, "Households expect to repay the borrowing through higher future taxes and save the tax cut, leaving demand unchanged."],
 ["The crowding-out effect refers to government borrowing that:", ["reduces private investment by raising interest rates.", "reduces imports by weakening the currency.", "reduces tax revenue by slowing growth."], 0, "Larger government borrowing competes for funds, pushes up interest rates and displaces private investment."],
 ["Which of the following is most likely an automatic stabilizer?", ["A new infrastructure programme", "Unemployment benefit payments", "A one-off cut in corporate tax rates"], 1, "Unemployment benefits rise in a downturn without any new decision. The other two are discretionary measures."],
 ["The time it takes for a government to approve and implement a fiscal measure after recognizing the need for it is the:", ["action lag.", "impact lag.", "recognition lag."], 0, "The action lag is the delay in enacting and implementing policy. The impact lag is the delay before the policy affects the economy."],
 ["Compared with direct taxes, indirect taxes are most likely to:", ["be more progressive.", "take longer to change.", "be quicker to implement."], 2, "Taxes on spending can be changed almost immediately, while changes to income taxes take longer to enact and to affect behaviour."],
 ["The best indicator of whether fiscal policy is becoming more expansionary is an increase in the:", ["headline budget deficit.", "structural budget deficit.", "ratio of tax revenue to GDP."], 1, "The structural deficit strips out the effect of the cycle. The headline deficit also widens automatically in a recession."],
 ["Which of the following is an argument for being concerned about the size of a country's national debt?", ["The debt is owed mainly to the country's own citizens.", "Higher future tax rates may reduce incentives to work and invest.", "The borrowing has financed investment in productive infrastructure."], 1, "Servicing high debt may require higher taxes, which can discourage economic activity. The other statements are arguments against concern."],
 ["A government wants a fiscal measure that takes effect quickly. Which tool is least suitable?", ["A change in excise duties", "A change in transfer payments", "A programme of capital spending"], 2, "Capital projects take a long time to plan, approve and build, so their effect arrives late."],
]))

R.append(dict(id="mp", n="Monetary Policy", k="MONETARY", w=3, c="#8a5cc2",
terms=[
 ["Monetary policy", "Para politikası", "Central bank actions that influence the quantity of money and credit and the level of interest rates.", "Merkez bankasının para ve kredi miktarını ve faiz düzeyini etkileyen işlemleri."],
 ["Policy rate", "Politika faizi", "The interest rate the central bank sets or targets to steer short-term market rates.", "Merkez bankasının kısa vadeli piyasa faizlerini yönlendirmek için belirlediği veya hedeflediği faiz oranı."],
 ["Open market operations", "Açık piyasa işlemleri", "Purchases and sales of securities by the central bank to change bank reserves.", "Merkez bankasının banka rezervlerini değiştirmek için menkul kıymet alıp satması."],
 ["Reserve requirement", "Zorunlu karşılık", "The share of deposits that banks must hold as reserves.", "Bankaların mevduatın rezerv olarak tutmak zorunda olduğu kısmı."],
 ["Price stability", "Fiyat istikrarı", "Low and stable inflation; the main objective of most central banks.", "Düşük ve istikrarlı enflasyon; çoğu merkez bankasının temel amacı."],
 ["Inflation targeting", "Enflasyon hedeflemesi", "A framework in which the central bank announces an inflation target and sets policy to achieve it.", "Merkez bankasının bir enflasyon hedefi açıkladığı ve politikayı buna ulaşacak biçimde belirlediği çerçeve."],
 ["Transmission mechanism", "Aktarım mekanizması", "The channels through which a change in the policy rate affects prices and output.", "Politika faizindeki değişikliğin fiyatları ve çıktıyı etkilediği kanallar."],
 ["Neutral rate", "Nötr faiz", "The policy rate that neither stimulates nor restrains the economy.", "Ekonomiyi ne canlandıran ne de yavaşlatan politika faizi."],
 ["Central bank independence", "Merkez bankası bağımsızlığı", "Freedom of the central bank from political interference in setting policy.", "Merkez bankasının politika belirlerken siyasi müdahaleden uzak olması."],
 ["Liquidity trap", "Likidite tuzağı", "A situation in which people hold any extra money supplied, so increasing the money supply does not lower interest rates or raise spending.", "İnsanların arz edilen ek parayı elde tuttuğu, bu yüzden para arzını artırmanın faizleri düşürmediği veya harcamayı artırmadığı durum."],
 ["Quantitative easing (QE)", "Niceliksel genişleme", "Large-scale purchases of securities by the central bank to add liquidity when policy rates are near zero.", "Politika faizleri sıfıra yakınken likidite sağlamak için merkez bankasının büyük ölçekli menkul kıymet alımı."],
 ["Exchange rate targeting", "Döviz kuru hedeflemesi", "A framework in which the central bank keeps the currency within a band against another currency.", "Merkez bankasının para birimini başka bir para birimine karşı belirli bir bant içinde tuttuğu çerçeve."],
],
notes="""<h3>What central banks do</h3>
<ul>
<li>Sole issuer of currency, banker to the government and to banks, lender of last resort, holder of gold and foreign exchange reserves, often regulator of the payments system and of banks, and conductor of monetary policy.</li>
<li>The main objective is <b>price stability</b>. Some central banks also have mandates for employment, growth, financial stability or the exchange rate.</li>
<li>Unexpected inflation is costly: it redistributes wealth from lenders to borrowers and makes price signals unreliable.</li>
</ul>
<h3>Three tools</h3>
<div class="tbl"><table>
<tr><th>Tool</th><th>To expand</th><th>To contract</th></tr>
<tr><td>Open market operations</td><td>Buy securities: bank reserves rise</td><td>Sell securities: bank reserves fall</td></tr>
<tr><td>Policy rate</td><td>Lower it</td><td>Raise it</td></tr>
<tr><td>Reserve requirement</td><td>Lower it: banks can lend more</td><td>Raise it: banks can lend less</td></tr>
</table></div>
<h3>Transmission mechanism</h3>
<ul>
<li>A change in the policy rate works through four channels:</li>
<li><b>Market interest rates:</b> bank lending and deposit rates follow.</li>
<li><b>Asset prices:</b> higher discount rates lower the value of bonds, shares and property.</li>
<li><b>Expectations and confidence:</b> households and firms revise their views of future growth and inflation.</li>
<li><b>Exchange rate:</b> higher rates attract capital and strengthen the currency, which reduces net exports.</li>
<li>Together these change domestic demand and net external demand, and through them inflation.</li>
</ul>
<h3>What makes a central bank effective</h3>
<ul>
<li><b>Independence.</b> Operational independence: free to set the policy rate. Target independence: also free to define the inflation target.</li>
<li><b>Credibility:</b> the public believes the bank will do what it says, so expectations stay anchored.</li>
<li><b>Transparency:</b> the bank explains its view of the economy and its decisions.</li>
</ul>
<h3>Targeting frameworks</h3>
<ul>
<li><b>Inflation targeting:</b> an announced target, often around 2% with a band, pursued with the policy rate. The target is not zero, to keep a safety margin against deflation.</li>
<li><b>Exchange rate targeting:</b> the bank buys or sells its own currency to hold the rate. The country effectively imports the monetary policy and inflation rate of the anchor country and gives up independent control of domestic interest rates.</li>
</ul>
<h3>Is policy tight or loose?</h3>
<p class="f">neutral rate = real trend rate of growth + inflation target</p>
<ul>
<li>Policy rate above neutral: contractionary. Below neutral: expansionary.</li>
<li>The source of inflation matters. Against a <b>demand shock</b>, tightening is appropriate. Against a <b>supply shock</b> such as a jump in oil prices, tightening lowers output further.</li>
</ul>
<h3>Limits</h3>
<ul>
<li>The central bank controls short-term rates, not long-term rates. If markets doubt its resolve on inflation, long-term yields can rise when it eases.</li>
<li><b>Liquidity trap:</b> demand for money becomes so elastic that added money is simply held.</li>
<li>Policy rates cannot fall far below zero; banks may hoard reserves instead of lending. Quantitative easing tries to work around this.</li>
<li>Deflation is especially hard to fight because real debt burdens rise and spending is postponed.</li>
</ul>
<h3>Fiscal and monetary policy together</h3>
<div class="tbl"><table>
<tr><th>Fiscal</th><th>Monetary</th><th>Interest rates</th><th>Output</th><th>Private sector share</th></tr>
<tr><td>Expansionary</td><td>Expansionary</td><td>Lower</td><td>Higher</td><td>Private and public both grow</td></tr>
<tr><td>Expansionary</td><td>Contractionary</td><td>Higher</td><td>Depends</td><td>Falls: government share rises</td></tr>
<tr><td>Contractionary</td><td>Expansionary</td><td>Lower</td><td>Depends</td><td>Rises: government share falls</td></tr>
<tr><td>Contractionary</td><td>Contractionary</td><td>Higher</td><td>Lower</td><td>Private and public both shrink</td></tr>
</table></div>""",
qs=[
 ["An economy's real trend growth rate is 2% and its inflation target is 2%. If the policy rate is 5%, monetary policy is best described as:", ["neutral.", "expansionary.", "contractionary."], 2, "The neutral rate is 2% + 2% = 4%. A policy rate above neutral restrains the economy."],
 ["A central bank that buys government securities in the open market will most likely:", ["increase bank reserves.", "decrease the money supply.", "increase short-term interest rates."], 0, "Payment for the securities adds to bank reserves, which expands lending capacity and puts downward pressure on short-term rates."],
 ["An increase in the policy rate is least likely to be transmitted to the economy through:", ["asset prices.", "the exchange rate.", "government spending."], 2, "The four channels are market interest rates, asset prices, expectations and the exchange rate. Government spending is a fiscal policy tool."],
 ["In a liquidity trap, an increase in the money supply will most likely:", ["cause a sharp rise in inflation.", "have little effect on interest rates or spending.", "cause a large fall in long-term interest rates."], 1, "The extra money is simply held, so interest rates do not fall further and spending does not respond."],
 ["A country that targets its exchange rate against the currency of a larger trading partner will most likely:", ["retain full control over domestic interest rates.", "end up with an inflation rate similar to that of the partner.", "eliminate the need to hold foreign exchange reserves."], 1, "Holding the exchange rate ties domestic monetary conditions to those of the anchor country, so inflation converges. Reserves are needed to defend the target."],
 ["A central bank that is free to set the policy rate but must aim for an inflation target chosen by the government has:", ["target independence only.", "operational independence only.", "both operational and target independence."], 1, "Operational independence covers how policy is conducted. Target independence would also let the bank define the inflation target."],
 ["If fiscal policy is expansionary and monetary policy is contractionary, the most likely result is:", ["lower interest rates and a larger private sector share of the economy.", "higher interest rates and a larger government share of the economy.", "lower interest rates and a smaller government share of the economy."], 1, "Government demand grows while tight money raises interest rates and restrains private spending, so the public sector's share increases."],
 ["An increase in the reserve requirement will most likely:", ["increase the funds banks have available to lend.", "decrease the funds banks have available to lend.", "have no effect on bank lending."], 1, "Banks must hold a larger share of deposits as reserves, leaving less to lend, which contracts the money supply."],
 ["Inflation rises because of a sharp increase in oil prices while output falls. If the central bank tightens policy in response, the most likely result is that:", ["output falls further.", "output returns quickly to trend.", "inflation rises further."], 0, "This is a supply shock. Tightening reduces demand and so deepens the fall in output."],
 ["Most inflation-targeting central banks choose a target above zero mainly to:", ["raise government revenue.", "weaken the exchange rate.", "reduce the risk of deflation."], 2, "A small positive target leaves a buffer so that negative shocks do not push the economy into deflation, which is hard to reverse."],
]))
