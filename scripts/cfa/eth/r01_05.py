# CFA Level I · Ethical and Professional Standards · part 1. Original study notes and questions.
# The Code and Standards are summarized in our own words; consult CFA Institute's Standards of Practice Handbook for the official text.
R = []

R.append(dict(id="et", n="Ethics and Trust in the Investment Profession", k="TRUST", w=3, c="#3b7dd8",
terms=[
 ["Ethics", "Etik", "The study of moral principles that guide what is right and wrong behaviour.", "Doğru ve yanlış davranışı yönlendiren ahlaki ilkelerin incelenmesi."],
 ["Code of ethics", "Etik kuralları", "A written set of moral principles that guide the behaviour of members of a group.", "Bir grubun üyelerinin davranışını yönlendiren yazılı ahlaki ilkeler."],
 ["Standards of conduct", "Mesleki davranış standartları", "Specific minimum behaviours required of members of a profession.", "Bir mesleğin üyelerinden beklenen belirli asgari davranışlar."],
 ["Profession", "Meslek", "An occupation with specialized knowledge, a code of conduct, and a commitment to serve clients and society.", "Uzmanlık bilgisi, davranış kuralları ve müşterilere ve topluma hizmet bağlılığı olan iş alanı."],
 ["Situational influences", "Durumsal etkiler", "External pressures, such as money, prestige or loyalty, that can lead people to act unethically.", "İnsanları etik dışı davranmaya itebilecek para, prestij veya sadakat gibi dış baskılar."],
 ["Overconfidence bias", "Aşırı güven yanlılığı", "Overestimating one's own ethical character, which can lead to poor decisions.", "Kişinin kendi etik karakterini abartması; kötü kararlara yol açabilir."],
 ["Legal vs ethical", "Yasal ile etik arasındaki fark", "Actions can be legal but unethical, or illegal but ethical; laws are a minimum.", "Davranışlar yasal ama etik dışı ya da yasa dışı ama etik olabilir; yasalar asgari düzeydir."],
 ["Ethical decision-making framework", "Etik karar verme çerçevesi", "A structured process: identify, consider, decide and act, then reflect.", "Yapılandırılmış süreç: belirle, değerlendir, karar ver ve uygula, sonra üzerine düşün."],
],
notes="""<h3>Why ethics matters in investment</h3>
<ul>
<li>Clients cannot easily judge the quality of financial advice, so the industry depends on <b>trust</b>. Unethical behaviour damages clients, firms and the efficient functioning of markets.</li>
<li>A <b>profession</b> has specialized knowledge, admission standards, a code of conduct, monitoring and enforcement, and a commitment to put clients first.</li>
<li>Laws set a minimum; they lag behind market practice and vary by country. Ethical behaviour often requires more than the law demands.</li>
</ul>
<h3>Why people act unethically</h3>
<ul>
<li><b>Overconfidence:</b> believing oneself to be ethical and not examining decisions carefully.</li>
<li><b>Situational influences:</b> money, prestige, loyalty to an employer or colleague, and short-term focus can drown out long-term consequences.</li>
</ul>
<h3>A framework for decisions</h3>
<ul>
<li><b>Identify:</b> the facts, the stakeholders and duties owed, the ethical principles, and any conflicts of interest.</li>
<li><b>Consider:</b> situational influences, alternative actions, and seek guidance (compliance, colleagues, mentors).</li>
<li><b>Decide and act.</b></li>
<li><b>Reflect:</b> was the outcome as expected, and what would you do differently?</li>
</ul>
<div class="trap"><b>Exam trap</b>Legal is not the same as ethical. A question may describe something permitted by law that still violates a professional standard.</div>""",
qs=[
 ["Trust in the investment profession matters especially because:", ["clients can easily verify the quality of advice.", "clients often cannot easily judge the quality of advice.", "regulation removes all conflicts of interest."], 1, "The information gap between professionals and clients makes trust essential."],
 ["Which statement about laws and ethics is most accurate?", ["Ethical behaviour may require more than the law requires.", "Anything legal is ethical.", "Laws are always stricter than ethical codes."], 0, "Laws set minimum standards and may lag behind market practices."],
 ["An analyst is sure he would never act unethically and so does not examine his decisions closely. He is most likely exhibiting:", ["anchoring.", "overconfidence bias.", "situational influence."], 1, "Overconfidence in one's own ethics can lead to poor decisions."],
 ["A portfolio manager feels pressure to keep a large client happy at the expense of other clients. This is an example of:", ["a situational influence.", "a standard of conduct.", "the mosaic theory."], 0, "External pressures such as loyalty and money are situational influences."],
 ["The first step in an ethical decision-making framework is to:", ["take action.", "reflect on the outcome.", "identify the facts, stakeholders and duties."], 2, "Decisions start with understanding the situation and the obligations involved."],
 ["Which of the following is a characteristic of a profession?", ["No minimum entry requirements", "A code of conduct with monitoring and enforcement", "A focus on the practitioner's own interests"], 1, "Professions set and enforce standards of behaviour for their members."],
 ["An action that is legal in a given country:", ["is always ethical.", "may still be unethical.", "is always required by professional standards."], 1, "The law and ethics can diverge; professionals should consider both."],
 ["After making an ethical decision, an analyst reviews whether the outcome matched her expectations. This step is:", ["identify.", "consider.", "reflect."], 2, "Reflection helps improve future decisions."],
]))

