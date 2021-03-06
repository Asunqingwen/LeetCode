"""
给定字符串 S and T，找出 S 中最短的（连续）子串 W ，使得 T 是 W 的 子序列 。

如果 S 中没有窗口可以包含 T 中的所有字符，返回空字符串 ""。如果有不止一个最短长度的窗口，返回开始位置最靠左的那个。

示例 1：

输入：
S = "abcdebdde", T = "bde"
输出："bcde"
解释：
"bcde" 是答案，因为它在相同长度的字符串 "bdde" 出现之前。
"deb" 不是一个更短的答案，因为在窗口中必须按顺序出现 T 中的元素。
 

注：

所有输入的字符串都只包含小写字母。All the strings in the input will only contain lowercase letters.
S 长度的范围为 [1, 20000]。
T 长度的范围为 [1, 100]。
"""


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # 滑动窗口，往后拉到满足T是W的子串，得出满足可能W窗口；往前推到T是W的子串，得出最小长度

        ans = len(S) + 1
        start, end = -1, -1

        point1, point2 = 0, 0
        while point1 < len(S):
            if S[point1] == T[point2]:
                point2 += 1
            if point2 == len(T):
                # 找到满足条件的窗口了，往前推，得到最小窗口长度
                right = point1  # 先把这个end位置记下来
                point2 -= 1  # 这个玩意儿先归位把
                while point2 >= 0:
                    if S[point1] == T[point2]:
                        point2 -= 1
                    point1 -= 1
                # 跳出循环了，这个时候point2指向-1，而point1指向start - 1
                if right - point1 < ans:
                    ans = right - point1
                    start = point1 + 1
                    end = right + 1
                # 继续走，point1先+1归位，然后再加1，要换下一个开始标志了。
                point1 += 1
            point1 += 1

        if ans == len(S) + 1:
            return ""
        else:
            return S[start: end]


