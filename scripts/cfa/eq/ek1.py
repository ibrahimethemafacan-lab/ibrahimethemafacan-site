# CFA Level I · Equity Investments · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
EK = {}

EK["mo"] = dict(
terms=[
 ["Real asset", "Reel varlık", "A physical asset such as real estate, equipment or commodities.", "Gayrimenkul, ekipman veya emtia gibi fiziki varlık."],
 ["Financial asset", "Finansal varlık", "A claim such as a security, contract or currency; shares of a mining company are financial assets.", "Menkul kıymet, sözleşme veya döviz gibi bir alacak hakkı; bir maden şirketinin payları da finansal varlıktır."],
 ["Validity instruction", "Geçerlilik talimatı", "An order instruction stating when an order may be filled, such as day, good-till-cancelled or fill-or-kill.", "Emrin ne zaman gerçekleşebileceğini belirten talimat; örneğin günlük, iptal edilene kadar geçerli veya gerçekleşmezse iptal."],
 ["Execution instruction", "Gerçekleştirme talimatı", "An order instruction stating how to fill an order, such as market or limit.", "Emrin nasıl gerçekleştirileceğini belirten talimat; örneğin piyasa veya limit emri."],
 ["Behind the market", "Piyasanın gerisinde", "A limit buy below the best bid or a limit sell above the best ask; least likely to be filled.", "En iyi alışın altındaki limit alış veya en iyi satışın üstündeki limit satış; gerçekleşme olasılığı en düşüktür."],
 ["Call market", "Seans (call) piyasası", "A market in which a security trades only at specific times, at one price that clears the market.", "Bir menkul kıymetin yalnızca belirli zamanlarda, piyasayı temizleyen tek bir fiyattan işlem gördüğü piyasa."],
 ["Brokered market", "Aracılı piyasa", "A market in which brokers find counterparties, used for unique assets such as art or real estate.", "Aracıların karşı taraf bulduğu piyasa; sanat eseri veya gayrimenkul gibi benzersiz varlıklar için kullanılır."],
 ["Securitizer", "Menkul kıymetleştiren kurum", "An intermediary that issues securities backed by a pool of similar assets.", "Benzer varlıklardan oluşan bir havuza dayalı menkul kıymet ihraç eden aracı."],
],
notes="""<h3>More on margin and orders</h3>
<p class="f">margin call price = P<sub>0</sub> × (1 − initial margin) / (1 − maintenance margin)</p>
<p class="f">leverage ratio = 1 / initial margin · return on equity = (ending value − loan − interest + dividends − equity) / equity</p>
<ul>
<li>Initial margin is the minimum equity required at purchase. After a margin call, the account must be restored to the <b>initial</b> margin.</li>
<li>A <b>stop-loss sell</b> protects a long position; a <b>stop buy</b> protects a short position.</li>
<li>Order instructions: execution (market, limit, all-or-nothing), validity (day, GTC, fill-or-kill, stop), clearing.</li>
<li>Limit orders: <b>inside the market</b> between best bid and best ask; <b>aggressive</b> if they can be filled at once; <b>behind the market</b> if away from the best quotes.</li>
<li>Short sellers pay the lender any dividends, must post margin and cannot withdraw the sale proceeds.</li>
<li>Markets: order-driven (price and time priority; crossing networks), quote-driven (dealers), brokered (unique assets). Call markets trade at set times; continuous markets trade whenever open.</li>
<li>Efficiency: <b>operational</b> (low costs), <b>informational</b> (prices reflect information), <b>allocational</b> (capital goes to its best use).</li>
<li>Regulation aims to preserve trust, prevent fraud, set minimum standards and ease performance evaluation; it does not eliminate investment risk.</li>
<li>Money markets: maturities of one year or less. Primary markets: new issues, proceeds go to the issuer; secondary markets set prevailing prices.</li>
</ul>""",
qs=[
 ["Compared with forward contracts, futures contracts have:", ["standardized terms.", "less liquidity.", "more counterparty risk."], 0, "Futures are exchange traded, standardized and cleared."],
 ["Which order is behind the market when the best bid is 52.00 and the best ask is 52.20?", ["A limit buy at 51.80", "A limit sell at 52.10", "A market sell order"], 0, "A buy below the best bid is behind the market; market orders never are."],
 ["Shares of a listed company that owns oil fields are best classified as:", ["financial assets.", "real assets.", "physical assets."], 0, "The shares are claims on the company, not physical assets themselves."],
 ["An investor buys 300 shares at $30 with 50% initial margin and sells them at $36. Ignoring interest, dividends and costs, her return is:", ["20%", "40%", "60%"], 1, "Gain of $6 on equity of $15 per share = 40%."],
 ["An investor buys a share at $50 with an initial margin of 40% and a maintenance margin of 25%. He will receive a margin call if the price falls below:", ["$37.50", "$40.00", "$42.50"], 1, "50 × (1 − 0.40)/(1 − 0.25) = 40."],
 ["An investor buys 200 shares at $50 with 50% initial margin and pays 6% interest on the loan. The share pays a $1 dividend and she sells at $55 after one year. Her return on equity is closest to:", ["14%", "18%", "22%"], 1, "Equity 5,000. Proceeds 11,000 − loan 5,000 − interest 300 + dividends 200 = 5,900 → 18%."],
 ["A trader buys shares at $80 with a leverage ratio of 2.5 and sells them at $72. Ignoring costs, his return on equity is:", ["−25%", "−10%", "−4%"], 0, "Price falls 10%; with 2.5× leverage the equity loses 25%."],
 ["An instruction that a limit order is good only for the day is a(n):", ["validity instruction.", "execution instruction.", "clearing instruction."], 0, "Validity instructions state when an order can be filled."],
 ["A fill-or-kill limit buy order includes:", ["execution and validity instructions.", "execution and clearing instructions.", "validity and clearing instructions."], 0, "The limit price is an execution instruction; fill-or-kill is a validity instruction."],
 ["A financial system in which transactions are cheap is:", ["operationally efficient.", "informationally efficient.", "allocationally efficient."], 0, "Operational efficiency refers to low trading costs."],
 ["A market that directs capital to its most productive uses is:", ["allocationally efficient.", "operationally efficient.", "informationally efficient."], 0, "Allocational efficiency depends on prices being informative."],
 ["An investor who has sold a share short and wants to limit losses if the price rises should place a:", ["stop buy order.", "stop sell order.", "limit sell order."], 0, "A stop buy closes the short if the price climbs."],
 ["An investor wants to buy 100 shares at $60 with an initial margin of 40%. The amount she must borrow is:", ["$2,400", "$3,600", "$6,000"], 1, "She pays 40% (2,400) and borrows 60% (3,600)."],
 ["Which statement about call markets is most accurate?", ["Stocks trade only at specific times.", "Trades happen around the clock.", "Dealers set prices continuously."], 0, "All orders are gathered and a single clearing price is set."],
 ["A market for financial assets with maturities of one year or less is a:", ["money market.", "capital market.", "primary market."], 0, "Capital markets trade longer-term instruments."],
 ["Which statement about primary and secondary markets is least accurate?", ["New securities are sold in primary markets.", "Proceeds from secondary market sales go to the issuer.", "Secondary markets set prevailing market prices."], 1, "Secondary trades are between investors."],
 ["After a margin call, the investor must restore the account to the:", ["initial margin.", "maintenance margin.", "variation margin."], 0, "The deposit brings equity back to the initial margin level."],
 ["Which option position is a long position?", ["The buyer of a put", "The writer of a call", "The writer of a put"], 0, "Buyers of options, calls or puts, are long the option."],
 ["A unique painting is most likely to be traded in a(n):", ["brokered market.", "order-driven market.", "quote-driven market."], 0, "Brokers search for a buyer for rare assets."],
 ["An electronic crossing network is best described as a(n):", ["order-driven market.", "quote-driven market.", "brokered market."], 0, "It matches buy and sell orders, usually at prices from other markets."],
 ["Financial intermediaries that issue securities backed by a pool of similar assets are:", ["securitizers.", "arbitrageurs.", "block brokers."], 0, "Securitization pools loans or receivables into tradable securities."],
 ["Which is least likely a feature of a well-functioning market?", ["Timely information on prices and volumes", "Large price changes from one trade to the next", "Prices that adjust quickly to new information"], 1, "Liquid markets have price continuity."],
 ["Which is most likely an objective of market regulation?", ["To preserve trust in financial markets", "To limit investors' downside risk", "To guarantee investment returns"], 0, "Regulation cannot remove investment risk."],
 ["Which statement about short sales is most accurate?", ["The short seller must pay the lender any dividends.", "The short seller may withdraw the sale proceeds.", "The lender must post margin."], 0, "The short seller posts margin and the proceeds stay in the account."],
 ["Compared with a market order to sell, a limit order to sell specifies:", ["a minimum acceptable price.", "a maximum acceptable price.", "immediate execution."], 0, "The seller will not accept less than the limit."],
])

