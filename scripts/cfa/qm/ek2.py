import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- rr: Rates and Returns ---
_g = (1.2 * .9) ** .5 - 1
EK["rr"] = G(
    [("A fund returns +20% in year 1 and −10% in year 2. What are the arithmetic and geometric mean returns?",
      f"arithmetic mean = (20% − 10%) / 2 = {(20-10)/2:.1f}%|geometric mean = (1.20 × 0.90)<sup>1/2</sup> − 1 = {_g*100:.2f}%",
      "The geometric mean is the rate at which money actually grew. It is always below the arithmetic mean unless every return is the same."),
     ("An investor puts 1,000 into a stock each month. The price is 10 in the first month and 20 in the second. What is the average cost per share?",
      f"shares bought = 1,000/10 + 1,000/20 = {1000/10+1000/20:.0f}|average cost = 2,000 / 150 = {2000/150:.2f} (the harmonic mean of 10 and 20)",
      "With equal amounts invested each period, the harmonic mean, not the arithmetic mean of 15, gives the average price paid.")],
    (["Measure", "Use it for"], [
        ["Arithmetic mean", "Expected return for a single period"],
        ["Geometric mean", "Compound growth over several periods"],
        ["Harmonic mean", "Average price when equal amounts are invested; averaging ratios such as P/E"],
        ["Time-weighted return", "Evaluating a manager: unaffected by deposits and withdrawals"],
        ["Money-weighted return", "The investor's own experience: an IRR, affected by the timing and size of cash flows"],
        ["Real return", "(1 + nominal) / (1 + inflation) − 1"]]),
    "Typical items give a short return series and ask for one of the means, or ask which return measure fits a situation. For the same data, harmonic ≤ geometric ≤ arithmetic. If the manager does not control cash flows, the time-weighted return is the fair measure.")

# --- tv: Time Value of Money ---
EK["tv"] = G(
    [("A preferred share pays a dividend of 5 forever and investors require 8%. A common share will pay a dividend of 2.00 next year, growing at 4% forever, and investors require 9%. Value both.",
      f"preferred = 5 / 0.08 = {5/.08:.2f}|common = D<sub>1</sub> / (r − g) = 2.00 / (0.09 − 0.04) = {2/(.09-.04):.2f}", ""),
     ("A 10-year zero-coupon bond with a face value of 100 trades at 61.39. What is its yield?",
      f"r = (100 / 61.39)<sup>1/10</sup> − 1 = {((100/61.39)**.1-1)*100:.2f}%",
      "Price and yield are two views of the same thing: given one, solve for the other.")],
    (["Pair", "Difference"], [
        ["Annuity vs perpetuity", "A fixed number of level payments vs level payments forever (PV = payment / r)"],
        ["Ordinary annuity vs annuity due", "Payments at the end vs at the beginning of each period; the annuity due is worth (1 + r) times more"],
        ["Implied return vs implied growth", "Solving the pricing equation for r, or for g, given the market price"],
        ["Cash flow additivity", "Present values at the same date can be added; two strategies with identical cash flows must have the same price"]]),
    "Expect a present value, an implied yield or an implied growth rate. Cash flow additivity is behind three items in the curriculum: forward interest rates, forward exchange rates and option pricing by replication. Make sure the dividend in the constant-growth formula is next year's, not the one just paid.")

# --- sm: Statistical Measures ---
_x = [2, 4, 6, 8, 10]; _m = sum(_x) / 5; _v = sum((i - _m) ** 2 for i in _x) / 4
EK["sm"] = G(
    [("A sample of five annual returns is 2%, 4%, 6%, 8% and 10%. Find the mean, the mean absolute deviation, the sample standard deviation and the coefficient of variation.",
      f"mean = {_m:.0f}%|MAD = (4 + 2 + 0 + 2 + 4) / 5 = {sum(abs(i-_m) for i in _x)/5:.1f}%|sample variance = (16 + 4 + 0 + 4 + 16) / (5 − 1) = {_v:.0f}|standard deviation = {_v**.5:.2f}%|coefficient of variation = {_v**.5:.2f} / 6 = {_v**.5/_m:.2f}",
      "A sample variance divides by n − 1; a population variance divides by n.")],
    (["Shape", "What it means"], [
        ["Positive (right) skew", "Long right tail: mean &gt; median &gt; mode"],
        ["Negative (left) skew", "Long left tail: mean &lt; median &lt; mode; more frequent large losses"],
        ["Leptokurtic (excess kurtosis &gt; 0)", "Fatter tails and a higher peak than the normal distribution: more extreme outcomes"],
        ["Platykurtic (excess kurtosis &lt; 0)", "Thinner tails than the normal distribution"],
        ["Target semideviation", "Dispersion of returns below a target only: a measure of downside risk"]]),
    "Besides calculation, expect interpretation: which fund has more risk per unit of return (higher coefficient of variation), or what negative skew and excess kurtosis imply for risk (large losses are more likely than a normal distribution suggests). Correlation measures linear association only and never proves causation.")

