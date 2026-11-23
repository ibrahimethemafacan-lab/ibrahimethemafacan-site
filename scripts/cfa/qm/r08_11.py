# CFA Level I · Quantitative Methods · readings 8–11. Original study notes and questions.
R = []

R.append(dict(id="ht", n="Hypothesis Testing", k="TESTING", w=3, c="#c2417a",
terms=[
 ["Null hypothesis (H0)", "Sıfır hipotezi (H0)", "The statement being tested; it is assumed true unless the sample gives strong evidence against it and always contains the equality.", "Test edilen önerme; örneklem aksine güçlü kanıt vermedikçe doğru kabul edilir ve her zaman eşitliği içerir."],
 ["Alternative hypothesis (Ha)", "Alternatif hipotez (Ha)", "The statement accepted if the null hypothesis is rejected; usually what the researcher hopes to show.", "Sıfır hipotezi reddedilirse kabul edilen önerme; genellikle araştırmacının göstermek istediği durumdur."],
 ["Test statistic", "Test istatistiği", "A number computed from the sample and compared with a critical value to decide whether to reject the null hypothesis.", "Örneklemden hesaplanan ve sıfır hipotezinin reddedilip reddedilmeyeceğine karar vermek için kritik değerle karşılaştırılan sayı."],
 ["Significance level", "Anlamlılık düzeyi", "The probability of rejecting a true null hypothesis that the researcher is willing to accept.", "Araştırmacının kabul ettiği, doğru bir sıfır hipotezini reddetme olasılığı."],
 ["Type I error", "Birinci tip hata", "Rejecting a null hypothesis that is true.", "Doğru olan sıfır hipotezini reddetmek."],
 ["Type II error", "İkinci tip hata", "Failing to reject a null hypothesis that is false.", "Yanlış olan sıfır hipotezini reddedememek."],
 ["Power of a test", "Testin gücü", "The probability of correctly rejecting a false null hypothesis; one minus the probability of a Type II error.", "Yanlış bir sıfır hipotezini doğru biçimde reddetme olasılığı; bir eksi ikinci tip hata olasılığı."],
 ["Critical value", "Kritik değer", "The boundary of the rejection region for the test statistic.", "Test istatistiği için ret bölgesinin sınırı."],
 ["p-value", "p-değeri", "The smallest significance level at which the null hypothesis can be rejected.", "Sıfır hipotezinin reddedilebileceği en küçük anlamlılık düzeyi."],
 ["One-tailed test", "Tek kuyruklu test", "A test in which the rejection region lies in only one tail of the distribution.", "Ret bölgesinin dağılımın yalnızca bir kuyruğunda bulunduğu test."],
 ["Degrees of freedom", "Serbestlik derecesi", "The number of independent observations available to estimate a parameter.", "Bir parametreyi tahmin etmek için kullanılabilen bağımsız gözlem sayısı."],
 ["Paired comparisons test", "Eşleştirilmiş karşılaştırma testi", "A test of the mean of the differences between two dependent samples.", "Bağımlı iki örneklem arasındaki farkların ortalamasına ilişkin test."],
],
notes="""<h3>The procedure</h3>
<ul>
<li>1. State the null and alternative hypotheses.</li>
<li>2. Choose the test statistic and identify its distribution.</li>
<li>3. Set the significance level.</li>
<li>4. State the decision rule (critical value).</li>
<li>5. Collect data and compute the test statistic.</li>
<li>6. Decide: reject or fail to reject the null. Then make the investment decision.</li>
</ul>
<h3>Setting up hypotheses</h3>
<div class="tbl"><table>
<tr><th>Question</th><th>H<sub>0</sub></th><th>H<sub>a</sub></th><th>Test</th></tr>
<tr><td>Is it different from θ<sub>0</sub>?</td><td>θ = θ<sub>0</sub></td><td>θ ≠ θ<sub>0</sub></td><td>Two-tailed</td></tr>
<tr><td>Is it greater than θ<sub>0</sub>?</td><td>θ ≤ θ<sub>0</sub></td><td>θ &gt; θ<sub>0</sub></td><td>One-tailed (right)</td></tr>
<tr><td>Is it less than θ<sub>0</sub>?</td><td>θ ≥ θ<sub>0</sub></td><td>θ &lt; θ<sub>0</sub></td><td>One-tailed (left)</td></tr>
</table></div>
<ul>
<li>The equals sign always sits in the null. What the researcher wants to demonstrate goes in the alternative.</li>
<li>We never "accept" the null; we either reject it or fail to reject it.</li>
</ul>
<h3>Two kinds of error</h3>
<div class="tbl"><table>
<tr><th>Decision</th><th>H<sub>0</sub> is true</th><th>H<sub>0</sub> is false</th></tr>
<tr><td>Do not reject H<sub>0</sub></td><td>Correct</td><td>Type II error (probability β)</td></tr>
<tr><td>Reject H<sub>0</sub></td><td>Type I error (probability α)</td><td>Correct (power = 1 − β)</td></tr>
</table></div>
<ul>
<li>The significance level α is the probability of a Type I error.</li>
<li>For a given sample size, lowering α raises β and reduces power. The only way to lower both is a larger sample.</li>
</ul>
<h3>p-value</h3>
<ul>
<li>The p-value is the smallest significance level at which the null can be rejected.</li>
<li>Decision rule: reject if <b>p-value &lt; α</b>. A p-value of 0.03 rejects at 5% but not at 1%.</li>
<li>Statistical significance is not the same as economic significance. After transaction costs, taxes and risk, a statistically significant result may not be worth acting on.</li>
<li>When many tests are run, some will appear significant by chance. Rejections should be adjusted for this multiple testing problem.</li>
</ul>
<h3>Which test statistic</h3>
<div class="tbl"><table>
<tr><th>Hypothesis about</th><th>Statistic</th><th>Degrees of freedom</th></tr>
<tr><td>A single mean (variance unknown)</td><td>t = (X̄ − μ<sub>0</sub>) / (s / √n)</td><td>n − 1</td></tr>
<tr><td>Difference of two means, independent samples, equal variances</td><td>t with pooled variance</td><td>n<sub>1</sub> + n<sub>2</sub> − 2</td></tr>
<tr><td>Mean of differences, dependent samples (paired)</td><td>t = (d̄ − μ<sub>d0</sub>) / (s<sub>d</sub> / √n)</td><td>n − 1</td></tr>
<tr><td>A single variance</td><td>χ² = (n − 1)s² / σ<sub>0</sub>²</td><td>n − 1</td></tr>
<tr><td>Equality of two variances</td><td>F = s<sub>1</sub>² / s<sub>2</sub>²</td><td>n<sub>1</sub> − 1 and n<sub>2</sub> − 1</td></tr>
</table></div>
<ul>
<li>The chi-square and F distributions are bounded below by zero and are not symmetric.</li>
<li>For the F-test, put the larger sample variance in the numerator.</li>
<li>Use the <b>paired</b> test when the two samples are linked, for example the same funds before and after a rule change, or two shares over the same months.</li>
</ul>
<div class="trap"><b>Exam trap</b>Tests about means use t. Tests about one variance use chi-square. Tests comparing two variances use F. Questions often test nothing more than this matching.</div>""",
qs=[
 ["A Type I error is best described as:", ["rejecting a true null hypothesis.", "rejecting a false null hypothesis.", "failing to reject a false null hypothesis."], 0, "A Type I error is a false rejection. Failing to reject a false null is a Type II error, and rejecting a false null is the correct decision."],
 ["The power of a test is best described as the probability of:", ["a Type II error.", "rejecting a false null hypothesis.", "failing to reject a true null hypothesis."], 1, "Power = 1 − P(Type II error): the chance that the test detects a false null."],
 ["A test produces a p-value of 0.03. The null hypothesis should be rejected at a significance level of:", ["1% but not 5%.", "5% but not 1%.", "both 1% and 5%."], 1, "Reject when the p-value is below the significance level. 0.03 is below 0.05 but above 0.01."],
 ["A sample of 64 monthly returns has a mean of 1.5% and a standard deviation of 4.0%. The t-statistic for testing whether the population mean equals zero is closest to:", ["0.38", "3.00", "24.00"], 1, "t = (1.5 − 0) / (4.0 / √64) = 1.5 / 0.5 = 3.00."],
 ["The appropriate test statistic for a hypothesis about the value of a single population variance is the:", ["t-statistic.", "F-statistic.", "chi-square statistic."], 2, "A single variance is tested with the chi-square statistic with n − 1 degrees of freedom."],
 ["An analyst wants to test whether the return variances of two independent, normally distributed funds are equal. The most appropriate test statistic is the:", ["t-statistic.", "F-statistic.", "chi-square statistic."], 1, "Equality of two variances is tested with the ratio of the sample variances, which follows an F distribution."],
 ["An analyst compares the monthly returns of two shares over the same 36 months and believes both are affected by the same market events. The most appropriate test of whether their mean returns differ is a:", ["chi-square test.", "paired comparisons test.", "difference in means test with pooled variance."], 1, "The samples are dependent, so the test is based on the mean of the monthly differences. The pooled-variance test assumes independent samples."],
 ["A researcher wants to show that a fund's mean return is greater than 6%. The most appropriate hypotheses are:", ["H0: μ = 6% versus Ha: μ ≠ 6%.", "H0: μ ≤ 6% versus Ha: μ > 6%.", "H0: μ ≥ 6% versus Ha: μ < 6%."], 1, "What the researcher hopes to demonstrate goes in the alternative, and the null carries the equality."],
 ["For a given sample size, reducing the significance level from 5% to 1% will most likely:", ["increase the power of the test.", "increase the probability of a Type I error.", "increase the probability of a Type II error."], 2, "A lower significance level makes rejection harder, so a false null is more likely to survive. Type I error probability falls and power falls."],
 ["A sample of 25 observations has a variance of 0.0025. The test statistic for the hypothesis that the population variance equals 0.0016 is closest to:", ["24.0", "37.5", "39.1"], 1, "χ² = (n − 1)s² / σ0² = 24 × 0.0025 / 0.0016 = 37.5. Using n instead of n − 1 gives 39.1."],
]))

