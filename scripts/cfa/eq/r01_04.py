# CFA Level I · Equity Investments · readings 1–4. Original study notes and questions.
R = []

R.append(dict(id="mo", n="Market Organization and Structure", k="MARKETS", w=4, c="#3b7dd8",
terms=[
 ["Financial intermediary", "Finansal aracı", "An institution that stands between buyers and sellers or between savers and borrowers, such as a broker, dealer, bank or fund.", "Alıcılar ile satıcılar ya da tasarruf sahipleri ile borçlular arasında yer alan aracı kurum, banka veya fon gibi kuruluş."],
 ["Broker", "Aracı (broker)", "An agent who executes orders for clients and does not trade on its own account.", "Müşteri emirlerini yerine getiren ve kendi hesabına işlem yapmayan aracı."],
 ["Dealer", "Piyasa yapıcı (dealer)", "A firm that trades from its own inventory, buying at the bid and selling at the ask.", "Kendi portföyünden işlem yapan; alış fiyatından alıp satış fiyatından satan kurum."],
 ["Short position", "Açık (kısa) pozisyon", "A position that gains when the asset's price falls, for example selling borrowed shares.", "Varlığın fiyatı düştüğünde kazandıran pozisyon; örneğin ödünç alınan payların satılması."],
 ["Margin loan", "Kredili işlem kredisi", "Money borrowed from a broker to buy securities, with the securities as collateral.", "Menkul kıymet almak için aracı kurumdan alınan, menkul kıymetlerin teminat olduğu borç."],
 ["Initial margin", "Başlangıç teminatı", "The share of the purchase price the investor must pay with own money.", "Alış bedelinin yatırımcının kendi parasıyla ödemesi gereken oranı."],
 ["Maintenance margin", "Sürdürme teminatı", "The minimum equity, as a share of the position's value, the investor must keep in the account.", "Yatırımcının hesapta tutması gereken, pozisyon değerine oranla asgari özkaynak."],
 ["Margin call", "Teminat tamamlama çağrısı", "A demand to add funds when equity in a margin account falls below the maintenance margin.", "Kredili hesaptaki özkaynak sürdürme teminatının altına düştüğünde ek para yatırılması talebi."],
 ["Limit order", "Limitli emir", "An order to trade only at a specified price or better.", "Yalnızca belirlenen fiyattan veya daha iyisinden işlem yapılmasını isteyen emir."],
 ["Stop order", "Zarar durdur emri", "An order that becomes active only after the price reaches a specified level.", "Fiyat belirlenen düzeye ulaştıktan sonra devreye giren emir."],
 ["Primary market", "Birincil piyasa", "The market in which issuers sell newly created securities to investors.", "İhraççıların yeni oluşturulan menkul kıymetleri yatırımcılara sattığı piyasa."],
 ["Order-driven market", "Emir güdümlü piyasa", "A market in which trades are set by matching buy and sell orders under fixed rules.", "İşlemlerin belirli kurallarla alış ve satış emirlerinin eşleştirilmesiyle gerçekleştiği piyasa."],
],
notes="""<h3>What the financial system does</h3>
<ul>
<li>It lets people save and borrow, raise equity, manage risk, exchange assets for immediate and future delivery, and trade on information.</li>
<li>Its economic job is to <b>discover prices</b> and to <b>allocate capital</b> to its most productive uses.</li>
</ul>
<h3>Intermediaries</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>Role</th></tr>
<tr><td>Brokers, exchanges, alternative trading systems</td><td>Bring buyers and sellers together</td></tr>
<tr><td>Dealers</td><td>Provide liquidity by trading from their own inventory</td></tr>
<tr><td>Securitizers, investment companies</td><td>Pool assets and issue claims on the pool</td></tr>
<tr><td>Banks</td><td>Take deposits and lend</td></tr>
<tr><td>Insurers, arbitrageurs, clearing houses</td><td>Transfer risk, connect markets, guarantee settlement</td></tr>
</table></div>
<h3>Positions and leverage</h3>
<ul>
<li><b>Long:</b> gains when the price rises. <b>Short:</b> gains when the price falls. A short seller borrows shares, sells them, and later buys them back; it must pay the lender any dividends.</li>
<li>Buying on margin magnifies returns in both directions.</li>
</ul>
<p class="f">leverage ratio = 1 / initial margin</p>
<p class="f">price that triggers a margin call = P<sub>0</sub> × (1 − initial margin) / (1 − maintenance margin)</p>
<ul>
<li>Return on a margin purchase = (ending value − loan repaid − interest + dividends − equity invested) / equity invested.</li>
</ul>
<h3>Orders</h3>
<div class="tbl"><table>
<tr><th>Instruction</th><th>Examples</th></tr>
<tr><td>Execution: how to fill</td><td>Market order (immediately at best price); limit order (at the limit price or better)</td></tr>
<tr><td>Validity: when</td><td>Day order, good-till-cancelled, immediate-or-cancel, fill-or-kill, good-on-close</td></tr>
<tr><td>Clearing: how to settle</td><td>Instructions for the clearing firm; whether a sale is short</td></tr>
</table></div>
<ul>
<li>A buy limit order above the best ask (or a sell limit below the best bid) is <b>marketable</b>. A buy limit below the best bid is <b>behind the market</b>. A limit between the bid and the ask <b>makes a new market</b>.</li>
<li>A <b>stop-sell</b> order below the current price limits losses on a long position; a <b>stop-buy</b> above the price limits losses on a short.</li>
</ul>
<h3>Primary and secondary markets</h3>
<ul>
<li>Primary: new issues, through underwritten offerings, best-efforts offerings, private placements, shelf registrations, rights offerings.</li>
<li>Secondary: existing securities change hands. A liquid secondary market makes primary issuance easier and cheaper.</li>
</ul>
<div class="tbl"><table>
<tr><th>Market structure</th><th>How prices are set</th></tr>
<tr><td>Quote-driven (dealer)</td><td>Investors trade at dealers' quoted prices</td></tr>
<tr><td>Order-driven</td><td>Orders matched by rules: price priority, then display, then time</td></tr>
<tr><td>Brokered</td><td>Brokers search for counterparties, for unique assets such as large blocks or real estate</td></tr>
</table></div>
<h3>A well-functioning financial system</h3>
<ul>
<li><b>Operationally efficient:</b> low trading costs. <b>Informationally efficient:</b> prices quickly reflect information. <b>Allocationally efficient:</b> capital flows to its best uses.</li>
<li>Regulation aims to control fraud, agency problems and systemic risk, and to promote fairness.</li>
</ul>
<div class="trap"><b>Exam trap</b>In the margin call formula, use (1 − maintenance margin) in the denominator, not the maintenance margin itself.</div>""",
qs=[
 ["An investor buys 100 shares at $50 using an initial margin of 40% and later sells them at $60. Ignoring interest and dividends, the return on her equity is closest to:", ["20%", "33%", "50%"], 2, "Equity invested is 100 × 50 × 0.40 = $2,000. The gain is 100 × 10 = $1,000, so the return is 50%. Without leverage it would be 20%."],
 ["With an initial margin requirement of 40%, the maximum leverage ratio is:", ["1.67", "2.50", "4.00"], 1, "Leverage ratio = 1 / initial margin = 1 / 0.40 = 2.5."],
 ["An investor buys a share at $40 with an initial margin of 50%. The maintenance margin is 25%. The price below which she receives a margin call is closest to:", ["$20.00", "$26.67", "$30.00"], 1, "40 × (1 − 0.50) / (1 − 0.25) = 20 / 0.75 = $26.67."],
 ["The best bid is $26.00 and the best ask is $26.10. A limit order to buy at $25.80 is best described as:", ["marketable.", "behind the market.", "making a new market."], 1, "A buy limit below the best bid cannot be filled until prices fall, so it is behind the market."],
 ["An investor who owns a share and wants to limit her loss if the price falls should place a:", ["stop-sell order.", "limit-buy order.", "market-buy order."], 0, "A stop-sell order below the current price becomes active if the price falls to that level."],
 ["A company selling newly issued shares to investors for the first time is a transaction in the:", ["primary market.", "secondary market.", "over-the-counter dealer market."], 0, "Sales of new securities by issuers take place in the primary market."],
 ["A market in which investors trade with dealers at the prices the dealers quote is a:", ["brokered market.", "order-driven market.", "quote-driven market."], 2, "In a quote-driven market, dealers post bid and ask prices and trade from their inventory."],
 ["A financial system in which prices quickly reflect all available information is best described as:", ["operationally efficient.", "allocationally efficient.", "informationally efficient."], 2, "Informational efficiency concerns how fast and accurately prices incorporate information."],
 ["An order that must be filled immediately and in full, or not at all, is a:", ["day order.", "fill-or-kill order.", "good-till-cancelled order."], 1, "A fill-or-kill order is cancelled unless it can be executed at once in its entirety."],
 ["A short seller of a dividend-paying share must:", ["receive the dividends.", "pay the dividends to the share lender.", "pay the dividends to the issuing company."], 1, "The lender of the shares is still entitled to the dividends, so the short seller must pay them."],
]))

