# Přehled změn opravené verze (krok 8, oprava hodnocení i&i Prague v kroku 9)

Vygenerováno skriptem `scripts/oprav.py` z `data/vystup_agenta/` a `data/hodnoceni.csv`. Nepřepisovat ručně. Původní výstup agenta, hodnocení i měření zůstávají beze změny.

**Přesnost byla měřena na původním výstupu agenta** (`data/mereni_vzorku.md`). Opravená verze nemá nové nezávislé měření přesnosti: opravy vycházejí ze stejného hodnocení, takže čísla z měření na ni nejde přenést ani je přepočítat.

## Počty

| soubor | původně | opraveno | změna |
|---|---|---|---|
| investori.json | 27 | 23 | -4 |
| vyrazeni.csv | 17 | 19 | +2 |
| hranicni.csv | 1 | 1 | +0 |
| nevyresene.csv | 11 | 13 | +2 |
| **celkem výsledných id** | 56 | 56 | |

Stav kontroly zařazených (`stav_kontroly.csv`, sloupec `vysledek`):

- `s_opravou`: 4
- `hodnocena_pole_ano`: 10
- `s_vyhradou_nelze_overit`: 2
- `nehodnoceno`: 7

## Rozsah dokončené kontroly

- Ručně (s asistencí AI, README „Ruční kontrola – kdo hodnotil“) byl ohodnocen náhodný výběr 20 z 27 zařazených (seed 20261027, `data/vzorek_kontroly.csv`), deset polí na firmu, a sloučení Nation1 → N1.
- Sedm zařazených mimo vzorek a všech 29 vyřazených, hraničních a nevyřešených kandidátů z výstupu agenta ručně kontrolováno nebylo. V opravené verzi zůstávají obsahově beze změny.
- `hodnocena_pole_ano` znamená, že všechna hodnocená pole dostala `ano` v hodnocení s asistencí AI. Neznamená potvrzení všech údajů: nevyplněná pole se hodnotila jen z hlediska úplnosti a u poslední investice jde o nejnovější doloženou, ne o záruku úplnosti.
- Stav kontroly, neověřená pole a výhrady každého výsledného id jsou v `stav_kontroly.csv`. Do `investori.json` se nové pole nepřidává, schéma zůstává podle PLAN.md bod 4.

## Přesuny

Původní úplný záznam každého přesunutého id zůstává v `data/vystup_agenta/investori.json` (stejné id). Řádek v novém souboru na něj odkazuje ve sloupci `duvod`.

| id | původní stav | nový stav | důvod | důkaz (hodnoceni.csv) | URL |
|---|---|---|---|---|---|
| cz-n1-ventures | investori.json, zařazen | vyrazeni.csv, mimo_rozsah_pilotu | sídlo správce mimo ČR (GP v Lucembursku); skutečný investor, ne neinvestor | ř. 6 (cz-n1-ventures, rozsah_pilotu); dále ř. 3, ř. 4, ř. 2, ř. 10 | https://n1.rocks/disclosure<br>https://www.thevccorner.com/p/novoflow-ai-healthcare-startup<br>https://n1.rocks/ |
| cz-ii-biotech-investments | investori.json, zařazen | vyrazeni.csv, mimo_rozsah_pilotu | fond se sídlem v Lucembursku, česká s.r.o. je poradce a tým; skutečný investor, ne neinvestor | ř. 37 (cz-ii-biotech-investments, rozsah_pilotu); dále ř. 34, ř. 35, ř. 41, ř. 39 | https://www.inibio.eu/<br>https://www.lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-urychlily-vedecky-vyzkum-a-vyvoj/ |
| cz-tensor-ventures | investori.json, zařazen | nevyresene.csv, otazka sidlo | sídlo správce neověřené, pravidla pilotu vyžadují správce v ČR | ř. 17 (cz-tensor-ventures, rozsah_pilotu); dále ř. 13, ř. 14, ř. 15, ř. 19 | https://tensor.ventures/<br>https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06257241 |
| cz-presto-ventures | investori.json, zařazen | nevyresene.csv, otazka investice | přiřazení investic v okně k Prestu nedoložené (ne vyvrácené) | ř. 293 (cz-presto-ventures, investicni_cinnost); dále ř. 294, ř. 297, ř. 292, ř. 296 | https://pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-scale-multi-satellite-constellation/amp/<br>https://csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthening-space-and-thermal-intelligence-capabilities<br>https://techhorizons.eu/<br>https://www.prestoventures.com/ |

