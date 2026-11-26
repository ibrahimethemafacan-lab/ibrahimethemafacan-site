# CFA Level I · Portfolio Management · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
import re as _re
EK = {}

EK["r1"] = dict(
notes="""<h3>More on risk, return and the efficient frontier</h3>
<p class="f">σ<sub>p</sub>² = w<sub>1</sub>²σ<sub>1</sub>² + w<sub>2</sub>²σ<sub>2</sub>² + 2w<sub>1</sub>w<sub>2</sub>Cov<sub>1,2</sub></p>
<ul>
<li>With perfect positive correlation, portfolio standard deviation is the weighted average of the two; any correlation below +1 gives diversification benefits. Lower correlation moves the efficient frontier up and to the left.</li>
<li>Historically, small-cap equities have had the highest returns and volatility and T-bills the lowest; average returns and standard deviations have been <b>positively</b> related across asset classes.</li>
<li>A portfolio is below the efficient frontier (inefficient) if another has a higher return for the same or lower risk.</li>
<li>In Markowitz's framework risk is the <b>variance</b> of returns; inputs are expected returns, variances and covariances, not risk aversion or beta.</li>
<li>The optimal portfolio is where the investor's highest indifference curve is tangent to the efficient frontier (or the CAL). More risk-averse investors have steeper indifference curves.</li>
<li>Risk-averse investors may still choose a riskier asset if its expected return is high enough; between two assets with equal returns they choose the less risky one.</li>
<li>Adding an asset lowers portfolio risk if its correlation with the portfolio is below the ratio of the portfolio's standard deviation to the asset's.</li>
</ul>""",
qs=[
 ["A portfolio has 20% in an asset with a standard deviation of 25% and 80% in one with 10%. Their correlation is 0.3. The portfolio variance is closest to:", ["0.0089", "0.0113", "0.0144"], 1, "0.0025 + 0.0064 + 2 × 0.2 × 0.8 × 0.25 × 0.1 × 0.3 = 0.0113."],
 ["Two assets with standard deviations of 18% and 12% have a covariance of 0.0108. Their correlation is:", ["0.25", "0.50", "0.75"], 1, "0.0108 / (0.18 × 0.12)."],
 ["Two assets are perfectly positively correlated. A portfolio holds 30% in one with a standard deviation of 25% and 70% in one with 15%. Its standard deviation is:", ["15.0%", "18.0%", "20.0%"], 1, "Weighted average: 0.3 × 25 + 0.7 × 15."],
 ["A portfolio holds 25% in asset A (variance 0.0081) and 75% in asset B (variance 0.0225), with a covariance of 0.0045. Its standard deviation is closest to:", ["10.1%", "12.2%", "13.4%"], 1, "Variance = 0.000506 + 0.012656 + 0.001688 = 0.01485; √ = 12.2%."],
 ["Reducing the correlation between the two assets in a portfolio moves the efficient frontier:", ["up and to the left.", "down and to the right.", "straight down."], 0, "Lower risk for each level of return."],
 ["The portfolio on the efficient frontier that best suits an investor is determined by the:", ["investor's indifference curves.", "global minimum-variance portfolio.", "market portfolio only."], 0, "Utility determines the chosen point."],
 ["In the Markowitz framework, risk is defined as the:", ["variance of returns.", "probability of a loss.", "beta of the investment."], 0, "Beta belongs to the CAPM."],
 ["Which input is least likely required to construct the Markowitz efficient frontier?", ["Investors' risk aversion", "Expected returns", "Covariances of returns"], 0, "Risk aversion selects a point on the frontier but does not shape it."],
 ["Diversification provides benefits as long as the correlation between assets is:", ["less than +1.", "negative.", "zero."], 0, "Even modest positive correlation reduces risk."],
 ["Historically, which asset class has shown the smallest standard deviation of returns?", ["Treasury bills", "Long-term government bonds", "Large-cap equities"], 0, "Short maturities give stable returns."],
 ["Over long periods, the average returns and standard deviations of major asset classes have shown a:", ["positive relationship.", "negative relationship.", "no relationship."], 0, "Higher risk has been rewarded with higher returns."],
 ["Portfolio X has an expected return of 9% and a standard deviation of 14%. Portfolio Y has 10% and 12%. Which statement is correct?", ["X is below the efficient frontier.", "Y is below the efficient frontier.", "Both could be efficient."], 0, "Y offers more return for less risk."],
 ["Compared with a less risk-averse investor, a more risk-averse investor has indifference curves that are:", ["steeper.", "flatter.", "the same."], 0, "She demands more return for each unit of extra risk."],
 ["Risk aversion means that an investor will choose the less risky of two assets:", ["if they have the same expected return.", "even if it has a lower return.", "only if its return is higher."], 0, "Risk-averse investors can still take risk if paid for it."],
 ["Calculating the variance of a two-asset portfolio least likely requires each asset's:", ["beta.", "weight.", "standard deviation."], 0, "The covariance or correlation is also needed."],
])

