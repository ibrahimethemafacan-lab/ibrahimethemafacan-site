# CFA Level I · Fixed Income · additional exam-style questions, terms and notes.
# Original questions written to cover the concepts tested in exam-style question banks; no question text is reproduced.
import re as _re
EK = {}

EK["fe"] = dict(
notes="""<h3>More on bond features</h3>
<ul>
<li>A bond paying 2.5% of par every six months is a <b>5% semiannual</b> coupon bond.</li>
<li>The <b>indenture</b> contains the rights of bondholders: issuer, principal, coupon, maturity, source of repayment, collateral, credit enhancements and covenants. It does not include the credit rating or the identity of every bondholder.</li>
<li><b>Affirmative covenants</b> say what the issuer must do (pay taxes, maintain collateral and insurance). <b>Negative covenants</b> say what it must not do (sell assets, take on more debt, pay large dividends).</li>
<li>Money market securities have original maturities of one year or less.</li>
<li>A bond trades at a premium when its price is above par, which happens when its coupon exceeds the market yield.</li>
</ul>""",
qs=[
 ["A bond pays 2.5% of its par value every six months. It is a:", ["5% semiannual coupon bond.", "2.5% semiannual coupon bond.", "5% annual coupon bond."], 0, "Coupon rates are quoted annually."],
 ["A 7-year, 8% bond with semiannual coupons and €1,000 par pays each coupon of:", ["€40", "€80", "€560"], 0, "8% × 1,000 / 2."],
 ["A covenant requiring the issuer to keep insurance on pledged assets is a(n):", ["affirmative covenant.", "negative covenant.", "credit enhancement."], 0, "It requires an action."],
 ["A covenant that limits the issuer's ability to take on more debt is a(n):", ["negative covenant.", "affirmative covenant.", "external credit enhancement."], 0, "It prohibits an action."],
 ["The document that contains the overall rights of bondholders is the:", ["indenture.", "covenant.", "prospectus summary."], 0, "Covenants are part of the indenture."],
 ["A bond's indenture is least likely to specify the:", ["bond's credit rating.", "covenants.", "source of repayment."], 0, "Ratings come from rating agencies and can change."],
 ["A bond trades at a premium when its:", ["price is above par.", "yield is above its coupon.", "maturity is longer than ten years."], 0, "A coupon above the market yield pushes the price above par."],
 ["Which security is classified as a money market instrument?", ["A bond issued today that matures in nine months", "A ten-year bond with six months left", "A five-year floating-rate note"], 0, "Classification is based on original maturity."],
])

EK["fc"] = dict(
notes="""<h3>More on cash flow structures and options</h3>
<ul>
<li>Bullet: principal at maturity. Fully amortizing: equal payments. Partially amortizing: a <b>balloon</b> payment at maturity. A sinking fund retires part of the issue each year; it may allow retiring more than the minimum.</li>
<li>Embedded options: <b>call</b> (issuer), <b>put</b> (investor), <b>conversion</b> (investor). Callable bonds yield more than non-callable equivalents; putable bonds yield less. Higher volatility raises the value of both embedded options, so callable bond values fall and putable bond values rise.</li>
<li>Caps on floating-rate notes benefit the <b>issuer</b>; floors benefit the investor.</li>
<li>TIPS adjust the <b>principal</b> for inflation and pay a fixed coupon rate on the adjusted principal.</li>
<li>Internal credit enhancements: subordination, overcollateralization, excess spread. External: surety bonds, bank guarantees, letters of credit.</li>
<li>Eurobonds are issued outside the jurisdiction of the currency they are denominated in. A debenture in the US is unsecured.</li>
<li>Deferred coupon bonds pay nothing at first, then regular coupons. Step-up coupons rise on a set schedule.</li>
</ul>""",
qs=[
 ["Compared with an equivalent non-callable bond, a callable bond's yield is:", ["higher.", "lower.", "the same."], 0, "Investors are compensated for the issuer's option."],
 ["Compared with an equivalent non-putable bond, a putable bond's yield is:", ["lower.", "higher.", "the same."], 0, "Investors pay for the put by accepting a lower yield."],
 ["An increase in interest rate volatility will:", ["decrease the value of a callable bond and increase the value of a putable bond.", "increase the value of both.", "decrease the value of both."], 0, "Both embedded options become more valuable."],
 ["Which embedded option can be exercised by the issuer?", ["A call option", "A put option", "A conversion option"], 0, "Puts and conversions belong to investors."],
 ["Which feature of a floating-rate note benefits the issuer?", ["A cap", "A floor", "A put option"], 0, "A cap limits the coupon the issuer must pay."],
 ["US TIPS protect investors against inflation by adjusting the:", ["principal, with a fixed coupon rate.", "coupon rate, with a fixed principal.", "maturity date."], 0, "Coupons rise because they are paid on a larger principal."],
 ["Which is least likely an internal credit enhancement?", ["A surety bond from an insurer", "Overcollateralization", "Subordination"], 0, "Surety bonds come from third parties."],
 ["Which is least likely an external credit enhancement?", ["An excess spread account", "A letter of credit", "A bank guarantee"], 0, "Excess spread is internal to the structure."],
 ["A dollar-denominated bond issued by a Brazilian company to investors in Europe is best described as a:", ["Eurobond.", "domestic bond.", "foreign bond."], 0, "It is issued outside the jurisdiction of its currency."],
 ["A bond whose periodic payments are all equal and repay the principal in full is a(n):", ["fully amortizing bond.", "bullet bond.", "balloon bond."], 0, "Each payment includes interest and principal."],
 ["A bond that pays no coupons at first and then pays regular coupons is a:", ["deferred coupon bond.", "step-up bond.", "payment-in-kind bond."], 0, "Payment-in-kind bonds pay coupons in additional bonds."],
 ["A step-up coupon bond's coupon rate increases:", ["on a predetermined schedule.", "when a reference rate rises.", "when the issuer's rating falls."], 0, "Credit-linked coupons respond to ratings."],
 ["In the US, a debenture is:", ["an unsecured bond.", "a bond secured by specific assets.", "a short-term instrument."], 0, "It relies on the issuer's general credit."],
 ["Securitized bonds are most likely issued by:", ["special purpose entities.", "supranational entities.", "central banks."], 0, "The SPE holds the assets and issues the securities."],
 ["A company with a below-average credit rating can most likely reduce its borrowing cost by:", ["adding credit enhancements.", "issuing callable bonds.", "removing covenants."], 0, "Enhancements reduce credit risk for investors."],
])

