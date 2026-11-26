# CFA Level I · Alternative Investments · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
EK = {}

EK["af"] = dict(
terms=[
 ["Term sheet", "Şartlar özeti (term sheet)", "A summary of a fund's investment policy, fee structure and requirements for investors.", "Bir fonun yatırım politikasını, ücret yapısını ve yatırımcılardan beklenen şartları özetleyen belge."],
 ["Private placement memorandum (PPM)", "Özel plasman bilgilendirme belgesi", "The offering document describing a private fund's strategy, risks and terms.", "Özel bir fonun stratejisini, risklerini ve koşullarını anlatan teklif belgesi."],
 ["Side letter", "Yan mektup (side letter)", "An agreement giving one investor terms that differ from those of other investors, such as lower fees or extra reporting.", "Bir yatırımcıya diğerlerinden farklı koşullar tanıyan anlaşma; örneğin daha düşük ücret veya ek raporlama."],
 ["Preferred return", "Öncelikli getiri", "Another name for the hurdle rate that investors must receive before the manager shares in profits.", "Yöneticinin kâra ortak olmasından önce yatırımcıların alması gereken engel getirinin diğer adı."],
 ["Committed capital", "Taahhüt edilen sermaye", "The total amount investors have agreed to provide to a private fund over its life.", "Yatırımcıların özel bir fona ömrü boyunca sağlamayı kabul ettiği toplam tutar."],
],
notes="""<h3>Fund documents and fee bases</h3>
<ul>
<li><b>Term sheet:</b> investment policy, fees and investor requirements. <b>Private placement memorandum:</b> the full offering document. <b>Limited partnership agreement:</b> the legal contract. <b>Side letters:</b> investor-specific terms.</li>
<li>Hedge fund management fees are usually charged on <b>assets under management</b>; private equity management fees during the investment period are usually charged on <b>committed capital</b>.</li>
<li><b>Catch-up with a soft hurdle:</b> investors receive returns up to the hurdle, then the manager receives returns until it has its full share of the total; above that, profits are split. With a 100% catch-up and enough return, the manager ends up with its full percentage of the entire return.</li>
<li>Provisions that protect investors: high-water mark, hurdle, clawback, whole-of-fund waterfall. Provisions that favour the manager: catch-up, deal-by-deal waterfall.</li>
</ul>""",
qs=[
 ["Which fund document summarizes the fund's investment policy, fee structure and the requirements investors must meet?", ["Side letter", "Term sheet", "Subscription agreement"], 1, "The term sheet gives a summary of the key terms. Side letters set terms for individual investors."],
 ["A pension fund negotiates lower fees and quarterly holdings reports that other investors in the same hedge fund do not receive. These terms are most likely documented in a:", ["term sheet.", "side letter.", "limited partnership agreement."], 1, "Side letters record terms specific to one investor."],
 ["Compared with traditional long-only funds, alternative investment funds are more likely to:", ["offer daily liquidity.", "use leverage and short positions.", "be subject to extensive regulation."], 1, "Leverage, shorting and derivatives are characteristic of many alternative strategies."],
 ["An individual with a modest amount of capital wants exposure to a diversified group of private infrastructure assets. The most suitable method is:", ["fund investing.", "co-investing.", "direct investing."], 0, "Funds pool capital across many assets, so they need less capital per investor and give diversification, at the cost of higher fees."],
 ["A hedge fund charges '1.5 and 25'. Compared with a fund charging '2 and 20', it has a:", ["higher management fee and higher incentive fee.", "lower management fee and higher incentive fee.", "lower management fee and lower incentive fee."], 1, "The first number is the management fee and the second the incentive fee."],
 ["A fund earns 15% in a year. It charges a 20% incentive fee subject to a 6% soft hurdle with a full catch-up. The manager's incentive fee is:", ["1.8%", "2.4%", "3.0%"], 2, "Investors receive the first 6%. The catch-up then gives the manager the next 1.5%, so it holds 20% of the first 7.5%. The remaining 7.5% is split 80/20, adding 1.5%. The manager earns 3.0%, which is 20% of the whole return."],
 ["A fund earns 7% in a year. It charges a 20% incentive fee subject to a 6% soft hurdle with a full catch-up. The manager's incentive fee is:", ["0.2%", "1.0%", "1.4%"], 1, "Investors receive the first 6%. The catch-up gives the manager all further return until it holds 20% of the total, but only 1.0% remains above the hurdle, so the manager receives 1.0%."],
 ["A fund earns 15% in a year. It charges a 20% incentive fee subject to a 6% hard hurdle. The manager's incentive fee is:", ["1.8%", "2.4%", "3.0%"], 0, "With a hard hurdle, the fee applies only to returns above 6%: 20% × 9% = 1.8%."],
 ["Which of the following fee provisions primarily protects investors?", ["A catch-up clause", "A high-water mark", "A deal-by-deal waterfall"], 1, "A high-water mark prevents incentive fees until earlier losses are recovered. The other two favour the manager."],
 ["During its investment period, a private equity fund's management fee is most commonly calculated on:", ["committed capital.", "realized profits.", "year-end net asset value."], 0, "Private equity funds usually charge on capital committed; hedge funds on assets under management."],
 ["In a private equity fund, the term 'preferred return' refers to the:", ["hurdle rate.", "management fee.", "clawback amount."], 0, "Investors receive the preferred return before the general partner shares in profits."],
 ["Compared with traditional investments, alternative investments typically provide investors with:", ["less information about holdings.", "more transparency about holdings.", "the same level of disclosure."], 0, "Limited transparency and information asymmetry between managers and investors are typical challenges."],
])

