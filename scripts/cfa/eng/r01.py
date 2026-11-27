# CFA Level I · Exam English (Sınav İngilizcesi). Özgün içerik. Anlatım Türkçe, örnekler sınav dilinde İngilizce.
# Terim biçimi: [ifade, Türkçe karşılığı, İngilizce örnek cümle, Türkçe açıklama]
R = []

# ---------------------------------------------------------------- 1
R.append(dict(id="u1", n="Soru kökleri: soru ne istiyor?", k="QUESTION STEMS", w=3, c="#003894",
terms=[
 ["most likely", "en olası; büyük ihtimalle", "An increase in interest rates will most likely cause bond prices to fall.", "Üç şıktan en doğru olanı isteniyor. Diğer şıklar tamamen saçma olmayabilir; en güçlü olanı seçilir."],
 ["least likely", "en az olası", "Which of the following is least likely a current asset?", "Olumsuz soru: iki şık doğrudur, aranan YANLIŞ olandır. Sınavda en çok hata yapılan köktür."],
 ["closest to", "en yakın değer", "The bond's price is closest to:", "Hesap sorusu. Sonucunuz şıklarla birebir tutmayabilir; yuvarlama farkı normaldir, en yakın şık işaretlenir."],
 ["best described as", "en iyi şöyle tanımlanır", "A contract that gives the right, but not the obligation, to buy is best described as:", "Tanım sorusu. Verilen açıklamanın adını ya da türünü soruyor."],
 ["most accurate", "en doğru ifade", "Which of the following statements is most accurate?", "Üç ifadeden doğru olan seçilir. “least accurate” ise yanlış olanı ister."],
 ["most appropriate", "en uygun", "The most appropriate action for the analyst is to:", "Özellikle Ethics sorularında: yapılması gereken en doğru davranış soruluyor."],
 ["is consistent with", "ile tutarlıdır; uyumludur", "This behavior is consistent with loss aversion.", "Bir gözlemin hangi kavrama, teoriye ya da kurala uyduğunu sorar."],
 ["all else equal", "diğer her şey sabitken", "All else equal, a higher coupon rate results in a lower duration.", "Yalnızca tek bir değişken değişiyor, diğerleri sabit. “Holding other factors constant” ile aynı anlamdadır."],
 ["with respect to", "bakımından; ile ilgili olarak", "With respect to inventory accounting, the company's policy is:", "Sorunun hangi konuya odaklandığını söyler. “Regarding” ve “concerning” ile aynı işi görür."],
 ["would result in", "sonucunu doğurur", "Using LIFO instead of FIFO would most likely result in lower reported income.", "Varsayımsal bir durumun sonucunu sorar. “would” gerçek değil, olası bir durumu anlatır."],
],
notes="""<h3>Önce son cümleyi okuyun</h3>
<ul>
<li>Sorunun gövdesi uzun olabilir, ama ne istendiği çoğunlukla son cümlede yazar. Önce onu okuyun, sonra gövdeye dönün.</li>
<li>Level I'de her sorunun üç şıkkı vardır ve yanlış cevap puan götürmez; boş bırakmayın.</li>
<li>Sınavda “except”, “true/false” ya da “all of the above” yoktur. Onların yerine aşağıdaki kökler kullanılır.</li>
</ul>
<h3>Üç temel kök</h3>
<div class="tbl"><table>
<tr><th>Kök</th><th>Ne istiyor</th><th>Nasıl çözülür</th></tr>
<tr><td>most likely</td><td>En doğru şık</td><td>İki şık kısmen doğru görünebilir; en güçlüsünü seçin</td></tr>
<tr><td>least likely</td><td>Yanlış olan şık</td><td>Her şıkkın yanına D/Y yazın; tek “Y” cevaptır</td></tr>
<tr><td>closest to</td><td>Sayısal sonuç</td><td>Hesaplayın, en yakın şıkkı işaretleyin</td></tr>
</table></div>
<div class="trap"><b>Sınav tuzağı</b>“Least likely” sorusunda ilk doğru ifadeyi görünce işaretleyip geçmek en yaygın hatadır. Bu kökte doğru ifade cevap değildir.</div>
<h3>Aynı anlama gelen kalıplar</h3>
<ul>
<li><b>most likely</b> = most probably = is most likely to</li>
<li><b>best described as</b> = is an example of = is referred to as = is known as</li>
<li><b>all else equal</b> = holding other factors constant = ceteris paribus</li>
<li><b>with respect to</b> = regarding = concerning = in terms of</li>
</ul>""",
qs=[
 ["“Which of the following is least likely a characteristic of common shares?” Bu soruda ne aranıyor?", ["Adi payların özelliği olmayan şık", "Adi payların en önemli özelliği", "Adi payların üç özelliğinden herhangi biri"], 0, "“Least likely” yanlış olanı ister. İki şık adi payların gerçek özelliğidir; aranan, özellik olmayan şıktır."],
 ["A candidate calculates a bond price of 97.33. The choices are 96.50, 97.30 and 98.10. The stem ends with “closest to”. The correct choice is:", ["96.50", "97.30", "98.10"], 1, "“Closest to” en yakın değeri ister. 97,33'e en yakın şık 97,30'dur; yuvarlama farkı hesabın yanlış olduğu anlamına gelmez."],
 ["“All else equal, an increase in the discount rate will most likely decrease the present value.” The phrase “all else equal” means:", ["Every variable changes by the same amount", "Only the discount rate changes", "The present value does not change"], 1, "“All else equal”: diğer her şey sabit. Yalnızca iskonto oranı değişiyor, nakit akışları ve vade aynı kalıyor."],
 ["“An agreement to exchange a series of cash flows on future dates is best described as a:”", ["swap", "call option", "futures margin"], 0, "“Best described as” tanımın adını sorar. Gelecekte bir dizi nakit akışının değiştirilmesi swaptır."],
 ["“The most appropriate action for the analyst is to:” Bu kök hangi tür cevabı ister?", ["Analistin yaptığı hatanın adını", "Analistin kazanacağı tutarı", "Analistin yapması gereken en doğru davranışı"], 2, "“Most appropriate action”: en uygun davranış. Özellikle Ethics sorularında kullanılır; bir tanım ya da tutar değil, yapılacak şey sorulur."],
 ["“Using straight-line depreciation instead of an accelerated method would most likely result in:” “would” burada neyi gösterir?", ["Geçmişte kesinleşmiş bir olayı", "Varsayımsal bir durumun sonucunu", "Bir zorunluluğu"], 1, "“Would” varsayımsal durumu anlatır: şirket böyle yapsaydı ne olurdu. Zorunluluk için “must”, geçmiş için past tense kullanılır."],
 ["“This pattern is consistent with a market that is semi-strong efficient.” The sentence says that the pattern:", ["contradicts semi-strong efficiency", "proves the market is strong-form efficient", "fits what semi-strong efficiency predicts"], 2, "“Is consistent with”: ile tutarlı, uyumlu. Gözlem, yarı güçlü etkinliğin öngördüğü şeyle örtüşüyor; onu kanıtlamıyor, çürütmüyor da."],
]))