EK["it"] = dict(
notes="""<h3>More on issuance, trading and indexes</h3>
<ul>
<li>A <b>private placement</b> sells an issue to a small group of qualified investors. A <b>shelf registration</b> allows a series of issues over time under one filing. Sovereigns usually issue by <b>auction</b>.</li>
<li>Bid-ask spreads reflect liquidity and, indirectly, credit quality: wide spreads suggest illiquid or lower-quality bonds.</li>
<li>Aggregate bond indexes have <b>higher turnover</b> than equity indexes because bonds mature and are issued continually; they include large weights in government bonds.</li>
<li>Classification by issuer: government, financial, non-financial corporate. Other classifications include credit quality, maturity, currency and geography.</li>
<li>Asset-backed commercial paper is a short-term (money market) security.</li>
<li>Central banks sell government securities to drain reserves and slow growth (open market operations).</li>
</ul>""",
qs=[
 ["A company wants to sell its first bond issue only to a small number of wealthy investors. It will most likely use a:", ["private placement.", "public auction.", "shelf registration."], 0, "Private placements are sold to qualified investors."],
 ["A CFO who plans to issue debt in several pieces over the next few years will most likely use a:", ["shelf registration.", "single underwritten offering.", "private placement."], 0, "One filing covers future issues."],
 ["Compared with equity indexes, aggregate bond indexes have:", ["higher turnover.", "lower turnover.", "the same turnover."], 0, "Bonds mature and new ones are issued constantly."],
 ["Which type of issuer most often issues bonds by auction?", ["Sovereign governments", "Corporations", "Municipalities"], 0, "Auctions are standard for government debt."],
 ["Classification of bonds by issuer most likely includes:", ["financial sector bonds.", "floating-rate bonds.", "money market securities."], 0, "The other two relate to coupon type and maturity."],
 ["The bid-ask spread on a bond most likely conveys information about:", ["both its liquidity and its credit quality.", "its liquidity only.", "its credit quality only."], 0, "Lower-quality bonds tend to trade less and with wider spreads."],
 ["Asset-backed commercial paper is best described as a(n):", ["short-term investment.", "intermediate-term investment.", "long-term investment."], 0, "Commercial paper has maturities under one year."],
 ["A dealer quotes a bond at 97.10 bid and 98.40 ask. The wide spread suggests the bond is most likely:", ["illiquid.", "a newly issued government bond.", "highly rated."], 0, "Active government bonds trade at very narrow spreads."],
 ["A purchase of an entire new bond issue by a single investor is most accurately described as a(n):", ["private placement.", "underwritten offering.", "auction."], 0, "Public offerings are distributed widely."],
 ["To slow economic growth, a central bank is most likely to:", ["sell government securities.", "buy government securities.", "lower reserve requirements."], 0, "Selling drains reserves."],
])

EK["ci"] = dict(
notes="""<h3>More on corporate funding markets</h3>
<ul>
<li>The <b>interbank market</b> is where banks lend excess reserves to each other; its rate is the interbank (or central bank funds) rate.</li>
<li>In a <b>repo</b>, the seller of securities borrows cash; in a reverse repo the dealer is the lender. Overnight repos usually have lower repo rates and margins than term repos. Higher-quality collateral and greater demand for the security lower the repo rate.</li>
<li>Investment-grade issuers benefit from standardized, frequent issuance (such as MTN programmes), which lowers rollover risk.</li>
<li>High-yield bonds have more restrictive covenants, such as limits on dividends and additional debt.</li>
<li>The credit spread forms a larger share of the total yield for high-yield bonds.</li>
<li>With an upward-sloping yield curve, longer maturities require higher yields.</li>
</ul>""",
qs=[
 ["The rate a bank pays to borrow excess reserves from another bank is best described as the:", ["interbank rate.", "discount rate.", "repo margin."], 0, "Interbank lending is unsecured, usually overnight."],
 ["Which covenant is most likely found in a high-yield bond issue?", ["A limit on dividend payments", "A requirement to pay a minimum dividend", "No restrictions on additional borrowing"], 0, "High-yield investors want to protect the cash flows that service their bonds."],
 ["The credit spread makes up 5% of Bond A's yield, 10% of Bond B's and 30% of Bond C's. Bond C is most likely:", ["a high-yield bond.", "an investment-grade bond.", "a government bond."], 0, "Credit risk dominates high-yield yields."],
 ["Compared with a term repo, an overnight repo most likely has a:", ["lower repo rate and lower margin.", "higher repo rate and higher margin.", "higher repo rate and lower margin."], 0, "Shorter terms carry less risk."],
 ["A repurchase agreement is described as a reverse repo when:", ["the dealer is the lender of cash.", "the dealer is the borrower of cash.", "it lasts longer than one year."], 0, "It is named from the dealer's point of view."],
 ["Which statement about repo rates is most accurate?", ["Greater demand for the underlying security lowers the repo rate.", "Longer terms lower the repo rate.", "Lower-quality collateral lowers the repo rate."], 0, "Lenders accept less interest for collateral they want."],
 ["In a normal, upward-sloping yield curve environment, compared with 5-year bonds, corporate issuers must offer on 20-year bonds:", ["higher yields.", "lower yields.", "the same yields."], 0, "Investors require a term premium."],
 ["Reduced rollover risk from standardized, regular issuance mainly benefits:", ["investment-grade corporate issuers.", "high-yield issuers.", "one-off issuers."], 0, "MTN programmes let investment-grade issuers stagger maturities."],
])

