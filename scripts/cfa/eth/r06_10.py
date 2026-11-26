# CFA Level I · Ethical and Professional Standards · part 2. Original study notes and questions.
R = []

R.append(dict(id="s4", n="Standard IV: Duties to Employers", k="STANDARD IV", w=3, c="#2f8f5b",
terms=[
 ["Loyalty to employer", "İşverene sadakat", "Acting for the employer's benefit and not depriving it of one's skills or harming it.", "İşverenin yararına hareket etme; onu becerilerinden yoksun bırakmama veya zarar vermeme."],
 ["Preparing to leave", "Ayrılmaya hazırlanma", "Making arrangements for new employment, permitted as long as no duty to the current employer is breached.", "Mevcut işverene karşı görevler ihlal edilmediği sürece izinli olan, yeni iş için hazırlık yapma."],
 ["Non-compete agreement", "Rekabet yasağı sözleşmesi", "A contract limiting an employee from competing with the employer after leaving.", "Çalışanın ayrıldıktan sonra işverenle rekabet etmesini sınırlayan sözleşme."],
 ["Whistleblowing", "Usulsüzlük bildirimi", "Reporting the employer's illegal or unethical conduct to protect clients or market integrity.", "Müşterileri veya piyasa bütünlüğünü korumak için işverenin yasa dışı veya etik dışı davranışını bildirme."],
 ["Additional compensation arrangement", "Ek ücret düzenlemesi", "Compensation from outside parties for services that may conflict with the employer's interests.", "Dış taraflardan alınan ve işverenin çıkarlarıyla çatışabilecek hizmetler için ücret."],
 ["Supervisor", "Gözetimden sorumlu yönetici", "Anyone with authority over the work of others, responsible for reasonable efforts to prevent violations.", "Başkalarının işi üzerinde yetkisi olan ve ihlalleri önlemek için makul çabadan sorumlu kişi."],
 ["Compliance procedures", "Uyum prosedürleri", "Written policies designed to prevent and detect violations of laws and standards.", "Yasaların ve standartların ihlalini önlemek ve tespit etmek için hazırlanmış yazılı politikalar."],
],
notes="""<h3>IV(A) Loyalty</h3>
<ul>
<li>Act for the benefit of your employer and do not deprive it of your skills, disclose its confidential information, or otherwise harm it.</li>
<li>Duties to clients and to market integrity come before duties to the employer.</li>
<li><b>Leaving:</b> you may prepare to go (look for a job, form a new company), but while still employed you may not solicit current clients, take client lists or confidential records, or misuse firm property.</li>
<li>After leaving, you may contact former clients using public information or your own memory, if no non-compete agreement prevents it. Simple knowledge and experience gained on the job belong to you.</li>
<li>Independent practice in competition with the employer requires the employer's consent.</li>
<li><b>Whistleblowing</b> that breaks confidentiality may be justified to protect clients or market integrity, not for personal gain.</li>
</ul>
<h3>IV(B) Additional compensation arrangements</h3>
<ul>
<li>Do not accept gifts, benefits or compensation that compete with or could create a conflict with the employer's interests, unless you obtain <b>written consent from all parties</b> involved.</li>
<li>Consent should be based on full disclosure of the nature, amount and duration of the arrangement.</li>
</ul>
<h3>IV(C) Responsibilities of supervisors</h3>
<ul>
<li>Make reasonable efforts to ensure that anyone under your supervision complies with laws, rules and the Standards.</li>
<li>Do not accept supervisory responsibility if the firm's compliance system is inadequate; document the problem and decline in writing until it is fixed.</li>
<li>When a violation is suspected: investigate promptly, limit the employee's activity while investigating, and improve procedures. Reporting the violation up the chain alone is not enough.</li>
</ul>
<div class="trap"><b>Exam trap</b>Additional compensation needs written consent from all parties, not merely notice to the employer.</div>""",
qs=[
 ["While still employed, a portfolio manager calls several of her firm's clients to tell them about the new firm she will join next month and asks them to move. This violates:", ["Standard IV(A) Loyalty.", "Standard III(B) Fair Dealing.", "no Standard, because she has already accepted the new job."], 0, "Soliciting the employer's clients before leaving breaches the duty of loyalty."],
 ["After leaving her firm, an analyst contacts former clients whose names she remembers, using public phone listings. She has no non-compete agreement. This is:", ["a violation of IV(A).", "permitted.", "a violation of III(E)."], 1, "Contacting former clients from memory and public sources is allowed absent a non-compete agreement."],
 ["A member is offered a bonus by a client if the client's account outperforms its benchmark. Before accepting, he must obtain:", ["verbal consent from his supervisor.", "written consent from all parties involved.", "approval from CFA Institute."], 1, "Standard IV(B) requires written consent from all parties."],
 ["A supervisor learns that an employee may be front-running client orders. The most appropriate response is to:", ["report the matter to senior management and take no further action.", "investigate promptly and limit the employee's activities in the meantime.", "wait until the employee commits another violation."], 1, "Supervisors must investigate and take steps to prevent further violations."],
 ["A newly promoted head of trading finds that the firm has no adequate compliance procedures. She should:", ["accept the role and create procedures later.", "decline supervisory responsibility in writing until adequate procedures exist.", "resign immediately."], 1, "Supervisors should not accept responsibility without an adequate compliance system."],
 ["The duty of loyalty to an employer:", ["outweighs duties to clients.", "is subordinate to duties to clients and to market integrity.", "applies only to full-time employees."], 1, "The Standards rank obligations to clients and markets above those to the employer."],
 ["While still employed, an analyst downloads his employer's client list to use at a new firm. This violates:", ["Standard IV(A) Loyalty.", "Standard V(C) Record Retention.", "Standard I(B) Independence and Objectivity."], 0, "Client lists are the employer's property and may not be taken."],
 ["A member reports her firm's illegal practices to regulators to protect clients, breaching her firm's confidentiality policy. Under the Standards, this is:", ["always a violation of IV(A).", "potentially acceptable as whistleblowing.", "required in all circumstances."], 1, "Disclosure to protect clients or market integrity may be justified when not done for personal gain."],
]))