U Presta chybí důkaz o přiřazení investice. Chybějící důkaz neznamená, že subjekt není investor; čeká na ruční rozhodnutí v `nevyresene.csv`.

i&i Prague zůstává zařazená (oprava hodnocení v kroku 9, hodnoceni.csv ř. 65): uložený výpis ARES CasInvent (`ai-log/02-obohaceni/zdroje/ares_vr_09684221.json`) uvádí konvertibilní zápůjčku z 4. 3. 2025, nabídku 48 akcií třídy C i&i Prague (valná hromada 22. 5. 2025) a zapsané splacené zvýšení kapitálu k 30. 5. 2025. Upsání je doloženo nepřímo, smlouva o úpisu přímo ověřena není. Původní stav (je_investor = nelze_overit, přesun do `nevyresene.csv` s otázkou `nastroj`) je v `ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv` a v historii gitu (commit 0641e6a).

## Opravy poslední investice

Původní poslední investice je přesunutá na začátek `dalsi_investice` beze změny. `datum_investice` zůstává `null` (zdroje datum transakce jednoznačně neuvádějí), `datum_pro_filtr` = `oznameni`. Status je přepočítaný podle PLAN.md bod 2 k referenčnímu datu 2026-10-26. `jistota` se nemění (nová investice má jednu zprávu o transakci nebo zprávy s nedoloženou nezávislostí).

| id | původní stav | nový stav | kolo × vklad | doklad data | důkaz (hodnoceni.csv) | URL |
|---|---|---|---|---|---|---|
| cz-look-ai-ventures | Sodex Innovations, oznámení 2026-07-13, status aktivni | Embodied AI, oznámení 2026-09-22, datum_investice null, nástroj nezjisteno, kolo null, status aktivni | velikost kola ani vklad Look AI neuvedeny (Pulse 2.0: „did not disclose the size of the round“) | hlavička článku „Eva Slonkova / September 22, 2026“, metadata article:published_time 2026-09-22T23:59:13+00:00 | ř. 127 (cz-look-ai-ventures, posledni_investice) | https://lookai.vc/look-ai-ventures-backs-embodied-ai-robots-manufacturing/ |
| cz-purple-ventures | Comparables.ai, oznámení 2026-10-06, status aktivni | FLÆ Robotics, oznámení 2026-10-15, datum_investice null, nástroj neprima_indicie, kolo seed, status aktivni | seed přes 1 mil. EUR je velikost celého kola, vklad Purple neuveden | metadata stránky datePublished / article:published_time 2026-10-15T06:28:15Z; na stránce zobrazeno „Updated October 14, 2026“ a pole agregátoru „Funding Date: October 14, 2026“; Nordic9 uvádí 12. 10. 2026 | ř. 147 (cz-purple-ventures, posledni_investice) | https://www.thesaasnews.com/news/fl-robotics-raises-1m-seed/ |
| cz-reflex-capital | Grid.online, oznámení 2026-06-22, status aktivni | ArtMaster, oznámení 2026-10-21, datum_investice null, nástroj nezjisteno, kolo null, status aktivni | 2,4 mil. USD je velikost celého kola, vklad Reflexu neuveden | metadata stránky datePublished 2026-10-21T09:00:39+02:00 | ř. 157 (cz-reflex-capital, posledni_investice) | https://cc.cz/kdysi-si-v-amsterdamske-red-light-district-vydelaval-hranim-dnes-uz-diky-ai-uci-na-piano-stovky-tisic-lidi/ |
| cz-zaka-vc | ParcelBio, oznámení 2026-05-07, status aktivni | FinalDose, oznámení 2026-07-16, datum_investice null, nástroj nezjisteno, kolo null, status aktivni | velikost kola, vklad ZAKA ani kolo podklady ruční kontroly neuvádějí | datum 16. 7. 2026 podle hodnocení a kontrolního agenta (fáze A, 26. 10. 2026); v kroku 8 stránka vrátila HTTP 466 a znovu načtena nebyla | ř. 48 (cz-zaka-vc, posledni_investice) | https://zaka.vc/news/ |