R.append(dict(id="cs", n="Code of Ethics and Standards of Professional Conduct", k="CODE", w=3, c="#2e9e8f",
terms=[
 ["Code of Ethics", "Etik Kuralları", "The broad ethical principles that CFA Institute members and candidates agree to follow.", "CFA Institute üyelerinin ve adaylarının uymayı kabul ettiği genel etik ilkeler."],
 ["Standards of Professional Conduct", "Mesleki Davranış Standartları", "Seven groups of specific rules that apply the Code to practice.", "Etik Kuralları uygulamaya döken yedi grup ayrıntılı kural."],
 ["Professional Conduct Program", "Mesleki Davranış Programı", "CFA Institute's process for investigating and sanctioning violations.", "CFA Institute'un ihlalleri soruşturma ve yaptırım uygulama süreci."],
 ["Disciplinary Review Committee", "Disiplin İnceleme Komitesi", "The volunteer body that reviews conduct cases and decides on sanctions.", "Davranış dosyalarını inceleyen ve yaptırımlara karar veren gönüllü kurul."],
 ["Sanction", "Yaptırım", "A penalty such as censure, suspension or revocation of membership or the designation.", "Kınama, askıya alma veya üyeliğin ya da unvanın iptali gibi ceza."],
 ["Professional Conduct Statement", "Mesleki Davranış Beyanı", "The annual statement members and candidates complete about complaints, litigation and investigations.", "Üye ve adayların şikâyetler, davalar ve soruşturmalar hakkında her yıl doldurduğu beyan."],
 ["Integrity", "Dürüstlük", "Acting honestly and consistently with ethical principles.", "Dürüst ve etik ilkelerle tutarlı davranma."],
],
notes="""<h3>Structure</h3>
<ul>
<li>The <b>Code of Ethics</b> states broad principles; the <b>Standards of Professional Conduct</b> set out specific requirements in seven groups. The Standards of Practice Handbook explains them with examples.</li>
<li>They apply to all CFA Institute members and to candidates in the CFA Program.</li>
</ul>
<h3>What the Code asks, in brief</h3>
<ul>
<li>Act with integrity, competence, diligence and respect, and in an ethical manner toward clients, employers, colleagues and the public.</li>
<li>Put the integrity of the profession and the interests of clients above personal interests.</li>
<li>Use reasonable care and independent judgement in analysis, recommendations and actions.</li>
<li>Practise professionally and encourage others to do so, in a way that reflects well on the profession.</li>
<li>Promote the integrity and viability of global capital markets.</li>
<li>Maintain and improve professional competence.</li>
</ul>
<h3>The seven Standards</h3>
<div class="tbl"><table>
<tr><th>Standard</th><th>Covers</th></tr>
<tr><td>I. Professionalism</td><td>Knowledge of the law, independence and objectivity, misrepresentation, misconduct, competence</td></tr>
<tr><td>II. Integrity of Capital Markets</td><td>Material nonpublic information, market manipulation</td></tr>
<tr><td>III. Duties to Clients</td><td>Loyalty, prudence and care; fair dealing; suitability; performance presentation; confidentiality</td></tr>
<tr><td>IV. Duties to Employers</td><td>Loyalty, additional compensation arrangements, responsibilities of supervisors</td></tr>
<tr><td>V. Investment Analysis, Recommendations, and Actions</td><td>Diligence and reasonable basis, communication with clients, record retention</td></tr>
<tr><td>VI. Conflicts of Interest</td><td>Avoid or disclose conflicts, priority of transactions, referral fees</td></tr>
<tr><td>VII. Responsibilities as a CFA Institute Member or Candidate</td><td>Conduct in CFA Institute programs, reference to CFA Institute and the designation</td></tr>
</table></div>
<h3>Enforcement</h3>
<ul>
<li>The Professional Conduct Program investigates possible violations, prompted by the annual Professional Conduct Statement, written complaints, media reports, or exam proctor reports.</li>
<li>Staff may close the case, issue a cautionary letter, or propose a sanction. Members and candidates can accept or contest the sanction before a hearing panel.</li>
<li>Sanctions include public censure, suspension, revocation of membership or the right to use the designation, and, for candidates, suspension or prohibition from the program.</li>
</ul>
<div class="trap"><b>Exam trap</b>The Code and Standards apply to candidates as well as members, from the moment a candidate enrols.</div>""",
qs=[
 ["The CFA Institute Code of Ethics and Standards of Professional Conduct apply to:", ["members only.", "members and candidates.", "all investment professionals worldwide."], 1, "Candidates enrolled in the CFA Program are bound along with members."],
 ["Which of the following is part of Standard III, Duties to Clients?", ["Market manipulation", "Suitability", "Record retention"], 1, "Suitability is III(C). Market manipulation is II(B) and record retention is V(C)."],
 ["Standard II, Integrity of Capital Markets, covers:", ["material nonpublic information and market manipulation.", "loyalty to employers.", "referral fees."], 0, "Its two parts deal with insider information and manipulation."],
 ["Members and candidates are required to disclose complaints, litigation and investigations in their:", ["Professional Conduct Statement.", "research reports.", "client agreements."], 0, "The annual statement is one of the ways the Professional Conduct Program learns of possible violations."],
 ["Under the Code of Ethics, members and candidates should place the interests of clients:", ["after their employer's interests.", "above their own personal interests.", "equal to their own interests."], 1, "The Code asks members to put clients' interests and the integrity of the profession first."],
 ["Which of the following is a possible sanction under the Professional Conduct Program?", ["A fine paid to the client", "A criminal conviction", "Revocation of the right to use the CFA designation"], 2, "CFA Institute can censure, suspend or revoke membership and the designation; it cannot impose criminal penalties."],
 ["Standard VI, Conflicts of Interest, includes:", ["priority of transactions.", "fair dealing.", "performance presentation."], 0, "VI(B) Priority of Transactions sits with VI(A) disclosure and VI(C) referral fees."],
 ["A member who disagrees with a proposed sanction from the Professional Conduct Program may:", ["ignore it.", "contest it before a hearing panel.", "appeal to a national court only."], 1, "The process allows the matter to be referred to a panel of the Disciplinary Review Committee."],
]))

