# CFA Level I · Fixed Income · readings 1–5. Original study notes and questions.
R = []

R.append(dict(id="fe", n="Fixed-Income Instrument Features", k="FEATURES", w=2, c="#3b7dd8",
terms=[
 ["Par value", "Nominal değer", "The principal amount the issuer promises to repay at maturity; also called face value.", "İhraççının vadede geri ödemeyi taahhüt ettiği anapara; yüz değer de denir."],
 ["Coupon rate", "Kupon oranı", "The annual interest rate paid on the par value.", "Nominal değer üzerinden ödenen yıllık faiz oranı."],
 ["Tenor", "Kalan vade", "The time remaining until a bond's maturity.", "Tahvilin vadesine kalan süre."],
 ["Indenture", "İhraç sözleşmesi", "The legal contract that sets out the bond's terms and the obligations of the issuer.", "Tahvilin koşullarını ve ihraççının yükümlülüklerini belirleyen hukuki sözleşme."],
 ["Trustee", "Tahvil sahipleri temsilcisi", "A party, usually a bank, appointed to act in the bondholders' interests.", "Tahvil sahiplerinin çıkarlarını korumak üzere atanan taraf; genellikle bir banka."],
 ["Affirmative covenant", "Olumlu taahhüt", "A promise by the issuer to do something, such as pay taxes or maintain insurance.", "İhraççının vergi ödemek veya sigorta yaptırmak gibi bir şey yapma taahhüdü."],
 ["Negative covenant", "Olumsuz taahhüt", "A restriction on the issuer, such as limits on further borrowing or on selling assets.", "İhraççıya getirilen kısıtlama; örneğin ek borçlanma veya varlık satışı sınırları."],
 ["Secured bond", "Teminatlı tahvil", "A bond backed by a claim on specific assets.", "Belirli varlıklar üzerinde hakla desteklenen tahvil."],
 ["Internal credit enhancement", "İç kredi iyileştirmesi", "Protection built into the structure, such as subordination, overcollateralization or reserve accounts.", "Yapının içinde yer alan koruma; örneğin sıralama, fazla teminat veya rezerv hesapları."],
 ["External credit enhancement", "Dış kredi iyileştirmesi", "Protection provided by a third party, such as a guarantee or a letter of credit.", "Üçüncü bir tarafça sağlanan koruma; örneğin garanti veya akreditif."],
],
notes="""<h3>Basic features</h3>
<ul>
<li><b>Issuer:</b> governments, supranationals, agencies, companies, special purpose entities.</li>
<li><b>Maturity:</b> money market instruments mature within a year; capital market bonds beyond. Perpetual bonds have no maturity.</li>
<li><b>Par value</b> and <b>coupon rate</b> determine the coupon payment. A bond priced above par trades at a premium, below par at a discount.</li>
<li><b>Currency:</b> usually one, but a dual-currency bond pays coupons in one currency and principal in another.</li>
</ul>
<h3>The legal framework</h3>
<ul>
<li>The <b>indenture</b> sets out the terms; a <b>trustee</b> monitors the issuer's compliance on behalf of bondholders.</li>
<li><b>Affirmative covenants</b> require actions: pay interest and principal, maintain assets and insurance, file reports, comply with laws.</li>
<li><b>Negative covenants</b> limit actions: additional debt, liens on assets (negative pledge), asset sales, payments to shareholders, mergers.</li>
<li>Covenants protect lenders but too many restrict the business, so they are a negotiated balance.</li>
</ul>
<h3>Security and seniority</h3>
<ul>
<li><b>Secured</b> debt has a claim on specific collateral; <b>unsecured</b> debt has a general claim. Secured debt has higher expected recovery and therefore a lower yield.</li>
<li>Collateral examples: real property (mortgage bonds), equipment (equipment trust certificates), financial assets.</li>
</ul>
<h3>Credit enhancement</h3>
<div class="tbl"><table>
<tr><th>Internal</th><th>External</th></tr>
<tr><td>Subordination: junior tranches absorb losses first</td><td>Surety bonds and bank guarantees</td></tr>
<tr><td>Overcollateralization: collateral worth more than the bonds</td><td>Letters of credit</td></tr>
<tr><td>Reserve accounts and excess spread</td><td>Exposed to the guarantor's own credit risk</td></tr>
</table></div>
<h3>Legal, regulatory and tax issues</h3>
<ul>
<li><b>Domestic</b> bonds are issued in the issuer's home country and currency; <b>foreign</b> bonds in another country's market and currency; <b>eurobonds</b> outside any single country's jurisdiction.</li>
<li>Zero-coupon and other discount bonds may be taxed on the accrual of the discount each year, not only at maturity.</li>
</ul>
<div class="trap"><b>Exam trap</b>A negative pledge (not to pledge assets to other lenders) is a negative covenant, even though it sounds like a promise.</div>""",
qs=[
 ["The legal contract that sets out a bond's terms and the issuer's obligations is the:", ["covenant.", "indenture.", "prospectus summary."], 1, "The indenture is the full contract; covenants are clauses within it."],
 ["Which of the following is a negative covenant?", ["A requirement to pay taxes when due", "A requirement to maintain insurance on assets", "A limit on the amount of additional debt the issuer may take on"], 2, "Negative covenants restrict actions. Paying taxes and insuring assets are affirmative covenants."],
 ["Which of the following is a form of internal credit enhancement?", ["Subordination", "A bank guarantee", "A letter of credit"], 0, "Subordination is part of the structure itself. Guarantees and letters of credit come from third parties."],
 ["A bond with a par value of $1,000 has a 6% coupon rate paid semi-annually. Each coupon payment is:", ["$30", "$60", "$120"], 0, "Annual coupon is $60, paid in two instalments of $30."],
 ["Compared with an unsecured bond of the same issuer and maturity, a secured bond most likely has:", ["a lower yield.", "a higher yield.", "lower expected recovery."], 0, "A claim on collateral raises expected recovery in default, so investors accept a lower yield."],
 ["A bond that pays its coupons in one currency and its principal in another is a:", ["eurobond.", "foreign bond.", "dual-currency bond."], 2, "A dual-currency bond splits its payments between two currencies."],
 ["The main role of a bond trustee is to:", ["guarantee repayment of the bond.", "set the bond's coupon rate.", "monitor the issuer's compliance with the bond's terms."], 2, "The trustee acts for bondholders, monitoring covenants and taking action on default. It does not guarantee payment."],
 ["Collateral with a value well above the par value of the bonds it secures is an example of:", ["overcollateralization.", "a surety bond.", "a negative pledge."], 0, "Excess collateral provides a cushion against losses, an internal credit enhancement."],
]))