EK["ap"] = dict(
terms=[
 ["Independent fee calculation", "Bağımsız ücret hesaplama", "A fee arrangement in which the incentive fee is calculated on gross gains, not net of the management fee.", "Performans ücretinin yönetim ücreti düşülmeden brüt kazanç üzerinden hesaplandığı düzenleme."],
 ["Leveraged return", "Kaldıraçlı getiri", "The return on the investor's own capital when part of the position is financed with borrowing.", "Pozisyonun bir kısmı borçla finanse edildiğinde yatırımcının kendi sermayesi üzerindeki getiri."],
],
notes="""<h3>More on fee calculations</h3>
<ul>
<li>Read whether fees are calculated <b>independently</b> (incentive on gross gain) or <b>net</b> (incentive on gain after the management fee). Independent calculation gives higher total fees.</li>
<li>With a high-water mark, the incentive fee in a recovery year applies only to value above the previous peak, so it can be less than the full percentage of that year's gain, or zero.</li>
</ul>
<p class="f">leveraged return = [r × (V<sub>0</sub> + B) − r<sub>B</sub> × B] / V<sub>0</sub></p>""",
qs=[
 ["A fund starts the year with $200 million and earns 20% before fees. It charges a 2% management fee on year-end assets and a 20% incentive fee on the gross gain, calculated independently. The investors' net return is closest to:", ["13.60%", "14.08%", "16.00%"], 0, "Year-end value 240. Management fee 4.8; incentive fee 20% × 40 = 8.0. Net = (240 − 12.8 − 200) / 200 = 13.60%."],
 ["A fund with $80 million at the start of the year has a '1 and 10' fee structure, with the incentive fee calculated on gains net of the management fee. The gross return is 6%. The investors' net return is closest to:", ["4.45%", "4.92%", "5.40%"], 0, "Year-end 84.8; management fee 0.848; net gain 3.952; incentive 0.395. Net = (84.8 − 0.848 − 0.395 − 80) / 80 = 4.45%."],
 ["A fund with a high-water mark starts at 100, rises to 110 in Year 1, falls to 88 in Year 2 and rises to 105.6 in Year 3. Ignoring fees in the value path, the incentive fee for Year 3 is:", ["zero.", "20% of the Year 3 gain.", "20% of the gain above the hurdle."], 0, "The fund remains below its previous peak of 110, so no incentive fee is due."],
 ["A fund with a high-water mark and no hurdle rises from 100 to 110 in Year 1, falls to 99 in Year 2 and rises to 118.8 in Year 3. The Year 3 incentive fee will be:", ["less than 20% of the Year 3 gain.", "equal to 20% of the Year 3 gain.", "greater than 20% of the Year 3 gain."], 0, "The fee applies only to value above the 110 peak (8.8), not to the full 19.8 gain."],
 ["An investor puts $50 of her own money and $50 of borrowed money at 5% into an asset that returns 12%. Her return on equity is closest to:", ["12%", "19%", "24%"], 1, "Gain on 100 is 12; interest is 2.5; net 9.5 on 50 of equity = 19%."],
 ["Compared with fees calculated net of the management fee, incentive fees calculated independently of the management fee result in:", ["lower total fees.", "higher total fees.", "the same total fees."], 1, "The incentive fee is charged on a larger, gross gain."],
])

