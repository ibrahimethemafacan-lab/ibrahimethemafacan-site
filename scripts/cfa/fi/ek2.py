import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}

# --- fe: Fixed-Income Instrument Features ---
EK["fe"] = G(
    [("A bond has a par value of 1,000, a 5% annual coupon rate paid semiannually and trades at 950. What is each coupon payment, and what is the current yield?",
      f"coupon payment = 1,000 × 5% / 2 = {1000*.05/2:.2f}|current yield = annual coupon / price = 50 / 950 = {50/950*100:.2f}%",
      "The coupon rate is applied to par, not to the price. Because the bond trades below par, its current yield is above its coupon rate.")],
    (["Term", "What it is"], [
        ["Indenture", "The whole legal contract between issuer and bondholders"],
        ["Covenant", "One promise inside the indenture"],
        ["Affirmative covenant", "Something the issuer must do: pay on time, maintain assets, file reports"],
        ["Negative covenant", "Something the issuer must not do: add debt, pledge assets, pay large dividends"],
        ["Pari passu clause", "The bond ranks equally with the issuer's other senior debt"],
        ["Cross-default clause", "A default on another obligation triggers a default on this bond"]]),
    "Expect a short description of a clause and the question \"this is best described as\". Negative covenants restrict actions and are the costlier kind for the issuer; affirmative covenants are administrative. Also expect the link between coupon, yield and price: coupon below yield means a discount bond.")

# --- fc: Fixed-Income Cash Flows and Types ---
_pmt = 1000 * .06 / (1 - 1.06 ** -3)
EK["fc"] = G(
    [("A 1,000 loan at 6% is fully amortizing over three annual payments. What is the payment, and how much of the first payment is principal?",
      f"payment = 1,000 × 0.06 / (1 − 1.06<sup>−3</sup>) = {_pmt:.2f}|interest in year 1 = 1,000 × 6% = 60.00|principal in year 1 = {_pmt:.2f} − 60.00 = {_pmt-60:.2f}",
      "The payment is level, but the interest part falls and the principal part rises each year."),
     ("A convertible bond has a conversion ratio of 25 shares and the share price is 38. What is the conversion value?",
      f"conversion value = 25 × 38 = {25*38}",
      "If the bond trades at 1,020, it is worth more as a bond than as shares; conversion is not yet attractive.")],
    (["Structure", "Principal repaid", "Key point"], [
        ["Bullet", "All at maturity", "Highest credit exposure at the end"],
        ["Fully amortizing", "Gradually, level payments", "Nothing left at maturity"],
        ["Partially amortizing", "Partly over life, balloon at maturity", "Balloon payment remains"],
        ["Callable", "Issuer may redeem early", "Favors the issuer: higher yield, lower price than a straight bond"],
        ["Putable", "Holder may sell back early", "Favors the holder: lower yield, higher price than a straight bond"]]),
    "Questions name a feature and ask who benefits, or how the bond's yield compares with an otherwise identical straight bond. Callable means the investor is short an option; putable and convertible mean the investor is long one. Amortization questions ask for the interest or principal part of a given payment.")

# --- it: Fixed-Income Issuance and Trading ---
EK["it"] = G(
    [("A dealer quotes a corporate bond at 99.50 bid and 99.70 ask. An investor buys 1,000,000 par and sells it back immediately. What does the round trip cost?",
      f"buy at ask: 1,000,000 × 99.70% = {n(997000,0)}|sell at bid: 1,000,000 × 99.50% = {n(995000,0)}|cost = {n(2000,0)} (0.20 per 100 of par)",
      "The bid–ask spread is the dealer's compensation and the investor's cost of liquidity. Wider spreads signal a less liquid bond.")],
    (["Pair", "Difference"], [
        ["Primary vs secondary market", "Primary: issuer sells new bonds and receives the money. Secondary: investors trade existing bonds"],
        ["Underwritten vs best-efforts offering", "Underwritten: the bank buys the issue and bears the risk of unsold bonds. Best efforts: the bank only acts as agent"],
        ["Public offering vs private placement", "Private placement goes to a few qualified investors, with less disclosure and less liquidity"],
        ["Shelf registration", "One master registration, then several issues over time without a new prospectus each time"],
        ["On-the-run vs off-the-run", "The most recently issued government bond of a maturity vs older issues; on-the-run is more liquid"]]),
    "Typical questions describe an issuance method and ask you to name it, or ask who bears the risk that the issue does not sell. Remember that most bonds trade over the counter through dealers, not on exchanges, and that settlement for corporates is typically later than for governments.")