R.append(dict(id="s1", n="Standard I: Professionalism", k="STANDARD I", w=3, c="#c0563f",
terms=[
 ["Knowledge of the law", "Mevzuat bilgisi", "Members must understand and comply with applicable laws, rules and the Code and Standards, following the strictest.", "Üyeler geçerli yasaları, kuralları ve Etik Kurallar ile Standartları anlamalı ve en katı olana uymalıdır."],
 ["Dissociation", "Uzaklaşma (ilişkiyi kesme)", "Separating oneself from an activity that violates laws or the Standards, for example by refusing to participate or resigning.", "Yasaları veya standartları ihlal eden bir faaliyetten, örneğin katılmayı reddederek veya istifa ederek uzaklaşma."],
 ["Independence and objectivity", "Bağımsızlık ve tarafsızlık", "Avoiding any gift, benefit or pressure that could compromise professional judgement.", "Mesleki yargıyı zedeleyebilecek hediye, menfaat veya baskıdan kaçınma."],
 ["Issuer-paid research", "İhraççı tarafından ödenen araştırma", "Research paid for by the company being analysed; allowed only with safeguards such as a flat fee and disclosure.", "İncelenen şirketin ödediği araştırma; yalnızca sabit ücret ve açıklama gibi güvencelerle izinlidir."],
 ["Misrepresentation", "Yanıltıcı beyan", "Knowingly making false or misleading statements, including plagiarism and guarantees of investment performance.", "Bilerek yanlış veya yanıltıcı beyanda bulunma; intihal ve yatırım performansı garantisi dahil."],
 ["Plagiarism", "İntihal", "Using others' work or ideas without proper attribution.", "Başkalarının çalışmalarını veya fikirlerini uygun atıf yapmadan kullanma."],
 ["Misconduct", "Mesleki suistimal", "Dishonest, fraudulent or deceitful conduct, or any act that reflects badly on professional reputation or competence.", "Dürüst olmayan, hileli veya aldatıcı davranış ya da mesleki itibar veya yetkinliğe gölge düşüren eylem."],
 ["Competence", "Mesleki yeterlilik", "Acting with and maintaining the knowledge and skills needed for one's professional activities.", "Mesleki faaliyetler için gereken bilgi ve becerilere sahip olma ve bunları sürdürme."],
],
notes="""<h3>I(A) Knowledge of the law</h3>
<ul>
<li>Know and follow applicable laws and the Code and Standards. Where they differ, follow the <b>stricter</b>.</li>
<li>Do not knowingly participate in or assist violations. If you become aware of one, raise it with your supervisor or compliance; if it continues, <b>dissociate</b> (refuse to take part, and if needed resign).</li>
<li>Reporting to the authorities is not required by the Standards, though it may be advisable or required by law.</li>
</ul>
<h3>I(B) Independence and objectivity</h3>
<ul>
<li>Do not offer, solicit or accept anything that could reasonably compromise your independence or that of others.</li>
<li>Modest, customary gifts and entertainment are acceptable. Gifts from <b>clients</b> for past performance should be disclosed to the employer. Benefits from <b>third parties</b> that could influence future behaviour need much more caution.</li>
<li>Pay your own way on company visits where practical. Issuer-paid research must be for a flat fee, not tied to the conclusion, and disclosed.</li>
<li>Resist pressure from the investment banking side, issuers and large clients.</li>
</ul>
<h3>I(C) Misrepresentation</h3>
<ul>
<li>Do not knowingly misrepresent facts about investments, your qualifications, your firm's services or performance.</li>
<li>Do not guarantee investment returns, unless the product itself is guaranteed (for example, a government bond's promised payments).</li>
<li>Attribute others' work; using recognized public statistical data without citation is acceptable.</li>
</ul>
<h3>I(D) Misconduct</h3>
<ul>
<li>No dishonesty, fraud or deceit in professional life, and no act that reflects badly on your professional reputation, integrity or competence. Personal conduct matters only when it reflects on professional integrity.</li>
</ul>
<h3>I(E) Competence</h3>
<ul>
<li>Act with and keep up the knowledge and skills your work requires. Do not take on work you are not competent to do without getting help.</li>
</ul>
<div class="trap"><b>Exam trap</b>When local law is less strict than the Standards, follow the Standards. When local law is stricter, follow the law.</div>""",
qs=[
 ["A member works in a country whose securities laws are less strict than the CFA Institute Standards. She should follow:", ["local law.", "the Standards.", "whichever her employer prefers."], 1, "Members follow the stricter of applicable law and the Code and Standards."],
 ["An analyst learns that his colleagues are engaged in an activity that violates securities law. After raising it with compliance without result, the Standards require him to:", ["report it to the regulator.", "dissociate himself from the activity.", "continue working as usual."], 1, "Dissociation is required; reporting to authorities is not required by the Standards, though it may be advisable."],
 ["A client gives a portfolio manager tickets to a major sporting event in thanks for strong performance last year. The manager should:", ["refuse the gift.", "disclose the gift to her employer.", "accept it without telling anyone."], 1, "Gifts from clients for past performance are acceptable with disclosure to the employer."],
 ["A company offers to pay an analyst's research firm a fee that rises if the report recommends buying the shares. Accepting this would most likely violate:", ["Standard I(B) Independence and Objectivity.", "Standard III(B) Fair Dealing.", "Standard V(C) Record Retention."], 0, "Compensation tied to the conclusion compromises objectivity; issuer-paid research must use a flat fee."],
 ["A salesperson tells a client that a portfolio of corporate bonds is 'guaranteed to return 6% a year'. This most likely violates:", ["Standard I(A) Knowledge of the Law.", "Standard I(C) Misrepresentation.", "Standard IV(A) Loyalty."], 1, "Guaranteeing returns on a risky investment is a misrepresentation."],
 ["An analyst copies large parts of another firm's report into her own report without attribution. This violates the Standard on:", ["misconduct.", "misrepresentation.", "suitability."], 1, "Plagiarism is a form of misrepresentation under I(C)."],
 ["A member is arrested for a minor offence unrelated to his work and his honesty. This is most likely:", ["a violation of I(D) Misconduct.", "not a violation of the Standards.", "a violation of I(B) Independence and Objectivity."], 1, "I(D) concerns conduct that reflects on professional integrity or competence; unrelated personal matters generally do not."],
 ["A portfolio manager agrees to manage a complex derivatives strategy although she has no relevant experience and does not seek help. This most likely violates:", ["Standard I(E) Competence.", "Standard II(B) Market Manipulation.", "Standard VI(C) Referral Fees."], 0, "Members must have, or obtain, the knowledge and skills needed for the work they take on."],
]))