EK["pk"] = dict(
terms=[
 ["Angel investing", "Melek yatırım", "The earliest financing, often from individuals, to turn an idea into a business plan.", "Bir fikri iş planına dönüştürmek için genellikle bireylerden gelen en erken finansman."],
 ["Seed stage", "Tohum aşaması", "Venture financing for product development and market research.", "Ürün geliştirme ve pazar araştırması için girişim finansmanı."],
 ["Early stage", "Erken aşama", "Financing for companies moving into operation, before commercial sales.", "Ticari satışlardan önce faaliyete geçmekte olan şirketlere finansman."],
 ["Later stage", "Geç aşama", "Financing to expand a company that already has commercial sales.", "Ticari satışları olan bir şirketin büyümesi için finansman."],
 ["Mezzanine stage (venture capital)", "Halka arz öncesi aşama", "Venture financing that prepares a company for an initial public offering.", "Şirketi halka arza hazırlayan girişim finansmanı."],
 ["Vintage year", "Kuruluş (vintage) yılı", "The year a private equity fund makes its first investment.", "Bir özel sermaye fonunun ilk yatırımını yaptığı yıl."],
 ["PIPE", "Halka açık şirkete özel yatırım", "Private investment in public equity: capital provided to a listed company without taking it private.", "Borsada işlem gören bir şirkete, onu borsadan çıkarmadan sağlanan özel sermaye."],
],
notes="""<h3>Venture capital stages</h3>
<div class="tbl"><table>
<tr><th>Stage</th><th>Purpose of financing</th></tr>
<tr><td>Angel investing</td><td>Idea to business plan; often individuals</td></tr>
<tr><td>Seed</td><td>Product development and market research</td></tr>
<tr><td>Early</td><td>Start of operations, before commercial sales</td></tr>
<tr><td>Later</td><td>Expansion after sales begin</td></tr>
<tr><td>Mezzanine</td><td>Preparation for an initial public offering</td></tr>
</table></div>
<h3>Other private capital points</h3>
<ul>
<li><b>Vintage year:</b> year of the fund's first investment. Funds that invest when valuations are low, often in recessions, have tended to perform better.</li>
<li><b>PIPE:</b> private investment in public equity, for example to finance a restructuring, without delisting.</li>
<li>Distressed debt is typically found in <b>mature</b> companies in difficulty, not start-ups.</li>
<li><b>Direct lending</b> rarely includes warrants; mezzanine and venture debt often do.</li>
<li>Infrequent appraisals bias reported <b>volatility and correlations downward</b>.</li>
</ul>""",
qs=[
 ["An entrepreneur receives funding from a wealthy individual to develop her idea into a business plan. This stage is best described as:", ["seed stage.", "early stage.", "angel investing."], 2, "Angel investing is the earliest stage, often supporting the move from idea to plan."],
 ["Venture financing used mainly for product development and market research is:", ["seed stage.", "later stage.", "mezzanine stage."], 0, "Seed capital funds product development and market research."],
 ["A start-up is beginning operations but has not yet started commercial sales. Its financing is best described as:", ["early stage.", "later stage.", "mezzanine stage."], 0, "Early-stage financing supports companies moving into operation before sales."],
 ["A profitable private technology company raises capital to strengthen its balance sheet before an initial public offering planned for next year. This financing is best described as:", ["seed stage.", "early stage.", "mezzanine stage."], 2, "Mezzanine-stage venture capital prepares the company for its IPO."],
 ["A private equity fund's vintage year is the year in which it:", ["closes to new investors.", "makes its first investment.", "realizes its first exit."], 1, "Vintage year is commonly defined as the year of first investment, which may differ from the year capital was committed."],
 ["Private equity funds that began investing during economic contractions have historically tended to:", ["outperform.", "underperform.", "match the average fund."], 0, "Investing when valuations are depressed has tended to produce better returns."],
 ["A private equity firm buys newly issued shares in a listed company to finance its turnaround, without taking it private. This is best described as:", ["a leveraged buyout.", "venture capital.", "private investment in public equity."], 2, "A PIPE provides capital to a public company while it remains listed."],
 ["Distressed debt is most often associated with companies in the:", ["start-up stage.", "growth stage.", "mature stage."], 2, "Distressed situations typically involve established companies facing decline or restructuring."],
 ["Which type of private debt is least likely to include warrants?", ["Direct lending", "Venture debt", "Mezzanine debt"], 0, "Direct lending is senior and secured; equity kickers are typical of riskier private debt."],
 ["Infrequent valuation of private equity holdings most likely causes reported correlations with public equity to be:", ["overstated.", "understated.", "unaffected."], 1, "Smoothed valuations lag market moves, hiding the true co-movement with public markets."],
 ["Compared with traditional publicly traded bonds, private debt typically offers:", ["higher yields and lower liquidity.", "lower yields and higher liquidity.", "higher yields and higher liquidity."], 0, "Investors earn an illiquidity premium for holding loans that do not trade."],
])