# --- ci: Fixed-Income Markets for Corporate Issuers ---
_loan = 10_000_000 * (1 - .02); _int = _loan * .04 * 30 / 360
EK["ci"] = G(
    [("A dealer finances a bond worth 10,000,000 in a 30-day repo. The haircut is 2% and the repo rate is 4% (actual/360). How much is borrowed, and what is the repurchase price?",
      f"cash borrowed = 10,000,000 × (1 − 2%) = {n(_loan,0)}|interest = {n(_loan,0)} × 4% × 30/360 = {n(_int)}|repurchase price = {n(_loan+_int)}",
      "The haircut protects the cash lender if the collateral loses value. A higher repo rate goes with a longer term, weaker collateral, or a weaker borrower.")],
    (["Pair", "Difference"], [
        ["Repo vs reverse repo", "The same trade seen from two sides: the security seller borrows cash (repo); the cash lender does a reverse repo"],
        ["Commercial paper vs bank line", "CP is short-term unsecured market borrowing; a backup line of credit covers rollover risk"],
        ["Investment grade vs high yield issuance", "High yield issues carry more restrictive covenants, are more often secured, and behave more like equity"],
        ["Bilateral vs syndicated loan", "One lender vs a group of lenders sharing one loan"],
        ["General collateral vs special", "Special: a specific bond is in demand, so cash is lent against it at a lower repo rate"]]),
    "Calculation questions ask for the cash lent or the repurchase price, almost always on an actual/360 basis. Concept questions ask what raises the repo rate or the haircut, and which risk commercial paper issuers face: rollover risk.")

# --- gi: Fixed-Income Markets for Government Issuers ---
EK["gi"] = G(
    [("A treasury auctions 100 million of bonds. Competitive bids: 40 million at 4.00%, 50 million at 4.05%, 30 million at 4.10%. What do bidders pay in a single-price auction and in a multiple-price auction?",
      f"filled: 40 + 50 = 90 million; the last 10 million comes from the 4.10% bids|stop yield = 4.10%; bidders at 4.10% receive 10 of 30 = {10/30*100:.1f}% of their bid|single price: every winner receives 4.10%|multiple price: winners receive 4.00%, 4.05% and 4.10% respectively",
      "In a single-price auction all winners get the same (highest accepted) yield, which encourages aggressive bidding and tends to lower the government's cost.")],
    (["Issuer", "Repayment relies on"], [
        ["Sovereign", "Taxing power and, for local-currency debt, the ability to create money"],
        ["Non-sovereign (regional, municipal)", "Local taxes, or the cash flows of a specific project"],
        ["Quasi-government (agency)", "Own cash flows, often with an explicit or implicit government guarantee"],
        ["Supranational", "Capital and guarantees of member states (for example, development banks)"]]),
    "Questions contrast local-currency with foreign-currency sovereign debt: default risk is higher in foreign currency because the government cannot print it. Others ask you to identify the auction type from a description, or to pick the most liquid issue: the on-the-run benchmark.")