EK["r2"] = dict(
notes="""<h3>More on capital market theory</h3>
<p class="f">E(R<sub>i</sub>) = R<sub>f</sub> + β<sub>i</sub>[E(R<sub>m</sub>) − R<sub>f</sub>] · β = Cov<sub>i,m</sub> / σ<sub>m</sub>² = ρσ<sub>i</sub>/σ<sub>m</sub></p>
<p class="f">Sharpe = (R<sub>p</sub> − R<sub>f</sub>)/σ<sub>p</sub> · Treynor = (R<sub>p</sub> − R<sub>f</sub>)/β · α = R<sub>p</sub> − [R<sub>f</sub> + β(R<sub>m</sub> − R<sub>f</sub>)] · M² = Sharpe × σ<sub>m</sub> + R<sub>f</sub> − R<sub>m</sub></p>
<ul>
<li>The CML plots combinations of the risk-free asset and the market portfolio, with standard deviation as the risk measure; its intercept is R<sub>f</sub> and its slope is the market's Sharpe ratio. Points to the right of the market portfolio require borrowing at R<sub>f</sub>.</li>
<li>The SML plots expected return against <b>beta</b>. In equilibrium, all assets plot on the SML; only efficient portfolios plot on the CML. Stocks above the SML are undervalued; below, overvalued.</li>
<li>Only systematic risk is priced; unsystematic risk can be diversified away. Total risk = systematic + unsystematic.</li>
<li>CAPM assumptions include: risk-averse, utility-maximizing investors with homogeneous expectations; a single period; no taxes or transaction costs; unlimited lending and borrowing at R<sub>f</sub>; infinitely divisible assets.</li>
<li>The market model is a single-factor model; Fama-French adds size and value factors; Carhart adds momentum.</li>
<li>The correlation of the risk-free asset with any risky portfolio is zero.</li>
<li>M² ranks portfolios the same way as the Sharpe ratio but in percentage terms.</li>
</ul>""",
qs=[
 ["The risk-free rate is 4%, the market risk premium is 7% and a share's beta is 1.3. Its required return is:", ["9.1%", "11.0%", "13.1%"], 2, "4% + 1.3 × 7%."],
 ["A share's expected return is 18%, the risk-free rate is 4% and the expected market return is 12%. Its beta is:", ["1.17", "1.50", "1.75"], 2, "(18 − 4)/(12 − 4)."],
 ["A share's covariance with the market is 0.0096 and the market's standard deviation is 16%. Its beta is:", ["0.375", "0.600", "1.667"], 0, "0.0096 / 0.0256."],
 ["A share has a correlation of 0.6 with the market and a standard deviation of 30%. The market's standard deviation is 20%. Its beta is:", ["0.60", "0.90", "1.50"], 1, "0.6 × 30/20."],
 ["A portfolio returned 14% with a standard deviation of 16% and a beta of 1.25. The risk-free rate is 4% and the market returned 10%. Its Sharpe ratio is:", ["0.50", "0.625", "0.80"], 1, "(14 − 4)/16."],
 ["For the portfolio above, the Treynor measure is:", ["6.0%", "8.0%", "10.0%"], 1, "(14 − 4)/1.25."],
 ["For the portfolio above, Jensen's alpha is:", ["1.5%", "2.5%", "4.0%"], 1, "14 − [4 + 1.25 × 6] = 2.5%."],
 ["For the portfolio above, with a market standard deviation of 20%, M² is:", ["4.0%", "6.5%", "8.5%"], 1, "0.625 × 20 + 4 − 10 = 6.5%."],
 ["A share costs $28, is expected to be worth $32 in a year and to pay a $0.80 dividend. Its beta is 1.2, the risk-free rate is 4% and the market return 10%. The share is:", ["undervalued, because its expected return exceeds its required return.", "overvalued.", "fairly valued."], 0, "Expected 17.1% versus required 11.2%."],
 ["The risk measure associated with the capital market line is:", ["standard deviation.", "beta.", "covariance."], 0, "The SML uses beta."],
 ["According to the CAPM, which risk is rewarded with higher expected returns?", ["Systematic risk", "Unsystematic risk", "Total risk"], 0, "Unsystematic risk can be diversified away."],
 ["A stock that plots below the security market line is most likely:", ["overvalued.", "undervalued.", "fairly valued."], 0, "Its expected return is too low for its beta."],
 ["A portfolio to the right of the market portfolio on the CML is created by:", ["borrowing at the risk-free rate to buy more of the market portfolio.", "lending at the risk-free rate.", "holding only the risk-free asset."], 0, "Leverage raises both risk and expected return."],
 ["In equilibrium, an inefficient portfolio will plot:", ["below the CML and on the SML.", "on the CML and below the SML.", "above both lines."], 0, "All assets plot on the SML; only efficient portfolios on the CML."],
 ["The correlation of returns on the risk-free asset with returns on a portfolio of risky assets is:", ["zero.", "positive.", "negative."], 0, "The risk-free return does not vary."],
 ["The slope of the capital market line measures:", ["excess return per unit of total risk.", "excess return per unit of beta.", "the risk-free rate."], 0, "It is the market's Sharpe ratio."],
 ["Which is not an assumption of capital market theory?", ["Investors can borrow but not lend at the risk-free rate", "There are no taxes or transaction costs", "Investors have homogeneous expectations"], 0, "Investors can both lend and borrow at the risk-free rate."],
 ["Beta is least accurately described as a:", ["standardized measure of a security's total risk.", "measure of systematic risk.", "covariance with the market divided by market variance."], 0, "Beta measures only systematic risk."],
 ["The additional factor that Carhart added to the Fama-French three-factor model is:", ["momentum.", "liquidity.", "profitability."], 0, "Past winners tend to keep outperforming in the short term."],
 ["An active manager will most likely short a security whose expected Jensen's alpha is:", ["negative.", "positive.", "zero."], 0, "It is expected to underperform its required return."],
 ["The market model is best described as a(n):", ["single-factor model.", "two-factor model.", "multifactor model."], 0, "The only factor is the market return."],
 ["An investor with half her wealth in a company she founded is most exposed to:", ["unsystematic risk.", "systematic risk only.", "interest rate risk."], 0, "Her holding is highly concentrated."],
 ["A portfolio holds half in the risk-free asset and half in a risky portfolio with a standard deviation of 18%. Its standard deviation is:", ["9%", "12%", "18%"], 0, "The risk-free asset adds no risk and has zero correlation."],
])

