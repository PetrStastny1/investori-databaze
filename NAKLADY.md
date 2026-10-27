# Odhad nákladů na databázi investorů pro celý svět

Krok 7 (PLAN.md, bod 10). Čísla v tabulkách pocházejí z `python3 scripts/naklady.py`, který čte jen agregovanou spotřebu v [ai-log/07-naklady/spotreba.csv](ai-log/07-naklady/spotreba.csv) (vytváří ji `python3 scripts/spotreba_z_logu.py` z lokálních logů Claude Code). Úplný generovaný výstup je v [ai-log/07-naklady/vypocet.md](ai-log/07-naklady/vypocet.md). Oba skripty jsou deterministické a výpočet běží bez sítě.

## Shrnutí

- **Pilot (kroky 0–6) spotřeboval 193,3 mil. tokenů v 1 879 požadavcích na API, v přepočtu na ceny API zhruba 108 USD.** Pilot běžel v rámci předplatného Claude, takže jde o přepočet na ceny API, ne o skutečně zaplacenou částku. Částka 108 USD pokrývá jen tu část práce, kterou logy zachytily. Co v ní chybí, je v [seznamu neznámých položek](#neznámé-položky). Většinu ze 193 mil. tokenů (96 %) tvoří opakované čtení kontextu z cache, které je za dvacetinu ceny běžného vstupu.
- **Na kandidáta** stojí produkční část (sběr, obohacení, kontrola druhým agentem) 1,67 USD a zhruba 2 min 10 s času agentů při souběžnosti pilotu. **Na zařazený záznam** je to 3,46 USD.
- **Svět (5 600–11 000 zařazených, PLAN.md 8.2), při sazbě 25 USD/h (modelový předpoklad):**

  | | nízká | střední | vysoká |
  |---|---|---|---|
  | sestavení s kontrolním vzorkem: AI / člověk / celkem | $19 713 / $13 983 (559 h) / **$33 696** | $43 648 / $30 253 (1 210 h) / **$73 901** | $96 163 / $55 255 (2 210 h) / **$151 418** |
  | sestavení s plnou kontrolou: AI / člověk / celkem | $21 325 / $33 704 (1 348 h) / **$55 029** | $47 397 / $78 053 (3 122 h) / **$125 450** | $104 670 / $148 958 (5 958 h) / **$253 628** |
  | roční aktualizace poslední investice: AI / člověk / celkem | $4 190 / $1 225 (49 h) / **$5 415** | $16 303 / $2 067 (83 h) / **$18 370** | $51 445 / $3 125 (125 h) / **$54 570** |

- **Poměr nákladových položek:** při sazbě 25 USD/h je v sestavení s kontrolním vzorkem větší položkou AI. Lidská práce by byla větší položkou od sazby zhruba 35–44 USD/h. S plnou ruční kontrolou je lidská práce větší položkou už při 25 USD/h. Tento poměr popisuje jen rozložení nákladů a **neříká nic o tom, zda lze lidskou kontrolu nahradit**.
- Většinu lidských hodin tvoří ruční rozhodnutí nevyřešených a hraničních kandidátů, ne kontrolní vzorek. Je to zároveň nejméně podložená položka: čas na jedno rozhodnutí je modelový předpoklad a v pilotu tyto kandidáty nikdo ručně nerozhodoval.
- Výsledek je zhruba úměrný poměru kandidátů k zařazeným (56/27 z českého pilotu). Pro svět je to neověřený pracovní předpoklad. Při polovičním poměru vychází AI ve střední variantě na 22 000 USD, při dvojnásobném na 87 000 USD.

## 1. Naměřená spotřeba pilotu

### Postup čtení logů

- **Zdroj:** lokální logy Claude Code (`~/.claude/projects/…/*.jsonl` a `*/subagents/*.jsonl`). Ze záznamů typu `assistant` skript čte jen `message.usage`, `message.model`, časovou značku a identifikátory `message.id` a `requestId`. Obsah zpráv nečte do výstupu ani ho neukládá. Do CSV jdou jen agregovaná čísla.
- **Kroky 0 a 1** běžely s pracovním adresářem v domovské složce, takže jejich logy leží v `~/.claude/projects/-Users-petrstastny/`. Ke krokům jsem je přiřadil podle časů (13:28–14:03 UTC a 14:12–14:46 UTC 26. 10., commity 7036b5b a c007cb6). Pro potvrzení jsem nad rámec polí usage, model a čas přečetl ještě pole `cwd`, které ukazuje na adresář projektu.
- **Deduplikace:** Claude Code zapisuje každý blok odpovědi (text, volání nástroje…) jako samostatný záznam se stejnou usage celé odpovědi. Záznam se proto počítá jednou podle dvojice (`message.id`, `requestId`). Skript ověřuje, že vyřazené výskyty mají shodnou usage a že se žádná dvojice neopakuje napříč soubory, tedy ani po pokračování session 27. 10. **Ze 4 121 záznamů usage jsem vyřadil 2 242 duplicit a zůstalo 1 879 unikátních požadavků.** Duplicity napříč soubory: 0.
- **Přiřazení ke krokům** je v tabulce `SESSIONY` ve skriptu: jedna session na krok podle času, commitů a exportů v `ai-log/`. Session zkušební dávky je rozdělená v 15:02:31 UTC (konec dávky podle mereni.txt), krok 4 na fáze A a B podle commitu 967cb97 a krok 5 podle data (26. 10. příprava, 27. 10. uložení hodnocení). Pomocný agent patří celý k části, ve které začal.
- Probíhající session kroku 7 do součtu nezahrnuji.

### Spotřeba po krocích

Ceny API pro Claude Opus 5.5. Byl to jediný model v logech, hlavní konverzace i pomocní agenti.

| krok | požadavků API | tokenů celkem | z toho pomocní agenti | cena API | čas |
|---|---|---|---|---|---|
| 0 plán a založení | 46 | 4 809 722 | – | $3,34 | 34 min (rozpětí v logu) |
| 1 sběr kandidátů | 132 | 15 511 550 | 3 429 000 (3 agenti) | $9,01 | 34 min (rozpětí v logu) |
| 2 zkušební dávka + úprava pravidel | 40 | 4 421 482 | – | $3,07 | dávka 5 min 49 s (mereni.txt), celkem 36 min v logu |
| 2 obohacení | 1 039 | 94 629 262 | 79 253 923 (31 agentů) | $49,20 | 62 min 30 s (mereni.txt) |
| 3 automatická kontrola | 22 | 2 399 177 | – | $2,58 | 8 min (rozpětí v logu) |
| 4 kontrola druhým agentem | 540 | 61 958 241 | 56 165 245 (13 agentů) | $31,63 | 24 min 32 s (mereni.txt) |
| 5 příprava a uložení ruční kontroly | 36 | 7 394 805 | – | $6,81 | 28 min (rozpětí v logu) |
| 6 měření | 24 | 2 127 099 | – | $1,89 | 13 min (rozpětí v logu) |
| **celkem** | **1 879** | **193 251 338** | **138 848 168 (47 agentů)** | **$108** | |

Po druzích: hlavní konverzace 372 požadavků, 54,4 mil. tokenů, 33,75 USD. Pomocní agenti 1 507 požadavků, 138,8 mil. tokenů, 73,78 USD. Rozpad na vstup, zápis do cache (5 min / 1 h), čtení z cache a výstup je ve [vypocet.md](ai-log/07-naklady/vypocet.md).

**Co číslo 193 mil. tokenů znamená:** většinu (185 mil., 96 %) tvoří čtení kontextu z cache. Agent při každém volání znovu čte celý dosavadní kontext a cache ho účtuje za 0,20 USD/MTok místo 4 USD/MTok. Na ceně má tak čtení z cache jen zhruba třetinu (≈ 37 USD). Výstup (1,5 mil. tokenů) stojí zhruba 31 USD a zápis do cache zhruba 40 USD. **Přepočet ≈ 108 USD pokrývá jen zachycenou část práce**, viz [Neznámé položky](#neznámé-položky).

„Rozpětí v logu“ je čas od prvního do posledního volání API v kroku, včetně čekání na uživatele. Kde mereni.txt čas měří, používám jeho hodnotu.

**Webové požadavky (mereni.txt):** obohacení 1 121 (WebSearch 318, WebFetch 447 včetně 82 neúspěšných a 1 hlavního agenta, ARES 225, funding.tech.eu 85, curl 46). Kontrola druhým agentem 445 (WebSearch 34, WebFetch 5, curl 406). Zkušební dávka 51. Ve sběru kandidátů je známé jen „zhruba 120“ požadavků na funding.tech.eu (README), ostatní kroky požadavky neměřily.

### Srovnání s mereni.txt

| | mereni.txt | z logů: kontext posledního volání (součet přes agenty) | z logů: kumulativní spotřeba |
|---|---|---|---|
| krok 4, fáze A, 7 agentů | 1 265 644 | 1 264 850 | 39 111 426 |
| krok 4, fáze B, 6 agentů | 861 130 | 861 130 | 17 053 819 |
| krok 2, 31 agentů | neuvedeno | 3 476 650 | 79 253 923 |

Čísla v mereni.txt nejsou spotřeba. Jsou to velikosti kontextu posledního volání každého agenta (vstup + cache + výstup), tak jak je hlásí nástroj Agent po doběhnutí. Ve fázi B sedí přesně. Ve fázi A se liší o 794 tokenů (0,06 %), příčinu z polí usage nedohledám. Agent při každém volání znovu čte celý dosavadní kontext (většinou z cache), takže skutečná spotřeba je 31× (A) a 20× (B) vyšší. Pro náklady proto používám kumulativní hodnotu.

### Neznámé položky

Následující položky v součtu nejsou. Nejde o nulu, ale o neznámou hodnotu, takže skutečné náklady pilotu jsou vyšší než 108 USD:

- **WebFetch:** nástroj předává staženou stránku pomocnému modelu, jehož požadavky v logu nejsou. WebFetch na API je bez příplatku, tokeny pomocného modelu ale neznám.
- **WebSearch:** `usage.server_tool_use` je ve všech záznamech 0, vyhledávání běží mimo zalogované požadavky. Poplatek 10 USD / 1 000 vyhledávání počítám jen u kroků, kde je počet vyhledávání naměřený (obohacení, kontrola, zkušební dávka, celkem 3,61 USD). Tokeny výsledků vyhledávání jsou neznámé.
- **Asistence AI u ruční kontroly mimo Claude Code** (Claude a ChatGPT podle README, „Ruční kontrola – kdo hodnotil“): spotřeba neznámá.
- **Webové požadavky** ve sběru kandidátů a v krocích 0, 3, 5, 6.

## 2. Ceník

Zdroj: [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) (přesměrováno z docs.claude.com), načteno 27. 10. 2026. V USD za milion tokenů:

| model | vstup | zápis do cache 5 min | zápis do cache 1 h | čtení z cache | výstup |
|---|---|---|---|---|---|
| Claude Opus 5.5 | 4 | 5 | 8 | 0,20 | 20 |

Web search stojí 10 USD za 1 000 vyhledávání, web fetch je bez příplatku. Logy mají `inference_geo` „global“, takže se nepoužije násobek 1,1 za zpracování jen v USA. Batch API (sleva 50 %) do výpočtu nezahrnuji, protože agenti pracují interaktivně s nástroji.

**Pilot běžel v rámci předplatného Claude. Všechny částky jsou přepočet na ceny API, ne skutečně zaplacená částka.**

## 3. Jednotkové náklady pilotu

Na kandidáta = děleno 56 (57 vstupních, Nation1 sloučeno do N1 Ventures), na zařazený záznam = děleno 27.

| fáze | tokenů / kandidáta | cena / kandidáta | čas / kandidáta | tokenů / zařazený | cena / zařazený | čas / zařazený |
|---|---|---|---|---|---|---|
| sběr kandidátů | 276 992 | $0,16 | 36 s | 574 502 | $0,33 | 1 min 16 s |
| obohacení | 1 689 808 | $0,94 | 1 min 7 s | 3 504 787 | $1,94 | 2 min 19 s |
| automatická kontrola (vývoj skriptu) | 42 842 | $0,05 | 9 s | 88 858 | $0,10 | 18 s |
| kontrola druhým agentem | 1 106 397 | $0,57 | 26 s | 2 294 750 | $1,18 | 55 s |
| ruční kontrola: podpora AI v Claude Code | 132 050 | $0,12 | 30 s | 273 882 | $0,25 | 1 min 1 s |
| režie (plán, zkušební dávka, úprava pravidel, měření) | 202 827 | $0,15 | 1 min 30 s | 420 678 | $0,31 | 3 min 6 s |
| ruční kontrola: čas člověka (**modelový předpoklad**) | – | – | 3 min 34 s–5 min 21 s | – | – | 7 min 24 s–11 min 7 s |

- Cena zahrnuje poplatek za web search tam, kde je počet vyhledávání naměřený. Čas obohacení a kontroly druhým agentem je z mereni.txt, u ostatních fází jde o rozpětí volání v logu. Agenti běželi souběžně (4–6 v obohacení, 6–7 v kontrole), takže čas na kandidáta je čas při této souběžnosti.
- Automatická kontrola stála jednorázově vývoj skriptu. Její další spuštění je lokální a tokeny nespotřebuje.
- **Ruční kontrola – čas člověka není změřený.** Používám modelový předpoklad 10–15 min na firmu s asistencí AI, tedy 3 h 20 min až 5 h za 20 firem. V tabulce je rozpočítaný na 56 kandidátů / 27 zařazených, i když ručně bylo zkontrolováno jen 20 zařazených. Z logů ho neodhaduji: hodnocení probíhalo zčásti mimo Claude Code a rozpětí v logu nic neříká o čase člověka.

## 4. Přepočet na svět

### Základ a předpoklady

- **Počet zařazených:** scénář z PLAN.md 8.2, po typech: VC 2 400–5 600, PE 2 800–4 200, family office 400–1 200, celkem 5 600–11 000. Střední varianta bere středy rozpětí (8 300). CVC a andělé ve scénáři chybějí (PLAN.md 8.2).
- **Kandidátů na zařazený záznam: 56/27 = 2,07, jen jako pracovní předpoklad.** Pilot zahrnoval český VC/CVC, svět i PE a family office, a přenositelnost poměru jsme neověřili. U family office (PLAN.md počítá s tím, že pravidly projde 5–15 %) může být poměr výrazně horší. Citlivost uvádím níže.
- **Podíl nevyřešených a hraničních:** 12/56 = 21,4 % kandidátů (výsledek agenta před ruční kontrolou, naměřeno). Každý takový případ musí rozhodnout člověk, jinak databáze nevznikne. **Čas na jedno rozhodnutí je modelový předpoklad** (stejný jako u ruční kontroly firmy). V pilotu nevyřešené a hraniční kandidáty nikdo ručně nerozhodoval, takže čas na ně není naměřený ani odhadnutý z praxe. Tato položka tvoří ve všech variantách většinu lidských hodin s kontrolním vzorkem (415 z 559 h, 961 z 1 210 h, 1 833 z 2 210 h) a je ze všech položek nejméně podložená.
- **Hodinová sazba člověka: 25 USD/h, modelový předpoklad**, ne zjištěná tržní cena. Je to parametr `SAZBA_USD_H` ve skriptu.

| parametr (předpoklad) | nízká | střední | vysoká |
|---|---|---|---|
| zařazených záznamů | 5 600 | 8 300 | 11 000 |
| násobek tokenů na kandidáta vůči ČR | 1,0 | 1,5 | 2,5 |
| násobek času člověka vůči ČR | 1,0 | 1,25 | 1,5 |
| min na firmu, ruční kontrola (základ, modelový předpoklad) | 10 | 12,5 | 15 |
| vrstev kontrolního vzorku | 3 (VC, PE, FO) | 3 (VC, PE, FO) | 3 (VC, PE, FO) |
| opakování režie metodiky (nové typy, jazykové oblasti) | 5 | 10 | 20 |
| aktualizace: tokeny přepočtu vůči obohacení | 20 % | 35 % | 50 % |
| aktualizace: min na kontrolu poslední investice | 3 | 4 | 5 |

### Co se mimo ČR zhorší a jak to promítám

| zhoršení | proč | promítnutí do variant |
|---|---|---|
| **Jazyky** | zprávy o transakcích, weby a rejstříky v jiných jazycích: víc vyhledávání, překlad, víc chyb ve výkladu | násobek tokenů 1,0–2,5, násobek času člověka 1,0–1,5 (kontrolor musí číst zdroje v cizím jazyce nebo se spolehnout na překlad AI) |
| **Rejstříky bez otevřeného API** | v pilotu ověřovalo identitu bezplatné API ARES (225 požadavků). Jinde bývají rejstříky placené, neúplné nebo jen přes web (u lucemburských GP se právní subjekt nepodařilo ověřit ani v pilotu) | vyšší násobek tokenů (víc pokusů přes WebFetch a neúspěšných stažení). **Poplatky za placené rejstříky a databáze ve výpočtu nejsou**, jsou to samostatný parametr |
| **Chybějící média** | menší trhy, PE a family office mají méně veřejných zpráv o transakcích. Víc kandidátů skončí jako nevyřešení nebo bez doložené investice | vyšší násobek tokenů (delší hledání, než agent skončí) a citlivost na poměr kandidátů. Podíl nevyřešených držím na pilotních 21,4 %. Každých +10 p. b. přidá ve střední variantě zhruba 450 h ruční práce |
| **Struktury fondů** | GP/AIFM v Lucembursku, na Kajmanech nebo v Delaware, tým jinde. V pilotu to byl hlavní zdroj sporů o sídlo | víc nevyřešených případů a čas člověka. Hlavně je potřeba upřesnit pravidlo sídla před škálováním (oddíl 5) |

### Výsledky

Kontrolní vzorek je náhodný výběr zařazených záznamů pro odhad přesnosti s přesností **±5 p. b. při 95 %**. Vzorec je n₀ = z²·p(1−p)/E² pro nejhorší případ p = 0,5, tedy n₀ ≈ 385, s korekcí na konečný soubor. Ve všech třech variantách se počítá stejnou metodou, zvlášť pro VC, PE a family office (3 vrstvy po zhruba 200–360 záznamech), protože typy se podle PLAN.md 8.2 ve spolehlivosti liší. Velikost vzorku se mezi variantami liší jen podle velikosti vrstev. ±5 p. b. platí pro pole, které je vyplněné u všech záznamů vzorku. U ticketu a kapitálu, vyplněných v pilotu u 55 % a 40 % záznamů, bude interval širší.

**Co kontrolní vzorek dokládá a co ne:**

- Kontrolní vzorek slouží k **odhadu kvality souboru** (podílu správných záznamů a polí v databázi jako celku a po typech).
- **Nepotvrzuje správnost každého jednotlivého záznamu.** Záznamy mimo vzorek zůstávají ručně nezkontrolované a chyby v nich vzorek neopraví. Opraví se jen chyby nalezené ve vzorku.
- Interval ±5 p. b. popisuje **jen výběrovou nejistotu** (vliv náhodného výběru). Nezahrnuje možné chyby samotného hodnocení s asistencí AI: když se kontrolor s AI splete, interval to nezachytí.

| položka | nízká | střední | vysoká |
|---|---|---|---|
| zařazených záznamů | 5 600 | 8 300 | 11 000 |
| kandidátů (× 56/27) | 11 615 | 17 215 | 22 815 |
| AI: sběr, obohacení, kontrola druhým agentem | $19 363 | $43 049 | $95 088 |
| AI: režie metodiky | $55 | $110 | $219 |
| AI: podpora ruční kontroly (vzorek) | $295 | $489 | $855 |
| **AI celkem, s kontrolním vzorkem** | **$19 713** | **$43 648** | **$96 163** |
| AI celkem, s plnou ruční kontrolou | $21 325 | $47 397 | $104 670 |
| AI na zařazený záznam (vzorek) | $3,52 | $5,26 | $8,74 |
| čas agentů při souběžnosti pilotu | 418 h | 930 h | 2 054 h |
| min člověka na firmu | 10,0 | 15,6 | 22,5 |
| ruční rozhodnutí nevyřešených a hraničních (**modelový předpoklad**) | 415 h | 961 h | 1 833 h |
| kontrolní vzorek: firem / hodin | 867 / 144 h | 958 / 249 h | 1 005 / 377 h |
| **člověk celkem, s kontrolním vzorkem** | **559 h** | **1 210 h** | **2 210 h** |
| plná ruční kontrola zařazených | 933 h | 2 161 h | 4 125 h |
| **člověk celkem, s plnou ruční kontrolou** | **1 348 h** | **3 122 h** | **5 958 h** |

**Průběžná aktualizace (ročně):** čtvrtletní přepočet poslední investice u všech zařazených záznamů. AI za něj zaplatí 20–50 % tokenů obohacení na záznam. Člověk každé čtvrtletí zkontroluje náhodný vzorek pole `posledni_investice` (±5 p. b. při 95 % pro p = 0,79 z pilotu, zhruba 245–250 záznamů).

| | nízká | střední | vysoká |
|---|---|---|---|
| AI ročně (4 přepočty) | $4 190 | $16 303 | $51 445 |
| člověk ročně | 49 h | 83 h | 125 h |

**Rozsah aktualizace:** čtvrtletní aktualizace modeluje jen pole poslední investice (a s ním to, zda investor zůstává v 24měsíčním okně). **Nemodeluje úplnou údržbu všech údajů** (typ, sídlo, sektory, ticket, kapitál, zdroje) **ani hledání nových investorů**, kteří do databáze přibudou. Skutečné náklady na údržbu proto budou vyšší.

### Náklady v USD

Sazba 25 USD/h je modelový předpoklad, ne zjištěná tržní cena.

| položka | nízká | střední | vysoká |
|---|---|---|---|
| sestavení s kontrolním vzorkem: AI | $19 713 | $43 648 | $96 163 |
| sestavení s kontrolním vzorkem: člověk | $13 983 | $30 253 | $55 255 |
| **sestavení s kontrolním vzorkem: celkem** | **$33 696** | **$73 901** | **$151 418** |
| sestavení s plnou kontrolou: AI | $21 325 | $47 397 | $104 670 |
| sestavení s plnou kontrolou: člověk | $33 704 | $78 053 | $148 958 |
| **sestavení s plnou kontrolou: celkem** | **$55 029** | **$125 450** | **$253 628** |
| roční aktualizace: AI | $4 190 | $16 303 | $51 445 |
| roční aktualizace: člověk | $1 225 | $2 067 | $3 125 |
| **roční aktualizace: celkem** | **$5 415** | **$18 370** | **$54 570** |

Při sazbě 25 USD/h je v sestavení s kontrolním vzorkem větší položkou AI, s plnou kontrolou lidská práce. Ve variantě se vzorkem by lidská práce byla větší položkou od sazby zhruba 35 USD/h (nízká), 36 USD/h (střední) a 44 USD/h (vysoká). Je to jen poměr nákladových položek. Neříká nic o tom, zda lze lidskou kontrolu nahradit kontrolním agentem (oddíl 5).

### Citlivost na poměr kandidátů k zařazeným

Mění se položky úměrné počtu kandidátů: AI za sběr, obohacení a kontrolu a ruční rozhodnutí nevyřešených. Poloviční poměr (1,04) je blízko spodní meze 1, kdy by pravidly prošel každý kandidát.

| varianta | poměr 1,04 (× 0,5) | poměr 2,07 (pilot) | poměr 4,15 (× 2) |
|---|---|---|---|
| nízká: AI / člověk (vzorek) | $10 032 / 352 h | $19 713 / 559 h | $39 077 / 974 h |
| střední: AI / člověk (vzorek) | $22 124 / 730 h | $43 648 / 1 210 h | $86 697 / 2 171 h |
| vysoká: AI / člověk (vzorek) | $48 619 / 1 294 h | $96 163 / 2 210 h | $191 252 / 4 044 h |

Plná ruční kontrola: ve variantě nízká 1 141 / 1 348 / 1 763 h, střední 2 642 / 3 122 / 4 083 h, vysoká 5 042 / 5 958 / 7 792 h.

## 5. Kam směřovat lidskou kontrolu

Priority vycházejí z [data/mereni_vzorku.md](data/mereni_vzorku.md) (20 zařazených firem):

1. **Poslední investice.** Ze všech polí má nejnižší správnost: 15/19 = 78,9 % (95% CI 56,7–91,5 %). Všechny 4 chyby výstupu mají stejný vzor: agent uvedl doloženou investici, ale přehlédl novější (Look AI, Purple, Reflex, ZAKA). Kontrolor by měl u každého záznamu, nebo aspoň u celého kontrolního vzorku, projít novinky na webu investora a nejnovější zprávy po datu, které uvedl agent. Totéž pole je předmětem čtvrtletní aktualizace a jejího kontrolního vzorku.
2. **Sídlo a příslušnost u fondů se zahraničním správcem.** Z 20 firem byly 2 `ne` (i&i Biotech, N1: GP/AIFM v Lucembursku, tým v Praze) a 1 `nelze_overit` (Tensor). Šlo o upřesnění metodiky, ne o chybu agenta. Před škálováním je potřeba pravidlo sídla rozhodnout (správce × fond × tým). Ručně pak zkontrolovat záznamy, kde agent najde zahraniční GP/AIFM nebo fondovou strukturu (SCSp, S.à r.l., LP). Mimo ČR bude takových případů víc.
3. **Nezávislost zdrojů.** U 6/20 firem ji nešlo ověřit: agent měl `puvod` null a zprávy mohly vycházet z jedné tiskové zprávy. Lidská kontrola by měla jít na záznamy, jejichž investice stojí jen na zdrojích s neznámým původem. Systémovější řešení je vyžadovat původ zdroje už ve schématu.
4. **Přiřazení investice přes fondy** (Presto: investice provedl lucemburský fond jiného správce) a **nástroj investice** (i&i Prague: nástroj doložil až výpis z rejstříku portfoliové firmy, nepřímo): `je_investor` a `investicni_cinnost` nešlo ověřit u 1 a 1 z 20 firem (před opravou hodnocení i&i Prague v kroku 9 u 2 a 1).
5. **Nevyřešení a hraniční kandidáti** (21 % kandidátů) vyžadují rozhodnutí člověka vždy. V pilotu je zatím nikdo ručně nekontroloval.

**Omezení:** Netvrdím, kde by lidskou kontrolu mohl nahradit kontrolní agent. Konečné hodnocení vznikalo s asistencí AI a zčásti podle nálezů kontrolního agenta: 3 ze 4 chyb výstupu se našly až po přečtení jeho nálezů a 6 verdiktů se po nich změnilo z `ano` na `nelze_overit` (mereni_vzorku.md, 5.4). Kontrolní agent proto nebyl měřen proti nezávislému standardu a měření nahraditelnost lidské kontroly nedokládá. Ruční kontrola navíc pokryla jen zařazené. Recall (kolik investorů agent chybně vyřadil) změřený není a kontrola vyřazených by k hodinám výše ještě přibyla.

## 6. Omezení

- **Podhodnocení AI:** chybí tokeny pomocného modelu WebFetch, tokeny výsledků WebSearch, poplatky za vyhledávání ve sběru kandidátů a asistence AI mimo Claude Code (oddíl 1, Neznámé položky).
- **Pilot je malý a místní:** 56 kandidátů, český VC/CVC. Násobky pro svět, minuty na firmu, počet opakování režie a podíl tokenů aktualizace jsou předpoklady, ne měření.
- **Čas ruční kontroly je modelový předpoklad** (10–15 min na firmu s asistencí AI), ne naměřená hodnota. Totéž platí pro čas na ruční rozhodnutí nevyřešených a hraničních kandidátů, které v pilotu nikdo nerozhodoval. Tato položka tvoří většinu lidských hodin a je nejméně podložená.
- **Hodinová sazba 25 USD/h je modelový předpoklad**, ne zjištěná tržní cena.
- **Kontrolní vzorek** odhaduje kvalitu souboru, nepotvrzuje jednotlivé záznamy. Jeho ±5 p. b. popisuje jen výběrovou nejistotu, ne chyby hodnocení s asistencí AI. **Aktualizace** modeluje jen poslední investici, ne úplnou údržbu ani hledání nových investorů.
- **Sběr kandidátů** škáluji na kandidáta. Ve světě ale závisí spíš na počtu zemí a zdrojových seznamů a na deduplikaci mezi zeměmi.
- **Časy kroků 0, 1, 3, 5 a 6** jsou rozpětí volání v logu včetně čekání na uživatele. Čas agentů ve světě (930 h ve střední variantě) platí při souběžnosti pilotu. Při vyšší souběžnosti se zkrátí, omezují ho ale limity účtu.
- **Ceny:** stav ceníku k 27. 10. 2026, bez Batch API. Pilot těžil z cache promptů Claude Code. Jiná orchestrace se slabším využitím cache by vyšla dráž.
- **Mimo výpočet:** placené rejstříky a databáze transakcí, infrastruktura a vývoj nástrojů pro škálování, CVC a andělé (nejsou ve scénáři PLAN.md 8.2).
- **Přiřazení logů:** session kroků 0 a 1 leží v jiném adresáři logů (domovská složka) a přiřadil jsem je podle času a pole `cwd`.

## Zdroje

- Ceník Claude API: https://platform.claude.com/docs/en/about-claude/pricing (načteno 27. 10. 2026)
- Scénář počtu investorů: [PLAN.md](PLAN.md), bod 8.2
- Měření přesnosti: [data/mereni_vzorku.md](data/mereni_vzorku.md)
- Časy a webové požadavky: [ai-log/02-obohaceni/mereni.txt](ai-log/02-obohaceni/mereni.txt), [ai-log/02-zkusebni-davka/mereni.txt](ai-log/02-zkusebni-davka/mereni.txt), [ai-log/04-kontrola-zdroju/mereni.txt](ai-log/04-kontrola-zdroju/mereni.txt)
- Výsledek agenta (nevyřešení, hraniční) a kdo hodnotil: [README.md](README.md)
- Spotřeba z logů: [ai-log/07-naklady/spotreba.csv](ai-log/07-naklady/spotreba.csv) (`scripts/spotreba_z_logu.py`), výpočet: [ai-log/07-naklady/vypocet.md](ai-log/07-naklady/vypocet.md) (`scripts/naklady.py`)