R.append(dict(id="s5", n="Standard V: Investment Analysis, Recommendations, and Actions", k="STANDARD V", w=3, c="#c2417a",
terms=[
 ["Diligence", "Titizlik (özen)", "Thorough and careful work in analysing investments.", "Yatırımları analiz ederken kapsamlı ve dikkatli çalışma."],
 ["Reasonable basis", "Makul dayanak", "Research and evidence adequate to support an investment recommendation.", "Bir yatırım tavsiyesini desteklemeye yeterli araştırma ve kanıt."],
 ["Third-party research", "Üçüncü taraf araştırması", "Research prepared by others; may be relied on after a reasonable review of its soundness.", "Başkalarınca hazırlanan araştırma; sağlamlığı makul ölçüde incelendikten sonra kullanılabilir."],
 ["Group research", "Grup araştırması", "A recommendation reached by a team; a dissenting member may still be named if the process was sound.", "Bir ekibin vardığı tavsiye; süreç sağlamsa muhalif üye de adıyla yer alabilir."],
 ["Communication with clients", "Müşterilerle iletişim", "Disclosing the investment process, its risks and limitations, and separating fact from opinion.", "Yatırım sürecini, risklerini ve sınırlamalarını açıklama ve olgu ile görüşü ayırma."],
 ["Record retention", "Kayıtların saklanması", "Keeping records that support analysis, recommendations and actions.", "Analizi, tavsiyeleri ve işlemleri destekleyen kayıtları saklama."],
 ["Quantitative model risk", "Nicel model riski", "The risk that models used in analysis are flawed or poorly understood.", "Analizde kullanılan modellerin hatalı olması veya iyi anlaşılmaması riski."],
],
notes="""<h3>V(A) Diligence and reasonable basis</h3>
<ul>
<li>Exercise diligence, independence and thoroughness in analysis, and have a reasonable and adequate basis, supported by research, for every recommendation and action.</li>
<li>The level of diligence depends on the investment's complexity and the role of the member.</li>
<li><b>Third-party research</b> may be used after a reasonable review: assumptions, rigour, timeliness, objectivity.</li>
<li><b>Group research:</b> a member who disagrees with a team's conclusion need not remove her name if the process was sound; she may document her dissent.</li>
<li>Understand the models you use, including their assumptions and limitations, and test them across scenarios. When selecting external managers, do appropriate due diligence.</li>
</ul>
<h3>V(B) Communication with clients and prospective clients</h3>
<ul>
<li>Disclose the basic format and general principles of the investment process, and promptly disclose material changes.</li>
<li>Use reasonable judgement in identifying the factors important to recommendations and communicate them.</li>
<li>Disclose significant risks and limitations.</li>
<li>Distinguish between <b>fact and opinion</b> (for example, a projected growth rate is an opinion).</li>
<li>A brief report is acceptable if fuller supporting research is available on request.</li>
</ul>
<h3>V(C) Record retention</h3>
<ul>
<li>Develop and keep records that support investment analysis, recommendations, actions and communications.</li>
<li>Records belong to the <b>firm</b>. A member who changes jobs must recreate supporting records from public sources, not take the old firm's files.</li>
<li>Where no law or regulation specifies a period, CFA Institute recommends keeping records for at least <b>seven years</b>.</li>
</ul>
<div class="trap"><b>Exam trap</b>A dissenting analyst can stay named on a group report. She is not required to resign or to remove her name, provided she believes the process had a reasonable basis.</div>""",
qs=[
 ["An analyst uses a research report from another firm without checking its assumptions or methods. This most likely violates:", ["Standard V(A) Diligence and Reasonable Basis.", "Standard V(C) Record Retention.", "Standard III(B) Fair Dealing."], 0, "Third-party research may be used only after a reasonable review of its soundness."],
 ["A member of a research team disagrees with the team's buy recommendation, though she believes the process was thorough. Under the Standards she:", ["must remove her name from the report.", "may leave her name on the report and document her dissent.", "must resign from the team."], 1, "Group research is acceptable if it has a reasonable basis; dissent can be documented."],
 ["A report states that a company's earnings 'will grow 15% next year' without indicating that this is the analyst's estimate. This most likely violates:", ["Standard V(B) Communication with Clients and Prospective Clients.", "Standard II(B) Market Manipulation.", "Standard VII(A) Conduct as Participants in CFA Institute Programs."], 0, "Members must distinguish fact from opinion."],
 ["A manager changes his investment process from fundamental to purely quantitative but does not tell clients. This violates:", ["Standard IV(C) Responsibilities of Supervisors.", "Standard V(B) Communication with Clients.", "Standard III(E) Preservation of Confidentiality."], 1, "Material changes to the investment process must be disclosed promptly."],
 ["In the absence of other regulatory guidance, CFA Institute recommends retaining records for at least:", ["three years.", "five years.", "seven years."], 2, "Seven years is the recommended minimum where no rule applies."],
 ["When an analyst moves to a new employer, the research records she created at her old firm:", ["belong to her and may be taken.", "belong to the old firm and may not be taken.", "must be destroyed."], 1, "Records are the property of the firm; she must recreate support from public sources."],
 ["A portfolio manager uses a complex quantitative model he does not understand and cannot explain its key assumptions. This most likely violates:", ["Standard V(A) Diligence and Reasonable Basis.", "Standard I(C) Misrepresentation.", "Standard VI(B) Priority of Transactions."], 0, "Members must understand the models and assumptions behind their decisions."],
 ["An adviser sends clients a one-page summary of a recommendation and makes the full research available on request. Under the Standards this is:", ["a violation of V(B).", "acceptable.", "a violation of V(C)."], 1, "Brief communications are acceptable if supporting information is available."],
]))