R.append(dict(id="fc", n="Fixed-Income Cash Flows and Types", k="CASH FLOWS", w=2, c="#2e9e8f",
terms=[
 ["Bullet bond", "Vadede tek anapara ödemeli tahvil", "A bond that repays all of its principal at maturity.", "Anaparasının tamamını vadede geri ödeyen tahvil."],
 ["Amortizing bond", "İtfalı tahvil", "A bond that repays principal gradually over its life.", "Anaparayı ömrü boyunca kademeli olarak geri ödeyen tahvil."],
 ["Sinking fund", "Batan fon (itfa fonu)", "A provision requiring the issuer to retire part of the issue each year.", "İhraççının her yıl ihracın bir bölümünü itfa etmesini gerektiren hüküm."],
 ["Floating-rate note (FRN)", "Değişken faizli tahvil", "A bond whose coupon resets periodically to a reference rate plus a margin.", "Kuponu dönemsel olarak referans faiz artı bir marja göre yeniden belirlenen tahvil."],
 ["Payment-in-kind (PIK) bond", "Ayni faiz ödemeli tahvil", "A bond that may pay interest with additional bonds instead of cash.", "Faizi nakit yerine ek tahvillerle ödeyebilen tahvil."],
 ["Inflation-linked bond", "Enflasyona endeksli tahvil", "A bond whose principal or coupon is adjusted for changes in a price index.", "Anaparası veya kuponu bir fiyat endeksindeki değişime göre ayarlanan tahvil."],
 ["Callable bond", "Erken itfa edilebilir tahvil", "A bond the issuer may redeem before maturity at a set price.", "İhraççının vadeden önce belirlenen fiyattan geri ödeyebileceği tahvil."],
 ["Putable bond", "Satma hakkı tanınan tahvil", "A bond the holder may sell back to the issuer before maturity at a set price.", "Sahibinin vadeden önce ihraççıya belirlenen fiyattan geri satabileceği tahvil."],
 ["Convertible bond", "Paya dönüştürülebilir tahvil", "A bond the holder may exchange for a set number of the issuer's shares.", "Sahibinin ihraççının belirli sayıda payıyla değiştirebileceği tahvil."],
 ["Conversion ratio", "Dönüşüm oranı", "The number of shares received for each bond converted.", "Dönüştürülen her tahvil için alınan pay sayısı."],
 ["Contingent convertible bond", "Koşullu dönüştürülebilir tahvil", "A bond that converts into equity automatically when a trigger, such as a capital ratio, is breached.", "Sermaye oranı gibi bir eşik aşıldığında otomatik olarak paya dönüşen tahvil."],
],
notes="""<h3>Repaying principal</h3>
<div class="tbl"><table>
<tr><th>Structure</th><th>Principal repaid</th><th>Credit risk</th></tr>
<tr><td>Bullet</td><td>All at maturity</td><td>Highest</td></tr>
<tr><td>Partially amortizing</td><td>Part over time, a balloon at maturity</td><td>Middle</td></tr>
<tr><td>Fully amortizing</td><td>Fully over the life, as in a mortgage</td><td>Lowest</td></tr>
</table></div>
<ul>
<li>A <b>sinking fund</b> retires part of the issue each year, by calling bonds at a set price or buying them in the market. It lowers credit risk but creates reinvestment risk, and the call price may be below market when rates have fallen.</li>
</ul>
<h3>Coupon structures</h3>
<ul>
<li><b>Floating-rate notes:</b> coupon = reference rate + quoted margin, reset periodically. Little interest rate risk; caps and floors may apply.</li>
<li><b>Step-up coupons:</b> rise at set dates. <b>Credit-linked coupons:</b> rise if the issuer is downgraded.</li>
<li><b>Payment-in-kind:</b> interest paid with more bonds; used by highly leveraged issuers; investors demand a higher yield.</li>
<li><b>Deferred coupon:</b> no coupons for the first years. <b>Zero coupon:</b> none at all; sold at a discount.</li>
<li><b>Inflation-linked:</b> most commonly the principal is indexed, and a fixed coupon rate is paid on the adjusted principal.</li>
</ul>
<h3>Contingency provisions</h3>
<div class="tbl"><table>
<tr><th>Bond</th><th>Option belongs to</th><th>Price vs straight bond</th><th>Yield vs straight bond</th></tr>
<tr><td>Callable</td><td>Issuer</td><td>Lower</td><td>Higher</td></tr>
<tr><td>Putable</td><td>Investor</td><td>Higher</td><td>Lower</td></tr>
<tr><td>Convertible</td><td>Investor</td><td>Higher</td><td>Lower</td></tr>
</table></div>
<ul>
<li>Call types: American (any time after the protection period), European (one date), Bermudan (set dates). A make-whole call pays the present value of remaining cash flows, which makes calling unattractive.</li>
<li>Issuers call when rates fall, so investors face reinvestment at lower rates.</li>
</ul>
<h3>Convertible bonds</h3>
<p class="f">conversion price = par value / conversion ratio &nbsp;&nbsp;&nbsp; conversion value = conversion ratio × share price</p>
<ul>
<li>Conversion premium = bond price − conversion value. The bond is worth at least the higher of its straight bond value and its conversion value.</li>
<li><b>Warrants</b> attached to bonds give a separate right to buy shares. <b>Contingent convertibles</b> issued by banks convert to equity or are written down when capital falls below a trigger.</li>
</ul>
<div class="trap"><b>Exam trap</b>A callable bond has a higher yield than a straight bond because the investor is short the call option; a putable bond has a lower yield because the investor owns the put.</div>""",
qs=[
 ["A convertible bond with a par value of $1,000 has a conversion ratio of 25. The share price is $45. The conversion value of the bond is:", ["$1,000", "$1,080", "$1,125"], 2, "Conversion value = 25 × $45 = $1,125."],
 ["A convertible bond with a par value of $1,000 has a conversion ratio of 25. Its conversion price is:", ["$25", "$40", "$45"], 1, "Conversion price = par / conversion ratio = 1,000 / 25 = $40."],
 ["Compared with an otherwise identical option-free bond, a callable bond has:", ["a lower yield.", "a higher yield.", "a higher price."], 1, "The investor has sold a call option to the issuer and is compensated with a higher yield and lower price."],
 ["Compared with an otherwise identical option-free bond, a putable bond has:", ["a lower price.", "a higher price.", "a higher yield."], 1, "The investor owns the put, which has value, so the bond is priced higher and yields less."],
 ["A sinking fund provision most likely:", ["increases credit risk.", "reduces credit risk but creates reinvestment risk.", "eliminates the issuer's need to repay principal."], 1, "Retiring bonds steadily reduces the amount outstanding, but bonds retired early must be reinvested."],
 ["Inflation-linked bonds most commonly adjust for inflation through:", ["the principal amount.", "the maturity date.", "the coupon payment dates."], 0, "Capital-indexed bonds adjust the principal; the fixed coupon rate is paid on the adjusted principal."],
 ["A highly leveraged company issues bonds that may pay interest in additional bonds instead of cash. These are:", ["step-up bonds.", "deferred coupon bonds.", "payment-in-kind bonds."], 2, "PIK bonds let the issuer preserve cash by paying interest with more debt."],
 ["Among bonds of the same issuer with the same maturity, the one with the lowest credit risk is a:", ["bullet bond.", "partially amortizing bond.", "fully amortizing bond."], 2, "A fully amortizing bond reduces the amount owed with every payment, so less is at risk later."],
]))