EK["gi"] = dict(
notes="""<h3>More on government issuance</h3>
<ul>
<li>Sovereign auctions: non-competitive bids are filled first at the auction price; competitive bids are then filled from the <b>lowest</b> yield upward. The <b>cutoff yield</b> is the highest accepted competitive yield. In a single-price auction, all successful bidders pay the price at the cutoff yield.</li>
<li>Primary dealers bid at auctions for themselves and clients, and are counterparties to the central bank's open market operations.</li>
<li>Sovereign yields can be lower than non-sovereign yields because of taxing power, liquidity and the ability to print currency.</li>
<li>Supranational issuers include the IMF and World Bank.</li>
<li>Classification by geography: developed, emerging and frontier markets.</li>
</ul>""",
qs=[
 ["Bonds issued by the International Monetary Fund are best described as:", ["supranational bonds.", "sovereign bonds.", "agency bonds."], 0, "They are issued by multilateral organizations."],
 ["In a sovereign bond auction, bonds are allocated first to:", ["non-competitive bidders.", "competitive bidders with the highest yields.", "primary dealers only."], 0, "Non-competitive bidders accept the auction yield."],
 ["The cutoff yield in a government bond auction is the:", ["highest yield among accepted competitive bids.", "lowest yield bid.", "average of all bids."], 0, "Bids above it are rejected."],
 ["In a single-price auction, all successful bidders pay the price that corresponds to the:", ["cutoff yield.", "lowest accepted yield.", "average yield bid."], 0, "This is why it is called single-price."],
 ["Bond classifications by geography most likely include:", ["emerging market bonds.", "municipal bonds.", "supranational bonds."], 0, "The other two are classifications by issuer."],
 ["Primary dealers most likely work with a central bank in carrying out:", ["open market operations.", "fiscal policy.", "bank supervision."], 0, "They buy and sell government securities with the central bank."],
 ["Sovereign bond yields may be lower than non-sovereign yields because sovereigns:", ["can raise taxes and issue currency.", "always have AAA ratings.", "issue only short-term debt."], 0, "These powers lower default risk on local-currency debt."],
])

EK["bv"] = dict(
notes="""<h3>More on bond valuation</h3>
<ul>
<li>If the coupon exceeds the yield, the price is above par; if the yield is unchanged, the price falls toward par over time (pull to par). A discount bond's price rises toward par.</li>
<li>For option-free bonds, prices change more for a yield decrease than for an equal increase (convexity); longer and lower-coupon bonds are more sensitive.</li>
<li>Full price = flat price + accrued interest. Corporate bonds usually use 30/360; government bonds actual/actual.</li>
<li>Matrix pricing estimates yields for non-traded bonds by interpolating yields of comparable bonds with similar credit quality and maturity.</li>
<li>For a discount bond, current yield &lt; YTM; for a premium bond, current yield &gt; YTM.</li>
</ul>""",
qs=[
 ["A 4-year bond pays an annual coupon of 5% and yields 6.5%. Its price per 100 of par is closest to:", ["94.86", "95.79", "105.14"], 0, "PV of 5, 5, 5, 105 at 6.5%."],
 ["A 10-year bond pays a 7% coupon semiannually and yields 5.5%. Its price per 100 is closest to:", ["88.93", "100.00", "111.42"], 2, "20 periods at 2.75%, coupons of 3.5."],
 ["A bond with a 12% annual coupon trades at 88% of par. Its yield to maturity is:", ["above 12%.", "below 12%.", "equal to 12%."], 0, "A discount price means the yield exceeds the coupon."],
 ["For an option-free bond, as its yield increases, its price:", ["decreases at a decreasing rate.", "decreases at an increasing rate.", "increases at a decreasing rate."], 0, "The price-yield curve is convex."],
 ["A bond's quoted price is 98.40 and accrued interest is 2.10 per 100. Its full price is:", ["96.30", "98.40", "100.50"], 2, "Full price = flat price + accrued interest."],
 ["Matrix pricing is used mainly for bonds that:", ["do not trade actively.", "trade on exchanges.", "have no credit risk."], 0, "Yields of comparable traded bonds are interpolated."],
 ["To calculate accrued interest on a corporate bond, a dealer most likely uses:", ["30-day months and a 360-day year.", "actual days and a 365-day year.", "actual days and a 360-day year."], 0, "30/360 is common for corporate bonds."],
 ["A premium bond is held while its yield stays constant. Over time, its price will:", ["fall toward par.", "rise further above par.", "stay the same."], 0, "This is the constant-yield price trajectory."],
 ["For a bond trading at a discount, the current yield is:", ["lower than the yield to maturity.", "higher than the yield to maturity.", "equal to the yield to maturity."], 0, "The YTM also includes the gain to par."],
 ["If its yield does not change, a zero-coupon bond's price will least likely:", ["stay constant over time.", "approach par value.", "rise each year."], 0, "Its price accretes toward par."],
 ["A 10-year zero-coupon bond has a par value of 1,000. With a yield of 7% on a semiannual basis, its price is closest to:", ["502.57", "508.35", "576.71"], 0, "1,000 / 1.035^20 = 502.57."],
 ["Compared with an increase in yield of the same size, a decrease in yield causes an option-free bond's price to change by:", ["a larger amount.", "a smaller amount.", "the same amount."], 0, "Positive convexity."],
])

EK["yf"] = dict(
notes="""<h3>More on yields and spreads</h3>
<p class="f">EAR = (1 + r/m)<sup>m</sup> − 1 · current yield = annual coupon / price</p>
<ul>
<li>Converting yields: a semiannual-bond-basis yield of 5.2% is (1.026)² − 1 = 5.27% annual-pay.</li>
<li>Yield to worst: the lowest of the yield to maturity and the yields to each call date.</li>
<li>G-spread: over the interpolated government yield. I-spread: over the swap rate. Both are theoretically correct only with a <b>flat</b> spot curve. Z-spread: constant spread added to each spot rate.</li>
<li>OAS = Z-spread − option cost. For a callable bond OAS &lt; Z-spread; for a putable bond OAS &gt; Z-spread.</li>
</ul>""",
qs=[
 ["An 8-year, 6% annual coupon bond is priced at 93.50. Its yield to maturity is closest to:", ["6.0%", "7.1%", "7.6%"], 1, "Solving for the rate gives about 7.09%."],
 ["A 10-year, 7% semiannual bond is priced at 104. Its yield to maturity (semiannual basis) is closest to:", ["6.45%", "7.00%", "7.55%"], 0, "Solving gives 3.23% per half-year, ×2 = 6.45%."],
 ["A bond with an 8% annual coupon is callable in four years at 104 and is priced at 106. Its yield to call is closest to:", ["6.5%", "7.1%", "8.0%"], 1, "Solving for the rate with a final value of 104 at Year 4 gives 7.12%."],
 ["A bond with a 6% coupon trades at 94. Its current yield is closest to:", ["5.6%", "6.0%", "6.4%"], 2, "6 / 94 = 6.38%."],
 ["A stated rate of 10% compounded quarterly gives an effective annual rate closest to:", ["10.00%", "10.25%", "10.38%"], 2, "1.025^4 − 1."],
 ["A semiannual-bond-basis yield of 5.2% is equivalent to an annual-pay yield closest to:", ["5.13%", "5.20%", "5.27%"], 2, "1.026² − 1 = 5.27%."],
 ["Other things equal, as the number of compounding periods increases, the effective annual rate:", ["increases.", "decreases.", "does not change."], 0, "Interest earns interest more often."],
 ["G-spreads and I-spreads are theoretically correct only if the spot curve is:", ["flat.", "upward sloping.", "inverted."], 0, "Otherwise a single benchmark yield misprices individual cash flows."],
 ["An I-spread is a yield spread over:", ["swap rates.", "government bond yields.", "spot rates."], 0, "The G-spread uses government yields."],
 ["The yield to worst is the:", ["lowest of the yield to maturity and all yields to call.", "highest possible yield.", "yield to the first call date only."], 0, "It is the most conservative yield measure."],
 ["For a callable bond, the option-adjusted spread is:", ["less than the Z-spread.", "greater than the Z-spread.", "equal to the Z-spread."], 0, "OAS removes the value of the call option, which the investor has sold."],
 ["A bond with a Z-spread of 120 bp and an option cost of 35 bp has an OAS of:", ["35 bp", "85 bp", "155 bp"], 1, "OAS = Z-spread − option cost."],
 ["The Z-spread is the constant spread that, added to each government spot rate, makes the:", ["present value of the bond's cash flows equal its price.", "yield equal the coupon.", "duration equal zero."], 0, "It accounts for the shape of the spot curve."],
])