R.append(dict(id="s6", n="Standards VI–VII: Conflicts of Interest and Responsibilities as a Member or Candidate", k="STANDARDS VI–VII", w=3, c="#1f7a8c",
terms=[
 ["Conflict of interest", "Çıkar çatışması", "A situation in which a member's interests, or the firm's, could diverge from those of clients or employers.", "Üyenin veya firmanın çıkarlarının müşterilerin ya da işverenlerin çıkarlarından ayrışabileceği durum."],
 ["Full and fair disclosure", "Tam ve adil açıklama", "Disclosure that is prominent, delivered in plain language and effectively communicates the conflict.", "Belirgin, sade dille yapılan ve çatışmayı etkili biçimde aktaran açıklama."],
 ["Priority of transactions", "İşlem önceliği", "Client and employer transactions take precedence over personal transactions.", "Müşteri ve işveren işlemlerinin kişisel işlemlerden önce gelmesi."],
 ["Front-running", "Önden işlem (front-running)", "Trading for oneself ahead of a client's order or a recommendation.", "Bir müşteri emrinden veya tavsiyeden önce kendi hesabına işlem yapma."],
 ["Beneficial ownership", "Gerçek faydalanıcılık", "Having a direct or indirect financial interest in an account or security.", "Bir hesap veya menkul kıymette doğrudan veya dolaylı mali çıkara sahip olma."],
 ["Referral fee", "Yönlendirme ücreti", "Compensation received or paid for recommending services or clients.", "Hizmet veya müşteri tavsiye etmek karşılığında alınan ya da ödenen ücret."],
 ["CFA designation", "CFA unvanı", "The professional designation that may be used only as an adjective, after meeting all requirements.", "Tüm şartlar sağlandıktan sonra yalnızca sıfat olarak kullanılabilen mesleki unvan."],
 ["Candidate in the CFA Program", "CFA Programı adayı", "A person enrolled in the program; there is no partial designation such as 'Level I CFA'.", "Programa kayıtlı kişi; 'Level I CFA' gibi kısmi bir unvan yoktur."],
],
notes="""<h3>VI(A) Avoid or disclose conflicts</h3>
<ul>
<li>Avoid conflicts where possible; where not, make <b>full and fair disclosure</b> of anything that could reasonably impair independence and objectivity or interfere with duties to clients, prospects or the employer.</li>
<li>Disclosure must be prominent, in plain language, and effectively communicated.</li>
<li>Examples: owning shares one recommends, board seats, investment banking relationships, and compensation structures.</li>
</ul>
<h3>VI(B) Priority of transactions</h3>
<ul>
<li>Client and employer transactions come before transactions in which the member is a beneficial owner.</li>
<li>No <b>front-running</b>. Personal trading is not prohibited, but must not disadvantage clients: firms often require pre-clearance, blackout periods and reporting of holdings.</li>
<li>Family accounts that are fee-paying clients should be treated like other clients, neither favoured nor disadvantaged.</li>
</ul>
<h3>VI(C) Referral fees</h3>
<ul>
<li>Disclose to the employer, clients and prospective clients any compensation, consideration or benefit received or paid for recommending products or services, <b>before</b> entering into an agreement.</li>
</ul>
<h3>VII(A) Conduct in CFA Institute programs</h3>
<ul>
<li>Do not compromise the reputation or integrity of CFA Institute, the designation, or the integrity, validity or security of its exams.</li>
<li>Prohibited: cheating, disclosing exam questions or the specific topics tested, using unauthorized materials, misrepresenting information on the Professional Conduct Statement or in volunteer work.</li>
<li>Allowed: expressing opinions, including criticism, about CFA Institute and the program; discussing general topics covered in the curriculum.</li>
</ul>
<h3>VII(B) Reference to CFA Institute and the designation</h3>
<ul>
<li>Do not misrepresent or exaggerate what membership, the designation or candidacy means.</li>
<li>"CFA" is used as an adjective ("a CFA charterholder"), never as a noun, and not with partial designations ("CFA Level I").</li>
<li>A candidate may say he is "a Level II candidate in the CFA Program" or state factually that he passed exams on his first attempt, but not imply superior ability.</li>
<li>Only members in good standing who have completed the program and pay dues may use the designation.</li>
</ul>
<div class="trap"><b>Exam trap</b>Criticizing CFA Institute's policies is permitted. Revealing which topics appeared on the exam is not.</div>""",
qs=[
 ["An analyst issues a buy recommendation on a company in which she holds a large personal stake, without disclosing it. This violates:", ["Standard VI(A) Avoid or Disclose Conflicts.", "Standard III(C) Suitability.", "Standard IV(B) Additional Compensation Arrangements."], 0, "Ownership of the recommended security is a conflict that must be disclosed."],
 ["A portfolio manager buys shares for her own account just before placing a large buy order for her clients in the same shares. This violates:", ["Standard VI(B) Priority of Transactions.", "Standard VI(C) Referral Fees.", "Standard V(C) Record Retention."], 0, "Trading ahead of clients is front-running."],
 ["An adviser receives a payment from a tax accountant for each client he refers. Under the Standards he must:", ["refuse the payments.", "disclose the arrangement to his employer, clients and prospects before entering into an agreement.", "disclose the arrangement only if a client asks."], 1, "Referral fees must be disclosed in advance to all relevant parties."],
 ["Disclosure of a conflict of interest is adequate under the Standards when it is:", ["buried in the legal terms of a contract.", "prominent, in plain language and effectively communicated.", "made only to the employer."], 1, "Full and fair disclosure must be clear and noticeable."],
 ["After the Level I exam, a candidate posts online that the exam had many questions on a particular topic. This violates:", ["Standard VII(A) Conduct as Participants in CFA Institute Programs.", "Standard II(A) Material Nonpublic Information.", "no Standard, because the exam is over."], 0, "Disclosing the topics tested compromises exam integrity."],
 ["A charterholder writes an article criticizing CFA Institute's exam fees. This is:", ["a violation of VII(A).", "a violation of VII(B).", "permitted."], 2, "Members and candidates may express opinions about CFA Institute and the program."],
 ["Which of the following statements is consistent with Standard VII(B)?", ["'He is a CFA.'", "'She is a Level II candidate in the CFA Program.'", "'He holds the CFA Level I designation.'"], 1, "The designation is used as an adjective, and there is no partial designation for passing a level."],
 ["A charterholder states in marketing material that holding the designation means she will achieve better returns than other managers. This violates:", ["Standard VII(B) Reference to CFA Institute, the CFA Designation, and the CFA Program.", "Standard III(D) Performance Presentation.", "Standard I(E) Competence."], 0, "Members may not imply superior performance because of the designation."],
]))

