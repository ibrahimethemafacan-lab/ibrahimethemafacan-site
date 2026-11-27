import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guc import G, n

EK = {}
C = "Case."  # bu konuda örnekler sayısal değil, vaka biçimindedir

def V(ex, cf, ask):
    d = G(ex, cf, ask)
    d["notes"] = d["notes"].replace("<h3>Worked examples</h3>", "<h3>Worked cases</h3>").replace("<h3>Worked example</h3>", "<h3>Worked case</h3>").replace("<b>Question.</b>", "<b>Case.</b>")
    return d

# --- et: Ethics and Trust ---
EK["et"] = V(
    [("A fund manager may legally market a complex product to retail clients in her country. She knows most of them cannot understand its risks, and her bonus depends on sales. Is selling it acceptable because it is legal?",
      "", "No. Law sets a minimum; ethics asks what serves the client. The bonus is a situational influence pushing her toward a choice she might not otherwise make. Applying a decision framework (identify the facts and those affected, consider alternatives and conflicts, decide and act, reflect) would surface the clients' interests before the sale.")],
    (["Pair", "Difference"], [
        ["Ethical vs legal", "Some legal acts are unethical, and some ethical acts may be illegal; the two overlap but are not the same"],
        ["Code of ethics vs standards of conduct", "Broad principles and values vs specific rules for minimum acceptable behavior"],
        ["Profession vs occupation", "A profession has specialized knowledge, a code, a duty to clients and society, and a body that enforces standards"],
        ["Situational vs dispositional influences", "Pressure from circumstances (money, loyalty, authority) vs a person's own character; people overestimate the second"],
        ["Compliance culture vs ethical culture", "Following rules to avoid punishment vs wanting to do right when no rule applies"]]),
    "Questions are conceptual: why ethics matters more in investment management (clients cannot easily judge quality, and trust underlies markets), what a profession is, and which step of the decision framework a described action represents. \"Legal therefore ethical\" is always a wrong answer.")

# --- cs: Code and Standards ---
EK["cs"] = V(
    [("A client complains to CFA Institute that a charterholder misrepresented a fund's performance. What can happen?",
      "", "Professional Conduct staff open an inquiry, which may involve asking the member for a written explanation and interviewing the member, the complainant and others. If a violation is found, a sanction is proposed; the member may accept it or have the matter heard by a panel. Sanctions include public censure, suspension and revocation of membership or of the right to use the designation.")],
    (["Standard", "Topic"], [
        ["I", "Professionalism"],
        ["II", "Integrity of Capital Markets"],
        ["III", "Duties to Clients"],
        ["IV", "Duties to Employers"],
        ["V", "Investment Analysis, Recommendations, and Actions"],
        ["VI", "Conflicts of Interest"],
        ["VII", "Responsibilities as a CFA Institute Member or CFA Candidate"]]),
    "Know the seven standards by number and name, and the six components of the Code: act with integrity and competence; put clients and the profession above personal interest; use reasonable care and independent judgment; practice professionally and encourage others to; promote the integrity of capital markets; maintain and improve competence. Inquiries can start from self-disclosure, complaints, media reports or exam-day incidents.")

# --- s1: Standard I ---
EK["s1"] = V(
    [("A charterholder lives in a country with strict insider trading laws and does business in a country that has none. Which rules apply to her work in the second country?",
      "", "Standard I(A): follow the stricter of applicable law and the Code and Standards. The Code and Standards prohibit acting on material nonpublic information, so she may not, whatever the local law allows."),
     ("A company invites an analyst to visit its factory abroad and offers to pay for business-class flights and a luxury hotel.",
      "", "Standard I(B): the analyst should pay for the travel herself, or have her employer pay. Modest arrangements can be accepted when no commercial transport is available. Lavish hospitality from an issuer threatens independence and objectivity.")],
    (["Sub-standard", "Core idea", "Typical violation"], [
        ["I(A) Knowledge of the Law", "Follow the stricter rule; dissociate from violations", "Staying silent and involved after discovering wrongdoing"],
        ["I(B) Independence and Objectivity", "Do not offer or accept anything that could compromise judgment", "Accepting issuer gifts; changing a rating under pressure"],
        ["I(C) Misrepresentation", "No false statements, guarantees or plagiarism", "Copying research without credit; \"guaranteed\" returns"],
        ["I(D) Misconduct", "No dishonesty, fraud or deceit that reflects on professional integrity", "Fraud; repeated intoxication at work"],
        ["I(E) Competence", "Have or acquire the knowledge and skills the work requires", "Taking on work one is not qualified to do"]]),
    "Gift questions turn on who gives: a gift from an issuer threatens objectivity and should be refused unless modest; a bonus from a client for past performance may be accepted if disclosed to the employer. Under I(A), reporting to authorities is not required by the Standards, but dissociating is. Personal beliefs and civil disobedience unrelated to professional integrity do not violate I(D).")