EK["ix"] = dict(
terms=[
 ["Target market (index)", "Hedef piyasa (endeks)", "The market or segment an index is designed to represent; choosing it is the first step in index construction.", "Bir endeksin temsil etmek üzere tasarlandığı piyasa veya bölüm; endeks oluşturmanın ilk adımıdır."],
 ["Style index", "Stil endeksi", "An index of shares with a particular style, such as value or growth.", "Değer veya büyüme gibi belirli bir stile sahip paylardan oluşan endeks."],
 ["Sector index", "Sektör endeksi", "An index of companies in one economic sector.", "Tek bir ekonomik sektördeki şirketlerden oluşan endeks."],
],
notes="""<h3>More on indexes</h3>
<ul>
<li>Steps: choose the <b>target market</b>, then the constituents, then the weighting method; also decide rebalancing and reconstitution.</li>
<li>Price-weighted indexes (Dow Jones Industrial Average, Nikkei 225) must adjust the divisor for <b>stock splits</b>; a split lowers a successful company's weight.</li>
<li>Market-cap weighting acts like a <b>momentum</b> strategy; fundamental weighting (earnings, book value) has a <b>value tilt</b>. Market-cap indexes are usually float-adjusted.</li>
<li>Total return ≥ price return when constituents pay income. A market's performance over a period is best shown by the <b>change in index value</b>.</li>
<li>In CAPM, a broad index is the proxy for the market return. Benchmarks should match the manager's investment approach, such as a style index for a value fund.</li>
<li>Bond indexes are harder: more issues, an unstable universe (maturing bonds), and a lack of continuous trade data, so prices are often estimated.</li>
<li>Commodity indexes are based on <b>futures</b> prices. Hedge fund indexes are usually equal-weighted and biased <b>upward</b> by voluntary reporting.</li>
<li>Adding a share to a popular index tends to raise its price.</li>
</ul>""",
qs=[
 ["Which index weighting most resembles a momentum strategy?", ["Market-capitalization weighting", "Equal weighting", "Fundamental weighting"], 0, "Shares that rise get larger weights automatically."],
 ["Which type of index must adjust for stock splits?", ["Price-weighted", "Equal-weighted", "Market-capitalization-weighted"], 0, "A split changes the share price, so the divisor must be adjusted."],
 ["An index provider removes a company that has been acquired and adds another in its place. This is:", ["reconstitution.", "rebalancing.", "float adjustment."], 0, "Rebalancing changes weights; reconstitution changes membership."],
 ["Which is least likely needed when defining a security market index?", ["The target market", "The weighting method", "The names of investors who will track it"], 2, "The target market, constituents and weighting must be defined."],
 ["In the CAPM, a broad security market index is most likely used as a proxy for the:", ["market return.", "beta.", "risk-free rate."], 0, "The index stands in for the market portfolio."],
 ["A price-weighted index contains three shares priced at $40, $25 and $85. Its value is:", ["40", "50", "75"], 1, "(40 + 25 + 85)/3 = 50."],
 ["A price index and a total return index on the same shares start the year at the same level. At year-end, the total return index will be:", ["higher, if the shares paid dividends.", "lower, if the shares paid dividends.", "the same."], 0, "Total return adds income to price changes."],
 ["Which statement about bond indexes is least accurate?", ["The bond universe is more stable than the stock universe.", "There are more bond issues than share issues.", "Bond prices are often estimated."], 0, "Bonds mature and new ones are issued constantly."],
 ["A value-weighted index starts at 100 with 100 shares of A at $5 and 20 shares of B at $25. A rises to $7 and B falls to $20. The new index value is:", ["100", "110", "120"], 1, "Value rises from 1,000 to 700 + 400 = 1,100, so the index is 110."],
 ["The first step in building a security market index is choosing its:", ["target market.", "constituent securities.", "weighting method."], 0, "The target market determines which securities can be included."],
 ["Commodity indexes are usually based on the prices of:", ["commodity futures contracts.", "physical commodities.", "shares of commodity producers."], 0, "Futures provide observable, tradable prices."],
 ["The most appropriate benchmark for a fund that invests only in growth shares is a:", ["style index.", "sector index.", "broad market index."], 0, "The benchmark should match the manager's investment universe."],
 ["Compared with a market-cap-weighted index, an index weighted by earnings most likely has a:", ["value tilt.", "momentum tilt.", "growth tilt."], 0, "Shares with low prices relative to earnings get larger weights."],
 ["An index's quarterly price returns are 2%, 5%, −3% and 4%. Its price return for the year is closest to:", ["7.7%", "8.0%", "8.4%"], 1, "1.02 × 1.05 × 0.97 × 1.04 − 1 = 8.04%."],
 ["An index of bank shares that covers more than 90% of the sector's market value is best described as a:", ["sector index.", "style index.", "broad market index."], 0, "It covers one economic sector."],
 ["Which index is market-capitalization weighted?", ["MSCI All Country World Index", "Dow Jones Industrial Average", "Nikkei 225"], 0, "The other two are price weighted."],
 ["Which type of equity index is most likely adjusted for free float?", ["Market-capitalization-weighted", "Price-weighted", "Equal-weighted"], 0, "Float adjustment counts only shares available to the public."],
 ["Voluntary reporting by hedge fund managers biases hedge fund index returns:", ["upward.", "downward.", "in neither direction."], 0, "Funds with poor results tend to stop reporting."],
 ["When a share is added to a widely followed index, its price is most likely to:", ["rise.", "fall.", "be unaffected."], 0, "Index funds must buy it."],
 ["Equal weighting is most common in indexes of:", ["hedge funds.", "equities.", "bonds."], 0, "Hedge fund values are not well defined, so funds are weighted equally."],
 ["An index of value shares identified by low price-to-earnings ratios is best described as a:", ["style index.", "fundamental weighted index.", "sector index."], 0, "It groups shares by investment style."],
 ["Creating a bond index is more difficult than creating a stock index mainly because:", ["bonds do not trade continuously.", "bonds are less volatile.", "there are fewer bonds."], 0, "Many bond prices must be estimated."],
])