EK["ov"] = dict(
notes="""<h3>More on the portfolio management process and investors</h3>
<ul>
<li>Steps: <b>planning</b> (understand the client, IPS, capital market expectations, benchmark), <b>execution</b> (asset allocation, security analysis, portfolio construction; top-down or bottom-up), <b>feedback</b> (monitoring, rebalancing, performance measurement).</li>
<li>The portfolio approach evaluates each investment by its effect on the portfolio's risk and return. Diversification ratio = portfolio standard deviation / average standard deviation of its holdings.</li>
<li>Investor needs: endowments and foundations have long horizons, high risk tolerance and low liquidity needs. Property and casualty insurers have short horizons and high liquidity needs; life insurers longer horizons. Banks have short horizons and high liquidity needs.</li>
<li>Defined benefit: the employer promises payments and bears investment risk. Defined contribution: the employee bears the risk.</li>
<li>ETFs and open-end funds trade close to NAV; closed-end funds can trade at a premium or discount. Money market funds keep a NAV of 1.00. Buyout funds take companies private and replace management.</li>
<li>Passive management has been gaining market share from active management.</li>
</ul>""",
qs=[
 ["Which pooled investment is least likely to trade at a price different from its NAV?", ["An open-end mutual fund", "A closed-end fund", "An investment trust listed on an exchange"], 0, "Open-end funds issue and redeem shares at NAV."],
 ["Promised payments to beneficiaries are the plan sponsor's responsibility in:", ["a defined benefit plan only.", "a defined contribution plan only.", "both types of plan."], 0, "DC plans promise only contributions."],
 ["In a defined contribution plan, investment risk is borne by the:", ["employee.", "employer.", "fund manager."], 0, "Retirement income depends on investment results."],
 ["The execution step of the portfolio management process most likely includes:", ["asset allocation and security analysis.", "writing the IPS.", "performance measurement."], 0, "The IPS is planning; measurement is feedback."],
 ["Identifying a benchmark for a client portfolio is part of the:", ["planning step.", "execution step.", "feedback step."], 0, "It is set in the IPS."],
 ["Which investor is likely to have the shortest investment horizon?", ["A property and casualty insurer", "A foundation", "A life insurer"], 0, "Claims must be paid at short notice."],
 ["High risk tolerance, a long horizon and low liquidity needs most likely describe a(n):", ["endowment.", "bank.", "property and casualty insurer."], 0, "Endowments are intended to last indefinitely."],
 ["The portfolio approach to investing evaluates each investment based on its:", ["contribution to the portfolio's risk and return.", "stand-alone risk.", "past return."], 0, "Correlations matter."],
 ["The ratio of an equally weighted portfolio's standard deviation to the average standard deviation of its holdings is the:", ["diversification ratio.", "Sharpe ratio.", "information ratio."], 0, "Lower values show more diversification benefit."],
 ["A fund buys all the shares of a listed company, takes it private and replaces management. It is most likely a:", ["buyout fund.", "venture capital fund.", "hedge fund."], 0, "Buyouts acquire mature companies."],
 ["A mutual fund that holds short-term debt and keeps a NAV of 1.00 per share is a:", ["money market fund.", "bond index fund.", "closed-end fund."], 0, "It aims for a stable value."],
 ["Which statement about active and passive management is most accurate?", ["Passive management has been gaining market share.", "Active management fees have been rising.", "Passive funds charge higher fees."], 0, "Low costs have attracted investors to index funds."],
 ["Which is typically the first step in the portfolio management process?", ["Understanding the client's needs and preparing an IPS", "Selecting securities", "Rebalancing"], 0, "Planning comes first."],
 ["A pooled investment whose share price differs significantly from its NAV is most likely a(n):", ["closed-end fund.", "open-end fund.", "exchange-traded fund."], 0, "ETFs use arbitrage to stay close to NAV."],
])

