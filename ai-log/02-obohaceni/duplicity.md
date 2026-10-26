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

## Důvod

i&i Biotech Fund (značka i&i Bio) má vlastní investiční tým a poradce s jinými vlastníky a statutáry než i&i Prague. i&i Prague fond spoluzaložil a je jedním z jeho hlavních investorů (LP), fond ale nespravuje. Je to inkubátor a venture builder, který je ve 100% vlastnictví IOCB Tech s.r.o. Kromě sdílené značky „i&i“ a shodné adresy (Pobřežní 394/12, Praha 8) jsem nenašel společný tým ani společné řízení. Podle zadání shodná adresa ani vazba typu „založil“ samy nestačí.

## Doklady

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