R.append(dict(id="s2", n="Standard II: Integrity of Capital Markets", k="STANDARD II", w=3, c="#8a5cc2",
terms=[
 ["Material information", "Önemli bilgi", "Information that would likely affect a security's price or that a reasonable investor would want before deciding.", "Bir menkul kıymetin fiyatını etkilemesi muhtemel veya makul bir yatırımcının karar öncesinde bilmek isteyeceği bilgi."],
 ["Nonpublic information", "Kamuya açıklanmamış bilgi", "Information that has not been disseminated to the market.", "Piyasaya yayılmamış bilgi."],
 ["Mosaic theory", "Mozaik teorisi", "Reaching a conclusion by combining public information with nonmaterial nonpublic information, which is permitted.", "Kamuya açık bilgiyle önemli olmayan kamuya açık olmayan bilgiyi birleştirerek sonuca ulaşma; izinlidir."],
 ["Firewall", "Bilgi bariyeri (Çin seddi)", "Procedures that prevent the flow of confidential information between departments.", "Departmanlar arasında gizli bilgi akışını önleyen prosedürler."],
 ["Restricted list", "Yasaklı (kısıtlı) liste", "A list of securities in which a firm limits trading or recommendations because it may hold inside information.", "Firmanın içeriden bilgiye sahip olabileceği için işlem veya tavsiyeyi kısıtladığı menkul kıymetler listesi."],
 ["Information-based manipulation", "Bilgiye dayalı manipülasyon", "Spreading false or misleading information to move prices.", "Fiyatları hareket ettirmek için yanlış veya yanıltıcı bilgi yayma."],
 ["Transaction-based manipulation", "İşleme dayalı manipülasyon", "Trades that create a false impression of price or volume, or that attempt to corner a market.", "Fiyat veya hacim konusunda yanlış izlenim yaratan ya da piyasayı köşeye sıkıştırmaya çalışan işlemler."],
],
notes="""<h3>II(A) Material nonpublic information</h3>
<ul>
<li>If you have information that is both <b>material</b> and <b>nonpublic</b>, do not act on it and do not cause others to act on it.</li>
<li>Material: likely to move the price, or a reasonable investor would want to know it. Reliability of the source matters.</li>
<li>Nonpublic: not yet disseminated to the market. Information given to a group of analysts in a closed meeting is still nonpublic.</li>
<li>The <b>mosaic theory</b> allows conclusions drawn from public information plus nonmaterial nonpublic details, even if the conclusion would be material if disclosed by the company.</li>
<li>If you receive material nonpublic information, encourage the company to make it public.</li>
<li>Firms should use <b>firewalls</b>, restricted and watch lists, and monitoring of personal trading.</li>
</ul>
<h3>II(B) Market manipulation</h3>
<ul>
<li>Do not engage in practices that distort prices or artificially inflate trading volume with intent to mislead.</li>
<li><b>Information-based:</b> spreading false rumours, or recommending a security to push its price up and then selling ("pump and dump").</li>
<li><b>Transaction-based:</b> trades designed to give a false impression of activity, or to gain control of supply in order to manipulate the price.</li>
<li>Legitimate trading strategies, such as tax-loss selling or arbitrage, are not manipulation; intent to mislead is the key.</li>
</ul>
<div class="trap"><b>Exam trap</b>An analyst who pieces together small, nonmaterial facts from many sources and public data does not violate II(A), even if her conclusion is significant.</div>""",
qs=[
 ["A portfolio manager overhears, in a lift, an executive saying that his company will announce an unexpected large loss tomorrow. The manager sells the company's shares. This most likely violates:", ["Standard II(A) Material Nonpublic Information.", "Standard II(B) Market Manipulation.", "no Standard, because she did not seek the information."], 0, "The information is material and nonpublic; how it was obtained does not matter."],
 ["An analyst combines public financial statements with visits to the company's suppliers and concludes that sales will fall sharply. She issues a sell recommendation. This is:", ["a violation of II(A).", "a violation of II(B).", "permitted under the mosaic theory."], 2, "Combining public and nonmaterial nonpublic information is allowed even when the conclusion is material."],
 ["Information disclosed by a company to a small group of analysts at a private meeting is:", ["public, because analysts are professionals.", "nonpublic until it is disseminated to the market.", "never material."], 1, "Information is public only once it has been made available to the market."],
 ["An analyst who receives material nonpublic information should most likely:", ["trade quickly before others learn it.", "encourage the company to disclose it publicly.", "pass it to her clients first."], 1, "Members should not act on it and should encourage public disclosure."],
 ["A trader buys large amounts of a thinly traded share near the close to raise the price used to value his fund's holdings. This violates:", ["Standard II(B) Market Manipulation.", "Standard III(D) Performance Presentation.", "Standard V(A) Diligence and Reasonable Basis."], 0, "Trading to distort a price with intent to mislead is transaction-based manipulation."],
 ["An investor posts false rumours online about a takeover bid, then sells the shares after the price rises. This is an example of:", ["the mosaic theory.", "transaction-based manipulation.", "information-based manipulation."], 2, "Spreading misleading information to move prices is information-based manipulation."],
 ["The main purpose of a firewall within an investment bank is to:", ["prevent the flow of material nonpublic information between departments.", "protect computer systems from hackers.", "separate client and firm assets."], 0, "Firewalls stop inside information obtained by the advisory side from reaching traders and analysts."],
 ["A manager sells shares at a loss before year-end to realize a tax benefit for clients and buys similar shares. This is:", ["market manipulation.", "a legitimate trading strategy.", "a violation of II(A)."], 1, "Trades with a genuine purpose and no intent to mislead are not manipulation."],
]))

