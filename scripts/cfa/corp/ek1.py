# CFA Level I · Corporate Issuers · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
EK = {}

EK["of"] = dict(
terms=[
 ["Limited liability partnership (LLP)", "Sınırlı sorumlu ortaklık", "A partnership in which no partner is personally liable for the firm's debts beyond their investment.", "Hiçbir ortağın, yatırdığı tutarın ötesinde ortaklığın borçlarından kişisel olarak sorumlu olmadığı ortaklık."],
 ["Pass-through taxation", "Doğrudan ortaklara geçen vergilendirme", "Taxation in which business profits are taxed only once, as income of the owners.", "İşletme kârının yalnızca bir kez, sahiplerin geliri olarak vergilendirilmesi."],
],
notes="""<h3>More on organizational forms</h3>
<ul>
<li>A <b>limited partnership</b> needs at least one general partner (unlimited liability, runs the business) and at least one limited partner (liability limited to the investment, no role in management).</li>
<li>General partners usually receive a <b>larger share of profits</b> because they manage the business and bear unlimited liability.</li>
<li>Sole proprietorships and partnerships are <b>pass-through</b>: profits are taxed once, at the owners' level. Corporations may face <b>double taxation</b>.</li>
<li>Only the corporation is a <b>separate legal entity</b>; this, plus limited liability, makes raising capital easier.</li>
<li>Regulators typically require periodic financial disclosure from <b>listed</b> companies only.</li>
<li>To raise new equity and list shares, a company uses an <b>IPO</b>; a direct listing lists existing shares without raising capital.</li>
</ul>""",
qs=[
 ["Three founders of a consulting firm want two of them to run the business with unlimited liability while the third invests capital only, with liability limited to that investment. The most appropriate form is a:", ["general partnership.", "limited partnership.", "limited liability partnership."], 1, "A limited partnership combines general partners who manage with limited partners who only invest."],
 ["The minimum number of partners needed to form a limited partnership is:", ["one general partner and one limited partner.", "two general partners and one limited partner.", "one general partner and two limited partners."], 0, "At least one partner of each kind is required."],
 ["The owner of a sole proprietorship is liable for the business's obligations:", ["without limit.", "up to the amount invested.", "only if the business is incorporated."], 0, "There is no legal separation between a sole proprietor and the business."],
 ["Compared with limited partners, the general partners of a limited partnership typically:", ["receive a larger share of profits.", "receive a smaller share of profits.", "have no say in business decisions."], 0, "General partners run the business and bear unlimited liability, so they are rewarded with a larger share."],
 ["Which statement about the taxation of business forms is most accurate?", ["Corporate shareholders never pay tax on dividends.", "General partnership profits are taxed only at the level of the partners.", "Limited partners pay all of the tax due on a limited partnership's profits."], 1, "Partnerships are pass-through entities: all partners, general and limited, pay tax on their shares."],
 ["Periodic public disclosure of financial results is typically required by regulators for:", ["private companies only.", "listed companies only.", "both private and listed companies."], 1, "Listing brings disclosure obligations that private companies usually do not have."],
 ["A private company wants to raise new equity capital and have its shares trade on an exchange. It will most likely use:", ["an initial public offering.", "a direct listing.", "a leveraged buyout."], 0, "An IPO sells new shares to the public; a direct listing raises no new capital."],
 ["Profits may be taxed twice, once at the entity level and again when distributed to owners, under a:", ["corporation.", "general partnership.", "limited partnership."], 0, "Corporations pay tax on profits, and shareholders then pay tax on dividends."],
 ["Which of the following organizational forms is a separate legal entity from its owners?", ["Corporation", "General partnership", "Sole proprietorship"], 0, "A corporation can own assets, enter contracts and be sued in its own name."],
 ["In a limited partnership, the limited partners are most likely to:", ["manage daily operations.", "have unlimited liability for the partnership's debts.", "have no involvement in management decisions."], 2, "Limited partners are passive investors; taking part in management can put their limited liability at risk."],
])