EK["re"] = dict(
terms=[
 ["Economic infrastructure", "Ekonomik altyapı", "Assets that support economic activity: transport, utilities, energy and communications.", "Ekonomik faaliyeti destekleyen varlıklar: ulaşım, kamu hizmetleri, enerji ve iletişim."],
 ["Social infrastructure", "Sosyal altyapı", "Assets that serve the community, such as schools, hospitals, courts and prisons.", "Okul, hastane, adliye ve cezaevi gibi topluma hizmet eden varlıklar."],
 ["Development risk", "Geliştirme riski", "Risks specific to building property: permits, construction delays, cost overruns and finding tenants.", "Gayrimenkul inşasına özgü riskler: izinler, inşaat gecikmeleri, maliyet aşımları ve kiracı bulma."],
],
notes="""<h3>More on real estate and infrastructure risks</h3>
<ul>
<li>During sharp market falls, the correlation between REIT returns and equity returns <b>rises</b>, so diversification is weakest when it is most needed.</li>
<li>Risks specific to <b>development</b>: obtaining permits, construction delays and overruns, and leasing risk. Default and interest rate risk are not unique to development.</li>
<li>Direct property carries significant <b>liquidity risk</b> that is small in a portfolio of listed stocks and bonds.</li>
<li>Communications assets such as data centres and towers are economic infrastructure.</li>
</ul>""",
qs=[
 ["During a severe equity market decline, the correlation between REIT returns and equity market returns most likely:", ["falls.", "rises.", "stays the same."], 1, "REITs trade like equities in stressed markets, so their correlation with stocks increases."],
 ["Which of the following is an example of economic infrastructure?", ["A toll bridge", "A public school", "A prison"], 0, "Transport assets are economic infrastructure; schools and prisons are social infrastructure."],
 ["Which of the following is an example of social infrastructure?", ["A courthouse", "A power station", "A telecommunications tower"], 0, "Courts serve the community; power and telecoms are economic infrastructure."],
 ["Among infrastructure investments, the highest expected risk and return is typically associated with:", ["brownfield assets.", "greenfield assets.", "regulated utilities with long operating histories."], 1, "Greenfield projects carry construction and demand risk."],
 ["Which risk is specific to property development rather than to owning an existing, fully let building?", ["Interest rate risk", "Construction cost overruns", "Inflation risk"], 1, "Building creates risks of delays, overruns and permits that a completed property does not face."],
 ["Greenfield infrastructure investments are best characterized by:", ["steady, proven cash flows.", "opportunistic development of new assets.", "low exposure to regulatory approvals."], 1, "They involve building new assets, with uncertain future cash flows."],
 ["Compared with a portfolio of listed equities and bonds, a portfolio of directly owned buildings is exposed to significantly more:", ["market risk.", "liquidity risk.", "currency risk."], 1, "Buildings can take months to sell and transaction costs are high."],
 ["Data centres are most appropriately classified as:", ["social infrastructure.", "economic infrastructure.", "residential real estate."], 1, "Communications assets support economic activity and are economic infrastructure."],
])