# --- s2: Standard II ---
EK["s2"] = V(
    [("An analyst combines public filings, her own industry analysis and a non-material comment from a company's supplier, and concludes that earnings will disappoint. Separately, a colleague hears a chief financial officer tell a friend in a lift that the company will miss its earnings forecast.",
      "", "The analyst may trade and recommend: this is the mosaic theory, a conclusion built from public and non-material nonpublic information. The colleague has material nonpublic information: he must not trade or cause others to trade, and should encourage the company to make the information public.")],
    (["Pair", "Difference"], [
        ["Material", "A reasonable investor would want to know it; it would move the price"],
        ["Nonpublic", "Not yet disseminated to the market; telling a few analysts does not make it public"],
        ["Mosaic theory vs insider information", "Assembling non-material and public pieces is allowed; one material nonpublic fact is not"],
        ["Information-based manipulation", "Spreading false or misleading information to move a price"],
        ["Transaction-based manipulation", "Trades designed to create a false impression of price or activity"]]),
    "II(A) questions ask whether information is both material and nonpublic, and what to do next: do not act, do not pass it on, and seek public disclosure. Firms should use information barriers (firewalls), restricted lists and watch lists. Under II(B), intent matters: a legitimate trading strategy that happens to move prices is not manipulation.")

# --- s3: Standard III ---
EK["s3"] = V(
    [("A manager receives an allocation of an oversubscribed IPO. He gives all of it to his three largest clients, who pay the highest fees, although the issue also suits several smaller accounts.",
      "", "This violates III(B) Fair Dealing. Suitable clients must be treated fairly: allocate pro rata by order size, not by fee level or relationship. Fair does not mean equal; premium service levels are allowed if they are disclosed and do not disadvantage other clients."),
     ("A retired client with a low risk tolerance asks her adviser to buy a speculative technology stock she read about.",
      "", "Under III(C) Suitability the adviser should explain why the trade does not fit her investment policy statement. If it has a minor effect on the portfolio he may follow her instruction after warning her; if the effect is material, the policy statement should be updated first.")],
    (["Sub-standard", "Core idea"], [
        ["III(A) Loyalty, Prudence, and Care", "Client interests come before the employer's and one's own"],
        ["III(B) Fair Dealing", "Treat all clients fairly in recommendations and trades"],
        ["III(C) Suitability", "Know the client's objectives and constraints; judge investments in the context of the whole portfolio"],
        ["III(D) Performance Presentation", "Fair, accurate and complete; no cherry-picked results"],
        ["III(E) Preservation of Confidentiality", "Keep client information confidential unless it concerns illegal activity, the law requires disclosure, or the client permits it"]]),
    "Identify who the client is: for a pension plan, the duty is to the beneficiaries, not to the company's management. Soft-dollar (client brokerage) benefits must be used for the clients' benefit. Confidentiality continues after the relationship ends, but it does not block cooperation with a CFA Institute investigation.")

# --- s4: Standard IV ---
EK["s4"] = V(
    [("A portfolio manager plans to start her own firm. Before resigning she registers the company in the evenings, and tells two clients she will be leaving and hopes they will follow. After leaving she contacts former clients using phone numbers she finds online.",
      "", "Preparing to leave (registering the firm in her own time) is allowed. Soliciting clients before leaving violates IV(A) Loyalty. Contacting former clients afterwards with publicly available information is allowed, provided she took no client lists or records and has no non-compete agreement.")],
    (["Sub-standard", "Core idea", "Remember"], [
        ["IV(A) Loyalty", "Do not harm the employer or deprive it of your skills", "Whistleblowing to protect clients or markets can be justified; records belong to the firm"],
        ["IV(B) Additional Compensation Arrangements", "Outside pay or benefits tied to your work need written consent from all parties", "Applies to client bonuses and outside directorships"],
        ["IV(C) Responsibilities of Supervisors", "Make reasonable efforts to prevent and detect violations", "Without adequate procedures, decline supervisory responsibility in writing"]]),
    "Leaving-an-employer cases are the favourite: what may be taken (general skills and experience, names remembered), what may not (client lists, models, files, even self-created ones), and when solicitation may start (after departure). A supervisor who learns of a violation must respond promptly, investigate and limit the employee's activities; relying on the employee's word is not enough.")

# --- s5: Standard V ---
EK["s5"] = V(
    [("An analyst issues a \"buy\" based on a third-party research report she has not examined, and tells clients the stock \"will reach 80 within a year\". Her report omits the fact that her model was recently changed to rely on a single growth assumption.",
      "", "Three problems. V(A): she needs a reasonable basis, which includes checking that third-party research is sound. V(B): the price target is an opinion and must be presented as one, not as fact. V(B) again: clients must be told about significant changes to the investment process and about its limitations and risks.")],
    (["Sub-standard", "Core idea"], [
        ["V(A) Diligence and Reasonable Basis", "Research thorough enough to support the conclusion; group research may be signed if the process is sound, even if one disagrees"],
        ["V(B) Communication with Clients", "Describe the process and its changes, the significant risks and limitations, and separate fact from opinion"],
        ["V(C) Record Retention", "Keep records supporting recommendations and client communications; seven years is recommended where no rule exists"]]),
    "Typical items: relying on secondary or third-party research (allowed after reasonable checks), quantitative models (understand the assumptions and limits), and the fact-versus-opinion distinction. Records are the property of the firm; an analyst who changes jobs must recreate supporting documentation from public sources and the new firm's files.")

