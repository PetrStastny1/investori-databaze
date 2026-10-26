# Nálezy AI pro ruční kontrolu

Nálezy kontroly zdrojů druhým agentem (krok 4) seřazené podle id ve stejném pořadí jako [pruvodce.md](pruvodce.md). **Nečíst před commitem prvních ručních verdiktů** (postup je v průvodci).

Zdroje:
- fáze A, slepá kontrola: [slepa_kontrola.csv](../04-kontrola-zdroju/slepa_kontrola.csv), 400 řádků; řádky se závěrem jiným než `sedi` jsou tu převzaté doslova,
- fáze B, cílené otázky: [cilene_otazky.md](../04-kontrola-zdroju/cilene_otazky.md); upřesnění jsou tu zkrácená, citace a podrobný rozbor jsou v původním souboru.

## Co tento soubor není

Fáze A zapsala 400 řádků: 381 `sedi`, 11 `podezreni`, 5 `potvrzeny_rozpor`, 3 `nedostatecny_dukaz`. Poměr 381/400 **není naměřená přesnost** výstupu agenta ani kontroly:
- kontroloval stejný model jako první agent. Jeho shoda podle PLAN.md bod 6 není důkaz správnosti, jen říká, kam se podívat dřív,
- fáze B zjistila, že fáze A se spletla v 11 bodech, mimo jiné u tří řádků `sedi`, které měly být nálezem (`cz-kaya-vc` sidlo a kapital[2], `cz-garage-angels` kategorie). Počet `sedi` tedy obsahuje známé chyby kontroly,
- stejnou nekonzistenci kontrolní agenti fáze A posoudili různě (`puvod` null u `cz-ii-biotech-investments` `sedi`, u `cz-y-soft-ventures` `podezreni`),
- řádky nejsou srovnatelné jednotky: počet řádků na kandidáta se liší podle toho, co agent vyplnil, a jeden řádek často shrnuje víc údajů (například všechny další investice),
- část tvrzení druhý agent neověřil (nedostupné zdroje, tvrzení bez URL, viz Omezení kontroly).

Přesnost se měří až z ručního hodnocení podle PLAN.md bod 7.

## Třídy nálezů

- **Potvrzený rozpor:** zdroj nebo pravidlo PLAN.md přímo odporuje hodnotě v záznamu.
- **Podezření:** zdroje ukazují na možnou chybu, ale nedokazují ji, nebo výsledek závisí na nejednoznačném výkladu.
- **Nedostatečný důkaz:** hodnotu nebo tvrzení nešlo doložit dostupnými zdroji.
- Mimo tyto třídy jsou zvlášť vedené otázky výkladu PLAN.md (nejde o nález v datech) a omezení kontroly (co druhý agent neověřil).

U fáze A je třída převzatá ze sloupce `zaver`. Fáze B tytéž kategorie nepoužívala všude, její upřesnění zařadil hlavní agent podle znění cilene_otazky.md. Kde fáze B změnila závěr fáze A, je to u položky uvedeno.

## Otázky výkladu PLAN.md napříč kandidáty

Fáze B narazila na místa, která PLAN.md neupravuje. Rozhodnutí patří uživateli, tento soubor je nerozhoduje.

1. **Sídlo správce, nebo značky a týmu.** „Investiční firma (správce, značka) má sídlo v ČR“ nedává jednoznačnou odpověď, když správce (GP/AIFM) sídlí v Lucembursku a značka s týmem v Praze. Podle výkladu se mění zařazení `cz-n1-ventures`, `cz-tensor-ventures`, `cz-kaya-vc` a `cz-ii-biotech-investments`. `cz-depo-ventures` a `cz-zaka-vc` jsou CZ v obou výkladech. PLAN.md nemá ani otázku `sidlo` v nevyresene.csv.
2. **Klub nebo syndikát andělů.** Typ Angel je jen fyzická osoba, typ pro klub investující přes SPV chybí (`cz-garage-angels`, `cz-lumus-investments`).
3. **`neni_investor` pro subjekt bez investice v okně, který jinak investuje** (`cz-espira-investments`, `cz-mcwin-partners`). Bod 3 ho tam řadí, bod 2 říká, že status popisuje jen veřejnou stopu.
4. **Smíšená strategie equity a venture debt** (`cz-orbit-capital`): hranicni.csv, nebo vyrazeni.csv.
5. **Zakladatel a sponzor fondu, který investuje i přímo** (`cz-ii-prague` a `cz-ii-biotech-investments`).
6. **Kapitál:** schéma nemá pole pro přibližnou částku nebo mez (`cz-ii-biotech-investments`, `cz-inven-capital`, `cz-rockaway-ventures`), `plati_k` se vyplňuje nejednotně (u článků datum publikace, u nedatovaných webů null), PLAN.md nedefinuje hranici `committed_capital` / `fund_size` (`cz-czech-founders-vc` proti `cz-reflex-capital`, `cz-ii-biotech-investments`) a `fond` obsahuje popis místo názvu (`cz-kaya-vc`, `cz-reflex-capital`, `cz-soulmates-ventures`).
7. **`puvod`:** je volný text a u zpráv převzatých z oznámení firmy často null. U záznamů, kde nástroj stojí jen na nepřímé indicii, to jistotu nemění (strop `stredni`), u `cz-y-soft-ventures` ano.

## Nálezy podle id

### cz-n1-ventures

N1 Ventures · `investori.json` · zařazen · oddíl 1 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (11 sedi, 1 podezreni, 1 nedostatecny_dukaz).

**Podezření**