R.append(dict(id="gp", n="Introduction to the Global Investment Performance Standards (GIPS)", k="GIPS", w=3, c="#3b7dd8",
terms=[
 ["GIPS standards", "Küresel Yatırım Performans Standartları", "Voluntary, ethical standards for calculating and presenting investment performance.", "Yatırım performansını hesaplamak ve sunmak için gönüllü, etik standartlar."],
 ["Firm", "Firma (GIPS kapsamında)", "The entity that claims compliance with GIPS; compliance applies to the whole firm.", "GIPS'e uyum beyan eden kuruluş; uyum tüm firmayı kapsar."],
 ["Composite", "Kompozit", "An aggregation of one or more portfolios managed to a similar strategy or mandate.", "Benzer bir strateji veya yetkiyle yönetilen bir ya da daha fazla portföyün birleşimi."],
 ["Discretionary portfolio", "Takdire bağlı portföy", "A portfolio the manager can manage according to its strategy without significant client restrictions.", "Yöneticinin, önemli müşteri kısıtlamaları olmadan stratejisine göre yönetebildiği portföy."],
 ["Cherry-picking", "Seçici sunum (kiraz toplama)", "Presenting only the best-performing accounts or periods.", "Yalnızca en iyi performans gösteren hesapları veya dönemleri sunma."],
 ["Survivorship bias", "Hayatta kalma yanlılığı", "Excluding closed or poorly performing accounts from reported results.", "Kapatılan veya kötü performans gösteren hesapları raporlanan sonuçlardan çıkarma."],
 ["Verification", "Doğrulama", "An independent review of a firm's compliance with GIPS on a firm-wide basis; optional.", "Firmanın GIPS uyumunun firma genelinde bağımsız incelenmesi; isteğe bağlıdır."],
],
notes="""<h3>Why GIPS exists</h3>
<ul>
<li>Before common standards, managers could make results look better by showing only their best accounts (cherry-picking), dropping closed or poor accounts (survivorship bias), or choosing flattering periods.</li>
<li>GIPS gives prospective clients comparable, fair and complete performance information, and helps firms compete globally on a level field.</li>
</ul>
<h3>Key features</h3>
<ul>
<li><b>Voluntary:</b> no law requires them, though some clients demand compliance.</li>
<li><b>Firm-wide:</b> only investment management firms (and asset owners) can claim compliance, and only for the whole firm. Individuals, products and single composites cannot claim it.</li>
<li><b>No partial compliance:</b> a firm cannot claim to comply "except for" certain requirements.</li>
<li><b>Composites:</b> every actual, fee-paying, discretionary portfolio must be included in at least one composite, defined by strategy. Composites must be defined before the fact and portfolios cannot be moved to improve results.</li>
<li>Firms must present at least five years of compliant history (or since inception), building up to ten years.</li>
</ul>
<h3>Verification</h3>
<ul>
<li>Performed by an independent third party on the whole firm. It tests whether composites are constructed correctly and whether the firm's policies for calculating and presenting performance are designed in compliance and have been implemented.</li>
<li>Verification is <b>optional</b> but recommended; it does not certify any particular composite's performance.</li>
</ul>
<div class="trap"><b>Exam trap</b>A firm claims compliance; a portfolio manager or a fund cannot. And there is no such thing as partial compliance.</div>""",
qs=[
 ["Compliance with the GIPS standards is:", ["required by law in most countries.", "voluntary.", "required for all CFA charterholders."], 1, "GIPS are voluntary standards, though clients may expect them."],
 ["Which of the following can claim compliance with the GIPS standards?", ["An individual portfolio manager", "A single composite", "An investment management firm"], 2, "Compliance is claimed by the firm as a whole."],
 ["A firm complies with all GIPS requirements except the rules on composite construction. It may state that it:", ["complies with GIPS except for composite construction.", "cannot claim compliance with GIPS.", "partially complies with GIPS."], 1, "Partial compliance cannot be claimed."],
 ["Under GIPS, all actual, fee-paying, discretionary portfolios must be:", ["included in at least one composite.", "presented individually.", "excluded if their performance is poor."], 0, "Including every such portfolio prevents cherry-picking."],
 ["A manager shows prospective clients only the performance of her three best accounts. This practice, which GIPS aims to prevent, is called:", ["verification.", "cherry-picking.", "composite construction."], 1, "Selecting only the best accounts gives a misleading picture."],
 ["Verification under GIPS is:", ["mandatory and performed by the firm itself.", "optional and performed by an independent third party.", "mandatory and performed by CFA Institute."], 1, "Firms may choose to be verified by an independent verifier."],
 ["Excluding accounts that were closed after poor performance from a firm's reported track record creates:", ["survivorship bias.", "a composite.", "a discretionary portfolio."], 0, "Dropping failed accounts makes historical results look better than they were."],
 ["The main purpose of the GIPS standards is to:", ["guarantee investment returns.", "set fees for investment managers.", "provide fair, comparable and complete performance information."], 2, "GIPS aim at full disclosure and fair representation of performance."],
]))