EK["nr"] = dict(
terms=[
 ["Sector fund", "Sektör fonu", "A fund that invests in one commodity sector, such as energy or precious metals.", "Enerji veya değerli metaller gibi tek bir emtia sektörüne yatırım yapan fon."],
 ["Raw land", "İşlenmemiş arazi", "Undeveloped land that produces no regular income.", "Düzenli gelir üretmeyen, geliştirilmemiş arazi."],
],
notes="""<h3>More on commodities and land</h3>
<ul>
<li>When the cost of carrying a commodity (storage, insurance, financing) exceeds the benefits of holding it, the forward price is above spot: <b>contango</b>.</li>
<li><b>Convenience yield</b> is a non-cash benefit of holding the physical good. It is high when inventories are low and lowers the forward price; a high convenience yield is associated with <b>backwardation</b>, a near-zero one with contango.</li>
<li>Commodity exposure can be gained through futures, ETFs, managed futures funds, sector funds focused on one area, and producers' shares.</li>
<li><b>Farmland</b> produces income from harvests every year; <b>timberland</b> has long growth cycles; <b>raw land</b> produces no income.</li>
<li>Commodities offer diversification and an inflation hedge but <b>no current income</b>.</li>
</ul>""",
qs=[
 ["When the cost of carrying a commodity is greater than the benefits of holding it, the forward price is most likely:", ["below the spot price.", "equal to the spot price.", "above the spot price."], 2, "Net carrying costs raise the forward price above spot, producing contango."],
 ["A commodity whose convenience yield is close to zero most likely trades in:", ["contango.", "backwardation.", "a flat forward curve with no carrying costs."], 0, "With little benefit from holding the physical good, carrying costs dominate and futures trade above spot."],
 ["Inventories of a commodity are unusually low. Its convenience yield is most likely:", ["high.", "low.", "negative."], 0, "When the good is scarce, users value having it on hand, so convenience yield rises."],
 ["A fund that invests only in precious metals futures is best described as a:", ["sector fund.", "managed futures fund.", "fund of funds."], 0, "Sector funds focus on one commodity area."],
 ["Which of the following land investments is most likely to provide regular annual cash flows?", ["Farmland", "Raw land", "Timberland planted last year"], 0, "Crops are harvested and sold each year; raw land and young forests produce little income."],
 ["Which of the following is least likely a benefit of investing in commodities?", ["Current income", "Diversification", "Inflation protection"], 0, "Commodities do not pay interest or dividends."],
 ["A high convenience yield will most likely cause the forward price of a commodity to be:", ["lower.", "higher.", "unchanged."], 0, "Convenience yield is a benefit of holding the physical good, so it reduces the forward price."],
])