EK["yr"] = dict(
notes="""<h3>More on floating-rate and money market yields</h3>
<ul>
<li>If the <b>discount margin</b> (required margin) exceeds the quoted margin, the FRN trades below par; if it is lower, above par. A deterioration in credit raises the required margin.</li>
<li>The quoted margin is fixed for the life of the note.</li>
<li>Bond-equivalent yield: an add-on yield on a 365-day year. Discount-basis instruments: price = FV × (1 − days/360 × DR).</li>
</ul>""",
qs=[
 ["If an FRN's discount margin is lower than its quoted margin, the note most likely trades:", ["above par.", "below par.", "at par."], 0, "Investors require less than the note pays."],
 ["An FRN whose quoted margin is lower than investors now require will trade:", ["below par.", "above par.", "at par."], 0, "The coupon is too low for its risk."],
 ["As an FRN approaches maturity with no change in credit quality, its quoted margin:", ["stays the same.", "rises.", "falls."], 0, "The quoted margin is set at issuance."],
 ["A 120-day pure discount note is bought for 985 and matures at 1,000. Its bond-equivalent yield is closest to:", ["4.5%", "4.6%", "4.7%"], 1, "(1000/985 − 1) × 365/120 = 4.63%."],
 ["A 1,000 note with 90 days to maturity is quoted at a discount rate of 2% on a 360-day basis. Its price is:", ["980", "995", "998"], 1, "1,000 × (1 − 0.02 × 90/360)."],
 ["A bond-equivalent yield for a money market instrument is a(n):", ["add-on yield based on a 365-day year.", "discount yield based on a 360-day year.", "add-on yield based on a 360-day year."], 0, "This allows comparison with bond yields."],
 ["An issuer whose credit quality improves after issuing an FRN will most likely see the note's price:", ["rise above par.", "fall below par.", "stay at par."], 0, "The required margin falls below the quoted margin."],
])

EK["ts"] = dict(
notes="""<h3>More on spot and forward rates</h3>
<p class="f">(1 + S<sub>n</sub>)<sup>n</sup> = (1 + S<sub>n−1</sub>)<sup>n−1</sup>(1 + F<sub>n−1,1</sub>)</p>
<ul>
<li>A spot curve is the yield curve for zero-coupon bonds. Bonds valued with spot rates have arbitrage-free values; discount each cash flow at its own spot rate.</li>
<li>If spot rates are rising, forward rates exceed spot rates; when the curve is flat, a single yield prices all bonds correctly.</li>
<li>The term structure of yield volatility relates yield volatility to <b>maturity</b>.</li>
<li>A coupon bond's YTM is a weighted average of the spot rates, closer to the rate at its maturity.</li>
</ul>""",
qs=[
 ["The one-year spot rate is 4% and the two-year spot rate is 5.5%. The one-year forward rate one year from now is closest to:", ["5.5%", "6.5%", "7.0%"], 2, "1.055² / 1.04 − 1 = 7.02%."],
 ["The three-year spot rate is 5% and the four-year spot rate is 6%. The one-year forward rate three years from now is closest to:", ["6.0%", "7.0%", "9.1%"], 2, "1.06^4 / 1.05^3 − 1 = 9.06%."],
 ["Spot rates are 4%, 5% and 5.5% for one, two and three years. A three-year bond with a 6% annual coupon is worth closest to:", ["100.00", "101.48", "102.20"], 1, "6/1.04 + 6/1.05² + 106/1.055³."],
 ["A spot rate curve shows the yields to maturity of:", ["zero-coupon bonds.", "coupon bonds trading at par.", "money market instruments."], 0, "The par curve shows coupon bonds at par."],
 ["To find the arbitrage-free value of a government bond, each cash flow should be discounted at the:", ["spot rate for its maturity.", "bond's yield to maturity.", "coupon rate."], 0, "Each cash flow is a zero-coupon bond."],
 ["If the yield curve is flat, the value of a bond calculated with spot rates will be:", ["equal to its value calculated with the YTM.", "higher than the YTM value.", "lower than the YTM value."], 0, "All spot rates equal the single yield."],
 ["The term structure of yield volatility shows the relationship between yield volatility and:", ["maturity.", "duration.", "credit rating."], 0, "Short-term yields are usually more volatile."],
 ["The three-year spot rate is 12.1% and the two-year spot rate is 11.3%. The one-year forward rate two years from now is:", ["above 12.1%.", "between 11.3% and 12.1%.", "below 11.3%."], 0, "Rising spot rates imply forward rates above them."],
 ["Bootstrapping is used to derive:", ["spot rates from par rates.", "par rates from forward rates only.", "credit spreads."], 0, "It extracts zero rates one maturity at a time."],
])