# --- bv: Bond Valuation: Prices and Yields ---
_p = 5/1.06 + 5/1.06**2 + 105/1.06**3
EK["bv"] = G(
    [("A three-year bond pays a 5% annual coupon. The market discount rate is 6%. What is the price per 100 of par?",
      f"PV = 5/1.06 + 5/1.06<sup>2</sup> + 105/1.06<sup>3</sup>|= {5/1.06:.3f} + {5/1.06**2:.3f} + {105/1.06**3:.3f} = {_p:.3f}",
      "The coupon rate is below the market rate, so the bond trades at a discount."),
     ("A 6% semiannual bond is settled 60 days into a 180-day coupon period. The flat price is 98.40. What is the full price?",
      f"accrued interest = 3.00 × 60/180 = {3*60/180:.2f}|full price = flat price + accrued interest = 98.40 + 1.00 = {98.40+1:.2f}",
      "The buyer pays the full price. The flat price is what dealers quote, so that the quote does not jump on coupon dates.")],
    (["Pair", "Difference"], [
        ["Full (dirty) price vs flat (clean) price", "Full includes accrued interest and is the amount paid; flat is the quoted price"],
        ["Coupon rate vs yield to maturity", "Coupon fixes the cash flows; YTM is the single rate that discounts them to the price"],
        ["Premium vs discount", "Coupon above YTM: price above par. Coupon below YTM: price below par"],
        ["Matrix pricing", "Estimating the yield of an illiquid bond from comparable bonds, usually by interpolating between maturities"]]),
    "You will be asked to price a bond from a yield, or to say whether it trades at a premium or discount without calculating. Know the four relationships: price moves inversely to yield; the relationship is convex; lower coupons and longer maturities mean greater price sensitivity; and a bond's price is pulled to par as maturity approaches.")

# --- yf: Yield and Yield Spread Measures for Fixed-Rate Bonds ---
_q = 4 * (1.03 ** .5 - 1)
EK["yf"] = G(
    [("A bond's yield to maturity is 6.00% on a semiannual bond basis. What is the effective annual yield, and what is the equivalent yield with quarterly periodicity?",
      f"effective annual yield = 1.03<sup>2</sup> − 1 = {(1.03**2-1)*100:.2f}%|quarterly periodicity = 4 × (1.03<sup>1/2</sup> − 1) = {_q*100:.3f}%",
      "More compounding periods per year means a lower stated annual rate for the same effective yield. Compare bonds only after putting their yields on the same periodicity.")],
    (["Spread", "Measured over", "Use"], [
        ["G-spread", "Government bond yield (interpolated)", "Simple benchmark spread"],
        ["I-spread", "Swap rate of the same maturity", "Common for bonds priced against swaps"],
        ["Z-spread", "Whole spot curve; a constant added to each spot rate", "Accounts for the shape of the curve"],
        ["Option-adjusted spread", "Z-spread minus the value of the embedded option", "Comparing callable with option-free bonds"]]),
    "Periodicity conversions and yield-to-call calculations are standard. For spreads, the usual trap is the callable bond: its OAS is smaller than its Z-spread, because part of the Z-spread pays the investor for the call option, not for credit and liquidity risk. Yield to worst is the lowest of the yield to maturity and all yields to call.")

# --- yr: Floating-Rate Instruments ---
_c = (3.00 + .80) / 2; _d = (3.00 + 1.20) / 200
_pf = sum(_c / (1 + _d) ** t for t in range(1, 5)) + 100 / (1 + _d) ** 4
_tb = 100 * (1 - .04 * 90 / 360)
EK["yr"] = G(
    [("A two-year floating-rate note pays MRR + 0.80% semiannually. MRR is 3.00% and investors require a margin of 1.20%. What is the price per 100?",
      f"coupon per period = (3.00% + 0.80%) / 2 × 100 = {_c:.2f}|discount rate per period = (3.00% + 1.20%) / 2 = {_d*100:.2f}%|price = PV of four payments of {_c:.2f} plus 100 at {_d*100:.2f}% = {_pf:.3f}",
      "The quoted margin is below the required (discount) margin, so the note trades below par. If the two were equal, it would be priced at par on each reset date."),
     ("A 90-day Treasury bill is quoted at a discount rate of 4.00% (360-day year). What are its price and its bond-equivalent yield (365-day add-on)?",
      f"price = 100 × (1 − 4% × 90/360) = {_tb:.2f}|bond-equivalent yield = (365/90) × (100 − {_tb:.2f}) / {_tb:.2f} = {365/90*(100-_tb)/_tb*100:.3f}%",
      "A discount rate understates the investor's return because it divides by face value, not by the amount invested.")],
    (["Pair", "Difference"], [
        ["Quoted margin vs discount margin", "Quoted margin is fixed in the contract and sets the coupon; discount (required) margin is what the market demands today"],
        ["Discount rate vs add-on rate", "Discount rate: interest as a share of face value. Add-on rate: interest as a share of the price paid"],
        ["360-day vs 365-day basis", "Money market quotes differ by convention; convert before comparing"],
        ["FRN vs fixed-rate bond", "An FRN has little interest rate risk because its coupon resets; its price changes mainly with credit risk"]]),
    "Expect \"is the FRN at a premium, at par or at a discount\" given the two margins, and conversions between discount-rate and add-on quotes. A credit downgrade raises the required margin and pushes an FRN below par even though market rates did not move.")