if __name__ == '__main__':
    S = "cnktshvvjnnwftckuerryorwnpirtxjgvzxyfxmnwtcrwdycwdndcguzzvziachknezyxsefcxdjnmncuzgeosxrswnkfsoioezgwwnhkfpruwvleohnhgdcrhljvuxovajjpznmemjefmzxcfycskqwiqybpjzqdnqgvqaaxfhobugozbccxlvzwyedqcdilzrqaxqalggwjoyzexdtxadjbtryuxzhplvihxewahnldiuvvfajnmtiwbrkumvepnwvufxhbwkravnbwhjtgigngxohbtuakxhftttyluatnasevhpxcgiqertakkldcojqyvqwtbowliufswqfzmtcgoaejgnwtwobrskkzbmsspcpveqrhfertkeitdomceozpdrfeemfgggzwfywvlovkpsxwhmgfhlqjlkmpraerxlnmkhjciziivtrvbduapionqlmgbgbrmpavvsfvmbgtczxitctsuqskkmfcsrmvbgoygkawcxxccpzefzddtajwnlwjvfvhegwyforoymslmynhexdvftlhvstybaboduqcjwcrbmtonvdfvjthyaukrddvvypdxbavtavdzlzejyayevkneupnafnvmdekmloeowmrppvlzpdtoszxqbsbugmjjcorsvmbcydzmzegoypqkfsjutadgdthbfgxnrnqacmagdmmhqcoxdvsocmwdopvyfsthczdyzxnrpdysagsuvecbpodjsvgfyohcotnabrnbbtgfmvlkxfietcpwiwlwloxskwfesezaozkdmwqmccqstctvrmijxsndduiqphtkbqnhmimfmfigkwanhglnvegxpswsplscnumykeyeeguvybhjqsalaajpxuucglrsxuccuussnlgmovkwpclajxwqpekpsklhhnmcdpdtrtmlyxhwzebvesjjgirfpvwyscwgkesahngjahacftxxoyevubhxlcsrpyxjwyyzdgsavkfkmoxrhjzvnquutgncyedgcmkhlomkdjjhnhbiefgnnyiqbhzkwfefgnzdyuhnecwgeqimempikgswvhnfewstpuvxwewgdlmeeicqqifmsxjjclwjsjctkeveuqfryqyuvahtxybgdufvdtaefnvnrooiofmesjypuegncrtvqhxussokaraopboqnngqebuueolxulrmwfdihjplfmiottohagheohyhsndmaldbupcqiflsklhhhubmpybgzggmsjhrhydjzgbyeljdzxlkzzdjqfngetkvkystbcetaxmycdsygtwvjvieehtetvtelxhldbcjnuawdoepicnitdymznrykpmpiexquobsaqylguwbdnulupzuchkxfpxrtjmecuckcigucggzieergyxhfmuiaaudnebsjpcrekmibkxylejpcmcmyivavsnbzoairaiafvikymdndjbqzkbdpzbenzhtnloqqkwtsvchejngxravpfwmcppdkoxsxcxwwursdcpqxrcbbtkammzpalutgkhlfegafzfusbtfzfdlpeyljiaqqddwtopkjmpllfacqwckirhwiqudfomcbhhroftcgrlekzmxxhhhinqwayyjbanmekzagyghkhzkmokhoojotfnznamekmhqptnkkqzcalhuiqsnpedcmowfjkyfhqjpsuowwrpdgxqcvyeuvijckhkoxeslqzexovcliqkkewdlzxveurjycsjrpubfxjcutvmniqnzdakwbdrwxxnmpzityozccozzmrunjgzryylaqpfuqxaqmrzpwjcfgscupkavzrocuizmmmffgzselluxhrgzizokacdsoaovdbeovbezzvrdsscofwkbiasytokpylwxmroekjyodhlulubkkjuxtcatmcjknpjeeuuysrmtfjvduqyifvpcjkcqoobdpdtcvsgtkjfghaelzpqytixemppcqrkfhwdilbkurywafiwbqeywcqyniypdxgcyfhkmmnnycaonwgsqwwswkkjkkofyjxiihaeswxjlglcmzghxdjvkhadjxatyqcsvtmvyrbjadlnvwsrmadgqnmkxmkoqfiydubdzxspyygmjiaorkfcxlsktcqtwojngoxfzjjdnupbfvagukavprsseanygyhywtixtxqochiiizchyusfwzktfwgcuvfjgcwqvwgsdwkodtpphxxddtdzionwqttvrsocpkhpgljvhdzgfmfgirszfpignwnkrxuccmqcljpdlgaxnfiaeeadrkqxegfedbpnjnpyobactbjoqfppkhiicohesrhjunplsmipuhxfsaumeqcrukxhfoacvobqavodstisklsxjwqtfbhycmleycdomvakdkbduzwksmgfjcdansworblcpvnzzfgzpmelictpyuqchonlduzfltlbskpfqrisshtaambszqqergfeefkvkiogrgwknepimwoqoxbdjdyisxeocdjocqqqcxemiuzzburlxzogsjcylrpgsmqgwzyynvxjxglfyerlfmzogaznhkkspcsomvvixpukzifbflzkcdfmeaxvwuhxszzmdxujtgqpphnmsuhjzszvsnvsykuokzwauiytajvohmmmwbyikmzwpcyodaxdonkeczgcmedfkoafpnclvhspddcpycrtlvqihxvtefrwmmkbpujccauhdsnlidiekgnxgwiwbimrdbwxqdosqoczluwzpaiunibzrewyopculgbhzjxqzdqgrfkrhslxvdvxypxaxjphqcoujfkalcfjopujlgowbsoctvqxdlkoceyngwtauwxcivwezgorjnkwacuyvyhlndztnxkqwflmqyoxnhtbzfzsoglazflewfqzixlvzmmrmihuexgehifhsbrvqeafdmjixgrzqsxppnvlcrmzxoufkfihwxkpimwwcdlldvdifigzfqhknxqmbaqdriyoztlniywvgjvcoaprfgwlwvwmddsxtlzvxhhmqhktlpmfdtiqnzbpqaclxtddwhpqdnkswoldhgcldcuaxvtieygsjmjgokfmmyfxvzryvluovavzhobgwrmkceqayvkwsvxtksqqxgfgadazgfmhgdsxjqakcuapfqggoumfoqugazlvnupwneheathmofbsqqilrbyvcnejjvknktenkmwvzocyrxwifjhrtkkvvyhloqnjyqmiaarrunwpxlttzvgvbicbktedyxdzwdooghxapvydbxiwmgvykfoylyxvxajpjemwvgygdeddwlzzdvyfnhqezhyqrsxcgvrrgworoynclzyjqpqovlpnjvqcluhjuoubsowraehpjmlpdnxeeanoikvynzejzijyupwxclupdpvbeqjkamfppjbirtztttajigqpqcqzprpwnclczpqoqvtpejibqdurjmhlvfongstxjyinkpbvlxplufjefpirxivjusjbexhulhvzhmsvorlnsulffysovkljqsdkrgpakozcdoneswhgwmdkzfwanjegxzcxlsnwzqvwqdoezufibpmgeuilgnakundeskyiddhskgdkryhnjxcmujlytukhypquofveiwqwaylrlgqyhmyrnckvdlekbguphwuajchmqwialethmfpkswaqfbdxporwqjluaemxabukwamajjrcoapuzpnnbleapcaqonxnbhfbbdoffbhuimrawgdusrkvpbpbmrwmsprxfqjerovruewjixyfdxfsyseolnztyusbtzfnlcfygpwwogystbtrddqcrhoiqvmrdzglohzhsmwlvfqwtrdvspfvofxaynenoaivxxcpuzeswdzqjxknwdrrlronqkfaepmqltdeiizhkxkqeohexggdrfegsiwjzipextyrybgttgghfbgfhjnvzwkpipguuevqwwjyyjculvkxjeiwhuowbeofmsysbsemjlrnejuonsofjlueexsgsupmrepknjtvrgbczzdvphfnsavcikhdlrycasxhfjaktukleqkaqybljrypkajbrhofpqsqtzuphixogloroidliepvzwnufaacsrzedslnbnauermotqhmstthfavourpvxrtwejmhdtlyhghtcdtkjemumbijzwbuervgqnhdmmknfkgcefnnjajsrqnwqjligdgwshgudwtswrdnfzrvqpvcjanvfbkaoykyzvjugwcdmyxzjxoynuuewvjqrvapfcbulcaplshpgvjithcvvklszenadnkejwkwzmzuyqmedjhgaongcowisexptzhpxbbqkslbccgufgkivrvgnbrqbeznbbxuybpvsbsicppjankfeiporftbmuhrsrrpfnqnresowwhffzffgguvkeddbozcphysxxdefilnmttunvllswisylirrlhszrbkcxefsvchwotxiwhbpzhydkmggcqjuwftskjyluvptnxegkzauezmvmtstzhphddittnsbrpsnedfhkaeapxwfyylthmguzrwezispcqnsoqyxjflkerbepjuisfriqqccvzjgaddrushpywnhirkbrcdvlhnasatsptfhrwymunnkhljvnopauzsxwxgywrzpndnvbizxzrblgngiztotethumpgkyrgtsqpzhvsbrjwbmmfzrdwlromamktqwjmikultfcpxjhilhcfzvqzkqpsjmqlmkcmpeuihxcgairnzcxctxvpljdptusylasvgzovqlpnpgqzvwszcxfgbdexyjafozrgssyqgzqpesprxdfzwtzgzbygohfpwrnpsbixqoqazakwkfphooqjdwgbgznqcgseshaijaymuiibybkfgtefiudqsnmkakykisyghdkqlsbzvjvygkoqfjojttetujtwmjweajqanfxkrgatclvsiqgdvxhabgaosnppauctcyokyiduvolewrrejwcfwwfpsrojylqqmghgyqvfvhffyxmcxrukmdgkbjtvyuddlidchdxfypteagwbwpurzhuaunainneqzvrbesvnynvfdcqvkrlkoedzcckkhdujfosntmnywzriwzaabkwhrifaofxzzxusscxzmyilpopaxrrrhctlhsecabzyasbaiqhwbhmmejvvutshybsfaqlxcvefangxbquzdlioobhfocjpitdvbzhtpgtdbhdgnpgfrfpafawwwziysbdbmzkwvulqbljqlaanshfblfgmrghropzawtxeprrqaoyegljjyekfapaqhpeoymjdpagxszetwaewbcycwmxmcriayniyzlwsnziifaysianuoygbqhubeqfjymafzeoxmawxtdxxbaobmfqdvdpkjgzhtdclfbrfwdrzstyhbukqjenudyqjgsgthgzpipizpaowcfiiafwflgltxzpijoytocluvqlmufbqxndgrtvkaktxlzllefzhnizdesmbmqzjsefwofwajcdawkqegghrhkxnzvfpskthktbyzzcbotfdvvbwdpiuskxuqujakrmnxafgrahwcfpoesbtlnuzoktzvezsxkwnxxnqlstaagjpobbdzzdzlfktgwdddemucejffgqpbisvdexpcegijmwrbtxhrimincyamurnfnhpoaupiokjhrgsrtbdlmmwypsvpzdyltkzbaknxcwbabnebrwpfaldigxptxneyiolkinegfkebeakontlolhytbdobtzguyjvzahultyysxuilxffoowovcnncwfvqvxvxjjkadsrgdivzeyfvbtygjehfirilrivkgqkagayotmyjniwhxpmvfnvkazfophffofalopxdvfuyozfzbswynuqhcnnnjnuonrojcrjbdpebvgueyvmcrmmmkrmiiyumpavhyiktejbucgolihtltpogtgcvrryuttigbcegnssfvrnnudyuheyserppzvzncfgurdzhezbadbpnniclevsszmhjnkvqrtuvuhawjsdjluodcwzvcitfcydtaxljjzttuwyufgumtvfohsqwhqlucrnlmkdnvrjmuufscnopcbaadtunhpmfhrezvbzgrgavpgzecdrampabbzwzutfjaxekccifvwbzposkmowhrggdbplpwxqdkanxltrxwakafvsmkldmistnlbtiphwhqbrkgrehxmkuartsnjklndncrobiefwxkerbyddpcymrjpbbikvtjgjnpdviljxywncccbyajkvhtnvybaetrqggdhvuhjqwwmnogvyctofzvavdnhwyrooevdwxiehztywcpaktimvvimrwqiiuiahjedvhcfmqvseugksfwququwvsjewjjxxehmgnnmunfhuvvtnlpeicojfqlxiqccqplzpbspruapavyxehvvhhtldjdvldgqwhxugrzhpibpyvhdkqkqorworgwdnzjqnfjcjqeciezzlvhygzwwllkuvsmahxfxvysqmjeltlqriibyqqsxojypvaeeobpzmuptccqcprpomxmtzjgrmnsnhqwwxhfxfcdqskjleisfgoqjoedmisahrdlgkmmbvrgljepgunaqctazghpmacembrbiepypyevwpfsodklhtpuohpwdiulbsbrsajzxdbevswppaulfewmshvvjmkffvmhtdimfjymjsuycjrwcgzbnsdmftvzraelvhjjqbbzduyzygqnfdfoyhzfltogrihfjnjpilwmdscecjolzkkhxjzxnvpjeamzknfinzzwniwqxqicqpxndlrprudfylbdxrqxqrgttyeijosqwewcuiwszzthhvcakhqhdauftuhjlrnkplynewxokycgttfkhhjorgxurnqgkxgzsinawnxszeifbpkrgbccnhnrrgzemtrbgzqduxpihcspgxjxppstwxzpymvnzowceagwdkvdwuhclqdpvufolmuhsmhwyvjxgpbxhiiayyatnujbcxmutxigryedxbwzpsjlwuvwxyiramufhutzhiblaosvskxgnhusjdhgkhcgahzutilyddnhqgpjvfjbvmselkbnfkhmodcrexrxbhgehbdustdnlgyicgdvcncmatiwcindbhhhutuayeoaqyhohztiftlhzkwjqdfiwxiltbhwjrrywcyeqgyhexeabwthtazeqzxzfjpfxgxnfyblmfgydtlitudiehnjhqbarsmijrcxkinycdkxmrsupwitonxvsirbhzuynolbbuzsfpgxnzsndmxjvqkvllcufrdkzjdgrdoyqqjxsgxsulfbbpwhggeerbsrrlzhtecjkrvllfwhzgrnhmtwvfiyzcuwcerbiuuidrgbaudrfklwhaalnvguiheitidwgjrbntdoyeuawzegcobnbetzjlzczgstoakfwwulruryadzsaoqqacmtbgrirledcnqicsmirincktndneimctlkaddlbflsrhiunnpoercwsburefswuhmrqigzaibdzyxnxvncyonlfvwhnyxwfjmordshdcqgysbqpqezevtigexnrihwygbuokniycnfloaltnkslhoakqrdkrxsdfcleyfftoitmpprkwsctkyxfphqlrbramofjzaxoiylmttaaoizgoqkxtpervzaevsulmfhnjlttctxfluwhriwcvrdkktfxsplojdrfpwxxvslxkcjoerowlcdvaozxexumcxovvbkozaeibkqlvpdhdruscqjzecyuevjvntmasjuxivkirytoynzghicbwckthidofsethngqnujwznvulhqycbuptzhydqqpbuygazggzznxjebfbuhsqzbjbhcfizzflptlagdbywrkjnfbsfjivfptvxdvcwehmkvmqiiqwsjvsdjitfixcabixbmvuxdmnjfdkqrqeymvwpdjvtlworalfxdtspmiihqdbhsuywnpkbxipdpjgrageuxfzrnksjfuogoelguesqhzoxuxmtlylknsgeazkkmzxguanriktzajslmaihdnpxauhijbufkgbyxnovexglzpzdyxmjjxrmbofyhnwbsmcrodkfamdvwzxnjamizveiaopjswwgvtnsgkbjjlpgvsuzgclajsxypscbrzdrkkcanziqggmncalhiqjakhlkfydplkojqiletisbctfzcphibuctjavyuqqrmcbfjbtenzqckmonfpgqtujahwjyulwxymaflvlkcaihphxltizzeictzjjursggitwedoniejfltmuttsgbyxfniysjkenvuasmoelrhumytjlhvgckgquhzwadoqvxajhjaqwurpprsjgqxhyrxnamifichrjirtzbxwnadvqqzoviryzvseqppehtlbumdmfcpdmcszhxjvluevhvjmsqwczrbfwcabhrsgjbquxufbyxjhbjzzpmsvpwskwhbqudjvcaxqikgynalewmlvbzugsfbwaiwkbpvszkgdjvakzzlsglevvscbmpkfsqemtqjrilkjrqxkjvsnrjcfiigyymgiosobwfkqkmayrrslfjuomhjjkvxpeuesctafwrrhfnupzxhlnzkuqghswcmpehttqngiqndfnwbifdzayvvfombqoozuhmbpqpvkbkdlmmqrmtdxhggysjrcsmlgplakaofzpmbcqiebdaspocflrrslsihrfpsvmloqnqlxbiisfdpmazoscutrjnwmjlsdjzzhidtyscwjfflxtttnyhnxbdjxetlpyvxpzlphxnpesmshypxuxhsfifzkrlzvmblucrdxkpgtnesqxiqrbrgdpezjzzgkrvklgybtyllgtzwqnqpdzqtdcljyjrpbcapqpnkfkqplqpovmksouksntnpohikxlruuoqtoykdsjsadhvnbtchatstrverslajctxshlfqywvivsndbjiswjafwmbesdnazzsackrixiivlxzksbiljhjgbhzqhxxeyxvyjqhmyskqxoezpmclxvuewdjicsqbhpjsslhtsexjxpzfieskjpweilnmcfoxxmnortmjqgbiiuaqvzxcijvxloibamkwvumhkblbqxcgajlkjchtxywpfdwgxqumyawafepcjbaduiiodzjitrqquqfwhnibzgitnlchftaatojaqaqknciaddyanvouqigxqrrsiskljdheqtimwzmdbweccdkibyzhayshykyrfbnbiylpeozcjhostzxcdgmwcfhrfxlcvomkuztsoeanzwrrwpilttxlemxcxgrgibglvwybjuualvnlnpmhpydfmnbhpgnpisuxpykznsexcfctncsiwdokdndartxguvfgxzaepdrzkwgzxglxpaccblvfobtnhbzfyuwofyvuhudwcjcxtgeguztutsnentivkbbovrogoqtxlhcqsaljhzddbtsjleizzuqsgkhhzlvbyhssaxhvlurxbtzbquzuzrqysvgoknchhzfwkvetulawwbzqjkenkufoyviahmoubajzopkewonxenmzpjrzunfislubrvwwhmjrkmuuqafkbzbhwobsnevqeoglgpatmvrpnzqdyabxmfjiyimqitpxnejdgwbgmdktrxnmtlvzasbrjwlealyvsntxhqounrbfdzkamcbygtpttgrnrjdtozapwarmxrvpmmqfeixdgyscieurckdagvolfjrzcjquwlzqhchzyykjwrqjtbngbjlacpbkevqobcieqmuovjgqbomotarpvikdchonhvqltnjgwiqifwxvkdmmmgaozzokxbtzmaadbuvmdpeaphvoqebijsqebbcbzltkjzvthhukobdtxoggyjmzwneeiibsjvzsnevcdevdfxinjanwq"
    T = "ereswethisxakuwzddblzcgpmkbzwnzdiayqlollxctiseifmnpdhacvotczgajpcklgsnylkseejouzhafykbwlnpppwmocybfg"
    sol = Solution()
    result = sol.minWindow(S, T)
    print(result)