# --- pt: Probability Trees ---
EK["pt"] = G(
    [("The probability that the economy expands is 60%. A company beats its earnings forecast with probability 80% in an expansion and 30% otherwise. What is the probability that it beats the forecast? If it does, what is the probability that the economy expanded?",
      f"P(beat) = 0.60 × 0.80 + 0.40 × 0.30 = {.6*.8:.2f} + {.4*.3:.2f} = {.6*.8+.4*.3:.2f}|P(expansion &#124; beat) = 0.48 / 0.60 = {.48/.6:.2f}",
      "The first line is the total probability rule; the second is Bayes' formula. The news of a beat raised the probability of expansion from 60% to 80%.")],
    (["Pair", "Difference"], [
        ["Unconditional vs conditional probability", "P(A) on its own vs P(A | B), given that B has happened"],
        ["Joint probability", "P(A and B) = P(A | B) × P(B)"],
        ["Independent vs mutually exclusive", "Independent: one event does not change the other's probability. Mutually exclusive: they cannot both happen, so they are strongly dependent"],
        ["Prior vs posterior probability", "Before the new information vs updated by Bayes' formula"],
        ["Expected value vs conditional expected value", "Weighted by all probabilities vs weighted within one scenario only"]]),
    "Draw the tree. Multiply along the branches to get joint probabilities and add across branches to get totals. Bayes questions always ask for the reverse of the conditional probability you were given. A common wrong option treats mutually exclusive events as independent.")

# --- pm: Portfolio Mathematics ---
EK["pm"] = G(
    [("An investor must not fall below a return of 4%. Portfolio A has an expected return of 10% and a standard deviation of 15%. Portfolio B has an expected return of 8% and a standard deviation of 8%. Which does Roy's safety-first criterion prefer?",
      f"SF ratio A = (10 − 4) / 15 = {(10-4)/15:.2f}|SF ratio B = (8 − 4) / 8 = {(8-4)/8:.2f}",
      "Choose B: its expected return lies more standard deviations above the threshold, so the probability of falling short is lower."),
     ("How many distinct covariances are needed for a portfolio of 20 assets?",
      f"n(n − 1) / 2 = 20 × 19 / 2 = {20*19//2}", "")],
    (["Pair", "Difference"], [
        ["Covariance vs correlation", "Covariance has units and no bounds; correlation is covariance divided by both standard deviations and lies between −1 and +1"],
        ["Safety-first ratio vs Sharpe ratio", "Same form, but the safety-first ratio subtracts the investor's threshold return instead of the risk-free rate"],
        ["Shortfall risk", "The probability that the return falls below the threshold; minimized by the highest safety-first ratio"],
        ["Portfolio return vs portfolio variance", "Return is a simple weighted average; variance also depends on every pairwise covariance"]]),
    "Expect a safety-first comparison, a covariance-to-correlation conversion, or a two-asset portfolio variance. Convert between the two with correlation = covariance / (σ<sub>A</sub> × σ<sub>B</sub>). A correlation of zero does not mean zero portfolio risk; it only removes the covariance term.")