EK["me"] = dict(
terms=[
 ["Overreaction effect", "Aşırı tepki etkisi", "Shares with poor returns over three to five years tend to outperform those with high returns over the same period.", "Üç-beş yıllık dönemde kötü getiri sağlayan payların, aynı dönemde yüksek getiri sağlayanlardan sonra daha iyi performans göstermesi."],
 ["Information cascade", "Bilgi çağlayanı", "Uninformed traders copying informed traders when information is unclear.", "Bilgi belirsizken bilgisiz yatırımcıların bilgili yatırımcıları taklit etmesi."],
 ["Conservatism", "Muhafazakârlık önyargısı", "Slow adjustment of beliefs to new information.", "İnançların yeni bilgiye yavaş uyarlanması."],
 ["Market value", "Piyasa değeri", "The price at which an asset can currently be bought or sold; observable without estimation.", "Bir varlığın şu anda alınıp satılabileceği fiyat; tahmin gerekmeden gözlemlenebilir."],
],
notes="""<h3>More on market efficiency</h3>
<ul>
<li>Weak form: past prices and volumes; technical analysis cannot earn abnormal returns. Semi-strong: all public information; fundamental analysis cannot either. Strong: public and private information; assumes no group has privileged access to information.</li>
<li>Momentum and overreaction contradict weak-form efficiency; anomalies based on public data (low P/E, earnings surprises) contradict semi-strong efficiency.</li>
<li>Efficiency improves with more participants, more analyst coverage, lower costs and fewer short-sale restrictions.</li>
<li>In efficient markets, portfolio managers still add value by understanding the client, setting risk tolerance, allocating among asset classes, diversifying (unsystematic risk) and minimizing costs.</li>
<li>Prices react only to the <b>unexpected</b> part of news; results in line with forecasts cause little movement.</li>
<li>Behavioural biases do not by themselves make markets inefficient if mispricing cannot be exploited consistently.</li>
<li>Calendar effects: January effect (tax-loss selling in December).</li>
</ul>""",
qs=[
 ["If markets are semi-strong-form efficient, a portfolio manager is least likely to add value by:", ["analysing published financial statements.", "allocating funds among asset classes.", "tailoring portfolios to client needs."], 0, "Public information is already in prices."],
 ["Market efficiency is most likely reduced by:", ["a ban on short selling.", "heavy analyst coverage.", "high trading volumes."], 0, "Restrictions prevent overpricing from being corrected."],
 ["Which form of the EMH assumes that no group of investors has privileged access to relevant information?", ["Strong form", "Weak form", "Semi-strong form"], 0, "If prices reflect private information too, no one can have an information monopoly."],
 ["The overreaction effect refers to shares with:", ["poor returns over three to five years later outperforming.", "high returns continuing to outperform.", "returns reversing within a week."], 0, "Prices overshoot and later reverse."],
 ["A persistent momentum effect would be evidence against:", ["weak-form efficiency, and therefore semi-strong-form efficiency too.", "semi-strong-form efficiency only.", "strong-form efficiency only."], 0, "Past prices would predict future returns; each stronger form includes the weaker one."],
 ["Uninformed traders who copy the actions of informed traders when information is unclear create:", ["an information cascade.", "loss aversion.", "conservatism."], 0, "Information cascades can help prices adjust."],
 ["An investor who is more averse to potential losses than to equal potential gains shows:", ["loss aversion.", "conservatism.", "overconfidence."], 0, "Losses hurt more than equal gains please."],
 ["Which would be inconsistent with an efficient market?", ["Biased price adjustments to news", "Independent price changes", "Rapid adjustment to new information"], 0, "In efficient markets, price adjustments are unbiased."],
 ["In an efficient market, which is least likely a role of the portfolio manager?", ["Diversifying to eliminate systematic risk", "Understanding the client's risk tolerance", "Minimizing transaction costs"], 0, "Diversification removes unsystematic, not systematic, risk."],
 ["The asset value that is observable without estimation is its:", ["market value.", "intrinsic value.", "fundamental value."], 0, "Intrinsic value must be estimated."],
 ["A company reports earnings exactly in line with analysts' forecasts. In an efficient market, its share price will most likely:", ["change little.", "rise sharply.", "fall sharply."], 0, "Only unexpected information moves prices."],
 ["A share is undervalued if its market price is:", ["below its intrinsic value.", "below its book value.", "above its intrinsic value."], 0, "Book value is an accounting measure."],
 ["Which would most likely improve a market's efficiency?", ["More market participants", "Wider bid-ask spreads", "More restrictions on short selling"], 0, "More participants means more analysis and trading on information."],
 ["A firm that believes markets are semi-strong-form efficient will most likely use:", ["passive portfolio management.", "an active strategy based on financial statement analysis.", "an enhanced index strategy based on price patterns."], 0, "Neither technical nor fundamental analysis is expected to add value."],
])