# --- ts: Term Structure ---
_f = 1.04 ** 2 / 1.03 - 1
EK["ts"] = G(
    [("The one-year spot rate is 3% and the two-year spot rate is 4%. What is the one-year forward rate one year from now (1y1y)?",
      f"(1 + S<sub>2</sub>)<sup>2</sup> = (1 + S<sub>1</sub>) × (1 + 1y1y)|1y1y = 1.04<sup>2</sup> / 1.03 − 1 = {_f*100:.2f}%",
      "The forward rate is the break-even rate: an investor is indifferent between two years at 4% and one year at 3% followed by one year at about 5.01%."),
     ("Using the same spot rates, price a two-year 5% annual coupon bond.",
      f"price = 5/1.03 + 105/1.04<sup>2</sup> = {5/1.03:.3f} + {105/1.04**2:.3f} = {5/1.03+105/1.04**2:.3f}",
      "Each cash flow is discounted at the spot rate for its own date. This is the no-arbitrage price.")],
    (["Curve", "What each point is"], [
        ["Spot curve", "Yield on a zero-coupon bond for that maturity"],
        ["Par curve", "Coupon rate that makes a bond of that maturity price at par"],
        ["Forward curve", "Rate agreed today for a loan starting in the future"],
        ["\"2y1y\" notation", "Starts in two years, lasts one year: the first number is when it starts, the second is the tenor"]]),
    "Forward-rate calculations from two spot rates are the core item. Also know the ordering: when the spot curve slopes upward, the forward curve lies above it and the par curve lies slightly below it; when it slopes downward, the order reverses.")

# --- rr: Interest Rate Risk and Return ---
_a = 6 * 1.06 + 106; _b = 6 * 1.04 + 106
EK["rr"] = G(
    [("An investor buys a two-year 6% annual coupon bond at par and holds it to maturity. What is the realized return if the coupon is reinvested at 6%, and if it is reinvested at 4%?",
      f"reinvest at 6%: future value = 6 × 1.06 + 106 = {_a:.2f}; return = ({_a:.2f}/100)<sup>1/2</sup> − 1 = {((_a/100)**.5-1)*100:.2f}%|reinvest at 4%: future value = 6 × 1.04 + 106 = {_b:.2f}; return = ({_b:.2f}/100)<sup>1/2</sup> − 1 = {((_b/100)**.5-1)*100:.2f}%",
      "The yield to maturity is earned only if coupons are reinvested at that same yield. A hold-to-maturity investor faces reinvestment risk, not price risk.")],
    (["Situation", "Dominant risk", "Hurt by"], [
        ["Horizon shorter than Macaulay duration (positive duration gap)", "Price risk", "Rising rates"],
        ["Horizon longer than Macaulay duration (negative gap)", "Reinvestment risk", "Falling rates"],
        ["Horizon equal to Macaulay duration", "The two offset", "Neither, for a one-time parallel shift"]]),
    "Questions give a horizon and a duration and ask which risk dominates. Duration gap = Macaulay duration − investment horizon. Another favorite: a capital gain or loss is measured against the bond's carrying value on the constant-yield price trajectory, not against the purchase price.")

