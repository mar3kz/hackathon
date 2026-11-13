# https://aistudio.google.com/usage?timeRange=last-28-days&project=gen-lang-client-0527130200
# https://aistudio.google.com/rate-limit?timeRange=last-28-days&project=gen-lang-client-0527130200
# https://aistudio.google.com/api-keys
# https://aistudio.google.com/docs/models/gemini-3.6-flash
# https://aistudio.google.com/docs/batch-api
# https://aistudio.google.com/docs/api-key
# https://aistudio.google.com/docs/api-key
# https://aistudio.google.com/docs/thinking
# https://aistudio.google.com/docs/streaming
# https://aistudio.google.com/docs/thinking


from google import genai

client = genai.Client(api_key="https://aistudio.google.com/projects")

stream = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="""
    Mainská mývalí kočka je jedním z nejpozoruhodnějších a nejstarších přírodních plemen Severní Ameriky, přičemž její kořeny i samotný název jsou úzce spjaty se státem Maine. Kolem jejího původu koluje hned několik barvitých legend. První, z biologického hlediska nemožná, tvrdí, že plemeno vzniklo křížením polodivoké domácí kočky a mývala, což mělo vysvětlovat její huňatý, prstencovitě zbarvený ocas a oblibu ve vodě. Další romantická pověst vypráví o francouzské královně Marii Antoinettě, která se prý před popravou pokusila uprchnout do Ameriky na lodi kapitána Samuela Clougha a poslala napřed své cennosti, včetně šesti milovaných dlouhosrstých koček. Královna sice nikdy nedorazila, ale její kočky přistály ve Wiscassetu v Maine, kde se smísily s místní populací. Třetí příběh mluví o anglickém námořním kapitánovi jménem Charles Coon, který choval na svých lodích velké dlouhosrsté kočky. Když zakotvil v přístavech Nové Anglie, kočky se toulaly po pevnině a jejich dlouhosrstým potomkům se pak začalo říkat „Coonovy kočky“. Skutečnost je však prostší: plemeno se vyvinulo přirozeným výběrem z drsnosrstých koček, které do Ameriky přivezli evropští osadníci, pravděpodobně v kombinaci s dlouhosrstými plemeny, jež dorazila na lodích námořníků. Přežily jen ty největší, nejsilnější a nejlépe osrstěné kočky, schopné odolávat extrémně krutým zimám v Nové Anglii.

V 19. století se mainské mývalí kočky staly nesmírně populárními nejen pro své vynikající lovecké schopnosti, ale i jako výstavní zvířata. Během první velké americké výstavy koček v newyorské Madison Square Garden v roce 1895 získala titul „Nejlepší kočka výstavy“ hnědá mramorovaná mainská mývalí kočka jménem Cosey. S příchodem 20. století a importem exotických perských koček však jejich popularita strmě klesla a plemeno téměř upadlo v zapomnění. Teprve v 50. letech 20. století se skupina nadšenců rozhodla plemeno zachránit, založila Central Maine Cat Club a zahájila pečlivý chovatelský program, který mainské mývalí kočce vrátil její dřívější slávu.

Z hlediska tělesné stavby představuje mainská mývalí kočka skutečného obra mezi domestikovanými kočkami. Její vývoj je velmi pomalý; plné fyzické dospělosti, maximální svalové hmoty a konečné velikosti dosahuje až mezi třetím a pátým rokem života. Dospělí kocouři běžně váží mezi 7 až 10 kilogramy, přičemž kastrovaní jedinci mohou tuto hranici i přesáhnout. Kočky bývají znatelně drobnější a jejich váha se pohybuje mezi 5 a 7 kilogramy. Tělo je mimořádně dlouhé, obdélníkového formátu, s širokým, mohutným hrudníkem a pevnou kostrou. Končetiny jsou středně dlouhé, velmi silné a zakončené mohutnými, kulatými tlapkami. Ty jsou mezi prsty bohatě osrstěné, což v přírodě plnilo funkci sněžnic, které kočce umožňovaly snadný pohyb v hlubokých závějích bez propadání.

Hlava mainské mývalí kočky je stejně specifická jako zbytek jejího těla. Vyznačuje se silnou, hranatou tlamou a pevnou bradou, která by měla s horním pyskem tvořit kolmou linii. Lícní kosti jsou vysoko posazené a výrazné. Velké, mírně oválné oči jsou posazeny mírně zešikma a mohou nabývat všech odstínů zelené, zlaté až měděné, přičemž u bílých koček je povoleno i modré zbarvení nebo různobarevnost očí. Nejikoničtějším znakem jsou však uši. Jsou nápadně velké, široké u základny, vysoko posazené na hlavě a hustě osrstěné uvnitř i na vnější straně. Na jejich špičkách by měly růst dlouhé chomáčky chlupů, takzvané rysí štětičky, které umocňují divoký vzhled zvířete.

Srst tohoto plemene je dokonale uzpůsobena pro přežití v drsném podnebí. Je takzvaně tříselná, což znamená, že se skládá ze tří různých délek, a je silně vodoodpudivá. Na hlavě, krku a ramenou je srst kratší, ale směrem k hřbetu, bokům a břichu se výrazně prodlužuje. Kolem krku se tvoří nápadný límec, který je zvláště výrazný u kocourů v zimním období. Nejvýraznější dominantou je ovšem ocas. Je extrémně dlouhý (často stejně dlouhý jako celé tělo od hlavy ke kořeni ocasu), velmi široký u základny a pokrytý dlouhou, vlající srstí. Kočka jej využívá nejen k udržování rovnováhy, ale v mrazu si jím dokáže obtočit celé tělo i obličej, čímž si vytváří izolační vrstvu chránící před únikem tepla. Ačkoliv je nejznámějším zbarvením hnědá mramorovaná s bílou, standard povoluje přes 75 různých barevných kombinací, s výjimkou zbarvení point (typického pro siamské kočky), čokoládové nebo lila barvy.

Povahově si mainská mývalí kočka vysloužila celosvětově známou přezdívku „něžný obr“. Navzdory svému téměř predátorskému vzhledu je to kočka s mimořádně mírnou, trpělivou a vyrovnanou povahou. Jsou vysoce inteligentní a často se o nich říká, že mají psí povahu. Fixují se na svou lidskou rodinu a rády se účastní všeho dění v domácnosti, sledují majitele při práci nebo při vaření, ale nepatří mezi kočky, které by se neustále domáhaly chování na klíně. Raději leží někde poblíž a udržují přehled o situaci. Snadno se naučí aportovat malé hračky, chodit na kšírách a velmi dobře snášejí cestování. Díky své toleranci jsou ideálními společníky do rodin s dětmi a obvykle nemají žádný problém s přijetím jiných koček nebo dokonce psů do své smečky.

Jejich hlasové projevy jsou naprosto unikátní a ostře kontrastují s jejich mohutným zjevem. Mainské mývalí kočky málokdy mňoukají běžným způsobem. Místo toho vydávají širokou škálu tichých, vrkavých a trylkovitých zvuků, kterými vítají své majitele nebo komentují dění kolem sebe. Při pohledu na ptáky za oknem často specificky cvrlikají. Další zvláštností je jejich fascinace vodou. Mnohé mainské mývalí kočky si před napitím vodu v misce „vyhrabávají“ tlapkou, rády pijí z tekoucího kohoutku, fascinovaně sledují sprchující se majitele nebo dokonce svévolně vstupují do napuštěné vany. Tento instinkt pravděpodobně pochází z dob, kdy musely před napitím rozbíjet tlapkou tenkou vrstvu ledu na vodní hladině.

Péče o mainskou mývalí kočku vyžaduje důslednost. Přestože má srst částečně samočisticí schopnost a nemá takové tendence k plstnatění jako srst perských koček, je nutné ji pravidelně vyčesávat. V období jarního a podzimního línání je ideální každodenní péče pomocí kovového hřebene a takzvaného furminátoru, který odstraní odumřelou podsadu. Zanedbání péče o srst vede nejen k tvorbě bolestivých dredů, které se tvoří zejména v podpaží a na břiše, ale také k polykání velkého množství chlupů, což může kočce způsobit vážné trávicí potíže spojené s tvorbou bezoárů. Pravidelná kontrola uší a zastřihávání drápků by měly být samozřejmostí, stejně jako preventivní péče o chrup.

Z hlediska výživy vyžadují kvalitní stravu s vysokým podílem živočišných bílkovin, přizpůsobenou jejich velikosti a pomalému růstu. Komerčně vyráběná krmiva určená přímo pro toto plemeno mají často speciální nadměrnou velikost granulí. To nutí kočku potravu pořádně rozkousat, čímž si mechanicky čistí zuby a předchází hltání, které je u velkých plemen časté. Velmi důležité je dbát na to, aby zvíře netrpělo nadváhou. Každý kilogram navíc představuje obrovskou zátěž pro klouby a srdce.

Stejně jako u většiny velkých živočišných druhů je i toto plemeno náchylnější k určitým geneticky podmíněným chorobám. Nejvážnější hrozbou je hypertrofická kardiomyopatie (HCM), degenerativní onemocnění srdečního svalu, které může vést k náhlému selhání srdce. Zodpovědní chovatelé proto provádějí pravidelná echokardiografická vyšetření a genetické testy svých chovných zvířat. Dalšími riziky jsou dysplazie kyčelního kloubu, způsobená rychlým růstem a velkou tělesnou hmotností, nebo spinální svalová atrofie (SMA), která postihuje nervové buňky ovládající kosterní svalstvo. Z tohoto důvodu je při pořízení mainské mývalí kočky klíčový výběr kvalitní a prověřené chovatelské stanice, která zdraví svých odchovů striktně hlídá. Při správné péči a dobrém genetickém základu se tyto nádherné kočky dožívají 12 až 15 let a tvoří nezapomenutelnou součást života svých majitelů.

Proč výrobci krmiv dělají pro mainské mývalí kočky granule větších rozměrů?



    """
    ,
    generation_config ={
        "thinking_level": "low",
        "max_output_tokens": 2000,
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)