EK["pl"] = dict(
notes="""<h3>More on portfolio planning</h3>
<ul>
<li>IPS components: introduction, statement of purpose, duties and responsibilities, procedures, investment objectives (return and risk), constraints, guidelines, evaluation and review, appendices (strategic asset allocation, rebalancing policy). The manager's compensation is not a standard component.</li>
<li>Constraints: <b>liquidity, time horizon, tax, legal and regulatory, unique circumstances</b>. Required minimum payouts of endowments are liquidity needs, often also legal constraints.</li>
<li>Risk tolerance = ability (wealth, horizon, income stability, dependants) and willingness (attitude). If they conflict, the advisor generally follows the <b>lower</b> one and may educate the client.</li>
<li>Return objectives can be absolute or relative (to a benchmark).</li>
<li>Asset classes for strategic allocation should have <b>low correlations between classes</b> and high correlations within each class, be mutually exclusive and cover the investable universe.</li>
<li>Tactical asset allocation departs temporarily from the strategic weights to exploit short-term views. Core-satellite: a passive core plus active satellites.</li>
<li>ESG integration can be done through exclusionary screening, positive screening, thematic investing, engagement and impact investing.</li>
</ul>""",
qs=[
 ["A manager who believes equities are overvalued in the short term cuts their weight below the strategic target. This is:", ["tactical asset allocation.", "strategic asset allocation.", "rebalancing."], 0, "It is a temporary deviation based on a market view."],
 ["Which is least likely a category of constraint in an IPS?", ["Return objective", "Liquidity needs", "Tax considerations"], 0, "Return is an objective, not a constraint."],
 ["Which factor is least likely to affect an investor's ability to take risk?", ["Years of investing experience", "Family situation", "Size of wealth"], 0, "Experience relates more to willingness and knowledge."],
 ["If an investor's ability to take risk is low but her willingness is high, the advisor should most appropriately:", ["follow the lower ability to take risk.", "follow the higher willingness.", "average the two."], 0, "The constraint on ability cannot be changed by attitude."],
 ["An endowment must by law pay out a minimum percentage of its assets each year. This is best classified as a:", ["liquidity and legal constraint.", "return objective only.", "unique circumstance only."], 0, "It requires cash and is imposed by law."],
 ["A firm invests most of a portfolio to track an index and uses active strategies for the rest. This is a:", ["core-satellite approach.", "tactical allocation.", "fully active approach."], 0, "The index part is the core."],
 ["Asset classes defined for strategic asset allocation should have correlations that are:", ["low between classes and high within each class.", "high between classes.", "high both between and within classes."], 0, "This makes diversification meaningful."],
 ["A return objective stated as 'beat the MSCI World Index by 1% a year' is:", ["a relative return objective.", "an absolute return objective.", "a constraint."], 0, "It is measured against a benchmark."],
 ["The major components of a typical IPS least likely include the:", ["investment manager's compensation.", "investment objectives.", "constraints."], 0, "Fees are set in the management agreement."],
 ["An investor requires her portfolio to produce a minimum amount of cash each year. This is a:", ["liquidity constraint.", "tax constraint.", "time horizon constraint."], 0, "She needs cash available."],
 ["Which is least likely a rationale for having an IPS?", ["It guarantees the investor's return objective will be met.", "It forces investors to state realistic goals.", "It gives a standard for judging performance."], 0, "No document can guarantee returns."],
 ["A questionnaire shows that an investor's willingness to take risk is high, but her financial situation shows a low ability. Her overall risk tolerance should be considered:", ["below average.", "above average.", "average."], 0, "Ability limits overall tolerance."],
 ["Excluding companies that produce weapons from a portfolio is an example of:", ["exclusionary screening.", "positive screening.", "impact investing."], 0, "Sectors or companies are ruled out."],
])