# ---------------------------------------------------------------- 2
R.append(dict(id="u2", n="Yön ve miktar ifadeleri", k="DIRECTION & SIZE", w=3, c="#0E7C86",
terms=[
 ["rise / raise", "yükselmek / yükseltmek", "Prices rise. The central bank raises the policy rate.", "“Rise” kendiliğinden artar (nesne almaz); “raise” birisi artırır (nesne alır). Geçmiş halleri: rose, raised."],
 ["decline / decrease / fall", "düşmek; azalmak", "Net income declined by 12% during the year.", "Üçü de azalışı anlatır. “Drop”, “shrink” ve “contract” da aynı yöndedir."],
 ["exceed", "aşmak; daha büyük olmak", "The project is accepted if its IRR exceeds the cost of capital.", "A exceeds B: A, B'den büyük. “Fall short of” bunun tersidir: altında kalmak."],
 ["offset", "dengelemek; telafi etmek", "The gain on the hedge offsets the loss on the bond.", "Bir etki diğerini götürüyor. “Partially offset” kısmen dengelemek demektir."],
 ["by … / to …", "… kadar / … seviyesine", "Revenue rose by 5% to 210 million.", "“By” değişimin büyüklüğünü, “to” ulaşılan seviyeyi verir. İkisini karıştırmak hesabı tamamen değiştirir."],
 ["at least / at most", "en az / en fazla", "There is a 5% probability of losing at least 2 million.", "“At least 2 million”: 2 milyon ya da daha fazlası. “At most”: 2 milyon ya da daha azı."],
 ["net of / gross of", "… düşüldükten sonra / düşülmeden önce", "The fund's return net of fees was 6.4%.", "“Net of fees”: ücretler düşülmüş. “Gross of fees”: ücretler henüz düşülmemiş."],
 ["basis point", "baz puan (yüzde birin yüzde biri)", "The yield increased by 50 basis points, from 4.00% to 4.50%.", "100 baz puan = %1. “bp” ya da “bps” diye kısaltılır."],
 ["twice / half / threefold", "iki katı / yarısı / üç katı", "The standard error is half as large when the sample is four times larger.", "“Twice as large as”: iki katı kadar. “Threefold increase”: üç katına çıkma."],
 ["remain unchanged", "değişmeden kalmak", "If both rise by the same amount, the spread remains unchanged.", "Üç şıklı karşılaştırma sorularının tipik seçeneği: increase, decrease, remain unchanged."],
],
notes="""<h3>Yön bildiren fiiller</h3>
<div class="tbl"><table>
<tr><th>Artış</th><th>Azalış</th><th>Değişmeme</th></tr>
<tr><td>increase, rise, grow, climb, widen, appreciate, expand</td><td>decrease, decline, fall, drop, shrink, narrow, depreciate, contract</td><td>remain unchanged, be unaffected, stay constant, be flat</td></tr>
</table></div>
<ul>
<li><b>Widen / narrow</b> fark ve spread için kullanılır: “the spread widened” (fark açıldı).</li>
<li><b>Appreciate / depreciate</b> para birimi ve varlık değeri için kullanılır: “the euro appreciated” (euro değer kazandı).</li>
</ul>
<h3>“By” ile “to” farkı</h3>
<p class="f">rose <b>by</b> 5% → %5 arttı (değişim)<br>rose <b>to</b> 5% → %5'e çıktı (seviye)<br>rose <b>from</b> 4% <b>to</b> 5% → 100 baz puan arttı; oransal olarak %25 arttı</p>
<div class="trap"><b>Sınav tuzağı</b>Faiz %4'ten %5'e çıkınca artış “1 percentage point” (100 baz puan) olur, “1 percent” değil. “Increased by 1%” denirse 4,00 × 1,01 = %4,04 kastediliyor olabilir. Soru hangisini söylüyor, dikkat edin.</div>
<h3>Karşılaştırma kalıpları</h3>
<ul>
<li><b>higher than / lower than</b>: … den yüksek / düşük</li>
<li><b>greater than or equal to</b>: büyük ya da eşit. <b>No less than</b> aynı anlamdadır.</li>
<li><b>no more than</b> = at most: en fazla</li>
<li><b>the higher of A and B</b>: A ve B'den büyük olanı. <b>The lower of cost and net realizable value</b>: maliyet ile net gerçekleşebilir değerden düşük olanı.</li>
<li><b>the ratio of A to B</b> = A / B. Sıra önemlidir: “debt to equity” borç bölü özkaynaktır.</li>
</ul>""",
qs=[
 ["Revenue rose by 5% to 210 million. Last year's revenue was closest to:", ["199.5 million", "200.0 million", "205.0 million"], 1, "“By 5%” değişimi, “to 210” ulaşılan seviyeyi verir: 210 / 1,05 = 200. 199,5 şıkkı 210'dan %5 düşmenin sonucudur, yani yanlış yöne hesaplanmıştır."],
 ["A bond's yield moves from 4.00% to 4.50%. The yield has increased by:", ["5 basis points", "50 basis points", "450 basis points"], 1, "1 baz puan = %0,01. Fark %0,50 olduğuna göre artış 50 baz puandır."],
 ["“The gain on the futures position partially offset the loss on the portfolio.” The sentence means that the total result was:", ["a loss smaller than the portfolio's loss alone", "a gain", "exactly zero"], 0, "“Partially offset”: kısmen dengeledi. Kazanç zararın bir kısmını götürdü; toplam sonuç hâlâ zarar ama daha küçük."],
 ["“The 5% one-day VaR is 2 million.” This means there is a 5% probability of losing:", ["exactly 2 million in a day", "at most 2 million in a day", "at least 2 million in a day"], 2, "VaR asgari kaybı verir: %5 olasılıkla kayıp 2 milyon ya da daha fazladır. “At least” = en az; “at most” = en fazla."],
 ["“The fund's return was 10% gross of fees and 6.4% net of fees.” The investor actually received:", ["3.6%", "6.4%", "10.0%"], 1, "“Net of fees”: ücretler düşüldükten sonra. Yatırımcının eline geçen %6,4'tür; %3,6 ücretlerin toplamıdır."],
 ["“Inventory is measured at the lower of cost and net realizable value.” Cost is 80 and net realizable value is 74. Inventory is reported at:", ["74", "77", "80"], 0, "“The lower of A and B”: ikisinden düşük olanı. 80 ile 74'ün düşüğü 74'tür."],
 ["“The central bank raised its policy rate and bond yields rose.” Which statement about the two verbs is correct?", ["Both verbs need an object", "“Raised” takes an object; “rose” does not", "“Rose” is the past tense of “raise”"], 1, "“Raise” birinin bir şeyi artırmasıdır (nesne alır: raised its policy rate). “Rise” kendiliğinden artmadır; geçmiş hali “rose”dur ve nesne almaz."],
 ["“The credit spread narrowed from 220 to 180 basis points.” The spread:", ["increased by 40 basis points", "decreased by 40 basis points", "decreased by 4 percentage points"], 1, "“Narrow” daralmak demektir, yani azalış. 220 − 180 = 40 baz puan; bu %0,40'tır, 4 yüzde puan değil."],
]))