# --- dm: Duration ---
_md = 7.2 / 1.05
EK["dm"] = G(
    [("A bond has a Macaulay duration of 7.2 and a yield to maturity of 5% (annual pay). The full price is 102.50. Estimate the price change if the yield rises by 50 basis points, and find the price value of a basis point.",
      f"modified duration = 7.2 / 1.05 = {_md:.3f}|% price change ≈ −{_md:.3f} × 0.50% = {-_md*.5:.2f}%|money duration = {_md:.3f} × 102.50 = {_md*102.5:.2f}|PVBP = {_md*102.5:.2f} × 0.0001 = {_md*102.5*.0001:.4f} per 100 of par",
      "For a semiannual bond, divide Macaulay duration by (1 + yield per period)."),
     ("A bond is priced at 100.00. If its yield falls by 5 bp the price is 100.40; if the yield rises by 5 bp it is 99.61. What is the approximate modified duration?",
      f"(PV<sub>−</sub> − PV<sub>+</sub>) / (2 × Δy × PV<sub>0</sub>) = (100.40 − 99.61) / (2 × 0.0005 × 100) = {(100.40-99.61)/(2*.0005*100):.2f}", "")],
    (["Measure", "Unit", "Answers"], [
        ["Macaulay duration", "Years", "Weighted average time to receive the cash flows"],
        ["Modified duration", "% per 1% of yield", "Percentage price change for a change in yield"],
        ["Money duration", "Currency", "Price change in currency for a 1% change in yield"],
        ["PVBP", "Currency", "Price change for one basis point"]]),
    "Besides the calculations, expect \"which bond has the highest duration\". Duration is higher with longer maturity, lower coupon and lower yield. A zero-coupon bond's Macaulay duration equals its maturity. A floating-rate note's duration is roughly the time to its next reset.")

# --- cv: Convexity ---
EK["cv"] = G(
    [("A bond has a modified duration of 8 and convexity of 90. Estimate the percentage price change if its yield rises by 100 basis points.",
      f"duration effect = −8 × 0.01 = {-8*.01*100:.2f}%|convexity adjustment = ½ × 90 × 0.01<sup>2</sup> = +{.5*90*.0001*100:.2f}%|total ≈ {(-8*.01+.5*90*.0001)*100:.2f}%",
      "The convexity adjustment is positive whether yields rise or fall. For a 100 bp fall the estimate is +8.00% + 0.45% = +8.45%."),
     ("A portfolio holds 60% in a bond with duration 4 and 40% in a bond with duration 9. What is the portfolio duration?",
      f"0.60 × 4 + 0.40 × 9 = {.6*4+.4*9:.1f}",
      "Weights are market values. This weighted average assumes a parallel shift of the yield curve.")],
    (["Pair", "Difference"], [
        ["Duration vs convexity", "Duration is the straight-line (first-order) estimate; convexity corrects for the curve in the price–yield relationship"],
        ["Positive vs negative convexity", "Option-free bonds are always positively convex. Callable bonds become negatively convex when yields are low, because the call caps the price"],
        ["More vs less convex bond", "With equal duration, the more convex bond gains more when yields fall and loses less when they rise, so it is priced richer"]]),
    "The standard item is the two-term price change. Do not forget the ½ and remember to square the yield change in decimals. Conceptual items ask which bond benefits most from large rate moves (the more convex one) and why a callable bond's price rises less when rates fall.")

# --- cr: Curve-Based and Empirical Measures ---
_ed = (102.90 - 99.30) / (2 * .0025 * 101.20)
EK["cr"] = G(
    [("A callable bond is priced at 101.20. A model gives 102.90 if the benchmark curve shifts down 25 bp and 99.30 if it shifts up 25 bp. What is the effective duration?",
      f"(PV<sub>−</sub> − PV<sub>+</sub>) / (2 × Δcurve × PV<sub>0</sub>) = (102.90 − 99.30) / (2 × 0.0025 × 101.20) = {_ed:.2f}", ""),
     ("A bond's key rate durations are 0.5 at two years and 4.0 at ten years. Only the ten-year rate rises, by 20 bp. Estimate the price change.",
      f"−4.0 × 0.20% = {-4*.2:.2f}%",
      "Key rate durations add up to the effective duration (here 4.5) and are the tool for non-parallel shifts.")],
    (["Measure", "Based on", "Needed for"], [
        ["Modified (yield) duration", "Change in the bond's own yield", "Option-free bonds"],
        ["Effective (curve) duration", "Shift in the benchmark curve, with cash flows allowed to change", "Bonds with embedded options, MBS"],
        ["Key rate duration", "Shift at a single maturity point", "Shaping risk: steepening, flattening"],
        ["Empirical duration", "Observed price moves in historical data", "Credit bonds, where spreads and benchmark yields move in opposite directions"]]),
    "Know when yield duration fails: if cash flows depend on rates, a bond has no well-defined yield to maturity, so use effective duration. Also expect the flight-to-quality item: for high-yield bonds, empirical duration is lower than analytical duration because spreads widen when government yields fall.")