### Změny v `poznamka`

Části poznámky, které popisovaly původní poslední investici jako nejnovější, by opraveným hodnotám odporovaly. Jsou nahrazené, ostatní text poznámky je beze změny. Původní znění je v `data/vystup_agenta/investori.json`.

- **cz-look-ai-ventures**:
  - „Poslední investice: Sodex Innovations, tech.eu 13. 7. 2026:“ → „Poslední doložená investice (oprava po ruční kontrole, krok 8): Embodied AI (Lausanne), tisková zpráva investora na lookai.vc s datem publikace 22. 9. 2026 v hlavičce článku: 'Look AI Ventures has backed Embodied AI ... The round was led by Faber VC'; velikost kola ani vklad Look AI neuvedeny, kolo neoznačeno, nástroj nezjištěn. Výhrada: Pulse 2.0 už 16. 9. 2026 jmenoval Look AI Ventures mezi investory, první veřejné oznámení tedy může být starší než datum_oznameni. Další: Sodex Innovations, tech.eu 13. 7. 2026:“
  - „Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.“ → „Poslední investice je nejnovější doložená investice podle ruční kontroly, ne záruka úplnosti.“
- **cz-purple-ventures**:
  - „Poslední investice: Comparables.ai (Finsko)“ → „Poslední doložená investice (oprava po ruční kontrole, krok 8): FLÆ Robotics, seed přes 1 mil. EUR (velikost celého kola, vklad Purple neuveden), TheSaaSNews s časem publikace 15. 10. 2026 v metadatech stránky, zdrojem článku je EU-Startups: 'The funding round included participation from Purple Ventures and Garage Angels'. Nástroj neprima_indicie (seed). Datum investice zdroj jednoznačně neurčuje, proto null. Výhrada: pole agregátoru 'Funding Date: October 14, 2026' a zobrazené 'Updated October 14, 2026' se s časem publikace rozcházejí, Nordic9 uvádí 12. 10. 2026 a původní zprávu EU-Startups jsem nečetl, první oznámení tedy může být starší než datum_oznameni. Další: Comparables.ai (Finsko)“
  - „Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.“ → „Poslední investice je nejnovější doložená investice podle ruční kontroly, ne záruka úplnosti.“
- **cz-reflex-capital**:
  - „Poslední investice: Grid.online, CzechCrunch 22. 6. 2026:“ → „Poslední doložená investice (oprava po ruční kontrole, krok 8): ArtMaster, CzechCrunch 21. 10. 2026: 'Teď ArtMaster uzavřel investici ve výši 2,4 milionu dolarů ... K dřívějším investorům se nově přidávají fondy Factorial Capital a český Reflex Capital'; 2,4 mil. USD je velikost celého kola, vklad Reflexu neuveden, kolo zdroj neoznačuje, nástroj nezjištěn (Nordic9 kolo označuje jako seed, nepřevzato). Datum uzavření neuvedeno. Další: Grid.online, CzechCrunch 22. 6. 2026:“
  - „Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.“ → „Poslední investice je nejnovější doložená investice podle ruční kontroly, ne záruka úplnosti.“