EK["eq"] = dict(
terms=[
 ["Participating preference shares", "Kâra katılan imtiyazlı paylar", "Preference shares that receive extra dividends if profits exceed a set level, in addition to the fixed dividend.", "Sabit temettünün yanı sıra kâr belirli bir düzeyi aşarsa ek temettü alan imtiyazlı paylar."],
 ["Global depository receipt (GDR)", "Küresel depo sertifikası (GDR)", "A depository receipt issued outside the issuer's home country and outside the US, often in US dollars.", "İhraççının ülkesi ve ABD dışında, çoğunlukla dolar cinsinden çıkarılan depo sertifikası."],
 ["American depository receipt (ADR)", "Amerikan depo sertifikası (ADR)", "A US dollar receipt trading in the US that represents shares of a foreign company.", "Yabancı bir şirketin paylarını temsil eden, ABD'de dolar cinsinden işlem gören sertifika."],
 ["Unsponsored depository receipt", "Sponsorsuz depo sertifikası", "A receipt issued without the company's involvement; the depository bank keeps the voting rights.", "Şirketin katılımı olmadan çıkarılan sertifika; oy haklarını depocu banka elinde tutar."],
 ["Basket of listed depository receipts (BLDR)", "Listelenmiş depo sertifikası sepeti", "An exchange-traded fund that holds a portfolio of depository receipts.", "Bir depo sertifikası portföyünü tutan borsa yatırım fonu."],
],
notes="""<h3>More on equity securities</h3>
<ul>
<li>Risk to the investor, from least to most: <b>putable</b>, option-free, <b>callable</b>. Preference shares are riskiest when callable and non-cumulative. Common shares are riskier, and have higher average returns, than preference shares.</li>
<li>Different classes of common shares can have different voting rights, dividends and priority in liquidation.</li>
<li>Book value of equity = assets − liabilities. With no dividends, net income raises book value; the market value need not change.</li>
<li>ROE is usually calculated on <b>average</b> book value, especially when book value is changing.</li>
<li>Equity finances long-term assets, expansion and research; it is least likely used for inventory.</li>
<li>Private equity: illiquid, no quoted prices, less disclosure, a long-term focus. It can be issued by private and public companies (PIPE). Mezzanine financing comes before an IPO in venture capital.</li>
<li>ADR and GDR holders face <b>currency risk</b>; a weaker dollar raises returns for foreign investors in US shares.</li>
<li>The cost of equity is the investors' minimum required return, not a company payment.</li>
</ul>""",
qs=[
 ["Investors typically have the most voting power with:", ["common shares.", "participating preference shares.", "unsponsored depository receipts."], 0, "Preference shares usually have no vote; unsponsored receipts leave votes with the bank."],
 ["Book value of equity equals the company's assets minus its:", ["liabilities.", "retained earnings.", "intangible assets."], 0, "It is the accounting value of the owners' claim."],
 ["A basket of listed depository receipts is best described as a(n):", ["exchange-traded fund of depository receipts.", "index of depository receipts.", "unsponsored receipt."], 0, "BLDRs are ETFs."],
 ["Preference shares are riskiest for the investor when they are:", ["callable and non-cumulative.", "callable and cumulative.", "non-callable and cumulative."], 0, "The issuer can redeem them, and missed dividends are lost."],
 ["Global depository receipts are most likely issued:", ["outside the issuer's home country and outside the US.", "in the US in dollars.", "only in the issuer's home market."], 0, "Receipts issued in the US are ADRs."],
 ["Compared with a listed company, a company owned by private equity is most likely to:", ["disclose less financial information.", "focus more on short-term results.", "have more liquid shares."], 0, "Private companies have fewer reporting obligations."],
 ["The main reason companies issue equity is to:", ["acquire assets to carry out operations.", "increase publicity.", "reduce taxes."], 0, "Equity funds long-term assets and growth."],
 ["Participating preference shares most likely:", ["receive extra dividends when profits are high.", "can be converted into common shares.", "can be sold back to the company."], 0, "The other two are convertible and putable features."],
 ["A US investor holds US shares. US share prices rise while the dollar falls. Which investor in these shares earns the highest return in their own currency?", ["The US investor", "A eurozone investor", "A Japanese investor"], 0, "Foreign investors lose when the dollar weakens against their currency."],
 ["In an industry where book values are rising, return on equity is best calculated using:", ["average book value.", "ending book value.", "beginning book value."], 0, "Average equity matches the income earned over the period."],
 ["For a company that pays no dividends, an increase in net income must increase its:", ["book value of equity.", "market value of equity.", "both book and market value."], 0, "Retained earnings rise; the market value depends on investors."],
 ["Equity is least likely used to finance:", ["inventory.", "research and development.", "new equipment."], 0, "Short-term needs are usually funded with short-term debt."],
 ["Compared with preferred shares, common shares most likely:", ["have higher average returns.", "have less volatile returns.", "pay more frequent dividends."], 0, "Higher risk is rewarded with higher expected returns."],
 ["Ranked from least to most risky for the investor, share types are:", ["putable, option-free, callable.", "callable, option-free, putable.", "option-free, putable, callable."], 0, "The put protects the investor; the call benefits the issuer."],
 ["Two owners of 100 shares in the same company receive 100 and 10 votes in a proxy vote. The most likely reason is that they own:", ["different classes of shares.", "shares bought at different times.", "shares held in different countries."], 0, "Share classes can carry different voting rights."],
 ["Which change would raise a company's return on equity?", ["Net income rises 5% and average equity rises 2%", "Net income falls 5% and average equity falls 3%", "Net income rises 4% and average equity rises 6%"], 0, "ROE rises when income grows faster than equity."],
 ["A company's cost of equity is least accurately described as:", ["a cash payment the company must make.", "the minimum return investors require.", "the expected total return in equilibrium."], 0, "It is an opportunity cost, not a contractual payment."],
 ["A US investor buys ADRs of a Japanese company while a Japanese investor buys its shares in Tokyo. Compared with the Japanese investor, the US investor faces additional:", ["currency risk.", "liquidity risk.", "credit risk."], 0, "The dollar/yen rate affects the US investor's return."],
 ["Which security is riskiest for the investor?", ["Callable common shares", "Putable common shares", "Callable preferred shares"], 0, "Common shares are riskier than preferred, and the call adds risk."],
 ["Private equity securities are issued by:", ["both private and public companies.", "private companies only.", "public companies only."], 0, "Listed companies can sell shares privately, for example in a PIPE."],
 ["A depository receipt for which the depository bank keeps the voting rights is a(n):", ["unsponsored depository receipt.", "sponsored depository receipt.", "global registered share."], 0, "In sponsored receipts, investors usually get the votes."],
])