# ---------------------------------------------------------------- 3
R.append(dict(id="u3", n="Bağlaçlar ve mantık", k="CONNECTORS", w=3, c="#B45309",
terms=[
 ["however", "ancak; bununla birlikte", "The bond is callable. However, it cannot be called in the first five years.", "Önceki cümleyle zıtlık kurar. Sorunun asıl bilgisi çoğu zaman “however”dan sonra gelir."],
 ["whereas / while", "oysa; … iken", "IFRS permits reversal of the write-down, whereas US GAAP does not.", "İki şeyi karşılaştırır. IFRS ile US GAAP farkı sorularında çok geçer."],
 ["although / despite", "… olmasına rağmen", "Although revenue grew, operating cash flow declined.", "“Although” cümle alır, “despite” isim alır: “despite the growth in revenue”."],
 ["unless", "… olmadıkça; … değilse", "The option will not be exercised unless the price exceeds 50.", "“Unless” = “if not”. Cümle: fiyat 50'yi aşmazsa opsiyon kullanılmaz."],
 ["provided that", "… şartıyla; … koşuluyla", "Gifts may be accepted provided that they are disclosed to the employer.", "Koşul bildirir. “As long as” ve “on condition that” ile aynı anlamdadır."],
 ["regardless of", "… ne olursa olsun; bağımsız olarak", "The convexity adjustment is positive regardless of the direction of the yield change.", "Sonucun bir etkene bağlı olmadığını söyler. “Irrespective of” aynı anlamdadır."],
 ["therefore / thus / hence", "bu nedenle; dolayısıyla", "The coupon rate is below the market rate; therefore, the bond trades at a discount.", "Sonuç bildirir. “Consequently” ve “as a result” da aynı işi görür."],
 ["rather than", "… yerine; … değil de", "Risk is measured by beta rather than by total risk.", "İki seçenekten ilkinin geçerli olduğunu söyler. “Instead of” ile aynıdır."],
 ["given that / assuming", "… olduğuna göre / … varsayımıyla", "Given that the null hypothesis is true, the probability of rejecting it is 5%.", "Sorunun ön koşulunu verir; hesap bu koşul altında yapılır."],
 ["respectively", "sırasıyla", "The returns on funds A and B were 6% and 9%, respectively.", "Sıralı eşleştirme: A %6, B %9. Sırayı karıştırmak cevabı tersine çevirir."],
],
notes="""<h3>Zıtlık bağlaçları cevabı taşır</h3>
<ul>
<li>Soru yazarları önce genel kuralı verir, sonra <b>however</b>, <b>but</b>, <b>although</b>, <b>yet</b> ya da <b>nevertheless</b> ile istisnayı ekler. Cevap çoğu zaman istisnadadır.</li>
<li><b>Whereas</b> ve <b>while</b> iki tarafı karşılaştırır; soruda hangi tarafın sorulduğuna bakın.</li>
<li><b>In contrast</b>, <b>conversely</b> ve <b>on the other hand</b> da zıtlık bildirir.</li>
</ul>
<h3>Koşul bağlaçları</h3>
<div class="tbl"><table>
<tr><th>Bağlaç</th><th>Anlamı</th><th>Örnek</th></tr>
<tr><td>if</td><td>eğer</td><td>If rates fall, prices rise.</td></tr>
<tr><td>unless</td><td>… olmadıkça (if not)</td><td>Do not trade unless the information is public.</td></tr>
<tr><td>provided that</td><td>… şartıyla</td><td>Allowed, provided that the client consents.</td></tr>
<tr><td>only if</td><td>yalnızca … ise</td><td>Exercise only if the option is in the money.</td></tr>
<tr><td>otherwise</td><td>aksi halde</td><td>Disclose the conflict; otherwise, decline the task.</td></tr>
</table></div>
<div class="trap"><b>Sınav tuzağı</b>“Unless” içinde gizli bir olumsuzluk vardır. “The firm will default unless it refinances” cümlesi, yeniden finansman sağlayamazsa temerrüde düşeceğini söyler.</div>
<h3>Sıralama ve eşleştirme</h3>
<ul>
<li><b>respectively</b>: sırasıyla. “A and B are 6% and 9%, respectively” → A %6, B %9.</li>
<li><b>the former / the latter</b>: ilki / ikincisi. “Stocks and bonds: the former are riskier” → hisseler daha riskli.</li>
<li><b>in turn</b>: sırayla; bunun sonucunda. Bir zincirin sonraki halkasını gösterir.</li>
</ul>""",
qs=[
 ["“The option will not be exercised unless the share price exceeds 50.” The share price is 47. The option:", ["will be exercised", "will not be exercised", "must be sold"], 1, "“Unless” = “if not”. Fiyat 50'yi aşmadıkça opsiyon kullanılmaz; 47, 50'yi aşmadığı için kullanılmaz."],
 ["“The returns on funds A, B and C were 4%, 7% and 5%, respectively.” The fund with the highest return is:", ["A", "B", "C"], 1, "“Respectively”: sırasıyla. A %4, B %7, C %5; en yüksek getiri B'dedir."],
 ["“Although net income increased, cash flow from operations decreased.” The sentence tells us that:", ["both measures increased", "both measures decreased", "the two measures moved in opposite directions"], 2, "“Although”: … olmasına rağmen. Net kâr arttığı halde faaliyet nakit akışı azalmış; ikisi zıt yönde hareket etmiş."],
 ["“Under IFRS, development costs may be capitalized, whereas under US GAAP they are generally expensed.” According to the sentence, capitalization is generally possible under:", ["IFRS only", "US GAAP only", "both IFRS and US GAAP"], 0, "“Whereas” iki tarafı karşılaştırır: IFRS'te aktifleştirilebilir, US GAAP'te genellikle giderleştirilir. Aktifleştirme yalnızca IFRS tarafındadır."],
 ["“A member may accept the gift provided that she discloses it to her employer.” The member accepts the gift and tells no one. She has:", ["complied, because gifts are allowed", "not complied, because the condition was not met", "complied, because disclosure is optional"], 1, "“Provided that”: … şartıyla. Kabul etmenin koşulu işverene bildirmektir; koşul yerine gelmediği için kurala uyulmamıştır."],
 ["“Performance should be judged by the Treynor ratio rather than the Sharpe ratio.” The writer recommends using:", ["the Treynor ratio", "the Sharpe ratio", "both ratios together"], 0, "“Rather than”: … yerine. Önerilen ilk söylenendir: Sharpe değil, Treynor oranı."],
 ["“Stocks and bonds both fell; the former fell by more.” Which fell by more?", ["Bonds", "Stocks", "They fell by the same amount"], 1, "“The former” ilk sayılanı, “the latter” ikinciyi gösterir. İlk sayılan stocks olduğu için daha çok düşen hisselerdir."],
 ["“The convexity adjustment increases the estimated price regardless of whether yields rise or fall.” If yields rise, the convexity adjustment is:", ["negative", "zero", "positive"], 2, "“Regardless of”: … ne olursa olsun. Getiri artsa da azalsa da düzeltme tahmini fiyatı artırır, yani pozitiftir."],
]))

