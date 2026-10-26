# Databáze investorů

Praktická úloha ve výběrovém řízení na pozici Junior AI Developer ve společnosti Clientelo.

## Zadání

Sestavit pomocí AI agentů spolehlivou databázi investorů, kteří vkládají vlastní nebo svěřený kapitál do soukromých firem výměnou za podíl (VC, CVC, PE, family office, andělé). Databáze nesmí obsahovat náhodné firmy. Každý údaj musí mít doložený zdroj a datum.

Součástí úlohy je:

- ověřit postup na pilotním vzorku (VC a CVC v ČR) a změřit jeho přesnost,
- odhadnout, kolik investorů lze z veřejných zdrojů dohledat ve světě,
- odhadnout náklady na zpracování celého světa.

Postup, pravidla zařazení, struktura záznamu a způsob měření jsou popsané v [PLAN.md](PLAN.md).

## Stav

Cílová skupina pilotu jsou VC/CVC se sídlem v ČR. Jde o můj zvolený rozsah, zadání VC fondy v jedné zemi uvádí jen jako příklad menšího vzorku. Pravidla pilotu jsou v [PLAN.md](PLAN.md), bod 3.

Hotový je krok 1 z bodu 9 plánu: seznam kandidátů pro pilot v `data/kandidati.csv`. Pro další zpracování jsem vybral všech 57 kandidátů, menší vzorek nevzniká. Jde o kandidáty, ne o ověřené investory.

Krok 2 proběhl ve dvou bězích:

- **Zkušební dávka** prvních 5 kandidátů podle abecedy podle pravidel platných před úpravami popsanými níže. Její původní výstup je archivovaný beze změn v [ai-log/02-zkusebni-davka/vystup_pravidla_v1/](ai-log/02-zkusebni-davka/vystup_pravidla_v1/) (shodný s commitem f4cd74d). Naměřená doba dávky je 5 min 49 s a zahrnuje jen zpracování agentem, bez kontroly, oprav a ručního ověřování ([ai-log/02-zkusebni-davka/](ai-log/02-zkusebni-davka/)). Do měření nevstupuje.
- **Vyhodnocení po úpravě metodiky:** všech 57 kandidátů včetně prvních pěti znovu podle aktuálních pravidel, v dávkách po 10 podle abecedy. Měří se jen tento běh, jeho výstup je v `data/vystup_agenta/` a podklady v [ai-log/02-obohaceni/](ai-log/02-obohaceni/). **Nejde o nezávislý test na dosud neviděných datech:** prvních pět kandidátů ovlivnilo návrh upravených pravidel, takže výsledek u nich (a tím i celkový výsledek) může vycházet lépe, než by vyšel na nových datech.

Ruční hodnocení zatím neproběhlo.

### Pravidla upravená po zkušební dávce

Dávka ukázala nejasnosti v určení typu a v doložení nástroje investice. Pravidla v [PLAN.md](PLAN.md) jsem upravil takto:

- **Typ:** určuje se podle vlastního popisu subjektu a doloženého fungování, ne podle toho, do čeho investuje. Family office spravuje majetek jedné nebo několika rodin a VC může být jeho investiční strategie. Samotné financování penězi rodiny pro typ family office nestačí. Přibyl typ korporátní investor bez samostatné jednotky (provozní firma investující z vlastní společnosti), který není CVC a je mimo rozsah pilotu.
- **Nevyřešená rozhodnutí:** když jsou důkazy o typu nebo nástroji rozporné nebo nedostatečné, agent kandidáta nezařadí ani nevyřadí a zapíše ho do `data/vystup_agenta/nevyresene.csv` k ručnímu rozhodnutí.
- **Nástroj (podmínka 3):** u každé investice se zapisuje, jestli je podíl nebo konvertibilní nástroj doložený (zdroj ho výslovně uvádí, nebo investor je zapsaný jako společník portfoliové firmy), jestli jde jen o nepřímou indicii, nebo jestli je nezjištěný. Podmínku splní doložený nástroj a také nepřímá indicie, když zdroj dokládá účast konkrétního investora v pre-seed, seed nebo series kole a nejsou zjištěné informace, že jeho účast byla výhradně nekonvertibilní dluh. U smíšených kol nerozhoduje jen označení celého kola.

**Riziko tohoto rozhodnutí.** Účast v pre-seed, seed nebo series kole je přijatý pracovní předpoklad, ne doložený nástroj. Investor, který se kola účastnil úvěrem nebo jiným nekonvertibilním dluhem, o čemž zdroj nic neuvádí, tak může být chybně zařazen. Proto má záznam opřený jen o tento předpoklad jistotu investice nejvýš `stredni` a lze ho při ruční kontrole spočítat a zkontrolovat zvlášť. Jak často zdroje nástroj neuvádějí a jak často je předpoklad chybný, zatím změřené není.