- **cz-zaka-vc**:
  - „Poslední investice: ParcelBio, seed 13 mil. USD“ → „Poslední doložená investice (oprava po ruční kontrole, krok 8): FinalDose, oznámení investora na zaka.vc/news 16. 7. 2026 ('we’re excited to announce our investment in FinalDose'); vlastní oznámení investora je podle PLAN.md bod 2 přípustná zpráva o transakci. Velikost kola, vklad ZAKA ani kolo podklady ruční kontroly neuvádějí, nástroj nezjištěn. Výhrada: stránka novinek uvádí i PerfectBit (tisková zpráva 18. 8. 2026, PitchBook podle vyhledávání seed 26. 6. 2026), ruční kontrola ho neposoudila, nezapsáno. Další: ParcelBio, seed 13 mil. USD“
  - „Web a stránka novinek uvádějí i další investice z let 2025–2026 (Cirrus Therapeutics, DeepSeq.AI, FinalDose aj.), ty jsem nezávislou zprávou o transakci neověřil.“ → „Web a stránka novinek uvádějí i další investice z let 2025–2026 (Cirrus Therapeutics, DeepSeq.AI, PerfectBit aj.), ty ověřené nejsou; FinalDose doložila ruční kontrola (viz poslední investice).“
  - „Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.“ → „Poslední investice je nejnovější doložená investice podle ruční kontroly, ne záruka úplnosti.“

## Opravy zaznamenané jen v přehledu (záznam je mimo pilot)

| id | pole | původně | doložená hodnota | důkaz (hodnoceni.csv) | URL |
|---|---|---|---|---|---|
| cz-n1-ventures | ticket | null (agent ticket nezapsal) | web n1.rocks: „Typical 1st investment $100K–$1M“ (100 000–1 000 000 USD, první investice) | ř. 10 (cz-n1-ventures, ticket) | https://n1.rocks/ |
| cz-ii-biotech-investments | ticket | min 150 000, max 2 000 000 EUR (jeden spojený interval) | dva intervaly: od 150 000 EUR při zakládání firmy (business creation) a preferovaně 500 000–2 000 000 EUR při růstu; schéma dva intervaly neumí, spojený interval se nepoužije | ř. 41 (cz-ii-biotech-investments, ticket) | https://www.inibio.eu/ |

Do `vyrazeni.csv` se ticket nezapisuje (schéma CSV ho nemá), je uvedený ve sloupci `duvod`. U i&i Biotech se nevytváří společný interval.

## Ověření v kroku 8

Doplňující fakta z ruční kontroly ověřil Claude načtením stránek 27. 10. 2026 (bez dalšího plošného dohledávání):

- Look AI: https://lookai.vc/look-ai-ventures-backs-embodied-ai-robots-manufacturing/ má v hlavičce článku „Eva Slonkova / September 22, 2026“ a v metadatech article:published_time 2026-09-22T23:59:13+00:00. Pulse 2.0 (https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/) má datePublished 2026-09-16 a jmenuje Look AI Ventures mezi investory; ponecháno jako výhrada.
- Purple: https://www.thesaasnews.com/news/fl-robotics-raises-1m-seed/ má v metadatech datePublished 2026-10-15T06:28:15Z, na stránce „Updated October 14, 2026“ a pole agregátoru „Funding Date: October 14, 2026“; jako zdroj uvádí EU-Startups. Nordic9 uvádí 12. 10. 2026. Použito datum_oznameni 2026-10-15, datum_investice null.
- Reflex: článek CzechCrunch o ArtMasteru má datePublished 2026-10-21; kolo neoznačuje.
- ZAKA: https://zaka.vc/news/ vrátila v kroku 8 HTTP 466 a znovu načtena nebyla. FinalDose a datum 16. 7. 2026 vycházejí z hodnocení (ř. 48) a z kontrolního agenta (fáze A).

## Rozšíření schématu

