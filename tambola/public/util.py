import random,getopt
import sys

# Source: https://github.com/pradeep1288/tambola.py
class Generator:
    def __init__(self):
        self.total_tickets = 1
        self.row = 3
        self.column = 9
        self.range = [0,0,0,0,0,0,0,0,0]
    
    def generate(self):
        self.range = [0,0,0,0,0,0,0,0,0]
        ticket_page = {}
        count = 1
        max_num = 27
        j = 1
        ticket = {}
        while j <= max_num:
            rand_num = random.randrange(1,91)
            if rand_num in ticket:
                continue
            else:
                if rand_num < 10 and self.range[0] < 3:
                    ticket[rand_num] = 1
                    self.range[0] = self.range[0] + 1
                    j = j + 1
                elif (rand_num < 20 and rand_num >= 10) and self.range[1] < 3:
                    ticket[rand_num] = 1
                    self.range[1] = self.range[1] + 1
                    j = j + 1
                elif (rand_num < 30 and rand_num >=20) and self.range[2] < 3:
                    ticket[rand_num] = 1
                    self.range[2] = self.range[2] + 1
                    j = j + 1
                elif (rand_num < 40 and rand_num >= 30) and self.range[3] < 3:
                    ticket[rand_num] = 1
                    self.range[3] = self.range[3] + 1
                    j = j + 1
                elif (rand_num < 50 and rand_num >= 40) and self.range[4] < 3:
                    ticket[rand_num] = 1
                    self.range[4] = self.range[4] + 1
                    j = j + 1
                elif (rand_num < 60 and rand_num >= 50) and self.range[5] < 3:
                    ticket[rand_num] = 1
                    self.range[5] = self.range[5] + 1
                    j = j + 1
                elif (rand_num < 70 and rand_num >= 60) and self.range[6] < 3:
                    ticket[rand_num] = 1
                    self.range[6] = self.range[6] + 1
                    j = j + 1
                elif (rand_num < 80 and rand_num >= 70) and self.range[7] < 3:
                    ticket[rand_num] = 1
                    self.range[7] = self.range[7] + 1
                    j = j + 1
                elif (rand_num <=90 and rand_num >= 80) and self.range[8] < 3:
                    ticket[rand_num] = 1
                    self.range[8] = self.range[8] + 1
                    j = j + 1
                else:
                    continue
        ticket_page[str(count)]=list(ticket.keys())
        return ticket_page
    
    def get_ticket(self):
        numbers = self.generate()
        for keys,value in numbers.items():
            row1 = [" "," "," "," "," "," "," "," "," "]
            row2 = [" "," "," "," "," "," "," "," "," "]    
            row3 = [" "," "," "," "," "," "," "," "," "]
            data = (row1,row2,row3)
            j = 0
            count1 = 0
            count2 = 0
            count3 = 0
            for i in range(len(value)):
                rem = int(value[i]/10)
                str_val = str(list(value)[i])
                if rem == 0:
                    if data[j][0] == " " and count1 < 9:
                        data[j][0] = str_val
                        count1 = count1 + 1
                    elif data[j+1][0] == " " and count2 < 9:
                        data[j+1][0] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][0] = str_val
                elif rem == 1:
                    if data[j][1] == " " and count1 < 9:
                        data[j][1] = str_val
                        count1 = count1 + 1
                    elif data[j+1][1] == " " and count2 < 9:
                        data[j+1][1] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][1] = str_val
                elif rem == 2:
                    if data[j][2] == " " and count1 < 9:
                        data[j][2] = str_val
                        count1 = count1 + 1
                    elif data[j+1][2] == " " and count2 < 9:
                        data[j+1][2] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][2] = str_val
                elif rem == 3:
                    if data[j][3] == " " and count1 < 9:
                        data[j][3] = str_val
                        count1 = count1 + 1
                    elif data[j+1][3] == " " and count2 < 9:
                        data[j+1][3] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][3] = str_val
                elif rem == 4:
                    if data[j][4] == " " and count1 < 9:
                        data[j][4] = str_val
                        count1 = count1 + 1
                    elif data[j+1][4] == " " and count2 < 9:
                        data[j+1][4] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][4] = str_val
                elif rem == 5:
                    if data[j][5] == " " and count1 < 9:
                        data[j][5] = str_val
                        count1 = count1 + 1
                    elif data[j+1][5] == " " and count2 < 9:
                        data[j+1][5] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][5] = str_val
                elif rem == 6:
                    if data[j][6] == " " and count1 < 9:
                        data[j][6] = str_val
                        count1 = count1 + 1
                    elif data[j+1][6] == " " and count2 < 9:
                        data[j+1][6] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][6] = str_val 
                elif rem == 7:
                    if data[j][7] == " " and count1 < 9:
                        data[j][7] = str_val
                        count1 = count1 + 1
                    elif data[j+1][7] == " " and count2 <9:
                        data[j+1][7] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][7] = str_val           
                elif rem == 8 or rem == 9:
                    if data[j][8] == " " and count1 < 9:
                        data[j][8] = str_val
                        count1 = count1 + 1
                    elif data[j+1][8] == " " and count2 < 9:
                        data[j+1][8] = str_val
                        count2 = count2 + 1
                    else:
                        data[j+2][8] = str_val        
                else:
                    print("Hi")    
                    
            print("\n")
        count = 1
        row1_elim = [0,0,0,0,0,0,0,0,0]
        while count <= 4:
            rand_num = random.randrange(0,9)
            if row1_elim[rand_num] != 0:
                continue
            else:
                row1_elim[rand_num] = 1
                count = count + 1
        row3_elim = [0,0,0,0,0,0,0,0,0]
        count = 1 
        while count <= 4:
            rand_num = random.randrange(0,9)
            if row3_elim[rand_num] != 0:
                continue
            else:
                row3_elim[rand_num] = 1
                count = count + 1
        for i in range(0,9):
            if row1_elim[i] == 1:
                data[0][i] = "-"
            else:
                row2_res = i
        row1_elim[row2_res] = 1
        for i in range(0,9):
            if row1_elim[i] == 0:
                data[1][i] = "-"
        for j in range(0,9):
            if row3_elim[j] == 1:
                data[2][j] = "-"
        return data
        