# --- si: Simulation Methods ---
EK["si"] = G(
    [("A share price rises from 100 to 110 over a year. What is the continuously compounded return? If that return is earned for two years, what is the ending price?",
      f"r = ln(110 / 100) = {math.log(1.1)*100:.2f}%|price after two years = 100 × e<sup>2 × 0.0953</sup> = {100*math.exp(2*math.log(1.1)):.2f}",
      "Continuously compounded returns add up over time, which is why they are modelled as normal while prices are lognormal.")],
    (["Pair", "Difference"], [
        ["Normal vs lognormal", "Normal: symmetric, can be negative, used for returns. Lognormal: bounded at zero, skewed right, used for prices"],
        ["Monte Carlo simulation vs bootstrap", "Monte Carlo draws from a distribution the analyst specifies; bootstrap resamples the observed data with replacement"],
        ["Simulation vs analytical solution", "Simulation gives an estimate, not an exact answer, and cannot explain cause and effect"],
        ["Independent and identically distributed", "The assumption that lets volatility scale with the square root of time"]]),
    "Questions ask which method needs no distributional assumption (bootstrap), why prices are modelled as lognormal (they cannot fall below zero), or what the steps of a Monte Carlo simulation are: specify the variables and their distributions, draw random values, compute the outcome, repeat, and summarise the distribution of results.")

# --- ei: Estimation and Inference ---
EK["ei"] = G(
    [("A sample of 100 returns has a mean of 8% and a standard deviation of 20%. What is the standard error of the mean, and the 95% confidence interval?",
      f"standard error = s / √n = 20 / √100 = {20/10:.1f}%|95% interval = 8 ± 1.96 × 2.0 = {8-1.96*2:.2f}% to {8+1.96*2:.2f}%",
      "Quadrupling the sample size would halve the standard error.")],
    (["Pair", "Difference"], [
        ["Standard deviation vs standard error", "Dispersion of individual observations vs dispersion of the sample mean around the true mean"],
        ["Stratified vs cluster sampling", "Sample from every subgroup, in proportion vs pick whole subgroups at random and sample only those"],
        ["Convenience vs judgmental sampling", "Whatever is easy to obtain vs selected using the researcher's expertise; neither is probability sampling"],
        ["Bootstrap vs jackknife", "Resample with replacement, many times vs leave out one observation at a time"],
        ["Central limit theorem", "For large samples (n ≥ 30) the sample mean is approximately normal whatever the population's distribution"]]),
    "Expect a standard error or confidence interval, and questions that describe a sampling method. Bias questions are common: survivorship bias (only surviving funds), look-ahead bias (information not available at the time), data snooping (searching until something looks significant) and time-period bias.")

# --- ht: Hypothesis Testing ---
EK["ht"] = G(
    [("A manager claims a mean annual return different from 5%. A sample of 100 returns has a mean of 8% and a standard deviation of 20%. Test at the 5% level (critical values ±1.98).",
      f"H<sub>0</sub>: μ = 5%; H<sub>a</sub>: μ ≠ 5%|t = (8 − 5) / (20 / √100) = {(8-5)/2:.2f}|1.50 is inside ±1.98: do not reject H<sub>0</sub>",
      "The sample mean differs from 5%, but not by enough to rule out chance. We never \"accept\" the null; we fail to reject it.")],
    (["Decision", "Null is true", "Null is false"], [
        ["Reject the null", "Type I error (probability = significance level α)", "Correct (probability = power)"],
        ["Do not reject the null", "Correct", "Type II error (probability = β)"]]),
    "Know the error table and that power = 1 − P(Type II error). Lowering the significance level reduces Type I errors but raises Type II errors. Choosing the test is also examined: t-test for a mean or a difference in means, paired t-test for dependent samples, chi-square for a single variance, F-test for two variances. Reject when the p-value is below the significance level.")

