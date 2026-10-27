# Výpočet nákladů (generováno skriptem scripts/naklady.py, nepřepisovat ručně)

Ceny API: Claude Opus 5.5, USD/MTok: vstup 4, zápis do cache 5 min 5, zápis do cache 1 h 8, čtení z cache 0,20, výstup 20; web search 10 USD / 1 000. Zdroj https://platform.claude.com/docs/en/about-claude/pricing, načteno 27. 10. 2026. Pilot běžel v předplatném Claude, ceny jsou přepočet na API, ne zaplacená částka.

## 1. Naměřená spotřeba pilotu po krocích (deduplikované logy Claude Code)

| krok | požadavků API | vstup | zápis cache 5 min | zápis cache 1 h | čtení cache | výstup | tokenů celkem | z toho pomocní agenti | cena API | čas |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 plán a založení | 46 | 92 | 0 | 160 373 | 4 592 252 | 57 005 | 4 809 722 | – | $3,34 | 34 min 9 s (rozpětí v logu) |
| 1 sběr kandidátů | 132 | 268 | 260 597 | 241 367 | 14 869 496 | 139 822 | 15 511 550 | 3 429 000 | $9,01 | 33 min 59 s (rozpětí v logu) |
| 2 zkušební dávka + úprava pravidel | 40 | 80 | 0 | 144 416 | 4 223 700 | 53 286 | 4 421 482 | – | $3,07 | 5 min 49 s dávka (mereni.txt) + úprava pravidel; 36 min 23 s v logu |
| 2 obohacení | 1039 | 2 138 | 2 953 720 | 267 862 | 90 698 524 | 707 018 | 94 629 262 | 79 253 923 | $49,20 | 1 h 2 min (mereni.txt) |
| 3 automatická kontrola | 22 | 44 | 0 | 141 787 | 2 206 985 | 50 361 | 2 399 177 | – | $2,58 | 8 min 8 s (rozpětí v logu) |
| 4 kontrola druhým agentem | 540 | 1 106 | 1 992 482 | 162 530 | 59 377 548 | 424 575 | 61 958 241 | 56 165 245 | $31,63 | 24 min 32 s (mereni.txt) |
| 5 příprava a uložení ruční kontroly | 36 | 72 | 0 | 479 656 | 6 834 858 | 80 219 | 7 394 805 | – | $6,81 | 27 min 33 s (rozpětí v logu) |
| 6 měření | 24 | 50 | 0 | 101 934 | 1 991 138 | 33 977 | 2 127 099 | – | $1,89 | 13 min 3 s (rozpětí v logu) |
| **celkem 0–6** | 1879 | 3 850 | 5 206 799 | 1 699 925 | 184 794 501 | 1 546 263 | 193 251 338 | | **$108** | |

Podle druhu konverzace a modelu (kroky 0–6):

| druh | model | agentů | požadavků API | tokenů celkem | cena API |
|---|---|---|---|---|---|
| hlavní konverzace | claude-opus-5-5 | – | 372 | 54 403 170 | $33,75 |
| pomocný agent | claude-opus-5-5 | 47 | 1507 | 138 848 168 | $73,78 |

Neznámé, do součtu nezahrnuto (není to nula):

- krok 05, ruční kontrola: asistence AI mimo Claude Code: README: zdroje a návrhy verdiktů zčásti od Claude a ChatGPT mimo tyto logy; spotřeba neznámá
- krok 01–06, WebFetch: zpracování stránek pomocným modelem: nástroj WebFetch předává stránku pomocnému modelu; tyto požadavky v logu nejsou
- krok 01–06, WebSearch: samostatné požadavky vyhledávání: usage.server_tool_use je ve všech záznamech 0; vyhledávání běží mimo zalogované požadavky

Webové požadavky (mereni.txt; `–` = neměřeno):

| krok | WebSearch | WebFetch | ARES | funding.tech.eu | curl | celkem |
|---|---|---|---|---|---|---|
| 0 plán a založení | – | – | – | – | – | – |
| 1 sběr kandidátů | – | – | – | – | – | – |
| 2 zkušební dávka + úprava pravidel | 9 | 20 | 11 | 11 | 0 | 51 |
| 2 obohacení | 318 | 447 | 225 | 85 | 46 | 1121 |
| 3 automatická kontrola | – | – | – | – | – | – |
| 4 kontrola druhým agentem | 34 | 5 | 0 | 0 | 406 | 445 |
| 5 příprava a uložení ruční kontroly | – | – | – | – | – | – |
| 6 měření | – | – | – | – | – | – |

## 2. Jednotkové náklady pilotu

Na kandidáta = děleno 56, na zařazený záznam = děleno 27. Cena web search je jen u kroků, kde je počet vyhledávání naměřený.

| fáze | tokenů / kandidáta | cena / kandidáta | čas / kandidáta | tokenů / zařazený | cena / zařazený | čas / zařazený |
|---|---|---|---|---|---|---|
| sběr kandidátů | 276 992 | $0,16 | 0 min 36 s | 574 502 | $0,33 | 1 min 16 s |
| obohacení | 1 689 808 | $0,94 | 1 min 7 s | 3 504 787 | $1,94 | 2 min 19 s |
| automatická kontrola | 42 842 | $0,05 | 0 min 9 s | 88 858 | $0,10 | 0 min 18 s |
| kontrola druhým agentem | 1 106 397 | $0,57 | 0 min 26 s | 2 294 750 | $1,18 | 0 min 55 s |
| ruční kontrola: podpora AI v Claude Code | 132 050 | $0,12 | 0 min 30 s | 273 882 | $0,25 | 1 min 1 s |
| režie: plán, zkušební dávka a úprava pravidel, měření | 202 827 | $0,15 | 1 min 30 s | 420 678 | $0,31 | 3 min 6 s |
| ruční kontrola: čas člověka (**modelový předpoklad, ne měření**) | – | – | 3 min 34 s–5 min 21 s | – | – | 7 min 24 s–11 min 7 s |