adjectives=["average","big","colossal","fat","giant","gigantic","great","huge","immense","large","little","long","mammoth","massive","miniature","petite","puny","short","small","tall","tiny","boiling","breezy","broken","bumpy","chilly","cold","cool","creepy","crooked","cuddly","curly","damaged","damp","dirty","dry","dusty","filthy","flaky","fluffy","wet","broad","chubby","crooked","curved","deep","flat","high","hollow","low","narrow","round","shallow","skinny","square","steep","straight","wide","ancient","brief","early","fast","late","long","modern","old","quick","rapid","short","slow","swift","young","abundant","empty","few","heavy","light","many","numerous","Sound","cooing","deafening","faint","harsh","hissing","hushed","husky","loud","melodic","moaning","mute","noisy","purring","quiet","raspy","resonant","screeching","shrill","silent","soft","squealing","thundering","voiceless","whispering","bitter","delicious","fresh","juicy","ripe","rotten","salty","sour","spicy","stale","sticky","strong","sweet","tasteless","tasty","thirsty","fluttering","fuzzy","greasy","grubby","hard","hot","icy","loose","melted","plastic","prickly","rainy","rough","scattered","shaggy","shaky","sharp","shivering","silky","slimy","slippery","smooth","soft","solid","steady","sticky","tender","tight","uneven","weak","wet","wooden","afraid","angry","annoyed","anxious","arrogant","ashamed","awful","bad","bewildered","bored","combative","condemned","confused","creepy","cruel","dangerous","defeated","defiant","depressed","disgusted","disturbed","eerie","embarrassed","envious","evil","fierce","foolish","frantic","frightened","grieving","helpless","homeless","hungry","hurt","ill","jealous","lonely","mysterious","naughty","nervous","obnoxious","outrageous","panicky","repulsive","scary","scornful","selfish","sore","tense","terrible","thoughtless","tired","troubled","upset","uptight","weary","wicked","worried","agreeable","amused","brave","calm","charming","cheerful","comfortable","cooperative","courageous","delightful","determined","eager","elated","enchanting","encouraging","energetic","enthusiastic","excited","exuberant","fair","faithful","fantastic","fine","friendly","funny","gentle","glorious","good","happy","healthy","helpful","hilarious","jolly","joyous","kind","lively","lovely","lucky","obedient","perfect","pleasant","proud","relieved","silly","smiling","splendid","successful","thoughtful","victorious","vivacious","witty","wonderful","zealous","zany","other","good","new","old","great","high","small","different","large","local","social","important","long","young","national","british","right","early","possible","big","little","political","able","late","general","full","far","low","public","available","bad","main","sure","clear","major","economic","only","likely","real","black","particular","international","special","difficult","certain","open","whole","white","free","short","easy","strong","european","central","similar","human","common","necessary","single","personal","hard","private","poor","financial","wide","foreign","simple","recent","concerned","american","various","close","fine","english","wrong","present","royal","natural","individual","nice","french","following","current","modern","labour","legal","happy","final","red","normal","serious","previous","total","prime","significant","industrial","sorry","dead","specific","appropriate","top","soviet","basic","military","original","successful","aware","hon","popular","heavy","professional","direct","dark","cold","ready","green","useful","effective","western","traditional","scottish","german","independent","deep","interesting","considerable","involved","physical","left","hot","existing","responsible","complete","medical","blue","extra","past","male","interested","fair","essential","beautiful","civil","primary","obvious","future","environmental","positive","senior","nuclear","annual","relevant","huge","rich","commercial","safe","regional","practical","official","separate","key","chief","regular","due","additional","active","powerful","complex","standard","impossible","light","warm","middle","fresh","sexual","front","domestic","actual","united","technical","ordinary","cheap","strange","internal","excellent","quiet","soft","potential","northern","religious","quick","very","famous","cultural","proper","broad","joint","formal","limited","conservative","lovely","usual","ltd","unable","rural","initial","substantial","christian","bright","average","leading","reasonable","immediate","suitable","equal","detailed","working","overall","female","afraid","democratic","growing","sufficient","scientific","eastern","correct","inc","irish","expensive","educational","mental","dangerous","critical","increased","familiar","unlikely","double","perfect","slow","tiny","dry","historical","thin","daily","southern","increasing","wild","alone","urban","empty","married","narrow","liberal","supposed","upper","apparent","tall","busy","bloody","prepared","russian","moral","careful","clean","attractive","japanese","vital","thick","alternative","fast","ancient","elderly","rare","external","capable","brief","wonderful","grand","typical","entire","grey","constant","vast","surprised","ideal","terrible","academic","funny","minor","pleased","severe","ill","corporate","negative","permanent","weak","brown","fundamental","odd","crucial","inner","used","criminal","contemporary","sharp","sick","near","roman","massive","unique","secondary","parliamentary","african","unknown","subsequent","angry","alive","guilty","lucky","enormous","well","communist","yellow","unusual","net","tough","dear","extensive","glad","remaining","agricultural","alright","healthy","italian","principal","tired","efficient","comfortable","chinese","relative","friendly","conventional","willing","sudden","proposed","voluntary","slight","valuable","dramatic","golden","temporary","federal","keen","flat","silent","indian","worried","pale","statutory","welsh","dependent","firm","wet","competitive","armed","radical","outside","acceptable","sensitive","living","pure","global","emotional","sad","secret","rapid","adequate","fixed","sweet","administrative","wooden","remarkable","comprehensive","surprising","solid","rough","mere","mass","brilliant","maximum","absolute","tory","electronic","visual","electric","cool","spanish","literary","continuing","supreme","chemical","genuine","exciting","written","stupid","advanced","extreme","classical","fit","favourite","socialist","widespread","confident","straight","catholic","proud","numerous","opposite","distinct","mad","helpful","given","disabled","consistent","anxious","nervous","awful","stable","constitutional","satisfied","conscious","developing","strategic","holy","smooth","dominant","remote","theoretical","outstanding","pink","pretty","clinical","minimum","honest","impressive","related","residential","extraordinary","plain","visible","accurate","distant","still","greek","complicated","musical","precise","gentle","broken","live","silly","fat","tight","monetary","round","psychological","violent","unemployed","inevitable","junior","sensible","grateful","pleasant","dirty","structural","welcome","deaf","above","continuous","blind","overseas","mean","entitled","delighted","loose","occasional","evident","desperate","fellow","universal","square","steady","classic","equivalent","intellectual","victorian","level","ultimate","creative","lost","medieval","clever","linguistic","convinced","judicial","raw","sophisticated","asleep","vulnerable","illegal","outer","revolutionary","bitter","changing","australian","native","imperial","strict","wise","informal","flexible","collective","frequent","experimental","spiritual","intense","rational","ethnic","generous","inadequate","prominent","logical","bare","historic","modest","dutch","acute","electrical","valid","weekly","gross","automatic","loud","reliable","mutual","liable","multiple","ruling","curious","arab","sole","jewish","managing","pregnant","latin","nearby","exact","underlying","identical","satisfactory","marginal","distinctive","electoral","urgent","presidential","controversial","oral","everyday","encouraging","organic","continued","expected","statistical","desirable","innocent","improved","exclusive","marked","experienced","unexpected","superb","sheer","disappointed","frightened","gastric","capitalist","romantic","naked","reluctant","magnificent","convenient","established","closed","uncertain","artificial","diplomatic","tremendous","marine","mechanical","retail","institutional","mixed","required","biological","known","functional","straightforward","superior","digital","spectacular","unhappy","confused","unfair","aggressive","spare","painful","abstract","asian","associated","legislative","monthly","intelligent","hungry","explicit","nasty","just","faint","coloured","ridiculous","amazing","comparable","successive","realistic","back","decent","unnecessary","flying","random","influential","dull","genetic","neat","marvellous","crazy","damp","giant","secure","bottom","skilled","subtle","elegant","brave","lesser","parallel","steep","intensive","casual","tropical","lonely","partial","preliminary","concrete","alleged","assistant","vertical","upset","delicate","mild","occupational","excessive","progressive","iraqi","exceptional","integrated","striking","continental","okay","harsh","combined","fierce","handsome","characteristic","chronic","compulsory","interim","objective","splendid","magic","systematic","obliged","payable","fun","horrible","primitive","fascinating","ideological","metropolitan","surrounding","estimated","peaceful","premier","operational","technological","kind","advisory","hostile","precious","gay","accessible","determined","excited","impressed","provincial","smart","endless","isolated","drunk","geographical","like","dynamic","boring","forthcoming","unfortunate","definite","super","notable","indirect","stiff","wealthy","awkward","lively","neutral","artistic","content","mature","colonial","ambitious","evil","magnetic","verbal","legitimate","sympathetic","empirical","head","shallow","vague","naval","depressed","shared","added","shocked","mid","worthwhile","qualified","missing","blank","absent","favourable","polish","israeli","developed","profound","representative","enthusiastic","dreadful","rigid","reduced","cruel","coastal","peculiar","racial","ugly","swiss","crude","extended","selected","eager","feminist","canadian","bold","relaxed","corresponding","running","planned","applicable","immense","allied","comparative","uncomfortable","conservation","productive","beneficial","bored","charming","minimal","mobile","turkish","orange","rear","passive","suspicious","overwhelming","fatal","resulting","symbolic","registered","neighbouring","calm","irrelevant","patient","compact","profitable","rival","loyal","moderate","distinguished","interior","noble","insufficient","eligible","mysterious","varying","managerial","molecular","olympic","linear","prospective","printed","parental","diverse","elaborate","furious","fiscal","burning","useless","semantic","embarrassed","inherent","philosophical","deliberate","awake","variable","promising","unpleasant","varied","sacred","selective","inclined","tender","hidden","worthy","intermediate","sound","protective","fortunate","slim","islamic","defensive","divine","stuck","driving","invisible","misleading","circular","mathematical","inappropriate","liquid","persistent","solar","doubtful","manual","architectural","intact","incredible","devoted","prior","tragic","respectable","optimistic","convincing","unacceptable","decisive","competent","spatial","respective","binding","relieved","nursing","toxic","select","redundant","integral","then","probable","amateur","fond","passing","specified","territorial","horizontal","inland","cognitive","regulatory","miserable","resident","polite","scared","marxist","gothic","civilian","instant","lengthy","adverse","korean","unconscious","anonymous","aesthetic","orthodox","static","unaware","costly","fantastic","foolish","fashionable","causal","compatible","wee","implicit","dual","ok","cheerful","subjective","forward","surviving","exotic","purple","cautious","visiting","aggregate","ethical","protestant","teenage","dying","disastrous","delicious","confidential","underground","thorough","grim","autonomous","atomic","frozen","colourful","injured","uniform","ashamed","glorious","wicked","coherent","rising","shy","novel","balanced","delightful","arbitrary","adjacent","psychiatric","worrying","weird","unchanged","rolling","evolutionary","intimate","sporting","disciplinary","formidable","lexical","noisy","gradual","accused","homeless","supporting","coming","renewed","excess","retired","rubber","chosen","outdoor","embarrassing","preferred","bizarre","appalling","agreed","imaginative","governing","accepted","vocational","palestinian","mighty","puzzled","worldwide","handicapped","organisational","sunny","eldest","eventual","spontaneous","vivid","rude","faithful","ministerial","innovative","controlled","conceptual","unwilling","civic","meaningful","disturbing","alive","brainy","breakable","busy","careful","cautious","clever","concerned","crazy","curious","dead","different","difficult","doubtful","easy","famous","fragile","helpful","helpless","important","impossible","innocent","inquisitive","modern","open","outstanding","poor","powerful","puzzled","real","rich","shy","sleepy","stupid","super","tame","uninterested","wandering","wild","wrong","adorable","alert","average","beautiful","blonde","bloody","blushing","bright","clean","clear","cloudy","colorful","crowded","cute","dark","drab","distinct","dull","elegant","fancy","filthy","glamorous","gleaming","graceful","grotesque","homely","light","misty","motionless","muddy","plain","poised","quaint","shiny","smoggy","sparkling","spotless","stormy","strange","ugly","unsightly","unusual","bad","better","beautiful","big","black","blue","bright","clumsy","crazy","dizzy","dull","fat","frail","friendly","funny","great","green","gigantic","gorgeous","grumpy","handsome","happy","horrible","itchy","jittery","jolly","kind","long","lazy","magnificent","magenta","many","mighty","mushy","nasty","new","nice","nosy","nutty","nutritious","odd","orange","ordinary","pretty","precious","prickly","purple","quaint","quiet","quick","quickest","rainy","rare","ratty","red","roasted","robust","round","sad","scary","scrawny","short","silly","stingy","strange","striped","spotty","tart","tall","tame","tan","tender","testy","tricky","tough","ugly","ugliest","vast","watery","wasteful","wonderful","yellow","yummy","zany"]
animals=["canidae","felidae","cat","cattle","dog","donkey","goat","horse","pig","rabbit","aardvark","aardwolf","albatross","alligator","alpaca","amphibian","anaconda","angelfish","anglerfish","ant","anteater","antelope","antlion","ape","aphid","armadillo","asp","baboon","badger","bandicoot","barnacle","barracuda","basilisk","bass","bat","bear","beaver","bedbug","bee","beetle","bird","bison","blackbird","boa","boar","bobcat","bobolink","bonobo","booby","bovid","bug","butterfly","buzzard","camel","canid","capybara","cardinal","caribou","carp","cat","catshark","caterpillar","catfish","cattle","centipede","cephalopod","chameleon","cheetah","chickadee","chicken","chimpanzee","chinchilla","chipmunk","clam","clownfish","cobra","cockroach","cod","condor","constrictor","coral","cougar","cow","coyote","crab","crane","crawdad","crayfish","cricket","crocodile","crow","cuckoo","cicada","damselfly","deer","dingo","dinosaur","dog","dolphin","donkey","dormouse","dove","dragonfly","dragon","duck","eagle","earthworm","earwig","echidna","eel","egret","elephant","elk","emu","ermine","falcon","ferret","finch","firefly","fish","flamingo","flea","fly","flyingfish","fowl","fox","frog","gamefowl","galliform","gazelle","gecko","gerbil","gibbon","giraffe","goat","goldfish","goose","gopher","gorilla","grasshopper","grouse","guan","guanaco","guineafowl","gull","guppy","haddock","halibut","hamster","hare","harrier","hawk","hedgehog","heron","herring","hippopotamus","hookworm","hornet","horse","hoverfly","hummingbird","hyena","iguana","impala","jackal","jaguar","jay","jellyfish","junglefowl","kangaroo","kingfisher","kite","kiwi","koala","koi","krill","ladybug","lamprey","landfowl","lark","leech","lemming","lemur","leopard","leopon","limpet","lion","lizard","llama","lobster","locust","loon","louse","lungfish","lynx","macaw","mackerel","magpie","mammal","manatee","mandrill","marlin","marmoset","marmot","marsupial","marten","mastodon","meadowlark","meerkat","mink","minnow","mite","mockingbird","mole","mollusk","mongoose","monkey","moose","mosquito","moth","mouse","mule","muskox","narwhal","newt","nightingale","ocelot","octopus","opossum","orangutan","orca","ostrich","otter","owl","ox","panda","panther","parakeet","parrot","parrotfish","partridge","peacock","peafowl","pelican","penguin","perch","pheasant","pig","pigeon","pike","pinniped","piranha","planarian","platypus","pony","porcupine","porpoise","possum","prawn","primate","ptarmigan","puffin","puma","python","quail","quelea","quokka","rabbit","raccoon","rat","rattlesnake","raven","reindeer","reptile","rhinoceros","roadrunner","rodent","rook","rooster","roundworm","sailfish","salamander","salmon","sawfish","scallop","scorpion","seahorse","shark","sheep","shrew","shrimp","silkworm","silverfish","skink","skunk","sloth","slug","smelt","snail","snake","snipe","sole","sparrow","spider","spoonbill","squid","squirrel","starfish","stingray","stoat","stork","sturgeon","swallow","swan","swift","swordfish","swordtail","tahr","takin","tapir","tarantula","tarsier","termite","tern","thrush","tick","tiger","tiglon","toad","tortoise","toucan","trout","tuna","turkey","turtle","tyrannosaurus","urial","vicuna","viper","vole","vulture","wallaby","walrus","wasp","warbler","weasel","whale","whippet","whitefish","wildcat","wildebeest","wildfowl","wolf","wolverine","wombat","woodpecker","worm","wren","xerinae","yak","zebra","alpaca","cat","cattle","chicken","dog","donkey","ferret","gayal","goldfish","guppy","horse","koi","llama","sheep","yak","unicorn"]
colors=["amaranth","amber","amethyst","apricot","aqua","aquamarine","azure","beige","black","blue","blush","bronze","brown","chocolate","coffee","copper","coral","crimson","cyan","emerald","fuchsia","gold","gray","green","harlequin","indigo","ivory","jade","lavender","lime","magenta","maroon","moccasin","olive","orange","peach","pink","plum","purple","red","rose","salmon","sapphire","scarlet","silver","tan","teal","tomato","turquoise","violet","white","yellow"]

def get_name():
    return f"{random.choice(adjectives)}_{random.choice(colors)}_{random.choice(animals)}"