EK["st"] = dict(
terms=[
 ["Contractual obligation", "Sözleşmesel yükümlülük", "A payment the company is legally bound to make, such as interest and principal on debt.", "Şirketin yapmakla hukuken yükümlü olduğu ödeme; örneğin borcun faiz ve anapara ödemeleri."],
],
notes="""<h3>Risk preferences of stakeholders</h3>
<ul>
<li><b>Shareholders</b> have unlimited upside and limited downside, so they tend to prefer <b>more risk</b>. Creditors have limited upside (interest and principal) and prefer <b>less risk</b>.</li>
<li>Managers and directors may prefer less risk than shareholders, because their jobs and reputations depend on the company's survival.</li>
<li>Interest and principal are <b>contractual obligations</b>; dividends on common and preferred shares are paid at the board's discretion.</li>
<li><b>Shareholder theory:</b> governance focuses on the conflict between managers and owners. <b>Stakeholder theory:</b> governance also takes in employees, customers, suppliers, communities and regulators.</li>
</ul>""",
qs=[
 ["Under the stakeholder theory of corporate governance, the interests of local communities affected by a company's operations are:", ["ignored.", "considered alongside those of shareholders.", "considered only when they increase share value."], 1, "Stakeholder theory widens governance beyond shareholders to all groups affected by the company."],
 ["Under shareholder theory, corporate governance focuses mainly on conflicts between a company's managers and its:", ["owners.", "suppliers.", "employees."], 0, "Shareholder theory centres on aligning managers with the owners' interest in value."],
 ["A company takes on riskier projects to grow faster. This change is most likely to be favoured by:", ["its lenders only.", "its shareholders only.", "both its lenders and its shareholders."], 1, "Shareholders capture the upside; lenders bear more default risk without higher returns."],
 ["Which stakeholder group typically prefers the most business risk?", ["Shareholders", "Senior managers", "Creditors"], 0, "Their upside is unlimited and their loss is limited to their investment."],
 ["A company is legally required to make which of the following payments?", ["Interest and principal on its debt", "Dividends on its preferred shares", "Dividends on its common shares"], 0, "Dividends are declared at the board's discretion; debt service is contractual."],
 ["The stakeholders least likely to favour a high-risk strategy with the potential for superior returns are the company's:", ["creditors.", "shareholders.", "activist investors."], 0, "Creditors do not share in the upside but do suffer if the company defaults."],
])

EK["cg"] = dict(
terms=[
 ["Remuneration committee", "Ücret komitesi", "The board committee that sets the pay of senior executives.", "Üst yöneticilerin ücretini belirleyen yönetim kurulu komitesi."],
 ["Nominations committee", "Aday gösterme komitesi", "The board committee that recruits board members and assesses their independence.", "Yönetim kurulu üyelerini bulan ve bağımsızlıklarını değerlendiren komite."],
 ["Risk committee", "Risk komitesi", "The board committee that oversees the company's risk policies and risk appetite.", "Şirketin risk politikalarını ve risk iştahını gözeten komite."],
],
notes="""<h3>Board committees and governance risks</h3>
<div class="tbl"><table>
<tr><th>Committee</th><th>Main responsibilities</th></tr>
<tr><td>Audit</td><td>Financial reporting, internal controls, selecting and overseeing the external auditor</td></tr>
<tr><td>Remuneration (compensation)</td><td>Pay of the CEO and senior executives</td></tr>
<tr><td>Nominations</td><td>Recruiting directors, assessing their independence</td></tr>
<tr><td>Governance</td><td>Governance policies, code of ethics, board evaluation</td></tr>
<tr><td>Risk</td><td>Risk policy and risk appetite</td></tr>
</table></div>
<p>Weak governance leads to poorer decisions, weaker financial performance and <b>higher default risk</b>.</p>""",
qs=[
 ["Which board committee is most likely to set the chief executive officer's pay package?", ["Remuneration committee", "Nominations committee", "Risk committee"], 0, "Executive pay is the remuneration (compensation) committee's job."],
 ["Which of the following is least likely a consequence of weak corporate governance?", ["Higher default risk", "Lower default risk", "Poorer decision making"], 1, "Ineffective governance raises, not lowers, default risk."],
 ["A principal-agent relationship most likely exists between a company's:", ["shareholders and managers.", "suppliers and customers.", "directors and regulators."], 0, "Shareholders (principals) hire managers (agents) to act on their behalf."],
 ["Which of the following is least likely a responsibility of the nominations committee?", ["Recruiting new directors", "Assessing directors' independence", "Selecting the external auditor"], 2, "Selecting the auditor, subject to shareholder approval, is the audit committee's task."],
])