R.append(dict(id="ti", n="Parametric and Non-Parametric Tests of Independence", k="INDEPENDENCE", w=1, c="#5f6fd0",
terms=[
 ["Parametric test", "Parametrik test", "A test that concerns a population parameter and relies on assumptions about the population's distribution.", "Bir ana kütle parametresine ilişkin olan ve ana kütlenin dağılımı hakkındaki varsayımlara dayanan test."],
 ["Non-parametric test", "Parametrik olmayan test", "A test that does not concern a parameter or makes minimal assumptions about the population's distribution.", "Bir parametreye ilişkin olmayan veya ana kütlenin dağılımı hakkında çok az varsayım yapan test."],
 ["Pearson correlation", "Pearson korelasyonu", "The usual correlation coefficient, measuring linear association between two variables.", "İki değişken arasındaki doğrusal ilişkiyi ölçen olağan korelasyon katsayısı."],
 ["Spearman rank correlation", "Spearman sıra korelasyonu", "A correlation coefficient computed on the ranks of the observations instead of their values.", "Gözlemlerin değerleri yerine sıralarından hesaplanan korelasyon katsayısı."],
 ["Rank", "Sıra (rank)", "The position of an observation when the data are sorted.", "Veriler sıralandığında bir gözlemin konumu."],
 ["Contingency table", "Kontenjans tablosu (çapraz tablo)", "A table that counts observations classified by two categorical characteristics.", "İki kategorik özelliğe göre sınıflandırılmış gözlemlerin sayılarını gösteren tablo."],
 ["Categorical data", "Kategorik veri", "Data that sort observations into groups, with no numerical measurement.", "Gözlemleri sayısal ölçüm olmaksızın gruplara ayıran veri."],
 ["Observed frequency", "Gözlenen frekans", "The actual count of observations in a cell of the table.", "Tablonun bir hücresindeki gerçek gözlem sayısı."],
 ["Expected frequency", "Beklenen frekans", "The count a cell would have if the two classifications were independent.", "İki sınıflandırma bağımsız olsaydı hücrede olması beklenen sayı."],
 ["Test of independence", "Bağımsızlık testi", "A chi-square test of whether two categorical characteristics are related.", "İki kategorik özelliğin ilişkili olup olmadığını sınayan ki-kare testi."],
],
notes="""<h3>Parametric or non-parametric</h3>
<ul>
<li><b>Parametric tests</b> (t, chi-square for a variance, F) concern a parameter and assume something about the population, typically normality.</li>
<li>Use a <b>non-parametric</b> test when:</li>
<li>the data do not meet the distributional assumptions, for example a small sample from a clearly non-normal population,</li>
<li>there are outliers that would distort a parametric statistic,</li>
<li>the data are given as ranks or on an ordinal scale,</li>
<li>the hypothesis is not about a parameter, for example whether a sample is random.</li>
<li>When the assumptions do hold, the parametric test is preferred because it has more power.</li>
</ul>
<h3>Testing whether a correlation is zero (parametric)</h3>
<p class="f">t = r × √(n − 2) / √(1 − r²) &nbsp;&nbsp;&nbsp; degrees of freedom = n − 2</p>
<ul>
<li>H<sub>0</sub>: ρ = 0 against H<sub>a</sub>: ρ ≠ 0. Assumes both variables are normally distributed.</li>
<li>For the same sample correlation, a larger sample gives a larger t-statistic and a smaller critical value, so rejection becomes more likely. A small correlation can be significant in a big sample.</li>
</ul>
<h3>Spearman rank correlation (non-parametric)</h3>
<ul>
<li>Rank the observations of X and of Y separately, take the difference d between each pair of ranks, and compute:</li>
</ul>
<p class="f">r<sub>S</sub> = 1 − 6 Σd<sub>i</sub>² / [n(n² − 1)]</p>
<ul>
<li>Use it when the variables are not normally distributed or contain outliers. For samples larger than about 30 its significance is tested with the same t-formula, with n − 2 degrees of freedom.</li>
</ul>
<h3>Test of independence with a contingency table</h3>
<ul>
<li>Question: are two categorical classifications related? For example, is fund size (small, medium, large) related to investment style (value, blend, growth)?</li>
<li>H<sub>0</sub>: the two classifications are independent.</li>
</ul>
<p class="f">expected frequency of a cell = (row total × column total) / overall total</p>
<p class="f">χ² = Σ (O<sub>ij</sub> − E<sub>ij</sub>)² / E<sub>ij</sub> &nbsp;&nbsp;&nbsp; degrees of freedom = (r − 1)(c − 1)</p>
<ul>
<li>r is the number of rows and c the number of columns. The test is one-tailed: reject independence when the statistic exceeds the critical value.</li>
<li>Large gaps between observed and expected counts produce a large statistic and point to a relationship.</li>
</ul>
<div class="trap"><b>Exam trap</b>Degrees of freedom for the contingency table are (rows − 1) × (columns − 1), not the number of cells and not n − 1.</div>""",
qs=[
 ["A sample of 27 paired observations has a correlation of 0.40. The t-statistic for testing whether the population correlation equals zero is closest to:", ["2.00", "2.18", "2.27"], 1, "t = 0.40 × √25 / √(1 − 0.16) = 2.00 / 0.9165 = 2.18. Using √27 in the numerator gives 2.27."],
 ["A test of whether a population correlation equals zero uses 27 paired observations. The degrees of freedom are:", ["25", "26", "27"], 0, "The correlation test has n − 2 degrees of freedom: 27 − 2 = 25."],
 ["A non-parametric test is most appropriate when the:", ["data are ranks.", "sample is large.", "population is normally distributed."], 0, "Ranked data, outliers or violated distributional assumptions call for non-parametric tests. With a normal population, a parametric test is more powerful."],
 ["The Spearman rank correlation coefficient is calculated using the:", ["ranks of the observations.", "squared values of the observations.", "logarithms of the observations."], 0, "Spearman's coefficient replaces the values with their ranks, which makes it robust to outliers and non-normality."],
 ["A contingency table has 3 rows and 4 columns. The degrees of freedom for the chi-square test of independence are:", ["6", "11", "12"], 0, "(r − 1)(c − 1) = 2 × 3 = 6."],
 ["In a contingency table of 200 observations, a cell lies in a row with a total of 40 and a column with a total of 30. The expected frequency of the cell under independence is closest to:", ["6.0", "7.5", "35.0"], 0, "Expected frequency = (40 × 30) / 200 = 6.0."],
 ["The most appropriate statistic for testing whether two categorical characteristics are independent is the:", ["t-statistic.", "F-statistic.", "chi-square statistic."], 2, "Independence in a contingency table is tested by comparing observed with expected frequencies using a chi-square statistic."],
 ["For five pairs of ranked observations, the sum of the squared differences in ranks is 4. The Spearman rank correlation is closest to:", ["0.20", "0.80", "0.96"], 1, "rS = 1 − (6 × 4) / [5 × (25 − 1)] = 1 − 24 / 120 = 0.80."],
 ["Holding the sample correlation constant, increasing the sample size makes rejecting the hypothesis of zero correlation:", ["less likely.", "more likely.", "neither more nor less likely."], 1, "A larger n raises the t-statistic and lowers the critical value, so the same correlation is more likely to be judged significant."],
 ["In a chi-square test of independence, a cell has an observed frequency of 30 and an expected frequency of 24. Its contribution to the test statistic is closest to:", ["0.25", "1.20", "1.50"], 2, "(30 − 24)² / 24 = 36 / 24 = 1.50. Dividing by the observed frequency gives 1.20, which is the common error."],
]))