- `nevyresene.csv`, sloupec `otazka`: nové hodnoty `sidlo` (nevyřešené sídlo správce, cz-tensor-ventures) a `investice` (nevyřešené přiřazení investice, cz-presto-ventures), doplněné do PLAN.md bod 3 a do `scripts/zkontroluj_data.py`. Pravidla zařazení se nemění.
- `stav_kontroly.csv` (nový soubor jen v `data/opraveno/`): sloupce `id`, `vysledny_soubor`, `puvodni_soubor`, `ve_vzorku`, `kontrola`, `vysledek`, `pole_nelze_overit`, `opravena_pole`, `vyhrady`, `odkaz_hodnoceni`. `kontrola` je `hodnoceno_s_asistenci_ai` nebo `nekontrolovano`; `vysledek` je `s_opravou`, `hodnocena_pole_ano`, `s_vyhradou_nelze_overit` (některé pole `nelze_overit`), `presunuto` nebo `nehodnoceno`.

## Zbývající neověřené případy

| id | výsledný soubor | pole nelze_overit | výhrady |
|---|---|---|---|
| cz-credo-ventures | investori.json | – | rozsah pilotu: role Credo Ventures Management II a.s. jako správce nového fondu neověřena [ř. 226, rozsah_pilotu] |
| cz-ii-biotech-investments | vyrazeni.csv | nezavislost_zdroju | fond se sídlem v Lucembursku, česká s.r.o. je poradce a tým; skutečný investor, ne neinvestor (podrobně sloupec duvod v vyrazeni.csv); nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění [ř. 39, nezavislost_zdroju] |
| cz-ii-prague | investori.json | – | nástroj: oprava hodnocení v kroku 9 (původně je_investor = nelze_overit a přesun do nevyresene.csv); výpis ARES CasInvent uvádí konvertibilní zápůjčku i&i Prague z 4. 3. 2025, nabídku 48 akcií třídy C (VH 22. 5. 2025) a zapsané splacené zvýšení kapitálu 30. 5. 2025; upsání akcií i&i Prague je doloženo nepřímo, smlouva o úpisu přímo ověřena není [ř. 65, je_investor] |
| cz-kaya-vc | investori.json | – | mimo náhodný vzorek 20 z 27 zařazených (seed 20261027), údaje ručně nekontrolované; známý nález automatické kontroly (metodika): kapital[2].fond vyplněn u druhu committed_capital; bez dokončeného hodnocení neopraveno; nález kontrolního agenta (fáze B): správcem je podle kaya.vc/sustainability lucemburský AIFM KAYA VC GP S.à r.l.; sídlo správce neposouzeno, zařazení beze změny |
| cz-look-ai-ventures | investori.json | nezavislost_zdroju | nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění [ř. 128, nezavislost_zdroju]; Pulse 2.0 (https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/) vyšel 16. 9. 2026 a jmenuje Look AI Ventures mezi investory Embodied AI; první veřejné oznámení může být starší než datum_oznameni 2026-09-22 [ř. 127, posledni_investice] |
| cz-miton | investori.json | nezavislost_zdroju | nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění [ř. 288, nezavislost_zdroju]; poslední investice: citovaný zdroj Lupa.cz nedostupný, firma a datum potvrzeny náhradním zdrojem CzechCrunch [ř. 287, posledni_investice] |
| cz-n1-ventures | vyrazeni.csv | existence | sídlo správce mimo ČR (GP v Lucembursku); skutečný investor, ne neinvestor (podrobně sloupec duvod v vyrazeni.csv) |
| cz-presto-ventures | nevyresene.csv | investicni_cinnost \| je_investor \| posledni_investice | přiřazení investic v okně k Prestu nedoložené (ne vyvrácené) (podrobně sloupec duvod v nevyresene.csv) |
| cz-purple-ventures | investori.json | nezavislost_zdroju | nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění [ř. 148, nezavislost_zdroju]; FLÆ Robotics: datum_oznameni 2026-10-15 podle času publikace TheSaaSNews; „Funding Date: October 14, 2026“ (pole agregátoru) a Nordic9 12. 10. 2026 se rozcházejí, původní zpráva EU-Startups nečtena [ř. 147, posledni_investice] |
| cz-reflex-capital | investori.json | – | ArtMaster: Nordic9 označuje kolo jako seed, CzechCrunch kolo neoznačuje; kolo null, nástroj nezjištěn [ř. 157, posledni_investice] |
| cz-rockaway-ventures | investori.json | – | poslední investice: Nordic9 1. 3. 2026 uvádí seed do Float, původní oznámení nenalezeno [ř. 257, posledni_investice]; kapitál: zdroj „nearly €55 million“, záznam 55 000 000 je horní mez [ř. 261, kapital] |
| cz-startupyard | investori.json | – | typ: u investice Ydoca není jisté, zda šla z vlastních peněz StartupYard (TechBoost Syndicate) [ř. 56, typ]; poslední investice: firmy nového batche bez zmínky o investici, nedoloženo [ř. 58, posledni_investice] |
| cz-tensor-ventures | nevyresene.csv | rozsah_pilotu \| nezavislost_zdroju | sídlo správce neověřené, pravidla pilotu vyžadují správce v ČR (podrobně sloupec duvod v nevyresene.csv); nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění [ř. 19, nezavislost_zdroju] |
| cz-y-soft-ventures | investori.json | nezavislost_zdroju | nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění [ř. 178, nezavislost_zdroju] |
| cz-zaka-vc | investori.json | – | PerfectBit (tisková zpráva 18. 8. 2026 na zaka.vc/news, PitchBook podle vyhledávání seed 26. 6. 2026) neověřen, ruční kontrola ho neposoudila; FinalDose se v kroku 8 nepodařilo znovu načíst (HTTP 466) [ř. 48, posledni_investice]; typ VC obhajitelný pro Fund 1, AIN.UA 10. 3. 2025 ZAKA označuje jako family office [ř. 46, typ] |