EK["bb"] = dict(
notes="""<h3>More on behavioural biases</h3>
<div class="tbl"><table>
<tr><th>Type</th><th>Biases</th><th>How to deal with them</th></tr>
<tr><td>Cognitive: belief perseverance</td><td>Conservatism, confirmation, representativeness, illusion of control, hindsight</td><td>Usually corrected with better information and education</td></tr>
<tr><td>Cognitive: information processing</td><td>Anchoring and adjustment, mental accounting, framing, availability</td><td>Usually corrected</td></tr>
<tr><td>Emotional</td><td>Loss aversion, overconfidence, self-control, status quo, endowment, regret aversion</td><td>Harder to correct; often accommodated</td></tr>
</table></div>
<ul>
<li>Mental accounting: treating money differently depending on its source or intended use (wages versus bonuses).</li>
<li>Loss aversion: reluctance to sell a losing position to avoid realizing the loss.</li>
<li>Endowment bias: valuing an asset more simply because you own it. Under-diversification can come from familiarity, home bias and endowment effects.</li>
<li>Availability bias: judging likelihood by how easily examples come to mind; overreacting to news and anecdotes.</li>
<li>Behavioural finance helps explain bubbles: overconfidence and confirmation bias can feed them.</li>
</ul>""",
qs=[
 ["An investor puts his wages into safe investments but uses his bonuses for speculative trades. This is an example of:", ["mental accounting.", "framing bias.", "anchoring."], 0, "Money is treated differently depending on its source."],
 ["Cognitive errors most accurately describe biases that:", ["stem from faulty reasoning and can often be corrected with information.", "stem from feelings and are hard to correct.", "are always rational."], 0, "Emotional biases come from feelings."],
 ["Emotional biases are most likely to:", ["stem from feelings or intuition.", "be easily corrected by education.", "be information processing errors."], 0, "They are usually accommodated rather than corrected."],
 ["Which bias is related to information processing?", ["Anchoring", "Loss aversion", "Status quo"], 0, "The other two are emotional biases."],
 ["Conservatism, confirmation and representativeness biases are best described as:", ["belief perseverance biases.", "emotional biases.", "information processing errors."], 0, "They involve clinging to existing beliefs."],
 ["An investor refuses to sell a share that has fallen 35% because she does not want to realize the loss. This most likely shows:", ["loss aversion.", "availability bias.", "framing bias."], 0, "Losses feel worse than equal gains feel good."],
 ["Compared with emotional biases, cognitive errors are more likely to be:", ["corrected by better information.", "difficult to overcome.", "accommodated."], 0, "Education helps with cognitive errors."],
 ["An investor who judges how likely events are by how easily examples come to mind shows:", ["availability bias.", "conservatism bias.", "anchoring bias."], 0, "Recent or vivid news has too much influence."],
 ["An investor who overreacts to recent news and trades too often most likely shows:", ["availability bias.", "status quo bias.", "endowment bias."], 0, "Recent events dominate his judgement."],
 ["Loss aversion, overconfidence and status quo bias are:", ["emotional biases.", "cognitive errors.", "information processing errors."], 0, "They come from feelings."],
 ["An investor who values an inherited painting more than its market value simply because he owns it shows:", ["endowment bias.", "confirmation bias.", "anchoring."], 0, "Ownership raises perceived value."],
 ["Portfolios that are less diversified than traditional finance would suggest are best explained by:", ["familiarity and endowment biases.", "rational expectations.", "risk neutrality."], 0, "Investors overweight what they know or own."],
])

