# Rozhodnutí o možných duplicitách (krok 2)

Pravidlo: jedna investiční firma (správce, značka) = jeden záznam (PLAN.md bod 3). Mapování všech 57 vstupních id na výsledné id je v `mapovani_id.csv`.

## cz-fond-nase-cesko / cz-jt-ventures

**Rozhodnutí:** různé investiční firmy, neslučovat. J&T Ventures v této dávce nezpracováno.

**Důvod:** Shodná adresa Sokolovská 700/113a, Praha 8 je sídlo skupiny J&T (budova J&T Banky), kde sídlí i správci a desítky fondů skupiny. Nejde o jeden investiční tým a značku a ani jeden není fondem spravovaným druhým:

- Fond Naše Česko = „Naše ČESKO otevřený podílový fond“ (IČO 75164086, vznik 2023-03-31), správce J&T INVESTIČNÍ SPOLEČNOST, a.s. (IČO 47672684, představenstvo Pařízek, Martinec, Ochman, Sadloň, Tomis), portfolio manažer Martin Cakl, multi-asset strategie (PE, VC, nemovitosti, burzovní akcie). Zdroje: https://www.nase-cesko.cz/ , https://cc.cz/blba-nalada-neni-na-miste-cesko-je-na-tom-lepe-nez-se-zda-muzeme-byt-investicni-perla-zni-z-jt/
- J&T Ventures = samostatná VC značka (https://www.jtventures.cz/, „Podporujeme CEE & SEE foundery s globální ambicí“); její fond J&T Ventures CG SICAV a.s. (IČO 08220867) má jako statutární orgán AMISTA investiční společnost, a.s. (IČO 27437558), ne J&T Investiční společnost. Web J&T Ventures Fond Naše Česko ani Martina Cakla nezmiňuje.
- V kole ValkaAI (únor 2026) vystupují oba jako samostatní investoři: „od tuzemských fondů J&T Ventures, Tensor Ventures, BD Partners“ a „Fondu Naše Česko J&T Investiční společnosti“ (https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/); E15 je uvádí odděleně (https://www.e15.cz/byznys/startupy/konkurence-pro-zarubu-a-bosaka-startup-vlastimila-venclika-ziskal-stovky-milionu-a-prichazi-s-ai-komentatory-1431016).

**Stažené soubory ARES** (ai-log/02-obohaceni/zdroje/): ares_hledani_Nase_Cesko.json, ares_vr_75164086.json (NENALEZENO, fond jen v RES), ares_es_75164086.json, ares_hledani_JT_Ventures.json, ares_hledani_JT_Investicni_spolecnost.json, ares_vr_47672684.json, ares_vr_08220867.json. Dále fundingtecheu_inv_Fond_Nase_Cesko.json.

## Dvojice cz-ii-biotech-investments / cz-ii-prague

**Rozhodnutí:** různé firmy. Nesloučeno. Zpracován jen cz-ii-biotech-investments (zařazen jako VC). i&i Prague zpracuje jiná dávka.

### Důvod

i&i Biotech Fund (značka i&i Bio) má vlastní investiční tým a poradce s jinými vlastníky a statutáry než i&i Prague. i&i Prague fond spoluzaložil a je jedním z jeho hlavních investorů (LP), fond ale nespravuje. Je to inkubátor a venture builder, který je ve 100% vlastnictví IOCB Tech s.r.o. Kromě sdílené značky „i&i“ a shodné adresy (Pobřežní 394/12, Praha 8) jsem nenašel společný tým ani společné řízení. Podle zadání shodná adresa ani vazba typu „založil“ samy nestačí.

### Doklady

- **Biotech Investments s.r.o., IČO 10885978** (ARES: `ares_vr_10885978.json`)
  - Sídlo Pobřežní 394/12, Praha 8.
  - Jednatelé Tomáš Maršálek a Ivan Vohlmuth (od 2024-12-01). Karel Kubias byl jednatelem do 2024-11-30.
  - Společníci po 1/3: SVAI Biotech Investments s.r.o. (IČO 10698604), Luctonber s.r.o. (IČO 09012583) a KAMAVO Biotech Investments s.r.o. (IČO 10699317).
  - Mezi společníky není IOCB Tech ani i&i Prague.
  - https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/10885978
- **i&i Prague, s.r.o., IČO 06058485** (ARES: `ares_vr_06058485.json`)
  - Jediný společník IOCB TECH s.r.o. (IČO 28934024, 100 %).
  - Jednatelé David Stíbal (od 2025-04-01) a Zuzana Demianová (od 2026-10-01). Jaromír Zahrádka byl jednatelem do 2023-11-01.
  - Předmět podnikání: zprostředkování, výzkum a vývoj, poradenství atd.
  - Sídlo Pobřežní 394/12 je zapsané od 2024-07-29.
  - https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06058485
- **https://www.inibio.eu/**
  - Fond i&i Biotech Fund I SCSp (Lucembursko).
  - „Investment Adviser: Biotech Investments, s. r. o., Pobřežní 394/12“.
  - Tým: Kubias, Vohlmuth, Maršálek (Founding Partners), Šumová, Vukoja (Partners).
  - i&i Prague je uvedený jen mezi „Partners“.
- **https://www.iniprague.com/**
  - „We are a biotech incubator and venture builder“.
  - „In 2021, we established the i&i Biotech Fund in cooperation with the European Investment Fund.“
- **https://www.uochb.cz/en/news/346/new-academic-fund-to-support-research-startups-with-more-than-45-million-euros** (23. 9. 2021)
  - Fond vznikl „with substantial involvement from i&i Prague“.
  - i&i Prague je spolu s EIF jedním z hlavních investorů fondu.
  - Jaromír Zahrádka je uvedený jako ředitel i&i Bio a spoluzakladatel i&i Prague. To je personální vazba z doby založení. Na současném webu fondu v týmu není.
- **https://cvca.cz/en/biotech-investments/**
  - Člen CVCA „i&i Biotech Investments“ s adresou Pobřežní 394/12 a kontaktem Tomáš Maršálek (CFO).
  - Fond „was established with substantial involvement from i&i Prague, which in addition to financial backing will also be providing unique knowhow and expertise“.
- **https://www.uochb.cz/en/ini-bio**
  - Fond „is an extension of the successful pursuits of i&i Prague“.

**Soubory ARES:** `ares_hledani_iiBiotech.json`, `ares_hledani_iiPrague.json`, `ares_hledani_iiPrague_varianta_mezery.json`, `ares_hledani_BiotechInvestments.json`, `ares_hledani_iiBiotechFund.json`, `ares_hledani_BiotechFund.json`, `ares_vr_10885978.json`, `ares_vr_06058485.json`. Všechny jsou v `ai-log/02-obohaceni/zdroje/`.

**Nejistota:** Formálního správce (AIFM/GP) lucemburského fondu jsem nedoložil. Kdyby jím byla entita ovládaná i&i Prague / IOCB Tech, bylo by vhodné rozhodnutí přezkoumat. Žádný nalezený zdroj to ale neuvádí.

## Dvojice cz-n1-ventures / cz-nation1

**Rozhodnutí:** tatáž investiční firma, sloučeno. Zpracován jeden záznam `cz-n1-ventures` (zarazen, VC, CZ) a `cz-nation1` zapsán jako `slouceno`, `slouceno_do` = `cz-n1-ventures`.

### Důvod

Nation 1 (Nation1) je původní název značky. V roce 2023 se přejmenovala na N1 (N1 Ventures, web n1.rocks). Jde o jeden investiční tým a značku, ne o dvě firmy ani o fond spravovaný druhou firmou. Kromě shodné adresy to dokládá:
- veřejně oznámené přejmenování,
- stejní managing partneři,
- stejný kontakt,
- společné portfolio,
- general partneři fondů, kteří dodnes nesou název „Nation 1“.

Za výsledné id volím `cz-n1-ventures`, protože je to současná značka.

### Doklady

- **https://cc.cz/z-nation-1-je-n1-cesti-startupovi-investori-chystaji-druhy-fond-chteji-do-nej-ziskat-necelou-miliardu/** (CzechCrunch, 18. 9. 2023)
  - Titulek „Z Nation 1 je N1“, v textu „Přejmenovává se na N1“.
  - Managing partneři jsou Marek Moravec a Jaroslav Trojan. Nově partneři Klára Kocarová a Ondřej Homola.
- **https://n1.rocks/**
  - Tým: Marek Moravec, Jaroslav Trojan, Klára Kocárová, Ondřej Homola (Partners).
  - Kanceláře: „Prague: Národní 135/14, Prague 1“, dále San Francisco a Lucembursko.
  - Portfolio mimo jiné Snuggs.
- **https://n1.rocks/disclosure**
  - „Nation 1 GP S.à r.l. and Nation 1 GP II S.à r.l.“ jsou general partneři fondů Nation 1 a Nation 1 VC fund II.
- **https://cvca.cz/en/nation1-2/** (profil člena CVCA „Nation1“)
  - Adresa „Národni 135/14, 110 00 Praha 1“, web www.nation1.vc.
  - Kontakt „Jaroslav Trojan, Managing Partner, jaroslav@nation1.vc“.
  - Portfolio v ČR „VRgineers, Snuggs, Buildiro“.
- Web www.nation1.vc nešel načíst (WebFetch ECONNREFUSED, curl chyba 7). Doménu jsem proto nepřekládal, rozhodnutí stojí na zdrojích výše.

### ARES

- `ares_hledani_Nation1.json`: jediná shoda **Nation1 Investment s.r.o., IČO 09172807**. Výpis je v `ares_vr_09172807.json`.
  - Sídlo Bělehradská 858/23, Praha 2.
  - Jednatelé a společníci Jaroslav Ton a Petr Jiříček.
  - S týmem N1 nijak nesouvisí, s žádným z kandidátů ho nespojuji.
- Bez shody: `ares_hledani_N1Ventures.json`, `ares_hledani_Nation1_varianta_mezera.json` („Nation 1“) a `ares_hledani_N1Management.json`.
- `ares_hledani_N1_varianta_sro.json`: 3 nesouvisející subjekty.
- `ares_hledani_sidlo_Narodni_135_14.json` (hledání podle sídla): v budově sídlí desítky firem, žádná se jménem N1 ani Nation 1. Shodná adresa tedy sama nic nedokazuje.

Všechny soubory jsou v `ai-log/02-obohaceni/zdroje/`. Funding.tech.eu: `fundingtecheu_inv_N1_Ventures.json` (Liki24), `fundingtecheu_inv_Nation1.json` (not found), `fundingtecheu_hledani_Nation.json`.

**Nejistota:** Český právní subjekt investiční firmy jsem nenašel. Lucemburské GP znám jen z webu investora. Na rozhodnutí o sloučení to nemá vliv, týká se jen jistoty existence záznamu.

## Dvojice cz-purposetech / cz-tilia-impact-ventures

**Rozhodnutí:** různé firmy. Nesloučeno. Zpracován jen cz-purposetech (zařazen jako VC). Tilia Impact Ventures zpracuje jiná dávka.

### Důvod

PurposeTech a Tilia Impact Ventures jsou dvě samostatné investiční firmy. Každá má jinou značku, jiný investiční tým, jiné právní subjekty s jinými vlastníky a statutáry a vlastní fondy. Společná je jen adresa Drtinova 557/10, Praha 5 (budova Impact Hubu, s nímž obě spolupracují) a osoba Petra Vítka. Vítek je spoluzakladatel a partner Tilia a podle CzechCrunch s ním Fous PurposeTech „rozjel v roce 2022“. Dnes je ale u PurposeTech uvedený jen v Advisory Board a v rejstříku PurposeTech nefiguruje. Jedna spoluinvestice (Lifeyear, 2025) firmy také nespojuje. Podle zadání shodná adresa ani vazba typu „založil“ či „spoluinvestuje“ samy nestačí. Žádná z firem není fondem spravovaným tou druhou.

### Doklady

- **PurposeTech s.r.o., IČO 19183992** (ARES: `ares_vr_19183992.json`)
  - Drtinova 557/10, Praha 5, vznik 2023-03-24.
  - Jednatel Zdeněk Fred Fous.
  - Společníci: ZEFIRIA, s.r.o. (IČO 24272230, 60 %) a Impact Hub Czechia, a.s. (IČO 02418321, 40 %).
  - https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19183992
- **PurposeTech F1 s.r.o., osoba rizikového kapitálu, IČO 19185103** (ARES: `ares_vr_19185103.json`)
  - Fond, 100% vlastník PurposeTech s.r.o., jednatel Fous.
  - https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19185103
- **Tilia Impact Ventures, osoba rizikového kapitálu, s.r.o., IČO 17848911** (ARES: `ares_vr_17848911.json`)
  - Drtinova 557/10, vznik 2022-12-19.
  - Jednatelé a společníci (po 1/2) Silke Horáková a Petr Vítek.
  - https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17848911
- **Tilia Impact Partners s.r.o., IČO 17621615** (ARES: `ares_vr_17621615.json`)
  - Drtinova 557/10.
  - Jednatel Pavel Petřek, dříve Andrew Gray a Petr Vítek.
  - Společníci: Cangarena, PE track, Carisbrook a PV for Good (po 25 %).
  - https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17621615
- **https://www.purposetech.vc/**
  - „PurposeTech is a pre-seed fund…“, „founded in 2023 by serial entrepreneur Zdenek Fred Fous and Impact Hub“.
  - Fous je „Co-Founder & GP“, Petr Vítek je v „Advisory Board“.
  - Tilia web nezmiňuje.
- **https://tilia.vc/**
  - „Tilia Impact Ventures backs Czech and CEE region founders…“.
  - Tým: Horáková, Vítek (co-founders), Petřek, Gray (partners).
  - Vlastní investiční výbor a portfolio 21 firem.
  - PurposeTech web nezmiňuje.
- **https://cc.cz/cesky-fond-prehodnotil-jake-vysledky-ocekava-od-startupu-misto-prudkeho-rustu-a-miliard-hleda-zisk/** (10. 2. 2026)
  - „PurposeTech rozjel v roce 2022 s Petrem Vítkem“.
  - Vítek je zmíněn jako spoluzakladatel Tilia Impact Ventures.
- **https://en.ain.ua/2025/07/01/lifeyear-raises-eur28m/** (1. 7. 2025)
  - Spoluinvestice obou: „Verge HealthTech Fund, Tilia Impact Ventures, PurposeTech“.

**Soubory ARES:** `ares_hledani_PurposeTech.json`, `ares_hledani_TiliaImpact.json`, `ares_vr_19183992.json`, `ares_vr_19185103.json`, `ares_vr_17621615.json`, `ares_vr_17848911.json`. Všechny jsou v `ai-log/02-obohaceni/zdroje/`.

## Dvojice cz-rockaway-ventures / cz-rockawayx

**Rozhodnutí:** dvě různé investiční firmy, nesloučeno. Každý kandidát je zpracovaný samostatně:
- `cz-rockaway-ventures`: zarazen (VC, CZ),
- `cz-rockawayx`: nevyresene (otázka typ).

### Důvod

Obě značky mají společný původ ve skupině Rockaway Capital Jakuba Havrlanta a obě sídlí na stejné adrese (Generála Píky 430/26, Praha 6). Podle zadání to ke sloučení nestačí. Rozhoduje, že jde o dva různé investiční týmy a dvě značky s vlastními fondy, a ani jedna nespravuje fond té druhé.

- **Jiný tým**
  - Rockaway Ventures vedou General Partneři Petr Šmíd a Dušan Zábrodský, zakladatelem je Jakub Havrlant.
  - RockawayX vede Viktor Fischer (Managing Partner a CEO), dalšími členy jsou Samantha Bohbot, Adam Bilko, Marek Sandrik a další.
- **Jiné fondy a strategie**
  - Rockaway Ventures má Rockaway Ventures Fund II (necelých 55 mil. EUR) na late-seed a Series A tech startupy.
  - RockawayX má fondy VC I a VC II (oba uzavřené), Market Neutral Fund (Lichtenštejnsko) a Liquid Opportunities Fund (Kajmanské ostrovy). Zaměřuje se na kryptoaktiva.
- **Výslovná nezávislost:** CzechCrunch 27. 8. 2026 píše, že RockawayX vznikla v roce 2018 „v podhoubí skupiny Rockaway Capital Jakuba Havrlanta, dnes je to plně nezávislá struktura“.
- **Weby:** rockawayventures.com uvádí „part of the Rockaway Capital group“ a RockawayX nezmiňuje. Web rockawayx.com nezmiňuje Rockaway Ventures ani Rockaway Capital, jako dřívější název uvádí jen „Rockaway Blockchain Fund“.

### Doklady

- https://rockawayventures.com/
  - Uvádí „part of the Rockaway Capital group“ a „Rockaway Ventures Fund“.
- https://www.vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund (16. 5. 2025)
  - Fund II, „closed its second fund at nearly €55 million“.
  - GP Zábrodský a Šmíd.
- https://rockawayx.com/
  - Popis činnosti „Venture and yield strategies“, Liquidity, Infrastructure.
  - Kanceláře v Londýně, Praze a Dubaji.
  - Patička „© 2026 Blockad s.r.o. | RockawayX (previously Rockaway Blockchain Fund)“.
- https://rockawayx.com/about-us
  - Tým RockawayX.
- https://rockawayx.com/funds
  - Fondy RockawayX.
- https://cc.cz/cesi-krypto-a-40-miliard-pro-investice-nic-takoveho-zatim-jeste-nikdo-nepostavil-rika-sef-rockawayx/ (27. 8. 2026)
  - Výslovně „plně nezávislá struktura“.

### ARES (ai-log/02-obohaceni/zdroje/)

**Hledání**
- `ares_hledani_RockawayVentures.json`: 7 subjektů, všechny na adrese Generála Píky 430/26.
- `ares_hledani_RockawayX.json`: 6 subjektů, RockawayX a.s., Labs, Holding, Infra, Distribution a Research, všechny na adrese Generála Píky 430/26.
- `ares_hledani_Rockaway.json`: 48 výsledků, slouží jen k přehledu.
- `ares_hledani_Blockad.json`: Blockad s.r.o., IČO 08006458.

**Výpisy, skupina Rockaway Ventures**
- `ares_vr_06387136.json`: Rockaway Ventures a.s., zapsaná 2017. Představenstvo Jakub Havrlant (předseda) a Viktor Fischer (člen). Je to jediná personální vazba mezi oběma značkami. Jde o starší a.s. a sama nestačí ke sloučení.
- `ares_vr_14125129.json`: Rockaway Ventures Advisors a.s. Představenstvo Havrlant, Dušan Zábrodský a Andrea Lauren, tedy tým Rockaway Ventures.
- `ares_vr_14053942.json`: Rockaway Ventures Fund Holding a.s. Představenstvo Havrlant, Zábrodský a Lauren.
- `ares_vr_14235781.json`: Rockaway Ventures Fund SICAV a.s., fond kvalifikovaných investorů. Statutárem je AMISTA investiční společnost, a.s.

**Výpisy, skupina RockawayX**
- `ares_vr_17457009.json`: RockawayX a.s., dříve Snowcrash a.s. Předsedou správní rady je Viktor Fischer.
- `ares_vr_19311753.json`: RockawayX Holding a.s. Předsedou správní rady je Viktor Fischer.
- `ares_vr_08006458.json`: Blockad s.r.o. Jednatelem je Viktor Fischer, jediným společníkem RockawayX a.s.

**Shrnutí:** Statutární orgány entit Rockaway Ventures (Havrlant, Zábrodský, Lauren) se s entitami RockawayX (Fischer) nepřekrývají. Výjimkou je starší Rockaway Ventures a.s.

**funding.tech.eu:** `fundingtecheu_inv_Rockaway_Ventures.json` (16 kol, alias Rockaway Capital) a `fundingtecheu_inv_RockawayX.json` (7 kol, krypto, fintech a gaming). Každý profil má jiné portfolio.