# --- ti: Tests of Independence ---
_t = .4 * math.sqrt(25) / math.sqrt(1 - .16)
EK["ti"] = G(
    [("The sample correlation between two funds' returns is 0.40 over 27 months. Is it significantly different from zero at the 5% level (critical t with 25 degrees of freedom = 2.060)?",
      f"t = r × √(n − 2) / √(1 − r<sup>2</sup>) = 0.40 × √25 / √0.84 = {_t:.3f}|{_t:.3f} &gt; 2.060: reject the hypothesis of zero correlation", ""),
     ("In a contingency table, a cell's row total is 60, its column total is 50 and the grand total is 200. What is the expected frequency under independence, and how many degrees of freedom does a 3 × 4 table have?",
      f"expected = 60 × 50 / 200 = {60*50/200:.0f}|degrees of freedom = (3 − 1) × (4 − 1) = {2*3}", "")],
    (["Pair", "Difference"], [
        ["Parametric vs non-parametric test", "Assumes a distribution and tests a parameter vs makes few assumptions and often uses ranks"],
        ["Pearson vs Spearman correlation", "Linear relationship between values vs correlation between ranks; Spearman is robust to outliers"],
        ["When to go non-parametric", "Data are ranks, the distribution is clearly non-normal, or outliers dominate"],
        ["Chi-square test of independence", "Compares observed with expected frequencies in a contingency table of categorical data"]]),
    "The correlation t-test formula and its n − 2 degrees of freedom are the core numerical item. Notice that the same correlation can be significant in a large sample and insignificant in a small one. For the contingency table, a large chi-square statistic means the classifications are not independent.")

# --- lr: Simple Linear Regression ---
EK["lr"] = G(
    [("The covariance between a stock's and the market's returns is 0.006 and the variance of the market's returns is 0.004. Mean returns are 8% for the stock and 5% for the market. Find the slope and the intercept.",
      f"slope = covariance / variance of X = 0.006 / 0.004 = {.006/.004:.1f}|intercept = 0.08 − 1.5 × 0.05 = {.08-1.5*.05:.3f}", ""),
     ("A regression on 38 observations has a total sum of squares of 100 and a sum of squared errors of 36. Find R<sup>2</sup>, the standard error of estimate and the F-statistic.",
      f"SSR = 100 − 36 = {100-36}|R<sup>2</sup> = 64 / 100 = {64/100:.2f}|SEE = √(SSE / (n − 2)) = √(36 / 36) = {math.sqrt(36/36):.2f}|F = MSR / MSE = (64 / 1) / (36 / 36) = {64/1:.0f}",
      "In a simple regression, R<sup>2</sup> is the square of the correlation between X and Y, and the F-test and the t-test on the slope reach the same conclusion.")],
    (["Term", "Meaning"], [
        ["SST", "Total variation of the dependent variable"],
        ["SSR", "Variation explained by the regression"],
        ["SSE", "Unexplained variation (squared residuals)"],
        ["R<sup>2</sup> vs SEE", "Share of variation explained (higher is better) vs typical size of a residual (lower is better)"],
        ["Homoskedasticity", "Residual variance is constant across observations; its violation is heteroskedasticity"],
        ["Log-lin vs lin-log vs log-log", "Log of Y only (slope is a growth rate), log of X only, or both (slope is an elasticity)"]]),
    "Most items give an ANOVA table and ask for R<sup>2</sup>, SEE or F. Others ask you to interpret a slope, test it with t = (estimate − hypothesized value) / standard error, or name the assumption a residual plot violates. The four assumptions: linearity, constant variance, independent residuals, normal residuals.")

# --- bd: Big Data ---
EK["bd"] = G(
    [("A manager has ten years of news articles, each labelled by analysts as positive or negative for the company. She wants a model that labels new articles automatically. Which techniques apply?",
      "",
      "The text must first be turned into data with natural language processing. Because the training examples carry known labels, this is supervised learning, specifically classification. If there were no labels and she wanted to group similar articles, it would be unsupervised learning (clustering).")],
    (["Pair", "Difference"], [
        ["Supervised vs unsupervised learning", "Learns from labelled examples to predict a target vs finds structure in unlabelled data"],
        ["Deep learning", "Neural networks with many layers; used for images, speech and text, in supervised or unsupervised settings"],
        ["Overfitting vs underfitting", "Model fits noise and fails on new data vs model is too simple to capture the pattern"],
        ["Structured vs unstructured data", "Rows and columns vs text, images, audio"],
        ["Volume, velocity, variety", "Amount of data, speed at which it arrives, range of formats"],
        ["Artificial intelligence vs machine learning", "Systems that perform tasks needing human-like judgment vs the subset that learns rules from data"]]),
    "Questions are definitional: classify a task, a data type or a problem. Remember the practical cautions: data quality and sourcing biases, the \"black box\" nature of complex models, and that a model which performs perfectly on training data but poorly out of sample is overfitted.")