EK["rr"] = dict(
notes="""<h3>More on interest rate risk and return</h3>
<ul>
<li>Sources of return: coupons, reinvestment income and capital gains or losses (relative to the constant-yield price trajectory).</li>
<li>If yields fall after purchase: reinvestment income falls and the sale price rises. For a hold-to-maturity investor, only reinvestment risk matters; for a short-horizon investor, price risk dominates.</li>
<li><b>Duration gap</b> = Macaulay duration − investment horizon. A positive gap means price risk dominates (higher rates hurt); a negative gap means reinvestment risk dominates.</li>
<li>Matching Macaulay duration to the horizon makes the two risks offset for a parallel shift.</li>
<li>Bonds with lower coupons and shorter maturities have less reinvestment risk. A zero held to maturity has none.</li>
<li>The realized return equals the YTM only if coupons are reinvested at the YTM and the bond is held to maturity.</li>
</ul>""",
qs=[
 ["A 4-year, 6% annual-pay bond yields 7%. Its Macaulay duration is closest to:", ["3.43", "3.67", "4.00"], 1, "Weighted average time of the cash flows = 3.67 years."],
 ["For the bond above, modified duration is closest to:", ["3.43", "3.67", "3.92"], 0, "3.67 / 1.07 = 3.43."],
 ["An investor's horizon is 5 years and her bond's Macaulay duration is 7.2. Her duration gap is:", ["positive, so she is more exposed to price risk.", "negative, so she is more exposed to reinvestment risk.", "zero."], 0, "Duration exceeds the horizon."],
 ["Which bond characteristic most likely reduces reinvestment risk?", ["A lower coupon", "A longer maturity", "A call feature"], 0, "Smaller coupons mean less cash to reinvest."],
 ["If yields fall after purchase and the bond is held to maturity, the investor's realized return will be:", ["below the original yield to maturity.", "above the original yield.", "equal to the original yield."], 0, "Coupons are reinvested at lower rates."],
 ["Which duration measure should be matched to the investment horizon to offset reinvestment and price risk?", ["Macaulay duration", "Modified duration", "Effective duration"], 0, "Macaulay duration is measured in years."],
 ["Annual Macaulay duration is least accurately described as the:", ["approximate percentage price change for a 1% change in yield.", "weighted average time to receive the cash flows.", "horizon at which price and reinvestment risks offset."], 0, "That is modified duration."],
 ["In a Macaulay duration calculation, the weights for each cash flow are the:", ["share of the cash flow's present value in the bond's price.", "number of years to each payment.", "coupon rate."], 0, "Weights sum to one."],
 ["An investor whose bond's Macaulay duration is shorter than his horizon:", ["has a negative duration gap.", "has a positive duration gap.", "has no reinvestment risk."], 0, "He faces more reinvestment risk."],
 ["Can a zero-coupon bond held to maturity produce a capital gain or loss, assuming no default?", ["No, it returns par at maturity.", "Yes, if rates change.", "Yes, if inflation changes."], 0, "Its price follows the constant-yield path to par."],
])

EK["dm"] = dict(
notes="""<h3>More on duration</h3>
<p class="f">approximate ModDur = (PV<sub>−</sub> − PV<sub>+</sub>) / (2 × ΔYield × PV<sub>0</sub>) · money duration = ModDur × full price · PVBP = money duration × 0.0001</p>
<ul>
<li>Duration is higher for <b>longer maturities, lower coupons and lower yields</b>. Zero-coupon bonds have the most rate sensitivity for a given maturity; floaters the least.</li>
<li>Modified duration = Macaulay duration / (1 + yield per period), so it is always lower than Macaulay duration.</li>
<li>Duration underestimates price increases and overestimates price decreases for large yield changes, because it ignores convexity.</li>
<li>Call features reduce interest rate risk. When yields fall toward the coupon of a callable bond, its price rises little.</li>
<li>The money duration of a short instrument, like 360-day commercial paper, is roughly its maturity in years times its price.</li>
</ul>""",
qs=[
 ["A bond is priced at 100. If yields fall 50 bp its price rises to 103.9; if they rise 50 bp it falls to 96.3. Its approximate modified duration is:", ["3.8", "7.6", "15.2"], 1, "(103.9 − 96.3) / (2 × 0.005 × 100) = 7.6."],
 ["A $2 million position in a bond has a modified duration of 6.2. Its money duration is:", ["$124,000", "$1,240,000", "$12,400,000"], 2, "6.2 × 2,000,000."],
 ["For the position above, the price value of a basis point is closest to:", ["$124", "$1,240", "$12,400"], 1, "12,400,000 × 0.0001."],
 ["Which bond has the most interest rate risk?", ["24-year maturity, 5% coupon", "24-year maturity, 8% coupon", "8-year maturity, 5% coupon"], 0, "Longer maturity and lower coupon both increase duration."],
 ["Which five-year bond has the highest interest rate sensitivity?", ["A zero-coupon bond", "A floating-rate bond", "A 6% annual coupon bond"], 0, "All its value comes at maturity."],
 ["When rates rise, the modified duration of a 30-year discount bond:", ["decreases.", "increases.", "does not change."], 0, "Duration falls as yields rise."],
 ["Compared with its Macaulay duration, a bond's modified duration is:", ["lower.", "higher.", "the same."], 0, "It divides by (1 + yield per period)."],
 ["Holding other factors constant, a coupon bond's interest rate risk is higher when its:", ["yield is lower.", "coupon is higher.", "maturity is shorter."], 0, "Lower yields increase duration."],
 ["For large yield changes, using duration alone to estimate price changes:", ["understates price increases and overstates price decreases.", "is exact.", "overstates price increases."], 0, "Convexity adds to price in both directions."],
 ["All else equal, which is least likely to increase a bond's interest rate risk?", ["Adding a call feature", "A longer maturity", "A lower coupon"], 0, "A call caps price gains."],
 ["Compared with an otherwise identical option-free bond, a putable bond has:", ["less price volatility when rates rise.", "more price volatility when rates rise.", "the same volatility."], 0, "The put sets a floor on the price."],
])