Dále: sedm zařazených mimo vzorek (cz-cs-seed-starter, cz-fazole-ventures, cz-jic-ventures, cz-jt-ventures, cz-kaya-vc, cz-lighthouse-ventures, cz-tilia-impact-ventures) a 29 vyřazených, hraničních a nevyřešených kandidátů z výstupu agenta ručně kontrolováno nebylo. U všech zařazených platí, že poslední investice je nejnovější doložená, ne záruka úplnosti.

## Automatická kontrola opravené verze

`scripts/zkontroluj_data.py` čte jen `data/vystup_agenta/`. Pro kontrolu opravené verze se spouští nad dočasným kořenem mimo repozitář: kopie `data/kandidati.csv`, čtyř výsledkových souborů z `data/opraveno/` jako `data/vystup_agenta/` a kopie `ai-log/02-obohaceni/mapovani_id.csv`, ve které je u čtyř přesunutých id změněný sloupec `soubor`. Původní data se nepřesouvají ani nepřepisují. Kontrola URL (`--over-url`) se nespouštěla.

- `--datum 2026-10-26` (výchozí, den kroku 2): chyby struktury 0, metodický nesoulad 9, upozornění 8. Osm nálezů „datum není v budoucnosti“ má jedinou příčinu: zdroje čtené v kroku 8 mají `stazeno` 2026-10-27, tedy po referenčním datu. Devátý je známý nález u KAYA. Před opravou i&i Prague v kroku 9 bylo nálezů 10 (navíc `stazeno` přesunutého záznamu i&i Prague).
- `--datum 2026-10-27` (den ruční kontroly): chyby struktury 0, metodický nesoulad 1 (známý nález u cz-kaya-vc: `kapital[2].fond` u druhu `committed_capital`, mimo vzorek, bez dokončeného hodnocení neopraveno), upozornění 8 (stejná jako při 2026-10-26). Statusy se posunem referenčního data nemění.
- Upozornění je 8 místo 16 v `ai-log/03-kontrola/automaticka_kontrola.md` ze dvou důvodů: kontrola URL se nespouštěla (5 nedostupných URL v původní zprávě) a upozornění k `cvca.cz` a `plati_k` u N1 a i&i Biotech zmizela s přesunem jejich záznamů z `investori.json` do `vyrazeni.csv` (3 nálezy).

## Jak opravenou verzi znovu vytvořit

`python3 scripts/oprav.py` (bez sítě, deterministický; přepíše jen soubory v `data/opraveno/`).