R.append(dict(id="it", n="Fixed-Income Issuance and Trading", k="ISSUANCE", w=1, c="#c0563f",
terms=[
 ["Underwritten offering", "Yüklenimli halka arz", "An issue in which investment banks buy the whole issue and resell it, bearing the risk of unsold bonds.", "Yatırım bankalarının tüm ihracı satın alıp yeniden sattığı ve satılmayan tahvil riskini üstlendiği ihraç."],
 ["Best-efforts offering", "En iyi gayret esaslı ihraç", "An issue in which the bank acts only as a broker and does not guarantee the sale.", "Bankanın yalnızca aracı olduğu ve satışı garanti etmediği ihraç."],
 ["Auction", "İhale", "A method of issuance in which investors bid and the price is set by the bids; used for most government bonds.", "Yatırımcıların teklif verdiği ve fiyatın tekliflerle belirlendiği ihraç yöntemi; çoğu devlet tahvilinde kullanılır."],
 ["Shelf registration", "Raf kaydı", "A single registration that allows an issuer to sell bonds in several tranches over time.", "İhraççının tahvilleri zaman içinde birden çok dilimde satmasına izin veren tek kayıt."],
 ["Private placement", "Tahsisli satış", "A sale of unregistered securities directly to a small group of qualified investors.", "Kayıtlı olmayan menkul kıymetlerin küçük bir nitelikli yatırımcı grubuna doğrudan satışı."],
 ["Over-the-counter market", "Tezgâhüstü piyasa", "A dealer network in which trades are negotiated directly, outside an exchange.", "İşlemlerin borsa dışında doğrudan pazarlıkla yapıldığı aracı kurum ağı."],
 ["Bid-ask spread", "Alış-satış farkı", "The difference between the price at which a dealer buys and the price at which it sells.", "Bir aracının alış fiyatı ile satış fiyatı arasındaki fark."],
 ["Settlement", "Takas", "The exchange of cash for securities after a trade is agreed.", "İşlem kararlaştırıldıktan sonra nakdin menkul kıymetle değişimi."],
],
notes="""<h3>Primary market</h3>
<div class="tbl"><table>
<tr><th>Method</th><th>Features</th></tr>
<tr><td>Underwritten offering</td><td>Banks buy the issue at an agreed price and resell it; they bear the risk; common for corporate bonds</td></tr>
<tr><td>Best-efforts offering</td><td>Banks sell on commission; the issuer bears the risk</td></tr>
<tr><td>Auction</td><td>Investors bid; standard for government bonds</td></tr>
<tr><td>Shelf registration</td><td>One filing, several issues over time as needs arise; for established issuers</td></tr>
<tr><td>Private placement</td><td>Direct to qualified investors; customized terms; less liquid; less disclosure</td></tr>
</table></div>
<ul>
<li>In an underwritten deal the bank gauges demand through a <b>grey market</b> (forward trading before issue) and sets the coupon accordingly.</li>
</ul>
<h3>Secondary market</h3>
<ul>
<li>Most bonds trade <b>over the counter</b> through dealers, not on exchanges. Dealers quote bid and ask prices and hold inventory.</li>
<li>Liquidity varies greatly: recently issued government bonds trade constantly; many corporate bonds rarely trade after the first weeks.</li>
<li>A narrow <b>bid-ask spread</b> indicates high liquidity. Spreads widen in stressed markets and for small, complex or low-rated issues.</li>
<li>Settlement usually takes one to three business days; money market instruments often settle the same day.</li>
</ul>
<h3>Who participates</h3>
<ul>
<li>Issuers: governments, agencies, supranationals, financial institutions, non-financial companies.</li>
<li>Investors: central banks, pension funds, insurers, mutual funds, banks, hedge funds, individuals.</li>
<li>Intermediaries: investment banks, dealers, brokers, custodians, clearing systems.</li>
</ul>
<div class="trap"><b>Exam trap</b>In a best-efforts offering the bank does not commit its own capital, so unsold bonds are the issuer's problem.</div>""",
qs=[
 ["In an underwritten bond offering, the risk that the issue cannot be sold at the agreed price is borne by the:", ["issuer.", "investors.", "investment bank."], 2, "The underwriter buys the whole issue and must resell it."],
 ["In a best-efforts bond offering, the investment bank:", ["guarantees the issue price.", "buys the entire issue for its own account.", "acts as a broker and does not guarantee the sale."], 2, "The bank sells on a commission basis without committing its own capital."],
 ["An established company files one registration and then issues bonds in several tranches over two years as funds are needed. This method is:", ["an auction.", "a private placement.", "a shelf registration."], 2, "Shelf registration allows repeated issuance under a single filing."],
 ["Compared with a public offering, a private placement of bonds is most likely:", ["more liquid.", "less liquid.", "subject to more disclosure."], 1, "Privately placed bonds are not registered for public trading, so their secondary market is thin."],
 ["Most corporate bonds trade in the secondary market:", ["on stock exchanges.", "in over-the-counter dealer markets.", "only through central bank auctions."], 1, "Bond trading is mainly over the counter, between dealers and their clients."],
 ["Government bonds are most commonly issued through:", ["auctions.", "private placements.", "best-efforts offerings."], 0, "Sovereign issuers typically sell bonds through public auctions."],
 ["A narrow bid-ask spread on a bond most likely indicates that the bond is:", ["illiquid.", "highly liquid.", "about to default."], 1, "Dealers quote tight spreads when they can easily buy and sell the bond."],
 ["Compared with a recently issued government bond, a small corporate bond that has been outstanding for several years most likely has:", ["a narrower bid-ask spread.", "a wider bid-ask spread.", "the same bid-ask spread."], 1, "Older, smaller and riskier issues trade less often, so dealers demand wider spreads."],
]))

