# Měření přesnosti na vzorku 20 firem

Vygenerováno skriptem `scripts/mereni.py` z `data/hodnoceni.csv`. Nepřepisovat ručně.

## Co čísla znamenají a co ne

- Ručně byl ověřen náhodný výběr 20 z 27 zařazených (seed 20261027, `scripts/vyber_vzorku.py`, `data/vzorek_kontroly.csv`), s asistencí AI (README, „Ruční kontrola – kdo hodnotil“). Výsledky platí pro zařazené, ne pro všech 56 kandidátů. Nevyřešené a vyřazené kandidáty nikdo ručně nekontroloval, recall ze vzorku spočítat nejde.
- `nelze_overit` není potvrzená chyba, vykazuje se zvlášť jako nedostatečný důkaz.
- Konečná `ne` jsou rozdělená do skupin `chyba_vystupu` (skutečná chyba agenta), `upresneni_metodiky` (výklad upřesněný až při ruční kontrole) a `omezeni_schematu` (schéma hodnotu neumí zapsat). Zařazení do skupin je v tabulce `SKUPINA_NE` ve skriptu.
- Wilsonův interval předpokládá nezávislá pozorování. Řádky po polích jsou seskupené po firmách, takže souhrnný interval přes všechna pole je optimistický. Interval je bez korekce na konečný soubor (20 z 27), v tomto ohledu je spíš konzervativní.
- Přesnost = ano/(ano+ne), dolní mez = ano/(ano+ne+nelze_overit), tj. jako by každé `nelze_overit` bylo chybou.

## 1. Zařazení investorů (jednotka = firma, 20 firem)

Pole: existence, investicni_cinnost, je_investor, typ, rozsah_pilotu. Aspoň jedno `ne` → chybně zařazen; jinak aspoň jedno `nelze_overit` → neověřeno; jinak správně.

- správně 15, chybně 2, neověřeno 3

| firma | stav | pole `ne` (skupina) | pole `nelze_overit` |
|---|---|---|---|
| cz-ii-biotech-investments | chybne | rozsah_pilotu (upresneni_metodiky) | – |
| cz-ii-prague | neovereno | – | je_investor |
| cz-n1-ventures | chybne | rozsah_pilotu (upresneni_metodiky) | existence |
| cz-presto-ventures | neovereno | – | investicni_cinnost, je_investor |
| cz-tensor-ventures | neovereno | – | rozsah_pilotu |

a) Všechna `ne`:

- přesnost správně/(správně+chybně): 15/17 = 88,2 % (95% CI 65,7 %–96,7 %)
- dolní mez správně/20: 15/20 = 75,0 % (95% CI 53,1 %–88,8 %)

b) Jen vůči chybám výstupu: firmy, jejichž chybné zařazení je jen `upresneni_metodiky` (cz-ii-biotech-investments, cz-n1-ventures), jsou z jmenovatele vynechané, nepočítají se jako správné.

- správnost mezi 15 rozhodnutelnými případy po vyloučení 2 změn metodiky: 15/15 = 100,0 % (95% CI 79,6 %–100,0 %); vedle toho 3 neověřené (cz-ii-prague, cz-presto-ventures, cz-tensor-ventures). Nejde o 100% ověřenou databázi.
- dolní mez, jmenovatel 18: 15/18 = 83,3 % (95% CI 60,8 %–94,2 %)

## 2. Správnost vyplněných polí (jednotka = řádek id/pole)

`jen úplnost` = pole agent nevyplnil, do přesnosti nevstupuje (oddíl 3).

