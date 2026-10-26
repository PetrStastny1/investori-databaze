#!/usr/bin/env python3
"""Krok 6 (příprava): podklady pro ruční kontrolu.

Vytvoří ve stejném pořadí kandidátů:
- ai-log/05-rucni-kontrola/pruvodce.md (hodnoty agenta a zdroje, bez nálezů AI),
- ai-log/05-rucni-kontrola/nalezy_ai.md (nálezy kontroly zdrojů, fáze A a B),
- data/hodnoceni.csv (předvyplněné řádky bez verdiktů).

Čte jen původní výstup agenta a výsledky kroku 4, nic z nich nemění.
Spuštění z kořene repozitáře: python3 ai-log/05-rucni-kontrola/skripty/priprav_podklady.py
"""

import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[3]
VYSTUP = ROOT / "data" / "vystup_agenta"
CIL = ROOT / "ai-log" / "05-rucni-kontrola"
SLEPA = ROOT / "ai-log" / "04-kontrola-zdroju" / "slepa_kontrola.csv"
MAPOVANI = ROOT / "ai-log" / "02-obohaceni" / "mapovani_id.csv"
KANDIDATI = ROOT / "data" / "kandidati.csv"
HODNOCENI = ROOT / "data" / "hodnoceni.csv"

HODNOTIL = "Petr Šťastný"
OKNO_24 = "2024-10-26"
OKNO_12 = "2025-10-26"
HLAVICKA = ["soubor", "id", "pole", "hodnoceni", "pricina_chyby", "poznamka", "hodnotil", "datum"]

# Pořadí kontroly podle zadání. Skupina 4 je seřazená podle závažnosti nálezů kontroly
# zdrojů: nejdřív nález, který může změnit kategorii, pak potvrzené rozpory v polích,
# podezření, nedostatečné důkazy a drobnosti, nakonec kandidáti bez nálezu
# (zařazení před vyřazenými).
SKUPINY = [
    ("Příslušnost k pilotu", [
        "cz-n1-ventures", "cz-nation1", "cz-tensor-ventures", "cz-kaya-vc",
        "cz-ii-biotech-investments", "cz-zaka-vc", "cz-startupyard", "cz-ii-prague",
    ]),
    ("Možná chybná vyřazení", [
        "cz-orbit-capital", "cz-mcwin-partners", "cz-espira-investments",
    ]),
    ("Nevyřešení", [
        "cz-rockawayx", "cz-lumus-investments", "cz-chilli-ventures", "cz-fond-nase-cesko",
        "cz-moonhill-capital", "cz-botanique-hospitality", "cz-braiins", "cz-gi21-capital",
        "cz-jet-investment", "cz-kkcg", "cz-tarpan-capital",
    ]),
    ("Ostatní", [
        "cz-garage-angels",
        "cz-look-ai-ventures", "cz-jic-ventures", "cz-purple-ventures", "cz-reflex-capital",
        "cz-soulmates-ventures",
        "cz-y-soft-ventures", "cz-lighthouse-ventures", "cz-czech-founders-vc",
        "cz-depo-ventures", "cz-inven-capital", "cz-credo-ventures", "cz-cs-seed-starter",
        "cz-jt-ventures", "cz-rockaway-ventures",
        "cz-borovicka-capital", "cz-fazole-ventures", "cz-miton", "cz-presto-ventures",
        "cz-purposetech", "cz-tilia-impact-ventures",
        "cz-arx-equity-partners", "cz-mam-private-equity-fund", "cz-everita-capital",
        "cz-bd-partners", "cz-central-europe-industry-partners", "cz-emma-capital",
        "cz-genesis-capital", "cz-lion-beat-capital", "cz-qq-capital",
        "cz-skylimit-investments", "cz-stratum-partners", "cz-tcf-capital", "cz-thein",
        "cz-versute-investments",
    ]),
]

# Pole a otázky podle PLAN.md bod 6.
POLE_ZARAZENI = [
    ("existence", "Subjekt existuje (rejstřík nebo regulátor)"),
    ("investicni_cinnost", "Investiční činnost je doložená zprávou o transakci v okně 24 měsíců"),
    ("je_investor", "Je to investor podle pravidel z bodu 2 a 3"),
    ("typ", "Typ je zařazen správně"),
    ("rozsah_pilotu", "Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)"),
    ("posledni_investice", "Poslední investice sedí (firma, datum investice nebo oznámení podle "
                           "zprávy o transakci, `datum_pro_filtr`)"),
    ("nezavislost_zdroju", "Zdroje uvedené jako nezávislé mají opravdu různý původ"),
    ("sektory", "Sektory odpovídají zdroji"),
    ("ticket", "Ticket odpovídá zdroji"),
    ("kapital", "Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)"),
]
POLE_VYRAZENI = [
    ("je_investor", "Je kandidát investor podle pravidel z bodu 2 a 3"),
    ("rozsah_pilotu", "Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)"),
    ("kategorie", "Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`)"),
    ("duvod", "Sedí důvod vyřazení, který agent uvedl"),
]
POLE_NEVYRESENE = [
    ("je_investor", "Je kandidát investor podle pravidel z bodu 2 a 3 (zároveň moje rozhodnutí)"),
    ("rozsah_pilotu", "Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) (zároveň moje rozhodnutí)"),
    ("duvod", "Agent správně popsal, co chybí nebo si odporuje"),
]
POLE_SLOUCENI = [
    ("slouceni", "Nation1 a N1 Ventures jsou jedna investiční firma a sloučení podle PLAN.md "
                 "bod 3 („jedna investiční firma = jeden záznam“) je správné"),
]