R.append(dict(id="ci", n="Fixed-Income Markets for Corporate Issuers", k="CORPORATE", w=1, c="#8a5cc2",
terms=[
 ["Commercial paper", "Finansman bonosu", "Short-term unsecured debt issued by companies, usually sold at a discount.", "Şirketlerin ihraç ettiği, genellikle iskontolu satılan kısa vadeli teminatsız borç."],
 ["Backup line of credit", "Yedek kredi limiti", "A bank credit line used to repay commercial paper if it cannot be rolled over.", "Finansman bonosu yenilenemezse geri ödemek için kullanılan banka kredi limiti."],
 ["Rollover risk", "Yenileme riski", "The risk that maturing short-term debt cannot be refinanced.", "Vadesi gelen kısa vadeli borcun yeniden finanse edilememesi riski."],
 ["Repurchase agreement (repo)", "Geri alım vaadiyle satım (repo)", "A sale of securities with an agreement to buy them back at a higher price on a later date; in effect a secured loan.", "Menkul kıymetlerin daha sonra daha yüksek fiyattan geri alınmak üzere satılması; özünde teminatlı borçtur."],
 ["Repo rate", "Repo faizi", "The interest rate implied by the difference between the repurchase price and the sale price.", "Geri alım fiyatı ile satış fiyatı arasındaki farkın ima ettiği faiz oranı."],
 ["Haircut", "Teminat iskontosu (haircut)", "The percentage by which the collateral's value exceeds the cash lent in a repo.", "Repoda teminatın değerinin borç verilen nakdi aştığı yüzde."],
 ["Medium-term note (MTN)", "Orta vadeli tahvil programı", "Debt offered continuously through agents in amounts and maturities that suit investors.", "Aracılar aracılığıyla sürekli, yatırımcının istediği tutar ve vadede sunulan borçlanma aracı."],
 ["Investment grade", "Yatırım yapılabilir seviye", "Credit ratings of BBB− (or Baa3) and above.", "BBB− (veya Baa3) ve üzerindeki kredi notları."],
 ["High-yield bond", "Yüksek getirili tahvil", "A bond rated below investment grade.", "Yatırım yapılabilir seviyenin altında notu olan tahvil."],
 ["Wholesale funding", "Toptan fonlama", "Bank funding from other financial institutions and markets, as opposed to customer deposits.", "Müşteri mevduatı dışında, diğer finansal kurumlardan ve piyasalardan sağlanan banka fonlaması."],
],
notes="""<h3>Short-term funding for companies</h3>
<ul>
<li><b>Bank loans and lines of credit:</b> uncommitted lines can be withdrawn; committed lines and revolving facilities cost a fee but are reliable.</li>
<li><b>Secured loans and asset-based finance:</b> receivables or inventory as collateral; factoring sells the receivables.</li>
<li><b>Commercial paper:</b> large, creditworthy issuers; maturities under a year; usually rolled over. Issuers keep <b>backup lines of credit</b> because of <b>rollover risk</b>.</li>
</ul>
<h3>Long-term corporate debt</h3>
<ul>
<li>Corporate notes and bonds with fixed or floating coupons, issued under a shelf or a <b>medium-term note</b> programme.</li>
<li><b>Investment grade</b> (BBB−/Baa3 and above) versus <b>high yield</b>. The line matters because many investors may hold only investment-grade debt.</li>
<li>Secured and unsecured, senior and subordinated, with or without covenants.</li>
</ul>
<h3>Financial institutions</h3>
<ul>
<li>Banks fund themselves mainly with <b>deposits</b> (retail deposits are the most stable), plus <b>wholesale funding</b>: interbank loans, certificates of deposit, repos.</li>
<li>Regulation requires stable funding and liquid assets to limit the risk of a run.</li>
</ul>
<h3>Repurchase agreements</h3>
<p class="f">cash lent = collateral value × (1 − haircut)</p>
<p class="f">repo interest = cash lent × repo rate × days / 360</p>
<ul>
<li>A repo is a collateralized loan: the borrower sells securities and buys them back later at a higher price. The lender has a <b>reverse repo</b>.</li>
<li>Repo rates and haircuts are <b>higher</b> for longer terms, riskier or less liquid collateral, weaker counterparties, and when collateral is in plentiful supply. Scarce, in-demand collateral can trade at a low repo rate.</li>
<li>Repo is central to dealers' financing of their bond inventories and to central bank operations.</li>
</ul>
<div class="trap"><b>Exam trap</b>A bigger haircut means less cash for the same collateral; it protects the lender, not the borrower.</div>""",
qs=[
 ["A dealer enters a repo using bonds with a market value of $10 million as collateral. The haircut is 2%. The cash the dealer receives is:", ["$9.8 million", "$10.0 million", "$10.2 million"], 0, "Cash lent = 10 × (1 − 0.02) = $9.8 million."],
 ["A dealer borrows $9.8 million through a 30-day repo at a repo rate of 4%, on a 360-day basis. The repo interest is closest to:", ["$32,667", "$33,333", "$392,000"], 0, "9,800,000 × 0.04 × 30/360 = $32,667."],
 ["Companies that issue commercial paper typically maintain backup lines of credit mainly to manage:", ["currency risk.", "rollover risk.", "interest rate risk."], 1, "If new paper cannot be sold when old paper matures, the credit line provides the cash to repay it."],
 ["All else equal, the haircut on a repo will most likely be higher if the collateral is:", ["highly liquid.", "less liquid.", "a short-term government bill."], 1, "Lenders demand more protection when collateral may be hard to sell at a fair price."],
 ["The lowest rating considered investment grade is:", ["A−", "BBB−", "BB+"], 1, "BBB− (or Baa3) is the lowest investment-grade rating. BB+ is the highest high-yield rating."],
 ["For a bank, the most stable source of funding is typically:", ["retail deposits.", "interbank loans.", "commercial paper."], 0, "Insured retail deposits tend to stay even in stress, unlike wholesale funding."],
 ["Debt offered continuously by a company through agents, in a range of maturities chosen by investors, is a:", ["repo.", "commercial paper.", "medium-term note."], 2, "Medium-term note programmes let issuers sell debt continuously across many maturities."],
 ["From the lender's side, a repurchase agreement is economically equivalent to:", ["an unsecured loan.", "a collateralized loan.", "a purchase of equity."], 1, "The cash lender holds the securities as collateral until they are repurchased."],
]))