EK["wc"] = dict(
terms=[
 ["Permanent working capital", "Kalıcı işletme sermayesi", "The minimum level of current assets a company needs at all times.", "Şirketin her zaman ihtiyaç duyduğu asgari dönen varlık düzeyi."],
 ["Variable (seasonal) working capital", "Değişken (mevsimsel) işletme sermayesi", "Current assets needed above the permanent level, for example in peak seasons.", "Kalıcı düzeyin üstünde, örneğin yoğun sezonda ihtiyaç duyulan dönen varlıklar."],
 ["Moderate working capital approach", "Ölçülü işletme sermayesi yaklaşımı", "Funding permanent needs with long-term sources and variable needs with short-term sources.", "Kalıcı ihtiyaçları uzun vadeli, değişken ihtiyaçları kısa vadeli kaynakla finanse etme."],
],
notes="""<h3>Funding approaches for working capital</h3>
<div class="tbl"><table>
<tr><th>Approach</th><th>Permanent needs</th><th>Variable needs</th><th>Effect</th></tr>
<tr><td>Conservative</td><td>Long-term</td><td>Long-term (mostly)</td><td>Lower risk, higher cost, lower profitability</td></tr>
<tr><td>Moderate</td><td>Long-term</td><td>Short-term</td><td>Matches maturities</td></tr>
<tr><td>Aggressive</td><td>Short-term (partly)</td><td>Short-term</td><td>Cheaper, more refinancing risk</td></tr>
</table></div>
<ul>
<li>Long-term funding includes both long-term debt and equity.</li>
<li>CCC = DOH + DSO − DPO. If all three double, the CCC doubles. A fall in DPO <b>raises</b> the CCC by the same number of days.</li>
<li>Prepaid sales and low inventory give a low (even negative) CCC. Tighter credit from suppliers lowers DPO and raises the CCC.</li>
<li>A very high CCC suggests that too much is invested in working capital.</li>
<li>The quick ratio excludes inventory, the least liquid current asset.</li>
</ul>""",
qs=[
 ["A company funds its permanent current assets with long-term sources and its seasonal current assets with short-term borrowing. Its approach to working capital is best described as:", ["conservative.", "moderate.", "aggressive."], 1, "Matching each need with funding of similar maturity is the moderate approach."],
 ["Which funding mix is most consistent with a moderate approach to working capital?", ["Permanent needs funded with equity; variable needs with short-term debt", "Permanent needs funded with short-term debt; variable needs with long-term debt", "Both permanent and variable needs funded with long-term debt"], 0, "Equity is a long-term source, so this matches long-term funding to permanent needs."],
 ["A retailer collects most of its sales in advance and keeps very little inventory. Its cash conversion cycle is most likely:", ["low.", "high.", "equal to its days of inventory on hand."], 0, "Low DSO and low DOH both shorten the cycle."],
 ["A company's days of inventory on hand, days sales outstanding and days payable outstanding all double. Its positive cash conversion cycle will:", ["remain unchanged.", "increase by less than double.", "double."], 2, "Each term doubles, so (2·DOH + 2·DSO − 2·DPO) is twice the original cycle."],
 ["A company's days payable outstanding falls from 45 to 35 days, with inventory and receivable days unchanged. Its cash conversion cycle will:", ["fall by 10 days.", "rise by 10 days.", "rise by about 22%."], 1, "DPO is subtracted, so 10 fewer payable days add 10 days to the cycle."],
 ["A supplier offers terms of 3/20 net 60. The company can borrow from its bank at 9%. Which source of financing is cheaper?", ["The bank loan", "The supplier's credit", "They cost the same"], 0, "Forgoing a 3% discount for 40 extra days costs about (1 + 3/97)^(365/40) − 1 ≈ 32% a year, far above 9%."],
 ["A company's cash conversion cycle has lengthened each year for three years. Which is the most likely cause?", ["Its suppliers have shortened the credit they give it.", "It is collecting receivables faster.", "It is turning over inventory faster."], 0, "Shorter supplier credit lowers DPO and lengthens the cycle; the other two shorten it."],
 ["Which of the following is most consistent with a conservative approach to working capital?", ["Funding inventory with long-term debt", "Funding rent payments with short-term debt", "Funding all current assets with short-term debt"], 0, "Conservative policies rely on long-term sources even for current needs."],
 ["A company replaces short-term borrowing with long-term debt to fund its inventory. This is most likely to increase its:", ["profitability.", "financing costs.", "refinancing risk."], 1, "Long-term funds usually cost more, so costs rise while refinancing risk falls."],
 ["A very high cash conversion cycle most likely indicates that a company's investment in working capital is:", ["too low.", "appropriate.", "too high."], 2, "Cash is tied up for long periods in inventory and receivables."],
])