EK["cv"] = dict(
notes="""<h3>More on convexity</h3>
<p class="f">%ΔP ≈ −ModDur × Δy + ½ × Convexity × (Δy)² · approximate convexity = (PV<sub>−</sub> + PV<sub>+</sub> − 2PV<sub>0</sub>) / ((Δy)² × PV<sub>0</sub>)</p>
<ul>
<li>Positive convexity adds to price for both increases and decreases in yield. Callable bonds show <b>negative convexity</b> at low yields, when the call is likely to be exercised.</li>
<li>Portfolio duration as a weighted average of bond durations is simple but assumes parallel shifts of the yield curve.</li>
<li>Money convexity = convexity × full price of the position.</li>
</ul>""",
qs=[
 ["Negative convexity is most likely observed in:", ["callable bonds at low yields.", "callable bonds at high yields.", "government zero-coupon bonds."], 0, "The call caps price gains when yields fall."],
 ["A bond is priced at 100. If yields fall 50 bp its price rises to 103.9; if they rise 50 bp it falls to 96.3. Its approximate convexity is:", ["40", "80", "160"], 1, "(103.9 + 96.3 − 200) / (0.005² × 100) = 80."],
 ["A bond has a modified duration of 7 and a convexity of 90. For a 100 bp rise in yield, its estimated price change is closest to:", ["−7.45%", "−7.00%", "−6.55%"], 2, "−7 × 0.01 + 0.5 × 90 × 0.0001 = −6.55%."],
 ["For the same bond, a 100 bp fall in yield gives an estimated price change closest to:", ["+6.55%", "+7.00%", "+7.45%"], 2, "+7% + 0.45%."],
 ["A portfolio holds 30% in bonds with a duration of 4, 50% with 7 and 20% with 10. Its duration is:", ["6.7", "7.0", "7.3"], 0, "0.3 × 4 + 0.5 × 7 + 0.2 × 10."],
 ["A limitation of portfolio duration calculated as a weighted average of bond durations is that it assumes:", ["parallel shifts of the yield curve.", "no convexity in any bond.", "equal weights."], 0, "Non-parallel moves affect bonds differently."],
 ["Adjusting for convexity improves price change estimates because:", ["the price-yield relationship is curved.", "duration measures credit risk.", "convexity removes reinvestment risk."], 0, "Duration is a linear approximation."],
 ["For a given yield change, the gap between the actual price change and the duration estimate is larger for a bond with:", ["more convexity.", "less convexity.", "a shorter maturity."], 0, "Convexity measures the curvature that duration ignores."],
])

EK["cr"] = dict(
notes="""<h3>More on curve-based and empirical measures</h3>
<ul>
<li><b>Effective duration</b> and convexity use prices from a model with shifts in the benchmark curve; they are appropriate for bonds with embedded options and for securities without well-defined cash flows (MBS).</li>
<li>A callable bond's effective duration is below its modified duration.</li>
<li><b>Key rate durations</b> measure sensitivity to a change at one maturity on the curve; they are used for non-parallel shifts (shaping risk).</li>
<li><b>Empirical duration</b> comes from historical regressions of bond returns on benchmark yield changes. For high-yield bonds it is often below analytical duration, because credit spreads fall when government yields rise. For government bonds the two should be similar.</li>
</ul>""",
qs=[
 ["A callable bond priced at 1,000 has an effective duration of 5 and a modified duration of 6. If yields rise 1%, its price will most likely fall by about:", ["$50", "$60", "$110"], 0, "Use effective duration for bonds with embedded options."],
 ["Key rate duration measures a bond's sensitivity to a change in:", ["the yield at a specific maturity.", "its own yield to maturity.", "its credit spread."], 0, "It captures non-parallel shifts."],
 ["Which measure is most appropriate when an analyst expects a non-parallel shift in the yield curve?", ["Key rate duration", "Effective duration", "Modified duration"], 0, "Effective duration assumes parallel shifts."],
 ["The approach to duration that relies on historical relationships between benchmark yield changes and bond prices is:", ["empirical duration.", "analytical duration.", "Macaulay duration."], 0, "It is estimated with regression."],
 ["The appropriate measure of interest rate sensitivity for a bond with an embedded option is:", ["effective duration.", "Macaulay duration.", "modified duration."], 0, "Cash flows depend on rates."],
 ["For a portfolio of short-term government bonds, empirical and analytical durations should be:", ["similar.", "very different.", "unrelated."], 0, "There is little credit spread effect."],
 ["A bond has a modified duration of 8 and convexity of 100. If yields fall 50 bp, its price change is closest to:", ["+3.88%", "+4.00%", "+4.13%"], 2, "8 × 0.005 + 0.5 × 100 × 0.000025 = 4.125%."],
 ["A bond is priced at 100. If the benchmark curve shifts down 25 bp, a model gives 101.2; up 25 bp, 98.9. Its effective duration is:", ["2.3", "4.6", "9.2"], 1, "(101.2 − 98.9) / (2 × 0.0025 × 100) = 4.6."],
])

EK["ck"] = dict(
notes="""<h3>More on credit risk</h3>
<p class="f">expected loss = probability of default × loss given default · LGD = 1 − recovery rate</p>
<ul>
<li>The four Cs: <b>capacity</b>, <b>capital</b>, <b>collateral</b>, <b>character</b>. Capacity covers industry structure and company fundamentals. Collateral analysis includes intangible assets, depreciation and market value of equity. Character covers management's strategy, integrity and past treatment of bondholders.</li>
<li>Credit spreads widen when the economy weakens, equity markets fall, uncertainty rises or supply of bonds is high; they narrow in expansions.</li>
<li>Expecting spreads to narrow (economic expansion), an investor favours lower-quality bonds; expecting them to widen, government bonds.</li>
<li>Market liquidity risk: receiving less than fair value when selling.</li>
</ul>""",
qs=[
 ["A bond has a 3% probability of default and an expected recovery rate of 40%. Its expected loss is:", ["1.2%", "1.8%", "3.0%"], 1, "3% × 60%."],
 ["The risk of receiving less than market value when selling a bond is:", ["market liquidity risk.", "loss severity.", "downgrade risk."], 0, "Wide bid-ask spreads reflect it."],
 ["Which of the four Cs includes analysis of industry structure and company fundamentals?", ["Capacity", "Capital", "Character"], 0, "Capacity is the ability to repay."],
 ["Management's integrity, strategy and past treatment of bondholders are part of the analysis of:", ["character.", "capacity.", "collateral."], 0, "Character concerns management."],
 ["A manager expecting an economic expansion would most likely:", ["increase holdings of lower-rated corporate bonds.", "move into government bonds.", "shorten duration and sell high-yield bonds."], 0, "Spreads tend to narrow in expansions."],
 ["An investor expecting the spread between Treasuries and corporate bonds to widen should most likely:", ["buy Treasuries and sell corporate bonds.", "buy corporate bonds.", "buy both equally."], 0, "Corporate bond prices will fall relative to Treasuries."],
 ["Loss severity is the:", ["portion of a bond's value lost if the issuer defaults.", "probability of default.", "spread over Treasuries."], 0, "It equals 1 − recovery rate."],
 ["Yield spreads tend to widen when equity markets are:", ["weak.", "strong.", "stable."], 0, "Risk aversion rises."],
 ["Spreads between AAA and B rated bonds are most likely to widen when:", ["investors expect more uncertainty.", "the economy is expanding.", "default rates are falling."], 0, "Lower-quality bonds suffer more."],
 ["When demand for bonds is high and supply is low, yield spreads are most likely to:", ["narrow.", "widen.", "stay unchanged."], 0, "Strong demand lowers required compensation."],
])