R.append(dict(id="s3", n="Standard III: Duties to Clients", k="STANDARD III", w=3, c="#b8860b",
terms=[
 ["Loyalty, prudence and care", "Sadakat, basiret ve özen", "Acting for the client's benefit, putting the client's interests before one's own and the employer's.", "Müşterinin yararına hareket etme; müşterinin çıkarlarını kendi ve işverenin çıkarlarının önüne koyma."],
 ["Soft dollars", "Soft dolar (aracılık komisyonu karşılığı hizmet)", "Using client brokerage commissions to obtain research or services; the commissions belong to the client.", "Müşteri aracılık komisyonlarıyla araştırma veya hizmet alma; komisyonlar müşteriye aittir."],
 ["Fair dealing", "Adil davranma", "Treating all clients fairly when disseminating recommendations and executing trades.", "Tavsiyeleri yayarken ve işlemleri gerçekleştirirken tüm müşterilere adil davranma."],
 ["Suitability", "Uygunluk", "Making sure investments fit the client's objectives, constraints and the stated mandate.", "Yatırımların müşterinin hedeflerine, kısıtlarına ve belirtilen yetkiye uygun olmasını sağlama."],
 ["Performance presentation", "Performans sunumu", "Communicating investment performance fairly, accurately and completely.", "Yatırım performansını adil, doğru ve eksiksiz iletme."],
 ["Confidentiality", "Gizlilik", "Keeping information about current, former and prospective clients private, with limited exceptions.", "Mevcut, eski ve potansiyel müşteriler hakkındaki bilgileri, sınırlı istisnalarla gizli tutma."],
 ["Pro rata allocation", "Oransal dağıtım", "Allocating a partially filled trade among clients in proportion to their orders.", "Kısmen gerçekleşen bir işlemi müşteriler arasında emirleriyle orantılı paylaştırma."],
],
notes="""<h3>III(A) Loyalty, prudence and care</h3>
<ul>
<li>Put clients' interests before your employer's and your own. Act with the care a prudent person would use.</li>
<li>Identify who the client is: for a pooled fund, the duty is to the fund and its mandate, not to individual investors.</li>
<li>Brokerage commissions belong to the client: use them only for research that benefits the client ("soft dollars"), and seek best execution.</li>
<li>Vote proxies in the client's interest unless the cost outweighs the benefit.</li>
</ul>
<h3>III(B) Fair dealing</h3>
<ul>
<li>Deal fairly and objectively with all clients. "Fairly" does not mean "identically": different service levels are allowed if disclosed and available to all who pay for them.</li>
<li>Disseminate new recommendations and changes so that all clients have a fair chance to act. Do not give favoured clients advance notice.</li>
<li>Allocate trades fairly, for example <b>pro rata</b> when an order is partly filled, including IPO allocations.</li>
</ul>
<h3>III(C) Suitability</h3>
<ul>
<li>With an advisory relationship: learn the client's objectives and constraints, write and update an investment policy statement (at least annually), and judge suitability in the context of the whole portfolio.</li>
<li>For a fund managed to a mandate: follow the stated strategy and style.</li>
<li>If a client asks for an unsuitable trade: if it is a small part of the portfolio, the trade can be made after discussing it; if it would materially change the portfolio, update the IPS or get the client's written acknowledgement.</li>
</ul>
<h3>III(D) Performance presentation</h3>
<ul>
<li>Make reasonable efforts to ensure performance information is fair, accurate and complete. Do not present simulated or selected results as actual; disclose when performance is gross of fees or for a single account.</li>
<li>Compliance with GIPS is encouraged but not required.</li>
</ul>
<h3>III(E) Preservation of confidentiality</h3>
<ul>
<li>Keep client information confidential unless it concerns illegal activity, disclosure is required by law, or the client permits it.</li>
<li>Cooperating with CFA Institute's Professional Conduct Program is not a breach.</li>
</ul>
<div class="trap"><b>Exam trap</b>Fair dealing does not require treating every client identically; it requires that no client is disadvantaged unfairly.</div>""",
qs=[
 ["A portfolio manager uses client brokerage commissions to pay for research that benefits only the firm's proprietary trading desk. This violates:", ["Standard III(A) Loyalty, Prudence, and Care.", "Standard III(E) Preservation of Confidentiality.", "Standard VII(B) Reference to CFA Institute."], 0, "Commissions belong to clients and may be used only for services that benefit them."],
 ["An analyst changes her recommendation from buy to sell and calls her three largest clients before releasing the change to everyone else. This violates:", ["Standard III(B) Fair Dealing.", "Standard III(C) Suitability.", "Standard V(C) Record Retention."], 0, "All clients should have a fair opportunity to act on changed recommendations."],
 ["A firm receives only half of the IPO shares it ordered for several clients. The most appropriate allocation is:", ["to the largest clients first.", "pro rata to the clients' orders.", "to the clients who have been with the firm longest."], 1, "Pro rata allocation treats all participating clients fairly."],
 ["A firm offers a premium service with faster delivery of research to clients who pay more. Under the Standards this is:", ["prohibited.", "permitted if disclosed and available to all clients.", "permitted only for institutional clients."], 1, "Different service levels are allowed when disclosed and offered to all who want to pay for them."],
 ["An investment policy statement for an advisory client should be updated:", ["only when the client asks.", "at least annually and when circumstances change.", "every five years."], 1, "Regular review keeps recommendations suitable."],
 ["The manager of a small-cap growth fund buys large-cap value shares because he thinks they are cheap. This most likely violates:", ["Standard III(C) Suitability.", "Standard II(A) Material Nonpublic Information.", "Standard IV(B) Additional Compensation Arrangements."], 0, "For a fund, suitability means following the fund's stated mandate."],
 ["A manager's marketing material shows the performance of her best account as if it were her overall record. This violates:", ["Standard III(D) Performance Presentation.", "Standard III(E) Preservation of Confidentiality.", "Standard VI(A) Disclosure of Conflicts."], 0, "Presenting a selected account as representative is misleading."],
 ["An adviser discovers evidence that a client is using an account to launder money. Under the Standards, the adviser:", ["must keep the information confidential.", "may disclose the information because it concerns illegal activity.", "must close the account without telling anyone."], 1, "Confidentiality does not cover illegal activities; local law may also require reporting."],
]))