EK["ca"] = dict(
terms=[
 ["Degree of financial leverage (DFL)", "Finansal kaldıraç derecesi", "The percentage change in net income for a given percentage change in operating income.", "Faaliyet kârındaki belirli bir yüzde değişime karşılık net kârdaki yüzde değişim."],
 ["Front matter", "Rapor özeti (ön bölüm)", "The opening section of a research report with the recommendation, target price and key data.", "Araştırma raporunun öneri, hedef fiyat ve temel verileri içeren giriş bölümü."],
],
notes="""<h3>More on company analysis</h3>
<ul>
<li>An initial research report has a full company description, industry overview and competitive analysis; later reports focus on <b>updates, recommendations and rationale</b>, which appear in both.</li>
<li>Front matter: recommendation, target price, key financial data. Pro forma statements show the forecasts behind the valuation.</li>
<li>Sources: company (filings, press releases, investor relations) and third party (industry reports, competitors, suppliers).</li>
<li>ROE shows returns including the effect of leverage; ROIC excludes it. Debt-to-equity compares capital structures.</li>
<li>EBITDA ≥ EBIT ≥ pre-tax earnings for a company with depreciation and interest expense.</li>
<li>High operating leverage magnifies earnings growth when sales rise. DFL = %ΔNI / %ΔEBIT.</li>
<li>Economies of scale: fixed costs spread over more units, so average cost falls.</li>
<li>Pricing power comes from differentiation and few substitutes; commoditized markets are highly competitive.</li>
<li>Uses of capital: capital expenditure, acquisitions, dividends, buybacks, debt repayment.</li>
</ul>""",
qs=[
 ["Which item is most likely to appear in both an initial and a later research report on a company?", ["Recommendations and their rationale", "A full industry overview", "A detailed history of the company"], 0, "Later reports update the investment view."],
 ["An analyst who wants to measure returns including the effect of financial leverage should use:", ["return on equity.", "return on invested capital.", "operating margin."], 0, "ROIC uses both debt and equity, so it excludes the leverage effect."],
 ["To compare the capital structures of companies in one industry, the most useful ratio is:", ["debt-to-equity.", "inventory turnover.", "current ratio."], 0, "It shows the mix of debt and equity financing."],
 ["A company's operating income rises from $4.0 million to $4.4 million and its net income from $2.0 million to $2.3 million. Its degree of financial leverage is closest to:", ["1.0", "1.5", "2.0"], 1, "%ΔNI = 15%, %ΔEBIT = 10%; 15/10 = 1.5."],
 ["For a company with depreciation and interest expense, which is typically the largest?", ["EBITDA", "EBIT", "Pre-tax earnings"], 0, "EBITDA adds back depreciation and amortization to EBIT."],
 ["A product sells for $30, variable cost is $18 per unit, fixed costs are $40,000 and 5,000 units are sold. Total contribution margin is:", ["$20,000", "$60,000", "$150,000"], 1, "(30 − 18) × 5,000 = 60,000. Fixed costs are deducted afterwards."],
 ["Press releases and information from a company's investor relations department are:", ["company sources.", "third-party sources.", "independent sources."], 0, "They come from the company itself."],
 ["Which company is most likely to have significant pricing power?", ["One whose products have few substitutes", "One in a market with many identical products", "One with high exit costs"], 0, "Customers cannot easily switch."],
 ["During a period of rising sales, compared with companies with low operating leverage, companies with high operating leverage will most likely have:", ["faster earnings growth.", "slower earnings growth.", "the same earnings growth."], 0, "Fixed costs do not rise with sales, so profits grow faster."],
 ["A highly competitive market most likely has:", ["commoditized products.", "high switching costs.", "high barriers to entry."], 0, "Identical products compete on price."],
 ["Analysts include pro forma financial statements in research reports mainly to show:", ["the forecasts behind their valuation.", "historical sales growth.", "regulatory filings."], 0, "Pro forma statements present expected future results."],
 ["A company has revenue of 2,000, cost of sales of 1,100, operating expenses (excluding depreciation) of 400 and depreciation of 100. Its EBITDA is:", ["400", "500", "900"], 1, "2,000 − 1,100 − 400 = 500; EBIT would be 400."],
 ["The percentage change in net income for a given percentage change in operating income is the degree of:", ["financial leverage.", "operating leverage.", "total leverage."], 0, "Operating leverage relates operating income to sales."],
 ["In the uses of capital, an analyst would most likely include:", ["share buybacks and debt repayments.", "new share issues and new borrowing.", "asset sales."], 0, "The others are sources of capital."],
 ["A company experiencing economies of scale as output rises will see:", ["average cost per unit fall.", "total fixed costs fall.", "variable cost per unit rise."], 0, "Fixed costs are spread over more units."],
 ["A firm is most likely to have pricing power if its product is:", ["differentiated.", "a commodity.", "easily copied."], 0, "Differentiation reduces competition on price."],
])