# --- ck: Credit Risk ---
EK["ck"] = G(
    [("A bond has a 2% annual probability of default and an expected recovery rate of 40%. What is the expected loss? The bond offers a spread of 2.0% over the government bond; is the investor compensated?",
      f"loss given default = 1 − 40% = 60%|expected loss = 2% × 60% = {.02*.6*100:.1f}%|spread of 2.0% exceeds the expected loss of 1.2%",
      "The spread more than covers expected credit loss. The remainder pays for liquidity, taxes and the uncertainty of the loss.")],
    (["Term", "Meaning"], [
        ["Probability of default", "How likely the issuer fails to pay"],
        ["Loss given default (loss severity)", "Share of the exposure lost if default occurs: 1 − recovery rate"],
        ["Credit migration risk", "Risk of a rating downgrade, which widens the spread before any default"],
        ["Market liquidity risk", "Risk of selling below fair value because of a wide bid–ask spread"],
        ["Issuer rating vs issue rating", "Issuer rating reflects senior unsecured debt; individual issues are notched up or down for seniority"]]),
    "Expected-loss calculations are simple, so the difficulty is in the wording: \"recovery rate\" and \"loss severity\" are complements. Qualitative items test the Cs of credit analysis (capacity, capital, collateral, covenants, character) and the limits of ratings: they lag the market and do not measure price risk.")

# --- cg: Government credit ---
EK["cg"] = G(
    [("A revenue bond finances a toll road with net operating revenue of 30 million a year and annual debt service of 20 million. What is the debt service coverage ratio? A sovereign has debt of 600 billion and GDP of 1,000 billion; what is its debt-to-GDP ratio?",
      f"DSCR = 30 / 20 = {30/20:.1f}×|debt to GDP = 600 / 1,000 = {600/1000*100:.0f}%",
      "A revenue bond is repaid only from the project, so coverage is the key ratio. A sovereign is judged on the debt burden relative to the economy and on its capacity to raise revenue.")],
    (["Pair", "Difference"], [
        ["General obligation vs revenue bond", "GO bonds are backed by the issuer's taxing power; revenue bonds only by one project's cash flows, so they are riskier"],
        ["Ability vs willingness to pay", "A sovereign can be able but unwilling; bondholders have little legal recourse"],
        ["Local-currency vs foreign-currency debt", "Foreign-currency debt usually has the lower rating, since it must be repaid from reserves or export earnings"],
        ["Qualitative vs quantitative factors", "Institutions, policy credibility and economic flexibility vs fiscal, growth and external-balance ratios"]]),
    "Questions describe a country or a municipality and ask which factor most supports or weakens its credit. Reserve-currency status, diversified exports and independent monetary policy are strengths; reliance on a single commodity and large foreign-currency debt are weaknesses.")

# --- cc: Corporate credit ---
EK["cc"] = G(
    [("A company reports EBIT of 120, EBITDA of 200, interest expense of 30 and total debt of 500. Compute interest coverage and leverage.",
      f"EBIT / interest = 120 / 30 = {120/30:.1f}×|debt / EBITDA = 500 / 200 = {500/200:.1f}×",
      "Higher coverage is better; higher leverage is worse. Compare with industry peers and with the company's own history, not in isolation.")],
    (["Ranking (highest claim first)", "Note"], [
        ["First-lien / senior secured", "Claim on specific pledged assets"],
        ["Senior unsecured", "General claim; the basis for the issuer rating"],
        ["Subordinated and junior subordinated", "Paid only after senior claims; lowest recovery"],
        ["Pari passu", "Claims of the same rank share equally, whatever their maturity"],
        ["Structural subordination", "Parent-company debt ranks behind subsidiary debt for the subsidiary's assets"]]),
    "Expect a table of ratios for two issuers and \"which has the higher credit quality\". Also expect seniority questions: in a bankruptcy the priority of claims is the starting point, but it is not always followed strictly in a reorganization. Secured debt has a higher recovery rate, not a lower probability of default.")