R.append(dict(id="gi", n="Fixed-Income Markets for Government Issuers", k="GOVERNMENT", w=1, c="#b8860b",
terms=[
 ["Sovereign bond", "Devlet tahvili", "A bond issued by a national government.", "Merkezi hükümet tarafından ihraç edilen tahvil."],
 ["Treasury bill", "Hazine bonosu", "A short-term zero-coupon government security sold at a discount.", "İskontolu satılan kısa vadeli, kuponsuz devlet menkul kıymeti."],
 ["On-the-run", "Son ihraç (gösterge)", "The most recently issued government bond of a given maturity; the most liquid and used as a benchmark.", "Belirli bir vadede en son ihraç edilen devlet tahvili; en likit olanıdır ve gösterge olarak kullanılır."],
 ["Off-the-run", "Eski ihraç", "A previously issued government bond that has been replaced as the benchmark by a newer one.", "Daha yeni bir ihraçla gösterge olma niteliğini yitirmiş, önceden ihraç edilmiş devlet tahvili."],
 ["Single-price auction", "Tek fiyatlı ihale", "An auction in which all successful bidders pay the same price, set by the highest accepted yield.", "Tüm başarılı teklif sahiplerinin, kabul edilen en yüksek getiriyle belirlenen aynı fiyatı ödediği ihale."],
 ["Agency bond", "Kamu kurumu tahvili", "A bond issued by a government agency or government-sponsored entity.", "Bir kamu kurumu veya devlet destekli kuruluş tarafından ihraç edilen tahvil."],
 ["Supranational bond", "Uluslarüstü kuruluş tahvili", "A bond issued by an international organization owned by several governments, such as a development bank.", "Kalkınma bankası gibi birden fazla hükümetin sahip olduğu uluslararası kuruluşun ihraç ettiği tahvil."],
 ["General obligation bond", "Genel yükümlülük tahvili", "A local government bond backed by the issuer's taxing power.", "İhraççının vergilendirme yetkisiyle desteklenen yerel yönetim tahvili."],
 ["Revenue bond", "Gelire dayalı tahvil", "A local government bond backed only by the revenue of a specific project.", "Yalnızca belirli bir projenin geliriyle desteklenen yerel yönetim tahvili."],
],
notes="""<h3>Sovereign debt</h3>
<ul>
<li>Governments borrow to cover deficits and refinance debt. Maturities range from bills (under a year, zero coupon) to notes and long-term bonds.</li>
<li>Debt in the government's own currency carries little default risk, because the state can raise taxes or create money. Debt in a <b>foreign currency</b> is riskier.</li>
<li>Many governments issue <b>inflation-linked</b> bonds and some issue floating-rate bonds.</li>
</ul>
<h3>Issuance</h3>
<ul>
<li>Mostly through regular, pre-announced <b>auctions</b>, often with primary dealers obliged to bid.</li>
<li>In a <b>single-price</b> (Dutch) auction, everyone whose bid is accepted pays the price matching the highest accepted yield. In a <b>multiple-price</b> auction, each pays its own bid.</li>
<li><b>On-the-run</b> issues are the newest and most liquid; they serve as the risk-free benchmark curve. <b>Off-the-run</b> issues trade at slightly higher yields because they are less liquid.</li>
</ul>
<h3>Non-sovereign government debt</h3>
<ul>
<li><b>Regional and local governments:</b> cannot create money, so they carry more credit risk than the sovereign. <b>General obligation</b> bonds rest on taxing power; <b>revenue</b> bonds rest on a project's revenues (tolls, utilities) and are riskier.</li>
<li><b>Agencies</b> and government-sponsored entities: often have an explicit or implicit guarantee, so they trade close to sovereign yields.</li>
<li><b>Supranationals</b> such as development banks: usually highly rated thanks to their owners' backing and conservative lending.</li>
</ul>
<h3>Uses of government bonds</h3>
<ul>
<li>Benchmark for pricing other bonds, collateral for repo and central bank operations, safe haven in market stress, and a tool of monetary policy.</li>
</ul>
<div class="trap"><b>Exam trap</b>A revenue bond is backed only by the project's income. If the project fails, the issuer's general taxes do not stand behind it.</div>""",
qs=[
 ["The most recently issued government bond of a given maturity is called:", ["off-the-run.", "on-the-run.", "a supranational bond."], 1, "On-the-run issues are the newest, most liquid and serve as benchmarks."],
 ["Compared with on-the-run government bonds, off-the-run bonds of similar maturity typically trade at:", ["lower yields.", "higher yields.", "the same yields."], 1, "They are less liquid, so investors require a small yield premium."],
 ["A national government is least likely to default on debt that is denominated in:", ["its own currency.", "a foreign currency.", "a basket of foreign currencies."], 0, "A government can raise taxes or create money in its own currency, but it cannot create foreign currency."],
 ["A local government bond backed only by tolls collected on a new bridge is a:", ["revenue bond.", "general obligation bond.", "sovereign bond."], 0, "Revenue bonds depend on the cash flows of a specific project."],
 ["Compared with a general obligation bond of the same local government, a revenue bond most likely has:", ["lower credit risk.", "higher credit risk.", "the same credit risk."], 1, "Its repayment depends on one project, not the issuer's broad taxing power."],
 ["In a single-price government bond auction, all successful bidders pay a price based on the:", ["lowest bid yield.", "average bid yield.", "highest accepted yield."], 2, "The auction clears at the highest yield needed to sell the full amount, and everyone pays that price."],
 ["A bond issued by a multilateral development bank owned by many governments is a:", ["sovereign bond.", "supranational bond.", "general obligation bond."], 1, "Supranational issuers are international organizations owned by several countries."],
 ["Treasury bills are typically:", ["sold at a discount with no coupon.", "long-term bonds with fixed coupons.", "floating-rate notes with a quoted margin."], 0, "Bills are short-term, zero-coupon instruments whose return is the difference between purchase price and face value."],
]))
