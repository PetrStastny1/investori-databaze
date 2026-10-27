# Databáze investorů

Praktická úloha ve výběrovém řízení na pozici Junior AI Developer ve společnosti Clientelo. Zadání: pomocí AI agentů sestavit spolehlivou databázi investorů, kteří vkládají vlastní nebo svěřený kapitál do soukromých firem za podíl, ověřit postup na pilotu a změřit jeho přesnost, odhadnout počet investorů ve světě a náklady na zpracování celého světa.

Pilot jsem udělal pro VC a CVC se sídlem v ČR. Pravidla, schéma záznamu a metodika měření jsou v [PLAN.md](PLAN.md), odhad nákladů v [NAKLADY.md](NAKLADY.md).

## Výsledek

Ze 4 zdrojů jsem sestavil 57 kandidátů. Po sloučení Nation1 do N1 Ventures zbylo 56 subjektů.

| | původní výstup agenta | opravená verze (krok 8) |
|---|---|---|
| zařazení (VC/CVC se sídlem v ČR) | 27 | **23** |
| vyřazení, z toho `mimo_rozsah_pilotu` / `neni_investor` | 17 (15 / 2) | **19** (17 / 2) |
| nevyřešení (k ručnímu rozhodnutí) | 11 | **13** |
| hraniční (venture debt) | 1 | **1** |
| celkem | 56 | 56 |