EK["ic"] = dict(
terms=[
 ["Focus strategy", "Odaklanma stratejisi", "Targeting a narrow market segment with either low cost or differentiation.", "Dar bir pazar bölümünü düşük maliyet veya farklılaştırma ile hedefleme."],
 ["Industry base rate", "Sektör baz oranı", "The baseline profitability of an industry, toward which companies tend to converge.", "Şirketlerin zamanla yaklaştığı, sektörün temel kârlılık düzeyi."],
 ["Growth industry", "Büyüme sektörü", "An industry whose sales and profits grow faster than average, regardless of the business cycle.", "Satış ve kârı iş çevriminden bağımsız olarak ortalamadan hızlı büyüyen sektör."],
],
notes="""<h3>More on industry analysis</h3>
<ul>
<li>Commercial classification systems (GICS and others) group companies by <b>principal business activity</b>, usually the source of most revenue. A sector is broader than an industry (transportation sector, airline industry).</li>
<li>Defensive industries (food, beverages, utilities) are stable through the cycle; growth industries grow regardless of the cycle; cyclical industries swing with it.</li>
<li>HHI above 2,500 indicates high concentration: more pricing power, higher profitability, less competition.</li>
<li>Porter's five forces: threat of entry, power of suppliers, power of buyers, threat of substitutes, rivalry among competitors. Competition increases with low barriers, low concentration, unused capacity and commodity products.</li>
<li>Economic profits are most likely with high barriers to entry and low rivalry.</li>
<li>Strategies: cost leadership (price cuts, efficiency; suits slow-changing industries), differentiation (market research, premium prices; overcomes buyer power), focus (a hybrid within a narrow segment).</li>
<li>Steps: define the industry, survey it (size, growth, segments), analyse structure and competition (five forces), analyse external influences (PESTLE), then evaluate the company.</li>
<li>Industry analysis shows pricing power; competitive strategy and financial results are company analysis. Investing in an industry ETF gives industry exposure with little company-specific risk.</li>
</ul>""",
qs=[
 ["After analysing an industry, which element should an analyst examine for a specific company in it?", ["Its competitive strategy", "The industry's five forces", "The industry's size"], 0, "Strategy and financial performance are company-level analysis."],
 ["An investor wants exposure to an industry's risk but little company-specific risk. The most suitable approach is to:", ["buy an ETF covering the industry.", "buy a few small companies in the industry.", "buy the industry leader only."], 0, "A broad holding of the industry diversifies away company risk."],
 ["Industries whose sales and profits grow faster than average regardless of the business cycle are:", ["growth industries.", "defensive industries.", "cyclical industries."], 0, "Defensive industries are stable but not fast growing."],
 ["An industry has a Herfindahl-Hirschman Index of 2,850. It most likely has:", ["greater pricing power.", "greater competitive intensity.", "lower profitability."], 0, "An HHI above 2,500 indicates high concentration."],
 ["An industry has four firms with market shares of 35%, 30%, 25% and 10%. Its HHI is:", ["2,500", "2,850", "3,200"], 1, "35² + 30² + 25² + 10² = 1,225 + 900 + 625 + 100 = 2,850."],
 ["Which competitive strategy best suits industries where products are stable and innovation is slow?", ["Cost leadership", "Differentiation", "Focus"], 0, "Efficiency is the main source of advantage when products do not change."],
 ["A company earns 65% of its revenue from one business line and 35% from another. A commercial classification system will most likely classify it by:", ["the line providing most of its revenue.", "both lines equally.", "the faster-growing line."], 0, "Principal business activity determines the classification."],
 ["In the industry and competitive analysis process, assessing barriers to entry and supplier power is part of:", ["analysing industry structure and competition.", "surveying the industry.", "defining the industry."], 0, "This is where Porter's five forces are applied."],
 ["Which of the following best describes transportation and airlines?", ["Transportation is the sector; airlines are the industry.", "Airlines are the sector; transportation is the industry.", "Both are industries."], 0, "A sector is a broader grouping than an industry."],
 ["Which barrier to entry would increase competition among companies in an industry?", ["Low capital requirements", "Strong customer loyalty", "Significant economies of scale"], 0, "Low barriers allow new competitors in."],
 ["A company following a differentiation strategy is most likely to emphasize:", ["market research.", "operating efficiency.", "price cuts."], 0, "It must understand what customers value."],
 ["The threat of substitutes is most likely to be low for a company that:", ["sells a product with few alternatives that customers value.", "sells a commodity.", "faces many similar products."], 0, "Customers have nowhere else to turn."],
 ["Industry analysis is most likely to give an analyst insight into a company's:", ["pricing power.", "competitive strategy.", "financial performance."], 0, "The industry's structure determines how much pricing power firms have."],
 ["Aggressive price cuts to gain market share are most associated with a:", ["cost leadership strategy.", "product differentiation strategy.", "service differentiation strategy."], 0, "Low costs allow low prices."],
 ["Economic profits are most likely in an industry with:", ["high barriers to entry and low rivalry.", "low barriers and high rivalry.", "many substitutes."], 0, "Profits are protected from new and existing competitors."],
 ["Food, beverage and utility companies are examples of:", ["defensive industries.", "cyclical industries.", "growth industries."], 0, "Demand for necessities is stable."],
 ["The bargaining power of customers is best overcome by a:", ["differentiation strategy.", "cost leadership strategy.", "commodity strategy."], 0, "Unique products give customers fewer alternatives."],
 ["Competition in an industry is most likely increased by:", ["low barriers, low concentration and high unused capacity.", "high barriers, high concentration and low unused capacity.", "low barriers, high concentration and low unused capacity."], 0, "All three push firms to compete on price."],
 ["In industry analysis, the industry base rate is the:", ["baseline profitability of the industry.", "average market share of its companies.", "minimum number of companies in it."], 0, "Companies' profitability tends to converge toward it."],
 ["Which is most likely assessed when surveying an industry?", ["Its growth rate and size", "Its five forces", "Its PESTLE factors"], 0, "The survey describes size, growth and segments."],
])