EK["rm"] = dict(
terms=[
 ["Value at risk (VaR)", "Riske maruz değer (RMD)", "The minimum loss expected over a period with a given probability, such as 5% of days.", "Belirli bir olasılıkla, örneğin günlerin %5'inde, bir dönemde beklenen asgari kayıp."],
 ["Conditional VaR", "Koşullu riske maruz değer", "The expected loss given that the loss exceeds VaR; a measure of tail risk.", "Kaybın RMD'yi aştığı durumda beklenen kayıp; kuyruk riski ölçüsü."],
 ["Scenario analysis", "Senaryo analizi", "Estimating the effect on a portfolio of several factors changing at once.", "Birkaç etkenin aynı anda değişmesinin portföye etkisini tahmin etme."],
],
notes="""<h3>More on risk management</h3>
<ul>
<li>The aim of risk management is not to eliminate risk but to identify, measure and choose which risks to take, in line with the organization's goals and risk tolerance.</li>
<li>Financial risks: market, credit, liquidity. Non-financial: operational (people, processes, systems, external events), model, legal, regulatory, tax, settlement, solvency, reputational.</li>
<li><b>Risk governance</b> is top-down direction and oversight of risk management by the board, including setting risk tolerance.</li>
<li>Methods: avoid, accept, prevent, <b>transfer</b> (insurance moves the risk to another party), <b>shift</b> (derivatives change the distribution of outcomes).</li>
<li>Measures: duration and rho for interest rates, beta for equities, VaR and conditional VaR for tail risk. Scenario analysis changes several factors at once; sensitivity analysis changes one.</li>
<li>Internal and external risks interact, so they should be considered together.</li>
</ul>""",
qs=[
 ["Which risk is most accurately classified as non-financial?", ["Model risk", "Liquidity risk", "Credit risk"], 0, "Model errors arise inside the organization."],
 ["A manager estimates the effect on a portfolio of a 3% rise in interest rates combined with a 15% fall in equities. This is:", ["scenario analysis.", "sensitivity analysis.", "value at risk."], 0, "Several factors change together."],
 ["An objective of the risk management process is to:", ["identify risks and decide which to take.", "eliminate all risks.", "maximize returns regardless of risk."], 0, "Taking some risk is necessary to earn returns."],
 ["Buying insurance is best described as a way to:", ["transfer a risk.", "shift a risk.", "prevent a risk."], 0, "Another party bears the loss."],
 ["Operational risk is the risk that:", ["people, processes or systems fail and cause losses.", "a counterparty defaults.", "market prices move."], 0, "It includes human error and external events."],
 ["Value at risk and conditional VaR are measures of:", ["tail risk.", "liquidity risk.", "model risk."], 0, "They describe losses in bad outcomes."],
 ["Examples of financial risks include:", ["credit, market and liquidity risk.", "operational, model and tax risk.", "legal and reputational risk."], 0, "The others are non-financial."],
 ["Measures of interest rate sensitivity least likely include:", ["beta.", "duration.", "rho."], 0, "Beta measures sensitivity to equity markets."],
 ["Risk governance is best described as:", ["top-down oversight of risk management by the board.", "measuring daily VaR.", "buying insurance."], 0, "It sets the framework and risk tolerance."],
 ["Risk management should consider internal and external risks:", ["together, because they interact.", "independently.", "only if they are large."], 0, "A single event can trigger both."],
])

# Sayı içermeyen sorularda doğru şıkları sırayla A/B/C'ye dağıt.
_n = 0
for _e in EK.values():
    for _q in _e.get("qs", []):
        if any(_re.search(r"\d", _x) for _x in _q[1]): continue
        _j = _n % 3; _o = _q[1]; _i = _q[2]
        _o[_i], _o[_j] = _o[_j], _o[_i]; _q[2] = _j; _n += 1