R.append(dict(id="ix", n="Security Market Indexes", k="INDEXES", w=4, c="#2e9e8f",
terms=[
 ["Security market index", "Menkul kıymet piyasası endeksi", "A measure of the value of a group of securities that represents a market or segment.", "Bir piyasayı veya bölümü temsil eden menkul kıymet grubunun değerinin ölçüsü."],
 ["Price return", "Fiyat getirisi", "The return from changes in the prices of the constituents only.", "Yalnızca endeks bileşenlerinin fiyat değişimlerinden kaynaklanan getiri."],
 ["Total return", "Toplam getiri", "The return from price changes plus the income, such as dividends, paid by the constituents.", "Fiyat değişimleri ile bileşenlerin ödediği temettü gibi gelirlerin toplam getirisi."],
 ["Price-weighted index", "Fiyat ağırlıklı endeks", "An index in which each security's weight is its price divided by the sum of all prices.", "Her menkul kıymetin ağırlığının, fiyatının tüm fiyatların toplamına bölümü olduğu endeks."],
 ["Equal-weighted index", "Eşit ağırlıklı endeks", "An index in which every constituent has the same weight.", "Tüm bileşenlerin aynı ağırlığa sahip olduğu endeks."],
 ["Market-capitalization-weighted index", "Piyasa değeri ağırlıklı endeks", "An index in which weights are proportional to each company's market value.", "Ağırlıkların her şirketin piyasa değeriyle orantılı olduğu endeks."],
 ["Float adjustment", "Fiili dolaşım düzeltmesi", "Using only shares available to the public, excluding those held by insiders or governments.", "İçeriden kişilerin veya devletlerin elindeki paylar hariç, yalnızca halka açık payların kullanılması."],
 ["Fundamental weighting", "Temel göstergelere göre ağırlıklandırma", "Weighting constituents by measures such as earnings, sales or book value instead of price.", "Bileşenleri fiyat yerine kâr, satış veya defter değeri gibi ölçütlere göre ağırlıklandırma."],
 ["Rebalancing", "Yeniden dengeleme", "Adjusting the weights of existing constituents back to their target weights.", "Mevcut bileşenlerin ağırlıklarını hedef ağırlıklarına geri getirme."],
 ["Reconstitution", "Endeks bileşimini yenileme", "Changing which securities are included in the index.", "Endekse hangi menkul kıymetlerin dahil olduğunu değiştirme."],
 ["Survivorship bias", "Hayatta kalma yanlılığı", "Upward bias that arises when failed or closed members drop out of a data set.", "Başarısız olan veya kapanan üyelerin veri setinden çıkmasıyla ortaya çıkan yukarı yönlü yanlılık."],
],
notes="""<h3>Price return and total return</h3>
<p class="f">price return = (V<sub>1</sub> − V<sub>0</sub>) / V<sub>0</sub> &nbsp;&nbsp;&nbsp; total return = (V<sub>1</sub> − V<sub>0</sub> + income) / V<sub>0</sub></p>
<ul>
<li>Over long periods the gap between the two grows large, because dividends compound.</li>
</ul>
<h3>Building an index</h3>
<ul>
<li>Choices: the market it represents, which securities, how to weight them, when to rebalance, when to reconstitute.</li>
</ul>
<div class="tbl"><table>
<tr><th>Weighting</th><th>Weight of each security</th><th>Strength</th><th>Weakness</th></tr>
<tr><td>Price</td><td>Price / sum of prices</td><td>Simple</td><td>Arbitrary: high-priced shares dominate; splits change weights</td></tr>
<tr><td>Equal</td><td>1 / number of securities</td><td>Simple, no concentration</td><td>Overweights small companies; needs frequent rebalancing</td></tr>
<tr><td>Market capitalization</td><td>Market value / total market value</td><td>Reflects the investable market; self-rebalancing</td><td>Overweights overvalued and large companies; momentum tilt</td></tr>
<tr><td>Fundamental</td><td>Earnings, sales, book value or dividends</td><td>Avoids overweighting overvalued shares</td><td>Value tilt; needs rebalancing</td></tr>
</table></div>
<ul>
<li>A price-weighted index equals the sum of prices divided by a <b>divisor</b>; the divisor is changed after splits or composition changes so that the index level does not jump.</li>
<li>Its return equals the return on a portfolio holding <b>one share</b> of each constituent.</li>
<li>An equal-weighted return is the simple average of the constituents' returns.</li>
</ul>
<h3>Uses of indexes</h3>
<ul>
<li>Gauges of market sentiment, proxies for the market in risk and return models (such as the CAPM), benchmarks for active managers, models for index funds and ETFs, and measures of asset allocation results.</li>
</ul>
<h3>Indexes by asset class</h3>
<ul>
<li><b>Equity:</b> broad market, multi-market, sector, style (value, growth, size).</li>
<li><b>Fixed income:</b> harder to build and replicate. The universe is huge, issues mature and change constantly, many bonds trade rarely, and prices often come from dealers' estimates.</li>
<li><b>Commodities:</b> based on futures, so returns include the roll and the collateral yield, not only spot prices.</li>
<li><b>Real estate:</b> appraisal-based, repeat-sales, or based on listed real estate investment trusts.</li>
<li><b>Hedge funds:</b> built from voluntary reports. Funds stop reporting when they do badly, which creates <b>survivorship bias</b> and overstates returns.</li>
</ul>
<div class="trap"><b>Exam trap</b>In a price-weighted index, a 10% move in the highest-priced share has the largest effect, whatever the company's size.</div>""",
qs=[
 ["An index contains three shares priced at $10, $20 and $30. Over a month their prices change to $12, $18 and $33. The price return on a price-weighted index of these shares is closest to:", ["5.0%", "6.7%", "10.0%"], 0, "Sum of prices goes from 60 to 63, a return of 5.0%. The divisor cancels out."],
 ["An index contains three shares priced at $10, $20 and $30. Over a month their prices change to $12, $18 and $33. The price return on an equal-weighted index of these shares is closest to:", ["5.0%", "6.7%", "10.0%"], 1, "The individual returns are +20%, −10% and +10%; their average is 6.7%."],
 ["An index contains three shares priced at $10, $20 and $30, with 100, 50 and 10 shares outstanding. Their prices change to $12, $18 and $33. The price return on a market-capitalization-weighted index is closest to:", ["5.0%", "5.7%", "6.7%"], 1, "Market value rises from 1,000 + 1,000 + 300 = 2,300 to 1,200 + 900 + 330 = 2,430, a return of 5.7%."],
 ["In a price-weighted index, the constituent with the greatest weight is the one with the:", ["highest share price.", "most shares outstanding.", "largest market capitalization."], 0, "Weights depend only on price, regardless of the number of shares or company size."],
 ["Over a year, an equity index had a price return of 6% and its constituents paid dividends equal to 2% of the starting value. The total return is closest to:", ["4%", "6%", "8%"], 2, "Total return adds income to the price change: 6% + 2% = 8%."],
 ["A disadvantage of an equal-weighted index is that it:", ["requires frequent rebalancing.", "is dominated by the largest companies.", "gives the most weight to the highest-priced shares."], 0, "Price changes move weights away from equality, so the index must be rebalanced often."],
 ["Compared with a market-capitalization-weighted index, a fundamentally weighted index typically has a:", ["value tilt.", "growth tilt.", "momentum tilt."], 0, "Weights based on earnings or book value give relatively more weight to shares with low prices relative to fundamentals."],
 ["Removing some securities from an index and adding new ones is called:", ["rebalancing.", "reconstitution.", "float adjustment."], 1, "Reconstitution changes the membership of the index; rebalancing changes the weights of existing members."],
 ["Hedge fund indexes are most likely to:", ["overstate returns.", "understate returns.", "use price weighting."], 0, "Funds report voluntarily and stop reporting after poor results, so survivorship bias pushes reported returns up."],
 ["Compared with equity indexes, bond indexes are more difficult to construct and replicate mainly because:", ["bonds pay periodic coupons.", "bond markets have fewer issuers.", "many bonds trade infrequently and their constituents change often."], 2, "Illiquidity, dealer-estimated prices and frequent turnover as bonds mature make bond indexes hard to build and track."],
]))