# ---------------------------------------------------------------- 4
R.append(dict(id="u4", n="Olumsuzluk ve tuzak ifadeler", k="NEGATION", w=3, c="#BE185D",
terms=[
 ["neither … nor", "ne … ne de", "The analyst neither owns the stock nor covers the company.", "İkisi de olumsuz: hisseye sahip değil, şirketi de izlemiyor."],
 ["fail to", "… yapmamak; başaramamak", "The supervisor failed to investigate the complaint.", "Olumsuzluk taşır ama “not” içermez. “Fail to reject the null”: sıfır hipotezini reddedememek."],
 ["unlikely", "olası değil; muhtemel değil", "It is unlikely that the deferred tax liability will reverse.", "“Likely”nin olumsuzu. “Least likely” ile karıştırmayın: o bir soru köküdür."],
 ["lack / absent", "eksikliği / … yokken", "Absent a guarantee, the bond would be rated lower.", "“Absent X” = “without X” = X olmasaydı. “Lack of liquidity”: likidite eksikliği."],
 ["rarely / seldom / hardly", "nadiren / neredeyse hiç", "Such bonds are rarely traded on exchanges.", "Olumsuza yakın anlam taşırlar. “Hardly any” neredeyse hiç demektir; “hard” ile ilgisi yoktur."],
 ["no longer", "artık … değil", "The asset is no longer recognized on the balance sheet.", "Eskiden öyleydi, şimdi değil."],
 ["not necessarily", "ille de … değil; şart değil", "A higher return does not necessarily mean a better manager.", "Kesin bir olumsuzluk değil: olabilir de olmayabilir de."],
 ["cannot be ruled out", "ihtimali dışlanamaz", "A further downgrade cannot be ruled out.", "Çift olumsuzluk: dışlanamaz, yani mümkündür."],
 ["other than", "… dışında", "Assets other than cash are valued at fair value.", "“Except” yerine kullanılır: nakit hariç tüm varlıklar."],
 ["prohibited / permitted", "yasak / izin verilen", "Reversal of the impairment loss is prohibited under US GAAP.", "“Prohibited” = not allowed. “Permitted” = allowed. “Required” ise zorunlu demektir; “permitted” ile aynı şey değildir."],
],
notes="""<h3>“Not” içermeyen olumsuzluklar</h3>
<div class="tbl"><table>
<tr><th>İfade</th><th>Anlamı</th></tr>
<tr><td>fail to, neglect to</td><td>yapmamak</td></tr>
<tr><td>lack, absence of, absent, without</td><td>yokluğu; olmadan</td></tr>
<tr><td>unlikely, unable, unaffected, unrelated</td><td>un- ön eki olumsuz yapar</td></tr>
<tr><td>rarely, seldom, hardly, scarcely</td><td>neredeyse hiç</td></tr>
<tr><td>prohibited, forbidden, precluded</td><td>yasak</td></tr>
<tr><td>exempt from, excluded from</td><td>muaf; kapsam dışı</td></tr>
</table></div>
<h3>Çift olumsuzluk</h3>
<ul>
<li><b>not uncommon</b> = yaygın. <b>Not inconsistent with</b> = tutarlı. <b>Not unlikely</b> = olası.</li>
<li><b>cannot be rejected</b>: reddedilemez. Dikkat: bu “kabul edildi” demek değildir.</li>
<li><b>no fewer than</b> = en az. <b>No more than</b> = en fazla.</li>
</ul>
<div class="trap"><b>Sınav tuzağı</b>“Least likely” ile olumsuz bir şık yan yana gelince çift olumsuzluk oluşur. Örnek: “Which is least likely prohibited?” sorusu, yasak OLMAYAN yani izin verilen şıkkı arar. Kökü ve şıkları ayrı ayrı sadeleştirin.</div>
<h3>İzin, zorunluluk, yasak</h3>
<div class="tbl"><table>
<tr><th>İngilizce</th><th>Türkçe</th></tr>
<tr><td>must, is required to, shall</td><td>zorunlu</td></tr>
<tr><td>should, is recommended</td><td>önerilir (zorunlu değil)</td></tr>
<tr><td>may, is permitted to, is allowed to</td><td>yapabilir (izinli)</td></tr>
<tr><td>must not, may not, is prohibited from</td><td>yapamaz (yasak)</td></tr>
<tr><td>need not, is not required to</td><td>yapmak zorunda değil</td></tr>
</table></div>
<p>“May not” çoğu zaman “olmayabilir” değil, <b>yasak</b> anlamındadır: “Members may not trade on material nonpublic information.”</p>""",
qs=[
 ["“The analyst failed to disclose the conflict of interest.” The analyst:", ["disclosed the conflict", "did not disclose the conflict", "had no conflict to disclose"], 1, "“Fail to” yapmamak demektir. Analist çıkar çatışmasını açıklamamıştır."],
 ["“We fail to reject the null hypothesis.” The correct interpretation is that:", ["the null hypothesis has been proved true", "the alternative hypothesis has been accepted", "the evidence is not strong enough to reject the null"], 2, "“Fail to reject” reddedememek demektir; sıfır hipotezinin doğru olduğu kanıtlanmış olmaz. Kanıt, reddetmek için yeterince güçlü değildir."],
 ["“Members may not use material nonpublic information.” The sentence means that using such information is:", ["prohibited", "optional", "possible but unlikely"], 0, "Kural cümlelerinde “may not” yasak bildirir: üyeler önemli ve kamuya açıklanmamış bilgiyi kullanamaz."],
 ["“Absent the parent's guarantee, the subsidiary's bonds would be rated lower.” The sentence implies that the guarantee:", ["does not exist", "lowers the rating", "supports the current rating"], 2, "“Absent X” = X olmasaydı. Garanti olmasaydı not daha düşük olurdu; demek ki garanti var ve mevcut notu destekliyor."],
 ["“It is not uncommon for high-yield bonds to be secured.” Secured high-yield bonds are:", ["fairly common", "very rare", "prohibited"], 0, "Çift olumsuzluk: “not uncommon” = oldukça yaygın."],
 ["“Verification is recommended but not required.” A firm that is not verified:", ["cannot claim compliance", "can still claim compliance", "must wait five years"], 1, "“Recommended” önerilir, “required” zorunlu demektir. Doğrulama zorunlu olmadığına göre doğrulanmamış firma da uyum beyan edebilir."],
 ["“The company has no assets other than cash.” The company owns:", ["only cash", "everything except cash", "no cash"], 0, "“Other than”: … dışında. Nakit dışında varlığı yok, yani yalnızca nakdi var."],
 ["“The bond is neither callable nor putable.” The bond has:", ["a call feature only", "both a call and a put feature", "no embedded option"], 2, "“Neither … nor”: ne … ne de. Tahvil ne geri çağrılabilir ne de geri satılabilir; gömülü opsiyonu yoktur."],
]))

