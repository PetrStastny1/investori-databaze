# Průvodce ruční kontrolou

Podklad pro krok 6 z PLAN.md bod 9: ruční ověření všech kandidátů pilotu. U každého kandidáta je původní rozhodnutí agenta, hodnoty ke kontrole s odkazy na zdroje a pole, která hodnotím. Otázky a názvy polí jsou podle PLAN.md bod 6: plná kontrola u zařazených, zkrácená u vyřazených a hraničních, u nevyřešených `je_investor`, `rozsah_pilotu` a `duvod`. Nálezy kontroly zdrojů tu nejsou.

Vytvořeno skriptem [skripty/priprav_podklady.py](skripty/priprav_podklady.py) z `data/vystup_agenta/` a `ai-log/02-obohaceni/mapovani_id.csv`.

## Postup

1. První ruční verdikty vyplním do `data/hodnoceni.csv` **bez čtení** [nalezy_ai.md](nalezy_ai.md) a commitnu je.
2. Před první změnou po přečtení nálezů AI se `data/hodnoceni.csv` zkopíruje do `ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv`:
   `cp data/hodnoceni.csv ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv`
3. Do `data/hodnoceni.csv` pak zapíšu konečný verdikt a do sloupce `poznamka` důvod změny.
4. Přínos druhého agenta bude jen orientační, protože pořadí kontroly je podle jeho nálezů. Kandidáti, u kterých druhý agent něco našel, jsou kontrolovaní dřív a pozorněji, takže porovnání verdiktů před a po čtení nálezů není nezávislé měření.

## Jak vyplňovat `data/hodnoceni.csv`

- Řádky jsou předvyplněné ve stejném pořadí jako tento průvodce: `soubor`, `id`, `pole` a `hodnotil` = Petr Šťastný. Sloupce `hodnoceni`, `pricina_chyby`, `poznamka` a `datum` jsou prázdné.
- `hodnoceni`: `ano` / `ne` / `nelze_overit` (PLAN.md bod 6).
- `pricina_chyby` jen u chyby: `spatny_zdroj`, `chybne_cteni`, `zastaraly_udaj` nebo `chyba_pravidel` (PLAN.md bod 7).
- Nevyřešení: `je_investor` a `rozsah_pilotu` zároveň zaznamenávají moje rozhodnutí, zvolený typ nebo nástroj uvedu v poznámce (PLAN.md bod 6). Výsledek patří do `data/opraveno/`, původní výstup agenta se nemění.
- U prázdného pole (`null`) PLAN.md bod 7 měří přesnost jen mezi vyplněnými a zvlášť podíl vyplněných.
- Sloučení Nation1 → N1 nemá v PLAN.md vlastní pole. Řádek používá `soubor` = `mapovani_id.csv` a `pole` = `slouceni`, stejně jako kontrola zdrojů (krok 4).
- Okno 24 měsíců začíná 2024-10-26, hranice 12 měsíců (`aktivni` / `investice_dolozena_12_24_mesicu`) je 2025-10-26. Obojí agent počítal ke dni zpracování 2026-10-26.

## Pořadí

1. **Příslušnost k pilotu:** sídla N1, Tensor, KAYA a i&i Biotech, typ ZAKA a StartupYard, i&i Prague. Kontrola sloučení Nation1 → N1 je samostatný oddíl hned za N1.
2. **Možná chybná vyřazení:** Orbit, McWin, Espira.
3. **Nevyřešení.**
4. **Ostatní** podle závažnosti nálezů kontroly zdrojů. Kandidáti bez nálezu jsou na konci, zařazení před vyřazenými.

U každého kandidáta je odkaz na jeho id v [nalezy_ai.md](nalezy_ai.md). Ten otevírám až po commitu prvních verdiktů.

## Přehled