EK["ci"] = dict(
terms=[
 ["Going concern project", "Faaliyetin sürekliliği projesi", "A capital investment to maintain the business or lower its costs, such as replacing equipment.", "İşi sürdürmek veya maliyetleri düşürmek için yapılan yatırım; örneğin ekipman yenileme."],
 ["Regulatory or compliance project", "Mevzuata uyum projesi", "An investment required by regulators or insurers, often for safety or environmental reasons, that produces little or no revenue.", "Düzenleyici veya sigortacıların zorunlu kıldığı, genellikle güvenlik veya çevre amaçlı, az gelir üreten veya hiç gelir üretmeyen yatırım."],
 ["Post-audit", "Sonradan denetim", "Comparing a project's actual results with its forecasts, to improve future forecasting.", "Bir projenin gerçekleşen sonuçlarını tahminlerle karşılaştırıp gelecekteki tahminleri iyileştirme."],
 ["Externality", "Dışsallık", "An effect of a project on the company's other businesses, positive or negative.", "Bir projenin şirketin diğer işleri üzerindeki olumlu veya olumsuz etkisi."],
 ["Timing option", "Zamanlama opsiyonu", "The right to delay an investment until more information is available.", "Daha fazla bilgi gelene kadar yatırımı erteleme hakkı."],
 ["Sizing option", "Ölçek opsiyonu", "The right to expand (growth option) or abandon a project later.", "Projeyi ileride büyütme (büyüme opsiyonu) veya terk etme hakkı."],
 ["Flexibility option", "Esneklik opsiyonu", "The right to change operating decisions such as prices, inputs or products made.", "Fiyat, girdi veya üretilen ürün gibi faaliyet kararlarını değiştirme hakkı."],
 ["Fundamental option", "Temel opsiyon", "A project whose payoff depends on an underlying price, such as a mine that is opened only if the commodity price is high.", "Getirisi bir dayanak fiyata bağlı olan proje; örneğin emtia fiyatı yüksekse açılan maden."],
],
notes="""<h3>Types of capital investment</h3>
<ul>
<li><b>Going concern</b> (maintenance, replacement, cost reduction), <b>regulatory/compliance</b> (little or no revenue), <b>expansion</b> of the existing business, and <b>new products or markets</b>, which need the most detailed analysis because their forecasts are most uncertain.</li>
<li>Steps of the capital allocation process: idea generation, analysing proposals, planning the capital budget, monitoring and post-audit. Arranging financing is not one of them.</li>
<li>Principles: decisions use <b>after-tax incremental cash flows</b> and their timing; include opportunity costs and externalities; ignore sunk costs; financing costs are reflected in the discount rate.</li>
</ul>
<h3>Real options</h3>
<div class="tbl"><table>
<tr><th>Option</th><th>Example</th></tr>
<tr><td>Timing</td><td>Delay the start of a project</td></tr>
<tr><td>Sizing (expansion or abandonment)</td><td>Enlarge a plant later; close it if it becomes unprofitable</td></tr>
<tr><td>Flexibility</td><td>Change prices, inputs or products, such as converting a production line</td></tr>
<tr><td>Fundamental</td><td>Open a mine when the metal price rises; buy film rights to a book</td></tr>
</table></div>
<p>A real option is a right, not an obligation, so its value can <b>never be negative</b>. If NPV is negative, the discount rate is above the IRR.</p>""",
qs=[
 ["A project requires 250,000 today and returns 70,000, 90,000, 60,000, 85,000 and 100,000 at the end of Years 1 to 5. At a required return of 10%, its NPV is closest to:", ["53,200", "75,800", "155,000"], 0, "Discounting each flow at 10% gives a present value of about 303,200; minus 250,000 gives about 53,200. The 155,000 option ignores discounting."],
 ["A machine costs 30,000 and increases after-tax cash flows by 8,000 a year for four years and 6,500 a year for the two years after that. Its IRR is closest to:", ["12.6%", "13.6%", "14.6%"], 1, "The rate that sets the present value of the inflows equal to 30,000 is about 13.6%."],
 ["A project costs 15,000 and returns 4,200 a year for five years. At a cost of capital of 9%, its NPV is closest to:", ["−1,340", "+1,340", "+16,340"], 1, "4,200 × 3.8897 = 16,337; minus 15,000 = +1,337. The third option forgets the initial outlay."],
 ["A company can spend 480,000 to develop a site that will produce 150,000 a year for six years and then cost 120,000 to restore in Year 7. Alternatively it can sell the site today. At a required return of 14%, the minimum price it should accept is closest to:", ["55,300", "103,300", "535,300"], 0, "PV of inflows 583,300 minus PV of the restoration cost 48,000 gives 535,300; minus the 480,000 outlay gives an NPV of about 55,300, the value the company would give up by selling."],
 ["An investment costs 600,000 and returns 250,000 at the end of Years 2 and 3 and 300,000 at the end of Year 4. Its IRR is closest to:", ["8.0%", "10.0%", "12.0%"], 1, "The rate that makes the present value of the three inflows equal to 600,000 is about 10%."],
 ["An investment costs 120,000 and returns 12,000, 16,000 and 20,000 in Years 1 to 3, plus 130,000 from its sale at the end of Year 3. At a required return of 11%, its NPV is closest to:", ["−58,000", "+13,500", "+58,000"], 1, "PV of all inflows ≈ 133,500; minus 120,000 ≈ +13,500."],
 ["A project has an NPV of 4.5 million and an IRR of 11%, and the company's cost of capital is 9%. The company should:", ["accept it, based on both NPV and IRR.", "accept it, based on NPV only.", "reject it, because the IRR is too low."], 0, "NPV is positive and IRR exceeds the cost of capital, so both rules say accept."],
 ["If a project's NPV is negative, the discount rate used is:", ["below its IRR.", "equal to its IRR.", "above its IRR."], 2, "NPV falls as the discount rate rises and is zero at the IRR."],
 ["A company spent 80,000 on a market study last year for a new product, and the product is expected to increase sales of one of its existing products. In evaluating the new product, the company should:", ["include both the study cost and the effect on the existing product.", "exclude the study cost and include the effect on the existing product.", "include the study cost and exclude the effect on the existing product."], 1, "The study is a sunk cost; the effect on the other product is a positive externality."],
 ["Which item is least relevant when estimating a project's cash flows?", ["Sunk costs", "Opportunity costs", "Taxes"], 0, "Money already spent does not change with the decision."],
 ["Which type of capital investment typically requires the most detailed analysis?", ["Replacing a machine to lower costs", "A safety upgrade required by regulators", "Launching a new product in a new market"], 2, "New products and markets have the most uncertain forecasts."],
 ["Which of the following is least likely a step in the capital allocation process?", ["Generating investment ideas", "Arranging financing for projects", "Conducting a post-audit"], 1, "The steps are idea generation, analysis, planning the capital budget, and monitoring with post-audit."],
 ["Capital investments that typically produce little or no revenue are:", ["regulatory or compliance projects.", "expansion projects.", "new market projects."], 0, "They are made to meet safety or environmental requirements and keep the business running."],
 ["Which of the following is a basic principle of capital allocation?", ["Decisions are based on cash flows.", "Projects are analysed before taxes.", "Opportunity costs are excluded."], 0, "Capital allocation uses after-tax incremental cash flows, including opportunity costs."],
 ["A copper producer decides to open a new mine after a sustained rise in copper prices. This is best described as a:", ["timing option.", "flexibility option.", "fundamental option."], 2, "The project's value depends directly on the price of the underlying commodity."],
 ["A publisher pays for the right to turn a popular novel into a television series at some point in the future. This is best described as a:", ["fundamental option.", "flexibility option.", "sizing option."], 0, "The value of the right depends on the future value of the underlying project, the series itself."],
 ["A manufacturer installs equipment that will let it switch one of its petrol-engine production lines to electric engines in a few years. This is best described as a:", ["timing option.", "flexibility option.", "growth option."], 1, "Flexibility options let the company change the products it makes or the inputs it uses."],
 ["Which of the following is an example of a flexibility option?", ["The right to raise the product's price if demand is strong", "The right to double the plant's capacity in four years", "The right to close the plant if production becomes unprofitable"], 0, "Price-setting and production options are flexibility options; expanding or closing are sizing options."],
 ["The value of a real option:", ["can never be negative.", "is negative if the project's NPV is negative.", "is negative if the option is not exercised."], 0, "An option is a right, so the holder can always walk away."],
])