EK["cf"] = dict(
terms=[
 ["Top-down forecast", "Yukarıdan aşağı tahmin", "A forecast starting from macroeconomic or industry data, such as GDP growth and market share.", "GSYH büyümesi ve pazar payı gibi makro veya sektör verilerinden başlayan tahmin."],
 ["Bottom-up forecast", "Aşağıdan yukarı tahmin", "A forecast built from company-level drivers, such as prices and volumes or sales per store.", "Fiyat ve hacim veya mağaza başına satış gibi şirket düzeyindeki etkenlerden kurulan tahmin."],
 ["Historical base rate convergence", "Tarihsel baz orana yakınsama", "Forecasting that a company's growth or profitability will move toward the industry or economy average.", "Bir şirketin büyümesinin veya kârlılığının sektör ya da ekonomi ortalamasına yaklaşacağını öngören tahmin."],
],
notes="""<h3>More on forecasting</h3>
<ul>
<li>Top-down: GDP growth, industry growth and market share. Bottom-up: prices × volumes, store counts, capacity.</li>
<li>Cost of goods sold and selling expenses follow revenue; administrative expenses are mostly fixed and grow with <b>inflation</b>.</li>
<li>Maintenance capex grows with inflation (start from historical depreciation); growth capex follows the company's growth.</li>
<li>Working capital items are forecast from turnover ratios: receivables = revenue × DSO / 365.</li>
<li>Exclude non-recurring items, such as remeasurement gains, from revenue forecasts.</li>
<li>Management tends to guide revenue low and costs high, so analysts lean the other way.</li>
<li>Historical results are a good base for mature, stable companies, not for young or restructuring ones.</li>
<li>Scenario analysis accounts for changes in the economic environment. Summary measures can be forecast when detail is not needed.</li>
</ul>""",
qs=[
 ["A company has days sales outstanding of 36 and revenue of $25 million, expected to grow 6%. Receivables on the pro forma balance sheet are closest to:", ["$2.47 million", "$2.61 million", "$2.75 million"], 1, "26.5 × 36/365 = 2.61."],
 ["To forecast a company's capital structure mix, an analyst is most likely to use the:", ["debt-to-equity ratio.", "current ratio.", "inventory turnover."], 0, "It measures the mix of debt and equity."],
 ["In forecasting next year's revenue, an analyst is most likely to exclude:", ["a one-off gain on remeasuring a subsidiary.", "price increases on main products.", "sales from new stores."], 0, "Non-recurring items do not represent ongoing revenue."],
 ["A top-down revenue forecast is most likely based on expected:", ["GDP growth.", "sales at existing and new stores.", "prices and volumes of each product."], 0, "The other two are bottom-up approaches."],
 ["A company is expected to grow 6% and inflation is forecast at 2%. Maintenance capital expenditure will most likely be forecast to grow at:", ["2%", "6%", "8%"], 0, "Maintenance spending keeps pace with inflation; growth capex follows the 6%."],
 ["To forecast maintenance capital expenditure, an analyst often starts from the company's:", ["historical depreciation.", "prior asset sales.", "dividend history."], 0, "Depreciation approximates the cost of replacing worn assets."],
 ["Revenue this year is $40 million. Nominal GDP is expected to grow 4%, and the company to grow 25% faster than GDP. Next year's revenue is closest to:", ["$41.6 million", "$42.0 million", "$50.0 million"], 1, "Growth = 4% × 1.25 = 5%; 40 × 1.05 = 42."],
 ["Baseline revenue is $8 million and is expected to grow 4%. With a forecast gross margin of 60%, forecast cost of goods sold is closest to:", ["$3.20 million", "$3.33 million", "$4.99 million"], 1, "Revenue 8.32 × (1 − 0.60) = 3.33."],
 ["An analyst forecasts revenue from expected selling prices and volumes of each product. This is a:", ["bottom-up approach.", "top-down approach.", "hybrid based on GDP."], 0, "It builds revenue from company-level drivers."],
 ["A benefit of scenario analysis in forecasting is that it:", ["reflects possible changes in the economic environment.", "removes the need for assumptions.", "gives a single precise forecast."], 0, "It shows outcomes under different conditions."],
 ["A company's market share is 8% and its sales are $24 million. Industry sales are expected to grow 5% and its share to rise to 9%. Expected sales are closest to:", ["$25.2 million", "$27.0 million", "$28.4 million"], 2, "Industry sales 300 × 1.05 = 315; 9% of 315 = 28.35."],
 ["A constant growth rate linked to inflation is most suitable for forecasting:", ["administrative expenses.", "cost of goods sold.", "selling expenses."], 0, "Administrative costs are mostly fixed; the others vary with sales."],
 ["Management guides both revenue and operating expense growth at 4%–6%. Given management's usual tendency, an analyst is most likely to forecast:", ["revenue near 6% and expenses near 4%.", "revenue near 4% and expenses near 6%.", "both at 5%."], 0, "Managers tend to guide conservatively so they can beat expectations."],
 ["Using historical results as the base for next year's forecast is most appropriate for a:", ["mature company with stable operations.", "start-up.", "company in the middle of a restructuring."], 0, "Past results are a good guide only when the business is stable."],
 ["An analyst uses historical base rate convergence for a company in a mature industry. She is most likely to forecast growth close to:", ["the industry's median growth rate.", "the company's best year.", "zero."], 0, "Growth is expected to move toward the industry or economy average."],
])