## Sběr kandidátů (krok 1)

Staženo 26. 10. 2026. Výsledek: **57 unikátních kandidátů**.

### Zdroje

| Zdroj | Co jsem převzal | Kandidátů | Mimo rozsah |
|---|---|---|---|
| [CVCA, řádní členové](https://cvca.cz/en/category/full-members/) | 27 řádných členů (PE/VC investoři podle CVCA); přidružení členové jsou podle CVCA poradci a banky, nepřebíral jsem je | 19 | 8 (sídlo mimo ČR) |
| [CEE Funding Map](https://www.pampam.city/funds-poland-BJpHbykKoXoBaILayYBs) (Warsaw Equity Group, CzechInvest, Czech Founders) | 95 položek mapy ČR a Polska s adresou | 38 | 55 (sídlo v Polsku, u Tachles VC v USA) |
| [funding.tech.eu](https://funding.tech.eu/api-docs), kola českých firem 2025–2026 | 60 kol, 113 jmen investorů | 26 | 84 (z toho 8 s nevyřešeným sídlem, viz Omezení) |
| [Dealroom, veřejná část](https://dealroom.co/investors/manifest.json) | manifest 609 investorů, jen Credo Ventures má zemi Czechia | 1 | – |

Kandidát může být ve více zdrojích, proto součet sloupce nedává 57. Ve dvou a více zdrojích je 20 kandidátů, jen v jednom 37 (CVCA 9, mapa 19, funding.tech.eu 9).

### Postup

1. **Rozsah = sídlo v ČR podle zdroje.** U CVCA a mapy rozhoduje adresa, kterou uvádí sám zdroj. funding.tech.eu sídlo investora neeviduje (`countries` jsou země portfolia), proto jsem jména rozdělil takto:
   - jména shodná s kandidátem z CVCA nebo z mapy jsem přiřadil k němu,
   - fyzické osoby (typ `Angel` ve zdroji) a popisy typu „existing shareholders“ jsou mimo rozsah pilotu,
   - u zbylých 65 organizací (a u Tachles VC, který na mapě nemá adresu) jsem sídlo dohledal ve veřejném zdroji s URL a citací (vlastní web, rejstřík, tisková zpráva). Všech 9 českých sídel jsem ověřil v obchodním rejstříku (or.justice.cz).
2. **Bez posuzování.** Typ (VC, CVC, PE, family office…) ani aktivitu jsem neposuzoval. Mezi kandidáty jsou proto i subjekty, které zdroj označuje jako PE nebo family office, provozní firmy (Braiins, Botanique Hospitality), fond J&T Investiční společnosti (Fond Naše Česko) a klub andělů (Garage Angels). O jejich zařazení se rozhodne v kroku 3.
3. **Deduplikace.** Ručně podle shodného názvu nebo jeho varianty (aliasy z funding.tech.eu) a domény webu, explicitně v tabulce ve [scripts/sestav_kandidaty.py](scripts/sestav_kandidaty.py). Shoda adresy sama o sobě nestačí.
4. **Dohledatelnost.** `zdroj_seznamu` a `zdroj_url` jsou u kandidáta z více zdrojů seznamy oddělené ` | ` ve stejném pořadí, jeden pár na každý výskyt. U funding.tech.eu je `zdroj_url` záznam investora v API, ze kterého jsem jméno převzal.
5. **`id`** má tvar `cz-nazev-bez-diakritiky`, je stabilní a v dalších krocích se nemění.
6. **`web`** je převzatý ze zdroje (CVCA, mapa). U kandidátů jen z funding.tech.eu pochází z ověření sídla. Kde jsem web nedoložil, je prázdný.

Podklady jsou v [ai-log/01-kandidati/](ai-log/01-kandidati/): extrakty zdrojů (`zdroje/`), ověření sídel s URL a citacemi (`sidla_overeni.json`), všechny vynechané výskyty s důvodem, jak je sběr původně zapsal (`mimo_rozsah.csv`, beze změn), dodatečné opravy sběru (`opravy_sberu.csv`) a sběrné skripty (`skripty/`). Výsledné CSV vytváří `python3 scripts/sestav_kandidaty.py`.

### Omezení

- **funding.tech.eu:** webové rozhraní vracelo HTTP 429 s bezpečnostní kontrolou Vercelu. Agent ji neprolomil, data ale vzal z oficiálního bezklíčového API téhož zdroje (`/api/v1`, robots.txt ho povoluje). Původní pokyn zakazoval po nedostupnosti zdroje použít náhradní nástroj, takže použití API ho nedodrželo. Schválil jsem ho dodatečně, až po dokončení sběru. Dataset obsahuje jen 60 kol českých firem za 2025–2026, pokrytí je tedy neúplné.
- **Dealroom:** aplikace (app.dealroom.co, czechia.dealroom.co) vrací HTTP 403, neobcházel jsem ji. Veřejná část (stránky zemí a měst, market mapy) investory v ČR nevypisuje. Manifest obsahuje jen top investory světa.
- **CEE Funding Map:** typ fondu (VC, PE, family office…) je na mapě jen v poškozených fragmentech importu, proto jsem ho nepřebíral. ARX Equity má na mapě polskou adresu, v CVCA pražskou, a je veden jako kandidát.
- **Nevyřešená sídla:** u 8 organizací z funding.tech.eu (Creandum, Decibel, Lumiere AI Ventures, Northzone, Puzzle Ventures, Riverside Acceleration Capital, SCI Ventures, University2Ventures) se sídlo nepodařilo doložit. Nejsou prokazatelně zahraniční ani prokazatelně české, vedu je jako nevyřešené (`nevyreseno_sidlo`) v `opravy_sberu.csv`. Původní `mimo_rozsah.csv` je uvádí mezi vynechanými výskyty a zůstává beze změny. Počet kandidátů, místní rozsah pilotu i recall se proto vztahují jen k 57 kandidátům. Kdyby některá z 8 organizací sídlila v ČR, kandidátů by bylo až 65.
- **Sídla:** U Tachles VC vlastní web uvádí jen adresu v USA. U Botanique Hospitality je zdrojem sídla kromě rejstříku jen agregátor CB Insights. U QQ Capital rejstřík uvádí jediný subjekt toho jména, jeho totožnost s investorem v kole Navigara jsem ale nepotvrdil.
- **Možné duplicity, které jsem nesloučil** (doložená je jen shodná adresa nebo vazba): Nation1 (nation1.vc, doména se nepřekládá) a N1 Ventures (n1.rocks) na adrese Národní 135/14; i&i Biotech Investments a i&i Prague (i&i Prague podle svého webu založil i&i Biotech Fund); Tilia Impact Ventures a PurposeTech na adrese Drtinova 557/10; Fond Naše Česko a J&T Ventures na adrese Sokolovská 700/113a. Zatím zůstávají samostatně, v kroku 2 o nich rozhodne pravidlo „jedna investiční firma = jeden záznam“.
- **Ověření sídel** dělali pomocní agenti stejného modelu z veřejných webů. Česká sídla jsem znovu ověřil v rejstříku, zahraniční jen u agentů. Několik zahraničních sídel opírají jen agregátory (CB Insights, Caplight), viz `sidla_overeni.json`.

### Licence a atribuce dat funding.tech.eu

Podmínky jsem ověřil 26. 10. 2026 na [funding.tech.eu/for-ai](https://funding.tech.eu/for-ai), [api-docs](https://funding.tech.eu/api-docs) a v [llms.txt](https://funding.tech.eu/llms.txt). Stránka /terms vracela HTTP 429, nečetl jsem ji.

- **Licence:** data jsou pod [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). API je bezklíčové a pouze pro čtení, s limitem 120 požadavků za 60 s, 600 za hodinu a 2 000 denně na IP adresu. Sběr udělal zhruba 120 požadavků s pauzou mezi nimi.
- **Atribuce:** zdroj: „Tech.eu Funding Explorer“, https://funding.tech.eu/api-docs. U každého kandidáta z tohoto zdroje je v `zdroj_url` URL záznamu v API, ze kterého údaj pochází (např. https://funding.tech.eu/api/v1/investors/Credo%20Ventures).
- **Úpravy dat:**
  - `ai-log/01-kandidati/zdroje/fundingtecheu_kola_cz_2025_2026.json` je nezměněná odpověď `/api/v1/rounds` (filtr country = Czech Republic, 2025-01-01 až 2026-12-31), jen spojená ze stránek.
  - `fundingtecheu_investori.json` je zkrácený výtah z `/api/v1/investors/{name}` (jen `name`, `types`, `aliases`, `deals` a HTTP status).
  - Z jmen investorů jsem odvodil seznam kandidátů: varianty jmen jsem sloučil s kandidáty z jiných zdrojů a rozdělil je podle sídla.
  - Částky, data ani jiné hodnoty jsem neměnil a do `data/kandidati.csv` jsem je nepřebíral.

## Struktura

| Cesta | Obsah |
|---|---|
| `PLAN.md` | plán projektu |
| `data/kandidati.csv` | kandidáti ze seznamů |
| `data/vystup_agenta/` | původní výstup agenta (zařazení, vyřazení, hraniční a nevyřešené případy), beze změn |
| `data/hodnoceni.csv` | ruční hodnocení všech kandidátů |
| `data/opraveno/` | opravená verze po ručním hodnocení |
| `scripts/` | skripty pro automatickou kontrolu a měření |
| `ai-log/` | exporty konverzací s agenty |

## Licence

Viz [LICENSE](LICENSE).