# Nálezy fáze B (cilene_otazky.md) a omezení kontroly podle id. Třídy:
# rozpor = potvrzený rozpor, podezreni, nedostatecny = nedostatečný důkaz,
# jine = otázka výkladu PLAN.md nebo jiné upřesnění (není nález v datech),
# omezeni = co druhý agent nemohl ověřit (fáze A to vedla v řádcích se závěrem sedi).
# Položka: (třída, pole, původ, text).
NALEZY_B = {
    "cz-n1-ventures": [
        ("podezreni", "posledni_investice / dalsi_investice (Liki24)", "fáze B, nový nález",
         "Podmínku 3 u N1 nese jediná investice, Liki24 (Series A, Forbes UA 3. 7. 2025: „Раунд "
         "підтримали … N1 Ventures“). Web N1 ji vede pod „U-Tech is an independent fund built by N1“. "
         "Zda investici fondu U-Tech připsat N1, zdroje nerozhodují: PLAN.md bod 3 vede fondy pod jedním "
         "správcem jako podřízené údaje, „independent fund“ to zpochybňuje."),
        ("nedostatecny", "pravni_subjekt / sidlo", "fáze B, souhlas s fází A",
         "Správci Nation 1 GP S.à r.l. a Nation 1 GP II S.à r.l. i fondy jsou podle n1.rocks/disclosure "
         "lucemburské. Česká právnická osoba nenalezena (uložené odpovědi ARES pro „N1 Ventures“ a "
         "„Nation1“). Zápis GP v RCS nebo u CSSF nikdo neotevřel, jde jen o vlastní tvrzení webu."),
        ("jine", "rozsah_pilotu", "fáze B",
         "Výsledek závisí na výkladu pravidla „investiční firma (správce, značka) má sídlo v ČR“: podle "
         "značky a týmu CZ, podle sídla správce mimo ČR. Viz Otázky výkladu PLAN.md, bod 1."),
    ],
    "cz-tensor-ventures": [
        ("podezreni", "sidlo", "fáze B, souhlas s fází A",
         "tensor.ventures/legal-disclosures: „Tensor Ventures GP S.à r.l (the “GP”), as general partner "
         "and registered AIFM of Tensor Ventures Fund I“. Česká Tensor Ventures a.s. (IČO 06257241) má "
         "v rejstříku „správa vlastního majetku“, její roli vůči fondu zdroje nedokládají. Správce druhého "
         "(koinvestičního) fondu nedoložen, článek CzechCrunch citovaný agentem druhý agent nečetl."),
        ("podezreni", "nezavislost_zdroju (ValkaAI)", "fáze B, upřesnění fáze A (jistota sedi)",
         "Seznam Zprávy i Startbase mají `puvod` null, ačkoli Seznam píše „Firma zároveň uvádí“ a "
         "Startbase má foto „(c) ValkaAI“. Poznámka agenta sama uvádí, že „nejspíš vycházejí z informací "
         "firmy“. Jistotu `stredni` to nemění."),
        ("jine", "rozsah_pilotu", "fáze B",
         "Výsledek závisí na výkladu pravidla o sídle (správce, nebo značka a tým). Viz Otázky výkladu "
         "PLAN.md, bod 1."),
    ],
    "cz-kaya-vc": [
        ("rozpor", "kapital[2]", "fáze B, oprava fáze A (sedi → nedostatecny_dukaz)",
         "Položka má `druh` = `committed_capital` a vyplněný `fond` = „pátý fond (po first closingu)“. "
         "PLAN.md bod 4: „`fond` je název fondu u `fund_size`, jinak `null`“. Rozpor s pravidlem je "
         "doslovný, fáze B ho podle zadání kontroly zapsala jako nedostatecny_dukaz. Částka 70 000 000 EUR, "
         "měna, druh a datum (CzechCrunch 25. 6. 2025) sedí. Zda jde o chybu dat, nebo o příliš přísné "
         "pravidlo, nechala fáze B na uživateli."),
        ("podezreni", "sidlo", "fáze B, oprava fáze A (sedi → podezreni)",
         "kaya.vc/sustainability: „KAYA VC GP S.à r.l (the “General Partner” or “KAYA”), which is "
         "registered as a Luxembourg AIFM“. Česká Kaya F3 GP s.r.o. (IČO 19844166) je podle názvu GP "
         "jednoho fondu, kterého, zdroje neříkají. První agent lucemburského AIFM nezmínil a CZ zdůvodnil "
         "„podle rejstříku GP v Praze“. Fáze A stránku /sustainability nečetla. Kanceláře: Varšava, "
         "Praha, San Francisco, Londýn."),
        ("jine", "rozsah_pilotu", "fáze B",
         "Výsledek závisí na výkladu pravidla o sídle. Viz Otázky výkladu PLAN.md, bod 1."),
        ("jine", "kapital[1], kapital[2]", "fáze B",
         "„$85M Current Fund“ a „70 mil. EUR pátý fond po first closingu“ jsou pravděpodobně týž fond "
         "v jiné fázi a měně. Agent je nesčítá, což odpovídá PLAN.md. `fond` u kapital[1] je popis, "
         "ne název."),
    ],
    "cz-ii-biotech-investments": [
        ("podezreni", "sidlo", "fáze B, souhlas s fází A",
         "Citace „i&i Bio is a Luxembourg-based venture capital firm“ ověřena (text pod novinkami, ne na "
         "hlavní stránce). Fond i&i Biotech Fund I SCSp sídlí v Lucembursku, česká Biotech Investments "
         "s.r.o. je „Investment Adviser“. Agent lucemburský fond uvedl, ale bez označení „k ruční "
         "kontrole“ a bez vlastního popisu značky."),
        ("nedostatecny", "sidlo", "fáze B",
         "Kdo je správce (GP/AIFM) fondu i&i Biotech Fund I SCSp (RCS B 252970), web ani SFDR stránka "
         "neuvádějí a nikdo to neověřil."),
        ("podezreni", "nezavislost_zdroju (Theorema)", "fáze B",
         "Tři zprávy o Theoremě (Lupa, CzechCrunch, Vestbee) mají `puvod` null, podle bodu 6 by tedy "
         "formálně šlo o tři původy. Lupa ale píše „Startup Theorema … oznámil“, Vestbee má stejný výčet "
         "investorů a CzechCrunch vyšel týž den, spíš jde o jeden původ (oznámení startupu). Poznámka "
         "agenta sama uvádí, že nezávislost doložená není. Jistota `stredni` je povinná už proto, že žádná "
         "investice nemá `nastroj.doklad` = `dolozeno` (fáze A ji nazvala „konzervativně správnou“, "
         "fáze B zdůvodnění opravila)."),
        ("podezreni", "nezavislost_zdroju (Ternary, Antiverse)", "fáze B",
         "`puvod` null je sporný u IT Brief (Ternary, „Ternary says…“) a u Vestbee (Antiverse, „as "
         "Vestbee was informed“). Obě jsou jediným zdrojem dané investice, na jistotu bez vlivu."),
        ("jine", "kapital[0]", "fáze B",
         "„approximately €47 million“ (30. 11. 2022) je uloženo jako přesné číslo, přibližnost je jen "
         "v poznámce. Na téže stránce je novější nedatovaný údaj „manages over €53 million“, nezapsán. "
         "Hranici mezi `fund_size` a `committed_capital` PLAN.md nedefinuje."),
        ("jine", "rozsah_pilotu", "fáze B",
         "Výsledek závisí na výkladu pravidla o sídle. Viz Otázky výkladu PLAN.md, bod 1."),
    ],
    "cz-zaka-vc": [
        ("podezreni", "pravni_subjekt", "fáze B, souhlas s fází A",
         "Provozovatelem webu je podle zaka.vc/privacy-policy fond ZAKA VC I, osoba rizikového kapitálu, "
         "a.s. (IČO 21514992), ne ZAKA Management s.r.o., kterou agent uvádí jako „správce značky“. "
         "Sídlo je CZ v obou výkladech pravidla o sídle."),
    ],
    "cz-startupyard": [
        ("podezreni", "je_investor (Ydoca)", "fáze B",
         "Podmínku 3 nese jediná investice, Ydoca (CzechCrunch: pre-seed, StartupYard 500 tis. Kč). "
         "Fáze A u typu uvádí, že není jasné, zda šlo o vlastní peníze StartupYardu, nebo syndikátu "
         "andělů. `puvod` null u zprávy CzechCrunch nelze vyvrátit. Web (Batch 15) nabízí „simple "
         "convertible note“, což je přípustný nástroj."),
    ],
    "cz-ii-prague": [
        ("nedostatecny", "je_investor (vztah k cz-ii-biotech-investments)", "fáze B",
         "i&i Prague je zakladatelem a „main sponsor“ fondu i&i Biotech Fund I SCSp a zároveň investuje "
         "přímo: rejstřík CasInvent Pharma ukazuje úpis akcií i&i Prague v letech 2023 a 2025 a akcionáře "
         "při založení 2020. Kolo CasInvent 2025 fond i&i Biotech neupisoval, investice tedy patří i&i "
         "Prague (to rozhodnutí agenta podporuje). Kdo je GP fondu (RCS B 252970), nikdo neověřil. Kdyby "
         "to byla entita skupiny IOCB Tech / i&i Prague, mohl by se změnit výklad „jedna investiční firma“."),
        ("nedostatecny", "typ", "fáze B",
         "Část portfolia (12 firem) může pocházet ze zakládání spin-offů (venture builder, vklad "
         "know-how), ne z peněžní investice. Zdroje to nerozlišují."),
        ("jine", "je_investor, typ", "fáze B",
         "PLAN.md neřeší subjekt, který je zároveň sponzorem fondu a přímým investorem. Výluku „čistý LP“ "
         "i&i Prague nesplňuje. Pravidlo o akcelerátoru s vlastním kapitálem (typ VC) je na inkubátor "
         "použité výkladem. CVC sedí jen volně (vlastníkem je IOCB Tech, firma ÚOCHB AV ČR)."),
    ],
    "cz-orbit-capital": [
        ("nedostatecny", "kategorie (Sloneek)", "fáze B, nový nález",
         "Caplight („Sloneek Jun 2026 Series A Lead“) a Seedtable vedou Orbit jako lead série A "
         "Sloneeku. Primární zprávu se zněním nástroje druhý agent nenašel (parsers.vc za registrací, "
         "Seedtable HTTP 403). Dluh u Sloneeku dokládá jen to, že ho tech.eu řadí mezi investice Growth "
         "Debt Fund II. Kdyby šlo o podíl, Orbit by splnil body 2 a 3."),
        ("nedostatecny", "kategorie (IAG)", "fáze B",
         "IAG zmiňuje jen článek o fondu, samostatnou zprávu o transakci druhý agent nenašel. Nástroj ani "
         "datum nejsou doložené konkrétní zprávou."),
        ("jine", "kategorie", "fáze B",
         "Orbit má strategii Growth Equity i Growth Debt a v okně doložil jen dluh (Coding Giants, Jutro "
         "Medical výslovně). PLAN.md neříká, zda takový subjekt patří do hranicni.csv (`venture_debt`), "
         "nebo do vyrazeni.csv jako `neni_investor`. nevyresene.csv formálně nesedí, je jen pro typ a "
         "nástroj."),
    ],
    "cz-mcwin-partners": [
        ("podezreni", "kategorie", "fáze B, oprava fáze A (sedi → sedí formálně, oddělení sporné)",
         "McWin Partners s.r.o. (family office zakladatelů) a McWin Capital Partners (Londýn) mají stejné "
         "zakladatele a společnou značku, mcwin.cz odkazuje na mcwin.fund a portfolio na mcwin.cz se "
         "překrývá s fondy McWin (EasyMile, Exergyn, Vapiano, dean&david, EVERY). Proti: jiný právní "
         "subjekt, jiná role a mcwin.fund/our-team uvádí „McWin Partners Family Office“ jako samostatný "
         "subjekt. Pokud jde o jednu investiční firmu, existuje transakce v okně (Goodwin 14. 10. 2025, "
         "Ecorobotix Series D přes McWin Food Tech Fund) a kategorie by byla `mimo_rozsah_pilotu` (sídlo "
         "Londýn), ne `neni_investor`. Do pilotu se McWin nedostane v žádné variantě."),
        ("podezreni", "duvod", "fáze B",
         "Důvod je věcně přesný, ale nezmiňuje překryv portfolia a značky, který je pro rozhodnutí "
         "o duplicitě podstatný. Agent rozhodnutí neoznačil jako sporné."),
        ("jine", "kategorie", "fáze B",
         "PLAN.md řadí „bez doložené investice v okně“ do `neni_investor`, i když subjekt jinak investuje "
         "(bod 2: status popisuje jen veřejnou stopu). Vztah family office zakladatelů a jejich správce "
         "fondů PLAN.md neřeší."),
    ],
    "cz-espira-investments": [
        ("podezreni", "duvod", "fáze B, upřesnění fáze A (sedi s drobnou výhradou)",
         "„jiný fond a tým“ je zkratka: Mamajová je společnicí ESPIRA Investments s.r.o. (ARES 05528089) "
         "i EVERITA Capital s.r.o. (ARES 19067097). Fáze B to nepovažuje za věcnou chybu, závěr se nemění."),
        ("nedostatecny", "kategorie", "fáze B",
         "Investici v okně nenašla ani fáze B (web, vyhledávání, funding.tech.eu). Sbírku listin "
         "(výroční zprávy ESPIRA Investments s.r.o., IČO 05528089) nikdo neprošel. Nejnovější vstup "
         "8. 2. 2022 (Premier Clinic), exit 27. 7. 2022 (ICON)."),
        ("jine", "kategorie", "fáze B",
         "`neni_investor` je podle PLAN.md formálně správně (bez investice v okně), Espira ale v letech "
         "2018–2022 doloženě investovala. Zda brát EVERITA Capital (nová firma spoluzakladatelky na stejné "
         "adrese) jako nástupce, PLAN.md neřeší. Zdroje dokládají dvě různé firmy. V obou variantách je "
         "subjekt mimo pilot (typ PE)."),
    ],
    "cz-rockawayx": [],
    "cz-lumus-investments": [
        ("jine", "duvod, otazka", "fáze B",
         "Garage Angels (vyrazeni.csv, `mimo_rozsah_pilotu`) má podle fáze B stejnou strukturu (klub "
         "andělů, organizátor zakládá SPV pro každý deal) a stejnou otázku typu, kterou agent u LUMUS "
         "nechal nevyřešenou. U LUMUS k tomu přistupuje nezjištěný nástroj (Lumus ani jeho SPV nejsou "
         "mezi společníky Kardi AI), který by ho do nevyresene.csv poslal i sám. Viz cz-garage-angels."),
    ],
    "cz-chilli-ventures": [
        ("omezeni", "duvod", "fáze A",
         "CzechCrunch 2. 6. 2025 a PitchBook jsou v důvodu zmíněné bez URL, druhý agent je neověřil."),
    ],
    "cz-fond-nase-cesko": [
        ("omezeni", "duvod", "fáze A", "Údaj nordic9 („Bank“) je v důvodu bez URL, neověřeno."),
    ],
    "cz-moonhill-capital": [
        ("omezeni", "duvod", "fáze A",
         "Článek EU-Startups (Ekiden) vrátil HTTP 403. Fakta druhý agent ověřil z převzetí v Portugal "
         "Startup News."),
    ],
    "cz-garage-angels": [
        ("podezreni", "kategorie", "fáze B, oprava fáze A (sedi → podezreni)",
         "Fáze A zvážila jen alternativu VC/CVC. Podle fáze B je právním držitelem podílu SPV (GA "
         "Investiční VRV, CSI, GCOM, KAI), kterou Garage Angels Management s.r.o. založí, drží v době "
         "úpisu a pak převede na jednotlivé anděly (ARES: VRV ve vlastnictví Managementu do 2. 6. 2026, "
         "CSI do 19. 7. 2025). Tisková zpráva CasInvent (khanu.de): „independent investors from the "
         "Garage Angels network“, „an informal group of about 15 independent individual investors“. "
         "Předmět podnikání Management s.r.o.: „zprostředkování obchodu a služeb“. Pokud je klub "
         "organizátor investic jednotlivých andělů, kategorie by byla `neni_investor`, pokud investor, "
         "`mimo_rozsah_pilotu`. PLAN.md definuje Angel jako fyzickou osobu a typ pro klub nemá."),
        ("podezreni", "kategorie (konzistence s LUMUS)", "fáze B",
         "Strukturně obdobný LUMUS agent poslal do nevyresene.csv s otázkou typu, Garage Angels rozhodl "
         "sám. Viz cz-lumus-investments."),
        ("jine", "duvod", "fáze A i B (řádek se závěrem sedi)",
         "K. Obluk je společníkem GA Investiční GCOM, ne VRV. Důvod uvádí společníky souhrnně za obě SPV, "
         "fáze A to proto vedla jako drobnou nepřesnost se závěrem sedi."),
        ("omezeni", "web (nehodnotí se)", "fáze B",
         "Sloupec `web` je prázdný, ačkoli tiskové zprávy CasInvent uvádějí www.g-angels.cz. Web se "
         "druhému agentovi nepodařilo stáhnout (HTTP 301)."),
    ],
    "cz-look-ai-ventures": [
        ("podezreni", "nezavislost_zdroju (Lucida AI)", "fáze B",
         "tech.eu a Lupa mají `puvod` null, poznámka agenta přitom píše „pravděpodobně společný "
         "podklad“. Lupa má navíc citaci partnera Look AI, původ tedy ze stránek určit nelze. Na jistotu "
         "bez vlivu (strop `stredni`)."),
        ("jine", "je_investor (Digicust)", "fáze B",
         "Smíšené kolo (vklady investorů, garance aws „Equity Leverage“, konverze FlexCo). O nástroji "
         "Look AI („the Look.AI Fund is contributing €250,000“) zdroj nic neříká. Bod 4 chce v takovém "
         "případě rozhodovat podle účasti konkrétního investora."),
    ],
    "cz-purple-ventures": [
        ("nedostatecny", "nezavislost_zdroju (Comparables.ai)", "fáze B",
         "Původ zpráv tech.eu a Lupa (obě `puvod` null) nelze ze stránek určit. Lupa má údaj 10 mil. Kč "
         "a citaci Jana Staňka, které tech.eu nemá. Podmínku 3 nese jen Comparables.ai (Vetstor a "
         "Talentiqa mají `nezjisteno`)."),
    ],
    "cz-reflex-capital": [
        ("jine", "kapital[0]", "fáze B",
         "„upsali dvaadvacet“ je zapsané jako `fund_size` s fondem, obdobná formulace u Czech Founders VC "
         "jako `committed_capital`. PLAN.md hranici nedefinuje. `fond` obsahuje popis („třetí fond Reflex "
         "Capital (název ve zdroji neuveden)“), ne název."),
    ],
    "cz-soulmates-ventures": [
        ("rozpor", "posledni_investice / nastroj (Rightcharge 2026)", "fáze B, zpřesnění fáze A",
         "„Seed“ je jen v titulku UKTN. Text tiskové zprávy: „has raised a £500,000 growth funding round "
         "from existing investors“, CEO: „since our seed round“. Kolo seed tedy zdroj nedokládá, text mu "
         "odporuje. Investice by měla mít `kolo` null a `doklad` `nezjisteno`. Podmínku 3 nesou Rightcharge "
         "2025 (seed) a Antiverse (Series A)."),
        ("rozpor", "nezavislost_zdroju (Rightcharge 2025)", "fáze B, oprava fáze A („spíš nepřesný“ → chybný)",
         "Stránka UKTN je tisková zpráva (datelina „LONDON, United Kingdom (October 23, 2025)“, UKTN „we "
         "publish press releases“). `puvod` má být TZ Rightcharge, ne null. Na jistotu bez vlivu."),
        ("podezreni", "nezavislost_zdroju (Antiverse)", "fáze B",
         "Tech Funding News má `puvod` null. Má vlastní rozhovor, ale citace Sikyty je doslova shodná "
         "s Vestbee („as Vestbee was informed“)."),
        ("nedostatecny", "kapital[1]", "fáze B",
         "50 mil. EUR: Vestbee „has raised“, web „has launched“. Zda jde o upsanou, nebo cílovou velikost, "
         "zdroje neříkají. AUM 62 mil. EUR může být týž fond po navýšení (LinkedIn citovaný v poznámce "
         "nikdo nečetl)."),
    ],
    "cz-y-soft-ventures": [
        ("podezreni", "nezavislost_zdroju / jistota", "fáze B, upřesnění fáze A",
         "CzechCrunch 11. 9. 2025 („Letos již hlásili první, tzv. pre-seed, investici…“) odkazuje na "
         "dřívější oznámení. The Recycler je zpráva o změně vedení podle sdělení Y Soft a investici "
         "zmiňuje jednou větou bez kola, data a částky. `puvod` null tedy neodpovídá u dvou ze tří zpráv. "
         "U EIT Jumpstarter (zpráva programu EIT, spoluinvestora) je null obhajitelný. PLAN.md neříká, "
         "jaký minimální obsah musí zpráva o transakci mít, proto podle fáze B může být obhajitelná "
         "`stredni` i `vysoka`."),
    ],
    "cz-lighthouse-ventures": [
        ("podezreni", "dalsi_investice / nastroj (Merchantee)", "fáze B, oprava fáze A (sedi → sedí s výhradou)",
         "Nordic9 (`zdroj_url`) označuje kolo „pre-seed“, CzechCrunch 9. 6. 2026 (zdroj u Czech Founders "
         "VC) „rozšíření … seed investičního kola“ a „bridge round“, Raising.fi „undisclosed funding "
         "round“. Lighthouse má `datum_oznameni` 2026-06-03 (Nordic9), Czech Founders VC 2026-06-09. "
         "Podmínku 3 to nemění (Ranketta)."),
        ("nedostatecny", "dalsi_investice (Merchantee)", "fáze B",
         "Nordic9 působí jako databáze transakcí bez odkazu na původní zprávu, bod 2 u databáze odkaz "
         "vyžaduje. Raising.fi je obecný redakční text. Pro zařazení nerozhoduje (Ranketta, Hermetiq)."),
    ],
    "cz-czech-founders-vc": [
        ("podezreni", "posledni_investice (Merchantee)", "fáze B",
         "Totéž kolo Merchantee vedou dva záznamy různě: tento jako seed (CzechCrunch: prodloužení seed "
         "kola, „něco jako bridge round“), Lighthouse jako pre-seed (Nordic9). U bridge kola zdroj "
         "nástroj neuvádí a dluh nezmiňuje."),
        ("podezreni", "nezavislost_zdroju (Merchantee)", "fáze B",
         "`puvod` null, ačkoli CzechCrunch píše „Merchantee oznámilo“. Jediná zpráva o transakci, na "
         "jistotu bez vlivu."),
        ("jine", "kapital[0]", "fáze B",
         "10 mil. EUR (CzechCrunch 7. 9. 2022) jako `committed_capital` bez fondu. Czech Founders VC je "
         "sám fond, obdobný údaj u Reflexu je `fund_size`. Údaj je čtyři roky starý, PLAN.md stáří "
         "kapitálu neomezuje."),
    ],
    "cz-depo-ventures": [
        ("podezreni", "nezavislost_zdroju (Tapaya)", "fáze B, nový nález (fáze A puvod neposuzovala)",
         "Vestbee má `puvod` null, ale píše „Vestbee was told“ a citace Willa Ordea je doslova shodná "
         "s TZ na webu DEPO. Na jistotu bez vlivu."),
        ("nedostatecny", "rozsah_pilotu (sídlo)", "fáze B",
         "Sídlo je CZ v obou výkladech (DEPO VENTURES, s.r.o. je statutárem fondu AF III). Nový Ukraine "
         "Fund spravuje DEPO Ventures One SCSp. Že jeho správcem je lucemburská DEPO Ventures Sàrl, je "
         "jen z výtahu vyhledávače (businessinfo.cz vrátil HTTP 403)."),
    ],
    "cz-inven-capital": [
        ("podezreni", "je_investor (Andercore)", "fáze B",
         "Smíšené kolo „Series B round comprising equity and debt“. Dluh TZ nepřímo připisuje Commerzbank "
         "a KfW, nástroj Inven výslovně neuvádí. Podmínku 3 nese i Wint (Series D, bez zmínky o dluhu)."),
        ("jine", "kapital[0]", "fáze B",
         "„over EUR 500 million“ (TZ ČEZ 8. 2. 2023) je uloženo jako přesných 500 000 000, dolní mez je "
         "jen v poznámce. Zdroj sám zaměňuje AUM a fund size."),
    ],
    "cz-credo-ventures": [
        ("podezreni", "nezavislost_zdroju (Supernova)", "fáze B",
         "Tech.eu má `puvod` null, text s citací CEO vypadá na převzatou TZ. Jediná zpráva, na jistotu "
         "bez vlivu."),
    ],
    "cz-cs-seed-starter": [
        ("podezreni", "nezavislost_zdroju (Definic)", "fáze B",
         "CzechCrunch má `puvod` null, citace Miloty a Sovy jsou ve stylu TZ. Jediná zpráva, na jistotu "
         "bez vlivu."),
    ],
    "cz-jt-ventures": [
        ("podezreni", "nezavislost_zdroju (Choice)", "fáze B",
         "Tech.eu má `puvod` null, text obsahuje citaci CEO. Jediná zpráva, na jistotu bez vlivu."),
        ("jine", "kapital[0]", "fáze B, oprava vysvětlení fáze A (závěr sedi beze změny)",
         "„€120M / Výše aktiv“ (web, © 2024) je bez data, `plati_k` null. Fáze A tvrdila, že poznámka "
         "uvádí nejistotu data i druhu. Poznámka uvádí jen nejistotu data."),
    ],
    "cz-rockaway-ventures": [
        ("jine", "kapital[0]", "fáze B",
         "„closed its second fund at nearly €55 million“ je uloženo jako přesných 55 000 000 (ve "
         "skutečnosti horní mez), výhrada je jen v poznámce."),
    ],
    "cz-arx-equity-partners": [
        ("omezeni", "duvod", "fáze A",
         "Zmínka o HLB PROXY (30. 1. 2026) nemá v `zdroj_url` zdroj, neověřeno. Podle fáze A bez vlivu na "
         "závěr. Stránka Medicofit odkazuje na novější investici Direct4me (16. 3. 2026)."),
    ],
    "cz-mam-private-equity-fund": [
        ("omezeni", "duvod", "fáze A",
         "Dvě tiskové zprávy v PDF (8. 9. 2026, 24. 9. 2025) se nepodařilo převést na text. Data ověřena "
         "jen z názvů souborů, text TZ z webu mam-equity.cz."),
    ],
    "cz-everita-capital": [
        ("jine", "—", "fáze B",
         "Fáze B se EVERITA zabývala jen kvůli otázce, zda je nástupcem Espiry (viz "
         "cz-espira-investments). K záznamu EVERITA nález nemá."),
    ],
}
# Orbit: omezení z fáze A doplněné k nálezům fáze B.
NALEZY_B["cz-orbit-capital"].append(
    ("omezeni", "duvod", "fáze A", "Vestbee 2023 zmíněný v důvodu není v seznamu URL, neověřeno, bez vlivu."))