EK["ev"] = dict(
terms=[
 ["Sustainable growth rate", "Sürdürülebilir büyüme oranı", "g = retention ratio × ROE: the growth a company can fund from retained earnings.", "g = kâr alıkoyma oranı × özsermaye kârlılığı; şirketin dağıtmadığı kârla finanse edebileceği büyüme."],
 ["Holder-of-record date", "Hak sahibi tespit tarihi", "The date on which shareholders must be registered to receive a dividend.", "Temettü almak için pay sahibinin kayıtlı olması gereken tarih."],
 ["Special dividend", "Özel temettü", "A one-off cash dividend, often paid by cyclical companies in good years.", "Döngüsel şirketlerin çoğunlukla iyi yıllarda ödediği tek seferlik nakit temettü."],
 ["Stock dividend", "Bedelsiz pay", "A payment to shareholders in new shares instead of cash.", "Pay sahiplerine nakit yerine yeni pay olarak yapılan dağıtım."],
],
notes="""<h3>More on valuation</h3>
<p class="f">V<sub>0</sub> = D<sub>1</sub> / (k − g) · g = b × ROE · ROE = margin × turnover × leverage</p>
<p class="f">justified P<sub>0</sub>/E<sub>1</sub> = (D<sub>1</sub>/E<sub>1</sub>) / (k − g) · preferred share V = D / k<sub>p</sub></p>
<ul>
<li>The required return can be estimated with CAPM: k = R<sub>f</sub> + β(R<sub>m</sub> − R<sub>f</sub>). A higher beta raises k and lowers value.</li>
<li>The justified P/E rises with the payout ratio (g constant) and with g; it falls as k rises. With zero retention, P/E = 1/k.</li>
<li>Raising the payout lowers g ('dividend displacement of earnings'), so the net effect on value is uncertain.</li>
<li>Constant-growth DDM suits stable, mature dividend payers. Multistage models handle supernormal growth.</li>
<li>Enterprise value = market value of equity + debt + preferred − cash and short-term investments. EV multiples use operating measures (EBITDA, EBIT).</li>
<li>P/B suits firms with mostly liquid assets (banks); it works when earnings are negative. P/S works for loss-making firms; P/CF is harder to manipulate.</li>
<li>Asset-based models suit companies being liquidated, holding mostly liquid assets, or natural resource firms; they set a floor value.</li>
<li>Dividend chronology: declaration, ex-dividend, holder-of-record, payment. Buyers before the ex-dividend date receive the dividend. Stock splits and stock dividends do not change shareholder wealth.</li>
</ul>""",
qs=[
 ["A share has a required return of 13%, a constant growth rate of 8% and a payout ratio of 40%. Its justified P/E (P0/E1) is:", ["3.1", "8.0", "12.5"], 1, "0.40/(0.13 − 0.08) = 8.0."],
 ["A company's ROE is 18% and its payout ratio is 35%. Its sustainable growth rate is closest to:", ["6.3%", "11.7%", "18.0%"], 1, "0.65 × 18% = 11.7%."],
 ["Other things equal, which would most likely lower a company's P/E ratio?", ["A higher required return", "A higher growth rate", "A higher payout ratio with growth unchanged"], 0, "The required return is in the denominator."],
 ["A company has just paid a dividend of $2.40, which is expected to grow 5% a year. The required return is 12%. The share's value is:", ["$34.29", "$36.00", "$50.40"], 1, "2.40 × 1.05 / (0.12 − 0.05) = 36.00."],
 ["The effect on firm value of increasing the dividend payout ratio is:", ["uncertain.", "always positive.", "always negative."], 0, "Higher dividends now may be offset by lower future growth."],
 ["Other things equal, if a share's beta rises, its price will:", ["fall.", "rise.", "not change."], 0, "Higher beta raises the required return."],
 ["A preferred share with a $75 par value pays an 8% dividend. Similar shares yield 7.5%. Its value is closest to:", ["$75.00", "$80.00", "$85.00"], 1, "Dividend 6.00 / 0.075 = 80.00."],
 ["The free cash flow to equity model is best described as a(n):", ["present value model.", "enterprise value model.", "multiplier model."], 0, "It discounts expected cash flows to shareholders."],
 ["Asset-based valuation is most appropriate for a company that:", ["is being liquidated.", "has significant intangible assets.", "has cyclical earnings."], 0, "Asset values matter most when the business will not continue."],
 ["The risk-free rate is 4%, the market return is 10% and a share's beta is 1.3. The last dividend was $1.80 and dividends grow 5% a year. The share's value is closest to:", ["$24.23", "$27.79", "$32.14"], 1, "k = 4% + 1.3 × 6% = 11.8%; 1.89 / 0.068 = 27.79."],
 ["A company's growth rate in dividends and earnings can be estimated as the:", ["product of the retention ratio and ROE.", "product of the payout ratio and ROE.", "sum of ROE and the payout ratio."], 0, "g = b × ROE."],
 ["An advantage of the price-to-book ratio is that it:", ["can be used when earnings are negative.", "is unaffected by accounting choices.", "suits service firms with few assets."], 0, "Book value is usually positive even when earnings are not."],
 ["A company last paid a dividend of $1.00. Dividends will grow 20% for two years and then 5% a year. The required return is 11%. The share's value is closest to:", ["$17.50", "$22.70", "$25.20"], 1, "D1 = 1.20, D2 = 1.44, P2 = 1.512/0.06 = 25.20. Value = 1.20/1.11 + (1.44 + 25.20)/1.11² = 22.70."],
 ["An enterprise value multiple is typically calculated using a measure of:", ["operating income.", "net income.", "dividends."], 0, "EV belongs to all capital providers, so it is matched with pre-interest earnings."],
 ["A payment to shareholders in additional shares instead of cash is a:", ["stock dividend.", "special dividend.", "share repurchase."], 0, "It increases the number of shares without changing wealth."],
 ["The correct order of dividend dates is:", ["declaration, ex-dividend, holder-of-record, payment.", "declaration, holder-of-record, ex-dividend, payment.", "ex-dividend, declaration, payment, holder-of-record."], 0, "The ex-date comes before the record date because of settlement time."],
 ["A high dividend growth rate is most consistent with a:", ["high ROE.", "high payout ratio.", "low retention ratio."], 0, "g = retention × ROE."],
 ["A cyclical company in a very good year is most likely to declare a:", ["special dividend.", "higher regular dividend.", "stock dividend."], 0, "A one-off payment avoids committing to a higher regular level."],
 ["The constant-growth DDM is most appropriate for valuing a:", ["mature company with a stable dividend policy.", "start-up that retains all earnings.", "company with temporary very high growth."], 0, "The model assumes growth is constant and below k."],
 ["A share trades at $40, its expected dividend is $1.60 and its sustainable growth rate is 6%. The market's required return is:", ["4.0%", "6.0%", "10.0%"], 2, "k = D1/P0 + g = 4% + 6%."],
 ["A company has an equity market value of 300, debt of 120 and cash of 20. Its EBITDA is 50. Its EV/EBITDA is:", ["6.0", "8.0", "8.4"], 1, "EV = 300 + 120 − 20 = 400; 400/50 = 8.0."],
 ["A company's profit margin is 8%, asset turnover 1.5, equity multiplier 2.0 and retention ratio 0.6. Its sustainable growth rate is:", ["7.2%", "14.4%", "24.0%"], 1, "ROE = 8% × 1.5 × 2.0 = 24%; g = 0.6 × 24% = 14.4%."],
 ["If a company retains none of its earnings, its P/E ratio equals:", ["1/k.", "k + g.", "D/P + g."], 0, "With g = 0 and payout 100%, P/E = 1/k."],
 ["A company will pay its first dividend of $1.50 in three years' time; dividends then grow 5% a year. The required return is 12%. The share's value today is closest to:", ["$15.25", "$17.08", "$21.43"], 1, "P2 = 1.50/0.07 = 21.43; discounted two years at 12% = 17.08."],
 ["An investor buys a share on its ex-dividend date. She will:", ["not receive the declared dividend.", "receive the declared dividend.", "receive half the dividend."], 0, "The seller keeps it."],
 ["Other things equal, a stock split's effect on shareholder wealth is to:", ["leave it unchanged.", "increase it.", "decrease it."], 0, "Each share is worth proportionally less."],
 ["Which is not an assumption of the constant-growth DDM?", ["Dividends grow at a constant rate", "The required return exceeds the growth rate", "The share price grows faster than dividends"], 2, "In the model, the price grows at the same rate as dividends."],
 ["A preferred share pays $6 a year forever and similar securities yield 9%. Its value is closest to:", ["$54.00", "$66.67", "$75.00"], 1, "6 / 0.09 = 66.67."],
 ["Other things equal, an increase in a company's ROE will cause its constant-growth DDM value to:", ["rise.", "fall.", "stay the same."], 0, "Higher ROE raises g."],
 ["An analyst's estimate of intrinsic value is below the market price. If she is confident in her estimate, she will most likely:", ["sell or avoid the share.", "buy the share.", "take no position."], 0, "The share appears overvalued."],
])