| pole | ano | ne: chyba_vystupu | ne: upresneni_metodiky | ne: omezeni_schematu | nelze_overit | jen úplnost | přesnost ano/(ano+ne) | dolní mez ano/(ano+ne+nelze) |
|---|---|---|---|---|---|---|---|---|
| existence | 19 | 0 | 0 | 0 | 1 | 0 | 19/19 = 100,0 % (95% CI 83,2 %–100,0 %) | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %) |
| investicni_cinnost | 19 | 0 | 0 | 0 | 1 | 0 | 19/19 = 100,0 % (95% CI 83,2 %–100,0 %) | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %) |
| je_investor | 18 | 0 | 0 | 0 | 2 | 0 | 18/18 = 100,0 % (95% CI 82,4 %–100,0 %) | 18/20 = 90,0 % (95% CI 69,9 %–97,2 %) |
| typ | 20 | 0 | 0 | 0 | 0 | 0 | 20/20 = 100,0 % (95% CI 83,9 %–100,0 %) | 20/20 = 100,0 % (95% CI 83,9 %–100,0 %) |
| rozsah_pilotu | 17 | 0 | 2 | 0 | 1 | 0 | 17/19 = 89,5 % (95% CI 68,6 %–97,1 %) | 17/20 = 85,0 % (95% CI 64,0 %–94,8 %) |
| posledni_investice | 15 | 4 | 0 | 0 | 1 | 0 | 15/19 = 78,9 % (95% CI 56,7 %–91,5 %) | 15/20 = 75,0 % (95% CI 53,1 %–88,8 %) |
| nezavislost_zdroju | 14 | 0 | 0 | 0 | 6 | 0 | 14/14 = 100,0 % (95% CI 78,5 %–100,0 %) | 14/20 = 70,0 % (95% CI 48,1 %–85,5 %) |
| sektory | 16 | 0 | 0 | 0 | 0 | 4 | 16/16 = 100,0 % (95% CI 80,6 %–100,0 %) | 16/16 = 100,0 % (95% CI 80,6 %–100,0 %) |
| ticket | 10 | 0 | 0 | 1 | 0 | 9 | 10/11 = 90,9 % (95% CI 62,3 %–98,4 %) | 10/11 = 90,9 % (95% CI 62,3 %–98,4 %) |
| kapital | 8 | 0 | 0 | 0 | 0 | 12 | 8/8 = 100,0 % (95% CI 67,6 %–100,0 %) | 8/8 = 100,0 % (95% CI 67,6 %–100,0 %) |
| **celkem** | 156 | 4 | 2 | 1 | 12 | 25 | 156/163 = 95,7 % (95% CI 91,4 %–97,9 %) | 156/175 = 89,1 % (95% CI 83,7 %–92,9 %) |

Varianta jen vůči chybám výstupu: řádky `upresneni_metodiky` a `omezeni_schematu` (3) jsou z jmenovatele vynechané.

| pole | jmenovatel přesnosti | přesnost | jmenovatel dolní meze | dolní mez |
|---|---|---|---|---|
| existence | 19 | 19/19 = 100,0 % (95% CI 83,2 %–100,0 %) | 20 | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %) |
| investicni_cinnost | 19 | 19/19 = 100,0 % (95% CI 83,2 %–100,0 %) | 20 | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %) |
| je_investor | 18 | 18/18 = 100,0 % (95% CI 82,4 %–100,0 %) | 20 | 18/20 = 90,0 % (95% CI 69,9 %–97,2 %) |
| typ | 20 | 20/20 = 100,0 % (95% CI 83,9 %–100,0 %) | 20 | 20/20 = 100,0 % (95% CI 83,9 %–100,0 %) |
| rozsah_pilotu | 17 | 17/17 = 100,0 % (95% CI 81,6 %–100,0 %) | 18 | 17/18 = 94,4 % (95% CI 74,2 %–99,0 %) |
| posledni_investice | 19 | 15/19 = 78,9 % (95% CI 56,7 %–91,5 %) | 20 | 15/20 = 75,0 % (95% CI 53,1 %–88,8 %) |
| nezavislost_zdroju | 14 | 14/14 = 100,0 % (95% CI 78,5 %–100,0 %) | 20 | 14/20 = 70,0 % (95% CI 48,1 %–85,5 %) |
| sektory | 16 | 16/16 = 100,0 % (95% CI 80,6 %–100,0 %) | 16 | 16/16 = 100,0 % (95% CI 80,6 %–100,0 %) |
| ticket | 10 | 10/10 = 100,0 % (95% CI 72,2 %–100,0 %) | 10 | 10/10 = 100,0 % (95% CI 72,2 %–100,0 %) |
| kapital | 8 | 8/8 = 100,0 % (95% CI 67,6 %–100,0 %) | 8 | 8/8 = 100,0 % (95% CI 67,6 %–100,0 %) |
| **celkem** | 160 | 156/160 = 97,5 % (95% CI 93,7 %–99,0 %) | 172 | 156/172 = 90,7 % (95% CI 85,4 %–94,2 %) |