# --- s6: Standards VI–VII ---
EK["s6"] = V(
    [("An analyst writes a favourable report on a company in which he owns shares, without mentioning the holding. He buys more for his own account the day before the report is released.",
      "", "Not disclosing the ownership violates VI(A) Disclosure of Conflicts. Trading ahead of his own recommendation violates VI(B) Priority of Transactions: clients and the employer must be able to act first."),
     ("A candidate who passed Level II writes \"CFA, Level II\" on her profile, and after the exam posts which topics were emphasised in the questions.",
      "", "Both violate Standard VII. There is no partial designation: she may state that she passed Level II of the CFA Program. Revealing exam content, even in general terms about tested topics, breaches the confidentiality of the exam under VII(A).")],
    (["Sub-standard", "Core idea"], [
        ["VI(A) Disclosure of Conflicts", "Disclose fully, in plain language, anything that could impair independence, to clients and to the employer"],
        ["VI(B) Priority of Transactions", "Client trades first, then the employer's, then personal; family accounts that are clients are treated like any other client"],
        ["VI(C) Referral Fees", "Disclose any compensation paid or received for referrals before the client commits"],
        ["VII(A) Conduct in the CFA Program", "No cheating or sharing of exam content; opinions about the program itself are allowed"],
        ["VII(B) Reference to CFA Institute, the Designation and the Program", "State facts only; never imply superior ability or results"]]),
    "Conflicts are managed by disclosure, not necessarily by elimination. For VII(B), check the wording: \"CFA\" is used after a name as a designation, a candidate must be registered for an exam to claim candidacy, and statements such as \"charterholders achieve better returns\" are prohibited while \"I passed all three levels on my first attempts\" is a permitted fact.")

# --- gp: GIPS ---
EK["gp"] = V(
    [("An asset manager advertises that its equity division \"complies with GIPS except for the treatment of terminated accounts\", and shows a composite made up of its ten best-performing portfolios.",
      "", "Three errors. Compliance must be firm-wide, not for one division unless that division is defined and held out to the public as the firm. Partial compliance cannot be claimed: \"except for\" statements are prohibited. A composite must include all actual, fee-paying, discretionary portfolios managed to that strategy, including terminated ones up to the last full period.")],
    (["Pair", "Difference"], [
        ["Composite vs benchmark", "The firm's own portfolios with one strategy vs an independent reference for comparison"],
        ["Verification vs performance examination", "Third-party review of the firm's policies and procedures firm-wide vs testing of a specific composite's results"],
        ["Discretionary vs non-discretionary portfolio", "Only portfolios the manager is free to manage to the strategy go into composites"],
        ["Firm", "The distinct business entity held out to clients; total firm assets include all discretionary and non-discretionary assets"],
        ["Initial vs ongoing history", "At least five years of compliant performance (or since inception), then add a year annually up to ten"]]),
    "GIPS are voluntary, apply to firms rather than individuals, and exist so that prospective clients can compare managers fairly. Typical questions ask what a firm may claim, who may verify (an independent third party; verification is recommended, not required) and what a composite must contain. Composites are defined before performance is known, not after.")

# --- ea: Ethics Application ---
EK["ea"] = V(
    [("A manager's brother-in-law offers her a fee for each client she refers to his tax practice. She refers several clients without mentioning the fee, and she also buys for her own account a small-cap stock just before placing a large client order in it.",
      "", "Take each act separately. The undisclosed fee violates VI(C) Referral Fees: clients must know before they agree. Trading ahead of the client order is front-running and violates VI(B) Priority of Transactions; it also breaches the loyalty owed under III(A). The family relationship itself is not a violation.")],
    (["Often confused", "How to tell them apart"], [
        ["I(B) Independence vs VI(A) Disclosure of Conflicts", "Something that pressures your judgment (gifts, threats) vs a conflict that exists and must be disclosed (ownership, relationships)"],
        ["III(B) Fair Dealing vs VI(B) Priority of Transactions", "Fairness among clients vs clients ahead of yourself and your firm"],
        ["I(C) Misrepresentation vs V(B) Communication", "A false or plagiarized statement vs an incomplete description of process, risk or opinion"],
        ["IV(A) Loyalty vs IV(B) Additional Compensation", "Harming the employer vs taking outside pay without written consent"],
        ["III(C) Suitability vs V(A) Reasonable Basis", "Is it right for this client? vs is the recommendation itself well founded?"]]),
    "Application questions hide several facts in one story. Work in this order: who owes a duty to whom, which single act is being asked about, which standard covers that act, and what the best action would have been. Many wrong options describe conduct that is perfectly acceptable; do not assume every fact in the case is a violation.")