| # | id | název | soubor | rozhodnutí agenta | polí |
|---|---|---|---|---|---|
| 1 | [`cz-n1-ventures`](#1-cz-n1-ventures) | N1 Ventures | investori.json | zařazen | 10 |
| 2 | [`cz-nation1`](#2-cz-nation1) | Nation1 | mapovani_id.csv | sloučen do `cz-n1-ventures` | 1 |
| 3 | [`cz-tensor-ventures`](#3-cz-tensor-ventures) | Tensor Ventures | investori.json | zařazen | 10 |
| 4 | [`cz-kaya-vc`](#4-cz-kaya-vc) | KAYA VC | investori.json | zařazen | 10 |
| 5 | [`cz-ii-biotech-investments`](#5-cz-ii-biotech-investments) | i&i Biotech Investments | investori.json | zařazen | 10 |
| 6 | [`cz-zaka-vc`](#6-cz-zaka-vc) | ZAKA VC | investori.json | zařazen | 10 |
| 7 | [`cz-startupyard`](#7-cz-startupyard) | StartupYard | investori.json | zařazen | 10 |
| 8 | [`cz-ii-prague`](#8-cz-ii-prague) | i&i Prague | investori.json | zařazen | 10 |
| 9 | [`cz-orbit-capital`](#9-cz-orbit-capital) | Orbit Capital | hranicni.csv | hraniční, druh `venture_debt` | 4 |
| 10 | [`cz-mcwin-partners`](#10-cz-mcwin-partners) | McWin Partners | vyrazeni.csv | vyřazen, kategorie `neni_investor` | 4 |
| 11 | [`cz-espira-investments`](#11-cz-espira-investments) | Espira Investments | vyrazeni.csv | vyřazen, kategorie `neni_investor` | 4 |
| 12 | [`cz-rockawayx`](#12-cz-rockawayx) | RockawayX | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 13 | [`cz-lumus-investments`](#13-cz-lumus-investments) | LUMUS Investments | nevyresene.csv | nevyřešen, otázka `typ | nastroj` | 3 |
| 14 | [`cz-chilli-ventures`](#14-cz-chilli-ventures) | Chilli Ventures | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 15 | [`cz-fond-nase-cesko`](#15-cz-fond-nase-cesko) | Fond Naše Česko | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 16 | [`cz-moonhill-capital`](#16-cz-moonhill-capital) | Moonhill Capital | nevyresene.csv | nevyřešen, otázka `typ | nastroj` | 3 |
| 17 | [`cz-botanique-hospitality`](#17-cz-botanique-hospitality) | Botanique Hospitality | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 18 | [`cz-braiins`](#18-cz-braiins) | Braiins | nevyresene.csv | nevyřešen, otázka `nastroj` | 3 |
| 19 | [`cz-gi21-capital`](#19-cz-gi21-capital) | Gi21 Capital | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 20 | [`cz-jet-investment`](#20-cz-jet-investment) | Jet Investment | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 21 | [`cz-kkcg`](#21-cz-kkcg) | KKCG | nevyresene.csv | nevyřešen, otázka `nastroj` | 3 |
| 22 | [`cz-tarpan-capital`](#22-cz-tarpan-capital) | Tarpan Capital | nevyresene.csv | nevyřešen, otázka `typ` | 3 |
| 23 | [`cz-garage-angels`](#23-cz-garage-angels) | Garage Angels | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 24 | [`cz-look-ai-ventures`](#24-cz-look-ai-ventures) | Look AI Ventures | investori.json | zařazen | 10 |
| 25 | [`cz-jic-ventures`](#25-cz-jic-ventures) | JIC Ventures | investori.json | zařazen | 10 |
| 26 | [`cz-purple-ventures`](#26-cz-purple-ventures) | Purple Ventures | investori.json | zařazen | 10 |
| 27 | [`cz-reflex-capital`](#27-cz-reflex-capital) | Reflex Capital | investori.json | zařazen | 10 |
| 28 | [`cz-soulmates-ventures`](#28-cz-soulmates-ventures) | Soulmates Ventures | investori.json | zařazen | 10 |
| 29 | [`cz-y-soft-ventures`](#29-cz-y-soft-ventures) | Y Soft Ventures | investori.json | zařazen | 10 |
| 30 | [`cz-lighthouse-ventures`](#30-cz-lighthouse-ventures) | Lighthouse Ventures | investori.json | zařazen | 10 |
| 31 | [`cz-czech-founders-vc`](#31-cz-czech-founders-vc) | Czech Founders VC | investori.json | zařazen | 10 |
| 32 | [`cz-depo-ventures`](#32-cz-depo-ventures) | DEPO Ventures | investori.json | zařazen | 10 |
| 33 | [`cz-inven-capital`](#33-cz-inven-capital) | Inven Capital | investori.json | zařazen | 10 |
| 34 | [`cz-credo-ventures`](#34-cz-credo-ventures) | Credo Ventures | investori.json | zařazen | 10 |
| 35 | [`cz-cs-seed-starter`](#35-cz-cs-seed-starter) | ČS Seed Starter | investori.json | zařazen | 10 |
| 36 | [`cz-jt-ventures`](#36-cz-jt-ventures) | J&T Ventures | investori.json | zařazen | 10 |
| 37 | [`cz-rockaway-ventures`](#37-cz-rockaway-ventures) | Rockaway Ventures | investori.json | zařazen | 10 |
| 38 | [`cz-borovicka-capital`](#38-cz-borovicka-capital) | Borovicka Capital | investori.json | zařazen | 10 |
| 39 | [`cz-fazole-ventures`](#39-cz-fazole-ventures) | Fazole Ventures | investori.json | zařazen | 10 |
| 40 | [`cz-miton`](#40-cz-miton) | Miton | investori.json | zařazen | 10 |
| 41 | [`cz-presto-ventures`](#41-cz-presto-ventures) | Presto Ventures | investori.json | zařazen | 10 |
| 42 | [`cz-purposetech`](#42-cz-purposetech) | PurposeTech | investori.json | zařazen | 10 |
| 43 | [`cz-tilia-impact-ventures`](#43-cz-tilia-impact-ventures) | Tilia Impact Ventures | investori.json | zařazen | 10 |
| 44 | [`cz-arx-equity-partners`](#44-cz-arx-equity-partners) | ARX Equity Partners | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 45 | [`cz-mam-private-equity-fund`](#45-cz-mam-private-equity-fund) | MAM Private Equity Fund SICAV a.s. | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 46 | [`cz-everita-capital`](#46-cz-everita-capital) | EVERITA Capital | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 47 | [`cz-bd-partners`](#47-cz-bd-partners) | BD Partners | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 48 | [`cz-central-europe-industry-partners`](#48-cz-central-europe-industry-partners) | Central Europe Industry Partners | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 49 | [`cz-emma-capital`](#49-cz-emma-capital) | EMMA Capital | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 50 | [`cz-genesis-capital`](#50-cz-genesis-capital) | Genesis Capital | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 51 | [`cz-lion-beat-capital`](#51-cz-lion-beat-capital) | Lion Beat Capital | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 52 | [`cz-qq-capital`](#52-cz-qq-capital) | QQ Capital | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 53 | [`cz-skylimit-investments`](#53-cz-skylimit-investments) | SkyLimit Investments | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 54 | [`cz-stratum-partners`](#54-cz-stratum-partners) | Stratum Partners | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 55 | [`cz-tcf-capital`](#55-cz-tcf-capital) | TCF Capital | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 56 | [`cz-thein`](#56-cz-thein) | Thein | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |
| 57 | [`cz-versute-investments`](#57-cz-versute-investments) | Versute Investments | vyrazeni.csv | vyřazen, kategorie `mimo_rozsah_pilotu` | 4 |

## Skupina: Příslušnost k pilotu

<a id="1-cz-n1-ventures"></a>
### 1. N1 Ventures (`cz-n1-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [n1.rocks/](https://n1.rocks/)

Nálezy AI: [nalezy_ai.md#cz-n1-ventures](nalezy_ai.md#cz-n1-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Nation 1 GP S.à r.l. a Nation 1 GP II S.à r.l. (Lucembursko, general partneři fondů; zápis v rejstříku neověřen)“, IČO `null`
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [n1.rocks/disclosure](https://n1.rocks/disclosure)
  - asociace, CVCA, zdroj_datum `null`, puvod `null`: [cvca.cz/en/nation1-2/](https://cvca.cz/en/nation1-2/)
  - media, CzechCrunch, zdroj_datum `2023-09-18`, puvod `null`: [cc.cz/z-nation-1-je-n1-cesti-startupovi-investori-chystaji-druhy-fond-chteji-…](https://cc.cz/z-nation-1-je-n1-cesti-startupovi-investori-chystaji-druhy-fond-chteji-do-nej-ziskat-necelou-miliardu/)
- `jistota.existence`: `stredni`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Novoflow**, `datum_pro_filtr` `oznameni` → `2025-11-04`; zprávy o transakci: [thevccorner.com/p/novoflow-ai-healthcare-startup](https://www.thevccorner.com/p/novoflow-ai-healthcare-startup); podpůrné: portfolio_web [n1.rocks/](https://n1.rocks/)
- další: **Liki24**, `datum_pro_filtr` `oznameni` → `2025-07-03`; zprávy o transakci: [forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vik…](https://forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vikhodu-na-novi-evropeyski-rinki-03072025-31013), [inventure.com.ua/en/news/world/ukrainian-platform-liki24-raises-dollar9m-from…](https://inventure.com.ua/en/news/world/ukrainian-platform-liki24-raises-dollar9m-from-local-and-international-investors); podpůrné: portfolio_web [n1.rocks/utech-fund](https://n1.rocks/utech-fund)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Novoflow: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Liki24: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vik…](https://forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vikhodu-na-novi-evropeyski-rinki-03072025-31013)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Nation 1 GP S.à r.l. a Nation 1 GP II S.à r.l. (Lucembursko, general partneři fondů; zápis v rejstříku neověřen)“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Novoflow“, `datum_investice` `null`, `datum_oznameni` `2025-11-04`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`
  - zprava_o_transakci, The VC Corner, zdroj_datum `2025-11-04`, puvod `null`: [thevccorner.com/p/novoflow-ai-healthcare-startup](https://www.thevccorner.com/p/novoflow-ai-healthcare-startup)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [n1.rocks/](https://n1.rocks/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Novoflow: The VC Corner (puvod `null`) [thevccorner.com/p/novoflow-ai-healthcare-startup](https://www.thevccorner.com/p/novoflow-ai-healthcare-startup)
- Liki24: Forbes Ukraine (puvod `tisková zpráva Liki24`) [forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vik…](https://forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vikhodu-na-novi-evropeyski-rinki-03072025-31013); Inventure (puvod `https://forbes.ua/innovations/servis-dostavki-tabletok-liki24-zaluchiv-9-mln-dlya-vikhodu-na-novi-evropeyski-rinki-03072025-31013`) [inventure.com.ua/en/news/world/ukrainian-platform-liki24-raises-dollar9m-from…](https://inventure.com.ua/en/news/world/ukrainian-platform-liki24-raises-dollar9m-from-local-and-international-investors)

**`sektory`**: Sektory odpovídají zdroji
- AI, healthtech, frontier tech; zdroj [n1.rocks/](https://n1.rocks/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `60000000`, `mena` `USD`, `druh` `aum`, `plati_k` `null`, `fond` `null`; zdroj [n1.rocks/](https://n1.rocks/), zdroj_datum `null`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web n1.rocks 'N1 Ventures is an early-stage VC partnering with bold founders in AI, healthtech, and frontier tech'; doložené investice do startupů. Sloučeno s kandidátem cz-nation1: Nation 1 se v roce 2023 přejmenoval na N1 (CzechCrunch 18. 9. 2023 'Přejmenovává se na N1'; managing partneři Marek Moravec a Jaroslav Trojan, oba v týmu na n1.rocks); CVCA profil Nation1 má adresu Národní 135/14, Praha 1, kterou uvádí i n1.rocks jako pražskou kancelář, a kontakt Jaroslav Trojan, Managing Partner; obě značky uvádějí portfoliovou firmu Snuggs. Identita: český právní subjekt nenalezen. ARES hledání 'N1 Ventures', 'Nation 1', 'N1 Management' bez shody; 'Nation1' vrátil jen Nation1 Investment s.r.o. (IČO 09172807, Bělehradská 858/23, Praha 2, jednatelé a společníci Jaroslav Ton a Petr Jiříček), který s týmem N1 nijak nesouvisí, proto nepoužit. Podle n1.rocks/disclosure jsou general partnery fondů 'Nation 1 GP S.à r.l. and Nation 1 GP II S.à r.l.' (lucemburské AIF, GP 'registered alternative investment fund manager'); zápis v lucemburském RCS ani u CSSF jsem nedoložil (GLEIF bez výsledku), proto pravní subjekt nepotvrzen a jistota existence stredni (asociace CVCA, média). Sídlo: web uvádí kanceláře San Francisco, Praha (Národní 135/14) a Lucembursko; tým a značka jsou české (CzechCrunch 'Čeští startupoví investoři', CVCA), formální GP lucemburský; zeme CZ podle sídla značky/týmu, k ruční kontrole. Kapitál: web 'Today, we manage $60M across two funds focused on AI and healthcare.' (bez data, plati_k null). CVCA profil uvádí 'Volume of Funds Managed 35 milionů EUR' (starší údaj značky Nation1, nepřevzat, nesčítán). CzechCrunch 2023 uvádí cíl druhého fondu 35–40 mil. EUR (záměr, není kapitál). U-Tech je 'an independent fund built by N1' (velikost neuvedena). Ticket: web ho neuvádí; CVCA profil uvádí 'Preferred Ammount of Investment 50 tisíc – 1,5 milionů EUR' (profil asociace pod starou značkou, ne web/rozhovor investora), proto ticket null. Poslední investice: Novoflow, The VC Corner 4. 11. 2025: kolo 3,1 mil. USD (velikost celého kola, ne vklad N1) 'led by super angel Justin Hamilton, with participation from N1 Ventures'; typ kola ani nástroj zdroj neuvádí (agregátory Caplight a VCBacked uvádějí seed, bez odkazu na zprávu), nástroj nezjisteno. Novoflow je v portfoliu na n1.rocks. datum_oznameni = datum článku; zda jde o první oznámení, neověřeno, a hranice statusu (2025-10-26) je jen 9 dní před ním, proto status k ruční kontrole. Další: Liki24, Forbes Ukraine 3. 7. 2025 (podle tiskové zprávy firmy): 9 mil. USD 'у Series A раунді' (velikost celého kola), 'Раунд підтримали ... N1 Ventures'; Inventure přebírá Forbes (stejný původ). Nástroj neprima_indicie (Series A), podíl výslovně neuveden. Liki24 je na stránce fondu U-Tech na n1.rocks. Žádná investice nemá dolozeno a nezávislé potvrzení chybí, proto jistota investice stredni. Nepoužito: Flick (seed 6 mil. USD, květen 2026, TheSaaSNews podle BusinessWire uvádí investora jen jako 'N1'; BusinessWire nedostupný, Flick není v portfoliu na n1.rocks, ztotožnění jen přes agregátor Caplight), proto jako doklad nepoužito. funding.tech.eu uvádí jen Liki24 (Series A 2025-07, vodítko). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="2-cz-nation1"></a>
### 2. Nation1 (`cz-nation1`)

Soubor: `mapovani_id.csv` · rozhodnutí agenta: **sloučen do `cz-n1-ventures`**

Nálezy AI: [nalezy_ai.md#cz-nation1](nalezy_ai.md#cz-nation1) (číst až po commitu prvních verdiktů)

**Kandidát v `data/kandidati.csv`:** Nation1, web [nation1.vc/](https://www.nation1.vc/), seznam CVCA: [cvca.cz/en/nation1-2/](https://cvca.cz/en/nation1-2/)

**Odůvodnění agenta (`mapovani_id.csv`):**

> Nation1 je původní název téže investiční firmy: CzechCrunch 18. 9. 2023 'Z Nation 1 je N1' ('Přejmenovává se na N1', https://cc.cz/z-nation-1-je-n1-cesti-startupovi-investori-chystaji-druhy-fond-chteji-do-nej-ziskat-necelou-miliardu/), stejní managing partneři Marek Moravec a Jaroslav Trojan (https://n1.rocks/), shodná adresa Národní 135/14 a kontakt J. Trojan (https://cvca.cz/en/nation1-2/), GP fondů nesou jméno Nation 1 GP S.à r.l. (https://n1.rocks/disclosure). Jeden tým a značka, proto sloučeno do cz-n1-ventures.

**Rozhodnutí agenta s výpisem zdrojů:** [ai-log/02-obohaceni/duplicity.md](../02-obohaceni/duplicity.md), oddíl „Dvojice cz-n1-ventures / cz-nation1“

- **`slouceni`**: Nation1 a N1 Ventures jsou jedna investiční firma a sloučení podle PLAN.md bod 3 („jedna investiční firma = jeden záznam“) je správné. PLAN.md pro sloučení pole nemá, název převzatý z kroku 4.

Řádky v `hodnoceni.csv`: `slouceni`

<a id="3-cz-tensor-ventures"></a>
### 3. Tensor Ventures (`cz-tensor-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [tensor.ventures/](https://tensor.ventures/)

Nálezy AI: [nalezy_ai.md#cz-tensor-ventures](nalezy_ai.md#cz-tensor-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Tensor Ventures a.s.“, IČO `06257241`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-12-22`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06257241](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06257241)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [tensor.ventures/](https://tensor.ventures/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **ValkaAI**, `datum_pro_filtr` `oznameni` → `2026-02-24`; zprávy o transakci: [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599), [startbase.de/news/e12-millionen-pre-seed-fuer-valkaai/](https://www.startbase.de/news/e12-millionen-pre-seed-fuer-valkaai/)
- další: **AppFactor**, `datum_pro_filtr` `oznameni` → `2026-02-04`; zprávy o transakci: [theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-i…](https://theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-in-london-based-appfactor)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - ValkaAI: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599)
  - AppFactor: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-i…](https://theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-in-london-based-appfactor)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Tensor Ventures a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „ValkaAI“, `datum_investice` `null`, `datum_oznameni` `2026-02-24`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`
  - zprava_o_transakci, Seznam Zprávy, zdroj_datum `2026-02-24`, puvod `null`: [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599)
  - zprava_o_transakci, Startbase, zdroj_datum `2026-02-24`, puvod `null`: [startbase.de/news/e12-millionen-pre-seed-fuer-valkaai/](https://www.startbase.de/news/e12-millionen-pre-seed-fuer-valkaai/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- ValkaAI: Seznam Zprávy (puvod `null`) [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599); Startbase (puvod `null`) [startbase.de/news/e12-millionen-pre-seed-fuer-valkaai/](https://www.startbase.de/news/e12-millionen-pre-seed-fuer-valkaai/)
- AppFactor: The AI Insider (puvod `tisková zpráva (článek označen „PRESS RELEASE“)`) [theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-i…](https://theaiinsider.tech/2026/02/04/tensor-ventures-and-others-invest-4-million-us-in-london-based-appfactor)

**`sektory`**: Sektory odpovídají zdroji
- AI, quantum technology, computational biotech, sustainable tech; zdroj [tensor.ventures/](https://tensor.ventures/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web „Tensor Ventures explores deep tech innovation's frontiers & invests in uncharted territories“, „We participate in Seed and Series A rounds. Sometimes we lead; other times, we tag along with trusted partners.“, tým s rolemi „Founder, General Partner“, „VC Principal“; fond Tensor Ventures Fund I SCSp a druhý fond (Tensor Ventures Co-investment Fund s EIF z Národního plánu obnovy, CzechCrunch 15. 5. 2024: EIF „vybral Tensor Ventures jako správce“). Identita: ARES Tensor Ventures a.s. (dříve mr Fund a.s.), IČO 06257241, sídlo Pernerova 635/57, Praha 8 (do 16. 12. 2025 Pernerova 697/35, tuto adresu uvádí web jako „Contact in CZ“), člen představenstva Martin Drdúl, člen dozorčí rady Roman Smola – oba zakladatelé a General Partners podle webu. Sídlo: web uvádí jako adresu „Tensor Ventures GP S.à r.l. & Tensor Ventures Fund I SCSp, 1A Heienhaff, 1736 Senningerberg, Luxembourg“ (GP a fond, lucemburský rejstřík neověřen); tým a značka jsou české (kontakt Praha, média „Czech deep-tech company Tensor Ventures“), proto zeme CZ podle sídla značky/týmu, k ruční kontrole. Ticket: web ho neuvádí; rozpětí z agregátorů (např. €250k–1M) není deklarace investora, proto null. Kapitál: CzechCrunch 15. 5. 2024 nový fond „cílí na celkovou velikost až 50 milionů eur“ (cíl), tisková zpráva AppFactor „The fund has EUR 50 million … at its disposal“ (k dispozici) – ani jedno není doložené aum/committed_capital/fund_size, proto prázdné; EIF až 20 mil. EUR je závazek LP, ne velikost fondu; první fond „20 milionů eur“ (CzechCrunch) bez jednoznačného druhu ukazatele. Poslední investice: ValkaAI (CZ), pre-seed 12 mil. EUR (velikost celého kola, ne vklad Tensor), vedl Rockaway Ventures; Seznam Zprávy 24. 2. 2026: „přidaly se také J&T Ventures, Tensor Ventures, BD Partners“; Startbase 24. 2. 2026: „beteiligt sind zudem J&T Ventures, Tensor Ventures, BD Partners sowie Fond Naše Česko“. Nástroj neprima_indicie (pre-seed), podíl výslovně neuveden. Obě zprávy vyšly týž den a nejspíš vycházejí z informací firmy; nezávislost nedoložena, proto jistota investice stredni (žádná investice nemá doložený nástroj). Další: AppFactor (UK), seed 4 mil. USD (velikost kola), tisková zpráva 4. 2. 2026 „Tensor Ventures led a USD 4 million seed round in London-based AppFactor“. Agregátory (funding.tech.eu, CB Insights, PitchBook) uvádějí i novější účasti (Cnuic pre-seed 2026-04, Wultra 2026-06 podle PitchBook), zprávu o transakci jmenující Tensor jsem nenašel, nezapsáno; Wultra seed+ 3 mil. EUR (leden 2025) a Dynanic pre-seed 550k EUR (2024/2025) nečteno přímo. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="4-cz-kaya-vc"></a>
### 4. KAYA VC (`cz-kaya-vc`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [kaya.vc/](https://www.kaya.vc/)

Nálezy AI: [nalezy_ai.md#cz-kaya-vc](nalezy_ai.md#cz-kaya-vc) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Kaya F3 GP s.r.o.“, IČO `19844166`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-12-23`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19844166](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19844166)
  - media, CzechCrunch, zdroj_datum `2024-06-18`, puvod `null`: [cc.cz/stali-u-zrodu-startupoveho-ceska-kaya-spravuje-miliardy-ma-dva-jednoroz…](https://cc.cz/stali-u-zrodu-startupoveho-ceska-kaya-spravuje-miliardy-ma-dva-jednorozce-a-otevira-paty-fond/)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [kaya.vc/](https://www.kaya.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Viktor**, `datum_pro_filtr` `oznameni` → `2026-05-19`; zprávy o transakci: [finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-rai…](https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html), [thesaasnews.com/news/viktor-raises-75-million-series-a](https://www.thesaasnews.com/news/viktor-raises-75-million-series-a); podpůrné: portfolio_web [kaya.vc/](https://www.kaya.vc/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Viktor: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-rai…](https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Kaya F3 GP s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Viktor“, `datum_investice` `null`, `datum_oznameni` `2026-05-19`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`
  - zprava_o_transakci, Fortune (přetištěno Yahoo Finance), zdroj_datum `2026-05-19`, puvod `null`: [finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-rai…](https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html)
  - zprava_o_transakci, The SaaS News, zdroj_datum `2026-05-19`, puvod `https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html`: [thesaasnews.com/news/viktor-raises-75-million-series-a](https://www.thesaasnews.com/news/viktor-raises-75-million-series-a)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [kaya.vc/](https://www.kaya.vc/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Viktor: Fortune (přetištěno Yahoo Finance) (puvod `null`) [finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-rai…](https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html); The SaaS News (puvod `https://finance.yahoo.com/sectors/technology/articles/exclusive-ai-startup-viktor-raises-130000878.html`) [thesaasnews.com/news/viktor-raises-75-million-series-a](https://www.thesaasnews.com/news/viktor-raises-75-million-series-a)

**`sektory`**: Sektory odpovídají zdroji
- digital economy, physical economy, consumer economy; zdroj [kaya.vc/](https://www.kaya.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `1000000`, `max` `3000000`, `mena` `USD`; zdroj [kaya.vc/](https://www.kaya.vc/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `500000000`, `mena` `USD`, `druh` `aum`, `plati_k` `null`, `fond` `null`; zdroj [kaya.vc/](https://www.kaya.vc/), zdroj_datum `null`
- kapital[1]: `castka` `85000000`, `mena` `USD`, `druh` `fund_size`, `plati_k` `null`, `fond` `Current Fund (podle webu, název neuveden)`; zdroj [kaya.vc/](https://www.kaya.vc/), zdroj_datum `null`
- kapital[2]: `castka` `70000000`, `mena` `EUR`, `druh` `committed_capital`, `plati_k` `2025-06-25`, `fond` `pátý fond (po first closingu)`; zdroj [cc.cz/vsadila-na-rohlik-kdyz-ho-ostatni-investori-takrka-odepisovali-ted-chce…](https://cc.cz/vsadila-na-rohlik-kdyz-ho-ostatni-investori-takrka-odepisovali-ted-chce-kaya-dalsi-jednorozce/), zdroj_datum `2025-06-25`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web 'We invest in ambitious & gritty founders from CEE; pre-seed through to meaningful scale', 'patient capital'; člen CVCA (kandidát z CVCA), funding.tech.eu typ Venture capital; investice do startupů v kolech pre-seed až series A, dříve Enern. Identita: Kaya F3 GP s.r.o., IČO 19844166, Thámova 183/11, Praha 8 (shodná s pražskou adresou na webu), společníci Pavel Mucha 35 %, Tomáš Pačinda, Tomáš Obrtáč, Martin Rajčan, Petr Šmída po 15 %, Radovan Nesrsta 5 %, jednatelé Mucha a Pačinda; CzechCrunch (18. 6. 2024) jmenuje Muchu, Pačindu, Obrtáče a Rajčana jako partnery Kaya. Jde o GP jednoho z fondů; zda je hlavní správcovskou entitou celé značky, nepotvrzeno. Další entity: KAYA Advisory s.r.o. (IČO 22585737, Thámova 183/11), KAYA (fka Enern) s.r.o. (IČO 10838821, 100 % ENERN Investments, investiční fond s proměnným základním kapitálem, a.s., IČO 01790765). Sídlo: web uvádí kanceláře Varšava, Praha, San Francisco, Londýn bez označení centrály; sídlo investiční firmy beru CZ podle rejstříku GP v Praze a českého týmu (CzechCrunch: průkopník českého VC trhu). Ticket: web '$1–3M'; CzechCrunch 25. 6. 2025 uvádí 'od jednoho do tří milionů eur' – měna se liší, zapsán údaj z webu. Kapitál: web '$500M' 'AUM Total' a '$85M' 'Current Fund' (bez data, plati_k null); CzechCrunch 25. 6. 2025 'Pátý fond Kayi disponuje 70 miliony eur ... po first closingu' (zapsáno jako committed_capital k datu článku). Údaje se pravděpodobně překrývají, nesčítat. Sektory: web 'digital, physical, and consumer economies' (generalista). Poslední investice: Viktor (AI, Varšava), série A 75 mil. USD (velikost celého kola, ne vklad Kaya), vedl Accel, 'participation from Bek Ventures, Kaya VC, Inovo VC, and Tenacity Capital' (Fortune 19. 5. 2026); The SaaS News výslovně cituje Fortune/Yahoo jako zdroj, proto stejný původ a jistota investice stredni. Datum uzavření neuvedeno, proto datum_oznameni. Nástroj neprima_indicie (série A), podíl výslovně neuveden. funding.tech.eu uvádí i Jutro Medical (série A, 2025-12), E2B (série A, 2025-07), Supernova (2025-09); zprávy jsem nečetl, proto nezapsány. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="5-cz-ii-biotech-investments"></a>
### 5. i&i Biotech Investments (`cz-ii-biotech-investments`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [inibio.eu/](https://www.inibio.eu/)

Nálezy AI: [nalezy_ai.md#cz-ii-biotech-investments](nalezy_ai.md#cz-ii-biotech-investments) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Biotech Investments s.r.o.“, IČO `10885978`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-03-07`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/10885978](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/10885978)
  - asociace, CVCA, zdroj_datum `null`, puvod `null`: [cvca.cz/en/biotech-investments/](https://cvca.cz/en/biotech-investments/)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [inibio.eu/](https://www.inibio.eu/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Theorema**, `datum_pro_filtr` `oznameni` → `2026-03-27`; zprávy o transakci: [lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-…](https://www.lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-urychlily-vedecky-vyzkum-a-vyvoj/), [cc.cz/prvni-startup-prodali-za-stamiliony-ted-stavi-dalsi-diky-ai-jsme-30krat…](https://cc.cz/prvni-startup-prodali-za-stamiliony-ted-stavi-dalsi-diky-ai-jsme-30krat-rychlejsi-na-nic-necekame/), [vestbee.com/insights/articles/theorema-secures-2-85-m](https://www.vestbee.com/insights/articles/theorema-secures-2-85-m); podpůrné: portfolio_web [inibio.eu/](https://www.inibio.eu/)
- další: **Ternary Therapeutics**, `datum_pro_filtr` `oznameni` → `2026-03-17`; zprávy o transakci: [itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues](https://itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues); podpůrné: portfolio_web [inibio.eu/](https://www.inibio.eu/)
- další: **Antiverse**, `datum_pro_filtr` `oznameni` → `2026-03-03`; zprávy o transakci: [vestbee.com/insights/articles/antiverse-raises-9-3-m](https://www.vestbee.com/insights/articles/antiverse-raises-9-3-m); podpůrné: portfolio_web [inibio.eu/](https://www.inibio.eu/)
- další: **T-CURX**, `datum_pro_filtr` `oznameni` → `2025-12-17`; zprávy o transakci: [samedanltd.com/press-releases/t-curx-announces-20m-series-a-first-closing-led…](https://www.samedanltd.com/press-releases/t-curx-announces-20m-series-a-first-closing-led-by-biomedvc-to-fund-pipeline-of-clinical-stage-car-t-programs-and-advance-proprietary-non-viral-in-vivo-car-t-platform/); podpůrné: portfolio_web [inibio.eu/news/t-curx-announces-%2420m-series-a-first-closing-led-by-biomedvc…](https://www.inibio.eu/news/t-curx-announces-%2420m-series-a-first-closing-led-by-biomedvc-to-fund-pipeline-of-clinical-stage-car-t-programs-and-advance-proprietary-non-viral-in-vivo-car-t-platform)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Theorema: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-…](https://www.lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-urychlily-vedecky-vyzkum-a-vyvoj/)
  - Ternary Therapeutics: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues](https://itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues)
  - Antiverse: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [vestbee.com/insights/articles/antiverse-raises-9-3-m](https://www.vestbee.com/insights/articles/antiverse-raises-9-3-m)
  - T-CURX: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [samedanltd.com/press-releases/t-curx-announces-20m-series-a-first-closing-led…](https://www.samedanltd.com/press-releases/t-curx-announces-20m-series-a-first-closing-led-by-biomedvc-to-fund-pipeline-of-clinical-stage-car-t-programs-and-advance-proprietary-non-viral-in-vivo-car-t-platform/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Biotech Investments s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Theorema“, `datum_investice` `null`, `datum_oznameni` `2026-03-27`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2026-03-27`, puvod `null`: [lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-…](https://www.lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-urychlily-vedecky-vyzkum-a-vyvoj/)
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2026-03-27`, puvod `null`: [cc.cz/prvni-startup-prodali-za-stamiliony-ted-stavi-dalsi-diky-ai-jsme-30krat…](https://cc.cz/prvni-startup-prodali-za-stamiliony-ted-stavi-dalsi-diky-ai-jsme-30krat-rychlejsi-na-nic-necekame/)
  - zprava_o_transakci, Vestbee, zdroj_datum `2026-03-31`, puvod `null`: [vestbee.com/insights/articles/theorema-secures-2-85-m](https://www.vestbee.com/insights/articles/theorema-secures-2-85-m)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [inibio.eu/](https://www.inibio.eu/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Theorema: Lupa.cz (puvod `null`) [lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-…](https://www.lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-urychlily-vedecky-vyzkum-a-vyvoj/); CzechCrunch (puvod `null`) [cc.cz/prvni-startup-prodali-za-stamiliony-ted-stavi-dalsi-diky-ai-jsme-30krat…](https://cc.cz/prvni-startup-prodali-za-stamiliony-ted-stavi-dalsi-diky-ai-jsme-30krat-rychlejsi-na-nic-necekame/); Vestbee (puvod `null`) [vestbee.com/insights/articles/theorema-secures-2-85-m](https://www.vestbee.com/insights/articles/theorema-secures-2-85-m)
- Ternary Therapeutics: IT Brief UK (puvod `null`) [itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues](https://itbrief.co.uk/story/ternary-raises-gbp-3-6m-to-engineer-ai-molecular-glues)
- Antiverse: Vestbee (puvod `null`) [vestbee.com/insights/articles/antiverse-raises-9-3-m](https://www.vestbee.com/insights/articles/antiverse-raises-9-3-m)
- T-CURX: Samedan (tisková zpráva T-CURX) (puvod `null`) [samedanltd.com/press-releases/t-curx-announces-20m-series-a-first-closing-led…](https://www.samedanltd.com/press-releases/t-curx-announces-20m-series-a-first-closing-led-by-biomedvc-to-fund-pipeline-of-clinical-stage-car-t-programs-and-advance-proprietary-non-viral-in-vivo-car-t-platform/)

**`sektory`**: Sektory odpovídají zdroji
- drug discovery, medtech, diagnostics, AI; zdroj [inibio.eu/](https://www.inibio.eu/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `150000`, `max` `2000000`, `mena` `EUR`; zdroj [inibio.eu/](https://www.inibio.eu/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `47000000`, `mena` `EUR`, `druh` `fund_size`, `plati_k` `2022-11-30`, `fond` `i&i Biotech Fund I SCSp`; zdroj [inibio.eu/news/experienced-businessmen-join-forces-with-excellent-science%2C-…](https://www.inibio.eu/news/experienced-businessmen-join-forces-with-excellent-science%2C-invest-%E2%82%AC2m-in-the-fund-at-the-iocb), zdroj_datum `2022-11-30`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web investora se popisuje jako 'early stage biotech venture capital' a 'one of the very few VC funds in Europe focused exclusively on life science ventures'; doložené investice do startupů v kolech pre-seed/seed/series A. Struktura: fond i&i Biotech Fund I SCSp (Lucembursko, web uvádí 'Headquarters: 42, rue de la Vallée, L-2661 Luxembourg'), investičním poradcem a týmem je Biotech Investments, s. r. o., Pobřežní 394/12, Praha 8 (web, CVCA profil 'i&i Biotech Investments' se stejnou adresou a kontaktem Tomáš Maršálek, CFO). Sídlo investiční firmy (poradce/tým, značka i&i Bio) beru jako ČR; lucemburský je právní obal fondu. Identita: ARES Biotech Investments s.r.o., IČO 10885978, sídlo Pobřežní 394/12, Praha 8; jednatelé Tomáš Maršálek a Ivan Vohlmuth (oba na webu jako Founding Partners); společníci SVAI Biotech Investments s.r.o., Luctonber s.r.o. a KAMAVO Biotech Investments s.r.o. (po 1/3); Karel Kubias (Founding Partner podle webu) byl jednatelem do 2024-11-30. Lucemburský fond v rejstříku RCS jsem neověřoval. Fond byl založen v roce 2021 ve spolupráci s EIF a i&i Prague (dceřiná společnost ÚOCHB / IOCB Tech), který je podle ÚOCHB jedním z hlavních investorů fondu; i&i Prague je samostatná firma (incubator a venture builder, 100% IOCB Tech s.r.o.), viz par_cz-ii-biotech-investments__cz-ii-prague.md. Ticket podle webu: business creation 'from €150k', growth 'sweet spot €0.5M to €2M' (min 150 000, max 2 000 000 EUR). Kapitál: web investora 30. 11. 2022: 'the total capital of the fund has risen to approximately €47 million' (zapsáno jako fund_size, přibližná hodnota); stejná stránka v boxu About uvádí 'manages over €53 million' bez data, ÚOCHB 2021 'more than 45 million EUR'; nesčítám, novější nedatovaný údaj (dolní mez) nezapisuji. Poslední investice: Theorema (Praha, AI pro vědecký výzkum), pre-seed 3,3 mil. USD / 70 mil. Kč (velikost celého kola, ne vklad i&i), i&i Biotech Fund mezi investory podle Lupa.cz a CzechCrunch (oba 27. 3. 2026) a Vestbee (31. 3. 2026). Nezávislost zdrojů nedoložena (pravděpodobně všechny vycházejí z oznámení startupu), proto jistota investice stredni; nástroj neprima_indicie (pre-seed), podíl výslovně neuveden v žádném zdroji. Další: Ternary Therapeutics seed 3,6 mil. GBP (velikost kola; IT Brief 17. 3. 2026, jiné zdroje uvádějí oznámení 16. 3. 2026), Antiverse series A 9,3 mil. USD (velikost kola; i&i jako stávající investor, Vestbee 3. 3. 2026), T-CURX first closing series A 20 mil. USD (velikost kola, tisková zpráva 17. 12. 2025). Také KyDo Therapeutics seed 4,45 mil. EUR vedené I&I Bio (web investora 16. 9. 2025, jen web investora, nezapsáno). Sektory a fáze podle webu ('early stage', drug discovery, medtech, diagnostics, AI). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="6-cz-zaka-vc"></a>
### 6. ZAKA VC (`cz-zaka-vc`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [zaka.vc/](https://zaka.vc/)

Nálezy AI: [nalezy_ai.md#cz-zaka-vc](nalezy_ai.md#cz-zaka-vc) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „ZAKA Management s.r.o., Italská 2581/67, Vinohrady, 120 00 Praha 2 (správce značky; fond ZAKA VC I, osoba rizikového kapitálu, a.s., IČO 21514992)“, IČO `21053987`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-06-06`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21053987](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21053987)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-06-11`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21514992](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21514992)
  - media, CzechCrunch, zdroj_datum `2024-07-22`, puvod `null`: [cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milio…](https://cc.cz/zaka-vc-se-meni-z-rodinneho-na-klasicky-startupovy-fond-ma-stovky-milionu-korun/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **ParcelBio**, `datum_pro_filtr` `oznameni` → `2026-05-07`; zprávy o transakci: [biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-t…](https://biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-to-advance-next-generation-mrna-medicines); podpůrné: portfolio_web [zaka.vc/news/](https://zaka.vc/news/)
- další: **Vetstor (VETSTOR CZ s.r.o., IČO 21314675)**, `datum_pro_filtr` `oznameni` → `2025-12-09`; zprávy o transakci: [cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-des…](https://cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-desitky-milionu-ted-ma-i-od-kijonkove/)
- další: **Yenmo**, `datum_pro_filtr` `oznameni` → `2025-03-10`; zprávy o transakci: [en.ain.ua/2025/03/10/zaka-vc-joins-11m-yenmo/](https://en.ain.ua/2025/03/10/zaka-vc-joins-11m-yenmo/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - ParcelBio: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-t…](https://biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-to-advance-next-generation-mrna-medicines)
  - Vetstor (VETSTOR CZ s.r.o., IČO 21314675): `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Yenmo: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „ZAKA Management s.r.o., Italská 2581/67, Vinohrady, 120 00 Praha 2 (správce značky; fond ZAKA VC I, osoba rizikového kapitálu, a.s., IČO 21514992)“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „ParcelBio“, `datum_investice` `null`, `datum_oznameni` `2026-05-07`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`
  - zprava_o_transakci, ParcelBio (Business Wire, přetisk BioSpace), zdroj_datum `2026-05-07`, puvod `null`: [biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-t…](https://biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-to-advance-next-generation-mrna-medicines)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [zaka.vc/news/](https://zaka.vc/news/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- ParcelBio: ParcelBio (Business Wire, přetisk BioSpace) (puvod `null`) [biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-t…](https://biospace.com/press-releases/parcelbio-launches-with-13-million-in-financing-to-advance-next-generation-mrna-medicines)
- Vetstor (VETSTOR CZ s.r.o., IČO 21314675): CzechCrunch (puvod `null`) [cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-des…](https://cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-desitky-milionu-ted-ma-i-od-kijonkove/)
- Yenmo: AIN.UA (puvod `null`) [en.ain.ua/2025/03/10/zaka-vc-joins-11m-yenmo/](https://en.ain.ua/2025/03/10/zaka-vc-joins-11m-yenmo/)

**`sektory`**: Sektory odpovídají zdroji
- Health & Biotech, Industrial Tech; zdroj [zaka.vc/](https://zaka.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web „We are a seed & pre-seed VC fund, investing mainly in the US and Europe.“ CzechCrunch 22. 7. 2024: Zaka VC „se mění z rodinného na klasický startupový fond“, poprvé otevřený externím investorům, s týmem a investiční komisí (Andrej Petrus); jako family office se neoznačuje. Identita a sídlo: ARES vrací ZAKA Management s.r.o. (IČO 21053987, dříve ZAKA VC I s.r.o., Italská 2581/67, Praha 2, jednatelé Samuel Zálešák a Karolína Kasperová, společník ZAKA Holding s.r.o., IČO 17614597, jejímiž společníky jsou SORIA, a.s. a TELUS HOLDING, a.s.) a fond ZAKA VC I, osoba rizikového kapitálu, a.s. (IČO 21514992, stejné sídlo, správní rada Kasperová a Zálešák, předmět mj. správa majetku srovnatelná s obhospodařováním podle § 15 ZISIF). Média jmenují zakladatele Jána Kaspera a Petera Zálešáka (CzechCrunch, Startuprise), jejichž rodiny fond založily; statutáři v rejstříku nesou stejná příjmení, osobní shodu jsem nedoložil, propojení značky s firmami je tedy doloženo názvem, sídlem a příjmením, ne jmény statutárů. Web uvádí kanceláře Silicon Valley, London, Prague, Bratislava; Startuprise (19. 7. 2024) „Prague-based“, AIN.UA (10. 3. 2025) „Czech ZAKA VC“, CzechCrunch dříve „česko-slovenský fond“. Sídlo beru podle správce v Praze (CZ). Podíl ve Vetstoru drží ZAKA Startup 13 j.s.a. (slovenská právní forma), tj. část portfolia je i ve slovenských vehiklech. Ticket: web „The minimum ticket is 130K“ je minimální vklad LP (Startuprise: „minimum limited partner (LP) ticket of €130,000“), ne ticket do firmy, proto nevyplněno. Kapitál nevyplněn: web uvádí „17M Current fund size“ bez měny, Startuprise „€15 million ZAKA VC Fund I opened with a €10.5 million first closing in June 2024“ (cílová velikost a první closing, druh ukazatele výslovně neuveden), CzechCrunch „už vybral 10,5 milionu eur“. Poslední investice: ParcelBio, seed 13 mil. USD (velikost celého kola), vedl Breyer Capital, tisková zpráva ParcelBio přes Business Wire 7. 5. 2026: „with participation from General Catalyst, Y Combinator, Metaplanet, SurgePoint Capital, ZAKA VC, and other investors“. Nástroj neuveden, neprima_indicie (seed). Další: Vetstor, CzechCrunch 9. 12. 2025, Zaka VC a Purple Ventures „se účastní i aktuálního kola“ 1 mil. EUR (velikost kola), kolo neoznačeno, nástroj nezjištěn (dřívější pre-seed 13 mil. Kč; ZAKA Startup 13 j.s.a. je společníkem VETSTOR CZ s.r.o. od 3. 6. 2024, to se týká dřívějšího kola). Yenmo, kolo 1,1 mil. USD (velikost kola), AIN.UA 10. 3. 2025: „The round was backed by Czech ZAKA VC, Pioneer Fund, Team Ignite Ventures, Y Combinator, and angels“, kolo neoznačeno, nástroj nezjištěn. Jistota investice střední: žádná investice nemá doložený nástroj a ParcelBio dokládá jen jedna tisková zpráva. Funding.tech.eu (profil „Zaka VC“) má 13 dealů 2022–2024. Web a stránka novinek uvádějí i další investice z let 2025–2026 (Cirrus Therapeutics, DeepSeq.AI, FinalDose aj.), ty jsem nezávislou zprávou o transakci neověřil. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="7-cz-startupyard"></a>
### 7. StartupYard (`cz-startupyard`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `investice_dolozena_12_24_mesicu` · web [startupyard.com/](https://startupyard.com/)

Nálezy AI: [nalezy_ai.md#cz-startupyard](nalezy_ai.md#cz-startupyard) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „StartupYard Services s.r.o.“, IČO `06002820`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2020-10-15`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06002820](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06002820)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-04-12`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22266852](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22266852)
  - media, Lupa.cz, zdroj_datum `2012-02-02`, puvod `null`: [lupa.cz/clanky/startupyard-zmenil-majitele-sefovat-mu-bude-nikola-rafaj/](https://www.lupa.cz/clanky/startupyard-zmenil-majitele-sefovat-mu-bude-nikola-rafaj/)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [startupyard.com/](https://startupyard.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `investice_dolozena_12_24_mesicu`
- poslední: **Ydoca**, `datum_pro_filtr` `oznameni` → `2025-02-14`; zprávy o transakci: [cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-…](https://cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investovali-depo-ventures-a-startupyard/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Ydoca: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-…](https://cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investovali-depo-ventures-a-startupyard/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „StartupYard Services s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Ydoca“, `datum_investice` `null`, `datum_oznameni` `2025-02-14`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2025-02-14`, puvod `null`: [cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-…](https://cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investovali-depo-ventures-a-startupyard/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Ydoca: CzechCrunch (puvod `null`) [cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-…](https://cc.cz/live/petkrat-rychlejsi-vyberova-rizeni-do-cesko-slovenske-ai-platformy-ydoca-investovali-depo-ventures-a-startupyard/)

**`sektory`**: Sektory odpovídají zdroji
- deep tech, AI, kybernetická bezpečnost, IoT; zdroj [startupyard.com/](https://startupyard.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `25000`, `max` `null`, `mena` `EUR`; zdroj [startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/](https://startupyard.com/the-next-wave-begins-startupyard-announces-batch-15/), zdroj_datum `2025-09-11`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: akcelerátor s vlastním kapitálem, který investuje vlastní peníze do startupů. Web: „Accelerating Startups Since 2011“, „privately funded by Credo Ventures, Rockaway Capital Partners and experienced business angels“; stránka Batch 15 nabízí „€25k as a simple convertible note with the option for higher investment*“; investice do Ydoca doložena zprávou (viz níže). Podle PLAN.md (akcelerátor investující vlastní peníze za podíl s doloženými investicemi) zařazen jako VC. Identita: v ARES skupina subjektů StartupYard se shodným sídlem Perlová 371/5, Praha 1 a jednatelem Nikolou Rafajem (Lupa.cz 2. 2. 2012: „jehož zakladatel Nikola Rafaj se stane ředitelem StartupYardu“): StartupYard Services s.r.o. (IČO 06002820, společník Startup Yard Limited, Londýn), SPV jednotlivých běhů StartupYard Batch 5–15 (např. StartupYard Batch 15 s.r.o., IČO 22266852, vznik 2024-11-14, od 2026-03-21 další společníci vč. KINSKÝ Žďár, a.s.), StartupYard Fintech s.r.o. (IČO 22399356) aj. Jako pravni_subjekt uvádím StartupYard Services s.r.o. jako servisní/provozní společnost značky; že jde o správce značky, ani který subjekt investoval do Ydoca, zdroje výslovně neuvádějí (nepotvrzeno). Sídlo investiční firmy (značky) ČR: všechny české subjekty v Praze; mateřský společník servisní firmy je britský. Ticket: 25 tis. EUR deklarovaný na webu (Batch 15, „optional €25,000 cash investment“, s možností vyšší investice, max neuveden); starší podmínky (30 tis. EUR za 10 % z roku 2014) nepoužity. Kapitál: velikost fondu ani AUM investor neuvádí, prázdné. Sektory dle webu „deep-tech startups such as AI, cybersecurity, IoT, or another cutting-edge field“. Fáze: web uvádí jen podmínku „working prototype“, ne fázi kola, null. Poslední investice: Ydoca, CzechCrunch 14. 2. 2025: „V rámci pre-seed investičního kola startup získal financování v celkové výši 2,3 milionu korun“, „přičemž DEPO Ventures podpořilo projekt částkou 1,8 milionu a StartupYard částkou 500 tisíc korun.“ (500 tis. Kč je vklad StartupYardu podle zdroje, 2,3 mil. Kč velikost kola). Nástroj neprima_indicie (pre-seed), podíl ani konvertibilní nástroj zdroj neuvádí; v ARES má Ydoca s.r.o. (IČO 21364460) jen dva zakladatele po 50 %, StartupYard společníkem není (může jít o konvertibilní nástroj, nepotvrzeno). Jediná zpráva o transakci, proto jistota investice stredni. Datum uzavření neuvedeno. Novější investici (Batch 15 od září 2025, startupy nejmenovány) jsem zprávou nedoložil; funding.tech.eu uvádí poslední deal 2023 (Fungies). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="8-cz-ii-prague"></a>
### 8. i&i Prague (`cz-ii-prague`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `investice_dolozena_12_24_mesicu` · web [iniprague.com/](https://www.iniprague.com/)

Nálezy AI: [nalezy_ai.md#cz-ii-prague](nalezy_ai.md#cz-ii-prague) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „i&i Prague, s.r.o.“, IČO `06058485`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-10-25`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06058485](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06058485)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [iniprague.com/](https://www.iniprague.com/)
  - web_subjektu, ÚOCHB (mateřská instituce), zdroj_datum `null`, puvod `null`: [uochb.cz/en/ini-prague](https://uochb.cz/en/ini-prague)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `investice_dolozena_12_24_mesicu`
- poslední: **CasInvent Pharma**, `datum_pro_filtr` `oznameni` → `2025-06-26`; zprávy o transakci: [positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vy…](https://positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vyvoj-cilene-lecby-nadoru/), [khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-stron…](https://khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-strong-support-from-existing-and-local-investors-to-advance-ck1-inhibitor-development-for-treatment-resistant-cancer-patients/); podpůrné: rejstrik_spolecnik [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - CasInvent Pharma: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`, [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „i&i Prague, s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „CasInvent Pharma“, `datum_investice` `null`, `datum_oznameni` `2025-06-26`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`
  - zprava_o_transakci, Positiv.cz, zdroj_datum `2025-06-26`, puvod `TZ CasInvent Pharma`: [positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vy…](https://positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vyvoj-cilene-lecby-nadoru/)
  - zprava_o_transakci, KHAN-I (převzatá tisková zpráva CasInvent Pharma), zdroj_datum `2025-07-02`, puvod `TZ CasInvent Pharma`: [khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-stron…](https://khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-strong-support-from-existing-and-local-investors-to-advance-ck1-inhibitor-development-for-treatment-resistant-cancer-patients/)
  - rejstrik_spolecnik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-05-30`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- CasInvent Pharma: Positiv.cz (puvod `TZ CasInvent Pharma`) [positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vy…](https://positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vyvoj-cilene-lecby-nadoru/); KHAN-I (převzatá tisková zpráva CasInvent Pharma) (puvod `TZ CasInvent Pharma`) [khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-stron…](https://khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-strong-support-from-existing-and-local-investors-to-advance-ck1-inhibitor-development-for-treatment-resistant-cancer-patients/)

**`sektory`**: Sektory odpovídají zdroji
- drug development, diagnostics, medical technologies, life sciences; zdroj [iniprague.com/](https://www.iniprague.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: vlastní popis „We are a biotech incubator and venture builder“ (iniprague.com), ÚOCHB: „The company provides pre-seed financing for such projects“. Podle pravidel je akcelerátor/inkubátor s vlastním kapitálem a doloženými investicemi za podíl VC: i&i Prague investuje z vlastní společnosti (konvertibilní zápůjčka 100 000 EUR do CasInvent Pharma převedená na akcie, viz níže). Nejde o CVC velké firmy ani o provozní korporaci; jediný společník je IOCB TECH s.r.o. (IČO 28934024, 100 %), firma ÚOCHB AV ČR pro transfer technologií. Identita: ARES i&i Prague, s.r.o., IČO 06058485, Pobřežní 394/12, Praha 8 (shodně s webem), jednatelé David Stíbal (od 2025-04-01, na webu i&i Prague v rozhovoru) a Zuzana Demianová (od 2026-10-01). Oddělení od i&i Biotech Fund: fond i&i Biotech Fund I SCSp (poradce Biotech Investments s.r.o., IČO 10885978) je samostatná investiční firma (viz par_cz-ii-biotech-investments__cz-ii-prague.md); jeho investice (Antiverse, KyDo, Captain T Cell, Theorema aj.) i&i Prague nepřipisuji, ač je databáze Caplight slučuje. Kapitál fondu (45–47 mil. EUR) není kapitálem i&i Prague. Vlastní kapitál ani ticket i&i Prague nikde neuvádí (prázdné). Poslední investice: CasInvent Pharma, a.s. (Brno, IČO 09684221), další investiční kolo bez uvedené výše a bez označení fáze; tisková zpráva CasInvent (Positiv.cz 26. 6. 2025 „Zdroj: TZ Casinvent“; KHAN-I 2. 7. 2025): nové investory JIC Ventures, Garage Angels a Dynumerics „together contributing 50% of the total investment. The remaining investment was backed by longstanding investors including KHAN-I, i&i Prague, and Holeček Family Foundation.“ Nástroj doložen rejstříkem (ARES VR CasInvent, zápis 2025-05-30): valná hromada 22. 5. 2025 zvýšila základní kapitál o 768 000 Kč upsáním akcií třídy C; 48 ks akcií (jmenovitá hodnota 96 000 Kč) „předem určenému zájemci, kterým je společnost i&i Prague, s.r.o. … IČO: 060 58 485“, splacení započtením pohledávky 100 000 EUR „z titulu Smlouvy o konvertibilní zápůjčce (Convertible Loan Agreement)“ ze dne 4. 3. 2025. Rejstřík beru jen jako doklad nástroje, ne data; datum_investice proto null, datum_pro_filtr = oznámení 2025-06-26 (12–24 měsíců). Starší investice mimo okno: CasInvent pre-Series A 1,6 mil. EUR (velikost celého kola) oznámená 30. 1. 2024 (ctt.muni.cz). PerioTrap: Companisto uvádí i&i Prague mezi co-investory bez data a startbase (10. 3. 2026) i&i Prague u kola pre-Series A neuvádí, nepoužito. Nanoflexion: jen inkubace podle TUL/PitchBook, investice nedoložena zprávou. Jistota investice stredni: obě zprávy vycházejí z jedné tiskové zprávy CasInvent. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

## Skupina: Možná chybná vyřazení

<a id="9-cz-orbit-capital"></a>
### 9. Orbit Capital (`cz-orbit-capital`)

Soubor: `hranicni.csv` · rozhodnutí agenta: **hraniční, druh `venture_debt`** · web [orbitcapital.com/](https://orbitcapital.com/)

Nálezy AI: [nalezy_ai.md#cz-orbit-capital](nalezy_ai.md#cz-orbit-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Všechny investice nalezené v okně 24 měsíců (od 2024-10-26) jsou venture debt: Coding Giants – tech.eu 14. 10. 2026: „secured up to €6 million in venture debt financing from Orbit Capital“; Jutro Medical – tech.eu 16. 12. 2025: „The round also includes a debt component from mBank and Orbit Capital“; Sloneek, IAG a Talkin' Things – tech.eu 2. 7. 2026 je uvádí jako investice Growth Debt Fund II („Fund II has already begun deploying capital, with 5 investments so far, including Czech startups Sloneek and IAG … Polish startup Talkin' Things“). Orbit má i strategii Growth Equity (web orbitcapital.com/equity/, Vestbee 2023: minoritní podíly, portfolio Booksy, Mews, Preply, Rohlík), ale equity investici v okně 24 měsíců jsem zprávou o transakci nedoložil (Mews a Preply 2022 podle funding.tech.eu). Cypien AI v profilu funding.tech.eu patří podle VCBacked jinému subjektu (Orbit Ventures). Identita: ARES IČO 08319961 ORBIT Capital GP s.r.o., Thámova 289/13, Praha 8, jednatel a společník Radovan Nesrsta, který je uveden jako Partner na orbitcapital.com/equity/ i /debt/ (IČO identifikuje GP, ne celou skupinu). Kapitál: Growth Debt Fund II druhé uzavření 107 mil. EUR (tech.eu 2. 7. 2026).

**Zdroje uvedené agentem:**
- [tech.eu/2026/10/14/orbit-capital-backs-coding-giants-to-scale-stem-education-…](https://tech.eu/2026/10/14/orbit-capital-backs-coding-giants-to-scale-stem-education-internationally/)
- [tech.eu/2025/12/16/jutro-medical-extends-series-a-to-eur36m-for-ai-enabled-pr…](https://tech.eu/2025/12/16/jutro-medical-extends-series-a-to-eur36m-for-ai-enabled-primary-care-scale/)
- [tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-sca…](https://tech.eu/2026/07/02/orbit-capital-closes-eur107m-venture-debt-fund-for-cee-scaleups/)
- [orbitcapital.com/debt/](https://orbitcapital.com/debt/)
- [orbitcapital.com/equity/](https://orbitcapital.com/equity/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08319961](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08319961)
- [funding.tech.eu/api/v1/investors/Orbit%20Capital](https://funding.tech.eu/api/v1/investors/Orbit%20Capital)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: hranicni.csv, druh `venture_debt` (venture debt je podle PLAN.md bod 3 vyřazen ze základní databáze).
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="10-cz-mcwin-partners"></a>
### 10. McWin Partners (`cz-mcwin-partners`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `neni_investor`** · web [mcwin.cz/](https://mcwin.cz/)

Nálezy AI: [nalezy_ai.md#cz-mcwin-partners](nalezy_ai.md#cz-mcwin-partners) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Kandidát McWin Partners (web mcwin.cz) je podle vlastního webu 'the family office for our founders, Henry McGovern and Steven K. Winegar' ('We are a private investment firm, primarily investing in Unstoppable Trends'), adresa 'Pod Mlýnkem 60/23, 160 00 Praha'. ARES: McWin Partners s.r.o., IČO 08416907, sídlo Ke Kaplance 60, Praha 6, jednatelky Paloma Gamo Gimenez a Małgorzata Ewa McGovern, společníci Ebilux Investment S.à r.l. (Lucembursko) a Metropolitan Properties International s.r.o., činnost správa vlastního majetku a pronájem nemovitostí. Pro tento subjekt jsem v okně 24 měsíců (od 2024-10-26) nenašel žádnou zprávu o transakci: portfolio na mcwin.cz (EasyMile, Exergyn, Astranis, Worldcoin, Substack, NURX aj., bez dat, loga nahraná 2021) žádná zpráva nepotvrzuje a stránka 'Portfolio Funds' popisuje LP pozice ('Our portfolio of funds ranges from well-established PE & VC funds to small niche funds'). Doložené transakce v okně (Ecorobotix series D, Goodwin 14. 10. 2025; funding.tech.eu dále Incapto Coffee 4/2026) patří jiné firmě, McWin Capital Partners ('specialist private equity and venture capital firm', fond McWin Food Tech Fund, adresa London W1D 4AL), na kterou mcwin.cz jen odkazuje ('For more information, please visit McWin Capital Partners'). Bez doložené přímé investice v okně nesplňuje bod 2 PLAN.md.

**Zdroje uvedené agentem:**
- [mcwin.cz/](https://mcwin.cz/)
- [mcwin.cz/contact/](https://mcwin.cz/contact/)
- [mcwin.cz/portfolio/](https://mcwin.cz/portfolio/)
- [mcwin.cz/portfolio-funds/](https://mcwin.cz/portfolio-funds/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08416907](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08416907)
- [mcwin.fund/](https://mcwin.fund/)
- [goodwinlaw.com/en/news-and-events/news/2025/10/announcements-technology-goodw…](https://www.goodwinlaw.com/en/news-and-events/news/2025/10/announcements-technology-goodwin-advises-mcwin-capital-partners-in-ecorobotix-105-million)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `neni_investor`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="11-cz-espira-investments"></a>
### 11. Espira Investments (`cz-espira-investments`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `neni_investor`** · web [espirainvestments.com/](https://www.espirainvestments.com/)

Nálezy AI: [nalezy_ai.md#cz-espira-investments](nalezy_ai.md#cz-espira-investments) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Bez doložené investice v okně 24 měsíců (od 26. 10. 2024). Nejnovější investice podle tiskových zpráv na webu je 'ESPIRA Invests In Czech Premier Clinic' z 8. 2. 2022, poslední zpráva vůbec je exit ICON Communication Centres z 27. 7. 2022; novější transakci jsem nenašel ani v médiích a funding.tech.eu subjekt nezná. Existence: ARES ESPIRA Investments s.r.o., IČO 05528089, sídlo Na Florenci 2116/15, Praha 1, jednatelky a společnice Emília Wardrop Mamajová a Andrea Bartoňová. Subjekt se popisuje jako 'a private equity fund' (typ by byl PE, tedy i tak mimo pilot). Nové investice zakladatelky Mamajové jdou přes samostatnou firmu EVERITA Capital (IČO 19067097, jiný fond a tým), viz cz-everita-capital.

**Zdroje uvedené agentem:**
- [espirainvestments.com/press-releases/](https://www.espirainvestments.com/press-releases/)
- [espirainvestments.com/](https://www.espirainvestments.com/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05528089](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05528089)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `neni_investor`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

## Skupina: Nevyřešení

<a id="12-cz-rockawayx"></a>
### 12. RockawayX (`cz-rockawayx`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web [rockawayx.com/](https://rockawayx.com/)

Nálezy AI: [nalezy_ai.md#cz-rockawayx](nalezy_ai.md#cz-rockawayx) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investice doložena: RockawayX spoluvedla Series A 5 mil. USD (velikost kola) do OnRe, Cointelegraph 5. 5. 2026 'they co-led OnRe's $5 million Series A round' (nástroj neprima_indicie, series A); existence: Blockad s.r.o., IČO 08006458 (provozovatel webu podle patičky, jednatel Viktor Fischer, společník RockawayX a.s. IČO 17457009), sídlo Generála Píky 430/26, Praha 6. Typ ale nejednoznačný: sama se popisuje jako 'multi-strategy digital asset investment firm' a 'global digital asset investment firm' (AUM 1,5–2 mld. USD podle téže stránky), CzechCrunch 27. 8. 2026 uvádí strategie 'venture fondy, tržně neutrální fond, takzvané vaulty přímo na blockchainu a nyní hedgeový fond' a web člení činnost na Investments, Liquidity a Infrastructure (validátory). Oba venture fondy (RockawayX VC I z r. 2021, VC II) jsou na webu 'Closed'; aktivní jsou hedge fond Liquid Opportunities (Kajmanské ostrovy, CIMA) a Market Neutral Fund (Lichtenštejnsko, 'provides capital to digital asset protocols and companies'). Není tedy jasné, zda jde o VC, nebo o multistrategického správce kryptoaktiv, pro kterého typ v PLAN.md chybí. Nejisté je i sídlo: kanceláře Praha, Londýn, New York, Dubaj, české entity jsou v Praze, fondy v zahraničí. Rozhodlo by: z jakého vehiklu a v jaké podobě (equity vs. token vs. úvěr) šla investice do OnRe, zda RockawayX otevírá nový VC fond, a kde sídlí správce fondů.

**Zdroje uvedené agentem:**
- [cointelegraph.com/news/forward-industries-rockawayx-onre-solana-reinsurance](https://cointelegraph.com/news/forward-industries-rockawayx-onre-solana-reinsurance)
- [rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-inv…](https://www.rockawayx.com/insights/rockawayx-and-forward-industries-co-lead-strategic-investment-in-onre)
- [rockawayx.com/funds](https://rockawayx.com/funds)
- [rockawayx.com/](https://rockawayx.com/)
- [cc.cz/cesi-krypto-a-40-miliard-pro-investice-nic-takoveho-zatim-jeste-nikdo-n…](https://cc.cz/cesi-krypto-a-40-miliard-pro-investice-nic-takoveho-zatim-jeste-nikdo-nepostavil-rika-sef-rockawayx/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08006458](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08006458)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="13-cz-lumus-investments"></a>
### 13. LUMUS Investments (`cz-lumus-investments`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ | nastroj`** · web [lumusinvestment.com/](https://www.lumusinvestment.com/)

Nálezy AI: [nalezy_ai.md#cz-lumus-investments](nalezy_ai.md#cz-lumus-investments) (číst až po commitu prvních verdiktů)

**Otázka:** `typ | nastroj` · **možnosti:** `mimo_rozsah_pilotu | neni_investor`

**Důvod agenta (celý):**

> Identita: Lumus Investment Collective s.r.o., IČO 10664335, Kurzova 2222/16, Praha 5 (ARES; jednatelky a společnice Činčurová, Cerchlanová, Jacová, Zamborská = zakladatelky podle CzechCrunch; web uvádí „© 2025 Lumus Investment Collective s.r.o.“). Typ: subjekt se popisuje jako „a community of badass women who are actively and eagerly stepping into the angel investing world“, provozuje „diverse syndicates“ pro andělské investorky; CzechCrunch (4. 11. 2021): „Lumus není klasickým venture kapitálovým fondem“, investice jdou přes SPV, které společně vlastní investorky. Rejstřík ale ukazuje SPV Lumus V s.r.o. (IČO 14358336) a Lumus VI s.r.o. (IČO 17231167) se 100% společníkem Lumus Investment Collective s.r.o. Není tedy jasné, zda jde o andělskou skupinu/syndikát investující za podíl (pak investor mimo pilot, typ není VC ani CVC) nebo o organizátora syndikátu, který investice jen zprostředkovává (pak neni_investor). Investice v okně: Kardi AI, The AI Insider 29. 4. 2025: „The round includes new investment from Lumus Investment Collective“ (kolo 1,1 mil. EUR celkem, ne vklad Lumus); typ kola ani nástroj zdroj neuvádí a Lumus ani jeho SPV nejsou ve výpisu ARES Kardi AI Technologies s.r.o. (IČO 14328127, aktualizace 13. 2. 2026) mezi společníky → nástroj nezjištěn. Novější investice (≥ 2025-10-26) zprávou nedoložena; ArtMaster (2026) jen v portfoliu na webu. Rozhodlo by: doklad, kdo je smluvní stranou investic (Lumus/jeho SPV vs. jednotlivé investorky) a že šlo o podíl či konvertibilní nástroj (např. zápis Lumus SPV jako společníka, smlouva, zpráva uvádějící nástroj).

**Zdroje uvedené agentem:**
- [lumusinvestment.com/](https://www.lumusinvestment.com/)
- [cc.cz/jak-prilakat-k-investovani-do-startupu-vice-zen-ctyri-slovenky-sdruzuji…](https://cc.cz/jak-prilakat-k-investovani-do-startupu-vice-zen-ctyri-slovenky-sdruzuji-uz-250-andelskych-investorek-z-celeho-regionu/)
- [theaiinsider.tech/?p=34048](https://theaiinsider.tech/?p=34048)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/10664335](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/10664335)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14358336](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14358336)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17231167](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17231167)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14328127](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14328127)
- [lumusinvestment.com/portfolio](https://www.lumusinvestment.com/portfolio)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="14-cz-chilli-ventures"></a>
### 14. Chilli Ventures (`cz-chilli-ventures`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web [chilliventures.cz/](https://www.chilliventures.cz/)

Nálezy AI: [nalezy_ai.md#cz-chilli-ventures](nalezy_ai.md#cz-chilli-ventures) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investiční činnost doložená: DecisionRules oznámila 6. 5. 2025 uzavření kola 1,6 mil. EUR (velikost celého kola, ne vklad) vedeného Lighthouse Ventures 'with participation from Czech Founders VC, BD Partners, and Chilli Ventures' (TZ DecisionRules; převzaly Vestbee 6. 5. 2025 a The SaaS News, která kolo označuje 'seed funding'; CzechCrunch 2. 6. 2025 v přehledu dealů) -> nástroj neprima_indicie (seed), status by byl investice_dolozena_12_24_mesicu. Existence: ARES Chilli Ventures a.s., IČO 04106059, sídlo Arnošta z Pardubic 2789, Pardubice, statutáři Jan Mareček a Antonín Mlejnek = managing partner a partner podle webu. Nevyřešený je typ: web se jako VC ani fond neoznačuje; píše 'We are entrepreneurs who have built and continue to grow our own projects. Together, we create, invest...', 'We invest exclusively our own capital', zakládá vlastní provozní firmy ('In-house companies that started with an idea in our group': edera group, enigoo, speedlo, deep vision...), je LP ve VC fondech a investuje do PE fondů (Blackstone, Hamilton Lane...), a vedle toho dělá přímé pre-seed/seed investice ('Typical investment size 200-600k euros for a minority stake'). To odpovídá spíš investičnímu holdingu podnikatelů (Velký soukromý investor) nebo skupině podnikatelů, ale přímé startupové investice za menšinový podíl odpovídají i popisu VC. Agregátory si odporují (funding.tech.eu 'Venture capital', PitchBook podle vyhledávání primárně PE/Buyout). Rozhodlo by: zda je Chilli Ventures a.s. samostatná investiční firma (VC) nebo investiční holding majitelů skupiny (edera aj.), např. podle výroční zprávy/akcionářů ve sbírce listin a vlastního popisu v rozhovoru.

**Zdroje uvedené agentem:**
- [chilliventures.cz/](https://www.chilliventures.cz/)
- [decisionrules.io/articles/decisionrules-raises-eu1-6m-to-scale-automation-glo…](https://www.decisionrules.io/articles/decisionrules-raises-eu1-6m-to-scale-automation-globally)
- [thesaasnews.com/news/decisionrules-raises-1-6-million-in-seed-round](https://www.thesaasnews.com/news/decisionrules-raises-1-6-million-in-seed-round)
- [vestbee.com/blog/articles/decision-rules-secures-1-6-m](https://vestbee.com/blog/articles/decision-rules-secures-1-6-m)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04106059](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04106059)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="15-cz-fond-nase-cesko"></a>
### 15. Fond Naše Česko (`cz-fond-nase-cesko`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web [nase-cesko.cz/](https://www.nase-cesko.cz/)

Nálezy AI: [nalezy_ai.md#cz-fond-nase-cesko](nalezy_ai.md#cz-fond-nase-cesko) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investice je doložená: CzechCrunch 24. 2. 2026 uvádí v pre-seed kole ValkaAI (12 mil. EUR celé kolo, vedl Rockaway Ventures) „Fondu Naše Česko J&T Investiční společnosti“, E15 24. 2. 2026 „fond Naše Česko“ (nástroj neprima_indicie, kolo pre-seed; status by byl aktivni). Typ ale nelze určit: kandidát je fond kvalifikovaných investorů (ARES IČO 75164086 „Naše ČESKO otevřený podílový fond“, Sokolovská 700/113a, Praha 8, vznik 2023-03-31, jen RES, ve VR nenalezen) obhospodařovaný J&T INVESTIČNÍ SPOLEČNOST, a.s. (IČO 47672684), tedy fond pod správcem, ne samostatná investiční firma. Vlastní popis na webu je multi-asset: fond investuje do „soukromý kapitál (private equity), rozvojový kapitál (venture capital), nemovitosti a veřejně obchodovaný kapitál“, „napříč sektory“, od začínajících po zavedené firmy; CzechCrunch 2023 uvádí i dluhopisy CPI a burzovní akcie a startupy „prostřednictvím spřízněných fondů“. funding.tech.eu ho vede jako Venture capital (agregátor, ne vlastní popis), nordic9 jako Bank. Správce J&T IS je obecná investiční společnost (podílové fondy), ne VC. Rozhodlo by: zda vést záznam za správce J&T Investiční společnost / značku Naše Česko a jaký typ jim přiřadit (VC vs. PE / jiný typ mimo pilot); s typem VC by byl zařazen, s jiným typem mimo_rozsah_pilotu. Nejde o duplicitu s J&T Ventures (jiný správce a tým, viz par_cz-fond-nase-cesko__cz-jt-ventures.md).

**Zdroje uvedené agentem:**
- [nase-cesko.cz/](https://www.nase-cesko.cz/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/75164086](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/75164086)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/47672684](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/47672684)
- [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/)
- [e15.cz/byznys/startupy/konkurence-pro-zarubu-a-bosaka-startup-vlastimila-venc…](https://www.e15.cz/byznys/startupy/konkurence-pro-zarubu-a-bosaka-startup-vlastimila-venclika-ziskal-stovky-milionu-a-prichazi-s-ai-komentatory-1431016)
- [cc.cz/blba-nalada-neni-na-miste-cesko-je-na-tom-lepe-nez-se-zda-muzeme-byt-in…](https://cc.cz/blba-nalada-neni-na-miste-cesko-je-na-tom-lepe-nez-se-zda-muzeme-byt-investicni-perla-zni-z-jt/)
- [funding.tech.eu/api/v1/investors/Fond%20Na%C5%A1e%20%C4%8Cesko](https://funding.tech.eu/api/v1/investors/Fond%20Na%C5%A1e%20%C4%8Cesko)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="16-cz-moonhill-capital"></a>
### 16. Moonhill Capital (`cz-moonhill-capital`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ | nastroj`** · web [moonhill.capital/](https://www.moonhill.capital/)

Nálezy AI: [nalezy_ai.md#cz-moonhill-capital](nalezy_ai.md#cz-moonhill-capital) (číst až po commitu prvních verdiktů)

**Otázka:** `typ | nastroj` · **možnosti:** `zarazen | mimo_rozsah_pilotu | neni_investor`

**Důvod agenta (celý):**

> Účast v kolech v okně je doložena: Ekiden seed (Portugal Startup News 5. 5. 2026, převzato z EU-Startups 2026-05: „The round brought together investors including GSR, Flowdesk, Pyth, Aptos, Monolith, Hardcore Labs, Moonhill Capital“) a Turtle Club seed 6,2 mil. USD (Pulse 2.0 18. 5. 2025: „The funding round was led by THEIA… Frachtis, Moonhill Capital, Tulipa Capital“); funding.tech.eu uvádí obě kola (2026-05-04, 2025-05-13). Nástroj: žádný zdroj neuvádí akcie, podíl ani SAFE; jde o web3/krypto projekty a vlastní příspěvek Moonhill o Turtle Club (22. 10. 2024) zdůrazňuje tokenomiku („token holders will benefit from the treasury“), Turtle Club měl TGE 10/2025 – účast mohla být v tokenech, což není podíl ani konvertibilní nástroj podle bodu 2.3. Typ: sám se označuje „MOONHILL CAPITAL manages digital assets for accredited investors“ (meta popis webu) a strategii popisuje jako „investing in leading assets across emerging sectors“ s „Liquid capital … capturing attractive secondary market opportunities“, nabízí market making a „Assisted token launches“; funding.tech.eu ho vede jako „Venture capital“, CB Insights jako „Web3 investment fund“. Není jasné, zda jde o VC (rané investice za podíl), nebo správce kryptoaktiv. Sídlo/identita: web neuvádí adresu ani subjekt; „ETH Prague 2024 – As a home event for us“ (web) a CB Insights uvádějí Prahu; ARES vrací jediný subjekt MOONHILL CAPITAL s.r.o., IČO 09895043, Korunní 2569/108, Praha 10, vznik 2021-02-05 (web: „In 2021, we established Moonhill Capital“), jednatel a společník René Darmoš – vazbu na značku jiný zdroj nepotvrdil, IČO tedy nepotvrzené. Rozhodlo by: doložení nástroje (equity/SAFE vs. tokeny/SAFT) u Ekiden nebo Turtle Club a potvrzení, že Moonhill funguje jako VC (rané investice za podíl) a že správcem je MOONHILL CAPITAL s.r.o. v Praze.

**Zdroje uvedené agentem:**
- [portugalstartupnews.com/2026/05/05/ekiden-raises-e1-7m-to-advance-decentraliz…](https://portugalstartupnews.com/2026/05/05/ekiden-raises-e1-7m-to-advance-decentralized-derivatives-trading-platform/)
- [eu-startups.com/2026/05/ekiden-raises-e1-7-million-at-e17-million-valuation-f…](https://www.eu-startups.com/2026/05/ekiden-raises-e1-7-million-at-e17-million-valuation-for-blockchain-based-trading-platform-out-of-portugal/)
- [pulse2.com/turtle-club-6-2-million-secured-for-advancing-onchain-liquidity-di…](https://pulse2.com/turtle-club-6-2-million-secured-for-advancing-onchain-liquidity-distribution-protocol/)
- [moonhill.capital/](https://www.moonhill.capital/)
- [moonhill.capital/news](https://www.moonhill.capital/news)
- [moonhill.capital/news/moonhill-capital-invests-in-turtle-club](https://www.moonhill.capital/news/moonhill-capital-invests-in-turtle-club)
- [funding.tech.eu/api/v1/investors/Moonhill%20Capital](https://funding.tech.eu/api/v1/investors/Moonhill%20Capital)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09895043](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09895043)
- [cbinsights.com/investor/moonhill-capital](https://www.cbinsights.com/investor/moonhill-capital)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="17-cz-botanique-hospitality"></a>
### 17. Botanique Hospitality (`cz-botanique-hospitality`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web neuveden

Nálezy AI: [nalezy_ai.md#cz-botanique-hospitality](nalezy_ai.md#cz-botanique-hospitality) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investice je doložená: Forbes 25. 2. 2026 píše o seed kole RobosizeME za 2 mil. USD („doplněných o fond Botanique Hospitality“), Pulse 2.0 25. 2. 2026 („as well as Botanique Hospitality“). Předchozí seed kolo RobosizeME z července 2024 (Vestbee, AIN). Kolo seed znamená neprima_indicie, podmínka 3 je splněná jako pracovní předpoklad, takže jde o investora a o výsledku rozhoduje typ. Důkazy o typu si odporují a vlastní popis subjektu chybí (web jsem nenašel). Pro VC mluví Forbes („fond Botanique Hospitality“) a funding.tech.eu (types: Venture capital). Proti VC mluví Vestbee 23. 7. 2024: „Botanique Hospitality Management Group, which owns Botanique Hotel Prague and other hotels in Indonesia“, AIN: „hospitality-focused Czech – Indonesian newly forming Botanique Hospitality Management Group“ a předmět podnikání v ARES (ubytovací služby, nákup, prodej a správa nemovitostí). To odpovídá provozní hotelové skupině, která strategicky investuje do dodavatele hotelového softwaru (Korporátní investor bez samostatné jednotky = mimo_rozsah_pilotu). Doložená je jediná portfoliová firma (RobosizeME). Nejistá je i totožnost a sídlo. ARES vrátil Botanique Hospitality Management s.r.o., IČO 22402934, Sokolovská 204/11, Praha 8, vznik 23. 12. 2024, tedy až po kole z července 2024. Jednatelé a společníci jsou Tomáš Nesvorný a Harianto Solichin (po 50 %). Že tato s.r.o. je investorem v kole 2026 (a ne indonéská nebo jiná entita „Group“), žádný zdroj nedokládá, proto je totožnost nepotvrzená. Otázku by rozhodl vlastní popis subjektu (web, výroční zpráva ve sbírce listin), doklad, která entita investovala, a zda existuje samostatný investiční fond nebo jednotka.

**Zdroje uvedené agentem:**
- [forbes.cz/robosizeme-nabira-investory-startup-autora-kardi-ai-resi-nedostatek…](https://forbes.cz/robosizeme-nabira-investory-startup-autora-kardi-ai-resi-nedostatek-personalu-v-pohostinstvi/)
- [pulse2.com/robosizeme-2-million-raised-to-bring-ai-workflow-automation-to-the…](https://pulse2.com/robosizeme-2-million-raised-to-bring-ai-workflow-automation-to-the-global-hotel-industry)
- [vestbee.com/blog/articles/robosize-me-secures-seed](https://www.vestbee.com/blog/articles/robosize-me-secures-seed)
- [en.ain.ua/2024/07/23/brightcap-leads-seed-round-in-roboszieme-for-hospitality…](https://en.ain.ua/2024/07/23/brightcap-leads-seed-round-in-roboszieme-for-hospitality-automation-expansion)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22402934](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22402934)
- [funding.tech.eu/api/v1/investors/Botanique%20Hospitality](https://funding.tech.eu/api/v1/investors/Botanique%20Hospitality)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="18-cz-braiins"></a>
### 18. Braiins (`cz-braiins`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `nastroj`** · web [braiins.com/](https://braiins.com/)

Nálezy AI: [nalezy_ai.md#cz-braiins](nalezy_ai.md#cz-braiins) (číst až po commitu prvních verdiktů)

**Otázka:** `nastroj` · **možnosti:** `mimo_rozsah_pilotu | neni_investor`

**Důvod agenta (celý):**

> Typ: provozní firma (vlastní popis: „Braiins is a bitcoin mining technology company that develops software, firmware, hardware“), investuje přímo bez doložené samostatné investiční jednotky, tedy Korporátní investor bez samostatné jednotky, mimo pilot v každém případě. Investice Firefish: blog Braiins z 8. 4. 2025 uvádí „In September 2024, Braiins acquired a 15% stake in Firefish“ (podíl doložen, ale datum investice 2024-09 je před hranicí okna 2024-10-26; oznámení kola CzechCrunch 16. 4. 2025 do okna spadá, ale datum_pro_filtr = investice). Jediná transakce v okně: koupě amerického komoditního fondu CAMMS Capital od ETG, uzavřená „na konci letošního dubna“ 2026 (Seznam Zprávy 19. 5. 2026; CzechCrunch 27. 5. 2026 „Jde o fond CAMMS Capital, který Braiins získávají od investiční skupiny ETG“). Zdroje neuvádějí, zda Braiins kupuje podíl ve správcovské firmě (přímá investice za podíl do soukromé firmy), nebo fond/podílové jednotky (investice do fondu), ani podíl v %. Rozhodlo by: tisková zpráva nebo registr (SEC/NFA/CFTC) s tím, jaký subjekt a jaký podíl Braiins nabyl. Pokud jde o podíl ve firmě → mimo_rozsah_pilotu (investor, typ mimo pilot); pokud ne → neni_investor (v okně 24 měsíců žádná jiná doložená přímá investice). Identita: ARES vrací Braiins Systems s.r.o. (IČO 24147931, Křižíkova 148/34, Praha 8; jednatelé Pavel Moravec, Jan Čapek), Braiins Shop, Braiins Services a Braiins Forge; která entita investuje, zdroje neuvádějí (nepotvrzeno).

**Zdroje uvedené agentem:**
- [seznamzpravy.cz/clanek/ekonomika-finance-byznys-meny-kryptomeny-cesky-braiins…](https://www.seznamzpravy.cz/clanek/ekonomika-finance-byznys-meny-kryptomeny-cesky-braiins-rozsiruje-byznys-kupuje-newyorsky-komoditni-fond-306490)
- [cc.cz/cesti-prukopnici-tezby-bitcoinu-jdou-do-ropy-obili-i-kovu-za-stamiliony…](https://cc.cz/cesti-prukopnici-tezby-bitcoinu-jdou-do-ropy-obili-i-kovu-za-stamiliony-kupuji-americky-fond/)
- [braiins.com/blog/braiins-invests-in-bitcoin-backed-lending-platform-firefish-…](https://braiins.com/blog/braiins-invests-in-bitcoin-backed-lending-platform-firefish-in-a-1-8m-seed-round)
- [cc.cz/funguje-jako-zonky-kryte-bitcoiny-v-uschove-jich-ma-mit-za-dve-miliardy…](https://cc.cz/funguje-jako-zonky-kryte-bitcoiny-v-uschove-jich-ma-mit-za-dve-miliardy-cesky-startup-nabira-dalsi-miliony/)
- [braiins.com/](https://braiins.com/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24147931](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24147931)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="19-cz-gi21-capital"></a>
### 19. Gi21 Capital (`cz-gi21-capital`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web [gi21capital.com/](https://gi21capital.com/)

Nálezy AI: [nalezy_ai.md#cz-gi21-capital](nalezy_ai.md#cz-gi21-capital) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investiční činnost je doložená: Vestbee 14. 5. 2026: Zerops „has raised a $2 million seed round led by Gi21 Capital“ (také The SaaS News, zdroj tech.eu); nástroj neprima_indicie (seed, Gi21 jako lead). Identita: ARES Gi21 Capital a.s. (dříve Conwell Capital a.s.), IČO 19584229, Londýnská 2578/54, Praha 2, jediný člen statutárního orgánu i jediný akcionář Damir Špoljarič; Pulse 2.0 (7. 5. 2026) ho uvádí jako zakladatele a Gi21 jako „Prague-based, entrepreneur-led investment firm“ – sídlo ČR. Typ si odporuje: pro VC mluví investice do startupů v pre-seed/seed kolech, sekce „VC/PE technology“ na webu, označení „venture capital and private investment firm“ (The SaaS News) a typ „Venture capital“ ve funding.tech.eu. Proti tomu: Gi21 investuje jen peníze jednoho podnikatele („We only invest our own capital“, „We don’t have limited partners“, „Gi21 has evolved from a family office into a founder-first firm“ – Pulse 2.0), web se popisuje jako „multi-stage investment group“ a „diversified investment firm operating across digital and physical frontiers“ s divizemi datová centra, „Hotels & private aviation“ a mecenášství kultury, což odpovídá spíš typu Velký soukromý investor (investiční holding jednoho podnikatele), případně family office. Rozhodlo by: zda se VC aktivita vede jako samostatná investiční jednotka/značka s vlastním týmem (pak VC → zarazen), nebo jde o jednu z větví osobního investičního holdingu Damira Špoljariče (pak Velký soukromý investor → mimo_rozsah_pilotu).

**Zdroje uvedené agentem:**
- [vestbee.com/blog/articles/zerops-lands-2-m](https://vestbee.com/blog/articles/zerops-lands-2-m)
- [thesaasnews.com/news/zerops-raises-2m-seed-round](https://www.thesaasnews.com/news/zerops-raises-2m-seed-round)
- [pulse2.com/gi21-capital-profile-damir-spoljaric-interview/](https://pulse2.com/gi21-capital-profile-damir-spoljaric-interview/)
- [gi21capital.com/](https://gi21capital.com/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19584229](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19584229)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="20-cz-jet-investment"></a>
### 20. Jet Investment (`cz-jet-investment`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web [jetinvestment.eu/](https://jetinvestment.eu/)

Nálezy AI: [nalezy_ai.md#cz-jet-investment](nalezy_ai.md#cz-jet-investment) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investor podle bodů 2 a 3 je doložený: Jet Investment, a.s. (IČO 03890333, Pisárecká 271/13, Brno, investiční společnost s oprávněním přesáhnout rozhodný limit; představenstvo Igor Fait, Libor Šparlinek, Marek Malík, Lubor Turza; akcionář Jet Founders, a.s.) přes fond Jet Venture 1 investoval 1,8 mil. USD do AppNava ('equity investment', TZ 17. 9. 2026; CzechCrunch 17. 9. 2026 uvádí 4 investice fondu za měsíc: GigaScan, Phantasma Labs, Hermetiq, AppNava) a přes fond Jet 3 'is acquiring a 100% stake' v PEKAŘI a spol. (TZ 11. 9. 2026). Nevyřešený je typ: firma se popisuje jako 'leading Central European investment company' se třemi strategiemi 'Jet Private Equity', 'Jet Real Estate', 'Jet Venture Capital' (AUM '€ 700m+'), v TZ 'specializes in investments in Central European industry' a spravuje 'about CZK 17 billion' ve čtyřech fondech; profil CVCA uvádí 'Buy out, Growth, Rescue/Turnaround, Late-stage venture', ticket 15–80m EUR; CzechCrunch: 'Vedle private equity se v Jet Investment dlouhodobě specializují také na investice do průmyslových nemovitostí'. Zároveň má samostatný VC tým Jet Ventures (Managing Director Kamil Levinský) a fond Jet Venture 1 (cílová velikost 50 mil. EUR, 11 startupů). Převažující fungování ukazuje na PE (mimo_rozsah_pilotu), VC je jedna ze strategií správce. Rozhodlo by: zda se multi-strategický správce s převahou PE a samostatným VC týmem/fondem vede jako PE (VC strategie do poznámky), nebo zda Jet Ventures / Jet Venture 1 je samostatná investiční jednotka hodná typu VC (pak zarazen).

**Zdroje uvedené agentem:**
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03890333](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03890333)
- [jetinvestment.cz/en](https://www.jetinvestment.cz/en)
- [jetinvestment.cz/en/venture-capital](https://www.jetinvestment.cz/en/venture-capital)
- [jetinvestment.cz/en/news/jet-investment-vstupuje-do-americkeho-startupu-appna…](https://www.jetinvestment.cz/en/news/jet-investment-vstupuje-do-americkeho-startupu-appnava-ktery-pomoci-ai-predpovida-chovani-uzivatelu)
- [jetinvestment.cz/en/news/jet-investment-expands-nas-chleb-with-ostrava-based-…](https://www.jetinvestment.cz/en/news/jet-investment-expands-nas-chleb-with-ostrava-based-bakery-pekari-a-spol)
- [cc.cz/brnenska-startupova-ofenziva-miliardar-igor-fait-a-spol-investovali-beh…](https://cc.cz/brnenska-startupova-ofenziva-miliardar-igor-fait-a-spol-investovali-behem-mesice-pres-150-milionu/)
- [cvca.cz/en/jet-investment-2/](https://cvca.cz/en/jet-investment-2/)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="21-cz-kkcg"></a>
### 21. KKCG (`cz-kkcg`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `nastroj`** · web [kkcg.com/en/](https://kkcg.com/en/)

Nálezy AI: [nalezy_ai.md#cz-kkcg](nalezy_ai.md#cz-kkcg) (číst až po commitu prvních verdiktů)

**Otázka:** `nastroj` · **možnosti:** `mimo_rozsah_pilotu | neni_investor`

**Důvod agenta (celý):**

> Typ není VC/CVC v žádné variantě: KKCG se popisuje jako „an investment and innovation group operating a diverse range of companies“, „Founded by Karel Komárek“ (kkcg.com), v TZ „KKCG is an investment and innovation group with expertise in entertainment, energy, technology, real estate and more“; jde o investiční skupinu jednoho podnikatele (velký soukromý investor / PE, mezi nimi jsem nerozhodoval, výsledek to nemění), ne o samostatnou VC jednotku. Identita: KKCG Services a.s. (do 20. 1. 2025 KKCG a.s.), IČO 27107744, Evropská 866/71, Praha 6 (shodné s adresou HQ na webu), jediný akcionář KKCG Group AG, Kapellgasse 21, Luzern (CH). Nástroj: jediná nalezená přímá investice do soukromé firmy v okně 24 měsíců je Zilch (UK), oznámeno 13. 11. 2025: „The funding round was led by KKCG, the Czech investment group“, ale jde o „an equity and debt funding round“ (tech.eu), dluhová část = „expansion of Zilch's securitisation facility led by Deutsche Bank“ (Fintech Times); žádný zdroj neuvádí, zda KKCG vložil equity/akcie, a kolo není označeno jako seed/series, takže nástroj KKCG je nezjištěný. Ostatní transakce nedokládají podmínky: Ferretti (tender offer KKCG Maritime 2026) jsou veřejně obchodované akcie (Euronext Milan); Link-XPV (17. 12. 2025) je investice do fondu (LP), ne do firmy; Avenga (100 %, dokončeno 2/2024, oznámeno 12/2023) je mimo okno; nákupy firem v letech 2025–2026 provádí portfoliová firma Aricoma, ne KKCG přímo. Rozhodlo by: zpráva/TZ, která výslovně uvádí equity (akcie, podíl) účast KKCG v kole Zilch, nebo jiná doložená přímá koupě podílu v soukromé firmě po 26. 10. 2024 (pak mimo_rozsah_pilotu); pokud by účast byla jen dluhová a jiná investice není, neni_investor.

**Zdroje uvedené agentem:**
- [kkcg.com/en/](https://kkcg.com/en/)
- [tech.eu/2025/11/13/zilch-nets-175m-as-eyes-strategic-m-a/](https://tech.eu/2025/11/13/zilch-nets-175m-as-eyes-strategic-m-a/)
- [thefintechtimes.com/?p=130062](https://thefintechtimes.com/?p=130062)
- [pulse2.com/zilch-over-175-million-closed-to-advance-global-growth-and-expand-…](https://pulse2.com/zilch-over-175-million-closed-to-advance-global-growth-and-expand-consumer-payments-platform/amp/)
- [tools.prnewswire.com/en-us/live/20813/release/20260119EN65804](https://tools.prnewswire.com/en-us/live/20813/release/20260119EN65804)
- [lupa.cz/n/kkcg/](https://www.lupa.cz/n/kkcg/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/27107744](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/27107744)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

<a id="22-cz-tarpan-capital"></a>
### 22. Tarpan Capital (`cz-tarpan-capital`)

Soubor: `nevyresene.csv` · rozhodnutí agenta: **nevyřešen, otázka `typ`** · web [tarpangroup.net/tarpan-partners](https://www.tarpangroup.net/tarpan-partners)

Nálezy AI: [nalezy_ai.md#cz-tarpan-capital](nalezy_ai.md#cz-tarpan-capital) (číst až po commitu prvních verdiktů)

**Otázka:** `typ` · **možnosti:** `zarazen | mimo_rozsah_pilotu`

**Důvod agenta (celý):**

> Investice doložena: Filuta AI, seed 4,2 mil. USD (velikost celého kola, ne vklad), oznámeno 2025-06-24 (Rockaway Ventures: „The round also included participation from LionBeat Capital, TARPAN Partners…“; CzechStartups.gov.cz/Startup Kitchen podle Czech P.R.: Ladislav Šelepa „of Tarpan Partners, which was the manager of the investment round and invested in FILUTA AI itself“) – nástroj neprima_indicie (seed), status by byl investice_dolozena_12_24_mesicu. Typ si odporuje: vlastní web TARPAN Partners se popisuje jako „nezávislá poradenská společnost zaměřená na ekonomické a finanční poradenství“ (M&A, kapitálové poradenství, investice formou „společné investování se svými klienty“), reference jsou jen poradenské mandáty a v kole Filuta byla zároveň manažerem kola; naproti tomu agregátor Caplight uvádí „TARPAN.VC is a venture capital fund based in Prague“ (založeno 2018, jediné portfolio Filuta AI). Nejasný je i investující subjekt: TARPAN Partners s.r.o. (IČO 24733792) nebo TARPAN Capital s.r.o. (IČO 09228497, předmět „Správa vlastního majetku“, společník TARPAN Group v.o.s.), oba se sídlem Václavské nám. 773/4, Praha 1. Pokud jde o VC (samostatný fond/značka TARPAN.VC se sídlem v ČR) → zarazen; pokud poradenská firma spoluinvestující z vlastní společnosti (korporátní investor bez samostatné jednotky) → mimo_rozsah_pilotu. Rozhodlo by: vlastní popis TARPAN.VC/TARPAN Capital (web, rozhovor), doklad, který subjekt drží podíl ve Filutě (Filuta AI CZ s.r.o. má jediného společníka Filuta AI Inc., takže český rejstřík nepomůže), a další doložené vlastní investice.

**Zdroje uvedené agentem:**
- [rockawayventures.com/rockaway-ventures-leads-4-2m-seed-round-in-czech-ai-star…](https://rockawayventures.com/rockaway-ventures-leads-4-2m-seed-round-in-czech-ai-startup-filuta-ai/)
- [czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round…](https://czechstartups.gov.cz/en/novinky/investors-believe-in-ai-investment-seed-round-brings-filuta-ai-startup-4-2-million/)
- [tarpangroup.net/tarpan-partners](https://www.tarpangroup.net/tarpan-partners)
- [tarpangroup.net/sluzby/tarpan-partners/investice](https://www.tarpangroup.net/sluzby/tarpan-partners/investice)
- [caplight.com/investor/tarpanpartners-cz](https://www.caplight.com/investor/tarpanpartners-cz)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09228497](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09228497)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24733792](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24733792)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí).
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí).
- **`duvod`**: Agent správně popsal, co chybí nebo si odporuje.
- Zvolený typ nebo nástroj uvedu v poznámce.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `duvod`

## Skupina: Ostatní

<a id="23-cz-garage-angels"></a>
### 23. Garage Angels (`cz-garage-angels`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web neuveden

Nálezy AI: [nalezy_ai.md#cz-garage-angels](nalezy_ai.md#cz-garage-angels) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor, ale typ není VC/CVC: klub andělských investorů. Forbes 16. 2. 2026: 'Klub více než dvaceti andělských investorů, mezi nimiž nechybějí jména jako Jiří Hlavenka, Karel Obluk...', 'Průměrná výše investic se pohybuje kolem čtyř set tisíc eur... a podílí se na nich od čtyř do dvanácti investorů'; Lupa 21. 3. 2019: uskupení jednotlivých investorů, které žádá jen 'minoritní podíl'. Fungování podle rejstříku: Garage Angels z.s. (IČO 21814414, Orlí 483/1, Brno) vlastní 100 % Garage Angels Management s.r.o. (IČO 21657505), která je jednatelem jednoúčelových společností pro jednotlivé dealy (GA Investiční VRV s.r.o., IČO 24325244; GA Investiční GCOM s.r.o., IČO 19462867), jejichž společníky jsou jednotliví andělé (J. Hlavenka, K. Obluk, DENDIS VENTURES s.r.o., A. Filipenský aj.); fond ani upsaný kapitál nemá. Investice v okně doložená: Forbes 16. 2. 2026 'Nedávno podpořili nižšími stovkami tisíc eur firmu VR Life' a rakouský Sendance 'v obdobné výši'; ARES: GA Investiční VRV s.r.o. zapsána jako společník VR LIFE s.r.o. (IČO 07460481) od 2026-01-27 (podíl doložen). Sídlo ČR (Brno), ale typ = andělský klub/syndikát (Angel), ne VC ani CVC.

**Zdroje uvedené agentem:**
- [forbes.cz/andele-z-garaze-nakopli-moravu-ted-klub-elitnich-investoru-miri-za-…](https://forbes.cz/andele-z-garaze-nakopli-moravu-ted-klub-elitnich-investoru-miri-za-hranice/)
- [lupa.cz/aktuality/hlavenka-obluk-a-spol-rozjizdi-garage-angels-a-budou-invest…](https://www.lupa.cz/aktuality/hlavenka-obluk-a-spol-rozjizdi-garage-angels-a-budou-investovat-do-startupu/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21814414](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21814414)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21657505](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/21657505)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24325244](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24325244)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19462867](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19462867)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07460481](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07460481)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="24-cz-look-ai-ventures"></a>
### 24. Look AI Ventures (`cz-look-ai-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [lookai.vc/](https://lookai.vc/)

Nálezy AI: [nalezy_ai.md#cz-look-ai-ventures](nalezy_ai.md#cz-look-ai-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Look AI Ventures SICAV, a.s.“, IČO `17604087`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-10-07`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17604087](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17604087)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-04-22`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06385745](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06385745)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [lookai.vc/](https://lookai.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Sodex Innovations**, `datum_pro_filtr` `oznameni` → `2026-07-13`; zprávy o transakci: [tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligen…](https://tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligence-to-construction-sites/); podpůrné: portfolio_web [lookai.vc/](https://lookai.vc/)
- další: **Lucida AI**, `datum_pro_filtr` `oznameni` → `2026-06-30`; zprávy o transakci: [tech.eu/2026/06/30/lucida-ai-closes-7m-seed-round-for-speech-to-speech-ai/](https://tech.eu/2026/06/30/lucida-ai-closes-7m-seed-round-for-speech-to-speech-ai/), [lupa.cz/aktuality/cesi-investovali-do-konkurenta-duolinga-ktery-pro-vyuku-jaz…](https://www.lupa.cz/aktuality/cesi-investovali-do-konkurenta-duolinga-ktery-pro-vyuku-jazyku-nabizi-treba-ai-persony/)
- další: **Digicust**, `datum_pro_filtr` `oznameni` → `2025-12-03`; zprávy o transakci: [digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized](https://digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized), [trendingtopics.eu/digicust-zoll-23-millionen-euro/](https://www.trendingtopics.eu/digicust-zoll-23-millionen-euro/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Sodex Innovations: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Lucida AI: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [tech.eu/2026/06/30/lucida-ai-closes-7m-seed-round-for-speech-to-speech-ai/](https://tech.eu/2026/06/30/lucida-ai-closes-7m-seed-round-for-speech-to-speech-ai/)
  - Digicust: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized](https://digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Look AI Ventures SICAV, a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Sodex Innovations“, `datum_investice` `null`, `datum_oznameni` `2026-07-13`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`
  - zprava_o_transakci, tech.eu, zdroj_datum `2026-07-13`, puvod `null`: [tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligen…](https://tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligence-to-construction-sites/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [lookai.vc/](https://lookai.vc/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Sodex Innovations: tech.eu (puvod `null`) [tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligen…](https://tech.eu/2026/07/13/sodex-innovations-secures-4m-to-bring-real-time-intelligence-to-construction-sites/)
- Lucida AI: tech.eu (puvod `null`) [tech.eu/2026/06/30/lucida-ai-closes-7m-seed-round-for-speech-to-speech-ai/](https://tech.eu/2026/06/30/lucida-ai-closes-7m-seed-round-for-speech-to-speech-ai/); Lupa.cz (puvod `null`) [lupa.cz/aktuality/cesi-investovali-do-konkurenta-duolinga-ktery-pro-vyuku-jaz…](https://www.lupa.cz/aktuality/cesi-investovali-do-konkurenta-duolinga-ktery-pro-vyuku-jazyku-nabizi-treba-ai-persony/)
- Digicust: Digicust (tisková zpráva firmy) (puvod `null`) [digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized](https://digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized); Trending Topics (puvod `https://digicust.com/en/blog/digicust-pre-series-a-financing-round-finalized`) [trendingtopics.eu/digicust-zoll-23-millionen-euro/](https://www.trendingtopics.eu/digicust-zoll-23-millionen-euro/)

**`sektory`**: Sektory odpovídají zdroji
- AI; zdroj [lookai.vc/](https://lookai.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web 'the first investment fund in the Czech Republic that focuses exclusively on AI startups worldwide', pre-Series A venture capital fund; doložené investice do startupů. Značka a tým sídlí v Praze (kancelář Karla Engliše 5, Praha 5; registrované sídlo fondu Radlická 180/50, Praha 5), proto zeme CZ. Identita: ARES Look AI Ventures SICAV, a.s., IČO 17604087 (fond kvalifikovaných investorů, podfond Look AI Ventures I, IČO 75163705), individuální statutární orgán / obhospodařovatel do 5. 10. 2026 AVANT investiční společnost, a.s., od 5. 10. 2026 FTP Dimension investiční společnost, a.s. (web uvádí FTP Dimension jako správce). Provozní tým: Look AI Investments, a.s., IČO 06385745 (dříve AI Startup Incubator a.s., Radlická 180/50, Praha 5), akcionář SICAV na účet podfondu Look AI Ventures I; ve správní radě Martin Havlík a Daniel Kunz, které web uvádí jako Managing Partner a Partner. Záznam vedu za značku, fond a správce jsou podřízené údaje. Ticket: web ho neuvádí ('The terms and conditions of the investment are always drawn up to fit your startup'); tech.eu 13. 4. 2023 píše 'The targeted investment amount in one start-up is €250,000' bez citace investora, proto nevyplněno. Vklad do Digicust 250 000 EUR je jednotlivá investice, ne deklarovaný ticket. Kapitál: jen cíl 'aims to raise €20 million' (tech.eu 2023, záměr, ne velikost fondu), web velikost neuvádí, proto prázdné. Poslední investice: Sodex Innovations, tech.eu 13. 7. 2026: 'The round also welcomed new investors Bloomhaus, Look AI Ventures and the German business angel group Superangels'; kolo 4 mil. EUR (velikost celého kola) bez označení fáze, nástroj nezjištěn. Lucida AI: tech.eu 30. 6. 2026 seed kolo navýšené na 7 mil. USD (velikost celého kola) 'with participation from Next Tier Ventures, Look AI Ventures...'; Lupa.cz 30. 6. 2026 'Český fond Look AI Ventures se podílel na investici do startupu Lucida AI'; nástroj neprima_indicie (seed); nezávislost obou zpráv nedoložena (pravděpodobně společný podklad). Digicust: TZ firmy 3. 12. 2025 'the Look.AI Fund is contributing €250,000', celé kolo 2,3 mil. EUR, firma kolo označuje jako 'pre-Series A' i 'seed round'; Trending Topics vychází ze stejné TZ (jeden zdroj); zmínka o převodu na equity se týká zakladatelů a soukromých investorů, ne Look AI, proto neprima_indicie. Žádná investice nemá nástroj dolozeno, jistota investice stredni. funding.tech.eu uvádí 9 kol 2023–2026 (vodítko, ne doklad), mj. Checkstep 5/2026 (nedohledáno ve zprávě, nezapsáno). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="25-cz-jic-ventures"></a>
### 25. JIC Ventures (`cz-jic-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [jic.cz/en/potreby-a-sluzby/jic-ventures](https://www.jic.cz/en/potreby-a-sluzby/jic-ventures)

Nálezy AI: [nalezy_ai.md#cz-jic-ventures](nalezy_ai.md#cz-jic-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „JIC General Partner s.r.o.“, IČO `24074004`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-12-20`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24074004](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24074004)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-01-07`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24320358](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24320358)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-02-02`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04156293](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04156293)
  - media, Lupa.cz, zdroj_datum `2026-04-07`, puvod `null`: [lupa.cz/aktuality/v-brne-vznikl-fond-pro-startupy-ktery-bude-investovat-i-pen…](https://www.lupa.cz/aktuality/v-brne-vznikl-fond-pro-startupy-ktery-bude-investovat-i-penize-kraje/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **FaceUp**, `datum_pro_filtr` `oznameni` → `2026-05-19`; zprávy o transakci: [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do), [cc.cz/byl-to-studentsky-projekt-ted-uz-ma-hodnotu-pres-pul-miliardy-nabidky-n…](https://cc.cz/byl-to-studentsky-projekt-ted-uz-ma-hodnotu-pres-pul-miliardy-nabidky-na-odkup-odmitame-hlasi-cesi/), [lupa.cz/aktuality/whistleblowing-platforma-faceup-ziskala-pres-100-milionu-i-…](https://www.lupa.cz/aktuality/whistleblowing-platforma-faceup-ziskala-pres-100-milionu-i-od-brnenskeho-fondu-s-nimz-investuje-biskupstvi/); podpůrné: portfolio_web [jic.cz/en/potreby-a-sluzby/jic-ventures](https://www.jic.cz/en/potreby-a-sluzby/jic-ventures)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - FaceUp: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „JIC General Partner s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „FaceUp“, `datum_investice` `null`, `datum_oznameni` `2026-05-19`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`
  - zprava_o_transakci, JIC (tisková zpráva), zdroj_datum `2026-05-19`, puvod `null`: [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do)
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2026-05-19`, puvod `https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do`: [cc.cz/byl-to-studentsky-projekt-ted-uz-ma-hodnotu-pres-pul-miliardy-nabidky-n…](https://cc.cz/byl-to-studentsky-projekt-ted-uz-ma-hodnotu-pres-pul-miliardy-nabidky-na-odkup-odmitame-hlasi-cesi/)
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2026-05-19`, puvod `https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do`: [lupa.cz/aktuality/whistleblowing-platforma-faceup-ziskala-pres-100-milionu-i-…](https://www.lupa.cz/aktuality/whistleblowing-platforma-faceup-ziskala-pres-100-milionu-i-od-brnenskeho-fondu-s-nimz-investuje-biskupstvi/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [jic.cz/en/potreby-a-sluzby/jic-ventures](https://www.jic.cz/en/potreby-a-sluzby/jic-ventures)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- FaceUp: JIC (tisková zpráva) (puvod `null`) [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do); CzechCrunch (puvod `https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do`) [cc.cz/byl-to-studentsky-projekt-ted-uz-ma-hodnotu-pres-pul-miliardy-nabidky-n…](https://cc.cz/byl-to-studentsky-projekt-ted-uz-ma-hodnotu-pres-pul-miliardy-nabidky-na-odkup-odmitame-hlasi-cesi/); Lupa.cz (puvod `https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do`) [lupa.cz/aktuality/whistleblowing-platforma-faceup-ziskala-pres-100-milionu-i-…](https://www.lupa.cz/aktuality/whistleblowing-platforma-faceup-ziskala-pres-100-milionu-i-od-brnenskeho-fondu-s-nimz-investuje-biskupstvi/)

**`sektory`**: Sektory odpovídají zdroji
- deep tech, SaaS; zdroj [jic.cz/en/potreby-a-sluzby/jic-ventures](https://www.jic.cz/en/potreby-a-sluzby/jic-ventures), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `null`, `max` `1000000`, `mena` `EUR`; zdroj [jic.cz/en/potreby-a-sluzby/jic-ventures](https://www.jic.cz/en/potreby-a-sluzby/jic-ventures), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web se popisuje 'JIC Ventures is a Brno-born VC fund backing technology founders from pre-seed to exit' a 'lead[s] rounds'; fond s cca 40 investory (LP), většina kapitálu soukromá (Lupa.cz 7. 4. 2026), doložená investice za podíl do startupu. Iniciátorem je inovační agentura JIC (zájmové sdružení právnických osob, IČO 71180478), která drží 51 % ve správci; nejde o CVC (JIC není velká korporace) ani o akcelerátor bez kapitálu. Identita: správce/GP JIC General Partner s.r.o., IČO 24074004, Purkyňova 649/127, Brno, jednatelé a společníci Radim Kocourek a Miloš Sochor (po 24,5 %), JIC 51 %; Lupa.cz jmenuje Kocourka a Sochora jako vedení fondu. Fond: JIC Ventures 2 a.s., osoba rizikového kapitálu, IČO 24320358 (zapsán 2026-01-05, člen správní rady JIC General Partner s.r.o.). Starší investiční vehikl JIC Ventures, s.r.o., IČO 04156293 (100 % JIC, jednatel Radim Kocourek od 2021) – stejná značka a tým, jeden záznam. Sídlo Brno, CZ. Ticket: web 'Tickets up to €1M' (min neuveden). Kapitál nevyplněn: Lupa.cz uvádí, že fond 'hodlá se 400 miliony korun pomoct' a že fond není finálně uzavřený; Pulse2 (12. 4. 2026) 'The fund totals approximately CZK 400 million', ale bez citace investora a bez rozlišení upsaný/cílový – jde spíš o záměr/cíl, proto nezapsáno. Sektory podle webu 'Deep tech, SaaS, and other'. Poslední investice: FaceUp, série A, kterou vedl Fil Rouge Capital za účasti JIC Ventures; velikost celého kola 5 mil. USD (TZ JIC, CzechCrunch ~105 mil. Kč) resp. 'přes 110 milionů Kč' (Lupa.cz) – jde o velikost kola, ne vklad JIC Ventures; drobná nesrovnalost v částce se netýká firmy, data ani investora. Datum podpisu/uzavření neuvedeno, proto datum_oznameni 2026-05-19 (TZ JIC). Nástroj neprima_indicie (série A), podíl výslovně neuveden. Jistota investice stredni: CzechCrunch a Lupa.cz vyšly týž den jako TZ JIC a vlastní zjištění nedokládají (CzechCrunch navíc uvádí valuaci 'má se pohybovat' nad půl miliardy, původ nejasný), nezávislost nedoložena. funding.tech.eu uvádí ještě Eterny (2025-09) a Symfio (2025-08, pre-seed), zprávu o transakci jsem nečetl, proto nezapsány. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="26-cz-purple-ventures"></a>
### 26. Purple Ventures (`cz-purple-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [purple-ventures.com/](https://www.purple-ventures.com/)

Nálezy AI: [nalezy_ai.md#cz-purple-ventures](nalezy_ai.md#cz-purple-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Purple Ventures s.r.o.“, IČO `05775574`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-01-02`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05775574](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05775574)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [purple-ventures.com/](https://www.purple-ventures.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Comparables.ai**, `datum_pro_filtr` `oznameni` → `2026-10-06`; zprávy o transakci: [tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for…](https://tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for-dealmakers/), [lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy…](https://www.lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy-ze-sveta-do-projektu-se-zapojuji-cesi/); podpůrné: portfolio_web [purple-ventures.com/](https://www.purple-ventures.com/)
- další: **Vetstor**, `datum_pro_filtr` `oznameni` → `2025-12-09`; zprávy o transakci: [cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-des…](https://cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-desitky-milionu-ted-ma-i-od-kijonkove/); podpůrné: portfolio_web [purple-ventures.com/](https://www.purple-ventures.com/)
- další: **Talentiqa**, `datum_pro_filtr` `oznameni` → `2025-09-29`; zprávy o transakci: [cc.cz/prvni-kolo-pohovoru-dela-umela-inteligence-v-cezu-i-bageterii-boulevard…](https://cc.cz/prvni-kolo-pohovoru-dela-umela-inteligence-v-cezu-i-bageterii-boulevard-jeji-tvurci-ted-ziskali-25-milionu/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Comparables.ai: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for…](https://tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for-dealmakers/)
  - Vetstor: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Talentiqa: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Purple Ventures s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Comparables.ai“, `datum_investice` `null`, `datum_oznameni` `2026-10-06`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`
  - zprava_o_transakci, Tech.eu, zdroj_datum `2026-10-06`, puvod `null`: [tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for…](https://tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for-dealmakers/)
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2026-10-13`, puvod `null`: [lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy…](https://www.lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy-ze-sveta-do-projektu-se-zapojuji-cesi/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [purple-ventures.com/](https://www.purple-ventures.com/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Comparables.ai: Tech.eu (puvod `null`) [tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for…](https://tech.eu/2026/10/06/comparablesai-secures-6m-seed-to-scale-its-ai-platform-for-dealmakers/); Lupa.cz (puvod `null`) [lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy…](https://www.lupa.cz/aktuality/finove-pry-s-ai-behem-minut-najdou-byznysove-zajimave-firmy-ze-sveta-do-projektu-se-zapojuji-cesi/)
- Vetstor: CzechCrunch (puvod `null`) [cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-des…](https://cc.cz/vedla-miliardovou-sit-zverimexu-po-rodicovske-hlida-zdravi-mazlicku-desitky-milionu-ted-ma-i-od-kijonkove/)
- Talentiqa: CzechCrunch (puvod `null`) [cc.cz/prvni-kolo-pohovoru-dela-umela-inteligence-v-cezu-i-bageterii-boulevard…](https://cc.cz/prvni-kolo-pohovoru-dela-umela-inteligence-v-cezu-i-bageterii-boulevard-jeji-tvurci-ted-ziskali-25-milionu/)

**`sektory`**: Sektory odpovídají zdroji
- tech-enabled, purpose-driven technology startups; zdroj [purple-ventures.com/](https://www.purple-ventures.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `250000`, `max` `400000`, `mena` `EUR`; zdroj [purple-ventures.com/](https://www.purple-ventures.com/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web 'We are a venture capital fund investing into CEE+ tech-enabled innovations in pre-seed and seed stages.', 'Minority equity stake'. Je členem skupiny Purple Holding (patička webu 'member of Purple Holding'), ale vystupuje jako samostatný VC fond; druhý fond je podle CzechCrunch (26. 3. 2024) otevřen externím investorům a skupina do něj dává 14 mil. EUR z cíle 40 mil. EUR, CzechCrunch 30. 1. 2025 uvádí 35 externích investorů. Proto VC, ne korporátní investor. Identita: ARES Purple Ventures s.r.o. (do 2017 Purple Holding s.r.o.), IČO 05775574, Masarykova 409/26, Brno; jednatelé Jakub Nytra a Jan Staněk (na webu General Partner a Managing General Partner), jediný společník Purple Holding a.s. (IČO 06528554). Web uvádí stejné IČO. Existuje i Purple Ventures Advisory s.r.o. (IČO 19836155, Masarykova 410/28, Brno, jednatel Jakub Nytra), jako investiční subjekt nepoužit. Ticket deklarovaný webem: '€250k to €400k' 'initial ticket size, later follow-ons'. Sektory: web 'early-stage purpose-driven technology startups with initial revenue and global ambitions', bez výčtu odvětví. Kapitál: web uvádí 'Fund II has raised over CZK 700 million' bez data (zmínka 'Strong 2025') a v podobě dolní hranice; Lupa (březen 2026) 'přes 780 milionů' ve fondu, cíl fondu II 40 mil. EUR. Přesná částka upsaného kapitálu ani datum nejsou uvedeny, cíl není kapitál, proto kapital prázdný. Fond I kolem 15 mil. EUR (CzechCrunch 26. 3. 2024) nezapisuji, protože médium neuvádí, zda jde o velikost fondu podle investora. Poslední investice: Comparables.ai (Finsko), seed 6 mil. USD (velikost celého kola), vedly Pragmatech a Araya Ventures, Tech.eu 6. 10. 2026: 'with participation from Purple Ventures'; Lupa.cz 13. 10. 2026: 'Český fond Purple Ventures se zapojil 10 miliony Kč' (vklad v tomto kole, není to deklarovaný ticket). Nástroj neprima_indicie (seed). Lupa.cz cituje Jana Staňka a fotografii má od Purple Ventures, pravděpodobně vychází z podkladů fondu; nezávislost na zdroji Tech.eu nedoložena, a protože žádná investice nemá dolozeno, jistota investice stredni. Další: Vetstor, kolo 1 mil. EUR (velikost kola), CzechCrunch 9. 12. 2025: Zaka VC a Purple Ventures 'se účastní i aktuálního kola', kolo neoznačeno, nástroj nezjištěn; Talentiqa, 25 mil. Kč (velikost kola), CzechCrunch 29. 9. 2025, kolo neoznačeno, nástroj nezjištěn. funding.tech.eu (profil 'Purple Ventures', aliasy 'Purple') obsahuje i řadu francouzských firem (Woodoo, Bonx, Zealy, Lupin & Holmes); může jít o sloučení s jiným investorem 'Purple', proto profil nepoužívám jako doklad. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="27-cz-reflex-capital"></a>
### 27. Reflex Capital (`cz-reflex-capital`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [reflexcapital.com/](https://www.reflexcapital.com/)

Nálezy AI: [nalezy_ai.md#cz-reflex-capital](nalezy_ai.md#cz-reflex-capital) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Reflex Capital SE“, IČO `24269158`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-07-13`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24269158](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24269158)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [reflexcapital.com/](https://www.reflexcapital.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Grid.online**, `datum_pro_filtr` `oznameni` → `2026-06-22`; zprávy o transakci: [cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-no…](https://cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-novy-startup-uz-ma-150-milionu/), [e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zme…](https://www.e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zmenit-zpusob-dorucovani-baliku-1433723); podpůrné: portfolio_web [reflexcapital.com/](https://www.reflexcapital.com/)
- další: **Merchantee**, `datum_pro_filtr` `oznameni` → `2026-06-03`; zprávy o transakci: [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/), [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/); podpůrné: portfolio_web [reflexcapital.com/](https://www.reflexcapital.com/)
- další: **Choice**, `datum_pro_filtr` `oznameni` → `2026-03-16`; zprávy o transakci: [tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-opera…](https://tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-operating-system-across-europe/), [thenextweb.com/news/restaurant-tech-startup-choice-closes-7-1m-series-a](https://thenextweb.com/news/restaurant-tech-startup-choice-closes-7-1m-series-a); podpůrné: portfolio_web [reflexcapital.com/](https://www.reflexcapital.com/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Grid.online: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`, [cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-no…](https://cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-novy-startup-uz-ma-150-milionu/)
  - Merchantee: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/)
  - Choice: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-opera…](https://tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-operating-system-across-europe/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Reflex Capital SE“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Grid.online“, `datum_investice` `null`, `datum_oznameni` `2026-06-22`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2026-06-22`, puvod `null`: [cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-no…](https://cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-novy-startup-uz-ma-150-milionu/)
  - zprava_o_transakci, E15, zdroj_datum `2026-06-22`, puvod `oznámení firmy Grid.online (rubrika Tiskové zprávy, „Firma oznámila“)`: [e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zme…](https://www.e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zmenit-zpusob-dorucovani-baliku-1433723)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [reflexcapital.com/](https://www.reflexcapital.com/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Grid.online: CzechCrunch (puvod `null`) [cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-no…](https://cc.cz/opustil-vlastni-firmu-a-vsadil-na-to-ze-zlepsi-dorucovani-baliku-pro-novy-startup-uz-ma-150-milionu/); E15 (puvod `oznámení firmy Grid.online (rubrika Tiskové zprávy, „Firma oznámila“)`) [e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zme…](https://www.e15.cz/tiskove-zpravy/startup-navazany-na-grid-online-ziskal-miliony-chce-zmenit-zpusob-dorucovani-baliku-1433723)
- Merchantee: Nordic9 (puvod `null`) [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/); CzechCrunch (puvod `null`) [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/)
- Choice: Tech.eu (puvod `null`) [tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-opera…](https://tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-operating-system-across-europe/); The Next Web (puvod `null`) [thenextweb.com/news/restaurant-tech-startup-choice-closes-7-1m-series-a](https://thenextweb.com/news/restaurant-tech-startup-choice-closes-7-1m-series-a)

**`sektory`**: Sektory odpovídají zdroji
- nevyplněno (`null`)

**`ticket`**: Ticket odpovídá zdroji
- `min` `1000000`, `max` `2000000`, `mena` `EUR`; zdroj [cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startu…](https://cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startupy-pres-pul-miliardy/), zdroj_datum `2023-12-22`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `22000000`, `mena` `EUR`, `druh` `fund_size`, `plati_k` `2023-12-22`, `fond` `třetí fond Reflex Capital (název ve zdroji neuveden)`; zdroj [cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startu…](https://cc.cz/nova-sila-pro-reflex-capital-ondreje-fryce-ve-tretim-fondu-ma-na-startupy-pres-pul-miliardy/), zdroj_datum `2023-12-22`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: CzechCrunch (22. 12. 2023) jej popisuje „ve venture kapitálovém fondu Reflex Capital“, Tech.eu/TNW „a Czech VC“; zakladatel Ondřej Fryc k třetímu fondu: „Původně jsme chtěli dvacet milionů, nakonec jsme upsali dvaadvacet, ale investory jsme také odmítali“, tj. fond s externími investory. Fondy jsou v ARES zapsány jako osoby rizikového kapitálu (Reflex 2, osoba rizikového kapitálu SE, IČO 08240051; Reflex 3, osoba rizikového kapitálu SE, IČO 19381263; obě sídlo Rašínovo nábřeží 2000/78, Praha 2, statutár Josef Chvojka, vydávají investiční akcie) – podřízené údaje, ne samostatní investoři. Web se sám typem neoznačuje („We at Reflex Capital are entrepreneurs, just like you“, „We're partners, not bankers“). Souhrn vyhledávání zmínil, že Reflex začínal jako family office; zdroj jsem nečetl a současné fungování (fondy s externími upisovateli) odpovídá VC, proto VC. Identita: ARES Reflex Capital SE, IČO 24269158 (dříve Spread Capital SE), sídlo Rašínovo nábřeží 2000/78, Praha 2, shodné s adresou na webu („Reflex Capital SE, Rašínovo Nábřeží 2000/78“); člen představenstva Josef Chvojka, kterého web uvádí mezi partnery. Sídlo investiční firmy ČR (web uvádí i kancelář v San Francisku). Ticket: Ondřej Fryc v CzechCrunch 2023: „při naší typické investici mezi jedním až dvěma miliony eur“ (deklarace investora v rozhovoru, starší údaj). Kapitál: CzechCrunch 2023 „Uzavřel svůj třetí fond o velikosti dvaadvacet milionů eur“; zapsáno jako fund_size k datu článku (přesné datum uzavření neuvedeno, Fryc mluví o upsání). Údaj web „€150M invested“ je proinvestovaná částka, ne AUM, nezapsán. Fondy nesčítám. Sektory a fáze investor nevymezuje, null. Poslední investice: Grid.online, CzechCrunch 22. 6. 2026: „Připojili se i stávající podílníci z českých fondů Reflex Capital Ondřeje Fryce a J&T Ventures.“; v tabulce „Jak vypadá majetková struktura Grid.online?“ „Reflex Capital: 11,6 %“; na přelomu roku J&T Ventures, Reflex Capital a Juraj Atlas vložili 750 tis. EUR „formou konvertibilního úvěru, který se nyní propisuje do vlastnické struktury“. Nástroj proto podíl doložen (výslovně uvedený vlastnický podíl, konvertibilní úvěr převáděný na podíl); typ kola zdroj neuvádí. 4 mil. EUR je velikost celého kola, ne vklad Reflexu. E15 týž den (tiskové zprávy, „Firma oznámila“): „V projektu pokračují také dosavadní investoři Reflex Capital a J&T Ventures.“ Obě zprávy vyšly týž den a zřejmě vycházejí z oznámení firmy, nezávislost nedoložena, proto jistota investice stredni. Datum uzavření neuvedeno. Další: Merchantee – Nordic9 3. 6. 2026 „led by Reflex Capital“ (pre-seed, 1,8 mil. EUR / v textu 2,1 mil. USD), CzechCrunch 9. 6. 2026 „Kolo vedl fond Reflex Capital za účasti Czech Founders VC a Lighthouse Ventures.“ jako „rozšíření svého původního, takzvaného seed investičního kola“ o 30 mil. Kč (velikosti kola, ne vklad); označení kola se liší (pre-seed vs. rozšíření seedu), firma, investor ani období ne, kolo zapsáno podle CzechCrunch. Choice – Tech.eu 16. 3. 2026 „Alea Capital Partners led the funding, with participation from Reflex Capital, Smartlink, and J&T Ventures“, series A 7,1 mil. USD (velikost kola). Agregátory uvádějí i FaceUp series A (5/2026), ale dostupný výpis Reflex mezi investory nejmenuje, proto nezapsáno. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="28-cz-soulmates-ventures"></a>
### 28. Soulmates Ventures (`cz-soulmates-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [soulmatesventures.com/](https://www.soulmatesventures.com/)

Nálezy AI: [nalezy_ai.md#cz-soulmates-ventures](nalezy_ai.md#cz-soulmates-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Soulmates Ventures, osoba rizikového kapitálu, s.r.o.“, IČO `09789561`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-05-13`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09789561](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09789561)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [soulmatesventures.com/](https://www.soulmatesventures.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Rightcharge**, `datum_pro_filtr` `oznameni` → `2026-09-03`; zprávy o transakci: [uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmat…](https://www.uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmates-ventures-blackwood-ventures-and-purple-ventures/), [vestbee.com/insights/articles/rightcharge-raises-500-k](https://vestbee.com/insights/articles/rightcharge-raises-500-k), [pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20…](https://pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20x-arr-growth/); podpůrné: portfolio_web [soulmatesventures.com/](https://www.soulmatesventures.com/)
- další: **Antiverse**, `datum_pro_filtr` `oznameni` → `2026-03-03`; zprávy o transakci: [techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseas…](https://techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseases-with-no-effective-treatments/), [vestbee.com/insights/articles/antiverse-raises-9-3-m](https://vestbee.com/insights/articles/antiverse-raises-9-3-m); podpůrné: portfolio_web [soulmatesventures.com/](https://www.soulmatesventures.com/)
- další: **Rightcharge**, `datum_pro_filtr` `oznameni` → `2025-10-23`; zprávy o transakci: [uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-le…](https://www.uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-led-by-soulmates-ventures/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Rightcharge: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmat…](https://www.uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmates-ventures-blackwood-ventures-and-purple-ventures/)
  - Antiverse: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseas…](https://techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseases-with-no-effective-treatments/)
  - Rightcharge: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-le…](https://www.uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-led-by-soulmates-ventures/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Soulmates Ventures, osoba rizikového kapitálu, s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Rightcharge“, `datum_investice` `null`, `datum_oznameni` `2026-09-03`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`
  - zprava_o_transakci, UKTN (UK Tech News), zdroj_datum `2026-09-03`, puvod `tisková zpráva Rightcharge (formát TZ s datelinou a 'ENDS', nepojmenovaná)`: [uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmat…](https://www.uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmates-ventures-blackwood-ventures-and-purple-ventures/)
  - zprava_o_transakci, Vestbee, zdroj_datum `2026-09-03`, puvod `tisková zpráva Rightcharge (formát TZ s datelinou a 'ENDS', nepojmenovaná)`: [vestbee.com/insights/articles/rightcharge-raises-500-k](https://vestbee.com/insights/articles/rightcharge-raises-500-k)
  - zprava_o_transakci, Pulse 2.0, zdroj_datum `2026-09-03`, puvod `tisková zpráva Rightcharge (formát TZ s datelinou a 'ENDS', nepojmenovaná)`: [pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20…](https://pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20x-arr-growth/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [soulmatesventures.com/](https://www.soulmatesventures.com/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Rightcharge: UKTN (UK Tech News) (puvod `tisková zpráva Rightcharge (formát TZ s datelinou a 'ENDS', nepojmenovaná)`) [uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmat…](https://www.uktechnews.info/2026/09/03/rightcharge-secures-500000-investment-from-soulmates-ventures-blackwood-ventures-and-purple-ventures/); Vestbee (puvod `tisková zpráva Rightcharge (formát TZ s datelinou a 'ENDS', nepojmenovaná)`) [vestbee.com/insights/articles/rightcharge-raises-500-k](https://vestbee.com/insights/articles/rightcharge-raises-500-k); Pulse 2.0 (puvod `tisková zpráva Rightcharge (formát TZ s datelinou a 'ENDS', nepojmenovaná)`) [pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20…](https://pulse2.com/rightcharge-raises-growth-funding-to-expand-across-europe-after-20x-arr-growth/)
- Antiverse: Tech Funding News (puvod `null`) [techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseas…](https://techfundingnews.com/antiverse-lands-9-3m-can-it-be-a-turning-point-for-diseases-with-no-effective-treatments/); Vestbee (puvod `nepojmenovaný podklad ('as Vestbee was informed')`) [vestbee.com/insights/articles/antiverse-raises-9-3-m](https://vestbee.com/insights/articles/antiverse-raises-9-3-m)
- Rightcharge: UKTN (UK Tech News) (puvod `null`) [uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-le…](https://www.uktechnews.info/2025/10/23/rightcharge-secures-1-6-million-seed-investment-led-by-soulmates-ventures/)

**`sektory`**: Sektory odpovídají zdroji
- air, water, energy, mobility, education, healthcare, food and agriculture, circular economy; zdroj [soulmatesventures.com/](https://www.soulmatesventures.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `null`, `max` `3000000`, `mena` `EUR`; zdroj [soulmatesventures.com/](https://www.soulmatesventures.com/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `62000000`, `mena` `EUR`, `druh` `aum`, `plati_k` `null`, `fond` `null`; zdroj [soulmatesventures.com/](https://www.soulmatesventures.com/), zdroj_datum `null`
- kapital[1]: `castka` `50000000`, `mena` `EUR`, `druh` `fund_size`, `plati_k` `2025-03-18`, `fond` `fond Article 9 SFDR (název ve zprávě neuveden)`; zdroj [vestbee.com/insights/articles/soulmates-ventures-raises-50-m-fund](https://www.vestbee.com/insights/articles/soulmates-ventures-raises-50-m-fund), zdroj_datum `2025-03-18`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web 'We back bold, innovative entrepreneurs building a more sustainable future', článek na webu o sobě 'a small and young VC from Prague'; v rejstříku 'osoba rizikového kapitálu' s předmětem 'Správa majetku srovnatelná s obhospodařováním dle § 15 zákona č. 240/2013 Sb.'; vlastní akcelerační program (dříve 'green-investing accelerator company'), ale investuje vlastní fond za podíl ve vedených kolech, tedy VC. funding.tech.eu typ 'Venture capital'. Identita: Soulmates Ventures, osoba rizikového kapitálu, s.r.o. (dříve Soulmates CEE Fund s.r.o., Soulmates Investments...), IČO 09789561, Rohanské nábřeží 693/10, Praha 8 (shodné s druhou pražskou kanceláří na webu; web uvádí 'Prague HQ' Boudníkova 2538/13, Praha 8), jednatel Hynek Sochor (web: Founder), prokurista Michal Sikyta (web: Managing Partner). Jediný společník Soulmates Ventures Fund SICAV, a.s. (IČO 23302054, Hvězdova 1716/2b, Praha 4, statutár AVANT investiční společnost, a.s.), jehož podfond SVF 01 má IČO 75165708; fond je podřízený údaj, ne samostatný investor. Sídlo CZ. Ticket: web 'We fund each company with an initial investment of up to €3,000,000' (Vestbee 18. 3. 2025 navíc follow-on až 5 mil. EUR). Kapitál: web 'Assets Under Management' '€62M' (bez data, plati_k null); Vestbee 18. 3. 2025 'has raised a €50 million fund' (zapsáno jako fund_size; zakladatel na LinkedIn uvádí '€62M ... Article 9 SFDR fund' – údaje se zřejmě překrývají, nesčítat). Poslední investice: Rightcharge (Londýn, EV fleet charging), £500 000 (velikost celého kola, ne vklad Soulmates), UKTN 3. 9. 2026 'with Soulmates Ventures leading the round alongside BlackWood Ventures and Purple Ventures'; titulek UKTN 'Seed investment', tělo i Vestbee/Pulse 2.0 'growth funding round' – kolo označeno nejednotně, kolo seed převzato z titulku UKTN. Všechny tři zprávy z 3. 9. 2026 zřejmě vycházejí ze stejné TZ, jeden původ. Datum uzavření neuvedeno, proto datum_oznameni. Další: Antiverse (Cardiff), série A 9,3 mil. USD (velikost kola), Tech Funding News 3. 3. 2026 'The round was led by Soulmates Ventures' (vlastní rozhovor s zakladatelem), Vestbee 3. 3. 2026 'The round was led by Soulmates Ventures'; Development Bank of Wales uvádí 'a joint equity investment' jen za IIC a DBW, Soulmates nejmenuje, proto nástroj u Soulmates jen neprima_indicie. Rightcharge seed £1,6 mil. (velikost kola) UKTN 23. 10. 2025 'The round was led by Soulmates Ventures'. Nástroj: u žádné investice výslovně neuveden podíl, jen označení kol (seed, série A) – neprima_indicie, proto jistota investice stredni (nezávislost Vestbee od TFN u Antiverse navíc nedoložena). funding.tech.eu uvádí i FluoSphera, Better Medicine (pre-seed 08/2025), Lendorse (06/2025), Fusebox (01/2025); zprávy jsem nečetl nebo jen ve výsledcích hledání, nezapsány. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="29-cz-y-soft-ventures"></a>
### 29. Y Soft Ventures (`cz-y-soft-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `CVC` · země `CZ` · status `investice_dolozena_12_24_mesicu` · web [ysoft.com/ventures](https://www.ysoft.com/ventures)

Nálezy AI: [nalezy_ai.md#cz-y-soft-ventures](nalezy_ai.md#cz-y-soft-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Y Soft Ventures Management, a.s., Technická 2948/13, Královo Pole, 616 00 Brno (správce; investiční vehikly Y Soft Ventures, a.s., IČO 29314445, a Y Soft Ventures II, a.s., IČO 07890150)“, IČO `04504593`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-04-15`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04504593](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04504593)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-07-31`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/29314445](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/29314445)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-06-06`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07890150](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07890150)
  - media, The Recycler, zdroj_datum `2025-07-02`, puvod `null`: [therecycler.com/posts/new-leadership-for-y-soft-ventures/](https://therecycler.com/posts/new-leadership-for-y-soft-ventures/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `investice_dolozena_12_24_mesicu`
- poslední: **RoboTwin (RoboTwin s.r.o., IČO 14091682)**, `datum_pro_filtr` `oznameni` → `2025-07-02`; zprávy o transakci: [eitjumpstarter.eu/robotwin-secures-1-million-eur/](https://eitjumpstarter.eu/robotwin-secures-1-million-eur/), [cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-m…](https://cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-maji-desitky-milionu/), [therecycler.com/posts/new-leadership-for-y-soft-ventures/](https://therecycler.com/posts/new-leadership-for-y-soft-ventures/); podpůrné: rejstrik_spolecnik [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14091682](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14091682), portfolio_web [ysoft.com/ventures](https://www.ysoft.com/ventures)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - RoboTwin (RoboTwin s.r.o., IČO 14091682): `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `pre-seed`, [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14091682](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14091682)

**`typ`**: Typ je zařazen správně
- `typ`: `CVC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `CVC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Y Soft Ventures Management, a.s., Technická 2948/13, Královo Pole, 616 00 Brno (správce; investiční vehikly Y Soft Ventures, a.s., IČO 29314445, a Y Soft Ventures II, a.s., IČO 07890150)“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „RoboTwin (RoboTwin s.r.o., IČO 14091682)“, `datum_investice` `null`, `datum_oznameni` `2025-07-02`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `pre-seed`
  - zprava_o_transakci, EIT Jumpstarter, zdroj_datum `2025-07-02`, puvod `null`: [eitjumpstarter.eu/robotwin-secures-1-million-eur/](https://eitjumpstarter.eu/robotwin-secures-1-million-eur/)
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2025-09-11`, puvod `null`: [cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-m…](https://cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-maji-desitky-milionu/)
  - zprava_o_transakci, The Recycler, zdroj_datum `2025-07-02`, puvod `null`: [therecycler.com/posts/new-leadership-for-y-soft-ventures/](https://therecycler.com/posts/new-leadership-for-y-soft-ventures/)
  - rejstrik_spolecnik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-06-14`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14091682](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14091682)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [ysoft.com/ventures](https://www.ysoft.com/ventures)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- RoboTwin (RoboTwin s.r.o., IČO 14091682): EIT Jumpstarter (puvod `null`) [eitjumpstarter.eu/robotwin-secures-1-million-eur/](https://eitjumpstarter.eu/robotwin-secures-1-million-eur/); CzechCrunch (puvod `null`) [cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-m…](https://cc.cz/cesi-resi-urgentni-problem-evropy-od-byvalych-akcionaru-ppf-ci-eu-ted-maji-desitky-milionu/); The Recycler (puvod `null`) [therecycler.com/posts/new-leadership-for-y-soft-ventures/](https://therecycler.com/posts/new-leadership-for-y-soft-ventures/)

**`sektory`**: Sektory odpovídají zdroji
- Internet of Things, Industry 4.0, Smart Office, Retail 2.0, Smart City, Cyber Security, Big Data & Analytics, AR/VR (B2B); zdroj [ysoft.com/ventures](https://www.ysoft.com/ventures), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ CVC: Y Soft Ventures je samostatná investiční jednotka (vlastní právnické osoby a tým) firmy Y Soft Corporation, a.s. (IČO 26197740). Web: „We invest in the people who build innovative B2B tech startups in Central and Eastern Europe“ a je součástí Y Soft; The Recycler (2. 7. 2025) ji nazývá „the venture capital arm of enterprise office solutions provider Y Soft Corporation“, iToday (9. 11. 2021) „venture kapitálová platforma spadající pod Y Soft Corporation“. Identita: ARES vrací Y Soft Ventures Management, a.s. (IČO 04504593, Technická 2948/13, Brno), představenstvo Lukáš Konečný (předseda) a Václav Muchna; tato společnost je statutárním orgánem obou investičních vehiklů Y Soft Ventures, a.s. (IČO 29314445, dříve Y Soft Venture Capital SE) a Y Soft Ventures II, a.s. (IČO 07890150), všechny se sídlem Technická 2948/13, Brno. Jména odpovídají webu (Lukáš Konečný Managing Partner, Václav Muchna) a The Recycler (Konečný Managing Partner od 1. 7. 2025), totožnost potvrzena. Vehikly jsou podřízené údaje, ne samostatní investoři. Ticket ani kapitál investor na webu neuvádí, proto nevyplněno (Lupa/Forbes uvádějí starší záměry investovat, to není kapitál; databáze třetích stran s rozsahy ticketů nejsou deklarace investora). Poslední investice: RoboTwin, pre-seed kolo 1,25 mil. EUR (velikost celého kola včetně grantu EU, ne vklad Y Soft Ventures). EIT Jumpstarter 2. 7. 2025: „BD Partners, Y Soft Ventures and Jörg Rupp will fuel RoboTwin’s market expansion“, kolo „pre-seed“. CzechCrunch 11. 9. 2025 jmenuje Y Soft Ventures mezi investory pre-seed kola, financování „ve formě grantu Horizon Europe z programu EU a ekvitního financování od soukromých investorů“. The Recycler 2. 7. 2025: „The latest investment is in the deep-tech startup RoboTwin.“ Nástroj podíl doložen zápisem: v rejstříku RoboTwin s.r.o. (IČO 14091682) je Y Soft Ventures II, a.s. společníkem od 11. 6. 2025 (podíl 4327/174520), což je jen podpůrný doklad, datum investice z něj neberu. Datum pro filtr je oznámení 2025-07-02, tedy starší než 12 měsíců, status investice_dolozena_12_24_mesicu. Jistota investice střední: tři zprávy, ale nezávislost původu nedoložena (CzechCrunch píše „Letos již hlásili“, tj. vychází z dřívějšího oznámení; The Recycler pravděpodobně z tiskové zprávy Y Soft). The Recycler zároveň uvádí, že YSV „transitions from its investment phase to executing its first exits“ (portfolio management), novější investici jsem nenašel. Funding.tech.eu má jen 3 dealy z let 2015–2016. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="30-cz-lighthouse-ventures"></a>
### 30. Lighthouse Ventures (`cz-lighthouse-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [lhv.vc/](https://lhv.vc/)

Nálezy AI: [nalezy_ai.md#cz-lighthouse-ventures](nalezy_ai.md#cz-lighthouse-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Lighthouse Ventures GP s.r.o.“, IČO `07500912`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2024-04-03`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07500912](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07500912)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [lhv.vc/](https://lhv.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Hermetiq**, `datum_pro_filtr` `oznameni` → `2026-08-24`; zprávy o transakci: [lupa.cz/aktuality/cesky-miliardar-investuje-do-americke-firmy-ktera-pomoci-ai…](https://www.lupa.cz/aktuality/cesky-miliardar-investuje-do-americke-firmy-ktera-pomoci-ai-automatizuje-buildovani-softwaru/); podpůrné: portfolio_web [lhv.vc/](https://lhv.vc/)
- další: **Merchantee**, `datum_pro_filtr` `oznameni` → `2026-06-03`; zprávy o transakci: [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/), [raising.fi/news/merchantee-undisclosed-june-2026](https://raising.fi/news/merchantee-undisclosed-june-2026); podpůrné: portfolio_web [lhv.vc/](https://lhv.vc/)
- další: **Ranketta**, `datum_pro_filtr` `oznameni` → `2025-11-27`; zprávy o transakci: [vestbee.com/insights/articles/ranketta-secures-1-m](https://www.vestbee.com/insights/articles/ranketta-secures-1-m), [cc.cz/delal-vyzkum-s-mikolovem-v-jednadvaceti-ma-vlastni-startup-umoznuje-byt…](https://cc.cz/delal-vyzkum-s-mikolovem-v-jednadvaceti-ma-vlastni-startup-umoznuje-byt-videt-v-chatech-s-ai/); podpůrné: portfolio_web [lhv.vc/](https://lhv.vc/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Hermetiq: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Merchantee: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/)
  - Ranketta: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [vestbee.com/insights/articles/ranketta-secures-1-m](https://www.vestbee.com/insights/articles/ranketta-secures-1-m)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Lighthouse Ventures GP s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Hermetiq“, `datum_investice` `null`, `datum_oznameni` `2026-08-24`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2026-08-24`, puvod `null`: [lupa.cz/aktuality/cesky-miliardar-investuje-do-americke-firmy-ktera-pomoci-ai…](https://www.lupa.cz/aktuality/cesky-miliardar-investuje-do-americke-firmy-ktera-pomoci-ai-automatizuje-buildovani-softwaru/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [lhv.vc/](https://lhv.vc/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Hermetiq: Lupa.cz (puvod `null`) [lupa.cz/aktuality/cesky-miliardar-investuje-do-americke-firmy-ktera-pomoci-ai…](https://www.lupa.cz/aktuality/cesky-miliardar-investuje-do-americke-firmy-ktera-pomoci-ai-automatizuje-buildovani-softwaru/)
- Merchantee: Nordic9 (puvod `null`) [nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/](https://nordic9.com/news/merchantee-raised-18-million-in-a-pre-seed-fu/); Raising.fi (puvod `null`) [raising.fi/news/merchantee-undisclosed-june-2026](https://raising.fi/news/merchantee-undisclosed-june-2026)
- Ranketta: Vestbee (puvod `informace od firmy/investorů („as Vestbee was informed“)`) [vestbee.com/insights/articles/ranketta-secures-1-m](https://www.vestbee.com/insights/articles/ranketta-secures-1-m); CzechCrunch (puvod `informace od firmy/investorů (shodné datum a citace investorů jako Vestbee; nezávislý původ nedoložen)`) [cc.cz/delal-vyzkum-s-mikolovem-v-jednadvaceti-ma-vlastni-startup-umoznuje-byt…](https://cc.cz/delal-vyzkum-s-mikolovem-v-jednadvaceti-ma-vlastni-startup-umoznuje-byt-videt-v-chatech-s-ai/)

**`sektory`**: Sektory odpovídají zdroji
- B2B software, fintech, AI; zdroj [lhv.vc/](https://lhv.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `200000`, `max` `1000000`, `mena` `EUR`; zdroj [lhv.vc/](https://lhv.vc/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web se popisuje „Lighthouse Ventures is an early-stage venture capital, focused on technology projects with global vision“, Vestbee „a venture capital firm based in Prague, Czech Republic“; doložené investice do startupů v pre-seed kolech. Web uvádí „Lighthouse Seed Fund benefits from the support and financing of the Czech ESIF Fund of Funds (CZFoF)“ a „Start year of most recent Fund II: 2024“; fondy jsou podřízené údaje, právní subjekt fondu jsem v ARES nenašel (hledání „Lighthouse“ vrátilo jen GP). Identita: ARES Lighthouse Ventures GP s.r.o., IČO 07500912, sídlo Evropská 2758/11, Praha 6 (shodné s adresou kanceláře na webu „Evropská 2758/11, 160 00, Prague 6“), jednatel Michal Zálešák, kterého web i Vestbee uvádějí jako Managing Partner; společníci Michal Zálešák a Vladislav Vintner po 50 %. Předmět podnikání v rejstříku obecný. Sídlo investiční firmy ČR. Ticket deklaruje web: „Investment in a single startup: From €200k to €1m“; sektory „B2B Software of various verticals, Fintech, AI“; fáze „Idea / Seed“. Kapitál: nevyplněn; web velikost Fund II neuvádí; rozhovor CzechCrunch z 6. 4. 2020 (https://cc.cz/nejde-o-zdroj-penez-ale-jak-fondy-podporuji-startupy-v-rozvoji-i-pres-krizi-investujeme-dal-rika-zalesak-z-lighthouse-ventures/) uvádí „Celkem máme k dispozici zhruba 24 milionů eur“ a „celkovým kapitálem na úrovni 600 milionů korun“ – formulace „k dispozici“ a údaj redakce nejsou deklarovaný aum/committed/fund size a týkají se prvního fondu v roce 2020, proto prázdné. Poslední investice: Hermetiq (USA, AI pro software), Lupa.cz 24. 8. 2026 jmenuje mezi investory „a dále Lighthouse Ventures“; velikost celého kola 2,2 mil. USD (ne vklad Lighthouse), lead Jet Investment (750 tis. USD); Lupa typ kola neuvádí, Raising.fi (27. 8. 2026) ho označuje za seed, ale Lighthouse nejmenuje, proto nástroj nezjisteno. Další: Merchantee, Nordic9 3. 6. 2026: „Merchantee raised €1.8 million in a pre-seed funding round led by Reflex Capital“, „with participation from Czech Founders VC and Lighthouse Ventures“; Raising.fi 9. 6. 2026 „led by Reflex Capital, with participation from Lighthouse Ventures“ (kolo jako „undisclosed funding round“); 1,8 mil. EUR je velikost celého kola; Nordic9 uvádí v textu i 2,1 mil. USD (nejednotná částka, ne rozpor ve firmě, datu ani investorovi). Ranketta (Brno, AI viditelnost značek), Vestbee 27. 11. 2025: „The round was led by Lighthouse Ventures, with participation from Gi21 Capital“, „€1 million in pre-seed funding“; CzechCrunch týž den „tzv. pre-seed investici“, 1 mil. EUR (24 mil. Kč) je velikost celého kola. Nástroj: žádná investice nemá výslovně podíl/akcie, podmínka 3 se opírá o neprima_indicie (pre-seed, Merchantee a Ranketta), proto jistota investice stredni. Nezávislost: Vestbee a CzechCrunch publikovaly Rankettu tentýž den a obě zjevně vycházejí z informací firmy/investorů, Nordic9 a Raising.fi původ neuvádějí, nezávislost nedoložena. Agregátory (Caplight, PitchBook) uvádějí i BeatPulse Labs (6/2026), Deplace AI (2/2026), Prodeen (2026), zprávu o transakci jsem k nim nedohledal, proto nepoužity. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="31-cz-czech-founders-vc"></a>
### 31. Czech Founders VC (`cz-czech-founders-vc`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [czechfounders.vc/](https://czechfounders.vc/)

Nálezy AI: [nalezy_ai.md#cz-czech-founders-vc](nalezy_ai.md#cz-czech-founders-vc) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Czech Founders Ventures s.r.o., osoba rizikového kapitálu“, IČO `17051835`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2024-07-26`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17051835](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17051835)
  - media, CzechCrunch, zdroj_datum `2022-09-07`, puvod `null`: [cc.cz/uspesni-cesti-startupiste-budou-pomahat-novym-nadejim-vybrali-na-to-mez…](https://cc.cz/uspesni-cesti-startupiste-budou-pomahat-novym-nadejim-vybrali-na-to-mezi-sebou-ctvrt-miliardy/)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [czechfounders.vc/](https://czechfounders.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Merchantee**, `datum_pro_filtr` `oznameni` → `2026-06-09`; zprávy o transakci: [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/); podpůrné: portfolio_web [czechfounders.vc/](https://czechfounders.vc/)
- další: **Maxfusion**, `datum_pro_filtr` `oznameni` → `2026-01-14`; zprávy o transakci: [cc.cz/umoznuji-hromadne-tvorit-videoreklamy-i-s-ai-herci-izraelci-buduji-star…](https://cc.cz/umoznuji-hromadne-tvorit-videoreklamy-i-s-ai-herci-izraelci-buduji-startup-z-prahy-ziskali-investici/); podpůrné: portfolio_web [czechfounders.vc/](https://czechfounders.vc/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Merchantee: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/)
  - Maxfusion: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Czech Founders Ventures s.r.o., osoba rizikového kapitálu“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Merchantee“, `datum_investice` `null`, `datum_oznameni` `2026-06-09`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2026-06-09`, puvod `null`: [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [czechfounders.vc/](https://czechfounders.vc/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Merchantee: CzechCrunch (puvod `null`) [cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-ce…](https://cc.cz/resi-jeden-z-nejvetsich-problemu-evropskych-e-shopu-kvituje-investor-cesi-ziskali-dalsi-desitky-milionu/)
- Maxfusion: CzechCrunch (puvod `null`) [cc.cz/umoznuji-hromadne-tvorit-videoreklamy-i-s-ai-herci-izraelci-buduji-star…](https://cc.cz/umoznuji-hromadne-tvorit-videoreklamy-i-s-ai-herci-izraelci-buduji-startup-z-prahy-ziskali-investici/)

**`sektory`**: Sektory odpovídají zdroji
- nevyplněno (`null`)

**`ticket`**: Ticket odpovídá zdroji
- `min` `50000`, `max` `350000`, `mena` `EUR`; zdroj [czechfounders.vc/](https://czechfounders.vc/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `10000000`, `mena` `EUR`, `druh` `committed_capital`, `plati_k` `2022-09-07`, `fond` `null`; zdroj [cc.cz/uspesni-cesti-startupiste-budou-pomahat-novym-nadejim-vybrali-na-to-mez…](https://cc.cz/uspesni-cesti-startupiste-budou-pomahat-novym-nadejim-vybrali-na-to-mezi-sebou-ctvrt-miliardy/), zdroj_datum `2022-09-07`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: pre-seed fond zakladatelů pro firmy z CEE („Czech Founders VC mission is based on the need for a founders-focused investor“, „Pre-seed tickets. Typically €50-350k“, „No more than 15% equity“, czechfounders.vc); CzechCrunch (2022-09-07) jej popisuje jako fond regulovaný jako alternativní investiční fond, s podíly „maximálně patnáct procent“. Sídlo Praha. Identita: web uvádí „© Czech Founders Ventures s.r.o.“; ARES: Czech Founders Ventures s.r.o., osoba rizikového kapitálu, IČO 17051835, Salvátorská 931/8, Praha 1, jednatelé a společníci Vít Horký, Václav Pavlečka, Ivan Kristeľ, což odpovídá partnerům fondu podle CzechCrunch. Není totožný s neziskovou Czech Founders z.ú. (IČO 09761187). Kapitál: CzechCrunch uvádí „Všichni zde zmínění složili dohromady deset milionů eur, přibližně čtvrt miliardy korun“ (původní cíl 5 mil. EUR zdvojnásoben); zapsáno jako committed_capital k datu článku, údaj z roku 2022. Ticket 50–350 tis. EUR deklarovaný na webu a v CzechCrunch. Sektory investor nevymezuje (široké spektrum oborů), proto null. Velikost kol (ne vklad CF VC): Merchantee rozšíření seed kola o dalších 30 mil. Kč k původním 15 mil. Kč z roku 2024 (vedl Reflex Capital, dále Lighthouse Ventures; zakladatel o něm mluví jako o „něco jako bridge round“), funding.tech.eu uvádí 1,8 mil. EUR; Maxfusion 350 tis. EUR (spolu s andělem a zakladateli). Nástroj: Merchantee neprima_indicie (CzechCrunch: „rozšíření svého původního, takzvaného seed investičního kola“, „Kolo vedl fond Reflex Capital za účasti Czech Founders VC a Lighthouse Ventures.“), Maxfusion nezjištěn; obecně web deklaruje equity do 15 %. Jistota investice střední: jediná zpráva o transakci, žádný dolozeno. Data jsou data oznámení, datum uzavření zdroje neuvádějí. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední (agregátory jako PitchBook uvádějí další kola, např. AdSpawn 2026-04, které jsem zprávou neověřoval).

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="32-cz-depo-ventures"></a>
### 32. DEPO Ventures (`cz-depo-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [depoventures.com/](https://depoventures.com/)

Nálezy AI: [nalezy_ai.md#cz-depo-ventures](nalezy_ai.md#cz-depo-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „DEPO VENTURES, s.r.o.“, IČO `04753101`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-05-13`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04753101](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04753101)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [depoventures.com/](https://depoventures.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Zvook**, `datum_pro_filtr` `oznameni` → `2026-10-12`; zprávy o transakci: [kyivpost.com/post/86941](https://kyivpost.com/post/86941)
- další: **Tapaya**, `datum_pro_filtr` `oznameni` → `2026-04-29`; zprávy o transakci: [vestbee.com/blog/articles/tapaya-secures-1-m](https://vestbee.com/blog/articles/tapaya-secures-1-m); podpůrné: portfolio_web [depoventures.com/latest/turning-any-smartphone-into-a-payment-terminal-czech-…](https://depoventures.com/latest/turning-any-smartphone-into-a-payment-terminal-czech-fintech-tapaya-has-raised-eur-1-million)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Zvook: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Tapaya: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [vestbee.com/blog/articles/tapaya-secures-1-m](https://vestbee.com/blog/articles/tapaya-secures-1-m)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „DEPO VENTURES, s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Zvook“, `datum_investice` `null`, `datum_oznameni` `2026-10-12`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`
  - zprava_o_transakci, Kyiv Post, zdroj_datum `2026-10-13`, puvod `Defender Media (sdělení Petra Šímy, 12. 10. 2026)`: [kyivpost.com/post/86941](https://kyivpost.com/post/86941)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Zvook: Kyiv Post (puvod `Defender Media (sdělení Petra Šímy, 12. 10. 2026)`) [kyivpost.com/post/86941](https://kyivpost.com/post/86941)
- Tapaya: Vestbee (puvod `null`) [vestbee.com/blog/articles/tapaya-secures-1-m](https://vestbee.com/blog/articles/tapaya-secures-1-m)

**`sektory`**: Sektory odpovídají zdroji
- defence, space, fintech, industry 4.0, energy; zdroj [depoventures.com/](https://depoventures.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `250000`, `max` `500000`, `mena` `EUR`; zdroj [depoventures.com/](https://depoventures.com/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web se popisuje 'from community builders to professional VC fund GPs', 'Backing early-stage founders since 2016'; Kyiv Post ho označuje 'Czech venture capital firm DEPO Ventures'; doložené investice do startupů (pre-seed). Pod značkou běží i síť DEPO Angels a andělské fondy; v ARES existují fondy DEPO VENTURES AF II., osoba rizikového kapitálu, s.r.o. (IČO 11726377) a DEPO VENTURES AF III., osoba rizikového kapitálu, s.r.o. (IČO 17765838), vedené jako podřízené fondy, ne samostatní investoři (jejich výpisy VR nestaženy). Identita: ARES DEPO VENTURES, s.r.o., IČO 04753101 (dříve Hagberg s.r.o.), sídlo Plynární 1617/10, Praha 7, shodné s adresou na webu ('Plynární 10 street', 'Prague 7'); jednatel Petr Šíma, kterého Kyiv Post uvádí jako 'co-founder and managing partner'. Předmět podnikání v rejstříku je obecný (pronájem nemovitostí; výroba, obchod a služby). Podle vyhledávání (businessinfo.cz, nečteno přímo) spravuje nový Fond Ukrajina subjekt DEPO Ventures One SCSp / DEPO Ventures Sàrl (Lucembursko), nepotvrzeno; sídlo investiční firmy (značky) beru jako ČR podle webu a rejstříku. Ticket deklaruje web: 'Ticket €250K - 500K'. Sektory: 'Industry Defence, Space,FinTech, Industry 4.0, Energy'; fáze: 'Stage Inception & Pre-seed'. Kapitál: nenalezen údaj aum/committed/fund size od investora ani regulátora; web uvádí '€9M' nasazeného kapitálu (capital deployed, není kapitál fondu); NRI do Fondu Ukrajina vstupuje kapitálovou investicí 94 mil. Kč (závazek jednoho LP, ne velikost fondu); andělský fond II 'v plánované výši 45 milionů korun' (plán), proto kapital prázdný. Poslední investice: Zvook (ukrajinský defence startup), Kyiv Post 13. 10. 2026: 'DEPO Ventures invested an undisclosed amount in Zvook' přes nový Ukraine Fund; Petr Šíma obchod oznámil Defender Media 12. 10. 2026 (datum_oznameni). Kolo ani nástroj neuvedeny, nástroj nezjisteno. Další: Tapaya, pre-seed 1 mil. EUR (velikost celého kola, ne vklad DEPO); Vestbee 29. 4. 2026: 'raised €1 million in a pre-seed round led by Passion Capital and co-led by Depo Ventures'; web DEPO uvádí DEPO jako lead a Passion Capital jako co-lead (rozpor jen v roli lead/co-lead, účast DEPO, firma i období se shodují, proto investici používám). Nástroj neprima_indicie (pre-seed), podíl výslovně neuveden; žádná investice nemá dolozeno, proto jistota investice stredni. Web DEPO dále uvádí bez data Plexo (DEPO 'cornerstone investor in the company's pre-seed funding round') a WanderWallet (pre-seed 430 tis. EUR); bez data a nezávislé zprávy nezapsány. funding.tech.eu uvádí 21 kol 2022–2026 (vodítko, ne doklad). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="33-cz-inven-capital"></a>
### 33. Inven Capital (`cz-inven-capital`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `CVC` · země `CZ` · status `aktivni` · web [invencapital.cz/](https://www.invencapital.cz/)

Nálezy AI: [nalezy_ai.md#cz-inven-capital](nalezy_ai.md#cz-inven-capital) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Inven Capital, SICAV, a.s.“, IČO `02059533`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-09-25`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/02059533](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/02059533)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [invencapital.cz/](https://www.invencapital.cz/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Wint**, `datum_pro_filtr` `oznameni` → `2026-09-09`; zprávy o transakci: [wint.ai/?p=12204](https://wint.ai/?p=12204), [calcalistech.com/ctechnews/article/g1q2qcekz](https://www.calcalistech.com/ctechnews/article/g1q2qcekz)
- další: **Andercore**, `datum_pro_filtr` `oznameni` → `2026-02-11`; zprávy o transakci: [andercore.com/press/andercore-secures-40m-series-b-for-ai-driven-industrial-t…](https://www.andercore.com/press/andercore-secures-40m-series-b-for-ai-driven-industrial-trade-platform), [tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platf…](https://tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platform-following-a-40m-series-b-raise/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Wint: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series D`, [wint.ai/?p=12204](https://wint.ai/?p=12204)
  - Andercore: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series B`, [tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platf…](https://tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platform-following-a-40m-series-b-raise/)

**`typ`**: Typ je zařazen správně
- `typ`: `CVC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `CVC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Inven Capital, SICAV, a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Wint“, `datum_investice` `null`, `datum_oznameni` `2026-09-09`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series D`
  - zprava_o_transakci, Wint (tisková zpráva), zdroj_datum `2026-09-09`, puvod `null`: [wint.ai/?p=12204](https://wint.ai/?p=12204)
  - zprava_o_transakci, Calcalist (CTech), zdroj_datum `2026-09-09`, puvod `https://wint.ai/?p=12204`: [calcalistech.com/ctechnews/article/g1q2qcekz](https://www.calcalistech.com/ctechnews/article/g1q2qcekz)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Wint: Wint (tisková zpráva) (puvod `null`) [wint.ai/?p=12204](https://wint.ai/?p=12204); Calcalist (CTech) (puvod `https://wint.ai/?p=12204`) [calcalistech.com/ctechnews/article/g1q2qcekz](https://www.calcalistech.com/ctechnews/article/g1q2qcekz)
- Andercore: Andercore (tisková zpráva) (puvod `null`) [andercore.com/press/andercore-secures-40m-series-b-for-ai-driven-industrial-t…](https://www.andercore.com/press/andercore-secures-40m-series-b-for-ai-driven-industrial-trade-platform); Tech.eu (puvod `https://www.andercore.com/press/andercore-secures-40m-series-b-for-ai-driven-industrial-trade-platform`) [tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platf…](https://tech.eu/2026/02/11/andercore-is-expanding-its-ai-based-industrial-trade-platform-following-a-40m-series-b-raise/)

**`sektory`**: Sektory odpovídají zdroji
- climate tech; zdroj [invencapital.cz/](https://www.invencapital.cz/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `2000000`, `max` `30000000`, `mena` `EUR`; zdroj [invencapital.cz/](https://www.invencapital.cz/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `500000000`, `mena` `EUR`, `druh` `aum`, `plati_k` `2023-02-08`, `fond` `null`; zdroj [cez.cz/en/media/press-releases/expanding-strategic-partnership-eib-provides-f…](https://cez.cz/en/media/press-releases/expanding-strategic-partnership-eib-provides-further-eur-50-million-to-the-czech-fund-inven-capital-to-support-investments-into-climate-friendly-start-ups-172371), zdroj_datum `2023-02-08`

<details><summary>Poznámka agenta (celá)</summary>

Typ CVC: Inven Capital je podle tiskové zprávy ČEZ (8. 2. 2023) „CEZ Group´s venture capital fund“ a ČEZ je „the owner of Inven Capital“; jde o samostatný investiční subjekt (samosprávný investiční fond SICAV) velké firmy, tedy samostatná investiční jednotka. Web se sám popisuje „As a venture capital fund we invest EUR 500m from institutional investors…“; VC i CVC jsou v pilotu, výsledek na volbě nezávisí. Identita: ARES Inven Capital, SICAV, a.s., IČO 02059533, sídlo Pod křížkem 1773/2, Praha 4 – Braník (shodně s patičkou webu), předmět „činnost samosprávného investičního fondu“, dříve ČEZ Nová energetika, a.s.; předseda představenstva Petr Míkovec, místopředseda Ivo Němejc, člen Viktor Miškovský. Pod fondem jsou v ARES podfondy Inven Capital – Podfond A až D (IČO 75160692, 75160706, 75162903, 75163861), vedeny jako podřízené fondy, ne samostatní investoři. Ticket podle webu „Ticket size 2-30m EUR“. Kapitál: tisková zpráva ČEZ 8. 2. 2023 „The total assets value under management of Inven capital has now reached over EUR 500 million“ (zapsáno jako aum 500 mil. EUR, údaj je dolní mez „over“); táž zpráva uvádí „more than EUR 260 million at their disposal“ (k dispozici, není kapitál, nezapsáno). Web uvádí „bringing the total committed capital to €500 million“ v nedatované zprávě o EIB „for their new fund“; není jasné, ke kterému fondu a datu, proto nezapsáno. Nesčítám. Fáze investor sám neuvádí (null). Poslední investice: Wint (water intelligence, New York/Izrael), series D 36 mil. USD (velikost celého kola, ne vklad Inven), „co-led by LIP Ventures and Inven Capital“ (tisková zpráva Wint 9. 9. 2026, převzal Calcalist 9. 9. 2026), citace Michal Mravec, Investment Director Inven Capital. Další: Andercore (Berlín) series B 40 mil. USD „in equity and debt“ (velikost celého kola), „with Inven Capital joining this round“ / „joining as a new investor“, dluh je přisouzen „institutional financing from Commerzbank and KfW“; nástroj Inven výslovně neuveden, proto neprima_indicie (series B). Nástroj u obou investic jen neprima_indicie, podíl výslovně neuveden. Jistota investice stredni: Calcalist i Tech.eu vycházejí z tiskových zpráv firem, nezávislost nedoložena. Funding.tech.eu (jen vodítko) uvádí 23 kol, poslední 2026. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="34-cz-credo-ventures"></a>
### 34. Credo Ventures (`cz-credo-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [credoventures.com/](https://credoventures.com/)

Nálezy AI: [nalezy_ai.md#cz-credo-ventures](nalezy_ai.md#cz-credo-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Credo Ventures a.s.“, IČO `28538137`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2023-07-14`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/28538137](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/28538137)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [credoventures.com/](https://credoventures.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **SuperPlane**, `datum_pro_filtr` `oznameni` → `2026-06-24`; zprávy o transakci: [therecursive.com/serbian-superplane-pre-seed-dev-tool/](https://therecursive.com/serbian-superplane-pre-seed-dev-tool/), [thesaasnews.com/news/superplane-raises-2-28m-pre-seed](https://thesaasnews.com/news/superplane-raises-2-28m-pre-seed)
- další: **Supernova**, `datum_pro_filtr` `oznameni` → `2025-09-30`; zprávy o transakci: [tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-v…](https://tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-vibe-coding-to-enterprise-product-teams/); podpůrné: portfolio_web [credoventures.com/newsroom](https://credoventures.com/newsroom)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - SuperPlane: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [therecursive.com/serbian-superplane-pre-seed-dev-tool/](https://therecursive.com/serbian-superplane-pre-seed-dev-tool/)
  - Supernova: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-v…](https://tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-vibe-coding-to-enterprise-product-teams/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Credo Ventures a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „SuperPlane“, `datum_investice` `null`, `datum_oznameni` `2026-06-24`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`
  - zprava_o_transakci, The Recursive, zdroj_datum `2026-06-24`, puvod `null`: [therecursive.com/serbian-superplane-pre-seed-dev-tool/](https://therecursive.com/serbian-superplane-pre-seed-dev-tool/)
  - zprava_o_transakci, The SaaS News, zdroj_datum `2026-06-24`, puvod `https://therecursive.com/serbian-superplane-pre-seed-dev-tool/`: [thesaasnews.com/news/superplane-raises-2-28m-pre-seed](https://thesaasnews.com/news/superplane-raises-2-28m-pre-seed)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- SuperPlane: The Recursive (puvod `null`) [therecursive.com/serbian-superplane-pre-seed-dev-tool/](https://therecursive.com/serbian-superplane-pre-seed-dev-tool/); The SaaS News (puvod `https://therecursive.com/serbian-superplane-pre-seed-dev-tool/`) [thesaasnews.com/news/superplane-raises-2-28m-pre-seed](https://thesaasnews.com/news/superplane-raises-2-28m-pre-seed)
- Supernova: Tech.eu (puvod `null`) [tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-v…](https://tech.eu/2025/09/30/supernova-raises-92-million-series-a-to-bring-ai-powered-vibe-coding-to-enterprise-product-teams/)

**`sektory`**: Sektory odpovídají zdroji
- nevyplněno (`null`)

**`ticket`**: Ticket odpovídá zdroji
- `min` `1000000`, `max` `5000000`, `mena` `USD`; zdroj [credoventures.com/](https://credoventures.com/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `88000000`, `mena` `USD`, `druh` `fund_size`, `plati_k` `2026-03-23`, `fond` `Credo Stage 5`; zdroj [thenextweb.com/news/credo-ventures-88m-fund](https://thenextweb.com/news/credo-ventures-88m-fund), zdroj_datum `2026-03-23`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web se popisuje jako 'The fund of choice for CEE founders around the world building generational companies' a 'Leading Pre-Seed rounds', doložené investice za podíl do startupů. Identita: ARES Credo Ventures a.s., IČO 28538137, sídlo Karlovo náměstí 2097/10, Praha 2 (shodné s adresou Karlovo Náměstí 10 na webu), předseda správní rady Ondřej Bartoš. V ARES existuje i Credo Ventures Management II a.s. (IČO 24396893, vznik 2026-01-20, stejná adresa, předseda Maximilian Kolowrat-Krakowský, člen Jakub Křikava, kterého The Next Web cituje jako partnera Credo); pravděpodobně správcovská entita pro nový fond, role nepotvrzená. Web uvádí kanceláře v Praze a Krakově; sídlo investiční firmy beru jako ČR podle rejstříku. Ticket '$1M - $5M checks' deklaruje web. Kapitál: The Next Web 23. 3. 2026: 'Credo Ventures has closed Credo Stage 5, an $88 million fund raised in a single closing'; plati_k = datum zprávy, přesné datum uzavření neuvedeno. Starší fondy (např. fond IV 75 mil. EUR podle CzechCrunch) nezapisuji a nesčítám. Sektory: web výslovně 'Backing exceptional people, not thesis-driven', proto null. Poslední investice: SuperPlane, pre-seed 2,28 mil. EUR / 2,6 mil. USD (velikost celého kola, ne vklad Credo), Credo jako lead podle The Recursive 24. 6. 2026; The SaaS News z Recursive přímo vychází (stejný původ), proto jistota investice stredni; nezávislý druhý zdroj nedoložen. Nástroj neprima_indicie (pre-seed), podíl výslovně neuveden. Další: Supernova series A 9,2 mil. USD (velikost kola), Credo mezi účastníky podle Tech.eu 30. 9. 2025. Agregátory uvádějí i Modeinspect (seed, leden 2026) a Picogrid (series A, květen 2026), ale bez zprávy o transakci, kterou bych přečetl s Credo jmenovaným, proto nezapsány. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="35-cz-cs-seed-starter"></a>
### 35. ČS Seed Starter (`cz-cs-seed-starter`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `CVC` · země `CZ` · status `aktivni` · web [seedstarter.cz/](https://www.seedstarter.cz/)

Nálezy AI: [nalezy_ai.md#cz-cs-seed-starter](nalezy_ai.md#cz-cs-seed-starter) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „ČS Seed Starter, a.s.“, IČO `61058769`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-10-22`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/61058769](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/61058769)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [seedstarter.cz/](https://www.seedstarter.cz/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Definic**, `datum_pro_filtr` `oznameni` → `2026-06-12`; zprávy o transakci: [cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni…](https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/)
- další: **Repsense**, `datum_pro_filtr` `oznameni` → `2025-12-17`; zprávy o transakci: [cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ve…](https://cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ventures-a-ceska-sporitelna/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Definic: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni…](https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/)
  - Repsense: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje

**`typ`**: Typ je zařazen správně
- `typ`: `CVC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `CVC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „ČS Seed Starter, a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Definic“, `datum_investice` `null`, `datum_oznameni` `2026-06-12`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2026-06-12`, puvod `null`: [cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni…](https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Definic: CzechCrunch (puvod `null`) [cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni…](https://cc.cz/nakup-it-sluzeb-v-korporacich-je-casto-nefunkcni-hlasi-do-jejich-reseni-investuje-i-ceska-sporitelna/)
- Repsense: CzechCrunch (puvod `null`) [cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ve…](https://cc.cz/jejich-nastroj-havel-pomaha-i-v-nato-do-litevcu-ted-investuji-tensor-ventures-a-ceska-sporitelna/)

**`sektory`**: Sektory odpovídají zdroji
- nevyplněno (`null`)

**`ticket`**: Ticket odpovídá zdroji
- `min` `200000`, `max` `1000000`, `mena` `EUR`; zdroj [seedstarter.cz/](https://www.seedstarter.cz/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ CVC: web se sám označuje jako „Corporate Venture Capital of Česká spořitelna“ (https://www.seedstarter.cz/) a investiční činnost vykonává samostatná společnost ČS Seed Starter, a.s., jejímž jediným akcionářem je Česká spořitelna, a.s. (IČO 45244782), s předmětem činnosti „Investice do startupů a jiných právnických osob. Správa vlastního investičního portfolia.“ (ARES). Identita: IČO 61058769, sídlo Olbrachtova 1929/62, Praha 4; web uvádí stejné IČ; člen představenstva Tomáš Milota (ARES, členství od 2023-10-01) je na webu uveden jako CEO a v článku CzechCrunch o Definicu mluví „za Seed Starter ČS“. Odlišit od Seed Starteru Slovenské sporiteľne (samostatný slovenský program, na funding.tech.eu veden zvlášť). Ticket 200k–1M EUR a nástroj „CLA or equity investment“, menšinový podíl podle webu. Sektory web neuvádí (jen technologie pro bankovnictví a klienty), proto null. Kapitál: veřejně jen částky alokované nebo už proinvestované (např. „Banka jim zatím poslala 180 milionů“, CzechCrunch 2023), což není AUM/committed capital/fund size, proto prázdné. Velikost kol (ne vklad ČS): Definic seed 2,5 mil. EUR (vedl J&T Ventures, dále Slovak Investment Holding); Repsense 1,1 mil. EUR podle CzechCrunch (funding.tech.eu uvádí 2 mil. EUR, rozdíl jen ve velikosti kola, ne ve firmě, datu ani investorovi). Nástroj: Definic jen neprima_indicie (seed kolo, účast Seed Starteru výslovně uvedena), Repsense nezjištěn. Jistota investice střední: jediná zpráva o transakci (CzechCrunch), nezávislý druhý zdroj nedohledán, žádný dolozeno. Datum Definic = datum oznámení (CzechCrunch, 2026-06-12), datum uzavření kola zdroj neuvádí. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="36-cz-jt-ventures"></a>
### 36. J&T Ventures (`cz-jt-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [jtventures.cz/](https://www.jtventures.cz/)

Nálezy AI: [nalezy_ai.md#cz-jt-ventures](nalezy_ai.md#cz-jt-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „J&T Ventures CG SICAV a.s.“, IČO `08220867`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-05-16`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08220867](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08220867)
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-07-31`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22175903](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22175903)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [jtventures.cz/tym](https://www.jtventures.cz/tym)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **Wultra**, `datum_pro_filtr` `oznameni` → `2026-06-29`; zprávy o transakci: [lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-…](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/), [prnewswire.com/nl/persberichten/wultra-haalt--6-8-miljoen-op-in-een-series-a-…](https://www.prnewswire.com/nl/persberichten/wultra-haalt--6-8-miljoen-op-in-een-series-a-financieringsronde-om-de-wereldwijde-uitbreiding-van-post-kwantumoplossingen-voor-digitale-identiteit-te-versnellen-302814757.html)
- další: **Choice**, `datum_pro_filtr` `oznameni` → `2026-03-16`; zprávy o transakci: [tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-opera…](https://tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-operating-system-across-europe/)
- další: **ValkaAI**, `datum_pro_filtr` `oznameni` → `2026-02-24`; zprávy o transakci: [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Wultra: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-…](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
  - Choice: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-opera…](https://tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-operating-system-across-europe/)
  - ValkaAI: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „J&T Ventures CG SICAV a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Wultra“, `datum_investice` `null`, `datum_oznameni` `2026-06-29`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2026-06-29`, puvod `Wultra (informace firmy)`: [lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-…](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/)
  - zprava_o_transakci, PR Newswire (tisková zpráva Wultra), zdroj_datum `2026-07-01`, puvod `Wultra (informace firmy)`: [prnewswire.com/nl/persberichten/wultra-haalt--6-8-miljoen-op-in-een-series-a-…](https://www.prnewswire.com/nl/persberichten/wultra-haalt--6-8-miljoen-op-in-een-series-a-financieringsronde-om-de-wereldwijde-uitbreiding-van-post-kwantumoplossingen-voor-digitale-identiteit-te-versnellen-302814757.html)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Wultra: Lupa.cz (puvod `Wultra (informace firmy)`) [lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-…](https://www.lupa.cz/aktuality/ceska-firma-wultra-vybrala-dalsich-160-milionu-na-nasazeni-postkvantoveho-sifrovani/); PR Newswire (tisková zpráva Wultra) (puvod `Wultra (informace firmy)`) [prnewswire.com/nl/persberichten/wultra-haalt--6-8-miljoen-op-in-een-series-a-…](https://www.prnewswire.com/nl/persberichten/wultra-haalt--6-8-miljoen-op-in-een-series-a-financieringsronde-om-de-wereldwijde-uitbreiding-van-post-kwantumoplossingen-voor-digitale-identiteit-te-versnellen-302814757.html)
- Choice: Tech.eu (puvod `null`) [tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-opera…](https://tech.eu/2026/03/16/choice-secures-71m-series-a-to-expand-its-restaurant-operating-system-across-europe/)
- ValkaAI: CzechCrunch (puvod `null`) [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/)

**`sektory`**: Sektory odpovídají zdroji
- B2B, B2C, Marketplaces, sector agnostic; zdroj [jtventures.cz/](https://www.jtventures.cz/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `300000`, `max` `3000000`, `mena` `EUR`; zdroj [jtventures.cz/](https://www.jtventures.cz/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `120000000`, `mena` `EUR`, `druh` `aum`, `plati_k` `null`, `fond` `null`; zdroj [jtventures.cz/](https://www.jtventures.cz/), zdroj_datum `null`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: samostatná značka a tým (Managing Partner Adam Kočík, partneři David Polach, Zuzana Ondrejová, Martin Kešner) s vlastními fondy kvalifikovaných investorů; web 'Podporujeme CEE & SEE foundery s globální ambicí', 'Pre-seed až Series A', CzechCrunch ji řadí mezi 'tuzemské fondy'. Vazba na skupinu J&T (název, kancelář v budově J&T Banky) by mohla ukazovat i na CVC; obě varianty jsou v rozsahu pilotu, výsledek na tom nezávisí. Identita: značka sama nemá v ARES vlastní správcovskou firmu; fondy J&T Ventures CG SICAV a.s. (IČO 08220867, od 2019, sídlo Sokolovská 700/113a, Praha 8) a J&T Ventures III SICAV a.s. (IČO 22175903, vznik 2024-10-21, tatáž adresa), statutárním orgánem obou je AMISTA investiční společnost, a.s. (IČO 27437558, administrátor/obhospodařovatel, ne investiční tým). V dozorčí radě CG SICAV jsou Adam Kočík a Martin Kešner, tedy lidé z týmu na webu, takže fondy k značce přiřazuji. V ARES jsou dále J&T VENTURES I otevřený podílový fond (IČO 71508121) a podfond J&T Ventures II (IČO 75161435). Jako pravni_subjekt uvádím CG SICAV (hlavní fond s týmem v orgánech); formálního správce značky (investiční firmu) jsem v rejstříku nenašel. Sídlo investiční firmy ČR (adresa na webu i v rejstříku). Ticket '€300K – €3M' (Velikost investice) deklaruje web. Kapitál: web uvádí '€120M Výše aktiv' bez data a bez rozlišení fondů; zapsáno jako aum, plati_k neznámé (web © 2024), k ruční kontrole. Sektory web: 'B2B, B2C, Marketplaces, Sector Agnostic'. Poslední investice: Wultra, series A 6,8 mil. EUR (velikost celého kola, ne vklad J&T Ventures), vedl Seventure Partners, J&T Ventures jako stávající investor ('stávající investoři J&T Ventures a Elevator Ventures', Lupa 29. 6. 2026, 'informovala firma'; tisková zpráva Wultra na PR Newswire 1. 7. 2026). Oba zdroje vycházejí z informací firmy, proto jeden původ a jistota investice stredni. Datum uzavření neuvedeno, proto datum_oznameni. Další: Choice series A 7,1 mil. USD (velikost kola, Tech.eu 16. 3. 2026, 'participation from Reflex Capital, Smartlink, and J&T Ventures'), ValkaAI pre-seed 12 mil. EUR (velikost kola, CzechCrunch 24. 2. 2026, 'od tuzemských fondů J&T Ventures, Tensor Ventures, BD Partners'). Účast Fondu Naše Česko v kole ValkaAI je samostatný investor (jiný správce), J&T Ventures nepřipisována. Nástroj u všech neprima_indicie (series A / pre-seed), podíl výslovně neuveden. Agregátory (Seedtable, Caplight, funding.tech.eu) uvádějí v červnu 2026 i Definic (seed, 12. 6. 2026) a Grid.online; zprávu o transakci jsem nenašel, proto nezapsány; obě by byly starší než Wultra. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="37-cz-rockaway-ventures"></a>
### 37. Rockaway Ventures (`cz-rockaway-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [rockawayventures.com/](https://rockawayventures.com/)

Nálezy AI: [nalezy_ai.md#cz-rockaway-ventures](nalezy_ai.md#cz-rockaway-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Rockaway Ventures Advisors a.s.“, IČO `14125129`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-08-29`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14125129](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/14125129)
  - media, Vestbee, zdroj_datum `2025-05-16`, puvod `null`: [vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund](https://www.vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **ValkaAI**, `datum_pro_filtr` `oznameni` → `2026-02-24`; zprávy o transakci: [rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures), [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/), [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599)
- další: **Apptronik**, `datum_pro_filtr` `oznameni` → `2026-02-13`; zprávy o transakci: [lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humano…](https://www.lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humanoidu-a-to-po-boku-googlu-nebo-mercedes-benz/)
- další: **Remix**, `datum_pro_filtr` `oznameni` → `2025-12-19`; zprávy o transakci: [lupa.cz/aktuality/rockaway-investuje-do-evropskeho-digitalniho-second-hand-gi…](https://www.lupa.cz/aktuality/rockaway-investuje-do-evropskeho-digitalniho-second-hand-giganta-tahne-ho-umela-inteligence/), [vestbee.com/insights/articles/rockaway-ventures-backs-remix](https://vestbee.com/insights/articles/rockaway-ventures-backs-remix)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - ValkaAI: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
  - Apptronik: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humano…](https://www.lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humanoidu-a-to-po-boku-googlu-nebo-mercedes-benz/)
  - Remix: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `series A`, [lupa.cz/aktuality/rockaway-investuje-do-evropskeho-digitalniho-second-hand-gi…](https://www.lupa.cz/aktuality/rockaway-investuje-do-evropskeho-digitalniho-second-hand-giganta-tahne-ho-umela-inteligence/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Rockaway Ventures Advisors a.s.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „ValkaAI“, `datum_investice` `null`, `datum_oznameni` `2026-02-24`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`
  - zprava_o_transakci, Rockaway Capital (tisková zpráva), zdroj_datum `2026-02-24`, puvod `null`: [rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures)
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2026-02-24`, puvod `oznámení investice 24. 2. 2026 (pravděpodobně TZ Rockaway/ValkaAI, nedoloženo)`: [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/)
  - zprava_o_transakci, Seznam Zprávy, zdroj_datum `2026-02-24`, puvod `oznámení investice 24. 2. 2026 (pravděpodobně TZ Rockaway/ValkaAI, nedoloženo)`: [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- ValkaAI: Rockaway Capital (tisková zpráva) (puvod `null`) [rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures](https://www.rockawaycapital.com/en/news/e12m-investment-in-valkaai-led-by-rockaway-ventures); CzechCrunch (puvod `oznámení investice 24. 2. 2026 (pravděpodobně TZ Rockaway/ValkaAI, nedoloženo)`) [cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziska…](https://cc.cz/tvori-avatary-kteri-zvladnou-zive-komentovat-sportovni-zapasy-ted-ziskal-rekordni-investici/); Seznam Zprávy (puvod `oznámení investice 24. 2. 2026 (pravděpodobně TZ Rockaway/ValkaAI, nedoloženo)`) [seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-star…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-byznys-startupy-technologie-cesky-startup-ziskal-stovky-milionu-slibuje-prepsat-budoucnost-zabavy-299599)
- Apptronik: Lupa.cz (puvod `oznámení Apptronik o rozšíření kola Series A`) [lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humano…](https://www.lupa.cz/aktuality/cesti-investori-z-rockaway-investovali-do-americkych-humanoidu-a-to-po-boku-googlu-nebo-mercedes-benz/)
- Remix: Lupa.cz (puvod `oznámení Rockaway Ventures 19. 12. 2025`) [lupa.cz/aktuality/rockaway-investuje-do-evropskeho-digitalniho-second-hand-gi…](https://www.lupa.cz/aktuality/rockaway-investuje-do-evropskeho-digitalniho-second-hand-giganta-tahne-ho-umela-inteligence/); Vestbee (puvod `oznámení Rockaway Ventures 19. 12. 2025`) [vestbee.com/insights/articles/rockaway-ventures-backs-remix](https://vestbee.com/insights/articles/rockaway-ventures-backs-remix)

**`sektory`**: Sektory odpovídají zdroji
- retail a e-commerce, travel a hospitality, digitální logistika, digitální média, kybernetická bezpečnost, obrana, cleantech, proptech; zdroj [rockawayventures.com/](https://rockawayventures.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- kapital[0]: `castka` `55000000`, `mena` `EUR`, `druh` `fund_size`, `plati_k` `2025-05-16`, `fond` `Rockaway Ventures Fund II`; zdroj [vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund](https://www.vestbee.com/insights/articles/rockaway-ventures-closes-55-m-fund), zdroj_datum `2025-05-16`

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web se popisuje jako fond ('proud to be a part of the Rockaway Capital group', patička 'Rockaway Ventures Fund'), Vestbee 16. 5. 2025 'Prague-based European investment fund' investující do late-seed a Series A startupů; doložené menšinové investice do startupů. Rockaway Capital je investiční skupina J. Havrlanta, ne provozní korporace, proto ne CVC; podle TZ z 24. 2. 2026 je Rockaway Ventures 'progressive part of the newly established Rockaway Fund within Rockaway Capital'. Identita: ARES Rockaway Ventures Advisors a.s., IČO 14125129, Generála Píky 430/26, Praha 6; představenstvo Jakub Havrlant (předseda), Dušan Zábrodský, Andrea Lauren; Zábrodského uvádí Vestbee jako General Partnera Rockaway Ventures, Havrlanta jako zakladatele. Role této a.s. jako správce/poradce fondu z rejstříku výslovně nevyplývá (předmět činnosti 'Pronájem nemovitostí...'), vazba je přes osoby. Na stejné adrese jsou i Rockaway Ventures a.s. (IČO 06387136, představenstvo Havrlant, Viktor Fischer), Rockaway Ventures Fund Holding a.s. (IČO 14053942) a fond Rockaway Ventures Fund SICAV a.s. (IČO 14235781, statutár AMISTA investiční společnost, a.s.; fond je podřízený údaj). Ticket web ani média neuvádějí, proto null. Kapitál: Vestbee 'has closed its second fund at nearly €55 million' (Rockaway Ventures Fund II), zapsáno 55 mil. EUR jako fund_size s výhradou 'nearly'; plati_k = datum zprávy. Poslední investice: ValkaAI, pre-seed 12 mil. EUR (velikost celého kola, ne vklad Rockaway), Rockaway Ventures kolo vedla podle TZ Rockaway Capital i CzechCrunch a Seznam Zpráv ze stejného dne; nezávislost médií na TZ nedoložena, proto jeden původ. Nástroj neprima_indicie (pre-seed). Další: Apptronik, rozšíření Series A o 520 mil. USD (velikost kola), Lupa 13. 2. 2026 'Čeští investoři z Rockaway Ventures finančně vstoupili do americké společnosti Apptronik'; Remix, Lupa 19. 12. 2025 'Rockaway Ventures získává 20% podíl v Remixu' (podíl doložen; Series A podle Vestbee), Lupa a Vestbee vycházejí ze stejného oznámení. Agregátory (Caplight, PitchBook) uvádějí i CulturePulse (seed, červen 2026), Navigara, Float a AdSpawn, ale zprávu o transakci jsem nenašel, proto nezapsány. Jistota investice stredni: žádná investice nemá doloženě dva nezávislé původy. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="38-cz-borovicka-capital"></a>
### 38. Borovicka Capital (`cz-borovicka-capital`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `investice_dolozena_12_24_mesicu` · web [borovickacapital.com/](https://borovickacapital.com/)

Nálezy AI: [nalezy_ai.md#cz-borovicka-capital](nalezy_ai.md#cz-borovicka-capital) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Borovicka Capital s.r.o., Breitfeldova 709/17, Karlín, 186 00 Praha 8“, IČO `19966784`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-08-01`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19966784](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19966784)
  - media, Forbes Česko, zdroj_datum `2024-11-28`, puvod `null`: [forbes.cz/startupy-jsou-budoucnost-na-starem-stavet-nelze-rika-otec-ktery-pod…](https://forbes.cz/startupy-jsou-budoucnost-na-starem-stavet-nelze-rika-otec-ktery-podnika-se-syny/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `investice_dolozena_12_24_mesicu`
- poslední: **NutritionPro (Nutritionpro s.r.o., IČO 07752971)**, `datum_pro_filtr` `oznameni` → `2025-10-23`; zprávy o transakci: [forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak…](https://forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak-pohlreicha/); podpůrné: rejstrik_spolecnik [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07752971](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07752971)
- další: **Edmund (Edmund AI)**, `datum_pro_filtr` `oznameni` → `2025-02-12`; zprávy o transakci: [vestbee.com/blog/articles/edmund-secures-500-k](https://www.vestbee.com/blog/articles/edmund-secures-500-k)
- další: **Outfindo**, `datum_pro_filtr` `oznameni` → `2025-01-20`; zprávy o transakci: [cc.cz/poklada-jednoduche-otazky-a-tim-ulehcuje-slozite-nakupy-startup-outfind…](https://cc.cz/poklada-jednoduche-otazky-a-tim-ulehcuje-slozite-nakupy-startup-outfindo-ted-nabira-dalsi-miliony/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - NutritionPro (Nutritionpro s.r.o., IČO 07752971): `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`, [forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak…](https://forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak-pohlreicha/)
  - Edmund (Edmund AI): `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [vestbee.com/blog/articles/edmund-secures-500-k](https://www.vestbee.com/blog/articles/edmund-secures-500-k)
  - Outfindo: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `late-seed`, [cc.cz/poklada-jednoduche-otazky-a-tim-ulehcuje-slozite-nakupy-startup-outfind…](https://cc.cz/poklada-jednoduche-otazky-a-tim-ulehcuje-slozite-nakupy-startup-outfindo-ted-nabira-dalsi-miliony/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Borovicka Capital s.r.o., Breitfeldova 709/17, Karlín, 186 00 Praha 8“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „NutritionPro (Nutritionpro s.r.o., IČO 07752971)“, `datum_investice` `null`, `datum_oznameni` `2025-10-23`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`
  - zprava_o_transakci, Forbes Česko, zdroj_datum `2025-10-23`, puvod `null`: [forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak…](https://forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak-pohlreicha/)
  - rejstrik_spolecnik, ARES (výpis z veřejného rejstříku), zdroj_datum `2025-08-29`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07752971](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07752971)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- NutritionPro (Nutritionpro s.r.o., IČO 07752971): Forbes Česko (puvod `null`) [forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak…](https://forbes.cz/nutritionpro-zmenil-majitele-do-zisku-ho-pretaci-i-byznysovy-partak-pohlreicha/)
- Edmund (Edmund AI): Vestbee (puvod `null`) [vestbee.com/blog/articles/edmund-secures-500-k](https://www.vestbee.com/blog/articles/edmund-secures-500-k)
- Outfindo: CzechCrunch (puvod `null`) [cc.cz/poklada-jednoduche-otazky-a-tim-ulehcuje-slozite-nakupy-startup-outfind…](https://cc.cz/poklada-jednoduche-otazky-a-tim-ulehcuje-slozite-nakupy-startup-outfindo-ted-nabira-dalsi-miliony/)

**`sektory`**: Sektory odpovídají zdroji
- nevyplněno (`null`)

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web se popisuje „Borovicka Capital is an investment company with a strategic focus on venture capital investments“, investuje přímo do startupů v rané fázi ve střední Evropě, většinou jako koinvestor s menšinovými podíly (Forbes 28. 11. 2024: „zatím fungujeme hlavně jako koinvestoři“). Peníze jsou rodinné (otec Martin a synové Jakub a Lukáš Borovičkovi). Média ho nazývají „rodinný fond“ (CzechCrunch) nebo „rodinný VC fond“ (Forbes), jako family office se ale výslovně neoznačuje a samotné peníze jedné rodiny pro typ family office nestačí (PLAN.md bod 2). Identita: ARES vrátil Borovicka Capital s.r.o., IČO 19966784, sídlo Breitfeldova 709/17, Praha 8, jednatelé Martin a Jakub Borovička (Lukáš Borovička jednatelem a společníkem do 31. 7. 2026), společníci Jakub Borovička (51 %) a BC Holding s.r.o. (49 %). Jména odpovídají médiím (Forbes, CzechCrunch), totožnost je potvrzená. Předmět podnikání v rejstříku je obecná volná živnost, žádná licence ČNB jsem nedohledal ani nehledal. Ticket: investor ho sám nedeklaruje. Třetí strany (SuperScout) uvádějí 500 tis.–1,25 mil. EUR, to není deklarace investora, proto nevyplněno. Kapitál: nevyplněn. Forbes uvádí, že v roce 2024 „nainvestovali třicet milionů korun“ a že jsou „celkově připraveni vložit sumu ve výši 150 milionů korun“. To je záměr, ne AUM, upsaný kapitál ani velikost fondu. CzechCrunch uvádí, že otec vkládá peníze „formou půjček“ (financování investiční firmy, ne nástroj vůči startupům). Sektory: zdroj investora je neuvádí, jen „společenský dopad“ (CzechCrunch), proto null. Poslední investice: NutritionPro. Forbes 23. 10. 2025: investoři Borovicka Capital, Leverage a Lighthouse Ventures vykoupili podíly zakladatele Nurlana Abdrassilova („jsme se spojili s Leverage a Lighthouse Ventures a Nurlanův podíl vykoupili“). Nástroj podíl je doložený. Rejstřík Nutritionpro s.r.o. (IČO 07752971) vede Borovicka Capital s.r.o. jako společníka od 19. 6. 2024, nové podíly zapsané 5. 8. a 21. 8. 2025. Abdrassilov je vymazán 21. 8. 2025. To je jen podpůrný doklad, datum investice z rejstříku neberu. Částku zdroj neuvádí. Datum pro filtr je oznámení 2025-10-23, tedy jen 3 dny před hranicí 12 měsíců (2025-10-26), proto status investice_dolozena_12_24_mesicu. Jde o odkup podílu od zakladatele (sekundární transakce), ne o nové kolo. Další investice: Edmund, pre-seed kolo 500 000 EUR (velikost celého kola, ne vklad), vedl Lighthouse Ventures (Vestbee 12. 2. 2025). Outfindo, late-seed kolo 1,2 mil. EUR (velikost celého kola), vedl Eleven Ventures (CzechCrunch 20. 1. 2025). Funding.tech.eu uvádí stejné dva dealy (2025-01-20 a 2025-02-12). Jistota investice střední: k NutritionPro je jen jedna zpráva o transakci a rejstřík je jen podpůrný. Zprávu o novější investici (např. do kola Edmund v roce 2026) jsem nenašel, Borovicka Capital v ní jmenovaná není. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="39-cz-fazole-ventures"></a>
### 39. Fazole Ventures (`cz-fazole-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `investice_dolozena_12_24_mesicu` · web [fazole.vc/](https://www.fazole.vc/)

Nálezy AI: [nalezy_ai.md#cz-fazole-ventures](nalezy_ai.md#cz-fazole-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Fazole Ventures s.r.o.“, IČO `07491492`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2019-02-06`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07491492](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07491492)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [fazole.vc/](https://www.fazole.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `investice_dolozena_12_24_mesicu`
- poslední: **Everbot**, `datum_pro_filtr` `oznameni` → `2025-09-16`; zprávy o transakci: [forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-mi…](https://forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-miliardar-bouska/), [cc.cz/jak-se-vyznat-v-modelech-umele-inteligence-startup-nabizi-reseni-a-nabi…](https://cc.cz/jak-se-vyznat-v-modelech-umele-inteligence-startup-nabizi-reseni-a-nabira-desitky-milionu-korun/), [lupa.cz/aktuality/startup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepse…](https://www.lupa.cz/aktuality/startup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepseek-do-jednoho-rozhrani-ziskal-na-to-investici/); podpůrné: portfolio_web [fazole.vc/](https://www.fazole.vc/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - Everbot: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`, [forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-mi…](https://forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-miliardar-bouska/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Fazole Ventures s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „Everbot“, `datum_investice` `null`, `datum_oznameni` `2025-09-16`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`
  - zprava_o_transakci, Forbes Česko, zdroj_datum `2025-09-16`, puvod `společné oznámení Everbot / Fazole Ventures (tisková zpráva nedohledaná; shodné citace R. Berglowiece a P. Přikryla ve všech článcích)`: [forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-mi…](https://forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-miliardar-bouska/)
  - zprava_o_transakci, CzechCrunch, zdroj_datum `2025-09-16`, puvod `společné oznámení Everbot / Fazole Ventures (tisková zpráva nedohledaná; shodné citace R. Berglowiece a P. Přikryla ve všech článcích)`: [cc.cz/jak-se-vyznat-v-modelech-umele-inteligence-startup-nabizi-reseni-a-nabi…](https://cc.cz/jak-se-vyznat-v-modelech-umele-inteligence-startup-nabizi-reseni-a-nabira-desitky-milionu-korun/)
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2025-09-16`, puvod `společné oznámení Everbot / Fazole Ventures (tisková zpráva nedohledaná; shodné citace R. Berglowiece a P. Přikryla ve všech článcích)`: [lupa.cz/aktuality/startup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepse…](https://www.lupa.cz/aktuality/startup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepseek-do-jednoho-rozhrani-ziskal-na-to-investici/)
  - portfolio_web, web investora, zdroj_datum `null`, puvod `null`: [fazole.vc/](https://www.fazole.vc/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- Everbot: Forbes Česko (puvod `společné oznámení Everbot / Fazole Ventures (tisková zpráva nedohledaná; shodné citace R. Berglowiece a P. Přikryla ve všech článcích)`) [forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-mi…](https://forbes.cz/cesky-ai-start-up-everbot-ziskal-desitky-milionu-do-hry-vstupuje-miliardar-bouska/); CzechCrunch (puvod `společné oznámení Everbot / Fazole Ventures (tisková zpráva nedohledaná; shodné citace R. Berglowiece a P. Přikryla ve všech článcích)`) [cc.cz/jak-se-vyznat-v-modelech-umele-inteligence-startup-nabizi-reseni-a-nabi…](https://cc.cz/jak-se-vyznat-v-modelech-umele-inteligence-startup-nabizi-reseni-a-nabira-desitky-milionu-korun/); Lupa.cz (puvod `společné oznámení Everbot / Fazole Ventures (tisková zpráva nedohledaná; shodné citace R. Berglowiece a P. Přikryla ve všech článcích)`) [lupa.cz/aktuality/startup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepse…](https://www.lupa.cz/aktuality/startup-z-opavy-slucuje-desitky-ai-typu-gpt-llama-ci-deepseek-do-jednoho-rozhrani-ziskal-na-to-investici/)

**`sektory`**: Sektory odpovídají zdroji
- energetika, bankovnictví, doprava, retail, smart city, telco, B2B technologie; zdroj [fazole.vc/](https://www.fazole.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `1000000`, `max` `20000000`, `mena` `CZK`; zdroj [fazole.vc/](https://www.fazole.vc/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: web 'Fazole Ventures jsme založili proto, abychom pomohli chytrým lidem uspět... Podporujeme je v počáteční fázi růstu jejich firem tím, že poskytujeme financování', tým managing partner Pavel Přikryl a zakládající partneři Pavel Bouška a Luboš Černý; Forbes 12. 8. 2019 (https://forbes.cz/novy-startupovy-fond-na-scene-vetsinu-penez-poskytne-miliardar-bouska/) jej uvádí jako nový fond na 'české venture kapitálové scéně' ('Nový vehikl... se zaměřuje na rané investice do technologických startupů z oblasti B2B'; Přikryl: 'rodinnější povahou našeho fondu', 'Naší ambicí je vytvořit jakýsi venture kapitálový klub'). Většinu peněz podle Forbes přislíbil P. Bouška, který své další investice spravuje přes vlastní family office Fermia; Fazole je samostatná investiční firma tří partnerů s menšinovými podíly ve startupech, ne holding jednoho podnikatele ani family office. Identita: ARES Fazole Ventures s.r.o., IČO 07491492, sídlo Salvátorská 931/8, Praha 1 (shodné s adresou 'c/o Opero, Salvátorská 931/8' na webu), jednatelé Luboš Černý a Pavel Přikryl = partneři podle webu; společníci Luboš Černý 15 %, GROWTHGARAGE s.r.o. 25 % (poradenská firma, kterou podle webu vede Přikryl), PABCO s.r.o. 60 % (vazba na P. Bouška nepotvrzená). Předmět podnikání v ARES je jen 'pronájem nemovitostí, bytů a nebytových prostor' (obecný zápis). Ticket: web 'Náš "sweet spot" se pohybuje mezi 1-20 mil. CZK, ale zvážíme i větší objemy financování'. Kapitál: Forbes 2019 'Palebnou sílu přesně stanovenou nemá', proto prázdné. Poslední investice: Everbot (Opava), Forbes 16. 9. 2025: 'Do firmy míří desítky milionů korun od skupiny investorů v čele s fondem Fazole Ventures' a 'Fond Fazole Ventures získá v Everbotu výměnou za kapitál 12,2procentní podíl s možností navýšení až o 2,7 procentního bodu. Přesná výše investice v řádu desítek milionů korun nebyla zveřejněna.' CzechCrunch týž den: 'Lídrem investičního kola se stal fond Fazole Ventures', 'Everbot je nyní v pořadí desátou investicí Fazole Ventures.'; Lupa.cz týž den: 'nabral investici nižších desítek milionů korun výměnou za podíl 12,2 procenta'. Nástroj podíl doložený. Datum podpisu/uzavření žádný zdroj neuvádí, proto datum_oznameni. Všechny tři články vyšly 16. 9. 2025 se shodnými citacemi, tedy z jednoho oznámení -> jeden původ, jistota investice stredni. Status investice_dolozena_12_24_mesicu (oznámení 2025-09-16, tj. před 2025-10-26). Agregátory (Caplight) uvádějí Whalebone series B v únoru 2025 s účastí Fazole, zprávu o transakci s Fazole jsem nenašel (Forbes 2019 popisuje investici 15 mil. Kč do Whalebone v roce 2019), proto nezapsáno; funding.tech.eu uvádí jen Forloop (2022). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="40-cz-miton"></a>
### 40. Miton (`cz-miton`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [miton.cz/](https://www.miton.cz/)

Nálezy AI: [nalezy_ai.md#cz-miton](nalezy_ai.md#cz-miton) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „MITON CZ, s.r.o., Křižíkova 148/34, Karlín, 186 00 Praha 8“, IČO `25417967`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2022-02-05`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/25417967](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/25417967)
  - web_subjektu, Miton, zdroj_datum `null`, puvod `null`: [miton.cz/o-nas/](https://www.miton.cz/o-nas/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **DeepScout**, `datum_pro_filtr` `oznameni` → `2026-10-19`; zprávy o transakci: [lupa.cz/aktuality/miton-veri-v-ai-agenty-v-e-commerce-miliony-posila-do-sluzb…](https://www.lupa.cz/aktuality/miton-veri-v-ai-agenty-v-e-commerce-miliony-posila-do-sluzby-ktera-jim-umoznuje-hlidat-ceny-napric-trhem/)
- další: **ACE (padelová aplikace)**, `datum_pro_filtr` `oznameni` → `2026-10-01`; zprávy o transakci: [cc.cz/prodal-startup-americanum-ted-se-veze-na-vlne-padelu-pulku-jeho-nove-ap…](https://cc.cz/prodal-startup-americanum-ted-se-veze-na-vlne-padelu-pulku-jeho-nove-aplikace-ziskava-za-miliony-miton/), [miton.cz/blog/miton-investuje-do-ace-stravu-pro-padel-uz-pouziva-vice-nez-pol…](https://www.miton.cz/blog/miton-investuje-do-ace-stravu-pro-padel-uz-pouziva-vice-nez-polovina-ceskych-hracu/)
- další: **Whisper (AI agent pro zákaznickou podporu v e-commerce)**, `datum_pro_filtr` `oznameni` → `2026-02-02`; zprávy o transakci: [lupa.cz/aktuality/driv-koordinovali-jeziska-ted-dva-kamaradi-ziskali-se-stejn…](https://www.lupa.cz/aktuality/driv-koordinovali-jeziska-ted-dva-kamaradi-ziskali-se-stejnym-principem-penize-na-ai-agenta-pro-e-commerce/)
- další: **Bandits**, `datum_pro_filtr` `oznameni` → `2025-11-20`; zprávy o transakci: [lupa.cz/aktuality/aby-se-lepe-jelo-na-vlne-umele-inteligence-miton-investuje-…](https://www.lupa.cz/aktuality/aby-se-lepe-jelo-na-vlne-umele-inteligence-miton-investuje-do-startupu-ktery-ji-chce-firmam-zefektivnit/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - DeepScout: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - ACE (padelová aplikace): `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`, [cc.cz/prodal-startup-americanum-ted-se-veze-na-vlne-padelu-pulku-jeho-nove-ap…](https://cc.cz/prodal-startup-americanum-ted-se-veze-na-vlne-padelu-pulku-jeho-nove-aplikace-ziskava-za-miliony-miton/)
  - Whisper (AI agent pro zákaznickou podporu v e-commerce): `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Bandits: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „MITON CZ, s.r.o., Křižíkova 148/34, Karlín, 186 00 Praha 8“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „DeepScout“, `datum_investice` `null`, `datum_oznameni` `2026-10-19`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`
  - zprava_o_transakci, Lupa.cz, zdroj_datum `2026-10-19`, puvod `null`: [lupa.cz/aktuality/miton-veri-v-ai-agenty-v-e-commerce-miliony-posila-do-sluzb…](https://www.lupa.cz/aktuality/miton-veri-v-ai-agenty-v-e-commerce-miliony-posila-do-sluzby-ktera-jim-umoznuje-hlidat-ceny-napric-trhem/)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- DeepScout: Lupa.cz (puvod `null`) [lupa.cz/aktuality/miton-veri-v-ai-agenty-v-e-commerce-miliony-posila-do-sluzb…](https://www.lupa.cz/aktuality/miton-veri-v-ai-agenty-v-e-commerce-miliony-posila-do-sluzby-ktera-jim-umoznuje-hlidat-ceny-napric-trhem/)
- ACE (padelová aplikace): CzechCrunch (puvod `null`) [cc.cz/prodal-startup-americanum-ted-se-veze-na-vlne-padelu-pulku-jeho-nove-ap…](https://cc.cz/prodal-startup-americanum-ted-se-veze-na-vlne-padelu-pulku-jeho-nove-aplikace-ziskava-za-miliony-miton/); Miton (tisková zpráva na webu investora) (puvod `null`) [miton.cz/blog/miton-investuje-do-ace-stravu-pro-padel-uz-pouziva-vice-nez-pol…](https://www.miton.cz/blog/miton-investuje-do-ace-stravu-pro-padel-uz-pouziva-vice-nez-polovina-ceskych-hracu/)
- Whisper (AI agent pro zákaznickou podporu v e-commerce): Lupa.cz (puvod `null`) [lupa.cz/aktuality/driv-koordinovali-jeziska-ted-dva-kamaradi-ziskali-se-stejn…](https://www.lupa.cz/aktuality/driv-koordinovali-jeziska-ted-dva-kamaradi-ziskali-se-stejnym-principem-penize-na-ai-agenta-pro-e-commerce/)
- Bandits: Lupa.cz (puvod `null`) [lupa.cz/aktuality/aby-se-lepe-jelo-na-vlne-umele-inteligence-miton-investuje-…](https://www.lupa.cz/aktuality/aby-se-lepe-jelo-na-vlne-umele-inteligence-miton-investuje-do-startupu-ktery-ji-chce-firmam-zefektivnit/)

**`sektory`**: Sektory odpovídají zdroji
- AI a augmented workforce, krypto a web3, e-commerce, gastrotech, psychedelika a duševní zdraví; zdroj [miton.cz/o-nas/](https://www.miton.cz/o-nas/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `300000`, `max` `2000000`, `mena` `EUR`; zdroj [miton.cz/o-nas/](https://www.miton.cz/o-nas/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: Miton se na webu popisuje nadpisem „VC, ale ne tak úplně“, „Investujeme vlastní peníze“ a „nepodléháme klasickému fondovému cyklu“; investuje do startupů od pre-seed po series A s deklarovaným ticketem 300k–2M EUR („Obvyklá výše vstupní investice + follow-up investice v podobném řádu nebo vyšší“), má tým (web: 25 lidí) a partnery (např. Tomáš Hodboď), média ho nazývají „investiční skupina Miton“ (CzechCrunch 1. 10. 2026, Lupa 20. 11. 2025). Kapitál je vlastní kapitál zakladatelů a partnerů, ne LP fondu; nejde o holding jednoho podnikatele (zakladatelé Ondřej Raška, Tomáš Matějček, Milan Zemánek a další partneři) ani o provozní firmu (web popisuje jen investiční činnost), proto VC; funding.tech.eu ho ale vede jako „Corporate“ (viz nejasnosti). Často spoluzakládá firmy (Bandits: Miton „jako zakládající partner“; ACE: „rovnocenný partner“, partner Mitonu Hodboď se firmě věnuje), tj. venture-builder model s vlastním kapitálem za podíl. Identita: ARES MITON CZ, s.r.o., IČO 25417967, Křižíkova 148/34, Praha 8 (shodná s kancelářskou adresou na webu), jednatelé Milan Zemánek, Ondřej Raška, Tomáš Matějček, předmět podnikání mj. „Investování do startupů a jiných společností“, jediný společník M8H a.s. (IČO 04765117, představenstvo Matějček, Zemánek, Raška, Michal Jirák). Web (o-nas) uvádí „Jsme tři - Ondra, Tomáš, Milan“ a „Zakládáme MITON CZ, s.r.o.“, totožnost potvrzená. Skupina má desítky SPV „MITON …“ na stejné adrese (např. MITON INVESTMENT, a.s., IČO 27343430; MITON C a.s. a MITON Psychonauts s.r.o., jejichž spojení s kryptofondem Miton C a fondem Psychonauts jsem nepotvrdil), které jsou podřízené jedné investiční firmě; kterou entitou byla konkrétní investice provedena, zdroje neuvádějí. Ticket: deklarovaný na webu. Kapitál: nevyplněn; web uvádí „hodnota portfolia 450 mil. EUR“, to není investorem uvedené AUM / upsaný kapitál / velikost fondu; starší zpráva (Lupa 9. 11. 2021) o kryptofondu „na investice má stovky milionů“ je záměr bez přesné částky. Velikosti investic (vklad Mitonu, ne kola): Bandits 400 tis. EUR („Miton posílá 400 tisíc eur … do startupu Bandits“), Whisper 300 tis. EUR („získal na investici 300 tisíc eur“, financování posílá Miton), DeepScout „v milionech korun“ (Lupa 19. 10. 2026; dříve 5 mil. Kč v lednu 2025), ACE „řádově miliony korun“. Nástroj: doložený podíl u ACE (CzechCrunch: „Investiční skupina Miton se stává partnerem jeho padelové aplikace Ace a získává v ní poloviční podíl“); u DeepScout, Whisper a Bandits zdroje nástroj ani kolo neuvádějí (nezjisteno). Jistota investice stredni: ACE dokládá CzechCrunch a tisková zpráva na blogu Mitonu se stejným datem 1. 10. 2026; nezávislost původu nelze doložit (CzechCrunch neuvádí zdroj, pravděpodobně společné oznámení), ostatní investice mají jednu zprávu. Datum investice žádný zdroj neuvádí, všude jen datum oznámení. Poslední investice (DeepScout, 19. 10. 2026) je nejnovější nalezená, ne nutně skutečně poslední; funding.tech.eu dále uvádí Aim (7/2025), Firefish seed (4/2025) a DeepScout (3/2025), ty jsem zprávou neověřoval.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="41-cz-presto-ventures"></a>
### 41. Presto Ventures (`cz-presto-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [prestoventures.com/](https://www.prestoventures.com/)

Nálezy AI: [nalezy_ai.md#cz-presto-ventures](nalezy_ai.md#cz-presto-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Presto Ventures II a.s., osoba rizikového kapitálu“, IČO `11678704`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `2026-09-26`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/11678704](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/11678704)
  - web_subjektu, web investora, zdroj_datum `2026-05-25`, puvod `null`: [prestoventures.com/](https://www.prestoventures.com/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **SatVu (Satellite Vu)**, `datum_pro_filtr` `oznameni` → `2026-02-18`; zprávy o transakci: [pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-sc…](https://pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-scale-multi-satellite-constellation/amp/), [csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthe…](https://csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthening-space-and-thermal-intelligence-capabilities)
- další: **Occam (Occam Industries)**, `datum_pro_filtr` `oznameni` → `2026-02-11`; zprávy o transakci: [cc.cz/investori-v-cele-s-miliardarem-michalem-strnadem-posilaji-desitky-milio…](https://cc.cz/investori-v-cele-s-miliardarem-michalem-strnadem-posilaji-desitky-milionu-na-vyvoj-autonomnich-dronu/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - SatVu (Satellite Vu): `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`, [pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-sc…](https://pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-scale-multi-satellite-constellation/amp/)
  - Occam (Occam Industries): `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [cc.cz/investori-v-cele-s-miliardarem-michalem-strnadem-posilaji-desitky-milio…](https://cc.cz/investori-v-cele-s-miliardarem-michalem-strnadem-posilaji-desitky-milionu-na-vyvoj-autonomnich-dronu/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Presto Ventures II a.s., osoba rizikového kapitálu“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „SatVu (Satellite Vu)“, `datum_investice` `null`, `datum_oznameni` `2026-02-18`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `podil`, `doklad` `dolozeno`, `kolo` `null`
  - zprava_o_transakci, Pulse 2.0, zdroj_datum `2026-02-18`, puvod `null`: [pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-sc…](https://pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-scale-multi-satellite-constellation/amp/)
  - zprava_o_transakci, CSG (tisková zpráva), zdroj_datum `null`, puvod `null`: [csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthe…](https://csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthening-space-and-thermal-intelligence-capabilities)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- SatVu (Satellite Vu): Pulse 2.0 (puvod `null`) [pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-sc…](https://pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-scale-multi-satellite-constellation/amp/); CSG (tisková zpráva) (puvod `null`) [csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthe…](https://csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthening-space-and-thermal-intelligence-capabilities)
- Occam (Occam Industries): CzechCrunch (puvod `null`) [cc.cz/investori-v-cele-s-miliardarem-michalem-strnadem-posilaji-desitky-milio…](https://cc.cz/investori-v-cele-s-miliardarem-michalem-strnadem-posilaji-desitky-milionu-na-vyvoj-autonomnich-dronu/)

**`sektory`**: Sektory odpovídají zdroji
- security, defense, aerospace, dual-use; zdroj [prestoventures.com/](https://www.prestoventures.com/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `500000`, `max` `5000000`, `mena` `EUR`; zdroj [prestoventures.com/](https://www.prestoventures.com/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: Presto Ventures II a.s. je v ARES zapsána jako 'osoba rizikového kapitálu'; web: 'Since 2016, we’ve invested €40M from two funds.' a doložené investice do startupů za podíl. Současná strategie podle webu: 'Security, defense, and aerospace' (dual-use), 'Seed TO SERIES A', 'Tickets ranging from €500k to €5M.' (deklarovaný ticket). Identita: ARES Presto Ventures II a.s., osoba rizikového kapitálu, IČO 11678704, sídlo Revoluční 763/15, Praha 1 (do 1. 7. 2026 Na příkopě 859/22, tuto adresu uvádí i pozvánka na valnou hromadu na webu z 25. 5. 2026, čímž je entita propojena s webem); představenstvo od 1. 7. 2026 Eduard Kučera, Roman Nováček, předseda Miloš Kratochvíl (dříve Přemysl Rubeš, Lucie Brešová). Související entity na stejné adrese: Presto 2 GP s.r.o. (IČO 10803416, společníci mj. Přemysl Rubeš), Presto Management s.r.o. (IČO 19729740, jednatel Eduard Kučera) a Presto PTH a.s. (IČO 22147187, Na příkopě 859/22; v ARES člen správní rady Přemysl Rubeš, poslední aktualizace 2025-05-01). Který subjekt je správcem fondu Presto Tech Horizons, nepotvrzeno. Web uvádí kancelář Senovážné náměstí 869/28, Praha 1; sídlo investiční firmy je v každém případě ČR. Presto Tech Horizons (PTH) je fond Presto Ventures: CzechCrunch 11. 2. 2026 ho popisuje jako fond, 'jejž založila společnost Presto Ventures a zbrojařská skupina' CSG; web Presto ho vede jako vlastní fond ('Our new €150M fund targets ...'). Fond tedy vedu jako podřízený údaj, ne samostatného investora. Kapitál: web uvádí 'Our new €150M fund targets ...' (cíl) a CzechCrunch 26. 6. 2024 'Disponuje celkem 150 miliony eur' (k dispozici; titulek uvádí 4 miliardy, text 3,7 mld. Kč, rozpor), ani jedno není doložené aum/committed_capital/fund_size, proto kapital prázdný. Údaj '€40M from two funds' jsou proinvestované peníze, ne kapitál. Poslední investice: SatVu (UK), kolo 30 mil. GBP (velikost celého kola, ne vklad Presto), vedené NATO Innovation Fund; Pulse 2.0 18. 2. 2026 jmenuje Presto Tech Horizons mezi investory a uvádí 'bringing its total equity funding to £60 million', proto nástroj podíl dolozeno (kolo jako equity). Označení série si u agregátorů odporuje (Seedtable series A, CB Insights series C, Caplight series B), proto kolo null. Tisková zpráva CSG (partner a investor PTH) uvádí 'Presto Tech Horizons (PTH), a venture capital fund in which CSG is a partner and investor' a 'GBP 30 million investment round'; datum na stránce neuvedeno. Zda Pulse 2.0 vychází z tiskové zprávy SatVu a zda je nezávislá na TZ CSG, nedoloženo, proto jistota investice stredni. Další: Occam (UK), pre-seed 3 mil. EUR (velikost kola), vedl Presto Tech Horizons podle CzechCrunch 11. 2. 2026; nástroj neprima_indicie (pre-seed). Agregátory uvádějí i Choice series A (březen 2026) a Sloneek (červen 2026) s Presto, zprávu s Presto jmenovaným jsem nenašel, nezapsáno. Kontext: CzechCrunch 11. 3. 2026: zakladatel Přemysl Rubeš byl zadržen policií (podle partnera Vojty Ročka nesouvisí s podnikáním); fond PTH uvádí, že spolupráce s ním skončila v září 2025 a investiční činnost to neovlivňuje. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="42-cz-purposetech"></a>
### 42. PurposeTech (`cz-purposetech`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [purposetech.vc/](https://www.purposetech.vc/)

Nálezy AI: [nalezy_ai.md#cz-purposetech](nalezy_ai.md#cz-purposetech) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „PurposeTech s.r.o.“, IČO `19183992`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `null`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19183992](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19183992)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [purposetech.vc/](https://www.purposetech.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **auryx**, `datum_pro_filtr` `oznameni` → `2026-04-30`; zprávy o transakci: [enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/](https://www.enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/), [vestbee.com/insights/articles/auryx-raises-2-m](https://vestbee.com/insights/articles/auryx-raises-2-m), [businesscloud.co.uk/?p=195297](https://businesscloud.co.uk/?p=195297)
- další: **Tingit**, `datum_pro_filtr` `oznameni` → `2026-02-10`; zprávy o transakci: [vestbee.com/insights/articles/tingit-secures-1-5-m](https://vestbee.com/insights/articles/tingit-secures-1-5-m), [ellex.legal/project/tingit-com-platform-secures-investment/](https://ellex.legal/project/tingit-com-platform-secures-investment/)
- další: **Lifeyear**, `datum_pro_filtr` `oznameni` → `2025-07-01`; zprávy o transakci: [en.ain.ua/2025/07/01/lifeyear-raises-eur28m/](https://en.ain.ua/2025/07/01/lifeyear-raises-eur28m/)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - auryx: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/](https://www.enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/)
  - Tingit: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje
  - Lifeyear: `hodnota` `null`, `doklad` `nezjisteno`, `kolo` `null`, bez zdroje

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „PurposeTech s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „auryx“, `datum_investice` `null`, `datum_oznameni` `2026-04-30`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`
  - zprava_o_transakci, Cambridge Enterprise (spoluinvestor v kole), zdroj_datum `2026-04-30`, puvod `oznámení auryx / Cambridge Enterprise`: [enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/](https://www.enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/)
  - zprava_o_transakci, Vestbee, zdroj_datum `2026-04-30`, puvod `informace od auryx („as Vestbee was informed“), pravděpodobně stejné oznámení`: [vestbee.com/insights/articles/auryx-raises-2-m](https://vestbee.com/insights/articles/auryx-raises-2-m)
  - zprava_o_transakci, BusinessCloud, zdroj_datum `2026-05-01`, puvod `nedoloženo, pravděpodobně stejné oznámení auryx`: [businesscloud.co.uk/?p=195297](https://businesscloud.co.uk/?p=195297)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- auryx: Cambridge Enterprise (spoluinvestor v kole) (puvod `oznámení auryx / Cambridge Enterprise`) [enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/](https://www.enterprise.cam.ac.uk/news/auryx-2m-earbuds-continuous-health-monitors/); Vestbee (puvod `informace od auryx („as Vestbee was informed“), pravděpodobně stejné oznámení`) [vestbee.com/insights/articles/auryx-raises-2-m](https://vestbee.com/insights/articles/auryx-raises-2-m); BusinessCloud (puvod `nedoloženo, pravděpodobně stejné oznámení auryx`) [businesscloud.co.uk/?p=195297](https://businesscloud.co.uk/?p=195297)
- Tingit: Vestbee (puvod `null`) [vestbee.com/insights/articles/tingit-secures-1-5-m](https://vestbee.com/insights/articles/tingit-secures-1-5-m); Ellex (právní poradce transakce) (puvod `null`) [ellex.legal/project/tingit-com-platform-secures-investment/](https://ellex.legal/project/tingit-com-platform-secures-investment/)
- Lifeyear: AIN.UA (puvod `null`) [en.ain.ua/2025/07/01/lifeyear-raises-eur28m/](https://en.ain.ua/2025/07/01/lifeyear-raises-eur28m/)

**`sektory`**: Sektory odpovídají zdroji
- Health, Climate, Future of Work; zdroj [purposetech.vc/](https://www.purposetech.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- nevyplněno (`null`)

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: vlastní popis „PurposeTech is a pre-seed fund that backs founders reshaping Health, Climate, and the Future of Work“ (purposetech.vc); Vestbee 25. 9. 2024: uzavřel „pre-seed venture capital fund“; funding.tech.eu typ „Venture capital“. Samostatná investiční firma se sídlem v ČR, ne korporace ani family office. Identita: ARES PurposeTech s.r.o., IČO 19183992, Drtinova 557/10, Praha 5, vznik 2023-03-24, jednatel Zdeněk Fred Fous (na webu „Co-Founder & GP“), společníci ZEFIRIA, s.r.o. (60 %) a Impact Hub Czechia, a.s. (40 %); web uvádí „PurposeTech, s.r.o.“, Drtinova 557/10 a „founded in 2023 by serial entrepreneur Zdenek Fred Fous and Impact Hub“. Fond: PurposeTech F1 s.r.o., osoba rizikového kapitálu (dříve PurposeTech Fund I. s.r.o.), IČO 19185103, 100% vlastněný PurposeTech s.r.o., jednatel Fous – podřízený fond, ne samostatný investor. Sídlo investiční firmy Praha. Ticket: web má u otázky na typickou výši investice jen zástupný text (Lorem ipsum); CzechCrunch (10. 2. 2026) uvádí plán druhého fondu PT Capital podpořit firmu zhruba 0,5–1 mil. EUR – jde o plán fondu, který ještě neinvestuje, proto ticket nevyplněn. Kapitál: CzechCrunch uvádí, že první fond „od asi dvacítky investorů získali necelých šedesát milionů korun“ – nepřesná částka bez druhu ukazatele, nevyplněno; PT Capital „maximální velikost … deset milionů eur“ je cíl, zbytek se teprve získává, není kapitál. Poslední investice: auryx (Cambridge, UK), pre-seed kolo 2 mil. USD (velikost celého kola, ne vklad; BusinessCloud uvádí 1,5 mil. GBP) vedené Celero Ventures, „with participation from EWOR, Cambridge Enterprise Ventures, Vento, PurposeTech“ (Cambridge Enterprise 30. 4. 2026), Vestbee 30. 4. 2026 „with participation from PurposeTech“. Nástroj neprima_indicie (pre-seed kolo, nástroj neuveden). Další: Tingit (Litva), kolo 1,5 mil. EUR (velikost kola) vedené Coinvest Capital, „with participation from … Purpose Tech“ (Vestbee 10. 2. 2026), Ellex: „existing foreign investors in Tingit – … Czechia's Purpose Tech“; označení kola neuvedeno → nástroj nezjištěn. Lifeyear (UK/Estonsko), 2,8 mil. EUR včetně 1,5 mil. EUR grantu, „€1.3 million from venture capital funds, including Verge HealthTech Fund, Tilia Impact Ventures, PurposeTech“ (AIN 1. 7. 2025); kolo neoznačeno, nezjištěno. Jistota investice stredni: žádná investice nemá doložený nástroj a nezávislost zpráv o auryx (pravděpodobně jedno oznámení) nedoložena. Oddělení od Tilia Impact Ventures: jiná firma (viz par_cz-purposetech__cz-tilia-impact-ventures.md), společná je adresa Impact Hubu a Petr Vítek (spoluzakladatel Tilia, u PurposeTech v Advisory Board). Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="43-cz-tilia-impact-ventures"></a>
### 43. Tilia Impact Ventures (`cz-tilia-impact-ventures`)

Soubor: `investori.json` · rozhodnutí agenta: **zařazen** · typ `VC` · země `CZ` · status `aktivni` · web [tilia.vc/](https://tilia.vc/)

Nálezy AI: [nalezy_ai.md#cz-tilia-impact-ventures](nalezy_ai.md#cz-tilia-impact-ventures) (číst až po commitu prvních verdiktů)

**`existence`**: Subjekt existuje (rejstřík nebo regulátor)
- `pravni_subjekt`: „Tilia Impact Ventures, osoba rizikového kapitálu, s.r.o.“, IČO `17848911`
  - rejstrik, ARES (výpis z veřejného rejstříku), zdroj_datum `null`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17848911](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/17848911)
  - web_subjektu, web investora, zdroj_datum `null`, puvod `null`: [tilia.vc/](https://tilia.vc/)
- `jistota.existence`: `vysoka`

**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně 24 měsíců (okno od 2024-10-26, hranice 12 měsíců 2025-10-26)
- `status`: `aktivni`
- poslední: **FaceUp**, `datum_pro_filtr` `oznameni` → `2026-05-19`; zprávy o transakci: [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do), [itbrief.com.au/story/faceup-raises-usd-5-million-to-expand-compliance-suite](https://itbrief.com.au/story/faceup-raises-usd-5-million-to-expand-compliance-suite); podpůrné: rejstrik_spolecnik [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06142630](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06142630)
- další: **Theorema**, `datum_pro_filtr` `oznameni` → `2026-03-31`; zprávy o transakci: [vestbee.com/insights/articles/theorema-secures-2-85-m](https://vestbee.com/insights/articles/theorema-secures-2-85-m)
- další: **Minimist**, `datum_pro_filtr` `oznameni` → `2026-03-25`; zprávy o transakci: [trendingtopics.eu/minimist-anna-greil-ueber-das-neue-millioneninvestment/](https://www.trendingtopics.eu/minimist-anna-greil-ueber-das-neue-millioneninvestment/)
- další: **Flox Intelligence**, `datum_pro_filtr` `oznameni` → `2026-02-27`; zprávy o transakci: [pulse2.com/flox-intelligence-3-million-raised-to-scale-ai-wildlife-intelligen…](https://pulse2.com/flox-intelligence-3-million-raised-to-scale-ai-wildlife-intelligence-platform/), [techcrunch.com/?p=3173721](https://techcrunch.com/?p=3173721)

**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3
- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`
- podmínka 3, nástroj u jednotlivých investic:
  - FaceUp: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`, [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do)
  - Theorema: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [vestbee.com/insights/articles/theorema-secures-2-85-m](https://vestbee.com/insights/articles/theorema-secures-2-85-m)
  - Minimist: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `pre-seed`, [trendingtopics.eu/minimist-anna-greil-ueber-das-neue-millioneninvestment/](https://www.trendingtopics.eu/minimist-anna-greil-ueber-das-neue-millioneninvestment/)
  - Flox Intelligence: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `seed`, [pulse2.com/flox-intelligence-3-million-raised-to-scale-ai-wildlife-intelligen…](https://pulse2.com/flox-intelligence-3-million-raised-to-scale-ai-wildlife-intelligence-platform/)

**`typ`**: Typ je zařazen správně
- `typ`: `VC`, zdůvodnění agenta je v poznámce na konci oddílu

**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)
- `typ` `VC`, `zeme` `CZ`, sídlo podle `pravni_subjekt`: „Tilia Impact Ventures, osoba rizikového kapitálu, s.r.o.“

**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`)
- `firma` „FaceUp“, `datum_investice` `null`, `datum_oznameni` `2026-05-19`, `datum_pro_filtr` `oznameni`
- `nastroj`: `hodnota` `null`, `doklad` `neprima_indicie`, `kolo` `series A`
  - zprava_o_transakci, JIC (tisková zpráva spoluinvestora JIC Ventures), zdroj_datum `2026-05-19`, puvod `null`: [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do)
  - zprava_o_transakci, IT Brief Australia, zdroj_datum `2026-05-22`, puvod `nedoloženo, pravděpodobně oznámení FaceUp/investorů (citace představitelů firmy a investorů)`: [itbrief.com.au/story/faceup-raises-usd-5-million-to-expand-compliance-suite](https://itbrief.com.au/story/faceup-raises-usd-5-million-to-expand-compliance-suite)
  - rejstrik_spolecnik, ARES (výpis z veřejného rejstříku), zdroj_datum `null`, puvod `null`: [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06142630](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06142630)

**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ
- `jistota.investice`: `stredni`
- FaceUp: JIC (tisková zpráva spoluinvestora JIC Ventures) (puvod `null`) [jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do](https://www.jic.cz/en/about-us/pro-media/prvni-investice-noveho-fondu-jic-ventures-miri-do); IT Brief Australia (puvod `nedoloženo, pravděpodobně oznámení FaceUp/investorů (citace představitelů firmy a investorů)`) [itbrief.com.au/story/faceup-raises-usd-5-million-to-expand-compliance-suite](https://itbrief.com.au/story/faceup-raises-usd-5-million-to-expand-compliance-suite)
- Theorema: Vestbee (puvod `LinkedIn příspěvek Tilia Impact Ventures`) [vestbee.com/insights/articles/theorema-secures-2-85-m](https://vestbee.com/insights/articles/theorema-secures-2-85-m)
- Minimist: Trending Topics (puvod `oznámení Minimist`) [trendingtopics.eu/minimist-anna-greil-ueber-das-neue-millioneninvestment/](https://www.trendingtopics.eu/minimist-anna-greil-ueber-das-neue-millioneninvestment/)
- Flox Intelligence: Pulse 2.0 (puvod `nedoloženo (pravděpodobně oznámení Flox)`) [pulse2.com/flox-intelligence-3-million-raised-to-scale-ai-wildlife-intelligen…](https://pulse2.com/flox-intelligence-3-million-raised-to-scale-ai-wildlife-intelligence-platform/); TechCrunch (puvod `null`) [techcrunch.com/?p=3173721](https://techcrunch.com/?p=3173721)

**`sektory`**: Sektory odpovídají zdroji
- sector-agnostic (impact-driven); zdroj [tilia.vc/](https://tilia.vc/), zdroj_datum `null`

**`ticket`**: Ticket odpovídá zdroji
- `min` `300000`, `max` `1200000`, `mena` `EUR`; zdroj [tilia.vc/](https://tilia.vc/), zdroj_datum `null`

**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)
- nevyplněno (prázdný seznam)

<details><summary>Poznámka agenta (celá)</summary>

Typ VC: Vestbee (14. 3. 2024, VC of the month) „Tilia Impact Ventures is a Prague-based seed stage VC fund“; web tilia.vc „Tilia Impact Ventures backs Czech and CEE region founders to make systemic environmental and social change“, nástroje „Equity / Convertible debt“; funding.tech.eu typ „Venture capital“. Samostatná investiční firma, ne korporace ani family office; impact je investiční strategie. Identita: ARES Tilia Impact Ventures, osoba rizikového kapitálu, s.r.o. (do 2024-12-01 Tilia Impact Ventures - Fund 1 s.r.o.), IČO 17848911, Drtinova 557/10, Praha 5, zapsána 2022-12-19, od 2024-12-01 správa majetku podle § 15 ZISIF; jednatelé a společníci (po 1/2) Dr. Silke Horáková a Petr Vítek – na webu co-founders; adresa shodná s webem. Související Tilia Impact Partners s.r.o. (IČO 17621615, Drtinova 557/10, poradenství, jednatel Pavel Petřek, partner na webu) – role ve struktuře nedoložena. Fond II je lucemburský subjekt „Tilia Impact Ventures Fund II“ (51-53 rue de Merl, Lucemburk) zapsaný jako společník FaceUp Technology s.r.o. – podřízený fond, ne samostatný investor. Sídlo investiční firmy (značky) Praha. Ticket: web „0.3 - 1.2m EUR initial ticket“ (Vestbee 2024 uvádí €300k–1.5M). Kapitál nevyplněn: druhý fond Impact Seed Fund – Causeartist (15. 9. 2023) „successful first closing of its second fund, totaling €26m“ a cíl 32 mil. EUR, CzechCrunch (21. 9. 2023) „potvrzených 26 milionů eur“; druh ukazatele (committed/fund size) zdroj výslovně neuvádí a finální closing 32 mil. EUR nedoložen (Vestbee 2024 „second €32 million fund“ bez upřesnění) – proto prázdné. Poslední investice: FaceUp (Brno), Series A 5 mil. USD (velikost celého kola, ne vklad) vedená Fil Rouge Capital; JIC 19. 5. 2026: „Existing investors Jiří Hlavenka, Tilia Impact Ventures and Reflex Capital also took part“; IT Brief 22. 5. 2026: „Existing investor Tilia Impact Ventures also participated.“ Rejstřík FaceUp Technology s.r.o. (IČO 06142630): Tilia Impact Ventures Fund II společníkem od 2024-07-15 (podíl 9742/129894) – dokládá držbu podílu z dřívějšího seed kola (oznámeno 10/2024), ne nástroj účasti v Series A 2026, proto nástroj jen neprima_indicie. Další: Theorema, pre-seed 2,85 mil. EUR (velikost kola), Vestbee 31. 3. 2026 „pre-seed round was supported by … Tilia Impact Ventures“; Minimist (Vídeň), pre-seed 1 mil. EUR (velikost kola), Trending Topics 25. 3. 2026 „Die Runde wurde von Tilia Impact Ventures (mit Unterstützung von InvestEU) angeführt“; Flox Intelligence (Stockholm), Seed+ 3 mil. USD (velikost kola), Pulse 2.0 27. 2. 2026 „Seed+ round led by Tilia Impact Ventures“, TechCrunch 13. 10. 2026 „seed round led by Unconventional Ventures and Tilia Impact Ventures“. Investice PurposeTech nepřipisovány; Lifeyear (AIN 1. 7. 2025 výslovně jmenuje Tilia) neuveden mezi dalšími, protože novější investice stačí. Jistota investice stredni: žádná investice nemá nástroj výslovně doložen (jen kolo series A / pre-seed / seed) a u FaceUp nezávislost dvou zpráv nedoložena. Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.

</details>

Řádky v `hodnoceni.csv`: `existence`, `investicni_cinnost`, `je_investor`, `typ`, `rozsah_pilotu`, `posledni_investice`, `nezavislost_zdroju`, `sektory`, `ticket`, `kapital`

<a id="44-cz-arx-equity-partners"></a>
### 44. ARX Equity Partners (`cz-arx-equity-partners`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [arxequity.com/](https://www.arxequity.com/)

Nálezy AI: [nalezy_ai.md#cz-arx-equity-partners](nalezy_ai.md#cz-arx-equity-partners) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ PE, ne VC/CVC. Vlastní popis: „a leading Central European private equity firm“ (TZ Medicofit) a „ARX has become a leading private equity firm in its segment operating in the Central European“ region, zaměření na „mid-sized CE companies“, cíle „management or family-owned enterprises“, „more than € 300 million raised in four funds“ (About ARX). Doložená investice v okně: ARX 26. 8. 2026 oznámil „the acquisition of a majority stake in Medicofit“ (Slovinsko; nástroj podíl doložen), potvrzeno i Karanović & Partners (poradce ARX, nejde o nezávislý původ); dále HLB PROXY (většinový podíl, oznámeno 30. 1. 2026). Identita: Arx Equity Partners s.r.o., IČO 64943356, Praha 1, jednatelé Tomáš Lánský, Michal Aron, Brian Albert Wardrop, 100% společník ARX Equity Partners B.V. (Amsterdam); web uvádí „Headquartered in Prague“. Sídlo tedy pilotu nevadí, rozhoduje typ PE.

**Zdroje uvedené agentem:**
- [arxequity.com/about-arx/](https://www.arxequity.com/about-arx/)
- [arxequity.com/arx-equity-partners-acquires-majority-stake-in-medicofit-sloven…](https://www.arxequity.com/arx-equity-partners-acquires-majority-stake-in-medicofit-slovenias-leading-private-physiotherapy-provider/)
- [karanovicpartners.com/news/arx-equity-partners-acquires-majority-stake-in-med…](https://www.karanovicpartners.com/news/arx-equity-partners-acquires-majority-stake-in-medicofit/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/64943356](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/64943356)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="45-cz-mam-private-equity-fund"></a>
### 45. MAM Private Equity Fund SICAV a.s. (`cz-mam-private-equity-fund`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [mam-equity.cz/](https://www.mam-equity.cz/)

Nálezy AI: [nalezy_ai.md#cz-mam-private-equity-fund](nalezy_ai.md#cz-mam-private-equity-fund) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ PE, ne VC/CVC. Identita: MAM Private Equity Fund SICAV a.s., IČO 19381603, Klimentská 1216/46, Praha 1 (ARES; obhospodařovatel WOOPE investiční společnost a.s., IČO 09698051, zástupci Aleš Nykodým, Roman Sládek, Jan Novák = managing partneři uvedení na mam-equity.cz; poradce fondu MA Management, a.s.). Typ PE podle vlastního popisu a fungování: web „Investice do středně velkých ziskových společností v regionu střední Evropy“, „EBITDA na úrovni 25 až 250 mil Kč“, „Cílíme na společnosti, které nemají vyřešené nástupnictví“, většinové podíly Raycom 90 %, COMGUARD 70,4 %. Doložená investice v okně: TZ 8. 9. 2026 „Společnost ME Logistics Holding, za níž stojí investiční skupiny MAM Private Equity Fund a EDTI Group, dokončila akvizici 100% podílu ve společnostech PJ EXPEDIS a MUFF Logistics“, „V ME Logistics Holding drží fond 36% podíl“ (podíl doložen, status by byl aktivni); dále UNIPAP Packaging: TZ 24. 9. 2025 „MAM Private Equity Fund tak bude polovičním vlastníkem“ a Deloitte M&A Port 24. 9. 2025 „The company will be split evenly between BHS Private Equity Fund and MAM Private Equity Fund“. Sídlo ČR, rozsah pilotu nesplňuje kvůli typu.

**Zdroje uvedené agentem:**
- [mam-equity.cz/](https://www.mam-equity.cz/)
- [cdn.prod.website-files.com/64b63f96f6f93ab9880b90aa/6a9fbb232feede340d9d5c4f_…](https://cdn.prod.website-files.com/64b63f96f6f93ab9880b90aa/6a9fbb232feede340d9d5c4f_dffc421837b40cffff0c9ed92e6cb832_20260908_TZ_Akvizice_PJ%20Expedis%20a%20Muff%20Logistic%20vstupuj%C3%AD%20do%20nov%C3%A9%20etapy.pdf)
- [cdn.prod.website-files.com/64b63f96f6f93ab9880b90aa/68d2b2fb0d7e7d478cbb72a9_…](https://cdn.prod.website-files.com/64b63f96f6f93ab9880b90aa/68d2b2fb0d7e7d478cbb72a9_20250924_TZ_UNIPAP_Packaging.pdf)
- [deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zab…](https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zabalily-unipap.html)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19381603](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19381603)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="46-cz-everita-capital"></a>
### 46. EVERITA Capital (`cz-everita-capital`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [everitacap.com/](https://everitacap.com/)

Nálezy AI: [nalezy_ai.md#cz-everita-capital](nalezy_ai.md#cz-everita-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor, ale typ PE, ne VC/CVC. Vlastní popis: TZ z 31. 3. 2026 'EVERITA Capital, a private equity investment fund focused on investing in small and medium-sized companies in Central Europe'; web: '30 years of private equity experience', 'minority or majority' equity tickety 2-5 mil. EUR do zavedených ziskových SME s tržbami nad 3 mil. EUR; rozhovor Newstream 8. 5. 2025: 'naše minimum je podíl okolo 35 procent'. Doložené investice: Clintrial s.r.o. (Praha) – 31. 8. 2026 'has acquired, together with co-investors, a majority stake' (web EVERITA, potvrzuje Investors in Healthcare 1. 9. 2026; status by byl aktivni); Pekarna Hrstić (Split) – 31. 3. 2026 51% podíl (TZ EVERITA a tportal.hr). Existence: ARES EVERITA Capital s.r.o. (dříve EVERITA Investments s.r.o.), IČO 19067097, sídlo Na Florenci 2116/15, Praha 1, jednatelé a společníci Emília Wardrop Mamajová a Marko Jojič = Managing Partner a Partner podle webu. Sídlo v ČR splněno, rozhoduje typ.

**Zdroje uvedené agentem:**
- [everitacap.com/news/everita-capital-invests-in-the-expansion-of-pekarna-hrsti…](https://everitacap.com/news/everita-capital-invests-in-the-expansion-of-pekarna-hrstic-from-split)
- [everitacap.com/](https://everitacap.com/)
- [everitacap.com/news/everita-capital-vstupuje-do-spolecnosti-clintrial-a-podpo…](https://everitacap.com/news/everita-capital-vstupuje-do-spolecnosti-clintrial-a-podpori-rozvoj-klinickych-hodnoceni-v-cr)
- [investorsinhealthcare.com/articles/category/news/czech-republic-everita-capit…](https://www.investorsinhealthcare.com/articles/category/news/czech-republic-everita-capital-acquires-majority-stake-in-clintrial/)
- [tportal.hr/biznis/clanak/veliko-ulaganje-u-dalmaciji-splitska-pekarnica-dobil…](https://www.tportal.hr/biznis/clanak/veliko-ulaganje-u-dalmaciji-splitska-pekarnica-dobila-strateskog-partnera-20260331)
- [newstream.cz/money/investorka-emilia-mamajova-v-private-equity-je-treba-byt-t…](https://www.newstream.cz/money/investorka-emilia-mamajova-v-private-equity-je-treba-byt-trpelivy)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19067097](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19067097)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="47-cz-bd-partners"></a>
### 47. BD Partners (`cz-bd-partners`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [bdpartners.cz/](https://www.bdpartners.cz/)

Nálezy AI: [nalezy_ai.md#cz-bd-partners](nalezy_ai.md#cz-bd-partners) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ Family office, ne VC/CVC. Ladislav Bartoníček v rozhovoru (CzechCrunch, 28. 7. 2025): „Jsme joint family office. Sem tam můžeme udělat investiční krok stranou“, článek: „nejsme klasický fond“. Fungování odpovídá: web „A Prague-based private investment office … We invest our own capital“ a „We invest exclusively the capital of the two partners: no LPs, no fund cycle“. Investice do startupů (pre-seed až Series A) je investiční strategie, typ nemění (PLAN.md bod 2). Doložená investice v okně: účast v pre-seed kole ValkaAI (12 mil. EUR celé kolo, vedl Rockaway Ventures), Vestbee 24. 2. 2026: „The investment also saw participation from J&T Ventures, Tensor Ventures, BD Partners, and Fond Naše Česko.“ (nástroj neprima_indicie, kolo pre-seed). Identita: BD Partners a.s., IČO 19286511, Generála Píky 430/26, Praha 6, správní rada Ladislav Bartoníček a Jean-Pascal Duvieusart (shoda s webem a CzechCrunch).

**Zdroje uvedené agentem:**
- [cc.cz/sefoval-ppf-ted-investuje-do-startupu-vina-i-betonu-mame-na-to-az-25-mi…](https://cc.cz/sefoval-ppf-ted-investuje-do-startupu-vina-i-betonu-mame-na-to-az-25-miliardy-rika-bartonicek/)
- [bdpartners.cz/](https://www.bdpartners.cz/)
- [vestbee.com/insights/articles/valka-ai-raises-12-m](https://www.vestbee.com/insights/articles/valka-ai-raises-12-m)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19286511](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/19286511)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="48-cz-central-europe-industry-partners"></a>
### 48. Central Europe Industry Partners (`cz-central-europe-industry-partners`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [industrypartners.eu/en/](https://industrypartners.eu/en/)

Nálezy AI: [nalezy_ai.md#cz-central-europe-industry-partners](nalezy_ai.md#cz-central-europe-industry-partners) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor, ale typ PE, ne VC/CVC. Vlastní popis: „CEIP is an Operating Private Equity team with a conservative investment strategy“, ticket „50-250 mil.“ CZK equity, majoritní podíly („majority stake“), zavedené průmyslové firmy CZ/SK; média ho označují jako „private equity fond“ (CzechCrunch 19. 12. 2025, Seznam Zprávy 21. 7. 2026). Transakce v okně 24 měsíců: Timotec koupen přes portfoliovou firmu BLOCK („CEIP, a Czech private equity fund, acquired Timotec through its portfolio company BLOCK“, Deloitte M&A Port 18. 6. 2025); financování skupiny Twist s možností přeměny na menšinový podíl až 30 % (CzechCrunch 19. 12. 2025; CEIP odešel 6/2026 postoupením pohledávky, Seznam Zprávy 2. 6. 2026); Gersys se stal součástí portfoliové AMiT Transportation (web CEIP, 30. 6. 2026). Sídlo ČR: Central Europe Industry Partners, a.s., osoba rizikového kapitálu, IČO 05493234, Na Pankráci 1683/127, Praha 4 (ARES; představenstvo Petr Řehoř, Ondřej Benáček, Jakub Mateo; Benáček je managing partner CEIP podle webu a médií).

**Zdroje uvedené agentem:**
- [industrypartners.eu/en/](https://industrypartners.eu/en/)
- [deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q2/CEIP-enters-t…](https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q2/CEIP-enters-the-German-market-with-acquisition-of-Timotec.html)
- [cc.cz/majitel-trdlokafe-nebo-kytek-od-pepy-se-dohodl-s-investory-penize-mu-po…](https://cc.cz/majitel-trdlokafe-nebo-kytek-od-pepy-se-dohodl-s-investory-penize-mu-poslou-zkuseni-prumyslnici/)
- [seznamzpravy.cz/clanek/ekonomika-firmy-dalsi-rany-pro-twist-insolvencni-navrh…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-dalsi-rany-pro-twist-insolvencni-navrh-na-kytky-od-pepy-i-odchod-investora-307567)
- [industrypartners.eu/en/news/german-company-gersys-becomes-part-of-the-amit-tr…](https://industrypartners.eu/en/news/german-company-gersys-becomes-part-of-the-amit-transportation-group)
- [seznamzpravy.cz/clanek/ekonomika-firmy-fond-ceip-prodal-firmu-roka-industry-v…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-fond-ceip-prodal-firmu-roka-industry-vyrabejici-svarovane-konstrukce-311408)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05493234](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05493234)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="49-cz-emma-capital"></a>
### 49. EMMA Capital (`cz-emma-capital`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [emmacapital.cz/](https://www.emmacapital.cz/)

Nálezy AI: [nalezy_ai.md#cz-emma-capital](nalezy_ai.md#cz-emma-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor za podíl, ale typ Velký soukromý investor, ne VC/CVC. Web se popisuje jako 'private investment holding founded in 2012 by Jiří Šmejc', Šmejc je 'founder and majority shareholder'; aktivní role ve správě portfoliových firem (energie, logistika, gaming, distribuce zdravotnické techniky). Identita: EMMA Capital a.s. (dříve Emerging Markets Capital, a.s.), IČO 24262803, Na Zátorce 672/24, Praha 6, akcionář EMMA CAPITAL LIMITED (Kypr). Doložená investice v okně: Intergame 25. 6. 2026: 'Entain has agreed to sell an initial 20 per cent of its central and eastern Europe arm to joint venture partner EMMA Capital', 'EMMA Capital's shareholding will rise from 22.5 per cent to 42.5 per cent' (koupě podílu v nekótovaném Entain CEE, dokončení Q4 2026). Dále web EMMA: 'EMMA ZETA acquires majority stake in Montenegrin company Urion' (19. 9. 2025) a dokončení akvizice Diamedix (5. 3. 2025).

**Zdroje uvedené agentem:**
- [emmacapital.cz/](https://www.emmacapital.cz/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24262803](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/24262803)
- [intergameonline.com/igaming/news/entain-cee-sell-off-emma-capital-share](https://www.intergameonline.com/igaming/news/entain-cee-sell-off-emma-capital-share)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="50-cz-genesis-capital"></a>
### 50. Genesis Capital (`cz-genesis-capital`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [genesis.cz/](https://www.genesis.cz/)

Nálezy AI: [nalezy_ai.md#cz-genesis-capital](nalezy_ai.md#cz-genesis-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ PE, ne VC/CVC. Vlastní popis: web uvádí „sedm fondů privátního kapitálu o celkové velikosti přes 550 milionů euro“, sekce „Private Equity Funds“ (Genesis Private Equity Fund V, 225 mil. EUR, „obvyklá velikost jednotlivé investice 10-35 milionů euro“, investice do malých a středních podniků) a „Growth Equity Funds“ (GGEF I, 40 mil. EUR, ticket 1–4 mil. EUR, „menší a středně velké společnosti“); slovo venture web nepoužívá. Doložená investice v okně: MediaGuru/ČTK 16. 4. 2026 podle tiskové zprávy Genesis Capital: fond GPEF V „kupuje menšinový podíl ve společnosti POS Media Europe“ (nástroj podíl doložen); tamtéž v březnu 2026 GPEF V „koupil většinový podíl ve společnosti Fyzioterapie s úsměvem“. Identita: ARES Genesis Capital Equity s.r.o. (dříve GENESIS CAPITAL s.r.o.), IČO 25795856, Na Šafránce 1802/22, Praha 10, jednatelé Jan Tauber (zakladatel podle ČTK), Radan Hanzl, Ondřej Vičar, Martin Viliš; sídlo v ČR, rozhoduje typ PE.

**Zdroje uvedené agentem:**
- [genesis.cz/](https://www.genesis.cz/)
- [genesis.cz/en/](https://www.genesis.cz/en/)
- [mediaguru.cz/vlastnik-knihobotu-kupuje-podil-v-pos-media-europe](https://www.mediaguru.cz/vlastnik-knihobotu-kupuje-podil-v-pos-media-europe)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/25795856](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/25795856)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="51-cz-lion-beat-capital"></a>
### 51. Lion Beat Capital (`cz-lion-beat-capital`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [lionbeatcapital.com/](https://lionbeatcapital.com/)

Nálezy AI: [nalezy_ai.md#cz-lion-beat-capital](nalezy_ai.md#cz-lion-beat-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor, ale typ family office, ne VC/CVC. Web se výslovně označuje: 'We are a single-family office founded and owned by Kateřina Havrlant' (vedle VC i PE strategie, účast ve fondech Verve a Ellipsis Ventures); fungování tomu odpovídá: ARES Lion Beat Capital, s.r.o. (IČO 22402373, vznik 23. 12. 2024, Generála Píky 430/26, Praha 6, jediná společnice a statutární orgán Kateřina Havrlant, předmět mj. správa vlastního majetku) a Lion Beat Capital Group, a.s. (IČO 29794668, vznik 16. 7. 2026, jediná akcionářka a správní rada K. Havrlant). Investice v okně 24 měsíců doložena: Vestbee 24. 6. 2025 o seed kole Filuta AI 4,2 mil. USD (velikost celého kola) 'led by Rockaway Ventures, with support from Tarpan Capital and Lion Beat Capital'; Echo24 25. 6. 2025 'dalšími pak například firmy Tarpan Capital a Lion Beat Capital' (nástroj neprima_indicie, seed). Sídlo ČR splněno, typ mimo pilot (VC strategie family office).

**Zdroje uvedené agentem:**
- [lionbeatcapital.com/](https://lionbeatcapital.com/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22402373](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/22402373)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/29794668](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/29794668)
- [vestbee.com/blog/articles/filuta-ai-secures-4-2-m](https://vestbee.com/blog/articles/filuta-ai-secures-4-2-m)
- [echo24.cz/a/HEwzp/zpravy-ekonomika-investori-veri-ai-investicni-seed-kolo-pri…](https://www.echo24.cz/a/HEwzp/zpravy-ekonomika-investori-veri-ai-investicni-seed-kolo-prineslo-startupu-filuta-ai-pres-4-miliony-dolaru)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="52-cz-qq-capital"></a>
### 52. QQ Capital (`cz-qq-capital`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [qq.capital](https://www.qq.capital)

Nálezy AI: [nalezy_ai.md#cz-qq-capital](nalezy_ai.md#cz-qq-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor, ale typ family office (mimo pilot VC/CVC). Vlastní web se výslovně označuje: „QQ Capital is a venture family office in Prague, Czech Republic, investing in early stage technological companies.“ a „As a family office, we invest private resources, so we have no LPs to report to.“ (fungování odpovídá: vlastní soukromé prostředky, bez LP; VC je investiční strategie). Investice v okně: Navigara, seed 2,5 mil. USD (velikost celého kola, ne vklad) vedené Inovo VC „with participation from Rockaway Ventures and QQ Capital“, TZ PR Newswire 2026-02-28 (nástroj neprima_indicie, kolo seed). Identita: web uvádí QQ Capital SE, Hvězdova 1716/2b, Praha 4 a tým Michal Štencl, Andrej Jančar; ARES: QQ Capital SE, IČO 08676135, sídlo Hvězdova 1716/2b, Nusle, Praha 4, předseda představenstva Michal Štencl – totožnost s investorem v kole Navigara tím potvrzena (Navigara je i v portfoliu na webu).

**Zdroje uvedené agentem:**
- [qq.capital](https://www.qq.capital)
- [prnewswire.com/news-releases/navigara-launches-the-performance-layer-for-ente…](https://www.prnewswire.com/news-releases/navigara-launches-the-performance-layer-for-enterprise-engineering-teams-and-ai-tools-backed-by-2-5m-302700136.html)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08676135](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08676135)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="53-cz-skylimit-investments"></a>
### 53. SkyLimit Investments (`cz-skylimit-investments`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [skylimit.cz/](https://www.skylimit.cz/)

Nálezy AI: [nalezy_ai.md#cz-skylimit-investments](nalezy_ai.md#cz-skylimit-investments) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor, ale typ PE, ne VC/CVC. Web: SkyLimit Industry SICAV a.s. je 'private equity fond zaměřený na investice do malých a středně velkých strojírenských společností v České republice', strategie 'odkupů majoritních podílů ve strojírenských společnostech' od roku 2016. Doložená investice v okně 24 měsíců: 'Private equity fond SkyLimit Industry SICAV ... dokončil akvizici otrokovické společnosti Prozax, s. r. o.' (TZ PROTEXT na ČTK/ceskenoviny.cz 10. 9. 2025; Seznam Zprávy 9. 9. 2025 'koupil otrokovickou společnost Prozax'); rejstřík Prozax (IČO 63469243): SkyLimit Industry SICAV a.s. (IČO 05265754) zapsána jako 100% společník od 9. 9. 2025 (od 12. 3. 2026 je 100% společníkem Ceramet s.r.o., IČO 04852389, tj. podíl už nedrží). Datum pro filtr oznámení 2025-09-09 (status by byl investice_dolozena_12_24_mesicu). Identita: SkyLimit Investments s.r.o., IČO 04711629, Vodičkova 791/41, Praha 1, společníci a jednatelé Michal Bakajsa, Jaroslav Sopuch, Ľubomír Červeňák po 1/3 (TZ jmenuje Červeňáka jako zakladatele a Bakajsu jako spoluzakladatele SkyLimitu); fond SkyLimit Industry SICAV a.s., IČO 05265754, stejná adresa, statutár AVANT investiční společnost, a.s. Sídlo CZ.

**Zdroje uvedené agentem:**
- [skylimit.cz/](https://www.skylimit.cz/)
- [ceskenoviny.cz/tiskove/zpravy/fond-skylimit-posiluje-v-oblasti-prumyslove-aut…](https://www.ceskenoviny.cz/tiskove/zpravy/fond-skylimit-posiluje-v-oblasti-prumyslove-automatizace-dokoncil-akvizici-spolecnosti-prozax/2718984)
- [seznamzpravy.cz/clanek/ekonomika-firmy-fond-skylimit-kupuje-otrokovickou-firm…](https://www.seznamzpravy.cz/clanek/ekonomika-firmy-fond-skylimit-kupuje-otrokovickou-firmu-prozax-285595)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/63469243](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/63469243)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04711629](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/04711629)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05265754](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/05265754)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="54-cz-stratum-partners"></a>
### 54. Stratum Partners (`cz-stratum-partners`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [stratum.eu/](https://www.stratum.eu/)

Nálezy AI: [nalezy_ai.md#cz-stratum-partners](nalezy_ai.md#cz-stratum-partners) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ PE, ne VC/CVC. Vlastní popis na webu: „Stratum Partners is a private equity manager focused on Central Europe.“, „We provide equity investments of € 2–10 million“, spravuje „GGEF I, a growth capital fund specialising in investments into small and medium-sized companies“ a nový fond Stratum II (červenec 2026, cíl 65 mil. EUR); tým „combines over 100 years of private equity experience“. Doložená investice v okně: CzechCrunch 4. 12. 2025: „Kupcem je investiční společnost Genesis Capital prostřednictvím svého fondu Genesis Growth Equity Fund I“ (iForo / Poptávej.cz, citován Radim Jasek, „partner Genesis Capital Growth“); web Stratum 16. 12. 2025: „GGEF I has completed the acquisition of a majority stake in iFORO Group, s.r.o. (Poptávej.cz)“ (nástroj podíl doložen); dále podle webu ELIS DESIGN (29. 4. 2026, „equity investment“), Cross Masters (13. 11. 2025, většinový podíl). Identita: ARES Stratum Partners s.r.o., IČO 07607539 (dříve Genesis Growth s.r.o. a Genesis Capital Growth s.r.o., přejmenováno 25. 6. 2026), sídlo Škrétova 490/12, Praha 2, jednatelé a společníci Jiří Beneš, Marek Hoščálek, Radim Jasek (shodní s týmem na stratum.eu/team); sídlo v ČR, rozhoduje typ PE.

**Zdroje uvedené agentem:**
- [stratum.eu/](https://www.stratum.eu/)
- [stratum.eu/team/](https://stratum.eu/team/)
- [stratum.eu/news/](https://stratum.eu/news/)
- [cc.cz/dalsi-exit-cesti-investori-prodali-byznys-se-remeslniky-aby-se-mohli-so…](https://cc.cz/dalsi-exit-cesti-investori-prodali-byznys-se-remeslniky-aby-se-mohli-soustredit-na-vetsi-projekty/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07607539](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/07607539)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="55-cz-tcf-capital"></a>
### 55. TCF Capital (`cz-tcf-capital`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [tcfcap.com/](https://www.tcfcap.com/)

Nálezy AI: [nalezy_ai.md#cz-tcf-capital](nalezy_ai.md#cz-tcf-capital) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ není VC/CVC. Investice: CzechCrunch 10. 4. 2025 – TCF Tomáše Čupra „přes svůj investiční fond TCF v Macromo získal majoritní podíl hlasovacích práv výměnou za financování dalšího“ vývoje (soukromý český startup, nástroj podíl doložen, datum v okně 24 měsíců, částka nezveřejněna); dále CzechCrunch 12. 5. 2025 „TCF Capital koupila bavorskou firmu Töpfer Babywelt“ (spolu s TPAG). Typ: web se popisuje „TCF Capital je investiční skupina Tomáše Čupra, zakladatele Rohlík Group“, název podle CzechCrunch 27. 6. 2023 skrývá „Tomáš Čupr Family“, investuje převážně vlastní kapitál Čupra (externí zdroje případně „zhruba pětinu aktiv“), hlavní aktivum je podíl v Rohlik Group, strategie „Cílíme na majoritu nebo na silnou governance pozici“ a oblast „Business turnarounds“ – investiční holding jednoho podnikatele (Velký soukromý investor), ne VC fond se svěřeným kapitálem; family office se výslovně neoznačuje. Identita: provozovatel webu TCF-Cap Services s.r.o., IČO 09000909, Na příkopě 392/9, Praha 1 (zásady na webu, ARES), jediný společník Bizthusiasm, a.s. (IČO 03307611, člen představenstva Tomáš Čupr, stejná adresa); který subjekt drží podíly, nepotvrzeno. Sídlo ČR. Pilulka (úvěr až 80 mil. Kč s opcí, 2024, veřejně obchodovaná) jako doklad nepoužita.

**Zdroje uvedené agentem:**
- [cc.cz/tomas-cupr-slape-do-longevity-investuje-do-ceskeho-startupu-ktery-hlida…](https://cc.cz/tomas-cupr-slape-do-longevity-investuje-do-ceskeho-startupu-ktery-hlida-zdravi/)
- [cc.cz/tomas-cupr-vyrazil-na-nakupy-do-nemecka-k-pilulce-a-spol-pridava-vyrobc…](https://cc.cz/tomas-cupr-vyrazil-na-nakupy-do-nemecka-k-pilulce-a-spol-pridava-vyrobce-kojenecke-vyzivy/)
- [tcfcap.com/](https://www.tcfcap.com/)
- [tcfcap.com/about/about-a](https://www.tcfcap.com/about/about-a)
- [cc.cz/tomas-cupr-spousti-investicni-skupinu-jeji-hodnota-diky-rohliku-prekrac…](https://cc.cz/tomas-cupr-spousti-investicni-skupinu-jeji-hodnota-diky-rohliku-prekracuje-17-miliard-a-ma-rychle-rust/)
- [tcfcap.com/legal](https://www.tcfcap.com/legal)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09000909](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09000909)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03307611](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03307611)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="56-cz-thein"></a>
### 56. Thein (`cz-thein`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [thein.eu/](https://www.thein.eu/)

Nálezy AI: [nalezy_ai.md#cz-thein](nalezy_ai.md#cz-thein) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ PE, ne VC/CVC. Profil CVCA: „Type of Investment LBO, Growth capital“, „Preferred Ammount of Investment EUR 1-5 million in equity“, „Volume of Funds Managed EUR 40 million“, portfolio zavedených průmyslových a IT firem (TOP ALULIT, PONEC, COTRING, Aitcom…); skupina kupuje celé firmy (M-COM: „stoprocentní podíl“, Lupa 9. 10. 2024 – těsně před oknem). Nejnovější nalezená investice v okně: akvizice CubeTeam s.r.o. sekcí Thein Digital (Lupa.cz 6. 1. 2025: „Sekce Thein Digital získala menší českou firmu CubeTeam“; RMOL 8. 1. 2025, zdroj Thein Digital) → investice_dolozena_12_24_mesicu, nástroj podíl (akvizice). Subjekt: Thein Investments a.s., IČO 08839042, akcionář a předseda správní rady Tomáš Budník (ARES; dříve sídlo Pikrtova 1737/1a shodné s adresou v CVCA), fond Thein Private Equity SICAV a.s. IČO 11733861; sídlo ČR. Vadí jen typ.

**Zdroje uvedené agentem:**
- [cvca.cz/en/thein-2/](https://cvca.cz/en/thein-2/)
- [lupa.cz/aktuality/budnik-a-j-t-pokracuji-ve-skupovani-trhu-thein-ziskal-dalsi…](https://www.lupa.cz/aktuality/budnik-a-j-t-pokracuji-ve-skupovani-trhu-thein-ziskal-dalsi-it-firmu/)
- [rmol.cz/novinky/investicni-skupina-thein-ziskava-spolecnost-cubeteam-speciali…](https://www.rmol.cz/novinky/investicni-skupina-thein-ziskava-spolecnost-cubeteam-specializujici-se-na-zakazkovy-vyvoj-aplikaci)
- [lupa.cz/aktuality/budnik-a-j-t-kupuji-dalsi-ceskou-it-firmu-thein-diky-m-comu…](https://www.lupa.cz/aktuality/budnik-a-j-t-kupuji-dalsi-ceskou-it-firmu-thein-diky-m-comu-posili-v-kyberbezpecnosti/)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08839042](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/08839042)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/11733861](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/11733861)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`

<a id="57-cz-versute-investments"></a>
### 57. Versute Investments (`cz-versute-investments`)

Soubor: `vyrazeni.csv` · rozhodnutí agenta: **vyřazen, kategorie `mimo_rozsah_pilotu`** · web [versute.cz/](https://www.versute.cz/)

Nálezy AI: [nalezy_ai.md#cz-versute-investments](nalezy_ai.md#cz-versute-investments) (číst až po commitu prvních verdiktů)

**Důvod agenta (celý):**

> Skutečný investor podle bodů 2 a 3, ale typ PE, ne VC/CVC. Vlastní popis: „Jsme investiční a poradenskou společností působící jako manažer Private Equity fondů investujících zejména do malých a středních podniků“; CVCA: „Type of Investment Growth capital, Leveraged buyouts, Management buyouts“, ticket „EUR 1 mio – 5 mio (amount of invested equity)“. Investice v okně: BHS Private Equity Fund (spravovaný Versute Investments a.s.) koupil „significant minority stake in ALFA 3, s.r.o.“ (Forbes 4. 8. 2025 podle webu Versute; Schoenherr a ECOVIS 26. 11. 2025) a polovinu Unipap spolu s MAM Private Equity Fund (Deloitte M&A Port 24. 9. 2025: „The company will be split evenly between BHS Private Equity Fund and MAM Private Equity Fund“) → investice_dolozena_12_24_mesicu, nástroj podíl. Subjekt: VERSUTE INVESTMENTS a.s., IČO 03965953, Vodičkova 709/33, Praha 1, správní rada Luděk Palata (ARES); fondy VERSUTE Funds SICAV a.s. (IČO 03846784, dříve BHS Fund II) pod Versute investiční společnost, a.s. (IČO 08787131). Sídlo ČR, vadí jen typ.

**Zdroje uvedené agentem:**
- [versute.cz/](https://www.versute.cz/)
- [cvca.cz/en/versute-investments-2/](https://cvca.cz/en/versute-investments-2/)
- [schoenherr.eu/content/czech-republic-schoenherr-advises-bhs-private-equity-fu…](https://schoenherr.eu/content/czech-republic-schoenherr-advises-bhs-private-equity-fund-on-acquisition-of-alfa-3)
- [ecovis.com/cee/ecovis-corporate-finance-cz-advises-on-minority-stake-sale/](https://www.ecovis.com/cee/ecovis-corporate-finance-cz-advises-on-minority-stake-sale/)
- [deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zab…](https://www.deloitte.com/cz-sk/en/mnaport/articles/clanky-transakce/2025-q3/dva-fondy-zabalily-unipap.html)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03965953](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03965953)
- [ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03846784](https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/03846784)

- **`je_investor`**: Je kandidát investor podle pravidel z bodu 2 a 3.
- **`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR).
- **`kategorie`**: Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`). Agent: `mimo_rozsah_pilotu`.
- **`duvod`**: Sedí důvod vyřazení, který agent uvedl.

Řádky v `hodnoceni.csv`: `je_investor`, `rozsah_pilotu`, `kategorie`, `duvod`