### Kontrola sloučení (samostatně)

Řádků: 1. Do přesnosti polí výše nevstupuje.

- cz-nation1 → cz-n1-ventures: ano (CzechCrunch 18. 9. 2023: „Přejmenovává se na N1“, stejní managing partneři)

## 3. Úplnost (sektory, ticket, kapitál)

Potvrzené chybění = údaj ve zdroji existuje, agent ho nezapsal.

| pole | vyplněno z 20 | podíl vyplněných | potvrzené chybění |
|---|---|---|---|
| sektory | 16 | 16/20 = 80,0 % (95% CI 58,4 %–91,9 %) | 0 |
| ticket | 11 | 11/20 = 55,0 % (95% CI 34,2 %–74,2 %) | 1 (cz-n1-ventures) |
| kapital | 8 | 8/20 = 40,0 % (95% CI 21,9 %–61,3 %) | 0 |

## 4. Všechna `ne` a `nelze_overit`

| id | pole | skupina | příčina | poznámka (zkráceno) |
|---|---|---|---|---|
| cz-n1-ventures | rozsah_pilotu | upresneni_metodiky | chyba_pravidel | Upřesnění metodiky při ruční kontrole, ne jednoznačná chyba agenta: správci (GP/AIFM) v Lucembursku, v Praze tým |
| cz-ii-biotech-investments | rozsah_pilotu | upresneni_metodiky | chyba_pravidel | Upřesnění metodiky při ruční kontrole: fond i&i Biotech Fund I SCSp v Lucembursku („Luxemburg-based“), česká Biotech Investments s.r.o. je poradce a tým |
| cz-ii-biotech-investments | ticket | omezeni_schematu | chyba_pravidel | Web rozlišuje dva intervaly: od 150 tis. EUR při zakládání firmy a preferovaně 0,5–2 mil. EUR při růstu. Záznam je spojil do jednoho 150 tis.–2 mil.; schéma dv… |
| cz-zaka-vc | posledni_investice | chyba_vystupu | chybne_pouziti_pravidla (agent odmítl přípustný zdroj) | ParcelBio (7. 5. 2026) samotný sedí, ale není nejnovější doložená investice: zaka.vc/news 16. 7. 2026 „we’re excited to announce our investment in FinalDose“ –… |
| cz-look-ai-ventures | posledni_investice | chyba_vystupu | neurčeno | Přehlédnuta novější investice na webu investora: „Look AI Ventures Backs Embodied AI“ 22. 9. 2026 (https://lookai.vc/look-ai-ventures-backs-embodied-ai-robots-… |
| cz-purple-ventures | posledni_investice | chyba_vystupu | neurčeno | Comparables.ai (6. 10. 2026) samotný sedí, ale není nejnovější doložená investice: FLÆ Robotics seed, „The funding round included participation from Purple Ven… |
| cz-reflex-capital | posledni_investice | chyba_vystupu | neurčeno | Grid.online (22. 6. 2026) samotný sedí, ale není nejnovější doložená investice: ArtMaster, CzechCrunch 21. 10. 2026, „K dřívějším investorům se nově přidávají … |

Příčina `neurčeno`: z logu nejde doložit, zda agent zdroj viděl. U `upresneni_metodiky` a `omezeni_schematu` je `chyba_pravidel` hodnota z CSV, význam určuje skupina.

| id | pole | poznámka (zkráceno) |
|---|---|---|
| cz-n1-ventures | existence | Značka doložena (web, CVCA, CzechCrunch), právní subjekty Nation 1 GP S.à r.l. a GP II neověřeny v registru |
| cz-tensor-ventures | rozsah_pilotu | Web: Tensor Ventures GP S.à r.l. a Fund I SCSp v Lucembursku; správce druhého fondu (EIF) nedoložen |
| cz-tensor-ventures | nezavislost_zdroju | ValkaAI: Seznam Zprávy a Startbase (oba 24. 2. 2026, puvod null). Původ zdrojů nedoložen: agent má u zdrojů puvod null (vedené jako nezávislé), ale sám v pozná… |
| cz-ii-biotech-investments | nezavislost_zdroju | Theorema: Lupa.cz, CzechCrunch, Vestbee (puvod null). Původ zdrojů nedoložen: agent má u zdrojů puvod null (vedené jako nezávislé), ale sám v poznámce uvádí, ž… |
| cz-ii-prague | je_investor | Nástroj u kola 2025 nedoložen (kolo bez označení fáze). Agentem uvedený doklad z rejstříku dokládá i&i Prague jako jediného akcionáře jen 18. 11.–15. 12. 2020 … |
| cz-look-ai-ventures | nezavislost_zdroju | Lucida AI: tech.eu a Lupa.cz (oba 30. 6. 2026, puvod null). Původ zdrojů nedoložen: agent má u zdrojů puvod null (vedené jako nezávislé), ale sám v poznámce uv… |
| cz-purple-ventures | nezavislost_zdroju | Comparables.ai: tech.eu 6. 10. 2026 a Lupa.cz 13. 10. 2026 (puvod null; Lupa cituje Jana Staňka a má fotografii od Purple, to je indicie, ne důkaz). Původ zdro… |
| cz-y-soft-ventures | nezavislost_zdroju | RoboTwin: EIT Jumpstarter, CzechCrunch, The Recycler (puvod null; CzechCrunch „Letos již hlásili“ odkazuje na dřívější oznámení, to je indicie, ne důkaz). Půvo… |
| cz-miton | nezavislost_zdroju | ACE: CzechCrunch a blog Mitonu (oba 1. 10. 2026, puvod null). Původ zdrojů nedoložen: agent má u zdrojů puvod null (vedené jako nezávislé), ale sám v poznámce … |
| cz-presto-ventures | investicni_cinnost | Přiřazení uvedených investic k Prestu nedoloženo. Investice SatVu a Occam provedl fond (Presto) Tech Horizons – Tech Horizons SCSp, Lucembursko, správce Tech H… |
| cz-presto-ventures | je_investor | Podle dosud prověřených transakcí nelze ověřit; viz investicni_cinnost. |
| cz-presto-ventures | posledni_investice | SatVu 18. 2. 2026: přiřazení k Prestu nedoloženo (viz investicni_cinnost). |

## 5. Srovnání s kontrolním agentem (fáze A, jen 20 firem vzorku)

Konečné hodnocení vzniklo s asistencí AI a část změn až po přečtení nálezů kontrolního agenta, takže není nezávislý referenční standard. Srovnání popisuje shodu s konečným hodnocením a změny po přečtení nálezů, ne nezávisle změřenou přesnost kontrolního agenta. Počítají se unikátní dvojice id/pole, ne řádky agenta (`kapital[0]`, `kapital[1]` … jsou jedna dvojice). „Tutéž vadu“ = nález agenta se týká téže vady jako konečné hodnocení. Jde o interpretační přiřazení provedené AI porovnáním textů (tabulka `ZACHYCENI` ve skriptu), ne o automaticky ani nezávisle ověřenou skutečnost; upozornění na jinou část pole se nepočítá.

Mapování: pravni_subjekt→existence, investicni_cinnost→investicni_cinnost, typ→typ, sidlo→rozsah_pilotu, posledni_investice→posledni_investice, sektory→sektory, ticket→ticket, kapital[*]→kapital, slouceni→slouceni (plně srovnatelná); nastroj→je_investor, jistota_investice→nezavislost_zdroju (částečná).

### 5.1 Plně srovnatelná pole

Unikátních dvojic id/pole: 161, s aspoň jedním řádkem agenta: 136, označených (`zaver` ≠ `sedi`): 13.

| konečné hodnocení | dvojic | agent označil | z toho tutéž vadu | agent neoznačil |
|---|---|---|---|---|
| Konečné `ne` – chyba_vystupu | 4 | 4 | 4 | 0 |
| Konečné `ne` – upresneni_metodiky | 2 | 2 | 2 | 0 |
| Konečné `ne` – omezeni_schematu | 1 | 0 | 0 | 1 |
| Konečné `nelze_overit` | 4 | 2 | 2 | 2 |
| Označení agenta, která konečné hodnocení nepotvrdilo (konečně `ano`) | 5 | 5 | – | – |

Podrobnosti ke všem dvojicím s konečným `ne` / `nelze_overit` nebo s označením agenta:

| id | pole | konečně | tutéž vadu | nálezy agenta (zkráceno) |
|---|---|---|---|---|
| cz-ii-biotech-investments | rozsah_pilotu | ne (upresneni_metodiky) | ano – obojí: lucemburský fond, česká s.r.o. jen poradce | sidlo: podezreni – Investor se sám popisuje jako lucemburský: „i&i Bio is a Luxembourg-based venture capital firm“ (web, novinky) a „Headq… |
| cz-ii-biotech-investments | ticket | ne (omezeni_schematu) | – | vše `sedi` |
| cz-look-ai-ventures | existence | ano | – | pravni_subjekt: potvrzeny_rozpor – Identita sedí: ARES „Look AI Ventures SICAV, a.s.“, IČO 17604087, Radlická 180/50, Praha 5, statutární orgán AVANT inve… |
| cz-look-ai-ventures | posledni_investice | ne (chyba_vystupu) | ano – obojí: novější investice Embodied AI 22. 9. 2026 | posledni_investice: potvrzeny_rozpor – Údaje o Sodex sedí (tech.eu „13 July 2026“: „The round also welcomed new investors Bloomhaus, Look AI Ventures and … Su… |
| cz-n1-ventures | existence | nelze_overit | ano – obojí: GP v Lucembursku neověřeni v registru | pravni_subjekt: nedostatecny_dukaz – n1.rocks/disclosure: „Nation 1 GP S.à r.l and Nation 1 GP II S.à r.l. (the “GPs”), as general partner and registered al… |
| cz-n1-ventures | rozsah_pilotu | ne (upresneni_metodiky) | ano – obojí: lucemburští správci (GP/AIFM) | sidlo: podezreni – Web uvádí tři kanceláře: „415 Mission St, San Francisco, CA“, „Národní 135/14, Prague 1“, „Luxembourg 1A, Heienhaff, L-… |
| cz-presto-ventures | investicni_cinnost | nelze_overit | – | vše `sedi` |
| cz-presto-ventures | posledni_investice | nelze_overit | – | vše `sedi` |
| cz-purple-ventures | posledni_investice | ne (chyba_vystupu) | ano – obojí: novější FLÆ Robotics 14. 10. 2026 | posledni_investice: potvrzeny_rozpor – Comparables.ai (Tech.eu 6. 10. 2026 „with participation from Purple Ventures“, Lupa 13. 10. 2026 „Český fond Purple Ven… |
| cz-reflex-capital | posledni_investice | ne (chyba_vystupu) | ano – obojí: novější ArtMaster 21. 10. 2026 | posledni_investice: potvrzeny_rozpor – Grid.online (CC a E15 22. 6. 2026) je doložená, ale není nejnovější doložená investice: CzechCrunch 21. 10. 2026 (ArtMa… |
| cz-startupyard | existence | ano | – | pravni_subjekt: podezreni – ARES: StartupYard Services s.r.o., IČO 06002820, Perlová 371/5, Praha 1, jednatel Nikola Rafaj, jediný společník Startu… |
| cz-startupyard | typ | ano | – | typ: podezreni – Subjekt se sám označuje jako akcelerátor („Accelerating Startups Since 2011“), funding.tech.eu typ „Accelerator“. Batch… |
| cz-tensor-ventures | rozsah_pilotu | nelze_overit | ano – obojí: lucemburský GP, sídlo správce sporné | sidlo: podezreni – Web uvádí jako adresu „Tensor Ventures GP S.à r.l. & Tensor Ventures Fund I SCSp, 1A Heienhaff, 1736 Senningerberg, Lux… |
| cz-zaka-vc | existence | ano | – | pravni_subjekt: podezreni – ARES: ZAKA Management s.r.o. (dříve ZAKA VC I s.r.o.), IČO 21053987, Italská 2581/67, Praha 2, jednatelé Samuel Zálešák… |
| cz-zaka-vc | posledni_investice | ne (chyba_vystupu) | ano – obojí: novější FinalDose 16. 7. 2026 na zaka.vc/news | posledni_investice: podezreni – ParcelBio 2026-05-07 sedí (TZ Business Wire přes BioSpace). Ale stránka novinek ZAKA uvádí novější oznámení investic: 1… |
| cz-zaka-vc | typ | ano | – | typ: podezreni – Web: „We are a seed & pre-seed VC fund“; CzechCrunch 22. 7. 2024: „se mění z rodinného na klasický startupový fond“, „p… |

### 5.2 Částečná mapování (nastroj→je_investor, jistota_investice→nezavislost_zdroju)

Unikátních dvojic id/pole: 40, s aspoň jedním řádkem agenta: 40, označených (`zaver` ≠ `sedi`): 2.

| konečné hodnocení | dvojic | agent označil | z toho tutéž vadu | agent neoznačil |
|---|---|---|---|---|
| Konečné `ne` – chyba_vystupu | 0 | 0 | 0 | 0 |
| Konečné `ne` – upresneni_metodiky | 0 | 0 | 0 | 0 |
| Konečné `ne` – omezeni_schematu | 0 | 0 | 0 | 0 |
| Konečné `nelze_overit` | 8 | 1 | 1 | 7 |
| Označení agenta, která konečné hodnocení nepotvrdilo (konečně `ano`) | 1 | 1 | – | – |

Podrobnosti ke všem dvojicím s konečným `ne` / `nelze_overit` nebo s označením agenta:

| id | pole | konečně | tutéž vadu | nálezy agenta (zkráceno) |
|---|---|---|---|---|
| cz-ii-biotech-investments | nezavislost_zdroju | nelze_overit | – | vše `sedi` |
| cz-ii-prague | je_investor | nelze_overit | – | vše `sedi` |
| cz-look-ai-ventures | nezavislost_zdroju | nelze_overit | – | vše `sedi` |
| cz-miton | nezavislost_zdroju | nelze_overit | – | vše `sedi` |
| cz-presto-ventures | je_investor | nelze_overit | – | vše `sedi` |
| cz-purple-ventures | nezavislost_zdroju | nelze_overit | – | vše `sedi` |
| cz-soulmates-ventures | je_investor | ano | – | nastroj: nedostatecny_dukaz – Poslední investice: kolo „seed“ je převzato jen z titulku/štítku UKTN („£500,000 Seed investment“); text TZ i Vestbee a… |
| cz-tensor-ventures | nezavislost_zdroju | nelze_overit | – | vše `sedi` |
| cz-y-soft-ventures | nezavislost_zdroju | nelze_overit | ano – obojí: puvod null u zpráv, nezávislost nedoložena | jistota_investice: podezreni – Agent dal stredni s odůvodněním, že nezávislost nedoložena, ale u všech tří zpráv (EIT Jumpstarter, CzechCrunch, The Re… |

### 5.3 Nezmapovaná pole agenta

| pole agenta | řádků ve vzorku | z toho `zaver` ≠ `sedi` |
|---|---|---|
| web | 20 | 0 |
| faze | 17 | 0 |
| status | 20 | 0 |
| dalsi_investice | 17 | 0 |

### 5.4 Před a po přečtení nálezů AI

Porovnání `data/hodnoceni.csv` se stavem před přečtením nálezů (`ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv`), 10 polí 20 firem.

| | počet | dvojice |
|---|---|---|
| konečné `ne` nalezené už před přečtením nálezů AI | 4 | cz-n1-ventures/rozsah_pilotu (upresneni_metodiky), cz-ii-biotech-investments/rozsah_pilotu (upresneni_metodiky), cz-ii-biotech-investments/ticket (omezeni_schematu), cz-look-ai-ventures/posledni_investice (chyba_vystupu) |
| konečné `ne` nalezené až po nich | 3 | cz-zaka-vc/posledni_investice (chyba_vystupu), cz-purple-ventures/posledni_investice (chyba_vystupu), cz-reflex-capital/posledni_investice (chyba_vystupu) |
| konečné `nelze_overit`, už před přečtením | 6 | cz-n1-ventures/existence, cz-tensor-ventures/rozsah_pilotu, cz-ii-prague/je_investor, cz-presto-ventures/investicni_cinnost, cz-presto-ventures/je_investor, cz-presto-ventures/posledni_investice |
| změna `ano` → `nelze_overit` po přečtení | 6 | cz-tensor-ventures/nezavislost_zdroju, cz-ii-biotech-investments/nezavislost_zdroju, cz-look-ai-ventures/nezavislost_zdroju, cz-purple-ventures/nezavislost_zdroju, cz-y-soft-ventures/nezavislost_zdroju, cz-miton/nezavislost_zdroju |
| jiné změny verdiktu | 0 | – |