R.append(dict(id="me", n="Market Efficiency", k="EFFICIENCY", w=4, c="#c0563f",
terms=[
 ["Market efficiency", "Piyasa etkinliği", "The degree to which prices quickly and fully reflect available information.", "Fiyatların mevcut bilgiyi ne kadar hızlı ve eksiksiz yansıttığının derecesi."],
 ["Intrinsic value", "İçsel değer", "The value an investor with full understanding of an asset's characteristics would place on it.", "Varlığın özelliklerini tam olarak anlayan bir yatırımcının ona biçeceği değer."],
 ["Weak-form efficiency", "Zayıf formda etkinlik", "Prices reflect all past market data, such as prices and volume.", "Fiyatların fiyat ve hacim gibi tüm geçmiş piyasa verilerini yansıtması."],
 ["Semi-strong-form efficiency", "Yarı güçlü formda etkinlik", "Prices reflect all publicly available information.", "Fiyatların kamuya açık tüm bilgiyi yansıtması."],
 ["Strong-form efficiency", "Güçlü formda etkinlik", "Prices reflect all information, public and private.", "Fiyatların kamuya açık ve özel tüm bilgiyi yansıtması."],
 ["Abnormal return", "Olağandışı getiri", "The return in excess of what a model predicts for the risk taken.", "Üstlenilen risk için bir modelin öngördüğünün üzerindeki getiri."],
 ["Event study", "Olay çalışması", "A test of how quickly and how much prices react to a specific announcement.", "Fiyatların belirli bir açıklamaya ne kadar hızlı ve ne ölçüde tepki verdiğinin testi."],
 ["Market anomaly", "Piyasa anomalisi", "A persistent pattern in returns that is inconsistent with market efficiency.", "Piyasa etkinliğiyle bağdaşmayan, süreklilik gösteren getiri örüntüsü."],
 ["January effect", "Ocak etkisi", "The tendency of small-company shares to earn unusually high returns in early January.", "Küçük şirket paylarının ocak ayı başında olağandışı yüksek getiri sağlama eğilimi."],
 ["Momentum", "Momentum", "The tendency of recent winners to keep outperforming, and losers to keep underperforming, in the short term.", "Kısa vadede son dönemin kazananlarının iyi, kaybedenlerinin kötü performansı sürdürme eğilimi."],
 ["Loss aversion", "Kayıptan kaçınma", "Feeling the pain of a loss more strongly than the pleasure of an equal gain.", "Bir kaybın acısını, eşit büyüklükteki bir kazancın hazzından daha güçlü hissetme."],
 ["Herding", "Sürü davranışı", "Trading in the same direction as other investors, ignoring one's own information.", "Kendi bilgisini göz ardı ederek diğer yatırımcılarla aynı yönde işlem yapma."],
],
notes="""<h3>What efficiency means</h3>
<ul>
<li>In an efficient market, prices adjust quickly and accurately to new information, so no one can consistently earn returns above those justified by risk, after costs.</li>
<li>The market price is an unbiased estimate of intrinsic value. Individual prices may be wrong, but not in a predictable way.</li>
<li>Only <b>unexpected</b> information moves prices. Expected news is already in the price.</li>
</ul>
<h3>What makes a market more efficient</h3>
<ul>
<li>Many participants and analysts, easy access to information, few restrictions on trading (including short selling), low transaction and information costs.</li>
<li>Prices may stay away from intrinsic value by up to the cost of trading on the mispricing.</li>
</ul>
<h3>Three forms</h3>
<div class="tbl"><table>
<tr><th>Form</th><th>Prices reflect</th><th>Cannot earn abnormal returns with</th></tr>
<tr><td>Weak</td><td>Past prices and volume</td><td>Technical analysis</td></tr>
<tr><td>Semi-strong</td><td>All public information</td><td>Technical and fundamental analysis</td></tr>
<tr><td>Strong</td><td>All public and private information</td><td>Any information, including insider information</td></tr>
</table></div>
<ul>
<li>Evidence: developed markets are broadly weak-form and semi-strong-form efficient. They are not strong-form efficient: insiders can profit, which is why insider trading is illegal.</li>
<li>Implication for investors: in efficient markets, passive low-cost indexing is hard to beat. Active managers still add value by matching portfolios to clients' needs, and their analysis is what makes prices efficient.</li>
</ul>
<h3>Anomalies</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>Examples</th></tr>
<tr><td>Time series</td><td>January effect, day-of-week effects, momentum, overreaction followed by reversal</td></tr>
<tr><td>Cross-sectional</td><td>Size effect, value effect (low price-to-book shares outperforming)</td></tr>
<tr><td>Other</td><td>Closed-end fund discounts, slow price reaction after earnings surprises, IPO underperformance over the long run</td></tr>
</table></div>
<ul>
<li>Many anomalies shrink or disappear once published, are too small to exploit after costs, or are compensation for risk. Some are the product of <b>data mining</b>.</li>
</ul>
<h3>Behavioural finance</h3>
<ul>
<li>Investors may be loss-averse, overconfident, inclined to follow the herd, or to treat information inconsistently. These biases may explain some anomalies.</li>
<li>Markets can still be efficient if biased investors' trades are not predictable or are offset by arbitrageurs.</li>
</ul>
<div class="trap"><b>Exam trap</b>Strong-form efficiency implies semi-strong and weak form. Weak-form efficiency says nothing about whether fundamental analysis works.</div>""",
qs=[
 ["If a market is weak-form efficient, investors cannot consistently earn abnormal returns using:", ["insider information.", "technical analysis.", "fundamental analysis."], 1, "Weak-form efficiency means prices already reflect past trading data, which is what technical analysis uses."],
 ["If a market is semi-strong-form efficient, investors cannot consistently earn abnormal returns using:", ["insider information.", "analysis of published financial statements.", "information not yet available to the public."], 1, "All public information, including financial statements, is reflected in prices. Private information could still earn abnormal returns."],
 ["Evidence that corporate insiders earn abnormal returns when trading their own company's shares is inconsistent with:", ["weak-form efficiency.", "strong-form efficiency.", "semi-strong-form efficiency."], 1, "Only the strong form says that private information is reflected in prices."],
 ["Which of the following is most likely to reduce the efficiency of a market?", ["More analysts following the market", "Lower transaction costs", "Restrictions on short selling"], 2, "If pessimistic investors cannot sell short, their information reaches prices more slowly."],
 ["In an informationally efficient market, the market price of a share is best described as:", ["always equal to its intrinsic value.", "always below its intrinsic value.", "an unbiased estimate of its intrinsic value."], 2, "Prices can differ from intrinsic value, but the errors are not predictable in direction."],
 ["Small-company shares earning unusually high returns in the first days of the year is known as the:", ["size effect.", "January effect.", "momentum effect."], 1, "The January effect is a calendar anomaly often linked to tax-loss selling at year-end."],
 ["Shares that have performed well over the past several months continuing to outperform over the next few months is an example of:", ["momentum.", "the value effect.", "overreaction."], 0, "Momentum is the short-term persistence of relative performance."],
 ["An investor who holds on to losing shares in order to avoid realizing a loss is most likely exhibiting:", ["herding.", "loss aversion.", "overconfidence."], 1, "Loss aversion makes realizing losses feel especially painful."],
 ["If markets are highly efficient, the most appropriate strategy for most investors is to:", ["time the market.", "trade frequently on news.", "hold a low-cost passive portfolio."], 2, "When prices already reflect information, active trading adds costs without reliably adding returns."],
 ["In an efficient market, a share's price is most likely to change when a company announces earnings that are:", ["in line with expectations.", "different from expectations.", "the same as in the previous year."], 1, "Only the unexpected part of news changes prices; expected information is already reflected."],
]))