Ruční kontrola: 10–15 min na firmu s asistencí AI, za 20 firem 3 h 20 min až 5 h 0 min. Řádek výše to rozpočítává na všech 56 kandidátů / 27 zařazených, i když ručně bylo zkontrolováno jen 20 zařazených. Čas fází 0, 1, 3, 5, 6 je rozpětí volání v logu včetně čekání na uživatele.

## 3. Přepočet na svět

Pilotní vstupy: AI na kandidáta (sběr + obohacení + kontrola druhým agentem) $1,67, z toho obohacení $0,94; podpora AI u ruční kontroly $0,34 na kontrolovanou firmu; režie metodiky (kroky 0, 2z, 3, 6) $10,97 za jedno provedení; čas agentů 2 min 10 s na kandidáta při souběžnosti pilotu; nevyřešené a hraniční 12/56 = 21,4 % kandidátů; kandidátů na zařazený 56/27 = 2,07.

### 3.1 Parametry variant (předpoklady, ne měření)

| parametr | nízká | střední | vysoká |
|---|---|---|---|
| zařazených záznamů (PLAN.md 8.2) | 5 600 | 8 300 | 11 000 |
| násobek tokenů na kandidáta vůči ČR | 1,00 | 1,50 | 2,50 |
| násobek času člověka vůči ČR | 1,00 | 1,25 | 1,50 |
| min na firmu, ruční kontrola (základ ČR) | 10,0 | 12,5 | 15,0 |
| vrstev kontrolního vzorku | 3 | 3 | 3 |
| opakování režie metodiky | 5 | 10 | 20 |
| aktualizace: podíl tokenů obohacení | 0,20 | 0,35 | 0,50 |
| aktualizace: min na kontrolu poslední investice | 3,0 | 4,0 | 5,0 |

### 3.2 Výsledky (jednorázové sestavení + roční aktualizace)

| položka | nízká | střední | vysoká |
|---|---|---|---|
| zařazených záznamů | 5 600 | 8 300 | 11 000 |
| kandidátů (× 56/27) | 11 615 | 17 215 | 22 815 |
| AI: sběr, obohacení, kontrola druhým agentem | $19 363 | $43 049 | $95 088 |
| AI: režie metodiky | $54,87 | $110 | $219 |
| AI: podpora ruční kontroly – vzorek | $295 | $489 | $855 |
| **AI celkem, varianta s kontrolním vzorkem** | **$19 713** | **$43 648** | **$96 163** |
| AI celkem, varianta s plnou ruční kontrolou | $21 325 | $47 397 | $104 670 |
| AI na zařazený záznam (vzorek) | $3,52 | $5,26 | $8,74 |
| čas agentů při souběžnosti pilotu | 418 h | 930 h | 2 054 h |
| min člověka na firmu | 10,0 | 15,6 | 22,5 |
| ruční rozhodnutí nevyřešených a hraničních | 415 h | 961 h | 1 833 h |
| kontrolní vzorek: firem | 867 | 958 | 1 005 |
| kontrolní vzorek: hodin | 144 h | 249 h | 377 h |
| **člověk celkem, varianta se vzorkem** | **559 h** | **1 210 h** | **2 210 h** |
| plná ruční kontrola: hodin | 933 h | 2 161 h | 4 125 h |
| **člověk celkem, varianta s plnou kontrolou** | **1 348 h** | **3 122 h** | **5 958 h** |
| aktualizace: AI ročně (4× poslední investice) | $4 190 | $16 303 | $51 445 |
| aktualizace: vzorek poslední investice za čtvrtletí | 245 | 248 | 250 |
| aktualizace: člověk ročně | 49 h | 83 h | 125 h |

Kontrolní vzorek: n₀ = z²·p(1−p)/E² pro p = 0,5, E = 5 p. b., 95 % (n₀ ≈ 385), s korekcí na konečný soubor, ve všech variantách zvlášť pro VC, PE a family office. Vzorek poslední investice pro aktualizaci: p = 0,79 z pilotu.

### 3.3 Náklady v USD při sazbě 25 USD/h

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

### 3.4 Citlivost na poměr kandidátů k zařazeným

Mění se jen položky úměrné počtu kandidátů (AI sběr, obohacení, kontrola druhým agentem; ruční rozhodnutí nevyřešených). Poměr × 0,5 = 1,04 je blízko spodní meze 1.

| varianta | poměr | kandidátů | AI celkem (vzorek) | člověk celkem (vzorek) | člověk celkem (plná) |
|---|---|---|---|---|---|
| nízká | 1,04 | 5 807 | $10 032 | 352 h | 1 141 h |
| nízká | 2,07 | 11 615 | $19 713 | 559 h | 1 348 h |
| nízká | 4,15 | 23 230 | $39 077 | 974 h | 1 763 h |
| střední | 1,04 | 8 607 | $22 124 | 730 h | 2 642 h |
| střední | 2,07 | 17 215 | $43 648 | 1 210 h | 3 122 h |
| střední | 4,15 | 34 430 | $86 697 | 2 171 h | 4 083 h |
| vysoká | 1,04 | 11 407 | $48 619 | 1 294 h | 5 042 h |
| vysoká | 2,07 | 22 815 | $96 163 | 2 210 h | 5 958 h |
| vysoká | 4,15 | 45 630 | $191 252 | 4 044 h | 7 792 h |