R.append(dict(id="lr", n="Simple Linear Regression", k="REGRESSION", w=3, c="#1f7a8c",
terms=[
 ["Dependent variable", "Bağımlı değişken", "The variable whose variation the regression tries to explain (Y).", "Regresyonun değişimini açıklamaya çalıştığı değişken (Y)."],
 ["Independent variable", "Bağımsız değişken", "The variable used to explain the dependent variable (X); also called the explanatory variable.", "Bağımlı değişkeni açıklamak için kullanılan değişken (X); açıklayıcı değişken de denir."],
 ["Intercept", "Sabit terim (kesişim)", "The estimated value of the dependent variable when the independent variable is zero.", "Bağımsız değişken sıfır olduğunda bağımlı değişkenin tahmin edilen değeri."],
 ["Slope coefficient", "Eğim katsayısı", "The estimated change in the dependent variable for a one-unit change in the independent variable.", "Bağımsız değişkendeki bir birimlik değişim için bağımlı değişkende tahmin edilen değişim."],
 ["Residual", "Artık (kalıntı)", "The difference between an observed value of Y and the value predicted by the regression line.", "Y'nin gözlenen değeri ile regresyon doğrusunun öngördüğü değer arasındaki fark."],
 ["Ordinary least squares (OLS)", "En küçük kareler yöntemi", "The method that chooses the line minimizing the sum of squared residuals.", "Artıkların kareleri toplamını en küçük yapan doğruyu seçen yöntem."],
 ["Sum of squares error (SSE)", "Hata kareleri toplamı", "The variation in Y that the regression does not explain.", "Y'deki değişimin regresyon tarafından açıklanmayan kısmı."],
 ["Coefficient of determination (R²)", "Belirlilik katsayısı (R²)", "The fraction of the total variation in Y explained by the regression.", "Y'deki toplam değişimin regresyon tarafından açıklanan oranı."],
 ["Standard error of the estimate (SEE)", "Tahminin standart hatası", "The standard deviation of the residuals; a measure of how closely the line fits the data.", "Artıkların standart sapması; doğrunun veriye ne kadar iyi uyduğunun ölçüsü."],
 ["Homoskedasticity", "Sabit varyanslılık", "The variance of the residuals is the same for all observations.", "Artıkların varyansı tüm gözlemler için aynıdır."],
 ["Heteroskedasticity", "Değişen varyanslılık", "The variance of the residuals differs across observations.", "Artıkların varyansı gözlemler arasında farklılık gösterir."],
 ["Prediction interval", "Öngörü aralığı", "A range around a predicted value of Y that reflects the uncertainty of the forecast.", "Y'nin öngörülen değeri etrafında, tahminin belirsizliğini yansıtan aralık."],
],
notes="""<h3>The model</h3>
<p class="f">Y<sub>i</sub> = b<sub>0</sub> + b<sub>1</sub>X<sub>i</sub> + ε<sub>i</sub> &nbsp;&nbsp;&nbsp; fitted line: Ŷ<sub>i</sub> = b̂<sub>0</sub> + b̂<sub>1</sub>X<sub>i</sub></p>
<ul>
<li>Y is the dependent (explained) variable, X the independent (explanatory) variable, ε the error term.</li>
<li>Ordinary least squares picks the line that minimizes the sum of squared residuals.</li>
</ul>
<p class="f">b̂<sub>1</sub> = Cov(X,Y) / Var(X) &nbsp;&nbsp;&nbsp; b̂<sub>0</sub> = Ȳ − b̂<sub>1</sub>X̄</p>
<ul>
<li>The fitted line always passes through the point of means (X̄, Ȳ).</li>
<li>The slope has the same sign as the correlation between X and Y.</li>
</ul>
<h3>Four assumptions</h3>
<ul>
<li><b>Linearity:</b> the relationship between X and Y is linear in the parameters.</li>
<li><b>Homoskedasticity:</b> the variance of the residuals is constant across observations.</li>
<li><b>Independence:</b> the residuals are uncorrelated with one another. A pattern over time, such as seasonality, breaks this.</li>
<li><b>Normality:</b> the residuals are normally distributed.</li>
<li>Check them by plotting the residuals against X or against time. Outliers can pull the fitted line a long way.</li>
</ul>
<h3>Analysis of variance</h3>
<p class="f">SST = SSR + SSE</p>
<div class="tbl"><table>
<tr><th>Source</th><th>Sum of squares</th><th>Degrees of freedom</th><th>Mean square</th></tr>
<tr><td>Regression (explained)</td><td>SSR</td><td>1</td><td>MSR = SSR / 1</td></tr>
<tr><td>Error (unexplained)</td><td>SSE</td><td>n − 2</td><td>MSE = SSE / (n − 2)</td></tr>
<tr><td>Total</td><td>SST</td><td>n − 1</td><td></td></tr>
</table></div>
<p class="f">R² = SSR / SST = 1 − SSE / SST &nbsp;&nbsp;&nbsp; SEE = √MSE &nbsp;&nbsp;&nbsp; F = MSR / MSE</p>
<ul>
<li><b>R²</b> is the share of the variation in Y explained by X. In simple regression it equals the squared correlation between X and Y.</li>
<li><b>SEE</b> is in the units of Y; smaller means a tighter fit.</li>
<li>The <b>F-statistic</b> tests whether the slope is zero. With one independent variable it gives the same conclusion as the t-test on the slope, and F = t².</li>
</ul>
<h3>Testing the coefficients</h3>
<p class="f">t = (b̂<sub>1</sub> − B<sub>1</sub>) / s<sub>b̂1</sub> &nbsp;&nbsp;&nbsp; degrees of freedom = n − 2</p>
<ul>
<li>B<sub>1</sub> is the hypothesized value. It is often zero, but not always: testing whether a beta differs from 1 uses B<sub>1</sub> = 1.</li>
</ul>
<div class="trap"><b>Exam trap</b>Read the null hypothesis before computing t. Dividing the coefficient by its standard error is only correct when the hypothesized value is zero.</div>
<h3>Prediction</h3>
<ul>
<li>Insert the forecast X into the fitted equation to obtain Ŷ.</li>
<li>The prediction interval is Ŷ ± t<sub>critical</sub> × s<sub>f</sub>. The standard error of the forecast s<sub>f</sub> is larger than SEE and grows the further the forecast X is from X̄.</li>
</ul>
<h3>Functional forms</h3>
<div class="tbl"><table>
<tr><th>Model</th><th>Equation</th><th>Slope means</th></tr>
<tr><td>Lin-lin</td><td>Y = b<sub>0</sub> + b<sub>1</sub>X</td><td>Absolute change in Y for an absolute change in X</td></tr>
<tr><td>Log-lin</td><td>ln Y = b<sub>0</sub> + b<sub>1</sub>X</td><td>Relative change in Y for an absolute change in X</td></tr>
<tr><td>Lin-log</td><td>Y = b<sub>0</sub> + b<sub>1</sub> ln X</td><td>Absolute change in Y for a relative change in X</td></tr>
<tr><td>Log-log</td><td>ln Y = b<sub>0</sub> + b<sub>1</sub> ln X</td><td>Relative change in Y for a relative change in X (elasticity)</td></tr>
</table></div>
<ul>
<li>Transforming a variable with logarithms can turn a curved relationship into a linear one.</li>
</ul>""",
qs=[
 ["The covariance between X and Y is 0.006 and the variance of X is 0.004. The estimated slope coefficient of a regression of Y on X is closest to:", ["0.67", "1.50", "2.40"], 1, "Slope = Cov(X,Y) / Var(X) = 0.006 / 0.004 = 1.50."],
 ["In a regression of Y on X, the slope is 1.5, the mean of X is 4 and the mean of Y is 8. The intercept is closest to:", ["2.0", "5.3", "14.0"], 0, "Intercept = Ȳ − slope × X̄ = 8 − 1.5 × 4 = 2.0. The line passes through the point of means."],
 ["A regression has a total sum of squares of 200 and a sum of squares error of 50. The coefficient of determination is closest to:", ["0.25", "0.75", "0.87"], 1, "R² = 1 − SSE / SST = 1 − 50 / 200 = 0.75."],
 ["A simple linear regression based on 27 observations has a sum of squares error of 50. The standard error of the estimate is closest to:", ["1.36", "1.41", "2.00"], 1, "MSE = 50 / (27 − 2) = 2.0, and SEE = √2.0 = 1.41. Dividing by n instead of n − 2 gives 1.36."],
 ["A simple linear regression with 27 observations has a regression sum of squares of 150 and a sum of squares error of 50. The F-statistic is closest to:", ["3", "75", "150"], 1, "MSR = 150 / 1 = 150 and MSE = 50 / 25 = 2. F = 150 / 2 = 75."],
 ["Homoskedasticity means that the:", ["residuals are normally distributed.", "residuals are uncorrelated with one another.", "variance of the residuals is constant across observations."], 2, "Homoskedasticity is the constant-variance assumption. Normality and independence of the residuals are separate assumptions."],
 ["A regression of a share's return on the market return gives a slope of 1.5 with a standard error of 0.5. The t-statistic for testing the null hypothesis that the slope equals 1 is closest to:", ["1.0", "2.0", "3.0"], 0, "t = (1.5 − 1.0) / 0.5 = 1.0. The figure 3.0 tests a slope of zero, which is not the hypothesis stated."],
 ["A fitted regression is Ŷ = 2.0 + 1.5X. The predicted value of Y when X equals 6 is closest to:", ["9.0", "11.0", "21.0"], 1, "Ŷ = 2.0 + 1.5 × 6 = 11.0."],
 ["In a log-lin regression model, the slope coefficient is interpreted as the:", ["absolute change in Y for a relative change in X.", "relative change in Y for an absolute change in X.", "relative change in Y for a relative change in X."], 1, "In a log-lin model the dependent variable is in logarithms, so the slope gives the proportional change in Y for a one-unit change in X."],
 ["In a simple linear regression, the correlation between the dependent and independent variables is 0.8. The coefficient of determination is closest to:", ["0.64", "0.80", "0.89"], 0, "With one independent variable, R² equals the squared correlation: 0.8² = 0.64."],
]))