EK["hf"] = dict(
terms=[
 ["Fundamental growth strategy", "Temel büyüme stratejisi", "An equity strategy that buys companies with rapidly growing revenue and earnings.", "Hasılatı ve kârı hızla büyüyen şirketleri alan hisse stratejisi."],
 ["Fundamental value strategy", "Temel değer stratejisi", "An equity strategy that buys companies judged to be undervalued.", "Değerinin altında olduğu düşünülen şirketleri alan hisse stratejisi."],
 ["Short-biased strategy", "Kısa ağırlıklı strateji", "An equity strategy focused on finding overvalued shares to sell short.", "Açığa satmak için aşırı değerli payları bulmaya odaklanan hisse stratejisi."],
 ["Notice period", "Bildirim süresi", "The period after a redemption request within which the fund must pay the investor.", "Geri ödeme talebinden sonra fonun yatırımcıya ödeme yapması gereken süre."],
 ["Selection bias", "Seçim yanlılığı", "Distortion in an index caused by funds being classified inconsistently among strategies.", "Fonların stratejiler arasında tutarsız sınıflandırılmasından kaynaklanan endeks bozulması."],
 ["Separately managed account (SMA)", "Ayrı yönetilen hesap", "An account owned by the investor and run by a manager, offering control and transparency.", "Yatırımcının sahibi olduğu ve bir yöneticinin yönettiği, kontrol ve şeffaflık sağlayan hesap."],
],
notes="""<h3>More on hedge funds</h3>
<ul>
<li>Equity strategies: <b>fundamental growth</b> (fast-growing companies), <b>fundamental value</b> (undervalued companies), <b>short bias</b> (overvalued companies), market neutral.</li>
<li><b>Relative value</b> strategies such as convertible arbitrage and fixed income arbitrage aim to be market neutral; distressed and other event-driven strategies usually have a long bias.</li>
<li>Hedge funds are privately offered to qualified or accredited investors, usually as limited partnerships. Terms appear in the private placement memorandum, the partnership agreement and, for individual investors, side letters.</li>
<li><b>Separately managed accounts:</b> investor control, transparency, customized mandates, efficient use of capital and often lower fees; drawbacks include operational complexity and weaker manager incentives.</li>
<li>Evaluate a hedge fund against a strategy-specific benchmark or peer group, not a broad equity index.</li>
<li>Index biases: <b>survivorship</b> (failed funds drop out) and <b>backfill</b> (funds add good past results) overstate returns; <b>selection bias</b> comes from inconsistent classification.</li>
</ul>""",
qs=[
 ["An equity hedge fund that seeks mainly to profit from shares it considers overvalued follows a:", ["short-biased strategy.", "fundamental value strategy.", "fundamental growth strategy."], 0, "Short-biased funds look for overvalued companies to sell short."],
 ["An equity hedge fund that buys companies with rapidly rising revenue and earnings follows a:", ["short-biased strategy.", "fundamental value strategy.", "fundamental growth strategy."], 2, "Growth strategies focus on fast-growing businesses rather than cheap ones."],
 ["Which hedge fund strategy is least likely to have a net long bias?", ["Distressed securities", "Fundamental growth", "Convertible bond arbitrage"], 2, "Convertible arbitrage hedges the equity exposure and aims to be market neutral."],
 ["Which of the following is a relative value hedge fund strategy?", ["Merger arbitrage", "Fixed income arbitrage", "Short-biased equity"], 1, "Relative value strategies exploit pricing differences between related securities."],
 ["The performance of a hedge fund is most appropriately compared with:", ["a broad equity market index.", "a strategy-specific benchmark or peer group.", "the risk-free rate only."], 1, "Strategies differ widely, so the relevant comparison is with similar funds."],
 ["Which of the following is a drawback of investing in a hedge fund strategy through a separately managed account?", ["Less investor control", "Less transparency", "Greater operational complexity"], 2, "The investor gains control and transparency but must handle more operational and governance work."],
 ["After an investor asks to redeem hedge fund shares, the fund must pay within the:", ["lockup period.", "notice period.", "vintage period."], 1, "The notice period is the time the fund has to meet a redemption request."],
 ["A hedge fund index classifies similar funds inconsistently among strategy categories. This creates:", ["backfill bias.", "selection bias.", "survivorship bias."], 1, "Inconsistent allocation of funds to categories is selection bias."],
 ["Hedge funds are most commonly organized as:", ["trusts.", "corporations.", "limited partnerships."], 2, "The general partner manages the fund and investors are limited partners."],
 ["Which statement about hedge funds is most accurate?", ["They are open to all retail investors.", "They are offered privately to qualified investors.", "They are restricted to long-only strategies."], 1, "Hedge funds are lightly regulated private vehicles for qualified or accredited investors."],
 ["Which combination of index biases most likely causes reported hedge fund returns to be overstated?", ["Backfill bias and survivorship bias", "Selection bias and survivorship bias", "Backfill bias and selection bias"], 0, "Both add good results or remove bad ones, pushing reported returns up."],
])