# ---------------------------------------------------------------- 5
R.append(dict(id="u5", n="Zaman ve koşul ifadeleri", k="TIME & CONDITIONALS", w=3, c="#6D28D9",
terms=[
 ["prior to / subsequent to", "… den önce / … den sonra", "The dividend was declared prior to the year-end and paid subsequent to it.", "“Prior to” = before. “Subsequent to” = after. “Subsequently”: daha sonra."],
 ["at inception / at initiation", "başlangıçta; sözleşme kurulurken", "At initiation, the value of a forward contract is zero.", "Sözleşmenin ilk günü. Karşıtı: “at expiration” ya da “at maturity”."],
 ["at maturity / at expiration", "vadede / vade sonunda", "The principal is repaid at maturity.", "Tahvil ve kredilerde “maturity”, opsiyon ve vadeli işlemlerde “expiration” kullanılır."],
 ["as of", "… tarihi itibarıyla", "As of 31 December, total debt was 500 million.", "Belirli bir andaki durumu verir; bilanço kalemleri “as of” ile, gelir tablosu kalemleri “for the year ended” ile anlatılır."],
 ["year-over-year", "yıllık bazda; geçen yılın aynı dönemine göre", "Revenue grew 8% year-over-year.", "“YoY” diye kısaltılır. “Quarter-over-quarter” çeyreklik karşılaştırmadır."],
 ["to date", "bugüne kadar", "The fund has distributed 30 million to date.", "“Year to date (YTD)”: yıl başından bugüne."],
 ["trailing / forward", "geçmiş 12 aya dayalı / gelecek tahmine dayalı", "The trailing P/E is 15, and the forward P/E is 12.", "“Trailing” gerçekleşmiş son 12 ayı, “forward” beklenen gelecek 12 ayı kullanır."],
 ["upon", "… üzerine; … olduğunda", "Upon default, bondholders may seize the collateral.", "“Upon X” = X gerçekleştiği anda."],
 ["would have", "… olurdu (ama olmadı)", "If the firm had used FIFO, its income would have been higher.", "Gerçekleşmemiş geçmiş durum. Firma FIFO kullanmadı; kullansaydı kâr daha yüksek olurdu."],
 ["due / overdue / past due", "vadesi gelen / vadesi geçmiş", "Receivables more than 90 days past due are written off.", "“Due in 30 days”: 30 gün içinde ödenecek. “Past due” ve “overdue”: vadesi geçmiş."],
],
notes="""<h3>Zamanı gösteren kelimeler</h3>
<div class="tbl"><table>
<tr><th>Önce</th><th>Aynı anda</th><th>Sonra</th></tr>
<tr><td>prior to, before, previously, formerly, preceding</td><td>upon, when, as, at the time of, simultaneously</td><td>subsequent to, after, following, thereafter, later</td></tr>
</table></div>
<ul>
<li><b>Current</b>: cari, mevcut. <b>Current year</b> bu yıl, <b>prior year</b> geçen yıl.</li>
<li><b>Beginning / ending</b>: dönem başı / dönem sonu. “Beginning inventory”, “ending balance”.</li>
<li><b>Annual, semiannual, quarterly, monthly</b>: yıllık, altı aylık, üç aylık, aylık.</li>
<li><b>Per annum</b> = yıllık. <b>Annualized</b> = yıllıklandırılmış.</li>
</ul>
<h3>Koşul cümleleri</h3>
<div class="tbl"><table>
<tr><th>Yapı</th><th>Anlamı</th><th>Örnek</th></tr>
<tr><td>If + present, will</td><td>Gerçek olasılık</td><td>If rates rise, the price will fall.</td></tr>
<tr><td>If + past, would</td><td>Varsayım</td><td>If rates rose by 1%, the price would fall by 5%.</td></tr>
<tr><td>If + had, would have</td><td>Olmamış geçmiş</td><td>If rates had risen, the price would have fallen.</td></tr>
</table></div>
<div class="trap"><b>Sınav tuzağı</b>“Would have been higher” gördüğünüzde olay gerçekleşmemiştir. Soru, gerçekte kullanılan yöntem ile kullanılmayan yöntemi karşılaştırmanızı ister.</div>
<h3>Stok ve akım</h3>
<ul>
<li><b>As of / at</b> bir andaki durumu verir: bilanço. “Total assets at year-end”.</li>
<li><b>For the year / during the period</b> bir dönemi verir: gelir tablosu ve nakit akışı. “Revenue for the year”.</li>
<li><b>Average</b> dönem başı ile dönem sonunun ortalamasıdır; oranlarda bilanço kalemi çoğu zaman “average” alınır.</li>
</ul>""",
qs=[
 ["“If the company had capitalized the cost, its net income would have been higher.” What did the company actually do?", ["It capitalized the cost", "It expensed the cost", "It has not yet decided"], 1, "“Had … would have” gerçekleşmemiş bir geçmişi anlatır. Şirket aktifleştirmedi, yani giderleştirdi; aktifleştirseydi kârı daha yüksek olurdu."],
 ["“At initiation, the value of the forward contract is zero.” The phrase “at initiation” refers to:", ["the day the contract is agreed", "the day the contract expires", "any day during the contract's life"], 0, "“At initiation” = “at inception”: sözleşmenin kurulduğu gün. Vade sonu için “at expiration” denir."],
 ["“The trailing P/E is 15 and the forward P/E is 12.” The forward P/E is based on:", ["earnings of the last 12 months", "expected earnings of the next 12 months", "average earnings of the last 10 years"], 1, "“Forward” beklenen gelecek kârı, “trailing” gerçekleşmiş son 12 ayın kârını kullanır."],
 ["“Subsequent to the balance sheet date, the company issued new shares.” The shares were issued:", ["before the balance sheet date", "on the balance sheet date", "after the balance sheet date"], 2, "“Subsequent to” = after. Paylar bilanço tarihinden sonra ihraç edilmiştir."],
 ["“Upon default, the lender may take possession of the collateral.” The lender may take the collateral:", ["at any time", "only at maturity", "when default occurs"], 2, "“Upon X”: X gerçekleştiğinde. Borç veren teminata temerrüt gerçekleştiği anda el koyabilir."],
 ["“Total debt was 500 million as of 31 December; interest expense for the year was 30 million.” Which item describes a period, not a point in time?", ["Total debt", "Interest expense", "Both items"], 1, "“As of” bir andaki durumu (bilanço), “for the year” bir dönemi (gelir tablosu) verir. Dönemi anlatan faiz gideridir."],
 ["“Receivables more than 90 days past due are written off.” A receivable that was due 120 days ago and is still unpaid is:", ["not yet due", "written off", "paid early"], 1, "“Past due”: vadesi geçmiş. Vadesi 120 gün önce dolmuş ve ödenmemiş alacak 90 günü aştığı için kayıtlardan silinir."],
]))