TRIDY = [
    ("rozpor", "Potvrzený rozpor"),
    ("podezreni", "Podezření"),
    ("nedostatecny", "Nedostatečný důkaz"),
    ("jine", "Otázky výkladu PLAN.md a jiná upřesnění (nejde o nález v datech)"),
    ("omezeni", "Omezení kontroly (co druhý agent neověřil)"),
]
ZAVER_NA_TRIDU = {"potvrzeny_rozpor": "rozpor", "podezreni": "podezreni",
                  "nedostatecny_dukaz": "nedostatecny"}


def nacti_csv(cesta):
    with open(cesta, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def v(x):
    return "`null`" if x is None or x == "" else f"`{x}`"


def odkaz(u):
    u = u.strip()
    if u.startswith("http"):
        text = u.split("://", 1)[1]
        if text.startswith("www."):
            text = text[4:]
        if len(text) > 80:
            text = text[:77] + "…"
        text = text.replace("[", "(").replace("]", ")")
        href = quote(u, safe=":/?#&=%+@,;~!$*'-._")
        return f"[{text}]({href})"
    if u and (ROOT / u).exists():
        return f"[{u}](../../{u})"
    return f"`{u}`"


def odkazy(retezec):
    return [odkaz(u) for u in retezec.split(" | ") if u.strip()]


def citace(text):
    return "\n".join("> " + r if r else ">" for r in text.splitlines())


def zdroj_radek(z):
    return (f"{z['druh_zdroje']}, {z['vydavatel']}, zdroj_datum {v(z['zdroj_datum'])}, "
            f"puvod {v(z['puvod'])}: {odkaz(z['url'])}")


def investice_zaznamu(r):
    return [("poslední", r["posledni_investice"])] + [("další", i) for i in r["dalsi_investice"]]


def datum_filtru(inv):
    return inv["datum_investice"] if inv["datum_pro_filtr"] == "investice" else inv["datum_oznameni"]


def oddil_zarazeny(r):
    o = []
    ps = r["pravni_subjekt"]
    o.append(f"**`existence`**: Subjekt existuje (rejstřík nebo regulátor)")
    o.append(f"- `pravni_subjekt`: „{ps['hodnota']}“, IČO {v(ps['ico'])}")
    for z in ps["zdroje"]:
        o.append(f"  - {zdroj_radek(z)}")
    o.append(f"- `jistota.existence`: {v(r['jistota']['existence'])}")
    o.append("")

    o.append(f"**`investicni_cinnost`**: Investiční činnost je doložená zprávou o transakci v okně "
             f"24 měsíců (okno od {OKNO_24}, hranice 12 měsíců {OKNO_12})")
    o.append(f"- `status`: {v(r['status'])}")
    for druh, inv in investice_zaznamu(r):
        zpravy = [odkaz(z["url"]) for z in inv["zdroje"] if z["druh_zdroje"] == "zprava_o_transakci"]
        podpurne = [f"{z['druh_zdroje']} {odkaz(z['url'])}" for z in inv["zdroje"]
                    if z["druh_zdroje"] != "zprava_o_transakci"]
        o.append(f"- {druh}: **{inv['firma']}**, `datum_pro_filtr` {v(inv['datum_pro_filtr'])} → "
                 f"{v(datum_filtru(inv))}; zprávy o transakci: {', '.join(zpravy) or 'žádná'}"
                 + (f"; podpůrné: {', '.join(podpurne)}" if podpurne else ""))
    o.append("")

    o.append("**`je_investor`**: Je to investor podle pravidel z bodu 2 a 3")
    o.append("- podmínka 1: viz `existence`, podmínka 2: viz `investicni_cinnost`")
    o.append("- podmínka 3, nástroj u jednotlivých investic:")
    for druh, inv in investice_zaznamu(r):
        n = inv["nastroj"]
        zdroj = odkaz(n["zdroj_url"]) if n["zdroj_url"] else "bez zdroje"
        o.append(f"  - {inv['firma']}: `hodnota` {v(n['hodnota'])}, `doklad` {v(n['doklad'])}, "
                 f"`kolo` {v(n['kolo'])}, {zdroj}")
    o.append("")

    o.append("**`typ`**: Typ je zařazen správně")
    o.append(f"- `typ`: {v(r['typ'])}, zdůvodnění agenta je v poznámce na konci oddílu")
    o.append("")

    o.append("**`rozsah_pilotu`**: Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR)")
    o.append(f"- `typ` {v(r['typ'])}, `zeme` {v(r['zeme'])}, sídlo podle `pravni_subjekt`: „{ps['hodnota']}“")
    o.append("")

    p = r["posledni_investice"]
    n = p["nastroj"]
    o.append("**`posledni_investice`**: Poslední investice sedí (firma, datum investice nebo oznámení "
             "podle zprávy o transakci, `datum_pro_filtr`)")
    o.append(f"- `firma` „{p['firma']}“, `datum_investice` {v(p['datum_investice'])}, "
             f"`datum_oznameni` {v(p['datum_oznameni'])}, `datum_pro_filtr` {v(p['datum_pro_filtr'])}")
    o.append(f"- `nastroj`: `hodnota` {v(n['hodnota'])}, `doklad` {v(n['doklad'])}, `kolo` {v(n['kolo'])}")
    for z in p["zdroje"]:
        o.append(f"  - {zdroj_radek(z)}")
    o.append("")

    o.append("**`nezavislost_zdroju`**: Zdroje uvedené jako nezávislé mají opravdu různý původ")
    o.append(f"- `jistota.investice`: {v(r['jistota']['investice'])}")
    for druh, inv in investice_zaznamu(r):
        zpravy = [z for z in inv["zdroje"] if z["druh_zdroje"] == "zprava_o_transakci"]
        casti = [f"{z['vydavatel']} (puvod {v(z['puvod'])}) {odkaz(z['url'])}" for z in zpravy]
        o.append(f"- {inv['firma']}: " + ("; ".join(casti) if casti else "žádná zpráva o transakci"))
    o.append("")

    s = r["sektory"]
    o.append("**`sektory`**: Sektory odpovídají zdroji")
    if s["hodnota"]:
        o.append(f"- {', '.join(s['hodnota'])}; zdroj {odkaz(s['zdroj_url'])}, zdroj_datum {v(s['zdroj_datum'])}")
    else:
        o.append("- nevyplněno (`null`)")
    o.append("")

    t = r["ticket"]
    o.append("**`ticket`**: Ticket odpovídá zdroji")
    if t["min"] is None and t["max"] is None:
        o.append("- nevyplněno (`null`)")
    else:
        o.append(f"- `min` {v(t['min'])}, `max` {v(t['max'])}, `mena` {v(t['mena'])}; zdroj "
                 f"{odkaz(t['zdroj_url'])}, zdroj_datum {v(t['zdroj_datum'])}")
    o.append("")

    o.append("**`kapital`**: Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele)")
    if not r["kapital"]:
        o.append("- nevyplněno (prázdný seznam)")
    for i, k in enumerate(r["kapital"]):
        o.append(f"- kapital[{i}]: `castka` {v(k['castka'])}, `mena` {v(k['mena'])}, `druh` {v(k['druh'])}, "
                 f"`plati_k` {v(k['plati_k'])}, `fond` {v(k['fond'])}; zdroj {odkaz(k['zdroj_url'])}, "
                 f"zdroj_datum {v(k['zdroj_datum'])}")
    o.append("")

    o.append("<details><summary>Poznámka agenta (celá)</summary>")
    o.append("")
    o.append(r["poznamka"])
    o.append("")
    o.append("</details>")
    return o


def oddil_csv(r, pole, rozhodnuti):
    o = [f"**Důvod agenta (celý):**", "", citace(r["duvod"]), ""]
    o.append("**Zdroje uvedené agentem:**")
    o += [f"- {x}" for x in odkazy(r["zdroj_url"])]
    o.append("")
    for p, otazka in pole:
        doplnek = ""
        if p == "kategorie":
            doplnek = f" Agent: {rozhodnuti}."
        o.append(f"- **`{p}`**: {otazka}.{doplnek}")
    return o


def nacti_vse():
    zarazeni = {r["id"]: r for r in json.load(open(VYSTUP / "investori.json", encoding="utf-8"))}
    vyrazeni = {r["id"]: r for r in nacti_csv(VYSTUP / "vyrazeni.csv")}
    hranicni = {r["id"]: r for r in nacti_csv(VYSTUP / "hranicni.csv")}
    nevyresene = {r["id"]: r for r in nacti_csv(VYSTUP / "nevyresene.csv")}
    mapovani = {r["id"]: r for r in nacti_csv(MAPOVANI)}
    kandidati = {r["id"]: r for r in nacti_csv(KANDIDATI)}
    return zarazeni, vyrazeni, hranicni, nevyresene, mapovani, kandidati


def zarazeni_kandidata(id_, data):
    zarazeni, vyrazeni, hranicni, nevyresene, mapovani, _ = data
    if id_ in zarazeni:
        return "investori.json", POLE_ZARAZENI
    if id_ in vyrazeni:
        return "vyrazeni.csv", POLE_VYRAZENI
    if id_ in hranicni:
        return "hranicni.csv", POLE_VYRAZENI
    if id_ in nevyresene:
        return "nevyresene.csv", POLE_NEVYRESENE
    if mapovani.get(id_, {}).get("soubor") == "slouceno":
        return "mapovani_id.csv", POLE_SLOUCENI
    raise SystemExit(f"neznámé id {id_}")


def nazev(id_, data):
    zarazeni, vyrazeni, hranicni, nevyresene, _, kandidati = data
    for zdroj in (zarazeni, vyrazeni, hranicni, nevyresene, kandidati):
        if id_ in zdroj:
            return zdroj[id_]["nazev"]
    return id_


def rozhodnuti_text(id_, soubor, data):
    zarazeni, vyrazeni, hranicni, nevyresene, mapovani, _ = data
    if soubor == "investori.json":
        return "zařazen"
    if soubor == "vyrazeni.csv":
        return f"vyřazen, kategorie `{vyrazeni[id_]['kategorie']}`"
    if soubor == "hranicni.csv":
        return f"hraniční, druh `{hranicni[id_]['druh']}`"
    if soubor == "nevyresene.csv":
        return f"nevyřešen, otázka `{nevyresene[id_]['otazka']}`"
    return f"sloučen do `{mapovani[id_]['vysledne_id']}`"


POSTUP = f"""## Postup

1. První ruční verdikty vyplním do `data/hodnoceni.csv` **bez čtení** [nalezy_ai.md](nalezy_ai.md) a commitnu je.
2. Před první změnou po přečtení nálezů AI se `data/hodnoceni.csv` zkopíruje do `ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv`:
   `cp data/hodnoceni.csv ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv`
3. Do `data/hodnoceni.csv` pak zapíšu konečný verdikt a do sloupce `poznamka` důvod změny.
4. Přínos druhého agenta bude jen orientační, protože pořadí kontroly je podle jeho nálezů. Kandidáti, u kterých druhý agent něco našel, jsou kontrolovaní dřív a pozorněji, takže porovnání verdiktů před a po čtení nálezů není nezávislé měření.

## Jak vyplňovat `data/hodnoceni.csv`

- Řádky jsou předvyplněné ve stejném pořadí jako tento průvodce: `soubor`, `id`, `pole` a `hodnotil` = {HODNOTIL}. Sloupce `hodnoceni`, `pricina_chyby`, `poznamka` a `datum` jsou prázdné.
- `hodnoceni`: `ano` / `ne` / `nelze_overit` (PLAN.md bod 6).
- `pricina_chyby` jen u chyby: `spatny_zdroj`, `chybne_cteni`, `zastaraly_udaj` nebo `chyba_pravidel` (PLAN.md bod 7).
- Nevyřešení: `je_investor` a `rozsah_pilotu` zároveň zaznamenávají moje rozhodnutí, zvolený typ nebo nástroj uvedu v poznámce (PLAN.md bod 6). Výsledek patří do `data/opraveno/`, původní výstup agenta se nemění.
- U prázdného pole (`null`) PLAN.md bod 7 měří přesnost jen mezi vyplněnými a zvlášť podíl vyplněných.
- Sloučení Nation1 → N1 nemá v PLAN.md vlastní pole. Řádek používá `soubor` = `mapovani_id.csv` a `pole` = `slouceni`, stejně jako kontrola zdrojů (krok 4).
- Okno 24 měsíců začíná {OKNO_24}, hranice 12 měsíců (`aktivni` / `investice_dolozena_12_24_mesicu`) je {OKNO_12}. Obojí agent počítal ke dni zpracování 2026-10-26.

## Pořadí

1. **Příslušnost k pilotu:** sídla N1, Tensor, KAYA a i&i Biotech, typ ZAKA a StartupYard, i&i Prague. Kontrola sloučení Nation1 → N1 je samostatný oddíl hned za N1.
2. **Možná chybná vyřazení:** Orbit, McWin, Espira.
3. **Nevyřešení.**
4. **Ostatní** podle závažnosti nálezů kontroly zdrojů. Kandidáti bez nálezu jsou na konci, zařazení před vyřazenými.

U každého kandidáta je odkaz na jeho id v [nalezy_ai.md](nalezy_ai.md). Ten otevírám až po commitu prvních verdiktů.
"""


def pruvodce(data, poradi):
    zarazeni, vyrazeni, hranicni, nevyresene, mapovani, kandidati = data
    o = ["# Průvodce ruční kontrolou", "",
         "Podklad pro krok 6 z PLAN.md bod 9: ruční ověření všech kandidátů pilotu. U každého kandidáta je "
         "původní rozhodnutí agenta, hodnoty ke kontrole s odkazy na zdroje a pole, která hodnotím. Otázky "
         "a názvy polí jsou podle PLAN.md bod 6: plná kontrola u zařazených, zkrácená u vyřazených a "
         "hraničních, u nevyřešených `je_investor`, `rozsah_pilotu` a `duvod`. Nálezy kontroly zdrojů "
         "tu nejsou.", "",
         "Vytvořeno skriptem [skripty/priprav_podklady.py](skripty/priprav_podklady.py) z "
         "`data/vystup_agenta/` a `ai-log/02-obohaceni/mapovani_id.csv`.", "",
         POSTUP]

    o.append("## Přehled")
    o.append("")
    o.append("| # | id | název | soubor | rozhodnutí agenta | polí |")
    o.append("|---|---|---|---|---|---|")
    for cislo, skupina, id_ in poradi:
        soubor, pole = zarazeni_kandidata(id_, data)
        o.append(f"| {cislo} | [`{id_}`](#{cislo}-{id_}) | {nazev(id_, data)} | {soubor} | "
                 f"{rozhodnuti_text(id_, soubor, data)} | {len(pole)} |")
    o.append("")

    akt_skupina = None
    for cislo, skupina, id_ in poradi:
        if skupina != akt_skupina:
            o.append(f"## Skupina: {skupina}")
            o.append("")
            akt_skupina = skupina
        soubor, pole = zarazeni_kandidata(id_, data)
        # Kotva přehledu odkazuje na <a id>, nadpis s názvem by kotvu měnil.
        o.append(f'<a id="{cislo}-{id_}"></a>')
        o.append(f"### {cislo}. {nazev(id_, data)} (`{id_}`)")
        o.append("")
        hlavicka = [f"Soubor: `{soubor}`", f"rozhodnutí agenta: **{rozhodnuti_text(id_, soubor, data)}**"]
        if soubor == "investori.json":
            r = zarazeni[id_]
            hlavicka += [f"typ {v(r['typ'])}", f"země {v(r['zeme'])}", f"status {v(r['status'])}",
                         f"web {odkaz(r['web']['hodnota']) if r['web']['hodnota'] else '`null`'}"]
        elif soubor in ("vyrazeni.csv", "hranicni.csv", "nevyresene.csv"):
            r = {"vyrazeni.csv": vyrazeni, "hranicni.csv": hranicni, "nevyresene.csv": nevyresene}[soubor][id_]
            hlavicka.append(f"web {odkaz(r['web']) if r['web'] else 'neuveden'}")
        o.append(" · ".join(hlavicka))
        o.append("")
        o.append(f"Nálezy AI: [nalezy_ai.md#{id_}](nalezy_ai.md#{id_}) (číst až po commitu prvních verdiktů)")
        o.append("")

        if soubor == "investori.json":
            o += oddil_zarazeny(zarazeni[id_])
        elif soubor == "vyrazeni.csv":
            r = vyrazeni[id_]
            o += oddil_csv(r, pole, f"`{r['kategorie']}`")
        elif soubor == "hranicni.csv":
            r = hranicni[id_]
            o += oddil_csv(r, pole, f"hranicni.csv, druh `{r['druh']}` (venture debt je podle PLAN.md "
                                    f"bod 3 vyřazen ze základní databáze)")
        elif soubor == "nevyresene.csv":
            r = nevyresene[id_]
            o.append(f"**Otázka:** `{r['otazka']}` · **možnosti:** `{r['moznosti']}`")
            o.append("")
            o += oddil_csv(r, pole, "")
            o.append("- Zvolený typ nebo nástroj uvedu v poznámce.")
        else:
            m = mapovani[id_]
            k = kandidati[id_]
            o.append(f"**Kandidát v `data/kandidati.csv`:** {k['nazev']}, web {odkaz(k['web'])}, "
                     f"seznam {k['zdroj_seznamu']}: " + ", ".join(odkazy(k["zdroj_url"])))
            o.append("")
            o.append("**Odůvodnění agenta (`mapovani_id.csv`):**")
            o.append("")
            o.append(citace(m["poznamka"]))
            o.append("")
            o.append("**Rozhodnutí agenta s výpisem zdrojů:** "
                     "[ai-log/02-obohaceni/duplicity.md](../02-obohaceni/duplicity.md), oddíl "
                     "„Dvojice cz-n1-ventures / cz-nation1“")
            o.append("")
            for p, otazka in pole:
                o.append(f"- **`{p}`**: {otazka}. PLAN.md pro sloučení pole nemá, název převzatý z kroku 4.")
        o.append("")
        o.append(f"Řádky v `hodnoceni.csv`: {', '.join(f'`{p}`' for p, _ in pole)}")
        o.append("")
    return "\n".join(o)


def nalezy(data, poradi):
    slepa = nacti_csv(SLEPA)
    podle_id = {}
    for r in slepa:
        podle_id.setdefault(r["id"], []).append(r)
    zavery = Counter(r["zaver"] for r in slepa)

    o = ["# Nálezy AI pro ruční kontrolu", "",
         "Nálezy kontroly zdrojů druhým agentem (krok 4) seřazené podle id ve stejném pořadí jako "
         "[pruvodce.md](pruvodce.md). **Nečíst před commitem prvních ručních verdiktů** (postup je "
         "v průvodci).", "",
         "Zdroje:",
         "- fáze A, slepá kontrola: [slepa_kontrola.csv](../04-kontrola-zdroju/slepa_kontrola.csv), "
         f"{len(slepa)} řádků; řádky se závěrem jiným než `sedi` jsou tu převzaté doslova,",
         "- fáze B, cílené otázky: [cilene_otazky.md](../04-kontrola-zdroju/cilene_otazky.md); "
         "upřesnění jsou tu zkrácená, citace a podrobný rozbor jsou v původním souboru.", "",
         "## Co tento soubor není", "",
         f"Fáze A zapsala {len(slepa)} řádků: {zavery['sedi']} `sedi`, {zavery['podezreni']} `podezreni`, "
         f"{zavery['potvrzeny_rozpor']} `potvrzeny_rozpor`, {zavery['nedostatecny_dukaz']} "
         f"`nedostatecny_dukaz`. Poměr {zavery['sedi']}/{len(slepa)} **není naměřená přesnost** "
         "výstupu agenta ani kontroly:",
         "- kontroloval stejný model jako první agent. Jeho shoda podle PLAN.md bod 6 není důkaz "
         "správnosti, jen říká, kam se podívat dřív,",
         "- fáze B zjistila, že fáze A se spletla v 11 bodech, mimo jiné u tří řádků `sedi`, které měly "
         "být nálezem (`cz-kaya-vc` sidlo a kapital[2], `cz-garage-angels` kategorie). Počet `sedi` "
         "tedy obsahuje známé chyby kontroly,",
         "- stejnou nekonzistenci kontrolní agenti fáze A posoudili různě (`puvod` null u "
         "`cz-ii-biotech-investments` `sedi`, u `cz-y-soft-ventures` `podezreni`),",
         "- řádky nejsou srovnatelné jednotky: počet řádků na kandidáta se liší podle toho, co agent "
         "vyplnil, a jeden řádek často shrnuje víc údajů (například všechny další investice),",
         "- část tvrzení druhý agent neověřil (nedostupné zdroje, tvrzení bez URL, viz Omezení kontroly).",
         "",
         "Přesnost se měří až z ručního hodnocení podle PLAN.md bod 7.", "",
         "## Třídy nálezů", "",
         "- **Potvrzený rozpor:** zdroj nebo pravidlo PLAN.md přímo odporuje hodnotě v záznamu.",
         "- **Podezření:** zdroje ukazují na možnou chybu, ale nedokazují ji, nebo výsledek závisí na "
         "nejednoznačném výkladu.",
         "- **Nedostatečný důkaz:** hodnotu nebo tvrzení nešlo doložit dostupnými zdroji.",
         "- Mimo tyto třídy jsou zvlášť vedené otázky výkladu PLAN.md (nejde o nález v datech) a omezení "
         "kontroly (co druhý agent neověřil).", "",
         "U fáze A je třída převzatá ze sloupce `zaver`. Fáze B tytéž kategorie nepoužívala všude, její "
         "upřesnění zařadil hlavní agent podle znění cilene_otazky.md. Kde fáze B změnila závěr fáze A, "
         "je to u položky uvedeno.", "",
         "## Otázky výkladu PLAN.md napříč kandidáty", "",
         "Fáze B narazila na místa, která PLAN.md neupravuje. Rozhodnutí patří uživateli, tento soubor "
         "je nerozhoduje.", "",
         "1. **Sídlo správce, nebo značky a týmu.** „Investiční firma (správce, značka) má sídlo v ČR“ "
         "nedává jednoznačnou odpověď, když správce (GP/AIFM) sídlí v Lucembursku a značka s týmem "
         "v Praze. Podle výkladu se mění zařazení `cz-n1-ventures`, `cz-tensor-ventures`, `cz-kaya-vc` "
         "a `cz-ii-biotech-investments`. `cz-depo-ventures` a `cz-zaka-vc` jsou CZ v obou výkladech. "
         "PLAN.md nemá ani otázku `sidlo` v nevyresene.csv.",
         "2. **Klub nebo syndikát andělů.** Typ Angel je jen fyzická osoba, typ pro klub investující "
         "přes SPV chybí (`cz-garage-angels`, `cz-lumus-investments`).",
         "3. **`neni_investor` pro subjekt bez investice v okně, který jinak investuje** "
         "(`cz-espira-investments`, `cz-mcwin-partners`). Bod 3 ho tam řadí, bod 2 říká, že status "
         "popisuje jen veřejnou stopu.",
         "4. **Smíšená strategie equity a venture debt** (`cz-orbit-capital`): hranicni.csv, nebo "
         "vyrazeni.csv.",
         "5. **Zakladatel a sponzor fondu, který investuje i přímo** (`cz-ii-prague` a "
         "`cz-ii-biotech-investments`).",
         "6. **Kapitál:** schéma nemá pole pro přibližnou částku nebo mez (`cz-ii-biotech-investments`, "
         "`cz-inven-capital`, `cz-rockaway-ventures`), `plati_k` se vyplňuje nejednotně (u článků datum "
         "publikace, u nedatovaných webů null), PLAN.md nedefinuje hranici `committed_capital` / "
         "`fund_size` (`cz-czech-founders-vc` proti `cz-reflex-capital`, `cz-ii-biotech-investments`) a "
         "`fond` obsahuje popis místo názvu (`cz-kaya-vc`, `cz-reflex-capital`, `cz-soulmates-ventures`).",
         "7. **`puvod`:** je volný text a u zpráv převzatých z oznámení firmy často null. U záznamů, kde "
         "nástroj stojí jen na nepřímé indicii, to jistotu nemění (strop `stredni`), u `cz-y-soft-ventures` "
         "ano.", "",
         "## Nálezy podle id", ""]

    for cislo, skupina, id_ in poradi:
        soubor, _ = zarazeni_kandidata(id_, data)
        o.append(f"### {id_}")
        o.append("")
        o.append(f"{nazev(id_, data)} · `{soubor}` · {rozhodnuti_text(id_, soubor, data)} · "
                 f"oddíl {cislo} v [pruvodce.md](pruvodce.md)")
        o.append("")
        radky = podle_id.get(id_, [])
        pocty = Counter(r["zaver"] for r in radky)
        o.append(f"Fáze A: {len(radky)} řádků (" +
                 ", ".join(f"{pocty[k]} {k}" for k in ("sedi", "potvrzeny_rozpor", "podezreni",
                                                       "nedostatecny_dukaz") if pocty[k]) + ").")
        o.append("")

        polozky = {t: [] for t, _ in TRIDY}
        for r in radky:
            if r["zaver"] in ZAVER_NA_TRIDU:
                polozky[ZAVER_NA_TRIDU[r["zaver"]]].append(
                    f"`{r['pole']}` (fáze A, `{r['zaver']}`): {r['vysvetleni']} Zdroje: "
                    + ", ".join(odkazy(r["zdroj_url"])))
        for trida, pole, puvod, text in NALEZY_B.get(id_, []):
            polozky[trida].append(f"`{pole}` ({puvod}): {text}")

        if not any(polozky.values()):
            o.append("Bez nálezu: všechny řádky fáze A mají závěr `sedi` a fáze B se k záznamu "
                     "nevyjádřila. Bez nálezu neznamená ověřeno.")
            o.append("")
            continue
        for trida, nadpis in TRIDY:
            if polozky[trida]:
                o.append(f"**{nadpis}**")
                o.append("")
                o += [f"- {p}" for p in polozky[trida]]
                o.append("")
    return "\n".join(o)


def main():
    data = nacti_vse()
    poradi = []
    for skupina, ids in SKUPINY:
        for id_ in ids:
            poradi.append((len(poradi) + 1, skupina, id_))

    zarazeni, vyrazeni, hranicni, nevyresene, mapovani, _ = data
    ocekavane = set(zarazeni) | set(vyrazeni) | set(hranicni) | set(nevyresene) | {
        i for i, r in mapovani.items() if r["soubor"] == "slouceno"}
    ids = [id_ for _, _, id_ in poradi]
    assert len(ids) == len(set(ids)), "duplicitní id v pořadí"
    assert set(ids) == ocekavane, f"rozdíl: {set(ids) ^ ocekavane}"
    assert set(NALEZY_B) <= set(ids)

    (CIL / "pruvodce.md").write_text(pruvodce(data, poradi), encoding="utf-8")
    (CIL / "nalezy_ai.md").write_text(nalezy(data, poradi), encoding="utf-8")

    with open(HODNOCENI, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(HLAVICKA)
        for _, _, id_ in poradi:
            soubor, pole = zarazeni_kandidata(id_, data)
            for p, _ in pole:
                w.writerow([soubor, id_, p, "", "", "", HODNOTIL, ""])

    pocet = Counter(zarazeni_kandidata(i, data)[0] for i in ids)
    print(f"kandidátů {len(ids)} (sloučení započteno zvlášť): {dict(pocet)}")
    print(f"řádků hodnoceni.csv: {sum(len(zarazeni_kandidata(i, data)[1]) for i in ids)}")


if __name__ == "__main__":
    main()