R.append(dict(id="ea", n="Ethics Application", k="CASES", w=3, c="#2e9e8f",
terms=[
 ["Case analysis", "Vaka analizi", "Applying the Standards to a set of facts to decide whether a violation occurred and what should be done.", "Bir ihlal olup olmadığını ve ne yapılması gerektiğini belirlemek için standartları bir olay örgüsüne uygulama."],
 ["Reasonable person test", "Makul kişi ölçütü", "Judging conduct by what a reasonable professional would do in the same situation.", "Davranışı, aynı durumdaki makul bir profesyonelin ne yapacağına göre değerlendirme."],
 ["Recommended procedures", "Önerilen prosedürler", "Practices suggested to help comply with a Standard; not themselves requirements.", "Bir standarda uyumu kolaylaştırmak için önerilen uygulamalar; kendileri zorunlu değildir."],
 ["Blackout period", "Yasak dönem", "A period during which employees may not trade certain securities, often around recommendations or client trades.", "Çalışanların belirli menkul kıymetlerde işlem yapamadığı, çoğu zaman tavsiye veya müşteri işlemleri civarındaki dönem."],
 ["Pre-clearance", "Ön onay", "Requiring compliance approval before an employee makes a personal trade.", "Çalışanın kişisel işleminden önce uyum biriminin onayını gerektirme."],
 ["Watch list", "İzleme listesi", "A confidential list of securities whose trading is monitored because the firm may have sensitive information.", "Firmanın hassas bilgiye sahip olabileceği için işlemleri izlenen menkul kıymetlerin gizli listesi."],
],
notes="""<h3>How to work through an ethics case</h3>
<ul>
<li>1. Identify who the member owes duties to: clients, employer, the market, CFA Institute.</li>
<li>2. List the facts that matter: what the member knew, did and disclosed, and when.</li>
<li>3. Match the facts to the Standard most directly involved. Several may apply.</li>
<li>4. Ask what a reasonable, prudent professional would have done.</li>
<li>5. Decide whether a violation occurred, and what the member should do now: disclose, stop, dissociate, seek consent, or correct.</li>
</ul>
<h3>Common patterns</h3>
<div class="tbl"><table>
<tr><th>Fact pattern</th><th>Likely Standard</th></tr>
<tr><td>Gift or trip from a company being analysed</td><td>I(B) Independence and Objectivity</td></tr>
<tr><td>Guaranteed returns, plagiarism, overstated credentials</td><td>I(C) Misrepresentation</td></tr>
<tr><td>Trading on a tip from an insider</td><td>II(A) Material Nonpublic Information</td></tr>
<tr><td>Better treatment for big clients without disclosure</td><td>III(B) Fair Dealing</td></tr>
<tr><td>Investments that do not fit the client or fund mandate</td><td>III(C) Suitability</td></tr>
<tr><td>Soliciting clients before leaving</td><td>IV(A) Loyalty</td></tr>
<tr><td>Outside pay without written consent</td><td>IV(B) Additional Compensation</td></tr>
<tr><td>Recommendation without adequate research</td><td>V(A) Diligence and Reasonable Basis</td></tr>
<tr><td>Personal trades ahead of clients</td><td>VI(B) Priority of Transactions</td></tr>
<tr><td>Undisclosed referral payments</td><td>VI(C) Referral Fees</td></tr>
<tr><td>"CFA" used as a noun, exam content shared</td><td>VII(B) / VII(A)</td></tr>
</table></div>
<h3>Firm-level safeguards</h3>
<ul>
<li>Written compliance policies, training, pre-clearance and reporting of personal trades, blackout periods, restricted and watch lists, firewalls, documented trade allocation procedures, and annual reviews of investment policy statements.</li>
</ul>
<div class="trap"><b>Exam trap</b>Recommended procedures are good practice, not requirements. A firm that lacks a particular procedure has not automatically violated a Standard.</div>""",
qs=[
 ["An analyst accepts an all-expenses-paid luxury trip from a company she covers and then upgrades her rating on its shares. The Standard most directly at issue is:", ["I(B) Independence and Objectivity.", "III(D) Performance Presentation.", "VI(C) Referral Fees."], 0, "Lavish benefits from an issuer can compromise objectivity."],
 ["A manager places client orders for a thinly traded share after first buying it for his own account at a lower price. The Standard most directly violated is:", ["VI(B) Priority of Transactions.", "III(A) Loyalty, Prudence, and Care.", "II(B) Market Manipulation."], 0, "He has traded ahead of his clients, putting his own interest first."],
 ["A portfolio manager invests a conservative retiree's entire portfolio in speculative technology shares. The Standard most directly at issue is:", ["III(C) Suitability.", "V(C) Record Retention.", "VII(A) Conduct in CFA Institute Programs."], 0, "The investments do not match the client's objectives and constraints."],
 ["A firm's compliance manual recommends but does not require pre-clearance of personal trades. An employee trades without pre-clearance, but not ahead of any client order. The employee has:", ["violated VI(B).", "not necessarily violated any Standard.", "violated IV(C)."], 1, "Recommended procedures are not requirements; the question is whether clients were disadvantaged."],
 ["An adviser tells a prospective client that he 'is a CFA' and has 'never had a losing year'. The Standards most directly at issue are:", ["VII(B) and I(C).", "II(A) and III(E).", "IV(A) and VI(C)."], 0, "Using 'CFA' as a noun breaches VII(B); the performance claim may be misrepresentation under I(C)."],
 ["An analyst writes a sell recommendation based only on a rumour from an internet forum. The Standard most directly at issue is:", ["V(A) Diligence and Reasonable Basis.", "III(B) Fair Dealing.", "I(D) Misconduct."], 0, "A recommendation needs an adequate basis supported by research."],
 ["When analysing an ethics case, the first step is to:", ["decide on the sanction.", "identify the duties owed and the relevant facts.", "consult the client."], 1, "Understanding the duties and facts comes before matching them to Standards."],
 ["A firm prohibits employees from trading a security for a set period around the release of a recommendation on it. This safeguard is a:", ["watch list.", "blackout period.", "firewall."], 1, "Blackout periods prevent personal trades from benefiting from upcoming recommendations."],
]))