EK["cg"] = dict(
notes="""<h3>More on government credit</h3>
<ul>
<li>General obligation bonds are backed by the issuer's taxing power and usually have less credit risk than corporate bonds of the same rating. <b>Revenue bonds</b> are backed by the revenues of a project (a toll road) and carry more risk than GO bonds.</li>
<li>A municipal bond guarantee is insurance from a third party that payments will be made.</li>
<li>Sovereign analysis: institutional, economic, external, fiscal and monetary factors. A high interest-to-GDP ratio indicates weak fiscal flexibility.</li>
<li>Sovereigns can seldom be forced to pay; investors are concerned about the lack of legal recourse.</li>
</ul>""",
qs=[
 ["Compared with corporate bonds of the same rating, municipal general obligation bonds usually have less credit risk because they are backed by:", ["the issuer's taxing power.", "specific project revenues.", "federal government guarantees."], 0, "Taxes can be raised to service the debt."],
 ["A municipality issues bonds to build a toll road, repayable from tolls. These are best described as:", ["revenue bonds.", "general obligation bonds.", "sovereign bonds."], 0, "Repayment depends on the project's cash flows."],
 ["Compared with general obligation bonds, revenue bonds typically:", ["carry more credit risk.", "are backed by taxing power.", "carry less credit risk."], 0, "They rely on a single source of revenue."],
 ["A sovereign with a very high interest-to-GDP ratio most likely has:", ["weak fiscal flexibility.", "a strong external position.", "low credit risk."], 0, "A large share of output goes to interest."],
 ["An investor worries that if a government defaults, she will have little legal recourse. This concern relates mainly to:", ["sovereign credit risk.", "currency risk.", "liquidity risk."], 0, "Sovereigns are hard to force into repayment."],
 ["Which statement about municipal bonds is most accurate?", ["A bond guarantee is insurance from a third party.", "All municipal bonds are backed by taxes.", "Revenue bonds have no credit risk."], 0, "GO and revenue bonds differ in backing."],
])

EK["cc"] = dict(
notes="""<h3>More on corporate credit</h3>
<ul>
<li>Leverage: debt/EBITDA (lower is better), FFO/debt (higher is better). Coverage: EBITDA/interest. Higher net income lowers debt/EBITDA.</li>
<li>Issuer ratings (corporate family ratings) apply to senior unsecured debt; issue ratings can be <b>notched</b> up for secured debt or down for subordinated debt.</li>
<li>Priority: first lien, second lien, senior unsecured, senior subordinated, subordinated, junior subordinated. Recovery rates are highest for the highest priority.</li>
<li><b>Structural subordination</b>: debt of a parent ranks behind the subsidiary's own creditors for the subsidiary's cash flows.</li>
<li>Investment-grade unsecured bonds have few covenants (negative pledge, change of control). High-yield bonds have more (limits on debt, dividends, asset sales).</li>
<li>Issuing debt to buy back shares raises leverage and probability of default.</li>
</ul>""",
qs=[
 ["An increase in net income is most likely to decrease a borrower's:", ["debt-to-EBITDA ratio.", "FFO-to-debt ratio.", "interest coverage."], 0, "Higher earnings lower leverage."],
 ["Structural subordination means that a parent company's debt:", ["ranks behind the subsidiary's creditors for the subsidiary's cash flows.", "ranks ahead of the subsidiary's creditors.", "is secured by the subsidiary's assets."], 0, "The subsidiary pays its own creditors first."],
 ["Debt with lower priority than a firm's senior unsecured debt is:", ["subordinated debt.", "second lien debt.", "pari passu debt."], 0, "Second lien is secured and ranks higher."],
 ["Recovery rates are typically highest for:", ["first lien debt.", "senior unsecured debt.", "subordinated debt."], 0, "Higher priority means more is recovered."],
 ["A company issues high-yield bonds to buy back shares. The most likely effect on its credit risk is:", ["higher probability of default.", "lower probability of default.", "no change."], 0, "Leverage rises and equity cushion falls."],
 ["Which bond has the lowest priority of repayment from the same issuer?", ["Senior subordinated debt", "Senior unsecured debt", "Second lien debt"], 0, "Subordinated ranks below unsecured."],
 ["An issuer credit rating, compared with an issue credit rating, applies to the issuer's:", ["senior unsecured debt.", "secured debt only.", "subordinated debt."], 0, "Issue ratings are notched from it."],
 ["The covenants of unsecured investment-grade bonds most likely include a:", ["change of control provision.", "strict limit on dividends.", "limit on all capital spending."], 0, "Investment-grade covenants are light."],
 ["A secured bond is rated above the issuer's corporate family rating. This is an example of:", ["notching.", "structural subordination.", "cross-default."], 0, "Collateral improves expected recovery."],
])

EK["sc"] = dict(
notes="""<h3>More on securitization</h3>
<ul>
<li>Benefits: removes loans from the seller's balance sheet, frees capital for new lending, improves liquidity of loans, gives investors access to diversified pools and can lower funding costs.</li>
<li>Securitization does not improve the collectability of the underlying loans.</li>
<li>The SPE is legally <b>independent</b> of the seller (bankruptcy remote), which is why ABS can be rated above the seller's own bonds.</li>
<li>Total cash flows to ABS investors equal the pool's interest and principal less servicing and other fees.</li>
</ul>""",
qs=[
 ["Asset-backed securities may have a higher rating than the seller's own bonds because:", ["the SPE is legally separate from the seller.", "ABS are always government guaranteed.", "the seller guarantees the ABS."], 0, "Seller bankruptcy does not affect the assets in the SPE."],
 ["The special purpose entity in a securitization is:", ["independent of the seller.", "a subsidiary that shares the seller's credit risk.", "the servicer."], 0, "It is bankruptcy remote."],
 ["Which is least likely a benefit of securitization?", ["Improving the collectability of the loans", "Freeing capital for new lending", "Increasing liquidity for loans"], 0, "The loans themselves do not change."],
 ["Total cash flows to investors in an ABS issue equal:", ["the pool's interest and principal less fees.", "the pool's interest only.", "the seller's net income."], 0, "Servicing and other fees are deducted."],
 ["One primary benefit of securitization to the financial system is that it:", ["increases liquidity for mortgages and other loans.", "eliminates credit risk.", "raises borrowing costs."], 0, "Loans become tradable securities."],
])