- **23 zařazených neznamená 23 plně ověřených.** 7 z nich nebylo v kontrolním vzorku a ručně je nikdo nekontroloval. U zbylých 16 je stav v [stav_kontroly.csv](data/opraveno/stav_kontroly.csv): 4 s opravou poslední investice, 2 s polem, které nešlo ověřit, a 10 se všemi hodnocenými poli `ano`. I mezi nimi mají některé záznamy výhrady, například Credo, Rockaway, StartupYard nebo i&i Prague (nástroj doložený nepřímo).
- **Mimo pilot není totéž co neinvestor.** `mimo_rozsah_pilotu` (17) znamená, že agent subjekt vyhodnotil jako investora jiného typu (PE, family office…) nebo se sídlem mimo ČR. Ručně to bylo potvrzené jen u N1 a i&i Biotech. `neni_investor` (Espira, McWin) znamená jen to, že investice za posledních 24 měsíců není veřejně doložená. Kontrolní agent upozornil, že to samo nedokazuje, že nejde o investora ([cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md), oddíl „Espira a McWin“).
- Čtyři přesuny z opravené verze: N1 a i&i Biotech jsem přesunul mimo pilot (správce fondu je v Lucembursku). Tensor (sídlo správce) a Presto (přiřazení investic) jsem přesunul mezi nevyřešené. U Presta chybí důkaz, ale nic nedokládá, že nejde o investora. i&i Prague byla v kroku 8 také přesunutá mezi nevyřešené. V kroku 9 jsem hodnocení opravil podle již uloženého výpisu z rejstříku a vrátil ji mezi zařazené (viz [Chyby a opravy](#chyby-a-opravy)). Původní stav byl 22 zařazených a 14 nevyřešených.

Odkazy:

| co | kde |
|---|---|
| plán, pravidla, schéma | [PLAN.md](PLAN.md) |
| kandidáti | [data/kandidati.csv](data/kandidati.csv) |
| původní výstup agenta (beze změn, na něm se měřilo) | [data/vystup_agenta/](data/vystup_agenta/) |
| opravená verze a přehled změn | [data/opraveno/](data/opraveno/), [ZMENY.md](data/opraveno/ZMENY.md) |
| stav kontroly každého id | [data/opraveno/stav_kontroly.csv](data/opraveno/stav_kontroly.csv) |
| ruční hodnocení | [data/hodnoceni.csv](data/hodnoceni.csv) |
| vzorek kontroly | [data/vzorek_kontroly.csv](data/vzorek_kontroly.csv) |
| měření | [data/mereni_vzorku.md](data/mereni_vzorku.md) |
| náklady | [NAKLADY.md](NAKLADY.md) |
| exporty konverzací a podklady | [ai-log/](ai-log/) |

## Pravidla a zdroje

Zkrácená verze, plné znění je v [PLAN.md](PLAN.md), body 2–4.

- **Rozsah pilotu:** VC nebo CVC, jehož investiční firma (správce, značka) sídlí v ČR. Tento rozsah jsem zvolil já, zadání uvádí VC fondy v jedné zemi jen jako příklad. Skutečného investora jiného typu nebo se sídlem jinde vedu jako `mimo_rozsah_pilotu`, ne jako neinvestora.
- **Sídlo správce:** při ruční kontrole jsem rozhodl, že rozhoduje sídlo správce (GP/AIFM), ne kancelář nebo tým. Původní text pravidla tento případ neřešil (viz [Chyby a opravy](#chyby-a-opravy)).
- **Doložená investice:** aspoň jedna zpráva o konkrétní transakci za posledních 24 měsíců k referenčnímu datu 26. 10. 2026. Portfolio na webu ani zápis společníka v rejstříku samy nestačí. Datum investice a datum oznámení se zapisují zvlášť a filtr pracuje s oznámením, když datum investice zdroj neuvádí.
- **Nástroj:** podíl nebo konvertibilní nástroj. Účast v pre-seed, seed nebo series kole je přijatý pracovní předpoklad, ne doložený nástroj. Záznam opřený jen o něj má jistotu investice nejvýš `stredni`. Jak často je předpoklad chybný, změřené není.
- **Aktivita:** `aktivni` (investice do 12 měsíců) a `investice_dolozena_12_24_mesicu` je moje vlastní pracovní definice. Popisuje veřejnou stopu, ne skutečnou aktivitu.
- **Kapitál:** AUM, upsaný kapitál a velikost fondu se nezaměňují ani nesčítají. Ukládá se částka v původní měně, datum platnosti a druh ukazatele.
- **Chybějící údaje:** zůstávají `null`, nic se neodhaduje. Údaj bez URL se nevyplňuje. Rozporné nebo nedostatečné důkazy o typu, nástroji, sídle nebo přiřazení investice vedou do `nevyresene.csv`.

### Zdroje kandidátů

Staženo 26. 10. 2026. Kandidát může být ve více zdrojích (ve dvou a více je 20, v jednom 37).

| zdroj | kandidátů |
|---|---|
| [CVCA, řádní členové](https://cvca.cz/en/category/full-members/) | 19 |
| [CEE Funding Map](https://www.pampam.city/funds-poland-BJpHbykKoXoBaILayYBs) | 38 |
| [funding.tech.eu](https://funding.tech.eu/api-docs), kola českých firem 2025–2026 (60 kol) | 26 |
| [Dealroom, veřejný manifest](https://dealroom.co/investors/manifest.json) | 1 |

Omezení sběru: u 8 organizací z funding.tech.eu se sídlo nepodařilo doložit. Vedu je jako nevyřešené (`nevyreseno_sidlo` v [opravy_sberu.csv](ai-log/01-kandidati/opravy_sberu.csv)), kandidátů tak mohlo být až 65. Aplikace Dealroomu vracela HTTP 403. Dataset funding.tech.eu pokrývá jen 60 kol. Ověření sídel a výňatky ze zdrojů jsou v [ai-log/01-kandidati/](ai-log/01-kandidati/).

**Nástroje:** Claude Code (Claude Opus 5.5) s WebSearch a WebFetch, veřejné API [ARES](https://ares.gov.cz/) pro identitu a IČO a veřejné bezklíčové API funding.tech.eu. Skripty jsou v Pythonu jen se standardní knihovnou.

### Data funding.tech.eu: licence a atribuce

Podmínky jsem ověřil 26. 10. 2026 na [funding.tech.eu/for-ai](https://funding.tech.eu/for-ai), [api-docs](https://funding.tech.eu/api-docs) a v [llms.txt](https://funding.tech.eu/llms.txt). Stránka /terms vracela HTTP 429, nečetl jsem ji.

- **Zdroj:** „Tech.eu Funding Explorer“, https://funding.tech.eu/api-docs. Použité API: `https://funding.tech.eu/api/v1` (`/rounds` a `/investors/{name}`), bezklíčové, pouze pro čtení, limit 120 požadavků za 60 s, 600 za hodinu a 2 000 denně na IP. Ve sběru šlo zhruba o 120 požadavků.
- **Licence dat:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- **Úpravy:** [fundingtecheu_kola_cz_2025_2026.json](ai-log/01-kandidati/zdroje/fundingtecheu_kola_cz_2025_2026.json) je nezměněná odpověď `/api/v1/rounds` (Czech Republic, 2025-01-01 až 2026-12-31), jen spojená ze stránek. [fundingtecheu_investori.json](ai-log/01-kandidati/zdroje/fundingtecheu_investori.json) je zkrácený výtah z `/api/v1/investors/{name}`. Z jmen investorů jsem odvodil seznam kandidátů. Částky ani data jsem neměnil a do `kandidati.csv` jsem je nepřebíral. U kandidátů z tohoto zdroje je v `zdroj_url` URL záznamu v API.
- **Použití API:** původní pokyn pro sběr zakazoval po nedostupnosti webu použít náhradní nástroj. Použití API ho tedy nedodrželo. Schválil jsem ho dodatečně, až po dokončení sběru.

## Měření

Podrobně v [data/mereni_vzorku.md](data/mereni_vzorku.md) (generuje [scripts/mereni.py](scripts/mereni.py)).

**Vzorek.** Ručně (s asistencí AI, viz [Ruční kontrola – kdo hodnotil](#ruční-kontrola--kdo-hodnotil)) jsem hodnotil náhodný výběr 20 z 27 původně zařazených, deset polí na firmu. Výběr dělá `random.Random(20261027).sample(sorted(ids), 20)` ve [scripts/vyber_vzorku.py](scripts/vyber_vzorku.py), výsledek je v [data/vzorek_kontroly.csv](data/vzorek_kontroly.csv). Skript i seznam vznikly mimo Claude Code. Do repa přišly až v commitu 35583d9, spolu s rozpracovaným hodnocením. Agent v něm opravil jen cestu k souboru a načítání a ověřil, že ze seedu vychází tentýž seznam ([05-rucni-kontrola-ulozeni.txt](ai-log/05-rucni-kontrola-ulozeni.txt), úsek „its output matches data/vzorek_kontroly.csv byte for byte“). Výběr je tedy reprodukovatelný ze seedu. Kdy losování proběhlo vzhledem k začátku hodnocení, ale log nedokládá.

**Proč vzorek a asistence AI.**

- Plán počítal s ruční kontrolou všech záznamů. Kvůli termínu odevzdání (30. 10.) a rozsahu práce jsem kontrolu zúžil na náhodný vzorek 20 z 27 zařazených. Vzorek šlo zkontrolovat pořádně a výsledek má změřitelnou nejistotu (Wilsonův interval).
- Většina zdrojů je anglicky nebo ukrajinsky, proto jsem při vyhledávání a překladu použil AI. Verdikty jsem schvaloval a sporné výklady rozhodoval já.
- Zadavatele jsem se zeptal, jestli je kontrola s asistencí AI přijatelná. Kvůli termínu jsem na odpověď nečekal a postup jsem místo toho podrobně zdokumentoval, aby ho šlo posoudit.
- Podíl AI a můj jde rozlišit: každý hodnocený řádek v `hodnoceni.csv` má ve sloupci `hodnotil` označení. Stav před přečtením nálezů kontrolního agenta je uložený zvlášť a v něm je u každého řádku uvedeno, jestli verdikt navrhl Claude, nebo ChatGPT. Srovnání přínosu kontrolního agenta je v [mereni_vzorku.md](data/mereni_vzorku.md), oddíl 5.

**Správnost zařazení** (jednotka = firma, 95% Wilsonův interval):

| | výsledek |
|---|---|
| správně / chybně / neověřeno | 16 / 2 / 2 |
| přesnost na ověřitelných | 16/18 = **88,9 %** (67,2–96,9 %) |
| konzervativně, neověřené jako chyba | 16/20 = **80,0 %** (58,4–91,9 %) |

Obě chybná zařazení (N1, i&i Biotech) jsou **změny výkladu metodiky**, ne chyby agenta. Agent použil sídlo značky a týmu, já jsem při ruční kontrole rozhodl podle sídla správce. Bez nich je dolní mez 16/18 = 88,9 % (67,2–96,9 %). Neověřené jsou Tensor (sídlo správce) a Presto (přiřazení investic). Původní stav před opravou hodnocení i&i Prague v kroku 9: 15 / 2 / 3, tedy 15/17 = 88,2 % a 15/20 = 75,0 %.

**Správnost vyplněných polí** (jednotka = pole firmy, 20 firem × 10 polí):

| pole | přesnost ano/(ano+ne) | dolní mez s `nelze_overit` |
|---|---|---|
| **celkem** | 157/164 = **95,7 %** (91,5–97,9 %) | 157/175 = 89,7 % (84,3–93,4 %) |
| posledni_investice (nejslabší) | 15/19 = 78,9 % (56,7–91,5 %) | 15/20 = 75,0 % (53,1–88,8 %) |
| je_investor | 19/19 = 100 % (83,2–100 %) | 19/20 = 95,0 % (76,4–99,1 %) |
| rozsah_pilotu | 17/19 = 89,5 % (68,6–97,1 %) | 17/20 = 85,0 % (64,0–94,8 %) |
| nezavislost_zdroju | 14/14 = 100 % (78,5–100 %) | 14/20 = 70,0 % (48,1–85,5 %) |
| ostatní pole | bez `ne` | viz mereni_vzorku.md |

- `ne` je 7: 4 chyby výstupu (vždy přehlédnutá novější poslední investice: Look AI, Purple, Reflex, ZAKA), 2 změny výkladu metodiky (rozsah N1 a i&i Biotech) a 1 omezení schématu (dva intervaly ticketu i&i Biotech). Dalších 11 polí nešlo ověřit (`nelze_overit`), nejvíc u nezávislosti zdrojů (6). Když se počítají jen chyby výstupu, vychází 157/161 = 97,5 % (93,8–99,0 %). Původní stav před opravou v kroku 9 byl 156 `ano` a 12 `nelze_overit` (156/163, dolní mez 156/175).
- Úplnost: sektory vyplněné u 16/20 firem, ticket 11/20 (1 potvrzené chybění, N1), kapitál 8/20.
- Souhrnný interval přes pole je optimistický, protože pole jedné firmy nejsou nezávislá.
- **Sloučení Nation1 → N1** jsem hodnotil zvlášť (1 případ, správně) a do přesnosti polí nevstupuje.

**Co měření neříká.**

- Neříká, že databáze je ze 100 % správná.
- Recall ani úplnost českého trhu změřené nejsou. Vyřazené, hraniční a nevyřešené kandidáty nikdo ručně nekontroloval a orientační srovnání se seznamy neproběhlo.
- Měření platí pro původní výstup agenta. Opravená verze vychází ze stejného hodnocení a nové nezávislé hodnocení nemá.
- Hodnocení vzniklo s asistencí AI a zčásti po přečtení nálezů kontrolního agenta. Není to nezávislý referenční standard.

## Náklady

Podrobně v [NAKLADY.md](NAKLADY.md).

- **Pilot (kroky 0–6), změřeno z logů Claude Code:** 193,3 mil. tokenů v 1 879 požadavcích, 96 % tvoří čtení z cache. **V přepočtu na ceny API zhruba 108 USD.** Pilot jsem ale nezaplatil přes API, běžel v rámci předplatného Claude, takže jde o přepočet, ne o zaplacenou částku. Samotná produkční část (sběr, obohacení a kontrola druhým agentem) stojí 1,67 USD na kandidáta a 3,46 USD na zařazený záznam. To není rozpočítání celých 108 USD, plán, zkušební dávka, vývoj skriptů a měření v tom nejsou.
- **Nezachycená spotřeba** v součtu chybí a není nulová: tokeny pomocného modelu WebFetch, výsledky WebSearch, asistence Claude a ChatGPT v chatu, webové požadavky ve sběru a kroky 7–9.
- **Svět je scénář, ne změřený počet investorů:** 5 600–11 000 zařazených podle [PLAN.md](PLAN.md), bod 8.2. Poměr kandidátů k zařazeným (56/27), čas člověka 10–15 min na firmu, sazba 25 USD/h, násobky pro jazyky a rejstříky a podíl nevyřešených jsou modelové předpoklady.

| svět, USD | nízká | střední | vysoká |
|---|---|---|---|
| sestavení s kontrolním vzorkem (AI + člověk) | 33 696 | 73 901 | 151 418 |
| sestavení s plnou ruční kontrolou | 55 029 | 125 450 | 253 628 |
| roční aktualizace poslední investice | 5 415 | 18 370 | 54 570 |

Většinu lidských hodin tvoří ruční rozhodnutí nevyřešených kandidátů. Je to zároveň nejméně podložená položka, protože v pilotu je nikdo ručně nerozhodoval.

## Jak jsem pracoval s AI

První návrh plánu vznikl v chatu. Implementaci, sběr a zpracování jsem dělal v Claude Code. Každý krok měl vlastní session, exporty jsou v [ai-log/](ai-log/). Krok 5 je jedna session exportovaná dvakrát: [05-priprava.txt](ai-log/05-priprava.txt) obsahuje přípravu, [05-rucni-kontrola-ulozeni.txt](ai-log/05-rucni-kontrola-ulozeni.txt) celou session včetně uložení hodnocení. Pomocní agenti (3 ve sběru, 31 v obohacení, 13 v kontrole zdrojů) jsou v exportech zachycení jen svými závěrečnými zprávami hlavnímu agentovi. ChatGPT a Claude v chatu mi pomáhali s recenzí plánu, vyhledáním a překladem zdrojů a s návrhy verdiktů ruční kontroly.

Commity probíhaly podle exportů ve třech režimech:

- **Schválení po vypsání:** agent výsledek vypsal a commitoval až po mém schválení. Tak běžel krok 0 (diff PLAN.md), úprava pravidel po zkušební dávce, krok 7 (souhrn spotřeby a variant) a krok 8 (návrh přesunů a oprav).
- **Předem určené kontroly:** v zadání jsem určil kontroly, například očekávané počty, shodný výstup při dvou bězích nebo nezměněný původní výstup. Agent commitoval, jen když všechny prošly, jinak měl zastavit a vypsat rozdíl. Tak běželo uložení ruční kontroly v kroku 5, krok 6 (zastavil na rozdílu 157/156 a commitoval po mém potvrzení) a závěrečné commity kroků 7 a 8.
- **Commit podle zadání bez předchozího schválení:** agent výsledek sám zkontroloval, commitoval a pak vypsal souhrn. Tak běžel krok 1, výstup zkušební dávky, dávky obohacení (s ověřením shody archivu zkušební dávky s commitem f4cd74d), kroky 3 a 4 a příprava podkladů v kroku 5. Výstup jsem kontroloval až po commitu a opravy šly do dalších commitů.

| krok, export | co jsem agentovi zadal | jak jsem výstup kontroloval |
|---|---|---|
| 0 [plán a založení](ai-log/00-plan-a-zalozeni.txt) | opravit PLAN.md podle externí recenze v ChatGPT a mé kontroly (kapitál, aktivita, důkazy, měření, odhad rozsahu, druhý agent), založit repo a ověřit git identitu | dvě kola diffu PLAN.md před schválením |
| 1 [kandidáti](ai-log/01-kandidati.txt) | jen veřejné zdroje, nedostupnost zaznamenat a neobcházet, stabilní id, deduplikace bez zařazování, počet nepřizpůsobovat hypotéze | souhrn zdrojů a duplicit, dodatečné schválení API, ověření licence, 8 nevyřešených sídel, pravidla pilotu |
| 2 [zkušební dávka](ai-log/02-zkusebni-davka.txt) | 5 kandidátů podle schématu, pak úprava pravidel typu a nástroje | diff pravidel a dopad na 5 kandidátů, výstup dávky archivovaný beze změn |
| 2 [obohacení](ai-log/02-obohaceni.txt) | všech 57 v dávkách po 10, pravidla neměnit, nejasnosti zapisovat, surové odpovědi ARES a funding.tech.eu ukládat, měřit čas a požadavky | souhrn a commit po každé dávce, formální kontrola skriptem, [nejasnosti.md](ai-log/02-obohaceni/nejasnosti.md) |
| 3 [automatická kontrola](ai-log/03-kontrola.txt) | validátor struktury, pokrytí id, okna, nástroje a jistoty, upozornění na zdroje stažené bez ověření TLS, testy | testy na umělých chybách, zpráva [automaticka_kontrola.md](ai-log/03-kontrola/automaticka_kontrola.md) |
| 4 [kontrola zdrojů](ai-log/04-kontrola-zdroju.txt) | druhý agent (stejný model, nová konverzace): fáze A naslepo bez README a historie, fáze B cílené otázky | závěry po polích v [slepa_kontrola.csv](ai-log/04-kontrola-zdroju/slepa_kontrola.csv), oprava vlastních chyb fáze A v [cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md) |
| 5 [ruční kontrola](ai-log/05-rucni-kontrola-ulozeni.txt) | připravit průvodce a předvyplněné hodnocení bez verdiktů, nálezy AI oddělit, pak uložit hodnocení z mé kontroly | počty verdiktů a změn proti mým očekávaným hodnotám, při rozdílu bez commitu |
| 6 [měření](ai-log/06-mereni.txt) | PLAN.md sladit se skutečným postupem, deterministický mereni.py, oddělit tři druhy `ne` | kontrolní počty dodané v zadání, následně porovnané s výstupem skriptu; rozdíl 157/156 dohledán před commitem |
| 7 [náklady](ai-log/07-naklady.txt) | spotřeba jen z polí usage v lokálních logech, ceník z oficiálního zdroje, předpoklady výslovně označit | souhrn před commitem, druhé kolo úprav (sazba, rozsah aktualizace, význam vzorku) |
| 8 [opravená verze](ai-log/08-opraveno.txt) | oprav.py jen podle dokončeného hodnocení, přesuny a opravy s odkazem na řádek hodnocení | návrh přesunů před provedením, zamítnuté nové pole v investori.json, validace v dočasné kopii |

### Ruční kontrola – kdo hodnotil

„Petr Šťastný (asistence AI)“: zdroje vyhledal, přeložil a verdikt navrhl Claude, u části polí ChatGPT. Každý verdikt jsem schválil já a sporné výkladové otázky (sídlo správce, přiřazení přes fondy, chybějící údaje) jsem rozhodl sám. Štítek znamená schválení navržených verdiktů, ne to, že jsem osobně otevřel všechny zdroje. U všech polí jsem je neotevíral.

Stav před přečtením nálezů kontrolního agenta je uložen zvlášť v [hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv) (commit 35583d9). V něm je ještě rozlišeno, kdo verdikt navrhl: 194 řádků Claude, 7 ChatGPT. Změny po přečtení nálezů mají v poznámce „Změna po přečtení nálezů AI“. Stav před opravou hodnocení i&i Prague v kroku 9 je uložen v [hodnoceni_pred_opravou_ii_prague.csv](ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv). Oprava je v měření vykázaná zvlášť ([mereni_vzorku.md](data/mereni_vzorku.md), oddíl 5.5).

Kontrola proto není nezávislý referenční standard. Druhý agent byl stejný model v jiné konverzaci. Firmy vzorku byly vybrané náhodně, ale průvodce kontroly je řadil podle závažnosti nálezů kontrolního agenta. Srovnání jeho přínosu je jen orientační: ze 4 chyb výstupu našla ruční kontrola 3 (Purple, Reflex, ZAKA) až po přečtení jeho nálezů. Po přečtení se také 6 verdiktů změnilo z `ano` na `nelze_overit` ([mereni_vzorku.md](data/mereni_vzorku.md), oddíl 5.4).

## Chyby a opravy

Uvádím jen chyby doložené v repu a logu. Úsek v uvozovkách jde v uvedeném souboru vyhledat doslova. Druh chyby:

- **pravidla:** chyba nebo mezera v mých pravidlech,
- **aplikace:** chybné použití existujícího pravidla,
- **schéma:** schéma neumí hodnotu zapsat,
- **neurčeno:** příčinu z logu nejde zjistit.

### Návrh a pravidla

| chyba | druh | kdo našel | řešení | doklad |
|---|---|---|---|---|
| Plán z chatu definoval kapitál jako součet upsaného kapitálu nebo AUM, takže zaměňoval a sčítal různé ukazatele. | pravidla | externí recenze v ChatGPT | v kroku 0 nahrazeno seznamem `kapital` s druhem ukazatele a datem, bez sčítání | [00-plan-a-zalozeni.txt](ai-log/00-plan-a-zalozeni.txt): „Celkový investiční kapitál** = součet upsaného kapitálu“ |
| Hranici aktivity 12 měsíců plán připisoval CEE Funding Map, ta ale měří dvě investice za rok. | pravidla | recenze v ChatGPT | v kroku 0 označeno jako moje vlastní pracovní definice, status přejmenován | tamtéž: „Hranici 12 měsíců přebírám od CEE“ |
| Odhad pro ČR byl odvozený z počtu investičních kol, částky se převáděly na EUR. | pravidla | recenze v ChatGPT | v kroku 0 hypotéza bez odvození, původní měna | tamtéž: „Odhad vychází z počtu kol“ |
| Pravidlo „investiční firma (správce, značka) sídlí v ČR“ neurčuje, co platí, když správce sídlí v cizině a tým v Praze. | pravidla | kontrolní agent (fáze B), rozhodnuto při ruční kontrole | rozhodnuto podle sídla správce: N1 a i&i Biotech mimo pilot, Tensor nevyřešený. Text pravidla v PLAN.md upřesněný není a KAYA neposouzená, **nenapraveno, uvedeno jako omezení** | [cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md): „PLAN.md neříká, co platí, když správce (GP/AIFM) sídlí jinde než značka a tým“ |

### Sběr a obohacení (agent)

| chyba | druh | kdo našel | řešení | doklad |
|---|---|---|---|---|
| Ve sběru agent zařadil 8 organizací s nedoloženým sídlem mezi výskyty mimo rozsah, takže je skrytě vyřadil, přestože nebyly prokazatelně zahraniční. | aplikace | já při kontrole výsledku kroku 1 | vedeny jako nevyřešené v [opravy_sberu.csv](ai-log/01-kandidati/opravy_sberu.csv), původní `mimo_rozsah.csv` beze změny | 01-kandidati.txt: „8 se sídlem nedoloženým“, „Osm subjektů s nedoloženým sídlem zachovej jako nevyřešené“ |
| Ve zkušební dávce agent zařadil BD Partners jako VC, i když se ve zdroji sám označuje jako „joint family office“. | pravidla | agent sám jako nejasnost, rozhodl jsem já | nové pravidlo: typ podle doloženého fungování a vlastního popisu. V měřeném běhu je BD Partners `mimo_rozsah_pilotu` (family office) | [02-zkusebni-davka.txt](ai-log/02-zkusebni-davka.txt): „joint family office, nejsme klasický“ |
| Ve zkušební dávce agent prohlásil všech 5 kandidátů za investory podle podmínek plánu, i když nástroj investice doložený nebyl. | aplikace | agent sám jako nejasnost, rozhodl jsem já | tři úrovně dokladu nástroje (`dolozeno`, `neprima_indicie`, `nezjisteno`) a pravidlo pro `neprima_indicie`. Výstup dávky je archivovaný a neměřil se | tamtéž: „Všech pět kandidátů je investor podle bodů 2 a 3“ |
| Agent ve sběru použil API funding.tech.eu, i když pokyn zakazoval po nedostupnosti webu náhradní nástroj (provedená akce). | aplikace | agent to sám uvedl v souhrnu, rozhodl jsem já | dodatečně schváleno a zapsáno výše | [01-kandidati.txt](ai-log/01-kandidati.txt): „neobcházej ho přes cache, mirror ani jiný nástroj“, „API funding.tech.eu dodatečně schvaluji“ |
| Look AI, Purple, Reflex: agent přehlédl novější doloženou investici. | neurčeno | Look AI ruční kontrola před nálezy AI, Purple a Reflex kontrolní agent (fáze A) | v opravené verzi nová poslední investice, původní přesunutá do `dalsi_investice` | [hodnoceni.csv](data/hodnoceni.csv) ř. 127, 147, 157; [04-kontrola-zdroju.txt](ai-log/04-kontrola-zdroju.txt): „Embodied“, „ArtMaster“ |
| ZAKA: agent FinalDose znal, ale vlastní oznámení investora nepřijal jako zprávu o transakci, přestože ho PLAN.md připouští. | aplikace | kontrolní agent (fáze A) | v opravené verzi FinalDose, stránka v kroku 8 znovu načtena nebyla (viz Omezení) | poznámka záznamu v [vystup_agenta/investori.json](data/vystup_agenta/investori.json): „ty jsem nezávislou zprávou o transakci neověřil“; hodnoceni.csv ř. 48 |
| Presto: agent připsal Prestu investice fondu Tech Horizons (lucemburský správce). Vazba není doložená, ale ani vyvrácená. | neurčeno | ruční kontrola (kontrolní agent pole označil jako sedící) | přesun do `nevyresene.csv` (otázka `investice`) | 02-obohaceni.txt: „investice SatVu a Occam přičítám Presto Ventures“; hodnoceni.csv ř. 293 |
| N1: chybí ticket, který web uvádí („Typical 1st investment $100K–$1M“). | neurčeno | ruční kontrola | zapsáno v ZMENY.md, záznam je mimo pilot | hodnoceni.csv ř. 10 |
| i&i Biotech: dva intervaly ticketu sloučené do jednoho 150 tis.–2 mil. EUR. | schéma | ruční kontrola (návrh verdiktu ChatGPT) | v ZMENY.md oba intervaly, společný interval se nepoužije | 02-obohaceni.txt: „Ticket podle webu je 150 tis. až 2 mil. EUR.“; hodnoceni.csv ř. 41 |

### Postup a bezpečnost

| chyba | provedeno / zamítnuto | kdo našel | řešení | doklad |
|---|---|---|---|---|
| Stažení profilu CVCA (Thein) přes `curl -k`, tedy bez ověření TLS. | provedeno u Theinu, u Tensoru pokus zablokovalo oprávnění | agent sám v souhrnu dávky | automatická kontrola to hlásí jako upozornění. Zdroj se znovu neověřoval a Thein ručně kontrolovaný není, **nenapraveno, uvedeno jako omezení** | 02-obohaceni.txt: „stáhl přes curl -k kvůli chybě certifikátu“, „Curl bez ověření certifikátu zablokovala oprávnění“ |
| Přepsané surové odpovědi ARES: agent dávky 3 znovu stáhl `ares_hledani_iiPrague.json` a `ares_vr_06058485.json` z dávky 2. | provedeno | hlavní agent | git eviduje oba soubory jen v commitu 19ed337, přepsaný obsah byl tedy shodný. Přepsání varianty hledání v dávce 2 agent opravil sám přejmenováním. Jiný agent smazal prázdnou chybovou odpověď funding.tech.eu, ta obnovená není | 02-obohaceni.txt: „Přepsané surové soubory ARES“, „přepsala soubor“, „Odstraněný soubor:“ |
| Pokus obejít ochranu proti botům: curl s jiným User-Agent (krok 2, zdroje CasInvent) a opakované načtení zaka.vc po HTTP 466 (krok 8). | oba zamítnuté klasifikátorem, neproběhly | klasifikátor oprávnění Claude Code | agent pokračoval bez stránek, FinalDose proto znovu načtené není | 02-obohaceni.txt: „zamítl klasifikátor (obcházení ochrany proti botům)“; [08-opraveno.txt](ai-log/08-opraveno.txt): „Bot Check Circumvention“ |

### Kontrola a měření

| chyba | druh | kdo našel | řešení | doklad |
|---|---|---|---|---|
| Kontrolní agent ve fázi A nezachytil lucemburský AIFM u KAYA. Označil také 5 dvojic, které konečné hodnocení nepotvrdilo, a neoznačil Presto ani ticket i&i Biotech. U nástroje i&i Prague měl závěr `sedi`, který oprava hodnocení v kroku 9 potvrdila. | aplikace | sám ve fázi B; srovnání v mereni_vzorku.md | KAYA zůstává zařazená a neposouzená, **nenapraveno, uvedeno jako omezení** | cilene_otazky.md: „U Kaya to první agent ani fáze A nezachytili“ |
| Claude v chatu (asistence ruční kontroly) navrhl `ano` u poslední investice Purple, Reflex a ZAKA a přehlédl novější investice. Schválil jsem to. | aplikace | kontrolní agent, převzato po přečtení jeho nálezů | změna na `ne`, oprava v kroku 8 | [hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv); 05-rucni-kontrola-ulozeni.txt: „Očekávám přesně 9 změn“ |
| Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem, kde agent vedl zdroje s neznámým původem. | aplikace | u Y Soft kontrolní agent, u ostatních pěti Claude v chatu při sjednocení výkladu | změna na `nelze_overit`, `puvod` ani `jistota` se v opravené verzi nemění | tamtéž |
| Kontrolní počty pro krok 6 připravil Claude v chatu a do 157 `ano` započítal i řádek sloučení Nation1 → N1. Pro pole 20 firem bylo tehdy správně 156 (po opravě i&i Prague v kroku 9 je jich 157). | aplikace | agent kroku 6 | potvrdil jsem 156, sloučení se vykazuje zvlášť | [06-mereni.txt](ai-log/06-mereni.txt): „Skript dává 156 ano místo kontrolních 157“ |
| [mereni.txt kontroly zdrojů](ai-log/04-kontrola-zdroju/mereni.txt) uvádí jako „tokeny subagentů“ velikost kontextu posledního volání, ne spotřebu. | aplikace | agent kroku 7 | NAKLADY.md počítá s kumulativní spotřebou z logů. mereni.txt zůstal beze změny, rozdíl je vysvětlený v NAKLADY.md | [07-naklady.txt](ai-log/07-naklady.txt): „nejsou spotřeba, ale“ |
| i&i Prague: kontrola s asistencí AI (Claude v chatu, schváleno mnou) hodnotila `je_investor` jako `nelze_overit` s tím, že rejstřík CasInvent dokládá i&i Prague jen jako akcionáře v roce 2020. Přehlédla údaje z roku 2025 v tomtéž uloženém výpisu. Agentův `dolozeno` měl oporu, i když nepřímou. V kroku 8 kvůli tomu i&i Prague nesprávně skončila mezi nevyřešenými. | aplikace | Claude Code při přípravě README (krok 9) | oprava hodnocení, ne změna pravidel: `je_investor` = `ano` podle konvertibilní zápůjčky z 4. 3. 2025, nabídky 48 akcií třídy C (valná hromada 22. 5. 2025) a zapsaného splaceného zvýšení kapitálu k 30. 5. 2025. Samostatná smlouva o úpisu přímo ověřená není. Přepočítané měření i opravená verze, původní stav uložený zvlášť | [ares_vr_09684221.json](ai-log/02-obohaceni/zdroje/ares_vr_09684221.json): „48 ks Nových akcií“, „Smlouvy o konvertibilní zápůjčce“; hodnoceni.csv ř. 65; [hodnoceni_pred_opravou_ii_prague.csv](ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv) |

## Omezení a nedokončené části

- **Sedm zařazených mimo vzorek** (ČS Seed Starter, Fazole, JIC Ventures, J&T Ventures, KAYA, Lighthouse, Tilia) ručně kontrolovaných není.
- **Vyřazení, hraniční a nevyřešení** z původního výstupu (29 kandidátů) ručně kontrolovaní nejsou. Žádný nevyřešený případ jsem ručně nerozhodl, ani původní 11, ani 2 nové (Tensor, Presto).
- **Sídlo správce:** KAYA má podle kaya.vc/sustainability správce registrovaného jako lucemburský AIFM. Podle pravidla použitého u N1 by patřila mimo pilot, ale posouzená není a zůstává zařazená. Má i známý nález automatické kontroly: `fond` vyplněný u `committed_capital`. U Credo je neověřená role nové správcovské a.s.
- **Nezávislost zdrojů** nešla ověřit u 6 z 20 firem (zdroje s neznámým původem mohou vycházet z jedné tiskové zprávy).
- **Poslední investice** je nejnovější doložená, ne záruka, že novější neexistuje. Byla to nejslabší kategorie polí.
- **ZAKA:** stránku zaka.vc/news se při tvorbě oprav nepodařilo znovu načíst. Oprava na FinalDose vychází z dřívějšího hodnocení s asistencí AI a z kontroly druhým agentem. PerfectBit (tisková zpráva 18. 8. 2026) nikdo neposoudil a zapsaný není.
- **Datum stažení:** zdroje čtené v kroku 8 mají `stazeno` 27. 10. 2026, tedy den po referenčním datu. Pozdější datum stažení samo neznamená, že informace k 26. 10. 2026 neplatila. Automatická kontrola to při referenčním datu 26. 10. hlásí jako nesoulad (podrobnosti v ZMENY.md).
- **Ostatní:** Thein stažený bez ověření TLS. Pracovní předpoklad u nástroje (účast v seed kole) změřený není. Prvních 5 kandidátů ovlivnilo úpravu pravidel, takže běh není test na neviděných datech. Recall a úplnost trhu změřené nejsou. Globální počty i náklady jsou scénáře.

## Spuštění

Python 3 jen se standardní knihovnou, spouští se z kořene repa. Všechny skripty kromě `--over-url` běží bez sítě a jsou deterministické. Skripty v tabulce **přepisují svůj výstup v repu**. Při stejných vstupech vznikne stejný obsah, výjimky jsou uvedené.

| účel | příkaz | přepisuje |
|---|---|---|
| seznam kandidátů | `python3 scripts/sestav_kandidaty.py` | `data/kandidati.csv`, `ai-log/01-kandidati/mimo_rozsah.csv` |
| výběr vzorku | `python3 scripts/vyber_vzorku.py` | `data/vzorek_kontroly.csv` |
| kontrola dat bez sítě | `python3 scripts/zkontroluj_data.py --vystup /tmp/kontrola.md` | nic (s `--vystup` mimo repo) |
| kontrola dat včetně URL | `python3 scripts/zkontroluj_data.py --over-url` | `ai-log/03-kontrola/automaticka_kontrola.md` |
| testy validátoru | `python3 -m unittest scripts/test_zkontroluj_data.py` | nic |
| měření | `python3 scripts/mereni.py` | `data/mereni_vzorku.md` |
| spotřeba z logů | `python3 scripts/spotreba_z_logu.py` | `ai-log/07-naklady/spotreba.csv` |
| náklady | `python3 scripts/naklady.py` | `ai-log/07-naklady/vypocet.md` |
| opravená verze | `python3 scripts/oprav.py` | soubory v `data/opraveno/` |

- **zkontroluj_data.py:** uložená zpráva vznikla s `--over-url` (354 URL). Běh bez tohoto přepínače bez `--vystup` ji přepíše verzí bez kontroly URL. Výsledek kontroly URL se mění s časem a stavem webů. Další parametry jsou `--datum` (referenční datum, výchozí 2026-10-26) a `--koren`. Skript čte jen `data/vystup_agenta/`. Postup kontroly opravené verze v dočasném kořeni popisuje [ZMENY.md](data/opraveno/ZMENY.md). Návratový kód 1 znamená chybu struktury.
- **spotreba_z_logu.py** potřebuje původní lokální logy Claude Code v `~/.claude/projects/`, jinde nepůjde zopakovat. Skript skončí chybou, když v adresáři logů projektu je session, kterou jeho tabulka `SESSIONY` nezná. To dnes platí pro session kroku 8 a pozdější, `spotreba.csv` se pak nepřepíše.
- **naklady.py** čte jen uložený [spotreba.csv](ai-log/07-naklady/spotreba.csv), takže výpočet nákladů funguje i bez logů.

## Struktura repa

| cesta | obsah |
|---|---|
| `PLAN.md`, `NAKLADY.md`, `README.md`, `LICENSE` | plán, náklady, tento přehled, licence |
| `data/kandidati.csv` | 57 kandidátů |
| `data/vystup_agenta/` | původní výstup agenta: `investori.json`, `vyrazeni.csv`, `hranicni.csv`, `nevyresene.csv` |
| `data/hodnoceni.csv`, `data/vzorek_kontroly.csv` | ruční hodnocení, vzorek 20 firem |
| `data/mereni_vzorku.md` | výsledky měření |
| `data/opraveno/` | opravená verze, `stav_kontroly.csv`, `ZMENY.md` |
| `scripts/` | sběr, výběr vzorku, validátor a testy, měření, spotřeba, náklady, opravy |
| `ai-log/00-…08-*.txt` | exporty session kroků 0–8 |
| `ai-log/01-kandidati/` | výňatky zdrojů sběru, ověření sídel, opravy sběru, sběrné skripty |
| `ai-log/02-zkusebni-davka/` | archiv zkušební dávky, měření, surové odpovědi |
| `ai-log/02-obohaceni/` | mapování 57 id, duplicity, nejasnosti, měření, zadání pomocného agenta, surové odpovědi ARES a funding.tech.eu |
| `ai-log/03-kontrola/` | zpráva automatické kontroly |
| `ai-log/04-kontrola-zdroju/` | slepá kontrola, cílené otázky, měření, log požadavků |
| `ai-log/05-rucni-kontrola/` | průvodce, nálezy AI, stav hodnocení před nálezy, skript přípravy |
| `ai-log/07-naklady/` | agregovaná spotřeba a výpočet nákladů |
| `ai-log/09-readme/` | stav hodnocení před opravou i&i Prague v kroku 9 |

## Licence

Na autorskou práci v repozitáři (plán, kód, dokumentace, výběr a uspořádání dat) se vztahuje [LICENSE](LICENSE): prohlížení je dovolené jen pro hodnocení ve výběrovém řízení, jiné použití jen s mým písemným souhlasem. Data z veřejných zdrojů se řídí podmínkami svých vlastníků. Data z funding.tech.eu jsou pod CC BY 4.0, atribuci uvádím [výše](#data-fundingtecheu-licence-a-atribuce).