R.append(dict(id="bd", n="Introduction to Big Data Techniques", k="BIG DATA", w=1, c="#6b7a8f",
terms=[
 ["Fintech", "Finansal teknoloji (fintek)", "Technology-driven innovation in the design and delivery of financial services and products.", "Finansal hizmet ve ürünlerin tasarımı ile sunumunda teknolojiye dayalı yenilik."],
 ["Big Data", "Büyük veri", "Very large and varied data sets, from traditional and non-traditional sources, generated at high speed.", "Geleneksel ve geleneksel olmayan kaynaklardan gelen, yüksek hızda üretilen, çok büyük ve çeşitli veri setleri."],
 ["Alternative data", "Alternatif veri", "Data from non-traditional sources such as social media, sensors, satellites and transaction records.", "Sosyal medya, sensörler, uydular ve işlem kayıtları gibi geleneksel olmayan kaynaklardan gelen veri."],
 ["Structured data", "Yapılandırılmış veri", "Data organized in rows and columns that can be stored in a database.", "Satır ve sütunlar halinde düzenlenmiş, veritabanında saklanabilen veri."],
 ["Unstructured data", "Yapılandırılmamış veri", "Data with no predefined format, such as text, audio, images and video.", "Metin, ses, görüntü ve video gibi önceden tanımlı biçimi olmayan veri."],
 ["Artificial intelligence (AI)", "Yapay zekâ", "Computer systems that perform tasks normally requiring human intelligence.", "Normalde insan zekâsı gerektiren görevleri yerine getiren bilgisayar sistemleri."],
 ["Machine learning (ML)", "Makine öğrenmesi", "Algorithms that learn patterns from data and improve without being explicitly programmed with rules.", "Kuralları açıkça programlanmadan veriden örüntü öğrenen ve gelişen algoritmalar."],
 ["Supervised learning", "Gözetimli öğrenme", "Machine learning in which the training data are labelled with the correct output.", "Eğitim verisinin doğru çıktıyla etiketlendiği makine öğrenmesi."],
 ["Unsupervised learning", "Gözetimsiz öğrenme", "Machine learning in which the data are not labelled and the algorithm looks for structure itself.", "Verinin etiketlenmediği ve algoritmanın yapıyı kendisinin aradığı makine öğrenmesi."],
 ["Deep learning", "Derin öğrenme", "Machine learning that uses neural networks with many layers to detect complex patterns.", "Karmaşık örüntüleri saptamak için çok katmanlı sinir ağları kullanan makine öğrenmesi."],
 ["Overfitting", "Aşırı uyum", "A model fits the training data too closely, treating noise as signal, and predicts poorly on new data.", "Modelin eğitim verisine fazla uyması, gürültüyü sinyal sayması ve yeni veride kötü tahmin yapması."],
 ["Natural language processing (NLP)", "Doğal dil işleme", "Using computers to analyse and interpret human language.", "İnsan dilini çözümlemek ve yorumlamak için bilgisayarların kullanılması."],
],
notes="""<h3>Fintech in investment management</h3>
<ul>
<li>Fintech means technology-driven innovation in financial services. For investment work the main areas are analysis of large data sets and the analytical tools that process them: artificial intelligence and machine learning.</li>
</ul>
<h3>What makes data "big"</h3>
<ul>
<li><b>Volume:</b> the quantity of data, now measured in very large units.</li>
<li><b>Velocity:</b> the speed at which data arrive, often in real time.</li>
<li><b>Variety:</b> the range of formats, from structured tables to semi-structured and unstructured text, images and audio.</li>
<li>A fourth quality often added is <b>veracity</b>: how reliable the data are.</li>
</ul>
<h3>Where the data come from</h3>
<div class="tbl"><table>
<tr><th>Source</th><th>Examples</th></tr>
<tr><td>Traditional</td><td>Company filings, market prices, government statistics</td></tr>
<tr><td>Individuals</td><td>Social media posts, online reviews, web searches</td></tr>
<tr><td>Business processes</td><td>Card transactions, point-of-sale records, corporate "exhaust" data</td></tr>
<tr><td>Sensors</td><td>Satellite images, shipping and traffic data, connected devices</td></tr>
</table></div>
<ul>
<li>The last three groups are called <b>alternative data</b>.</li>
<li>Challenges: quality (bias, outliers, missing values), sheer size, and suitability for the question. Unstructured data usually need heavy preparation before analysis.</li>
</ul>
<h3>Artificial intelligence and machine learning</h3>
<ul>
<li>Machine learning algorithms find patterns in data without being given explicit rules. The data are split into a <b>training</b> set to fit the model, a <b>validation</b> set to tune it, and a <b>test</b> set to check how it performs on unseen data.</li>
</ul>
<div class="tbl"><table>
<tr><th>Type</th><th>Data</th><th>Typical task</th></tr>
<tr><td>Supervised</td><td>Labelled inputs and outputs</td><td>Predicting a value or assigning a category</td></tr>
<tr><td>Unsupervised</td><td>Unlabelled</td><td>Grouping similar items, finding structure</td></tr>
<tr><td>Deep learning</td><td>Either</td><td>Image, speech and language recognition using multi-layer neural networks</td></tr>
</table></div>
<ul>
<li><b>Overfitting:</b> the model learns the training data too precisely, including its noise, and fails on new data.</li>
<li><b>Underfitting:</b> the model is too simple to capture the real pattern.</li>
<li>Models can also be "black boxes": accurate, but hard to explain.</li>
</ul>
<h3>Data science: handling the data</h3>
<ul>
<li><b>Capture:</b> how data are collected and put into a usable format.</li>
<li><b>Curation:</b> cleaning, checking quality, dealing with errors and missing values.</li>
<li><b>Storage:</b> how data are recorded, archived and accessed.</li>
<li><b>Search:</b> how specific information is located within the data.</li>
<li><b>Transfer:</b> how data move from source or storage to the analytical tool.</li>
<li><b>Visualization:</b> for structured data, tables and charts; for unstructured data, tools such as tag clouds and mind maps.</li>
</ul>
<h3>Text analytics and natural language processing</h3>
<ul>
<li><b>Text analytics</b> uses programs to extract information from large bodies of text or voice data, such as filings, earnings calls and news.</li>
<li><b>Natural language processing</b> interprets human language. Applications include translation, speech recognition and sentiment analysis, for example scoring the tone of analyst reports or central bank statements.</li>
</ul>""",
qs=[
 ["The three characteristics most commonly used to define Big Data are volume, velocity and:", ["value.", "variety.", "volatility."], 1, "Volume, velocity and variety describe the size, speed and range of formats of the data. Veracity is sometimes added as a fourth."],
 ["Which of the following is best described as unstructured data?", ["Daily closing prices of a share", "A company's quarterly balance sheet figures", "The text of posts about a company on social media"], 2, "Text has no predefined row-and-column format. Prices and financial statement figures are structured."],
 ["A machine learning model is trained on data in which each observation is labelled with the correct outcome. This approach is best described as:", ["deep learning.", "supervised learning.", "unsupervised learning."], 1, "Labelled training data define supervised learning. Unsupervised learning works without labels."],
 ["An algorithm is given unlabelled data on thousands of companies and asked to group similar companies together. This is an example of:", ["overfitting.", "supervised learning.", "unsupervised learning."], 2, "Finding structure such as clusters in unlabelled data is unsupervised learning."],
 ["A model that performs very well on its training data but poorly on new data is most likely:", ["overfit.", "underfit.", "unsupervised."], 0, "Overfitting means the model has learned the noise in the training set, so it does not generalize."],
 ["Satellite images of retail car parks used to estimate store sales are best described as:", ["traditional data.", "alternative data.", "structured data."], 1, "Sensor-generated data from non-traditional sources are alternative data, and images are unstructured."],
 ["In data science, the process of ensuring data quality by cleaning the data and dealing with errors and missing values is called:", ["capture.", "curation.", "transfer."], 1, "Curation covers cleaning and quality checks. Capture is collection, and transfer is moving data to where it is analysed."],
 ["Scoring the tone of company earnings call transcripts as positive or negative is most likely an application of:", ["a tag cloud.", "data curation.", "natural language processing."], 2, "Interpreting human language, including sentiment analysis of text and speech, is natural language processing."],
 ["Deep learning is best described as machine learning that uses:", ["only labelled data.", "neural networks with many layers.", "linear regression on large data sets."], 1, "Deep learning relies on multi-layer neural networks and can be applied to labelled or unlabelled data."],
 ["The data set used to assess how well a fitted machine learning model predicts on unseen data is the:", ["test sample.", "training sample.", "validation sample."], 0, "The training sample fits the model, the validation sample tunes it and the test sample evaluates out-of-sample performance."],
]))