# ---------------------------------------------------------------- 6
R.append(dict(id="u6", n="Karıştırılan kelimeler", k="FALSE FRIENDS", w=3, c="#15803D",
terms=[
 ["security", "menkul kıymet (güvenlik değil)", "The fund invests in fixed-income securities.", "Finans metninde “security” menkul kıymettir. “Secured bond” ise teminatlı tahvildir."],
 ["equity", "özkaynak; hisse senedi", "Return on equity is net income divided by average equity.", "Bilançoda özkaynak, piyasada hisse senedi anlamına gelir. Hakkaniyet anlamı sınavda geçmez."],
 ["interest", "faiz; pay, çıkar", "The fund holds a controlling interest in the company.", "“Interest rate” faiz oranıdır. “Controlling interest” kontrol payı, “conflict of interest” çıkar çatışmasıdır."],
 ["outstanding", "tedavüldeki; ödenmemiş", "The company has 10 million shares outstanding.", "“Shares outstanding”: tedavüldeki paylar. “Outstanding debt”: ödenmemiş borç. “Olağanüstü” anlamı sınavda geçmez."],
 ["stock", "hisse senedi; stok", "Common stock is reported in equity; in British usage, stock can mean inventory.", "ABD kullanımında hisse senedi. Envanter için sınav “inventory” der."],
 ["yield / return", "getiri oranı (yield) / getiri (return)", "The bond's yield is 5%, but its return over the year was −2%.", "“Yield” tahvilin fiyatından hesaplanan vaat edilen orandır; “return” dönemde gerçekleşen toplam kazançtır."],
 ["revenue / income / earnings", "hasılat / gelir, kâr / kâr", "Revenue was 1,000 and net income was 60.", "“Revenue” ve “sales” en üst satırdır. “Net income”, “earnings” ve “profit” en alt satırdır: net kâr."],
 ["principal / principle", "anapara; asıl / ilke", "The principal is repaid at maturity. The Code sets out ethical principles.", "Yazımı benzer, anlamı ayrı. “Principal” ayrıca vekalet ilişkisindeki asildir (principal–agent)."],
 ["lend / borrow", "borç vermek / borç almak", "Banks lend to companies; companies borrow from banks.", "Yön zıttır. “Lender” borç veren, “borrower” borç alandır."],
 ["issue", "ihraç etmek; ihraç; konu", "The company issued bonds. The issue was rated AA.", "Fiil: ihraç etmek. İsim: ihraç edilen menkul kıymet. “Issuer” ihraççıdır."],
 ["premium / discount", "prim / iskonto", "The bond trades at a premium to par; the closed-end fund trades at a discount.", "“At a premium”: nominalin ya da değerin üstünde. “At a discount”: altında. “Option premium” opsiyonun fiyatıdır."],
 ["liability", "yükümlülük; borç", "Deferred tax liabilities are reported on the balance sheet.", "Bilançonun pasif tarafındaki borçlardır. “Limited liability” sınırlı sorumluluk demektir."],
],
notes="""<h3>Günlük anlamı ile finans anlamı farklı olan kelimeler</h3>
<div class="tbl"><table>
<tr><th>Kelime</th><th>Günlük anlam</th><th>Sınavdaki anlam</th></tr>
<tr><td>security</td><td>güvenlik</td><td>menkul kıymet</td></tr>
<tr><td>outstanding</td><td>olağanüstü</td><td>tedavüldeki; ödenmemiş</td></tr>
<tr><td>mature</td><td>olgun</td><td>vadesi dolmak</td></tr>
<tr><td>appreciate</td><td>takdir etmek</td><td>değer kazanmak</td></tr>
<tr><td>note</td><td>not</td><td>senet; orta vadeli borçlanma aracı; dipnot</td></tr>
<tr><td>bill</td><td>fatura</td><td>kısa vadeli hazine bonosu</td></tr>
<tr><td>charge</td><td>şarj; suçlama</td><td>gider; ücret; borç kaydı</td></tr>
<tr><td>turnover</td><td>devir</td><td>devir hızı (oran); İngiliz kullanımında ciro</td></tr>
<tr><td>position</td><td>konum</td><td>pozisyon: long (alım) ya da short (açığa satış)</td></tr>
</table></div>
<h3>Gelir tablosunda yukarıdan aşağıya</h3>
<p class="f">Revenue (sales) → hasılat<br>− Cost of goods sold → satışların maliyeti<br>= Gross profit → brüt kâr<br>− Operating expenses → faaliyet giderleri<br>= Operating income (EBIT) → faaliyet kârı<br>− Interest expense → faiz gideri<br>= Pretax income → vergi öncesi kâr<br>− Income tax expense → vergi gideri<br>= Net income (earnings, profit) → net kâr</p>
<div class="trap"><b>Sınav tuzağı</b>“Income” tek başına hasılat değildir. “Net income” net kârdır; hasılat için “revenue” ya da “sales” kullanılır. “Earnings per share” de hasılat değil, pay başına net kârdır.</div>
<h3>Yönü zıt çiftler</h3>
<ul>
<li><b>lend / borrow</b>: borç vermek / almak. <b>Lessor / lessee</b>: kiraya veren / kiracı.</li>
<li><b>buyer / seller</b> ve opsiyonda <b>holder (long) / writer (short)</b>: alan / yazan.</li>
<li><b>payable / receivable</b>: borç / alacak. <b>Accounts payable</b> ticari borçlar, <b>accounts receivable</b> ticari alacaklardır.</li>
<li><b>overstate / understate</b>: olduğundan yüksek / düşük göstermek.</li>
<li><b>creditor / debtor</b>: alacaklı / borçlu.</li>
</ul>""",
qs=[
 ["“The company has 10 million shares outstanding.” The word “outstanding” means that the shares are:", ["of exceptional quality", "issued and held by investors", "not yet paid for"], 1, "“Shares outstanding”: tedavüldeki paylar, yani ihraç edilmiş ve yatırımcıların elinde olan paylar. “Olağanüstü” anlamı burada geçerli değildir."],
 ["“The fund invests mainly in government securities.” The fund buys:", ["bonds and bills issued by the government", "security services for the government", "government insurance policies"], 0, "“Security” menkul kıymettir. “Government securities” devletin ihraç ettiği tahvil ve bonolardır."],
 ["“The euro appreciated against the dollar.” The euro:", ["was praised by investors", "lost value", "gained value"], 2, "“Appreciate” finans metninde değer kazanmak demektir. Karşıtı “depreciate”: değer kaybetmek."],
 ["A company reports revenue of 1,000, cost of goods sold of 600, operating expenses of 250 and no other items. Its operating income is:", ["150", "400", "750"], 0, "Revenue − COGS = brüt kâr 400; faaliyet giderleri düşülünce faaliyet kârı 150. 400 şıkkı “gross profit”tir, “operating income” değil."],
 ["“The bank lends at 6% and borrows at 4%.” On the money it lends, the bank:", ["pays 6%", "receives 6%", "receives 4%"], 1, "“Lend” borç vermektir. Banka verdiği kredi için %6 faiz alır; %4, borçlandığı fon için ödediği orandır."],
 ["“The bond matures in 2030 and trades at a premium.” The sentence says that the bond:", ["becomes more stable in 2030 and pays an option premium", "is repaid in 2030 and its price is above par", "is issued in 2030 at a price below par"], 1, "“Mature”: vadesi dolmak. “At a premium”: nominal değerin üstünde. Tahvil 2030'da itfa edilir ve fiyatı nominalin üzerindedir."],
 ["“Management overstated inventory.” Compared with its true value, reported inventory is:", ["too low", "correct", "too high"], 2, "“Overstate”: olduğundan yüksek göstermek. Raporlanan stok gerçek değerinin üzerindedir. Karşıtı “understate”."],
 ["“The lessee records a right-of-use asset.” The lessee is the party that:", ["owns the asset and rents it out", "uses the asset and makes lease payments", "finances the purchase for the owner"], 1, "“Lessee” kiracıdır: varlığı kullanır ve kira öder. Varlığın sahibi olup kiraya veren taraf “lessor”dur."],
]))