- `sidlo` (fáze A, `podezreni`): Web uvádí tři kanceláře: „415 Mission St, San Francisco, CA“, „Národní 135/14, Prague 1“, „Luxembourg 1A, Heienhaff, L-1736 Senningerberg“; tým „splits time between Prague and San Francisco“. Formální správci (GP/AIFM) i fondy jsou lucemburské. CzechCrunch a CVCA značku vedou jako českou. Zda má investiční firma/správce sídlo v ČR, zdroje jednoznačně neříkají; český právní subjekt nedoložen → zeme CZ je nejistá (agent sám uvádí „k ruční kontrole“). Zdroje: [n1.rocks/](https://n1.rocks/), [n1.rocks/disclosure](https://n1.rocks/disclosure), [cvca.cz/en/nation1-2/](https://cvca.cz/en/nation1-2/)
- `posledni_investice / dalsi_investice (Liki24)` (fáze B, nový nález): Podmínku 3 u N1 nese jediná investice, Liki24 (Series A, Forbes UA 3. 7. 2025: „Раунд підтримали … N1 Ventures“). Web N1 ji vede pod „U-Tech is an independent fund built by N1“. Zda investici fondu U-Tech připsat N1, zdroje nerozhodují: PLAN.md bod 3 vede fondy pod jedním správcem jako podřízené údaje, „independent fund“ to zpochybňuje.

**Nedostatečný důkaz**

- `pravni_subjekt` (fáze A, `nedostatecny_dukaz`): n1.rocks/disclosure: „Nation 1 GP S.à r.l and Nation 1 GP II S.à r.l. (the “GPs”), as general partner and registered alternative investment fund manager … of Nation 1 and Nation 1 VC fund II which are Luxembourg based alternative investment funds“. Jde jen o vlastní tvrzení webu; zápis v rejstříku/regulátoru (RCS, CSSF) agent nedoložil a ani já ho neotevřel. CVCA profil Nation1 a CzechCrunch 2023 existenci značky potvrzují. Jistota existence stredni odpovídá pravidlu, ale podmínka 1 bodu 2 (zápis v rejstříku nebo ekvivalent) zdroji doložena není. Zdroje: [n1.rocks/disclosure](https://n1.rocks/disclosure), [cvca.cz/en/nation1-2/](https://cvca.cz/en/nation1-2/), [cc.cz/z-nation-1-je-n1-cesti-startupovi-investori-chystaji-druhy-fond-chteji-…](https://cc.cz/z-nation-1-je-n1-cesti-startupovi-investori-chystaji-druhy-fond-chteji-do-nej-ziskat-necelou-miliardu/)
- `pravni_subjekt / sidlo` (fáze B, souhlas s fází A): Správci Nation 1 GP S.à r.l. a Nation 1 GP II S.à r.l. i fondy jsou podle n1.rocks/disclosure lucemburské. Česká právnická osoba nenalezena (uložené odpovědi ARES pro „N1 Ventures“ a „Nation1“). Zápis GP v RCS nebo u CSSF nikdo neotevřel, jde jen o vlastní tvrzení webu.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `rozsah_pilotu` (fáze B): Výsledek závisí na výkladu pravidla „investiční firma (správce, značka) má sídlo v ČR“: podle značky a týmu CZ, podle sídla správce mimo ČR. Viz Otázky výkladu PLAN.md, bod 1.

### cz-nation1

Nation1 · `mapovani_id.csv` · sloučen do `cz-n1-ventures` · oddíl 2 v [pruvodce.md](pruvodce.md)

Fáze A: 1 řádků (1 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-tensor-ventures

Tensor Ventures · `investori.json` · zařazen · oddíl 3 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (11 sedi, 1 podezreni).

**Podezření**

- `sidlo` (fáze A, `podezreni`): Web uvádí jako adresu „Tensor Ventures GP S.à r.l. & Tensor Ventures Fund I SCSp, 1A Heienhaff, 1736 Senningerberg, Luxembourg“ a jen „Contact in CZ Pernerova 697/35“; správce (GP) je tedy lucemburský. Pro CZ mluví tým, česká a.s. se stejnými osobami a TZ „Czech deep-tech company Tensor Ventures“. Zda „investiční firma (správce, značka)“ má sídlo v ČR, je výkladová otázka – agent ji správně označil k ruční kontrole. Zdroje: [tensor.ventures/](https://tensor.ventures/), [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06257241](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06257241), [theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-i…](https://theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-in-london-based-appfactor)
- `sidlo` (fáze B, souhlas s fází A): tensor.ventures/legal-disclosures: „Tensor Ventures GP S.à r.l (the “GP”), as general partner and registered AIFM of Tensor Ventures Fund I“. Česká Tensor Ventures a.s. (IČO 06257241) má v rejstříku „správa vlastního majetku“, její roli vůči fondu zdroje nedokládají. Správce druhého (koinvestičního) fondu nedoložen, článek CzechCrunch citovaný agentem druhý agent nečetl.
- `nezavislost_zdroju (ValkaAI)` (fáze B, upřesnění fáze A (jistota sedi)): Seznam Zprávy i Startbase mají `puvod` null, ačkoli Seznam píše „Firma zároveň uvádí“ a Startbase má foto „(c) ValkaAI“. Poznámka agenta sama uvádí, že „nejspíš vycházejí z informací firmy“. Jistotu `stredni` to nemění.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `rozsah_pilotu` (fáze B): Výsledek závisí na výkladu pravidla o sídle (správce, nebo značka a tým). Viz Otázky výkladu PLAN.md, bod 1.

### cz-kaya-vc

KAYA VC · `investori.json` · zařazen · oddíl 4 v [pruvodce.md](pruvodce.md)

Fáze A: 15 řádků (14 sedi, 1 podezreni).

**Potvrzený rozpor**

- `kapital[2]` (fáze B, oprava fáze A (sedi → nedostatecny_dukaz)): Položka má `druh` = `committed_capital` a vyplněný `fond` = „pátý fond (po first closingu)“. PLAN.md bod 4: „`fond` je název fondu u `fund_size`, jinak `null`“. Rozpor s pravidlem je doslovný, fáze B ho podle zadání kontroly zapsala jako nedostatecny_dukaz. Částka 70 000 000 EUR, měna, druh a datum (CzechCrunch 25. 6. 2025) sedí. Zda jde o chybu dat, nebo o příliš přísné pravidlo, nechala fáze B na uživateli.

**Podezření**

- `posledni_investice` (fáze A, `podezreni`): Viktor sedí (Fortune „May 19, 2026“, Series A, Kaya VC jmenována; datum_pro_filtr oznameni správně). Je ale pravděpodobně novější investice: Nordic9 (31 August 2026) „Frontier Computing raised $10M pre-seed, led by General Catalyst“ a v „Round investors“ uvádí „Kaya VC“. Jde o databázi bez odkazu na zprávu, která by Kayu jmenovala, takže to nedokazuji; Nordic9 profil Kaya uvádí v portfoliu i „Frontier Computing“. Status aktivni by se nezměnil. Zdroje: [finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-rai…](https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html), [nordic9.com/news/frontier-computing-raised-10m-pre-seed-led-by/](https://nordic9.com/news/frontier-computing-raised-10m-pre-seed-led-by/), [nordic9.com/companies/kaya-vc/](https://nordic9.com/companies/kaya-vc/), `websearch: Kaya VC investment 2026 Sensible Biotechnologies Frontier Computing round`
- `sidlo` (fáze B, oprava fáze A (sedi → podezreni)): kaya.vc/sustainability: „KAYA VC GP S.à r.l (the “General Partner” or “KAYA”), which is registered as a Luxembourg AIFM“. Česká Kaya F3 GP s.r.o. (IČO 19844166) je podle názvu GP jednoho fondu, kterého, zdroje neříkají. První agent lucemburského AIFM nezmínil a CZ zdůvodnil „podle rejstříku GP v Praze“. Fáze A stránku /sustainability nečetla. Kanceláře: Varšava, Praha, San Francisco, Londýn.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `rozsah_pilotu` (fáze B): Výsledek závisí na výkladu pravidla o sídle. Viz Otázky výkladu PLAN.md, bod 1.
- `kapital[1], kapital[2]` (fáze B): „$85M Current Fund“ a „70 mil. EUR pátý fond po first closingu“ jsou pravděpodobně týž fond v jiné fázi a měně. Agent je nesčítá, což odpovídá PLAN.md. `fond` u kapital[1] je popis, ne název.

### cz-ii-biotech-investments

i&i Biotech Investments · `investori.json` · zařazen · oddíl 5 v [pruvodce.md](pruvodce.md)

Fáze A: 14 řádků (13 sedi, 1 podezreni).

**Podezření**

- `sidlo` (fáze A, `podezreni`): Investor se sám popisuje jako lucemburský: „i&i Bio is a Luxembourg-based venture capital firm“ (web, novinky) a „Headquarters i&i Biotech Fund I SCSp … L-2661 Luxembourg“; česká s.r.o. je jen „Investment Adviser“. Tým a CVCA členství jsou v Praze, takže CZ je obhajitelné jako sídlo týmu, ale vlastní popis značky říká Lucembursko – pro pravidlo pilotu (sídlo investiční firmy v ČR) k ruční kontrole. Zdroje: [inibio.eu/](https://www.inibio.eu/), [inibio.eu/news/t-curx-announces-%2420m-series-a-first-closing-led-by-biomedvc…](https://www.inibio.eu/news/t-curx-announces-%2420m-series-a-first-closing-led-by-biomedvc-to-fund-pipeline-of-clinical-stage-car-t-programs-and-advance-proprietary-non-viral-in-vivo-car-t-platform), [inibio.eu/news/experienced-businessmen-join-forces-with-excellent-science%2C-…](https://www.inibio.eu/news/experienced-businessmen-join-forces-with-excellent-science%2C-invest-%E2%82%AC2m-in-the-fund-at-the-iocb), [cvca.cz/en/biotech-investments/](https://cvca.cz/en/biotech-investments/)
- `sidlo` (fáze B, souhlas s fází A): Citace „i&i Bio is a Luxembourg-based venture capital firm“ ověřena (text pod novinkami, ne na hlavní stránce). Fond i&i Biotech Fund I SCSp sídlí v Lucembursku, česká Biotech Investments s.r.o. je „Investment Adviser“. Agent lucemburský fond uvedl, ale bez označení „k ruční kontrole“ a bez vlastního popisu značky.
- `nezavislost_zdroju (Theorema)` (fáze B): Tři zprávy o Theoremě (Lupa, CzechCrunch, Vestbee) mají `puvod` null, podle bodu 6 by tedy formálně šlo o tři původy. Lupa ale píše „Startup Theorema … oznámil“, Vestbee má stejný výčet investorů a CzechCrunch vyšel týž den, spíš jde o jeden původ (oznámení startupu). Poznámka agenta sama uvádí, že nezávislost doložená není. Jistota `stredni` je povinná už proto, že žádná investice nemá `nastroj.doklad` = `dolozeno` (fáze A ji nazvala „konzervativně správnou“, fáze B zdůvodnění opravila).
- `nezavislost_zdroju (Ternary, Antiverse)` (fáze B): `puvod` null je sporný u IT Brief (Ternary, „Ternary says…“) a u Vestbee (Antiverse, „as Vestbee was informed“). Obě jsou jediným zdrojem dané investice, na jistotu bez vlivu.

**Nedostatečný důkaz**

- `sidlo` (fáze B): Kdo je správce (GP/AIFM) fondu i&i Biotech Fund I SCSp (RCS B 252970), web ani SFDR stránka neuvádějí a nikdo to neověřil.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kapital[0]` (fáze B): „approximately €47 million“ (30. 11. 2022) je uloženo jako přesné číslo, přibližnost je jen v poznámce. Na téže stránce je novější nedatovaný údaj „manages over €53 million“, nezapsán. Hranici mezi `fund_size` a `committed_capital` PLAN.md nedefinuje.
- `rozsah_pilotu` (fáze B): Výsledek závisí na výkladu pravidla o sídle. Viz Otázky výkladu PLAN.md, bod 1.

### cz-zaka-vc

ZAKA VC · `investori.json` · zařazen · oddíl 6 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (9 sedi, 3 podezreni).

**Podezření**

- `pravni_subjekt` (fáze A, `podezreni`): ARES: ZAKA Management s.r.o. (dříve ZAKA VC I s.r.o.), IČO 21053987, Italská 2581/67, Praha 2, jednatelé Samuel Zálešák a Karolína Kasperová, společník ZAKA Holding s.r.o.; ZAKA VC I, osoba rizikového kapitálu, a.s., IČO 21514992, stejné sídlo, správní rada Kasperová (předsedkyně) a Zálešák, § 15 ZISIF. Existence doložena. Že je ZAKA Management „správce značky“, rejstřík nedokládá – fond ZAKA VC I nemá ZAKA Management ve statutárním orgánu; propojení se zakladateli Jánem Kasperem a Peterem Zálešákem (CzechCrunch) je jen přes příjmení (agent to uvádí). Zdroje: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21053987](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21053987), [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21514992](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21514992), [cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milio…](https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/)
- `typ` (fáze A, `podezreni`): Web: „We are a seed & pre-seed VC fund“; CzechCrunch 22. 7. 2024: „se mění z rodinného na klasický startupový fond“, „poprvé otevřel také externím investorům“. Ale AIN.UA 10. 3. 2025 (zdroj, který agent sám cituje u Yenmo): „ZAKA VC is one of the most active family offices in Europe.“ a web rozlišuje „Family office 5M invested 34“ vs. „Fund 1 17M“. Tvrzení v poznámce „jako family office se neoznačuje“ tedy úplně neplatí; část investic (např. přes ZAKA Startup 13 j.s.a.) může jít z rodinného vehiklu. VC je pro Fund 1 obhajitelné, ale zdroje si částečně odporují (bod 2: nejednoznačný typ → ruční rozhodnutí). Zdroje: [zaka.vc/](https://zaka.vc/), [cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milio…](https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/), [en.ain.ua/2025/03/10/zaka-vc-joins-11m-yenmo/](https://en.ain.ua/2025/03/10/zaka-vc-joins-11m-yenmo/)
- `posledni_investice` (fáze A, `podezreni`): ParcelBio 2026-05-07 sedí (TZ Business Wire přes BioSpace). Ale stránka novinek ZAKA uvádí novější oznámení investic: 16. 7. 2026 „That’s why we’re excited to announce our investment in FinalDose.“ a 18. 8. 2026 tisková zpráva „PerfectBit: Building the Verified Data Layer for Physical AI“; PitchBook (WebSearch) uvádí PerfectBit seed 26-Jun-2026. Vlastní oznámení investora je podle bodu 2 tisková zpráva, takže nejnovější doložená investice může být novější než ParcelBio (status by se nezměnil). Sensible Biotechnologies ($47M, 10/2026) ZAKA neúčast – jen dřívější investor. Zdroje: [biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-t…](https://biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-to-advance-next-generation-mrna-medicines), [zaka.vc/news/](https://zaka.vc/news/), `websearch: ZAKA VC FinalDose PerfectBit seed round 2026`, `websearch: Sensible Biotechnologies $47M ZAKA VC`
- `pravni_subjekt` (fáze B, souhlas s fází A): Provozovatelem webu je podle zaka.vc/privacy-policy fond ZAKA VC I, osoba rizikového kapitálu, a.s. (IČO 21514992), ne ZAKA Management s.r.o., kterou agent uvádí jako „správce značky“. Sídlo je CZ v obou výkladech pravidla o sídle.

### cz-startupyard

StartupYard · `investori.json` · zařazen · oddíl 7 v [pruvodce.md](pruvodce.md)

Fáze A: 11 řádků (9 sedi, 2 podezreni).

**Podezření**

- `pravni_subjekt` (fáze A, `podezreni`): ARES: StartupYard Services s.r.o., IČO 06002820, Perlová 371/5, Praha 1, jednatel Nikola Rafaj, jediný společník Startup Yard Limited (Londýn), datumAktualizace 2020-10-15; StartupYard Batch 15 s.r.o. (IČO 22266852) stejná adresa, jednatel Rafaj, od 2026-03-21 další společníci vč. KINSKÝ Žďár, a.s. Existence subjektů doložena. Vazba konkrétního subjektu na značku jako investiční firmu je jen nepřímá: Lupa 2012 dokládá Rafaje jako ředitele StartupYardu, ale web StartupYardu (článek o TechBoost Syndicate) uvádí jako CEO „Cedric Maloux“; který subjekt investoval do Ydoca, zdroje neuvádějí (agent to přiznává). Ydoca s.r.o. (IČO 21364460) má v ARES jen dva zakladatele po 50 %. Zdroje: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06002820](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06002820), [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22266852](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22266852), [lupa.cz/clanky/startupyard-zmenil-majitele-sefovat-mu-bude-nikola-rafaj/](https://www.lupa.cz/clanky/startupyard-zmenil-majitele-sefovat-mu-bude-nikola-rafaj/), [startupyard.com/startupyard-and-depo-ventures-double-down-on-early-stage-deep…](https://startupyard.com/startupyard-and-depo-ventures-double-down-on-early-stage-deeptech-founders/), [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21364460](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21364460)
- `typ` (fáze A, `podezreni`): Subjekt se sám označuje jako akcelerátor („Accelerating Startups Since 2011“), funding.tech.eu typ „Accelerator“. Batch 15 (11. 9. 2025): „For the first time, founders can access an optional €25,000 cash investment“ – tedy přímé investování za peníze je u akcelerátoru nové, nabízené jako konvertibilní nota. Ydoca (únor 2025) proběhla v době spolupráce s DEPO Ventures v rámci „TechBoost Syndicate“ (web StartupYard, 2024: „Investors interested to join the Syndicate can apply here“), takže není jasné, zda 500 tis. Kč byly vlastní peníze StartupYardu, nebo syndikátu andělů. Pravidlo „akcelerátor investující vlastní peníze za podíl → VC“ je tak doloženo jen částečně. Zdroje: [startupyard.com/](https://startupyard.com/), [startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/](https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/), [startupyard.com/startupyard-and-depo-ventures-double-down-on-early-stage-deep…](https://startupyard.com/startupyard-and-depo-ventures-double-down-on-early-stage-deeptech-founders/), [cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-…](https://cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investovali-depo-ventures-a-startupyard/), [ai-log/02-obohaceni/zdroje/fundingtecheu_inv_StartupYard.json](../../ai-log/02-obohaceni/zdroje/fundingtecheu_inv_StartupYard.json)
- `je_investor (Ydoca)` (fáze B): Podmínku 3 nese jediná investice, Ydoca (CzechCrunch: pre-seed, StartupYard 500 tis. Kč). Fáze A u typu uvádí, že není jasné, zda šlo o vlastní peníze StartupYardu, nebo syndikátu andělů. `puvod` null u zprávy CzechCrunch nelze vyvrátit. Web (Batch 15) nabízí „simple convertible note“, což je přípustný nástroj.

### cz-ii-prague

i&i Prague · `investori.json` · zařazen · oddíl 8 v [pruvodce.md](pruvodce.md)

Fáze A: 11 řádků (11 sedi).

**Nedostatečný důkaz**

- `je_investor (vztah k cz-ii-biotech-investments)` (fáze B): i&i Prague je zakladatelem a „main sponsor“ fondu i&i Biotech Fund I SCSp a zároveň investuje přímo: rejstřík CasInvent Pharma ukazuje úpis akcií i&i Prague v letech 2023 a 2025 a akcionáře při založení 2020. Kolo CasInvent 2025 fond i&i Biotech neupisoval, investice tedy patří i&i Prague (to rozhodnutí agenta podporuje). Kdo je GP fondu (RCS B 252970), nikdo neověřil. Kdyby to byla entita skupiny IOCB Tech / i&i Prague, mohl by se změnit výklad „jedna investiční firma“.
- `typ` (fáze B): Část portfolia (12 firem) může pocházet ze zakládání spin-offů (venture builder, vklad know-how), ne z peněžní investice. Zdroje to nerozlišují.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `je_investor, typ` (fáze B): PLAN.md neřeší subjekt, který je zároveň sponzorem fondu a přímým investorem. Výluku „čistý LP“ i&i Prague nesplňuje. Pravidlo o akcelerátoru s vlastním kapitálem (typ VC) je na inkubátor použité výkladem. CVC sedí jen volně (vlastníkem je IOCB Tech, firma ÚOCHB AV ČR).

### cz-orbit-capital

Orbit Capital · `hranicni.csv` · hraniční, druh `venture_debt` · oddíl 9 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Nedostatečný důkaz**

- `kategorie (Sloneek)` (fáze B, nový nález): Caplight („Sloneek Jun 2026 Series A Lead“) a Seedtable vedou Orbit jako lead série A Sloneeku. Primární zprávu se zněním nástroje druhý agent nenašel (parsers.vc za registrací, Seedtable HTTP 403). Dluh u Sloneeku dokládá jen to, že ho tech.eu řadí mezi investice Growth Debt Fund II. Kdyby šlo o podíl, Orbit by splnil body 2 a 3.
- `kategorie (IAG)` (fáze B): IAG zmiňuje jen článek o fondu, samostatnou zprávu o transakci druhý agent nenašel. Nástroj ani datum nejsou doložené konkrétní zprávou.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kategorie` (fáze B): Orbit má strategii Growth Equity i Growth Debt a v okně doložil jen dluh (Coding Giants, Jutro Medical výslovně). PLAN.md neříká, zda takový subjekt patří do hranicni.csv (`venture_debt`), nebo do vyrazeni.csv jako `neni_investor`. nevyresene.csv formálně nesedí, je jen pro typ a nástroj.

**Omezení kontroly (co druhý agent neověřil)**

- `duvod` (fáze A): Vestbee 2023 zmíněný v důvodu není v seznamu URL, neověřeno, bez vlivu.

### cz-mcwin-partners

McWin Partners · `vyrazeni.csv` · vyřazen, kategorie `neni_investor` · oddíl 10 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Podezření**

- `kategorie` (fáze B, oprava fáze A (sedi → sedí formálně, oddělení sporné)): McWin Partners s.r.o. (family office zakladatelů) a McWin Capital Partners (Londýn) mají stejné zakladatele a společnou značku, mcwin.cz odkazuje na mcwin.fund a portfolio na mcwin.cz se překrývá s fondy McWin (EasyMile, Exergyn, Vapiano, dean&david, EVERY). Proti: jiný právní subjekt, jiná role a mcwin.fund/our-team uvádí „McWin Partners Family Office“ jako samostatný subjekt. Pokud jde o jednu investiční firmu, existuje transakce v okně (Goodwin 14. 10. 2025, Ecorobotix Series D přes McWin Food Tech Fund) a kategorie by byla `mimo_rozsah_pilotu` (sídlo Londýn), ne `neni_investor`. Do pilotu se McWin nedostane v žádné variantě.
- `duvod` (fáze B): Důvod je věcně přesný, ale nezmiňuje překryv portfolia a značky, který je pro rozhodnutí o duplicitě podstatný. Agent rozhodnutí neoznačil jako sporné.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kategorie` (fáze B): PLAN.md řadí „bez doložené investice v okně“ do `neni_investor`, i když subjekt jinak investuje (bod 2: status popisuje jen veřejnou stopu). Vztah family office zakladatelů a jejich správce fondů PLAN.md neřeší.

### cz-espira-investments

Espira Investments · `vyrazeni.csv` · vyřazen, kategorie `neni_investor` · oddíl 11 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Podezření**

- `duvod` (fáze B, upřesnění fáze A (sedi s drobnou výhradou)): „jiný fond a tým“ je zkratka: Mamajová je společnicí ESPIRA Investments s.r.o. (ARES 05528089) i EVERITA Capital s.r.o. (ARES 19067097). Fáze B to nepovažuje za věcnou chybu, závěr se nemění.

**Nedostatečný důkaz**

- `kategorie` (fáze B): Investici v okně nenašla ani fáze B (web, vyhledávání, funding.tech.eu). Sbírku listin (výroční zprávy ESPIRA Investments s.r.o., IČO 05528089) nikdo neprošel. Nejnovější vstup 8. 2. 2022 (Premier Clinic), exit 27. 7. 2022 (ICON).

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kategorie` (fáze B): `neni_investor` je podle PLAN.md formálně správně (bez investice v okně), Espira ale v letech 2018–2022 doloženě investovala. Zda brát EVERITA Capital (nová firma spoluzakladatelky na stejné adrese) jako nástupce, PLAN.md neřeší. Zdroje dokládají dvě různé firmy. V obou variantách je subjekt mimo pilot (typ PE).

### cz-rockawayx

RockawayX · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 12 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (1 podezreni, 1 nedostatecny_dukaz).

**Podezření**

- `duvod` (fáze A, `podezreni`): Většina faktů sedí: Cointelegraph 5. 5. 2026 „they co-led OnRe’s $5 million Series A round“; insight RockawayX „a leading multi-strategy digital asset investment firm with over $1.5 billion in AUM“ a zároveň „with over $2 billion in AUM“; CzechCrunch 27. 8. 2026 „venture fondy, tržně neutrální fond, takzvané vaulty přímo na blockchainu a nyní hedgeový fond“, kanceláře „v Praze, Londýně, New Yorku a Dubaji“; funds: VC I a VC II „[Closed]“, Liquid Opportunities (Cayman, CIMA) a Market Neutral Fund (Liechtenstein, „provides capital to digital asset protocols and companies“) „[Active]“; patička „© 2026 Blockad s.r.o.“, ARES Blockad s.r.o. IČO 08006458, Generála Píky 430/26, jednatel Viktor Fischer, 100% společník RockawayX a.s. IČO 17457009. Nesrovnalosti: (1) důvod opomíjí, že podle téhož článku CzechCrunch RockawayX v okně koupilo hedge fondovou firmu Relayer Capital (web: „RockawayX acquires crypto-focused hedge fund firm, Relayer Capital“, 25. 8. 2026) – další možná přímá transakce; (2) důvod sám uvádí jako rozhodující „equity vs. token vs. úvěr“ u OnRe a fond VC II výslovně investuje do „venture equity, pre-launch token projects, liquid tokens“, tedy nejistý je i nástroj, ne jen typ. Homepage uvádí kanceláře jen „London, Prague, and Dubai“ (New York je z CzechCrunch). Zdroje: [cointelegraph.com/news/forward-industries-rockawayx-onre-solana-reinsurance](https://cointelegraph.com/news/forward-industries-rockawayx-onre-solana-reinsurance), [rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-inv…](https://www.rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre), [rockawayx.com/funds](https://rockawayx.com/funds), [rockawayx.com/](https://rockawayx.com/), [cc.cz/cesi-krypto-a-40-miliard-pro-investice-nic-takoveho-zatim-jeste-nikdo-n…](https://cc.cz/cesi-krypto-a-40-miliard-pro-investice-nic-takoveho-zatim-jeste-nikdo-nepostavil-rika-sef-rockawayx/), [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08006458](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08006458)

**Nedostatečný důkaz**

- `otazka_moznosti` (fáze A, `nedostatecny_dukaz`): Otázka je jen „typ“ s možnostmi „zarazen | mimo_rozsah_pilotu“, ale důvod jako rozhodující uvádí i podobu investice do OnRe (equity vs. token vs. úvěr). Pokud by účast byla tokenová/úvěrová a nebyla by jiná doložená investice za podíl, výsledek by byl neni_investor, který ve výčtu chybí; podle PLAN.md by pak otázka měla být „typ | nastroj“. Proti tomu: Series A dává podle bodu 4 neprima_indicie a OnRe je „Bermuda-licensed reinsurance company“ (firma), takže pracovní předpoklad podmínky 3 je obhajitelný – pak je ovšem odkaz na nástroj v důvodu nadbytečný. Otázka a důvod si tedy vnitřně neodpovídají. Zdroje: [cointelegraph.com/news/forward-industries-rockawayx-onre-solana-reinsurance](https://cointelegraph.com/news/forward-industries-rockawayx-onre-solana-reinsurance), [rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-inv…](https://www.rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre), [rockawayx.com/funds](https://rockawayx.com/funds)

### cz-lumus-investments

LUMUS Investments · `nevyresene.csv` · nevyřešen, otázka `typ | nastroj` · oddíl 13 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `duvod, otazka` (fáze B): Garage Angels (vyrazeni.csv, `mimo_rozsah_pilotu`) má podle fáze B stejnou strukturu (klub andělů, organizátor zakládá SPV pro každý deal) a stejnou otázku typu, kterou agent u LUMUS nechal nevyřešenou. U LUMUS k tomu přistupuje nezjištěný nástroj (Lumus ani jeho SPV nejsou mezi společníky Kardi AI), který by ho do nevyresene.csv poslal i sám. Viz cz-garage-angels.

### cz-chilli-ventures

Chilli Ventures · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 14 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Omezení kontroly (co druhý agent neověřil)**

- `duvod` (fáze A): CzechCrunch 2. 6. 2025 a PitchBook jsou v důvodu zmíněné bez URL, druhý agent je neověřil.

### cz-fond-nase-cesko

Fond Naše Česko · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 15 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Omezení kontroly (co druhý agent neověřil)**

- `duvod` (fáze A): Údaj nordic9 („Bank“) je v důvodu bez URL, neověřeno.

### cz-moonhill-capital

Moonhill Capital · `nevyresene.csv` · nevyřešen, otázka `typ | nastroj` · oddíl 16 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Omezení kontroly (co druhý agent neověřil)**

- `duvod` (fáze A): Článek EU-Startups (Ekiden) vrátil HTTP 403. Fakta druhý agent ověřil z převzetí v Portugal Startup News.

### cz-botanique-hospitality

Botanique Hospitality · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 17 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-braiins

Braiins · `nevyresene.csv` · nevyřešen, otázka `nastroj` · oddíl 18 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-gi21-capital

Gi21 Capital · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 19 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-jet-investment

Jet Investment · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 20 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-kkcg

KKCG · `nevyresene.csv` · nevyřešen, otázka `nastroj` · oddíl 21 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-tarpan-capital

Tarpan Capital · `nevyresene.csv` · nevyřešen, otázka `typ` · oddíl 22 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-garage-angels

Garage Angels · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 23 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Podezření**

- `kategorie` (fáze B, oprava fáze A (sedi → podezreni)): Fáze A zvážila jen alternativu VC/CVC. Podle fáze B je právním držitelem podílu SPV (GA Investiční VRV, CSI, GCOM, KAI), kterou Garage Angels Management s.r.o. založí, drží v době úpisu a pak převede na jednotlivé anděly (ARES: VRV ve vlastnictví Managementu do 2. 6. 2026, CSI do 19. 7. 2025). Tisková zpráva CasInvent (khanu.de): „independent investors from the Garage Angels network“, „an informal group of about 15 independent individual investors“. Předmět podnikání Management s.r.o.: „zprostředkování obchodu a služeb“. Pokud je klub organizátor investic jednotlivých andělů, kategorie by byla `neni_investor`, pokud investor, `mimo_rozsah_pilotu`. PLAN.md definuje Angel jako fyzickou osobu a typ pro klub nemá.
- `kategorie (konzistence s LUMUS)` (fáze B): Strukturně obdobný LUMUS agent poslal do nevyresene.csv s otázkou typu, Garage Angels rozhodl sám. Viz cz-lumus-investments.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `duvod` (fáze A i B (řádek se závěrem sedi)): K. Obluk je společníkem GA Investiční GCOM, ne VRV. Důvod uvádí společníky souhrnně za obě SPV, fáze A to proto vedla jako drobnou nepřesnost se závěrem sedi.

**Omezení kontroly (co druhý agent neověřil)**

- `web (nehodnotí se)` (fáze B): Sloupec `web` je prázdný, ačkoli tiskové zprávy CasInvent uvádějí www.g-angels.cz. Web se druhému agentovi nepodařilo stáhnout (HTTP 301).

### cz-look-ai-ventures

Look AI Ventures · `investori.json` · zařazen · oddíl 24 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (10 sedi, 2 potvrzeny_rozpor).

**Potvrzený rozpor**

- `pravni_subjekt` (fáze A, `potvrzeny_rozpor`): Identita sedí: ARES „Look AI Ventures SICAV, a.s.“, IČO 17604087, Radlická 180/50, Praha 5, statutární orgán AVANT investiční společnost do 2026-10-05, od 2026-10-05 FTP Dimension investiční společnost; web „Look AI Ventures SICAV, a.s., Company ID No.: 176 04 087“. Look AI Investments, a.s. (IČO 06385745) má jako akcionáře „Look AI Ventures SICAV, a.s, jednající na účet Podfondu Look AI Ventures I“. Rozpor v detailu poznámky: agent píše, že ve správní radě Look AI Investments jsou „Martin Havlík a Daniel Kunz“, ale ARES uvádí Daniela Kunze ve správní radě jen 2017-08-29 až 2021-01-04; nyní je jediným členem Martin Havlík (od 2026-04-17). Vazba týmu na značku platí přes Havlíka a web. Existence vysoka v pořádku. Zdroje: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17604087](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17604087), [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06385745](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06385745), [lookai.vc/](https://lookai.vc/)
- `posledni_investice` (fáze A, `potvrzeny_rozpor`): Údaje o Sodex sedí (tech.eu „13 July 2026“: „The round also welcomed new investors Bloomhaus, Look AI Ventures and … Superangels“; datum_pro_filtr oznameni správně). Sodex ale není nejnovější doložená investice: na lookai.vc je zpráva z „September 22, 2026“ „Look AI Ventures has backed Embodied AI, a Lausanne-based robotics startup … The round was led by Faber VC“ (tisková zpráva investora, i na titulní stránce v News). Status aktivni se nemění. Také Checkstep (web „May 29, 2026 Look AI Ventures Backs Checkstep in £3M Round“) zpráva existuje, i když agent ji nedohledal. Zdroje: [tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligen…](https://tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligence-to-construction-sites/), [lookai.vc/](https://lookai.vc/), [lookai.vc/look-ai-ventures-backs-embodied-ai-robots-manufacturing/](https://lookai.vc/look-ai-ventures-backs-embodied-ai-robots-manufacturing/)

**Podezření**

- `nezavislost_zdroju (Lucida AI)` (fáze B): tech.eu a Lupa mají `puvod` null, poznámka agenta přitom píše „pravděpodobně společný podklad“. Lupa má navíc citaci partnera Look AI, původ tedy ze stránek určit nelze. Na jistotu bez vlivu (strop `stredni`).

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `je_investor (Digicust)` (fáze B): Smíšené kolo (vklady investorů, garance aws „Equity Leverage“, konverze FlexCo). O nástroji Look AI („the Look.AI Fund is contributing €250,000“) zdroj nic neříká. Bod 4 chce v takovém případě rozhodovat podle účasti konkrétního investora.

### cz-jic-ventures

JIC Ventures · `investori.json` · zařazen · oddíl 25 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (11 sedi, 1 potvrzeny_rozpor).

**Potvrzený rozpor**

- `posledni_investice` (fáze A, `potvrzeny_rozpor`): Údaje o FaceUp sedí (TZ JIC „19. 5. 2026“, Series A, vazba JIC Ventures; datum_pro_filtr oznameni správně). FaceUp ale není nejnovější doložená investice: Nordic9 (27 September 2026) „Elredo Voice closed a CZK 24 million pre-seed round led by JIC Ventures“ a Dealroom News (Oct 7, 2026) „JIC Ventures … has led a funding round of more than €1 million in Elredo Voice“ s citací Miloše Sochora. Status aktivni se nemění. (Starší vehikl JIC Ventures, s.r.o. je navíc v ARES CasInvent upisovatelem akcií v kole z 22. 5. 2025 – nezapsáno, ale starší než FaceUp.) Zdroje: [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do), [nordic9.com/news/elredo-voice-closed-a-czk-24-million-pre-seed/](https://nordic9.com/news/elredo-voice-closed-a-czk-24-million-pre-seed/), [dealroom.co/news/160679-elredo-voice-raises-1m-to-bring-ai-audiobook-producti…](https://dealroom.co/news/160679-elredo-voice-raises-1m-to-bring-ai-audiobook-production-to-us-publishers/), `websearch: Elredo Voice JIC Ventures pre-seed`

### cz-purple-ventures

Purple Ventures · `investori.json` · zařazen · oddíl 26 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (12 sedi, 1 potvrzeny_rozpor).

**Potvrzený rozpor**

- `posledni_investice` (fáze A, `potvrzeny_rozpor`): Comparables.ai (Tech.eu 6. 10. 2026 „with participation from Purple Ventures“, Lupa 13. 10. 2026 „Český fond Purple Ventures se zapojil 10 miliony Kč“) je doložená, ale není nejnovější: TheSaaSNews 14. 10. 2026 „FLÆ Robotics Raises €1M Seed … The funding round included participation from Purple Ventures and Garage Angels“ (Funding Date: October 14, 2026; odkaz na tuto zprávu jsem našel přes databázi Nordic9 na stránce Merchantee: „Flae Robotics raised €1 million in seed funding from Purple Ventures and Garage Angels“, 12 October 2026). Status se nemění (aktivni). Zdroje: [tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for…](https://tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for-dealmakers/), [lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy…](https://www.lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy-ze-sveta-do-projektu-se-zapojuji-cesi/), [thesaasnews.com/news/fl-robotics-raises-1m-seed/](https://www.thesaasnews.com/news/fl-robotics-raises-1m-seed/), [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/), `websearch: Flae Robotics seed Purple Ventures Garage Angels`

**Nedostatečný důkaz**

- `nezavislost_zdroju (Comparables.ai)` (fáze B): Původ zpráv tech.eu a Lupa (obě `puvod` null) nelze ze stránek určit. Lupa má údaj 10 mil. Kč a citaci Jana Staňka, které tech.eu nemá. Podmínku 3 nese jen Comparables.ai (Vetstor a Talentiqa mají `nezjisteno`).

### cz-reflex-capital

Reflex Capital · `investori.json` · zařazen · oddíl 27 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (11 sedi, 1 potvrzeny_rozpor).

**Potvrzený rozpor**

- `posledni_investice` (fáze A, `potvrzeny_rozpor`): Grid.online (CC a E15 22. 6. 2026) je doložená, ale není nejnovější doložená investice: CzechCrunch 21. 10. 2026 (ArtMaster): „Teď ArtMaster uzavřel investici ve výši 2,4 milionu dolarů … K dřívějším investorům se nově přidávají fondy Factorial Capital a český Reflex Capital“. Na ArtMaster upozorňuje i databáze Nordic9 na stránce Merchantee, kterou agent sám cituje („ArtMaster raises $2.4M in a seed round led by Factorial Capital, with participation from Reflex Capital“, 21 October 2026). Status se nemění (aktivni). Zdroje: [cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-no…](https://cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-novy-startup-uz-ma-150-milionu/), [e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zme…](https://www.e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zmenit-zpusob-dorucovani-baliku-1433723), [cc.cz/kdysi-si-v-amsterdamske-red-light-district-vydelaval-hranim-dnes-uz-dik…](https://cc.cz/kdysi-si-v-amsterdamske-red-light-district-vydelaval-hranim-dnes-uz-diky-ai-uci-na-piano-stovky-tisic-lidi/), [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/), `websearch: ArtMaster $2.4M seed Factorial Capital Reflex Capital`

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kapital[0]` (fáze B): „upsali dvaadvacet“ je zapsané jako `fund_size` s fondem, obdobná formulace u Czech Founders VC jako `committed_capital`. PLAN.md hranici nedefinuje. `fond` obsahuje popis („třetí fond Reflex Capital (název ve zdroji neuveden)“), ne název.

### cz-soulmates-ventures

Soulmates Ventures · `investori.json` · zařazen · oddíl 28 v [pruvodce.md](pruvodce.md)

Fáze A: 15 řádků (14 sedi, 1 nedostatecny_dukaz).

**Potvrzený rozpor**

- `posledni_investice / nastroj (Rightcharge 2026)` (fáze B, zpřesnění fáze A): „Seed“ je jen v titulku UKTN. Text tiskové zprávy: „has raised a £500,000 growth funding round from existing investors“, CEO: „since our seed round“. Kolo seed tedy zdroj nedokládá, text mu odporuje. Investice by měla mít `kolo` null a `doklad` `nezjisteno`. Podmínku 3 nesou Rightcharge 2025 (seed) a Antiverse (Series A).
- `nezavislost_zdroju (Rightcharge 2025)` (fáze B, oprava fáze A („spíš nepřesný“ → chybný)): Stránka UKTN je tisková zpráva (datelina „LONDON, United Kingdom (October 23, 2025)“, UKTN „we publish press releases“). `puvod` má být TZ Rightcharge, ne null. Na jistotu bez vlivu.

**Podezření**

- `nezavislost_zdroju (Antiverse)` (fáze B): Tech Funding News má `puvod` null. Má vlastní rozhovor, ale citace Sikyty je doslova shodná s Vestbee („as Vestbee was informed“).

**Nedostatečný důkaz**

- `nastroj` (fáze A, `nedostatecny_dukaz`): Poslední investice: kolo „seed“ je převzato jen z titulku/štítku UKTN („£500,000 Seed investment“); text TZ i Vestbee a Pulse 2.0 mluví o „growth funding round“ / „follow-on round“ od stávajících investorů, nikoli o seed či series kole – podmínka neprima_indicie (bod 4) je u této investice splněná jen sporně. Podmínka 3 je ale splněná jinými investicemi: Rightcharge 2025 „The £1.6M seed round was led by Soulmates Ventures“ a Antiverse „Series A … led by Soulmates Ventures“ (neprima_indicie, nástroj výslovně nikde neuveden). Zdroje: [uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmat…](https://www.uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmates-ventures-blackwood-ventures-and-purple-ventures/), [vestbee.com/insights/articles/rightcharge-raises-500-k](https://vestbee.com/insights/articles/rightcharge-raises-500-k), [pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20…](https://pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20x-arr-growth/), [uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-le…](https://www.uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-led-by-soulmates-ventures/), [techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseas…](https://techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseases-with-no-effective-treatments/)
- `kapital[1]` (fáze B): 50 mil. EUR: Vestbee „has raised“, web „has launched“. Zda jde o upsanou, nebo cílovou velikost, zdroje neříkají. AUM 62 mil. EUR může být týž fond po navýšení (LinkedIn citovaný v poznámce nikdo nečetl).

### cz-y-soft-ventures

Y Soft Ventures · `investori.json` · zařazen · oddíl 29 v [pruvodce.md](pruvodce.md)

Fáze A: 11 řádků (10 sedi, 1 podezreni).

**Podezření**

- `jistota_investice` (fáze A, `podezreni`): Agent dal stredni s odůvodněním, že nezávislost nedoložena, ale u všech tří zpráv (EIT Jumpstarter, CzechCrunch, The Recycler) zapsal puvod null; podle pravidla bodu 4/6 by to znamenalo tři různé původy a úroveň vysoka. Buď je puvod vyplněn nepřesně (CzechCrunch „Letos již hlásili“ odkazuje na dřívější oznámení), nebo je jistota podhodnocená – nekonzistence k ruční kontrole. Nástroj je dolozeno, takže pravidlo „bez dolozeno → stredni“ zde neplatí. Zdroje: [eitjumpstarter.eu/robotwin-secures-1-million-eur/](https://eitjumpstarter.eu/robotwin-secures-1-million-eur/), [cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-m…](https://cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-maji-desitky-milionu/), [therecycler.com/posts/new-leadership-for-y-soft-ventures/](https://therecycler.com/posts/new-leadership-for-y-soft-ventures/)
- `nezavislost_zdroju / jistota` (fáze B, upřesnění fáze A): CzechCrunch 11. 9. 2025 („Letos již hlásili první, tzv. pre-seed, investici…“) odkazuje na dřívější oznámení. The Recycler je zpráva o změně vedení podle sdělení Y Soft a investici zmiňuje jednou větou bez kola, data a částky. `puvod` null tedy neodpovídá u dvou ze tří zpráv. U EIT Jumpstarter (zpráva programu EIT, spoluinvestora) je null obhajitelný. PLAN.md neříká, jaký minimální obsah musí zpráva o transakci mít, proto podle fáze B může být obhajitelná `stredni` i `vysoka`.

### cz-lighthouse-ventures

Lighthouse Ventures · `investori.json` · zařazen · oddíl 30 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

**Podezření**

- `dalsi_investice / nastroj (Merchantee)` (fáze B, oprava fáze A (sedi → sedí s výhradou)): Nordic9 (`zdroj_url`) označuje kolo „pre-seed“, CzechCrunch 9. 6. 2026 (zdroj u Czech Founders VC) „rozšíření … seed investičního kola“ a „bridge round“, Raising.fi „undisclosed funding round“. Lighthouse má `datum_oznameni` 2026-06-03 (Nordic9), Czech Founders VC 2026-06-09. Podmínku 3 to nemění (Ranketta).

**Nedostatečný důkaz**

- `dalsi_investice (Merchantee)` (fáze B): Nordic9 působí jako databáze transakcí bez odkazu na původní zprávu, bod 2 u databáze odkaz vyžaduje. Raising.fi je obecný redakční text. Pro zařazení nerozhoduje (Ranketta, Hermetiq).

### cz-czech-founders-vc

Czech Founders VC · `investori.json` · zařazen · oddíl 31 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

**Podezření**

- `posledni_investice (Merchantee)` (fáze B): Totéž kolo Merchantee vedou dva záznamy různě: tento jako seed (CzechCrunch: prodloužení seed kola, „něco jako bridge round“), Lighthouse jako pre-seed (Nordic9). U bridge kola zdroj nástroj neuvádí a dluh nezmiňuje.
- `nezavislost_zdroju (Merchantee)` (fáze B): `puvod` null, ačkoli CzechCrunch píše „Merchantee oznámilo“. Jediná zpráva o transakci, na jistotu bez vlivu.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kapital[0]` (fáze B): 10 mil. EUR (CzechCrunch 7. 9. 2022) jako `committed_capital` bez fondu. Czech Founders VC je sám fond, obdobný údaj u Reflexu je `fund_size`. Údaj je čtyři roky starý, PLAN.md stáří kapitálu neomezuje.

### cz-depo-ventures

DEPO Ventures · `investori.json` · zařazen · oddíl 32 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

**Podezření**

- `nezavislost_zdroju (Tapaya)` (fáze B, nový nález (fáze A puvod neposuzovala)): Vestbee má `puvod` null, ale píše „Vestbee was told“ a citace Willa Ordea je doslova shodná s TZ na webu DEPO. Na jistotu bez vlivu.

**Nedostatečný důkaz**

- `rozsah_pilotu (sídlo)` (fáze B): Sídlo je CZ v obou výkladech (DEPO VENTURES, s.r.o. je statutárem fondu AF III). Nový Ukraine Fund spravuje DEPO Ventures One SCSp. Že jeho správcem je lucemburská DEPO Ventures Sàrl, je jen z výtahu vyhledávače (businessinfo.cz vrátil HTTP 403).

### cz-inven-capital

Inven Capital · `investori.json` · zařazen · oddíl 33 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

**Podezření**

- `je_investor (Andercore)` (fáze B): Smíšené kolo „Series B round comprising equity and debt“. Dluh TZ nepřímo připisuje Commerzbank a KfW, nástroj Inven výslovně neuvádí. Podmínku 3 nese i Wint (Series D, bez zmínky o dluhu).

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kapital[0]` (fáze B): „over EUR 500 million“ (TZ ČEZ 8. 2. 2023) je uloženo jako přesných 500 000 000, dolní mez je jen v poznámce. Zdroj sám zaměňuje AUM a fund size.

### cz-credo-ventures

Credo Ventures · `investori.json` · zařazen · oddíl 34 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

**Podezření**

- `nezavislost_zdroju (Supernova)` (fáze B): Tech.eu má `puvod` null, text s citací CEO vypadá na převzatou TZ. Jediná zpráva, na jistotu bez vlivu.

### cz-cs-seed-starter

ČS Seed Starter · `investori.json` · zařazen · oddíl 35 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (12 sedi).

**Podezření**

- `nezavislost_zdroju (Definic)` (fáze B): CzechCrunch má `puvod` null, citace Miloty a Sovy jsou ve stylu TZ. Jediná zpráva, na jistotu bez vlivu.

### cz-jt-ventures

J&T Ventures · `investori.json` · zařazen · oddíl 36 v [pruvodce.md](pruvodce.md)

Fáze A: 14 řádků (14 sedi).

**Podezření**

- `nezavislost_zdroju (Choice)` (fáze B): Tech.eu má `puvod` null, text obsahuje citaci CEO. Jediná zpráva, na jistotu bez vlivu.

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kapital[0]` (fáze B, oprava vysvětlení fáze A (závěr sedi beze změny)): „€120M / Výše aktiv“ (web, © 2024) je bez data, `plati_k` null. Fáze A tvrdila, že poznámka uvádí nejistotu data i druhu. Poznámka uvádí jen nejistotu data.

### cz-rockaway-ventures

Rockaway Ventures · `investori.json` · zařazen · oddíl 37 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `kapital[0]` (fáze B): „closed its second fund at nearly €55 million“ je uloženo jako přesných 55 000 000 (ve skutečnosti horní mez), výhrada je jen v poznámce.

### cz-borovicka-capital

Borovicka Capital · `investori.json` · zařazen · oddíl 38 v [pruvodce.md](pruvodce.md)

Fáze A: 11 řádků (11 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-fazole-ventures

Fazole Ventures · `investori.json` · zařazen · oddíl 39 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (12 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-miton

Miton · `investori.json` · zařazen · oddíl 40 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-presto-ventures

Presto Ventures · `investori.json` · zařazen · oddíl 41 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-purposetech

PurposeTech · `investori.json` · zařazen · oddíl 42 v [pruvodce.md](pruvodce.md)

Fáze A: 12 řádků (12 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-tilia-impact-ventures

Tilia Impact Ventures · `investori.json` · zařazen · oddíl 43 v [pruvodce.md](pruvodce.md)

Fáze A: 13 řádků (13 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-arx-equity-partners

ARX Equity Partners · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 44 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Omezení kontroly (co druhý agent neověřil)**

- `duvod` (fáze A): Zmínka o HLB PROXY (30. 1. 2026) nemá v `zdroj_url` zdroj, neověřeno. Podle fáze A bez vlivu na závěr. Stránka Medicofit odkazuje na novější investici Direct4me (16. 3. 2026).

### cz-mam-private-equity-fund

MAM Private Equity Fund SICAV a.s. · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 45 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Omezení kontroly (co druhý agent neověřil)**

- `duvod` (fáze A): Dvě tiskové zprávy v PDF (8. 9. 2026, 24. 9. 2025) se nepodařilo převést na text. Data ověřena jen z názvů souborů, text TZ z webu mam-equity.cz.

### cz-everita-capital

EVERITA Capital · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 46 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

**Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)**

- `—` (fáze B): Fáze B se EVERITA zabývala jen kvůli otázce, zda je nástupcem Espiry (viz cz-espira-investments). K záznamu EVERITA nález nemá.

### cz-bd-partners

BD Partners · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 47 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-central-europe-industry-partners

Central Europe Industry Partners · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 48 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-emma-capital

EMMA Capital · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 49 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-genesis-capital

Genesis Capital · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 50 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-lion-beat-capital

Lion Beat Capital · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 51 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-qq-capital

QQ Capital · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 52 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-skylimit-investments

SkyLimit Investments · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 53 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-stratum-partners

Stratum Partners · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 54 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-tcf-capital

TCF Capital · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 55 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-thein

Thein · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 56 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.

### cz-versute-investments

Versute Investments · `vyrazeni.csv` · vyřazen, kategorie `mimo_rozsah_pilotu` · oddíl 57 v [pruvodce.md](pruvodce.md)

Fáze A: 2 řádků (2 sedi).

Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu nevyjádřila. Bez nálezu neznamená ověřeno.