# --- sc: Securitization ---
EK["sc"] = G(
    [("An SPE issues 80 of senior notes, 15 of mezzanine notes and 5 of subordinated notes against a 100 loan pool. The pool loses 8. How are the losses allocated?",
      "subordinated: absorbs the first 5 and is wiped out|mezzanine: absorbs the next 3, leaving 12|senior: no loss",
      "This is credit tranching, or subordination. The senior notes are protected by 20 of junior tranches below them.")],
    (["Party or structure", "Role"], [
        ["Originator / seller", "Makes the loans and sells them to the SPE"],
        ["Special purpose entity (issuer)", "Buys the pool and issues the securities; legally separate from the seller"],
        ["Servicer", "Collects payments and handles delinquencies"],
        ["True sale", "Makes the SPE bankruptcy remote: the seller's creditors have no claim on the pool"],
        ["Covered bond", "Assets stay on the bank's balance sheet; investors have recourse to both the bank and the cover pool"]]),
    "Questions ask which party does what, and why an ABS can carry a higher rating than its originator: the assets are legally isolated in the SPE. The covered bond contrast is a favorite: dual recourse, assets on balance sheet, and non-performing assets must be replaced.")

# --- ab: ABS ---
EK["ab"] = G(
    [("An ABS is backed by a 110 million loan pool and has 100 million of notes outstanding. The pool yields 9%, the notes pay 5% and servicing costs 1%. What are the overcollateralization and the excess spread?",
      f"overcollateralization = 110 − 100 = 10 million ({10/100*100:.0f}% of the notes)|excess spread = 9% − 5% − 1% = {9-5-1}%",
      "Both are internal credit enhancement: losses are absorbed first by the excess spread and the extra collateral before any tranche is touched.")],
    (["Pair", "Difference"], [
        ["Internal vs external enhancement", "Internal: subordination, overcollateralization, excess spread. External: guarantees or letters of credit from a third party"],
        ["Amortizing vs non-amortizing collateral", "Auto loans repay principal over time; credit card receivables revolve, and principal is reinvested during the lockout period"],
        ["CDO vs CLO", "A CDO is backed by a pool of debt; a CLO specifically by leveraged loans, and is actively managed"],
        ["Time tranching vs credit tranching", "Sequential tranches redistribute prepayment timing; subordinated tranches redistribute credit losses"]]),
    "Typical items ask you to classify an enhancement as internal or external, or to say what happens to credit card ABS during the revolving period: principal collected buys new receivables, so investors receive only interest until the lockout ends or an early-amortization trigger is hit.")

# --- mb: MBS ---
_smm = 1 - (1 - .06) ** (1 / 12)
EK["mb"] = G(
    [("A borrower takes a 240,000 mortgage on a home valued at 300,000. What is the loan-to-value ratio? A pool is prepaying at a conditional prepayment rate of 6%; what is the single monthly mortality rate?",
      f"LTV = 240,000 / 300,000 = {240/300*100:.0f}%|SMM = 1 − (1 − 0.06)<sup>1/12</sup> = {_smm*100:.3f}%",
      "A lower LTV means more borrower equity and a lower expected loss. SMM is the monthly counterpart of the annual CPR.")],
    (["Pair", "Difference"], [
        ["Contraction vs extension risk", "Rates fall: prepayments speed up and the security shortens just when reinvestment rates are low. Rates rise: prepayments slow and it lengthens"],
        ["Pass-through vs CMO", "A pass-through passes all cash flows pro rata; a CMO redistributes them into tranches"],
        ["PAC vs support tranche", "A PAC has a stable schedule within a prepayment band; the support tranche absorbs the variability"],
        ["Agency vs non-agency RMBS", "Agency securities carry a guarantee, so the risk is prepayment; non-agency securities also carry credit risk and need enhancement"],
        ["Recourse vs non-recourse loan", "With recourse the lender can claim the borrower's other assets after foreclosure"]]),
    "Know both directions of prepayment risk and who bears it: support tranches take the most, PAC tranches the least. For CMBS, the loans are non-recourse, so analysis rests on the property's DSCR and LTV, and the main risk at maturity is balloon risk, since borrowers must refinance.")