# ---------------------------------------------------------------- 7
R.append(dict(id="u7", n="Muhasebe ve piyasa fiilleri", k="KEY VERBS", w=3, c="#1D4ED8",
terms=[
 ["recognize", "kayda almak; muhasebeleştirmek", "Revenue is recognized when the performance obligation is satisfied.", "Bir kalemin finansal tablolara girmesi. “Tanımak” anlamı burada geçerli değildir. Karşıtı: derecognize."],
 ["accrue / defer", "tahakkuk ettirmek / ertelemek", "Interest accrues daily. The gain is deferred until the asset is sold.", "“Accrued expense”: tahakkuk etmiş, henüz ödenmemiş gider. “Deferred revenue”: peşin alınmış, henüz kazanılmamış gelir."],
 ["capitalize / expense", "aktifleştirmek / giderleştirmek", "Development costs are capitalized; research costs are expensed.", "Aktifleştirilen harcama bilançoya varlık olarak girer; giderleştirilen doğrudan gelir tablosuna yazılır."],
 ["depreciate / amortize", "amortisman ayırmak (maddi) / itfa etmek (maddi olmayan)", "Equipment is depreciated over ten years; patents are amortized.", "Maddi duran varlıkta “depreciation”, maddi olmayan varlıkta ve borçta “amortization” kullanılır."],
 ["impair / write down", "değer düşüklüğü kaydetmek / değerini düşürmek", "Goodwill was impaired by 40 million.", "Varlığın defter değerinin geri kazanılabilir tutara indirilmesi. “Write off” tamamen silmek demektir."],
 ["incur", "(gider, zarar) üstlenmek; katlanmak", "The company incurred restructuring costs of 15 million.", "Giderin doğduğu anı anlatır; ödenmiş olması gerekmez."],
 ["redeem / retire", "itfa etmek; geri ödemek", "The issuer redeemed the bonds at par.", "Tahvilin ihraççı tarafından geri alınması ya da ödenmesi. “Call” erken itfa hakkıdır."],
 ["hedge", "korunmak; riski dengelemek", "The exporter hedged its currency exposure with a forward contract.", "Bir riskin zıt yönlü bir pozisyonla azaltılması. “Unhedged” korunmasız demektir."],
 ["default", "temerrüde düşmek; temerrüt", "The issuer defaulted on its interest payment.", "Borcun ödenmemesi. “Default rate” temerrüt oranıdır. Bilgisayardaki “varsayılan” anlamı burada geçmez."],
 ["exercise / expire", "(opsiyonu) kullanmak / süresi dolmak", "The option expired worthless because it was not exercised.", "“Exercise price” kullanım fiyatıdır. “Expire worthless”: değersiz olarak sona ermek."],
 ["pledge", "rehnetmek; teminat göstermek", "The company pledged its receivables as collateral.", "Bir varlığın borca karşılık teminat verilmesi. “Collateral” teminatın kendisidir."],
 ["settle", "takas etmek; ödeyerek kapatmak", "The contract is settled in cash at expiration.", "“Cash settlement” nakdi uzlaşma, “physical delivery” fiziki teslimdir. “Settlement date” takas tarihidir."],
],
notes="""<h3>Bir harcamanın yolculuğu</h3>
<div class="tbl"><table>
<tr><th>Fiil</th><th>Ne olur</th><th>Tablo</th></tr>
<tr><td>incur</td><td>Gider ya da maliyet doğar</td><td>Henüz belli değil</td></tr>
<tr><td>capitalize</td><td>Varlık olarak kaydedilir</td><td>Bilanço</td></tr>
<tr><td>depreciate / amortize</td><td>Yıllara yayılarak gidere dönüşür</td><td>Gelir tablosu, her yıl</td></tr>
<tr><td>expense</td><td>Doğduğu yıl tamamı gider yazılır</td><td>Gelir tablosu, tek seferde</td></tr>
<tr><td>impair / write down</td><td>Değeri düşerse defter değeri indirilir</td><td>Gelir tablosunda zarar</td></tr>
<tr><td>derecognize</td><td>Satılınca ya da hurdaya ayrılınca kayıttan çıkar</td><td>Bilançodan silinir</td></tr>
</table></div>
<h3>Tahakkuk ve erteleme</h3>
<ul>
<li><b>Accrued revenue</b>: kazanılmış, tahsil edilmemiş gelir (varlık). <b>Accrued expense</b>: doğmuş, ödenmemiş gider (yükümlülük).</li>
<li><b>Deferred (unearned) revenue</b>: tahsil edilmiş, kazanılmamış gelir (yükümlülük). <b>Prepaid expense</b>: ödenmiş, henüz kullanılmamış gider (varlık).</li>
</ul>
<div class="trap"><b>Sınav tuzağı</b>“Recognize” ile “realize” aynı şey değildir. “Unrealized gain” satış yapılmadan oluşan değer artışıdır; kayda alınmış (recognized) olabilir ama nakde dönmemiştir.</div>
<h3>Bir tahvilin ve bir opsiyonun hayatı</h3>
<p class="f">Bond: issue → trade → pay coupons → (call / put) → mature → redeem<br>Option: write (sell) / buy → hold → exercise <i>or</i> expire → settle</p>
<ul>
<li><b>Underwrite</b>: ihraca aracılık etmek, yüklenmek. <b>Roll over</b>: vadesi gelen borcu yenisiyle çevirmek.</li>
<li><b>Go long / go short</b>: alım / açığa satış pozisyonu almak. <b>Close out</b>: pozisyonu kapatmak.</li>
<li><b>Post margin</b>: teminat yatırmak. <b>Mark to market</b>: piyasa fiyatıyla günlük değerlemek.</li>
</ul>""",
qs=[
 ["“The company capitalized 20 million of development costs.” In the year of the spending, the 20 million appears mainly:", ["as an expense on the income statement", "as an asset on the balance sheet", "as a liability on the balance sheet"], 1, "“Capitalize” aktifleştirmek demektir: harcama bilançoda varlık olarak görünür ve sonraki yıllarda itfa edilerek gidere dönüşür."],
 ["“The firm received cash in advance and recorded deferred revenue.” Deferred revenue is:", ["revenue already earned but not collected", "cash collected but not yet earned", "an expense paid in advance"], 1, "“Deferred (unearned) revenue”: tahsil edilmiş ama henüz kazanılmamış gelir. Bir yükümlülüktür; hizmet verildikçe gelire dönüşür."],
 ["“The option expired worthless.” The option holder:", ["exercised the option at a profit", "sold the underlying asset", "did not exercise and lost the premium"], 2, "“Expire worthless”: değersiz olarak sona ermek. Opsiyon kullanılmamıştır; alıcının zararı ödediği primdir."],
 ["“The issuer defaulted on the coupon payment.” The issuer:", ["paid the coupon early", "chose the standard payment option", "did not pay the coupon when due"], 2, "“Default”: temerrüt. İhraççı kupon ödemesini vadesinde yapmamıştır."],
 ["“Goodwill was written down by 40 million.” As a result, reported net income for the period is:", ["higher by 40 million before tax", "lower by 40 million before tax", "unchanged"], 1, "“Write down” değerini düşürmek demektir; değer düşüklüğü zararı gelir tablosuna yazılır ve vergi öncesi kârı 40 milyon azaltır."],
 ["“The exporter hedged its dollar receivable with a forward contract.” The purpose of the forward is to:", ["increase the exposure to the dollar", "speculate on a rise in the dollar", "reduce the risk from changes in the exchange rate"], 2, "“Hedge”: korunmak. Forward, dolar alacağının kur değişiminden etkilenmesini azaltmak için kullanılmıştır."],
 ["“Interest of 3 million has accrued but has not been paid.” On the balance sheet, the 3 million is:", ["a liability", "a prepaid asset", "not shown at all"], 0, "“Accrued” tahakkuk etmiş demektir. Doğmuş ama ödenmemiş faiz bir yükümlülüktür (accrued interest payable)."],
 ["“The company pledged its inventory as collateral for the loan.” If the company defaults, the lender:", ["has a claim on the inventory", "must buy the inventory at cost", "loses its claim on the inventory"], 0, "“Pledge … as collateral”: teminat olarak rehnetmek. Temerrüt halinde borç verenin stoklar üzerinde hakkı vardır."],
]))