EK["cs"] = dict(
terms=[
 ["Bonding costs", "Bağlılık maliyetleri", "Costs managers bear to assure shareholders they will act in their interest, such as non-compete agreements; part of the net agency cost of equity.", "Yöneticilerin hissedarlara onların çıkarına davranacağını güvence altına almak için katlandığı maliyetler; örneğin rekabet yasağı sözleşmeleri. Özsermayenin net vekâlet maliyetinin parçasıdır."],
 ["Monitoring costs", "Gözetim maliyetleri", "Costs of supervising management, such as board oversight and audit fees.", "Yönetimi denetlemenin maliyetleri; örneğin yönetim kurulu gözetimi ve denetim ücretleri."],
 ["Residual loss", "Kalıntı kayıp", "Agency costs that remain even with monitoring and bonding in place.", "Gözetim ve bağlılık önlemlerine rağmen kalan vekâlet maliyetleri."],
],
notes="""<h3>More on capital structure theories</h3>
<ul>
<li><b>MM Proposition I without taxes:</b> capital structure does not affect firm value. <b>With taxes:</b> value rises with debt because of the tax shield, so the optimum is <b>100% debt</b>.</li>
<li><b>MM Proposition II:</b> the cost of equity rises with leverage. With taxes, WACC falls as leverage rises; firm value is maximized where WACC is minimized.</li>
<li><b>Static trade-off:</b> the tax shield is balanced against financial distress costs. Value of the levered firm = value unlevered + PV of tax shield − PV of distress costs. The optimum is where the levered firm's value exceeds the unlevered firm's by the most; WACC first falls, then rises.</li>
<li><b>Pecking order:</b> internal funds first, then debt, then new equity, because new equity sends the most negative signal.</li>
<li><b>Net agency cost of equity</b> = monitoring costs + bonding costs + residual loss.</li>
<li>Deviations from the target structure caused by market price moves or minimum issue sizes matter less than <b>deliberate</b> deviations, such as choosing to issue debt.</li>
</ul>
<p class="f">WACC = w<sub>d</sub> × r<sub>d</sub> × (1 − t) + w<sub>e</sub> × r<sub>e</sub></p>""",
qs=[
 ["A company needs a large amount of capital for an acquisition. Under the pecking order theory, it should prefer to use:", ["internal funds, because they send the least negative signal.", "new equity, because it does not add leverage.", "new debt, because it is cheapest."], 0, "The order of preference is internal funds, then debt, then new equity."],
 ["According to the static trade-off theory:", ["new debt is always better than new equity.", "an optimal proportion of debt maximizes firm value.", "companies should use less debt as their tax rate rises."], 1, "The tax benefit of debt is balanced against distress costs to find an optimum."],
 ["A company will fund a 40 million project with 16 million of debt and 24 million of equity, matching its current structure. The pre-tax cost of debt is 8%, the cost of equity is 14% and the tax rate is 30%. The discount rate for the project is closest to:", ["10.6%", "11.6%", "12.0%"], 0, "0.4 × 8% × 0.7 + 0.6 × 14% = 2.24% + 8.40% = 10.64%."],
 ["A company has debt with a market value of 25 million and equity with a market value of 50 million. The pre-tax cost of debt is 7%, the cost of equity 13% and the tax rate 25%. If these weights are its target, its WACC is closest to:", ["9.8%", "10.4%", "11.0%"], 1, "(1/3) × 7% × 0.75 + (2/3) × 13% = 1.75% + 8.67% = 10.42%."],
 ["A company requires its senior managers to sign non-compete agreements. The costs of these agreements are:", ["bonding costs, part of the net agency cost of equity.", "monitoring costs, part of the pecking order theory.", "residual losses, part of financial distress costs."], 0, "Bonding costs make it less attractive for managers to act against shareholders or to leave."],
 ["Under Modigliani and Miller's Proposition I without taxes, a company's value:", ["rises as it uses more debt.", "falls as it uses more equity.", "is unaffected by its capital structure."], 2, "With perfect markets and no taxes, the way cash flows are split does not change their total value."],
 ["Under the static trade-off theory, the optimal capital structure is where:", ["the unlevered company's value is highest.", "financial distress costs are lowest.", "the levered company's value exceeds the unlevered company's value by the most."], 2, "At that point the marginal tax benefit equals the marginal distress cost."],
 ["Under Modigliani and Miller's model with taxes, the optimal capital structure is:", ["100% equity.", "50% debt and 50% equity.", "100% debt."], 2, "Each additional unit of debt adds tax shield value and there are no distress costs."],
 ["Which statement about the static trade-off theory is most accurate?", ["The cost of equity rises as leverage increases.", "WACC first rises and then falls as leverage increases.", "The tax shield's value first rises and then falls."], 0, "Shareholders demand more return as risk grows. WACC first falls and then rises."],
 ["An analyst sees that three companies have moved away from their target capital structures. Which deviation should concern her most?", ["Company A, whose equity weight fell because its share price dropped", "Company B, whose debt weight rose because it chose to issue new debt", "Company C, whose equity weight rose because of a minimum issue size"], 1, "A deliberate change by management is more significant than deviations caused by markets or issue sizes."],
 ["Under Modigliani and Miller's Proposition II with taxes:", ["WACC rises as leverage rises.", "firm value is highest where WACC is lowest.", "a 50/50 structure maximizes value."], 1, "With taxes, more debt lowers WACC and raises value."],
])