EK["ab"] = dict(
notes="""<h3>More on ABS and covered bonds</h3>
<ul>
<li>Credit tranching (senior/subordinated) redistributes credit risk; time tranching redistributes prepayment risk. In a <b>waterfall</b>, senior tranches are paid first.</li>
<li>Credit card ABS are non-amortizing with a <b>lockout period</b> during which principal is reinvested. Some auto loan ABS have credit enhancement; most do.</li>
<li>Covered bonds remain on the issuer's balance sheet with <b>dual recourse</b> to the issuer and the cover pool. Hard-bullet: default if a scheduled payment is missed. Soft-bullet: maturity may be extended (usually up to a year).</li>
<li>CDOs have a <b>collateral manager</b> who buys and sells assets. Synthetic CDOs are backed by credit default swaps. A CDO backed by RMBS is a structured finance CDO.</li>
<li>Equity tranche value = collateral value − value of the debt tranches.</li>
</ul>""",
qs=[
 ["An ABS with a senior/subordinated structure is said to have:", ["credit tranching.", "time tranching.", "prepayment tranching."], 0, "Losses fall first on subordinated tranches."],
 ["Which type of ABS typically has a lockout period?", ["Credit card ABS", "Auto loan ABS", "Residential mortgage pass-throughs"], 0, "Principal is reinvested during the lockout."],
 ["A covered bond whose maturity can be extended by up to a year to avoid default is a:", ["soft-bullet covered bond.", "hard-bullet covered bond.", "conditional pass-through bond."], 0, "Hard-bullet bonds default on a missed payment."],
 ["Compared with equivalent ABS, covered bonds offer:", ["recourse to the issuing institution.", "lower credit quality.", "no collateral."], 0, "Investors have a claim on both the issuer and the cover pool."],
 ["In contrast with most ABS, a CDO:", ["employs a collateral manager.", "has no tranches.", "is always government guaranteed."], 0, "The manager actively trades the collateral."],
 ["A synthetic CDO is backed by a pool of:", ["credit default swaps.", "leveraged loans.", "mortgages."], 0, "It takes credit exposure through derivatives."],
 ["An ABS structure has collateral worth $500 million and debt tranches worth $430 million. The equity tranche is worth:", ["$70 million", "$430 million", "$930 million"], 0, "500 − 430."],
 ["Under a waterfall structure:", ["senior tranches are paid before junior tranches.", "all tranches share payments pro rata.", "equity is paid first."], 0, "Payments flow down by priority."],
])

EK["mb"] = dict(
notes="""<h3>More on MBS</h3>
<ul>
<li>The pass-through rate is below the mortgage rate by the servicing and guarantee fees.</li>
<li>Prepayment speed: higher PSA means faster prepayment and a shorter weighted average life. At 50 PSA, the WAL is longer than at 100 PSA but shorter than the weighted average maturity.</li>
<li><b>Contraction risk</b>: rates fall, prepayments speed up. <b>Extension risk</b>: rates rise, prepayments slow down; it is greatest when a PAC's support tranche is exhausted.</li>
<li>Support tranches absorb prepayment variability; they offer higher yields in return.</li>
<li>CMBS loans are <b>non-recourse</b> and offer call protection at the loan level (prepayment lockouts, defeasance, penalties) and the structure level (sequential tranches).</li>
<li>CMBS credit ratios: debt service coverage (higher is better) and loan-to-value (lower is better).</li>
<li>Strategic default is most likely with non-recourse loans. Lenders prefer loans with prepayment penalties.</li>
</ul>""",
qs=[
 ["An MBS has a pass-through rate of 4.3% while the mortgages in its pool average 4.5%. The difference is most likely due to:", ["servicing and guarantee fees.", "prepayments.", "defaults."], 0, "Fees are deducted from the mortgage interest."],
 ["An investor concerned about extension risk but willing to accept contraction risk should most appropriately buy a:", ["short-maturity sequential tranche.", "long-maturity sequential tranche.", "support tranche."], 0, "Short tranches are repaid first, limiting extension."],
 ["Extension in an agency RMBS is most likely to result from:", ["a rise in interest rates.", "a fall in interest rates.", "a rise in home prices."], 0, "Borrowers are less likely to refinance."],
 ["An agency RMBS pool prepaying at 50 PSA will have a weighted average life that is:", ["longer than at 100 PSA.", "shorter than at 100 PSA.", "equal to its weighted average maturity."], 0, "Slower prepayments extend the WAL."],
 ["Strategic default by a mortgage borrower is most likely if the loan is:", ["non-recourse.", "recourse.", "fully amortizing."], 0, "The lender can only take the property."],
 ["The pool of loans backing a commercial MBS consists of:", ["non-recourse loans.", "recourse loans only.", "a mix of recourse and non-recourse loans."], 0, "Lenders rely on the property's cash flows."],
 ["In a CMBS, an example of structure-level call protection is:", ["sequential-pay tranches.", "a prepayment lockout.", "defeasance."], 0, "The other two are loan-level protections."],
 ["The main reason to invest in a PAC CMO's support tranche rather than the PAC tranche is its:", ["higher yield.", "lower prepayment risk.", "shorter expected life."], 0, "It is paid for absorbing prepayment variability."],
 ["The annualized rate of prepayments on a mortgage pool is its:", ["conditional prepayment rate.", "single monthly mortality rate.", "PSA benchmark."], 0, "SMM is monthly."],
 ["In evaluating loans backing a CMBS, which ratio indicates lower credit risk when it is higher?", ["Debt service coverage ratio", "Loan-to-value ratio", "Prepayment rate"], 0, "Higher NOI relative to debt service is safer."],
])

# Sayı içermeyen sorularda doğru şıkları sırayla A/B/C'ye dağıt.
_n = 0
for _e in EK.values():
    for _q in _e.get("qs", []):
        if any(_re.search(r"\d", _x) for _x in _q[1]): continue
        _j = _n % 3; _o = _q[1]; _i = _q[2]
        _o[_i], _o[_j] = _o[_j], _o[_i]; _q[2] = _j; _n += 1