R.append(dict(id="eq", n="Overview of Equity Securities", k="EQUITY", w=4, c="#8a5cc2",
terms=[
 ["Common shares", "Adi paylar", "Equity with a residual claim on assets and profits and, usually, voting rights.", "Varlıklar ve kâr üzerinde artık hak ve genellikle oy hakkı taşıyan özkaynak payı."],
 ["Preference shares", "İmtiyazlı paylar", "Equity with priority over common shares for dividends and in liquidation, usually without voting rights.", "Temettü ve tasfiyede adi paylara göre öncelikli, genellikle oy hakkı olmayan pay."],
 ["Cumulative preference shares", "Birikimli imtiyazlı paylar", "Preference shares whose unpaid dividends accrue and must be paid before any common dividend.", "Ödenmeyen temettüleri biriken ve adi paylara temettü ödenmeden önce ödenmesi gereken imtiyazlı paylar."],
 ["Statutory voting", "Olağan (pay başına) oylama", "Each share carries one vote for each board seat.", "Her payın her yönetim kurulu koltuğu için bir oy taşıdığı oylama."],
 ["Cumulative voting", "Birikimli oylama", "Shareholders may cast all their votes for one or a few board candidates.", "Pay sahiplerinin tüm oylarını bir veya birkaç kurul adayına verebildiği oylama."],
 ["Callable shares", "Geri çağrılabilir paylar", "Shares that the issuer may buy back at a set price.", "İhraççının belirli bir fiyattan geri alabileceği paylar."],
 ["Putable shares", "Satma hakkı tanınan paylar", "Shares that the holder may sell back to the issuer at a set price.", "Sahibinin ihraççıya belirli bir fiyattan geri satabileceği paylar."],
 ["Convertible preference shares", "Dönüştürülebilir imtiyazlı paylar", "Preference shares that the holder can exchange for a set number of common shares.", "Sahibinin belirli sayıda adi paya dönüştürebileceği imtiyazlı paylar."],
 ["Depository receipt", "Depo sertifikası", "A security traded locally that represents shares of a foreign company held by a bank.", "Bir bankanın elinde tutulan yabancı şirket paylarını temsil eden, yerel piyasada işlem gören menkul kıymet."],
 ["Book value of equity", "Özkaynakların defter değeri", "Total assets minus total liabilities as reported on the balance sheet.", "Bilançoda raporlanan toplam varlıklar eksi toplam yükümlülükler."],
 ["Cost of equity", "Özkaynak maliyeti", "The minimum return investors require to hold the company's shares.", "Yatırımcıların şirketin paylarını tutmak için istediği en düşük getiri."],
 ["Private equity", "Girişim sermayesi (özel sermaye)", "Equity in companies whose shares are not publicly traded.", "Payları halka açık olarak işlem görmeyen şirketlerdeki özkaynak."],
],
notes="""<h3>Role of equity</h3>
<ul>
<li>Over long periods, equities have earned higher returns than bonds and bills, with higher volatility. They have been a reasonable but imperfect hedge against inflation.</li>
</ul>
<h3>Types of equity</h3>
<div class="tbl"><table>
<tr><th></th><th>Common shares</th><th>Preference shares</th></tr>
<tr><td>Dividend</td><td>Variable, at the board's discretion</td><td>Fixed rate; paid before common dividends</td></tr>
<tr><td>Claim in liquidation</td><td>Residual, last</td><td>Ahead of common, behind debt</td></tr>
<tr><td>Voting</td><td>Usually yes</td><td>Usually no</td></tr>
<tr><td>Risk</td><td>Higher</td><td>Lower, closer to debt</td></tr>
</table></div>
<ul>
<li><b>Cumulative</b> preference: missed dividends accrue. <b>Non-cumulative:</b> missed dividends are lost. <b>Participating:</b> extra dividend if profits exceed a target.</li>
<li><b>Callable</b> shares benefit the issuer and trade at a lower price; <b>putable</b> shares benefit the investor and trade at a higher price.</li>
<li><b>Convertible preference</b> gives fixed dividends plus the upside of conversion.</li>
<li><b>Statutory voting:</b> one vote per share per seat. <b>Cumulative voting:</b> votes = shares × seats, which can be concentrated; it helps minority shareholders win representation.</li>
<li>Dual-class structures give some shares more votes, letting founders keep control.</li>
</ul>
<h3>Public and private equity</h3>
<ul>
<li>Private equity: no public market, less liquidity, less disclosure, longer horizon, potentially stronger owner control over management.</li>
<li>Forms: venture capital (early-stage companies), leveraged buyouts, private investment in public equity.</li>
</ul>
<h3>Investing abroad</h3>
<ul>
<li><b>Direct investment:</b> buying shares on the foreign exchange, in its currency and under its rules.</li>
<li><b>Depository receipts:</b> traded locally, representing foreign shares. <b>Sponsored</b> (the foreign company is involved; holders get voting rights) or <b>unsponsored</b> (the bank acts alone; the bank keeps voting rights). Global depository receipts trade outside both the home country and the United States; American depository receipts trade in the United States.</li>
<li>Exchange-traded funds and baskets of depository receipts offer diversified exposure.</li>
</ul>
<h3>Book value, market value and returns</h3>
<p class="f">ROE = net income / average book value of equity</p>
<ul>
<li>Market value reflects investors' expectations of future cash flows. A price-to-book ratio above 1 means investors expect the company to create value beyond its recorded assets.</li>
<li>ROE can rise because profit rose, or because equity fell (for example through write-offs or buybacks), so look at the cause.</li>
<li>The <b>cost of equity</b> is the return investors require; it is not directly observable and must be estimated, for example with a dividend discount model or the CAPM.</li>
</ul>
<div class="trap"><b>Exam trap</b>Under cumulative voting, a holder of 100 shares electing 5 directors has 500 votes and may give all 500 to a single candidate.</div>""",
qs=[
 ["A shareholder owns 100 shares in an election for five board seats. Under cumulative voting, the maximum number of votes she can cast for a single candidate is:", ["100", "400", "500"], 2, "Total votes = shares × seats = 500, all of which may go to one candidate."],
 ["A company has net income of 120, beginning equity of 900 and ending equity of 1,100. Its return on equity is closest to:", ["10.9%", "12.0%", "13.3%"], 1, "ROE = 120 / average equity of 1,000 = 12.0%."],
 ["If a company skips a dividend on its cumulative preference shares, the missed dividend:", ["is permanently lost.", "is converted into common shares.", "must be paid before any common dividend."], 2, "Arrears on cumulative preference shares must be paid in full before ordinary shareholders receive dividends."],
 ["Compared with otherwise identical non-callable preference shares, callable preference shares most likely trade at:", ["a lower price.", "a higher price.", "the same price."], 0, "The call option belongs to the issuer, which limits the investor's upside, so investors pay less."],
 ["Compared with ordinary shares, putable shares are:", ["less risky for investors.", "more risky for investors.", "equally risky for investors."], 0, "The right to sell back at a set price limits the investor's downside."],
 ["Holders of sponsored depository receipts most likely:", ["have no voting rights.", "receive voting rights.", "must trade on the issuer's home exchange."], 1, "In a sponsored arrangement the foreign company is involved and the receipt holders obtain voting rights."],
 ["Compared with public equity, private equity is most likely characterized by:", ["more liquidity.", "more extensive public disclosure.", "a longer investment horizon."], 2, "Private equity investors are not under pressure from quarterly market expectations, and their holdings are illiquid."],
 ["A company's shares trade well above their book value. This most likely indicates that investors:", ["expect the company to create value.", "consider the shares overvalued.", "expect the company to be liquidated."], 0, "Market value above book value reflects expected future growth and profitability not captured on the balance sheet."],
 ["Which of the following is generally the least risky for an investor?", ["Ordinary shares", "Callable ordinary shares", "Cumulative preference shares"], 2, "Preference shares rank ahead of ordinary shares for dividends and in liquidation, and cumulative ones protect missed dividends."],
 ["A company's cost of equity is best described as the:", ["dividend paid per share.", "return on equity reported in its accounts.", "minimum return investors require to hold its shares."], 2, "The cost of equity is investors' required return; it must be estimated because it cannot be observed directly."],
]))