EK["bm"] = dict(
terms=[
 ["Tiered pricing", "Kademeli fiyatlama", "Charging different prices depending on the volume purchased.", "Satın alınan miktara göre farklı fiyat uygulama."],
 ["Dynamic pricing", "Dinamik fiyatlama", "Charging different prices at different times, depending on demand.", "Talebe bağlı olarak farklı zamanlarda farklı fiyat uygulama."],
 ["Add-on pricing", "Ek ürün fiyatlaması", "Selling a base product and charging extra, often at high margins, for options and upgrades.", "Temel ürünü satıp seçenek ve yükseltmeler için, çoğu zaman yüksek marjla, ek ücret alma."],
 ["Hidden revenue", "Gizli gelir modeli", "Giving a service free to users and earning revenue from third parties such as advertisers.", "Hizmeti kullanıcılara ücretsiz verip geliri reklamverenler gibi üçüncü taraflardan elde etme."],
 ["Penetration pricing", "Pazara giriş fiyatlaması", "Setting a low price to enter a market and build share.", "Pazara girmek ve pay kazanmak için düşük fiyat belirleme."],
 ["Value-based pricing", "Değere dayalı fiyatlama", "Setting price according to the value customers place on the product.", "Fiyatı müşterilerin ürüne verdiği değere göre belirleme."],
 ["B2B", "İşletmeden işletmeye (B2B)", "A business that sells its products or services to other businesses.", "Ürün veya hizmetlerini başka işletmelere satan şirket."],
 ["Direct sales", "Doğrudan satış", "A channel strategy in which the company sells to end customers without intermediaries.", "Şirketin aracı olmadan son müşteriye sattığı kanal stratejisi."],
],
notes="""<h3>Pricing models</h3>
<div class="tbl"><table>
<tr><th>Model</th><th>Idea</th></tr>
<tr><td>Value-based</td><td>Price set by value to the customer, such as richer standard features at a higher price</td></tr>
<tr><td>Tiered</td><td>Price depends on volume purchased</td></tr>
<tr><td>Dynamic</td><td>Price depends on time and demand (peak and off-peak)</td></tr>
<tr><td>Penetration</td><td>Low entry price to gain share</td></tr>
<tr><td>Freemium</td><td>Basic version free, extra features paid</td></tr>
<tr><td>Hidden revenue</td><td>Free to users, paid by advertisers or other third parties</td></tr>
<tr><td>Bundling</td><td>Several products sold together</td></tr>
<tr><td>Add-on</td><td>Base product plus high-margin extras</td></tr>
<tr><td>Razors and blades</td><td>Cheap device, profitable consumables</td></tr>
</table></div>
<p>A business model describes the customer, the product, the <b>channel strategy</b> (such as direct sales or distributors) and the pricing.</p>""",
qs=[
 ["A wholesaler charges lower unit prices to customers who buy larger quantities. This is best described as:", ["tiered pricing.", "dynamic pricing.", "penetration pricing."], 0, "Prices set by volume purchased are tiered pricing."],
 ["A cinema charges half price on weekday afternoons and raises prices by 25% on weekend evenings. This is best described as:", ["tiered pricing.", "dynamic pricing.", "value-based pricing."], 1, "Prices vary with the time of use and the level of demand."],
 ["A company that describes itself as B2B:", ["sells to other businesses.", "sells directly to consumers.", "acts as a marketplace for buyers and sellers."], 0, "B2B means business to business."],
 ["A furniture maker sells its sofas at a standard price but earns high margins on optional extras such as premium fabrics and stain protection. This is best described as:", ["add-on pricing.", "bundling.", "hidden revenue."], 0, "A base product plus high-margin optional extras is add-on pricing."],
 ["A company that describes itself as a direct sales business is describing its:", ["product.", "pricing strategy.", "channel strategy."], 2, "How a company reaches its customers is its channel strategy."],
 ["A new coffee brand launches at a price well below competitors' to win customers, and later offers discounts that increase with order size. These strategies are best described as:", ["penetration pricing, then tiered pricing.", "freemium pricing, then dynamic pricing.", "penetration pricing, then dynamic pricing."], 0, "A low entry price is penetration pricing; volume discounts are tiered pricing."],
 ["A music app lets users download a basic version at no charge and sells premium features separately. This is best described as:", ["freemium pricing.", "hidden revenue.", "penetration pricing."], 0, "Free basic access with paid upgrades is freemium."],
 ["A mobile game will be free, with no paid features, and will earn its revenue only from advertising. The most appropriate pricing model is:", ["freemium pricing.", "hidden revenue.", "penetration pricing."], 1, "Users pay nothing; third parties pay. Freemium would require paid features."],
 ["After a customer survey, a carmaker includes premium seats and a high-end sound system as standard features and prices the model above its rivals. This is best described as:", ["value-based pricing.", "bundling.", "dynamic pricing."], 0, "The price reflects the value customers place on the richer standard product."],
])