# ---------------------------------------------------------------- 8
R.append(dict(id="u8", n="Ethics sorularının dili", k="ETHICS LANGUAGE", w=3, c="#7C3AED",
terms=[
 ["violate / comply with", "ihlal etmek / uymak", "Did the analyst violate the Standards? She complied with the firm's policy.", "“Violation”: ihlal. “In compliance with”: … e uygun. “Breach” da ihlal demektir."],
 ["disclose", "açıklamak; bildirmek", "Members must disclose conflicts of interest to clients and to their employer.", "Ethics'in en sık geçen fiili. “Full disclosure”: tam açıklama. “Undisclosed”: açıklanmamış."],
 ["misrepresent", "yanlış beyan etmek; yanıltmak", "The manager misrepresented the fund's past performance.", "Gerçeği çarpıtmak ya da eksik göstermek. İsim hali: misrepresentation."],
 ["material", "önemli; fiyatı etkileyebilecek", "Material nonpublic information must not be used for trading.", "Makul bir yatırımcının kararını etkileyecek bilgi. “Malzeme” anlamı burada geçmez."],
 ["conflict of interest", "çıkar çatışması", "Owning shares in a company she covers creates a conflict of interest.", "Kişisel çıkarın müşteriye ya da işverene karşı görevle çatışması."],
 ["due diligence", "gerekli özen; ön inceleme", "The analyst performed due diligence before recommending the fund.", "Bir yatırımı önermeden önce yapılan dikkatli inceleme. “Diligence” tek başına özen demektir."],
 ["reasonable basis", "makul dayanak", "A recommendation must have a reasonable and adequate basis.", "Önerinin yeterli araştırma ve kanıta dayanması."],
 ["solicit", "(müşteri) kazanmaya çalışmak; talep etmek", "She may not solicit her employer's clients before leaving.", "İşten ayrılma vakalarının anahtar kelimesi. “Unsolicited request”: müşteriden kendiliğinden gelen talep."],
 ["on behalf of", "… adına", "The manager votes proxies on behalf of clients.", "Başkası için hareket etmek. “In the best interest of”: … in çıkarına en uygun biçimde."],
 ["fiduciary duty", "güvene dayalı özen ve sadakat yükümlülüğü", "A trustee owes a fiduciary duty to the plan's beneficiaries.", "Başkasının varlığını yöneten kişinin o kişinin çıkarını kendi çıkarının önüne koyma borcu."],
 ["written consent", "yazılı izin; yazılı onay", "Additional compensation requires written consent from all parties.", "“Obtain consent”: onay almak. “Prior consent”: önceden alınan onay."],
 ["dissociate", "kendini ayırmak; ilişiğini kesmek", "A member who learns of a violation must dissociate from the activity.", "İhlalden haberdar olan üyenin o faaliyetle bağını kesmesi; gerekirse görevden çekilmesi."],
],
notes="""<h3>Bir Ethics sorusunu okumak</h3>
<ul>
<li>Soru kısa bir hikâyedir. Önce son cümleyi okuyun: <b>“violated”</b> mi soruluyor, <b>“most appropriate action”</b> mı?</li>
<li>Hikâyede birden fazla kişi olabilir. Sorunun kimi sorduğunu (analyst, supervisor, firm) işaretleyin.</li>
<li>Her olgu ihlal değildir. Yanlış şıklar çoğu zaman tamamen kurallara uygun bir davranışı ihlal gibi gösterir.</li>
</ul>
<h3>Zorunluluk derecesi</h3>
<div class="tbl"><table>
<tr><th>İfade</th><th>Anlamı</th></tr>
<tr><td>must, is required to</td><td>Standardın şartı; yapılmazsa ihlal</td></tr>
<tr><td>should, is recommended, is encouraged to</td><td>Tavsiye; yapılmaması tek başına ihlal değil</td></tr>
<tr><td>must not, may not, is prohibited from</td><td>Yasak</td></tr>
<tr><td>may</td><td>İzinli; isteğe bağlı</td></tr>
</table></div>
<div class="trap"><b>Sınav tuzağı</b>“Recommended procedures” ile “requirements” farklıdır. Standards of Practice Handbook'taki tavsiyeleri uygulamamak tek başına ihlal sayılmaz; şıkta “required” yazıyorsa şüphelenin.</div>
<h3>Sık geçen kalıplar</h3>
<ul>
<li><b>in the best interest of the client</b>: müşterinin çıkarına en uygun biçimde</li>
<li><b>place the client's interests before their own</b>: müşterinin çıkarını kendi çıkarının önüne koymak</li>
<li><b>act with reasonable care and prudence</b>: makul özen ve basiretle hareket etmek</li>
<li><b>make full and fair disclosure</b>: tam ve adil açıklama yapmak</li>
<li><b>knowingly</b>: bilerek. “Knowingly participate”: bilerek katılmak. Bilmeden yapılan ile bilerek yapılan ayrılır.</li>
<li><b>front-running</b>: müşteri emrinden önce kendi hesabına işlem yapmak. <b>Churning</b>: komisyon için gereksiz işlem yapmak.</li>
<li><b>whistleblowing</b>: işverenin hukuka aykırı davranışını yetkililere bildirmek.</li>
</ul>""",
qs=[
 ["“Smith least likely violated the Standards by:” Bu soruda aranan şık hangisidir?", ["Smith'in en ağır ihlali", "Smith'in ihlal sayılmayan davranışı", "Smith'in işvereninin ihlali"], 1, "“Least likely violated”: en az olasılıkla ihlal etti. İki şık ihlaldir; aranan, kurallara uygun olan davranıştır."],
 ["“The information is material and nonpublic.” In this sentence, “material” means that the information:", ["is printed on paper", "concerns raw materials", "would likely affect the security's price"], 2, "“Material”: önemli. Makul bir yatırımcının kararını ya da menkul kıymetin fiyatını etkileyebilecek bilgi demektir."],
 ["“Additional compensation requires written consent from all parties involved.” A manager accepts a client's bonus offer after telling her employer about it by phone. She has:", ["complied, because the employer was informed", "not complied, because the consent was not in writing", "complied, because bonuses are always allowed"], 1, "“Written consent”: yazılı onay. İşverene telefonla haber vermek yazılı onay almak değildir; şart yerine gelmemiştir."],
 ["“Jones solicited his employer's clients before resigning.” Jones:", ["tried to win the clients for his new business", "informed the clients about market risks", "transferred the clients to a colleague"], 0, "“Solicit”: müşteri kazanmaya çalışmak. Jones istifa etmeden önce işvereninin müşterilerini kendi işine çekmeye çalışmıştır; bu IV(A) ihlalidir."],
 ["“The firm should adopt a restricted list.” The word “should” indicates that a restricted list is:", ["recommended", "required", "prohibited"], 0, "“Should” tavsiye bildirir. Zorunluluk için “must” ya da “is required to” kullanılır."],
 ["“The manager votes proxies on behalf of her clients.” The manager votes:", ["against her clients", "after her clients have voted", "for her clients, as their representative"], 2, "“On behalf of”: … adına. Yönetici oy hakkını müşterileri adına, onların temsilcisi olarak kullanır."],
 ["“Lee knowingly participated in the misrepresentation.” The word “knowingly” tells us that Lee:", ["was unaware of the misrepresentation", "was aware of it and took part anyway", "reported it to the authorities"], 1, "“Knowingly”: bilerek. Lee yanlış beyanın farkındaydı ve yine de katıldı; bu, sorumluluğunu ağırlaştırır."],
 ["“The analyst failed to disclose that she owns shares in the company.” Which Standard is most directly involved?", ["Disclosure of Conflicts", "Record Retention", "Performance Presentation"], 0, "Şirkette pay sahibi olmak bir çıkar çatışmasıdır ve açıklanması gerekir. “Failed to disclose” açıklamadığını söyler: VI(A) Disclosure of Conflicts."],
]))