EK["da"] = dict(
terms=[
 ["Token", "Token", "A digital representation, on a distributed ledger, of ownership of an asset or of rights.", "Dağıtık defter üzerinde bir varlığın sahipliğinin veya hakların dijital temsili."],
 ["Tokenization", "Tokenizasyon (varlıkların dijitalleştirilmesi)", "Recording ownership of real-world assets, such as property titles, as tokens on a distributed ledger.", "Tapu gibi gerçek dünya varlıklarının sahipliğini dağıtık defterde token olarak kaydetme."],
 ["Initial coin offering (ICO)", "İlk coin arzı", "A sale of new tokens or cryptocurrency to raise funds, usually with little regulation.", "Fon toplamak için yeni token veya kripto para satışı; genellikle az düzenlenmiştir."],
 ["Decentralized exchange", "Merkeziyetsiz borsa", "A platform where users trade digital assets directly through smart contracts, without an intermediary.", "Kullanıcıların dijital varlıkları aracı olmadan akıllı sözleşmelerle doğrudan alıp sattığı platform."],
 ["Consensus protocol", "Uzlaşı protokolü", "The rules by which network participants agree on the valid state of a ledger, such as proof of work or proof of stake.", "Ağ katılımcılarının defterin geçerli durumu üzerinde anlaştığı kurallar; örneğin iş ispatı veya hisse ispatı."],
 ["Whale", "Balina", "A holder of a large share of a cryptocurrency, able to move its price.", "Bir kripto paranın büyük bölümüne sahip olan ve fiyatını etkileyebilen kişi."],
 ["Coin trust", "Coin tröstü", "A vehicle that holds a large pool of a cryptocurrency directly and issues shares in it.", "Bir kripto paradan doğrudan büyük bir havuz tutan ve bunun paylarını ihraç eden yapı."],
],
notes="""<h3>More on digital assets</h3>
<ul>
<li>A <b>token</b> represents ownership or rights on a distributed ledger. <b>Asset-backed tokens</b> allow fractional ownership of expensive assets, adding liquidity and transparency and reducing transaction costs.</li>
<li><b>Consensus protocols</b> (proof of work, proof of stake) let participants agree on the ledger.</li>
<li>Stablecoins keep a stable value by linking it to reference assets such as currency reserves.</li>
<li><b>ICOs</b> give investors tokens or cryptocurrency, usually without voting rights; compared with IPOs they are cheaper and faster but far less regulated.</li>
<li>Decentralized exchanges are harder to regulate than centralized ones.</li>
<li>Most cryptocurrencies produce no cash flows, so their value rests on their usefulness and on expected price appreciation.</li>
<li>Vehicles: coin trusts hold the cryptocurrency directly; some ETFs and futures give exposure through derivatives and cash settlement.</li>
<li>Risks: volatility, fraud, loss of private keys (irretrievability), regulation, and, for small coins, <b>whales</b> who can move prices.</li>
</ul>""",
qs=[
 ["On a distributed ledger, ownership of a physical asset is most likely represented by a:", ["token.", "blockchain.", "consensus protocol."], 0, "Tokens represent ownership or rights; the blockchain is the ledger itself."],
 ["A stablecoin maintains a stable value mainly by:", ["being issued by a central bank.", "linking its value to reference assets.", "paying a fixed interest rate."], 1, "Stablecoins are backed by or pegged to assets such as currency reserves."],
 ["Proof of work and proof of stake are examples of:", ["tokens.", "consensus protocols.", "smart contracts."], 1, "They are methods for network participants to agree on the state of the ledger."],
 ["Investors in an initial coin offering typically receive:", ["registered shares.", "tokens or cryptocurrency.", "voting rights in the issuer."], 1, "ICOs sell digital tokens, usually without ownership or voting rights."],
 ["Compared with centralized exchanges, decentralized exchanges are more:", ["difficult to regulate.", "dependent on intermediaries.", "transparent about user identities."], 0, "Without a central operator, there is no single entity to supervise."],
 ["Unlike shares, most cryptocurrencies cannot be valued by:", ["observing market prices.", "comparing them with similar assets.", "discounting expected future cash flows."], 2, "They pay no dividends or interest, so cash flow valuation does not apply."],
 ["Tokenizing ownership of an expensive building is most likely to:", ["reduce its liquidity.", "increase its liquidity through fractional ownership.", "raise the costs of transferring ownership."], 1, "Smaller units can be traded more easily, with transparent records and lower transaction costs."],
 ["Which investment vehicle holds a cryptocurrency directly?", ["A coin trust", "A cash-settled cryptocurrency futures contract", "A futures-based cryptocurrency ETF"], 0, "Coin trusts own a pool of the coin; futures and futures-based funds do not."],
 ["Compared with an IPO, an initial coin offering typically involves:", ["higher issuance costs.", "lower issuance costs.", "more regulatory oversight."], 1, "ICOs avoid underwriters and registration, which lowers costs but also investor protection."],
 ["The risk that a few large holders can manipulate a cryptocurrency's price is most significant for:", ["large, widely held cryptocurrencies.", "small, thinly held cryptocurrencies.", "stablecoins backed by cash reserves."], 1, "Concentrated holdings in small coins let 'whales' move prices."],
 ["An investor who loses the private key to her cryptocurrency wallet faces the risk of:", ["fraud.", "irretrievability.", "counterparty default."], 1, "Without the key, the holdings cannot be accessed or recovered."],
 ["A government records vehicle ownership titles as digital tokens on a distributed ledger. This is best described as:", ["mining.", "tokenization.", "a smart contract."], 1, "Representing real-world assets as tokens is tokenization."],
 ["Digital assets may improve a traditional portfolio mainly by providing:", ["stable returns.", "guaranteed income.", "potential diversification."], 2, "Their returns have at times had low correlation with traditional assets, though they are very volatile."],
])
