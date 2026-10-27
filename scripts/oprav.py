"""Opravená verze dat podle dokončeného ručního hodnocení (krok 8, PLAN.md bod 7 a 9).

Čte data/vystup_agenta/ (investori.json, vyrazeni.csv, hranicni.csv, nevyresene.csv),
data/hodnoceni.csv, data/vzorek_kontroly.csv a ai-log/02-obohaceni/mapovani_id.csv,
nic z nich nemění. Bez síťových přístupů, deterministický.

Výstup do data/opraveno/:
- čtyři výsledkové soubory se stejným schématem jako data/vystup_agenta/,
- stav_kontroly.csv: stav ruční kontroly, neověřená pole a výhrady u každého výsledného id,
- ZMENY.md: přehled změn s odkazy na řádky hodnoceni.csv a URL.

Zapracovává jen změny doložené dokončeným hodnocením a jeho podklady. Konkrétní hodnoty jsou
v tabulkách PRESUNY, OPRAVY_INVESTIC, OPRAVY_MIMO_PILOT a VYHRADY. Každý odkaz na hodnocení
je dvojice (id, pole); skript ověří, že řádek existuje a má očekávaný verdikt.

Spuštění z kořene repa: python3 scripts/oprav.py
"""
import copy
import csv
import io
import json
from datetime import date
from pathlib import Path

koren = Path(__file__).resolve().parent.parent
VSTUP = koren / "data" / "vystup_agenta"
VYSTUP = koren / "data" / "opraveno"
HODNOCENI = koren / "data" / "hodnoceni.csv"
VZOREK = koren / "data" / "vzorek_kontroly.csv"
MAPOVANI = koren / "ai-log" / "02-obohaceni" / "mapovani_id.csv"

SOUBORY = ("investori.json", "vyrazeni.csv", "hranicni.csv", "nevyresene.csv")
SEP = " | "
REFERENCNI_DATUM = date(2026, 10, 26)  # stejné jako scripts/zkontroluj_data.py
STAZENO = "2026-10-27"  # den ruční kontroly a ověření v kroku 8
OCEKAVANO_ID = 56
PUVODNI = "data/vystup_agenta/investori.json"
UPLNOST = "Poslední investice je nejnovější doložená investice podle ruční kontroly, ne záruka úplnosti."
UPLNOST_OBECNE = ("Poslední investice je nejnovější doložená nebo nalezená, ne záruka, "
                  "že novější investice neexistuje.")

# ---------- přesuny ze zařazených ----------
# id → cílový soubor, řádek CSV (bez id, nazev, web, které se berou z původního záznamu),
# odkazy na hodnocení (id, pole, očekávaný verdikt) a krátký popis pro ZMENY.md.
PRESUNY = {
    "cz-n1-ventures": {
        "soubor": "vyrazeni.csv",
        "hodnoceni": [("rozsah_pilotu", "ne"), ("investicni_cinnost", "ano"), ("je_investor", "ano"),
                      ("existence", "nelze_overit"), ("ticket", "")],
        "novy_stav": "vyrazeni.csv, mimo_rozsah_pilotu",
        "popis": "sídlo správce mimo ČR (GP v Lucembursku); skutečný investor, ne neinvestor",
        "radek": {
            "kategorie": "mimo_rozsah_pilotu",
            "duvod": (
                "Ruční rozhodnutí o sídle správce (krok 8; hodnoceni.csv {r:rozsah_pilotu}, rozsah_pilotu = ne, "
                "skupina upresneni_metodiky): general partnery a správci fondů jsou Nation 1 GP S.à r.l. "
                "a Nation 1 GP II S.à r.l. v Lucembursku (n1.rocks/disclosure), v Praze sídlí tým a značka. "
                "Investiční firma (správce) tedy nemá sídlo v ČR a pravidla pilotu nesplňuje. Je to skutečný "
                "investor podle bodů 2 a 3, ne neinvestor ({r:investicni_cinnost}, {r:je_investor}: Novoflow, "
                "The VC Corner 4. 11. 2025; Liki24 series A, Forbes UA 3. 7. 2025). Výhrada: právní subjekty "
                "GP nejsou ověřené v registru ({r:existence}, existence = nelze_overit). Ticket v původním "
                "záznamu chybí, web n1.rocks uvádí „Typical 1st investment $100K–$1M“ ({r:ticket}, potvrzené "
                "chybění). Původní úplný záznam: " + PUVODNI + ", id cz-n1-ventures (agent jej zařadil)."),
            "zdroj_url": SEP.join([
                "https://n1.rocks/disclosure",
                "https://www.thevccorner.com/p/novoflow-ai-healthcare-startup",
                "https://n1.rocks/",
            ]),
        },
    },
    "cz-ii-biotech-investments": {
        "soubor": "vyrazeni.csv",
        "hodnoceni": [("rozsah_pilotu", "ne"), ("investicni_cinnost", "ano"), ("je_investor", "ano"),
                      ("ticket", "ne"), ("nezavislost_zdroju", "nelze_overit")],
        "novy_stav": "vyrazeni.csv, mimo_rozsah_pilotu",
        "popis": "fond se sídlem v Lucembursku, česká s.r.o. je poradce a tým; skutečný investor, ne neinvestor",
        "radek": {
            "kategorie": "mimo_rozsah_pilotu",
            "duvod": (
                "Ruční rozhodnutí o sídle správce (krok 8; hodnoceni.csv {r:rozsah_pilotu}, rozsah_pilotu = ne, "
                "skupina upresneni_metodiky): fond i&i Biotech Fund I SCSp sídlí v Lucembursku (ÚOCHB "
                "30. 11. 2022 „Luxemburg-based venture capital firm“, web „Headquarters: 42, rue de la Vallée, "
                "L-2661 Luxembourg“), česká Biotech Investments s.r.o. (IČO 10885978, Praha 8) je investiční "
                "poradce a tým. Pravidla pilotu proto nesplňuje. Je to skutečný investor podle bodů 2 a 3, "
                "ne neinvestor ({r:investicni_cinnost}, {r:je_investor}: Theorema pre-seed, Lupa.cz 27. 3. 2026). "
                "Ticket ({r:ticket}, omezení schématu): web rozlišuje dva intervaly, „from €150k“ při zakládání "
                "firmy (business creation) a „sweet spot €0.5M to €2M“ při růstu; spojený interval "
                "150 000–2 000 000 EUR z původního záznamu neplatí. Výhrada: nezávislost zdrojů u Theorema "
                "neověřena ({r:nezavislost_zdroju}). Původní úplný záznam: " + PUVODNI
                + ", id cz-ii-biotech-investments (agent jej zařadil)."),
            "zdroj_url": SEP.join([
                "https://www.inibio.eu/",
                "https://www.lupa.cz/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-milionu-aby-urychlily-vedecky-vyzkum-a-vyvoj/",
            ]),
        },
    },
    "cz-tensor-ventures": {
        "soubor": "nevyresene.csv",
        "hodnoceni": [("rozsah_pilotu", "nelze_overit"), ("existence", "ano"), ("investicni_cinnost", "ano"),
                      ("je_investor", "ano"), ("nezavislost_zdroju", "nelze_overit")],
        "novy_stav": "nevyresene.csv, otazka sidlo",
        "popis": "sídlo správce neověřené, pravidla pilotu vyžadují správce v ČR",
        "radek": {
            "otazka": "sidlo",
            "moznosti": SEP.join(["zarazen", "mimo_rozsah_pilotu"]),
            "duvod": (
                "Ruční kontrola (krok 8; hodnoceni.csv {r:rozsah_pilotu}, rozsah_pilotu = nelze_overit): web "
                "uvádí jako adresu Tensor Ventures GP S.à r.l. a Tensor Ventures Fund I SCSp v Lucembursku; "
                "česká Tensor Ventures a.s. (IČO 06257241, Praha 8) existuje ({r:existence}), ale není doloženo, "
                "že je správcem fondů, a správce druhého fondu (s EIF) doložen není. Pravidla pilotu vyžadují "
                "sídlo investiční firmy (správce) v ČR, neověřené sídlo proto zařazení brání. Investor podle "
                "bodů 2 a 3 je doložen ({r:investicni_cinnost}, {r:je_investor}). Rozhodne doložení správce "
                "(GP/AIFM) obou fondů: správce v ČR → zarazen, správce v Lucembursku → mimo_rozsah_pilotu "
                "(stejně jako N1 a i&i Biotech). Výhrada: nezávislost zdrojů u ValkaAI neověřena "
                "({r:nezavislost_zdroju}). Původní úplný záznam: " + PUVODNI + ", id cz-tensor-ventures."),
            "zdroj_url": SEP.join([
                "https://tensor.ventures/",
                "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/06257241",
            ]),
        },
    },
    "cz-ii-prague": {
        "soubor": "nevyresene.csv",
        "hodnoceni": [("je_investor", "nelze_overit"), ("investicni_cinnost", "ano"), ("typ", "ano"),
                      ("rozsah_pilotu", "ano"), ("posledni_investice", "ano")],
        "novy_stav": "nevyresene.csv, otazka nastroj",
        "popis": "nástroj u jediné investice v okně nedoložen (PLAN.md bod 3, Nevyřešená rozhodnutí)",
        "radek": {
            "otazka": "nastroj",
            "moznosti": SEP.join(["zarazen", "neni_investor"]),
            "duvod": (
                "Ruční kontrola (krok 8; hodnoceni.csv {r:je_investor}, je_investor = nelze_overit): jediná "
                "zapsaná investice v okně (CasInvent Pharma, oznámení 26. 6. 2025, TZ CasInvent přes Positiv.cz "
                "a KHAN-I) neuvádí nástroj ani označení kola. Doklad z rejstříku, o který agent opřel "
                "nastroj = dolozeno, ukazuje i&i Prague jako jediného akcionáře CasInvent jen 18. 11.–15. 12. 2020 "
                "(založení), ne tuto investici ({r:posledni_investice}). Podmínka 3 tedy doložená není a podle "
                "PLAN.md (bod 3, Nevyřešená rozhodnutí) jde kandidát k ručnímu rozhodnutí. Chybějící důkaz "
                "o nástroji neznamená, že i&i Prague není investor: investice je doložená ({r:investicni_cinnost}), "
                "typ VC a sídlo v ČR sedí ({r:typ}, {r:rozsah_pilotu}). Rozhodne zdroj, který uvede nástroj účasti "
                "i&i Prague v kole 2025: podíl nebo konvertibilní nástroj → zarazen, výhradně dluh → neni_investor. "
                "Původní úplný záznam: " + PUVODNI + ", id cz-ii-prague."),
            "zdroj_url": SEP.join([
                "https://positiv.cz/business/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vyvoj-cilene-lecby-nadoru/",
                "https://khanu.de/2025/07/02/casinvent-pharma-secures-next-investment-round-with-strong-support-from-existing-and-local-investors-to-advance-ck1-inhibitor-development-for-treatment-resistant-cancer-patients/",
                "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221",
            ]),
        },
    },
    "cz-presto-ventures": {
        "soubor": "nevyresene.csv",
        "hodnoceni": [("investicni_cinnost", "nelze_overit"), ("je_investor", "nelze_overit"),
                      ("posledni_investice", "nelze_overit"), ("existence", "ano"), ("rozsah_pilotu", "ano")],
        "novy_stav": "nevyresene.csv, otazka investice",
        "popis": "přiřazení investic v okně k Prestu nedoložené (ne vyvrácené)",
        "radek": {
            "otazka": "investice",
            "moznosti": SEP.join(["zarazen", "mimo_rozsah_pilotu", "neni_investor"]),
            "duvod": (
                "Ruční kontrola (krok 8; hodnoceni.csv {r:investicni_cinnost}, {r:je_investor}, "
                "{r:posledni_investice}, vše nelze_overit): investice v okně zapsané agentem (SatVu 18. 2. 2026, "
                "Occam 11. 2. 2026) provedl fond (Presto) Tech Horizons – Tech Horizons SCSp v Lucembursku se "
                "správcem Tech Horizons GP S.à r.l. a vlastní governance (techhorizons.eu); vazba jeho správy "
                "na Presto Ventures ani vztah v době investic nejsou doložené. Cílené ověření 27. 10. 2026 "
                "(Outfindo, Elin.ai) investici Presta v okně nedoložilo. Podmínka 2 tak pro subjekt záznamu "
                "(Presto Ventures II a.s., Praha 1, {r:existence}, {r:rozsah_pilotu}) doložená není. Přiřazení je "
                "nedoložené, ne vyvrácené: chybějící důkaz neznamená, že Presto Ventures není investor. Rozhodne "
                "doklad, kdo investice provedl a kdo fond spravuje: Presto jako investor se správcem v ČR → "
                "zarazen; investice jen přes fond se správcem v Lucembursku → mimo_rozsah_pilotu; bez jakékoli "
                "doložené investice Presta v okně → neni_investor. Původní úplný záznam: " + PUVODNI
                + ", id cz-presto-ventures."),
            "zdroj_url": SEP.join([
                "https://pulse2.com/satvu-raises-30-million-in-nato-innovation-fund-backed-round-to-scale-multi-satellite-constellation/amp/",
                "https://csg.com/en/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengthening-space-and-thermal-intelligence-capabilities",
                "https://techhorizons.eu/",
                "https://www.prestoventures.com/",
            ]),
        },
    },
}

# ---------- opravy poslední investice ----------
# Nová poslední investice podle hodnocení; původní se přesune na začátek dalsi_investice.
# Náhrady v poznamka: (původní text, nový text), každý původní text musí být v poznámce právě jednou.
OPRAVY_INVESTIC = {
    "cz-look-ai-ventures": {
        "hodnoceni": ("posledni_investice", "ne"),
        "investice": {
            "firma": "Embodied AI",
            "datum_investice": None,
            "datum_oznameni": "2026-09-22",
            "datum_pro_filtr": "oznameni",
            "nastroj": {"hodnota": None, "doklad": "nezjisteno", "kolo": None, "zdroj_url": None},
            "zdroje": [{
                "url": "https://lookai.vc/look-ai-ventures-backs-embodied-ai-robots-manufacturing/",
                "druh_zdroje": "zprava_o_transakci",
                "vydavatel": "Look AI Ventures (tisková zpráva investora)",
                "puvod": None,
                "zdroj_datum": "2026-09-22",
                "stazeno": STAZENO,
            }],
        },
        "doklad_data": ("hlavička článku „Eva Slonkova / September 22, 2026“, metadata "
                        "article:published_time 2026-09-22T23:59:13+00:00"),
        "kolo_vklad": "velikost kola ani vklad Look AI neuvedeny (Pulse 2.0: „did not disclose the size of the round“)",
        "nahrady": [
            ("Poslední investice: Sodex Innovations, tech.eu 13. 7. 2026:",
             "Poslední doložená investice (oprava po ruční kontrole, krok 8): Embodied AI (Lausanne), tisková "
             "zpráva investora na lookai.vc s datem publikace 22. 9. 2026 v hlavičce článku: 'Look AI Ventures "
             "has backed Embodied AI ... The round was led by Faber VC'; velikost kola ani vklad Look AI "
             "neuvedeny, kolo neoznačeno, nástroj nezjištěn. Výhrada: Pulse 2.0 už 16. 9. 2026 jmenoval Look AI "
             "Ventures mezi investory, první veřejné oznámení tedy může být starší než datum_oznameni. "
             "Další: Sodex Innovations, tech.eu 13. 7. 2026:"),
            ("Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.", UPLNOST),
        ],
    },
    "cz-purple-ventures": {
        "hodnoceni": ("posledni_investice", "ne"),
        "investice": {
            "firma": "FLÆ Robotics",
            "datum_investice": None,
            "datum_oznameni": "2026-10-15",
            "datum_pro_filtr": "oznameni",
            "nastroj": {"hodnota": None, "doklad": "neprima_indicie", "kolo": "seed",
                        "zdroj_url": "https://www.thesaasnews.com/news/fl-robotics-raises-1m-seed/"},
            "zdroje": [{
                "url": "https://www.thesaasnews.com/news/fl-robotics-raises-1m-seed/",
                "druh_zdroje": "zprava_o_transakci",
                "vydavatel": "TheSaaSNews",
                "puvod": "https://www.eu-startups.com/2026/10/flae-robotics-raises-over-e1-million-in-seed-funding-to-develop-its-ai-hospitality-agent/",
                "zdroj_datum": "2026-10-15",
                "stazeno": STAZENO,
            }],
        },
        "doklad_data": ("metadata stránky datePublished / article:published_time 2026-10-15T06:28:15Z; "
                        "na stránce zobrazeno „Updated October 14, 2026“ a pole agregátoru "
                        "„Funding Date: October 14, 2026“; Nordic9 uvádí 12. 10. 2026"),
        "kolo_vklad": "seed přes 1 mil. EUR je velikost celého kola, vklad Purple neuveden",
        "nahrady": [
            ("Poslední investice: Comparables.ai (Finsko)",
             "Poslední doložená investice (oprava po ruční kontrole, krok 8): FLÆ Robotics, seed přes 1 mil. EUR "
             "(velikost celého kola, vklad Purple neuveden), TheSaaSNews s časem publikace 15. 10. 2026 "
             "v metadatech stránky, zdrojem článku je EU-Startups: 'The funding round included participation "
             "from Purple Ventures and Garage Angels'. Nástroj neprima_indicie (seed). Datum investice zdroj "
             "jednoznačně neurčuje, proto null. Výhrada: pole agregátoru 'Funding Date: October 14, 2026' "
             "a zobrazené 'Updated October 14, 2026' se s časem publikace rozcházejí, Nordic9 uvádí 12. 10. 2026 "
             "a původní zprávu EU-Startups jsem nečetl, první oznámení tedy může být starší než datum_oznameni. "
             "Další: Comparables.ai (Finsko)"),
            ("Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.", UPLNOST),
        ],
    },
    "cz-reflex-capital": {
        "hodnoceni": ("posledni_investice", "ne"),
        "investice": {
            "firma": "ArtMaster",
            "datum_investice": None,
            "datum_oznameni": "2026-10-21",
            "datum_pro_filtr": "oznameni",
            "nastroj": {"hodnota": None, "doklad": "nezjisteno", "kolo": None, "zdroj_url": None},
            "zdroje": [{
                "url": "https://cc.cz/kdysi-si-v-amsterdamske-red-light-district-vydelaval-hranim-dnes-uz-diky-ai-uci-na-piano-stovky-tisic-lidi/",
                "druh_zdroje": "zprava_o_transakci",
                "vydavatel": "CzechCrunch",
                "puvod": None,
                "zdroj_datum": "2026-10-21",
                "stazeno": STAZENO,
            }],
        },
        "doklad_data": "metadata stránky datePublished 2026-10-21T09:00:39+02:00",
        "kolo_vklad": "2,4 mil. USD je velikost celého kola, vklad Reflexu neuveden",
        "nahrady": [
            ("Poslední investice: Grid.online, CzechCrunch 22. 6. 2026:",
             "Poslední doložená investice (oprava po ruční kontrole, krok 8): ArtMaster, CzechCrunch 21. 10. 2026: "
             "'Teď ArtMaster uzavřel investici ve výši 2,4 milionu dolarů ... K dřívějším investorům se nově "
             "přidávají fondy Factorial Capital a český Reflex Capital'; 2,4 mil. USD je velikost celého kola, "
             "vklad Reflexu neuveden, kolo zdroj neoznačuje, nástroj nezjištěn (Nordic9 kolo označuje jako seed, "
             "nepřevzato). Datum uzavření neuvedeno. Další: Grid.online, CzechCrunch 22. 6. 2026:"),
            ("Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.", UPLNOST),
        ],
    },
    "cz-zaka-vc": {
        "hodnoceni": ("posledni_investice", "ne"),
        "investice": {
            "firma": "FinalDose",
            "datum_investice": None,
            "datum_oznameni": "2026-07-16",
            "datum_pro_filtr": "oznameni",
            "nastroj": {"hodnota": None, "doklad": "nezjisteno", "kolo": None, "zdroj_url": None},
            "zdroje": [{
                "url": "https://zaka.vc/news/",
                "druh_zdroje": "zprava_o_transakci",
                "vydavatel": "ZAKA VC (oznámení investora na stránce novinek)",
                "puvod": None,
                "zdroj_datum": "2026-07-16",
                "stazeno": STAZENO,
            }],
        },
        "doklad_data": ("datum 16. 7. 2026 podle hodnocení a kontrolního agenta (fáze A, 26. 10. 2026); "
                        "v kroku 8 stránka vrátila HTTP 466 a znovu načtena nebyla"),
        "kolo_vklad": "velikost kola, vklad ZAKA ani kolo podklady ruční kontroly neuvádějí",
        "nahrady": [
            ("Poslední investice: ParcelBio, seed 13 mil. USD",
             "Poslední doložená investice (oprava po ruční kontrole, krok 8): FinalDose, oznámení investora "
             "na zaka.vc/news 16. 7. 2026 ('we’re excited to announce our investment in FinalDose'); vlastní "
             "oznámení investora je podle PLAN.md bod 2 přípustná zpráva o transakci. Velikost kola, vklad ZAKA "
             "ani kolo podklady ruční kontroly neuvádějí, nástroj nezjištěn. Výhrada: stránka novinek uvádí "
             "i PerfectBit (tisková zpráva 18. 8. 2026, PitchBook podle vyhledávání seed 26. 6. 2026), ruční "
             "kontrola ho neposoudila, nezapsáno. Další: ParcelBio, seed 13 mil. USD"),
            ("Web a stránka novinek uvádějí i další investice z let 2025–2026 (Cirrus Therapeutics, DeepSeq.AI, "
             "FinalDose aj.), ty jsem nezávislou zprávou o transakci neověřil.",
             "Web a stránka novinek uvádějí i další investice z let 2025–2026 (Cirrus Therapeutics, DeepSeq.AI, "
             "PerfectBit aj.), ty ověřené nejsou; FinalDose doložila ruční kontrola (viz poslední investice)."),
            ("Poslední investice je nejnovější nalezená, ne nutně skutečně poslední.", UPLNOST),
        ],
    },
}

# ---------- opravy zaznamenané jen v přehledu (záznam je mimo pilot) ----------
OPRAVY_MIMO_PILOT = [
    {"id": "cz-n1-ventures", "pole": "ticket", "verdikt": "",
     "puvodne": "null (agent ticket nezapsal)",
     "nove": "web n1.rocks: „Typical 1st investment $100K–$1M“ (100 000–1 000 000 USD, první investice)",
     "url": "https://n1.rocks/"},
    {"id": "cz-ii-biotech-investments", "pole": "ticket", "verdikt": "ne",
     "puvodne": "min 150 000, max 2 000 000 EUR (jeden spojený interval)",
     "nove": "dva intervaly: od 150 000 EUR při zakládání firmy (business creation) a preferovaně "
             "500 000–2 000 000 EUR při růstu; schéma dva intervaly neumí, spojený interval se nepoužije",
     "url": "https://www.inibio.eu/"},
]

# ---------- výhrady k polím hodnoceným „ano“ a další známé nálezy ----------
# id → seznam (text, odkaz na hodnocení (pole, verdikt) nebo None).
VYHRADY = {
    "cz-look-ai-ventures": [
        ("Pulse 2.0 (https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/) "
         "vyšel 16. 9. 2026 a jmenuje Look AI Ventures mezi investory Embodied AI; první veřejné oznámení může "
         "být starší než datum_oznameni 2026-09-22", ("posledni_investice", "ne")),
    ],
    "cz-purple-ventures": [
        ("FLÆ Robotics: datum_oznameni 2026-10-15 podle času publikace TheSaaSNews; „Funding Date: October 14, "
         "2026“ (pole agregátoru) a Nordic9 12. 10. 2026 se rozcházejí, původní zpráva EU-Startups nečtena",
         ("posledni_investice", "ne")),
    ],
    "cz-reflex-capital": [
        ("ArtMaster: Nordic9 označuje kolo jako seed, CzechCrunch kolo neoznačuje; kolo null, nástroj nezjištěn",
         ("posledni_investice", "ne")),
    ],
    "cz-zaka-vc": [
        ("PerfectBit (tisková zpráva 18. 8. 2026 na zaka.vc/news, PitchBook podle vyhledávání seed 26. 6. 2026) "
         "neověřen, ruční kontrola ho neposoudila; FinalDose se v kroku 8 nepodařilo znovu načíst (HTTP 466)",
         ("posledni_investice", "ne")),
        ("typ VC obhajitelný pro Fund 1, AIN.UA 10. 3. 2025 ZAKA označuje jako family office", ("typ", "ano")),
    ],
    "cz-startupyard": [
        ("typ: u investice Ydoca není jisté, zda šla z vlastních peněz StartupYard (TechBoost Syndicate)",
         ("typ", "ano")),
        ("poslední investice: firmy nového batche bez zmínky o investici, nedoloženo", ("posledni_investice", "ano")),
    ],
    "cz-rockaway-ventures": [
        ("poslední investice: Nordic9 1. 3. 2026 uvádí seed do Float, původní oznámení nenalezeno",
         ("posledni_investice", "ano")),
        ("kapitál: zdroj „nearly €55 million“, záznam 55 000 000 je horní mez", ("kapital", "ano")),
    ],
    "cz-credo-ventures": [
        ("rozsah pilotu: role Credo Ventures Management II a.s. jako správce nového fondu neověřena",
         ("rozsah_pilotu", "ano")),
    ],
    "cz-miton": [
        ("poslední investice: citovaný zdroj Lupa.cz nedostupný, firma a datum potvrzeny náhradním zdrojem "
         "CzechCrunch", ("posledni_investice", "ano")),
    ],
    "cz-kaya-vc": [
        ("známý nález automatické kontroly (metodika): kapital[2].fond vyplněn u druhu committed_capital; "
         "bez dokončeného hodnocení neopraveno", None),
        ("nález kontrolního agenta (fáze B): správcem je podle kaya.vc/sustainability lucemburský AIFM "
         "KAYA VC GP S.à r.l.; sídlo správce neposouzeno, zařazení beze změny", None),
    ],
}

# Popis neověřené nezávislosti zdrojů (6 případů, pole nezavislost_zdroju = nelze_overit).
NEZAVISLOST = ("nezávislost zdrojů neověřena: zprávy vedené s puvod null mohou mít společný podklad, "
               "společný původ ani nezávislost nejsou doložené; puvod ani jistota se nemění")


def nacti_csv(cesta):
    with cesta.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def nacti_hodnoceni():
    radky = {}
    for cislo, r in enumerate(nacti_csv(HODNOCENI), start=2):
        radky[(r["id"], r["pole"])] = (cislo, r)
    return radky


HODN = nacti_hodnoceni()


def odkaz(id_, pole, verdikt):
    """Číslo řádku hodnoceni.csv pro (id, pole); ověří očekávaný verdikt."""
    cislo, r = HODN[(id_, pole)]
    assert r["hodnoceni"] == verdikt, (id_, pole, r["hodnoceni"], verdikt)
    return cislo


def text_odkazu(id_, pole, verdikt):
    return f"ř. {odkaz(id_, pole, verdikt)} ({id_}, {pole})"


def rozsah_radku(id_):
    cisla = [c for (i, _), (c, r) in HODN.items() if i == id_ and r["soubor"] == "investori.json"]
    return f"hodnoceni.csv ř. {min(cisla)}–{max(cisla)}" if cisla else ""


def status(inv):
    """Status podle PLAN.md bod 2 a 4 vůči referenčnímu datu (plná data ISO)."""
    klic = "datum_investice" if inv["datum_pro_filtr"] == "investice" else "datum_oznameni"
    d = date.fromisoformat(inv[klic])
    rok = date(REFERENCNI_DATUM.year - 1, REFERENCNI_DATUM.month, REFERENCNI_DATUM.day)
    dva = date(REFERENCNI_DATUM.year - 2, REFERENCNI_DATUM.month, REFERENCNI_DATUM.day)
    assert dva <= d <= REFERENCNI_DATUM, (inv["firma"], d)
    return "aktivni" if d >= rok else "investice_dolozena_12_24_mesicu"


def oprav_zaznam(zaznam, oprava):
    novy = copy.deepcopy(zaznam)
    novy["dalsi_investice"] = [novy["posledni_investice"]] + novy["dalsi_investice"]
    novy["posledni_investice"] = copy.deepcopy(oprava["investice"])
    novy["status"] = status(novy["posledni_investice"])
    for stary, nahrada in oprava["nahrady"]:
        assert novy["poznamka"].count(stary) == 1, (zaznam["id"], stary)
        novy["poznamka"] = novy["poznamka"].replace(stary, nahrada)
    return novy


def csv_radky(radky, sloupce):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=sloupce)
    for r in radky:
        w.writerow(r)
    return buf.getvalue().encode("utf-8")


def sloupce(nazev):
    with (VSTUP / nazev).open(encoding="utf-8", newline="") as f:
        return next(csv.reader(f))


def vyrob():
    puvodni = json.loads((VSTUP / "investori.json").read_text(encoding="utf-8"))
    podle_id = {z["id"]: z for z in puvodni}
    vzorek = {r["id"] for r in nacti_csv(VZOREK)}

    # investori.json: opravy, přesuny ven, ostatní záznamy beze změny
    investori = []
    for z in puvodni:
        if z["id"] in PRESUNY:
            continue
        if z["id"] in OPRAVY_INVESTIC:
            pole, verdikt = OPRAVY_INVESTIC[z["id"]]["hodnoceni"]
            odkaz(z["id"], pole, verdikt)
            investori.append(oprav_zaznam(z, OPRAVY_INVESTIC[z["id"]]))
        else:
            investori.append(z)

    # vyrazeni.csv a nevyresene.csv: původní obsah beze změny + přesunuté řádky na konci
    pridane = {"vyrazeni.csv": [], "nevyresene.csv": []}
    for id_, p in PRESUNY.items():
        z = podle_id[id_]
        odkazy = {pole: text_odkazu(id_, pole, v) for pole, v in p["hodnoceni"]}
        radek = {"id": id_, "nazev": z["nazev"], "web": z["web"]["hodnota"], "stazeno": STAZENO}
        for k, v in p["radek"].items():
            radek[k] = v.replace("{r:", "{").format(**odkazy) if k == "duvod" else v
        pridane[p["soubor"]].append(radek)

    soubory = {
        "investori.json": (json.dumps(investori, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
        "hranicni.csv": (VSTUP / "hranicni.csv").read_bytes(),
    }
    for nazev, radky in pridane.items():
        soubory[nazev] = (VSTUP / nazev).read_bytes() + csv_radky(radky, sloupce(nazev))

    vysledky = {}
    for nazev in SOUBORY:
        if nazev == "investori.json":
            ids = [z["id"] for z in investori]
        else:
            ids = [r["id"] for r in csv.DictReader(io.StringIO(soubory[nazev].decode("utf-8"), newline=""))]
        for id_ in ids:
            vysledky.setdefault(id_, []).append(nazev)

    stav = stav_kontroly(vysledky, podle_id, vzorek)
    soubory["stav_kontroly.csv"] = csv_radky([dict(zip(STAV_SLOUPCE, STAV_SLOUPCE))] + stav, STAV_SLOUPCE)
    soubory["ZMENY.md"] = zmeny_md(podle_id, investori, vysledky, stav, vzorek).encode("utf-8")
    kontrola(vysledky, investori, puvodni, stav)
    return soubory, vysledky, stav


STAV_SLOUPCE = ["id", "vysledny_soubor", "puvodni_soubor", "ve_vzorku", "kontrola", "vysledek",
                "pole_nelze_overit", "opravena_pole", "vyhrady", "odkaz_hodnoceni"]


def puvodni_soubor(id_):
    for nazev in SOUBORY:
        if nazev == "investori.json":
            ids = {z["id"] for z in json.loads((VSTUP / nazev).read_text(encoding="utf-8"))}
        else:
            ids = {r["id"] for r in nacti_csv(VSTUP / nazev)}
        if id_ in ids:
            return nazev
    raise KeyError(id_)


def stav_kontroly(vysledky, podle_id, vzorek):
    radky = []
    for id_ in sorted(vysledky):
        soubor = vysledky[id_][0]
        hodnocene = {pole: (c, r) for (i, pole), (c, r) in HODN.items()
                     if i == id_ and r["soubor"] == "investori.json"}
        nelze = [p for p, (_, r) in hodnocene.items() if r["hodnoceni"] == "nelze_overit"]
        vyhrady = []
        if id_ in PRESUNY:
            vyhrady.append(f"{PRESUNY[id_]['popis']} (podrobně sloupec duvod v {soubor})")
        if "nezavislost_zdroju" in nelze:
            vyhrady.append(f"{NEZAVISLOST} [ř. {odkaz(id_, 'nezavislost_zdroju', 'nelze_overit')}, "
                           "nezavislost_zdroju]")
        for text, ref in VYHRADY.get(id_, []):
            vyhrady.append(f"{text} [ř. {odkaz(id_, *ref)}, {ref[0]}]" if ref else text)
        opravena = []
        if id_ in vzorek:
            kontrola_ = "hodnoceno_s_asistenci_ai"
            if id_ in PRESUNY:
                vysledek = "presunuto"
                opravena = ["zarazeni"]
            elif id_ in OPRAVY_INVESTIC:
                vysledek = "s_opravou"
                opravena = ["posledni_investice", "dalsi_investice", "status", "poznamka"]
            elif nelze:
                vysledek = "s_vyhradou_nelze_overit"
            else:
                vysledek = "hodnocena_pole_ano"
        else:
            assert not hodnocene or all(r["hodnoceni"] == "" for _, r in hodnocene.values()), id_
            kontrola_ = "nekontrolovano"
            vysledek = "nehodnoceno"
            if soubor == "investori.json":
                vyhrady.insert(0, "mimo náhodný vzorek 20 z 27 zařazených (seed 20261027), údaje ručně "
                                  "nekontrolované")
            else:
                vyhrady.insert(0, "původní rozhodnutí agenta, ručně nekontrolováno (PLAN.md bod 7)")
        if soubor == "investori.json":
            vyhrady.append(UPLNOST_OBECNE)
        radky.append({
            "id": id_, "vysledny_soubor": soubor, "puvodni_soubor": puvodni_soubor(id_),
            "ve_vzorku": "ano" if id_ in vzorek else "ne", "kontrola": kontrola_, "vysledek": vysledek,
            "pole_nelze_overit": SEP.join(nelze), "opravena_pole": SEP.join(opravena),
            "vyhrady": "; ".join(vyhrady), "odkaz_hodnoceni": rozsah_radku(id_) if id_ in vzorek else "",
        })
    return radky


def kontrola(vysledky, investori, puvodni, stav):
    """Každé výsledné id právě jednou, shoda s mapováním, nezměněné záznamy beze změny."""
    vicekrat = {i: s for i, s in vysledky.items() if len(s) != 1}
    assert not vicekrat, vicekrat
    assert len(vysledky) == OCEKAVANO_ID, len(vysledky)
    mapovane = {r["vysledne_id"] for r in nacti_csv(MAPOVANI)}
    assert mapovane == set(vysledky), mapovane ^ set(vysledky)
    puv = {z["id"]: z for z in puvodni}
    for z in investori:
        if z["id"] not in OPRAVY_INVESTIC:
            assert z == puv[z["id"]], z["id"]
    assert len(stav) == OCEKAVANO_ID


def pocty(vysledky):
    c = {}
    for s in vysledky.values():
        c[s[0]] = c.get(s[0], 0) + 1
    return c


def md_bunka(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def zmeny_md(podle_id, investori, vysledky, stav, vzorek):
    puv_pocty = {"investori.json": 27, "vyrazeni.csv": 17, "hranicni.csv": 1, "nevyresene.csv": 11}
    nove = pocty(vysledky)
    stav_id = {r["id"]: r for r in stav}
    zar = [r for r in stav if r["vysledny_soubor"] == "investori.json"]
    vys = {}
    for r in zar:
        vys[r["vysledek"]] = vys.get(r["vysledek"], 0) + 1
    o = []
    o.append("# Přehled změn opravené verze (krok 8)")
    o.append("")
    o.append("Vygenerováno skriptem `scripts/oprav.py` z `data/vystup_agenta/` a `data/hodnoceni.csv`. "
             "Nepřepisovat ručně. Původní výstup agenta, hodnocení i měření zůstávají beze změny.")
    o.append("")
    o.append("**Přesnost byla měřena na původním výstupu agenta** (`data/mereni_vzorku.md`). Opravená verze "
             "nemá nové nezávislé měření přesnosti: opravy vycházejí ze stejného hodnocení, takže čísla "
             "z měření na ni nejde přenést ani je přepočítat.")
    o.append("")
    o.append("## Počty")
    o.append("")
    o.append("| soubor | původně | opraveno | změna |")
    o.append("|---|---|---|---|")
    for n in SOUBORY:
        o.append(f"| {n} | {puv_pocty[n]} | {nove.get(n, 0)} | {nove.get(n, 0) - puv_pocty[n]:+d} |")
    o.append(f"| **celkem výsledných id** | {sum(puv_pocty.values())} | {sum(nove.values())} | |")
    o.append("")
    o.append("Stav kontroly zařazených (`stav_kontroly.csv`, sloupec `vysledek`):")
    o.append("")
    for k in ["s_opravou", "hodnocena_pole_ano", "s_vyhradou_nelze_overit", "nehodnoceno"]:
        o.append(f"- `{k}`: {vys.get(k, 0)}")
    o.append("")
    o.append("## Rozsah dokončené kontroly")
    o.append("")
    o.append("- Ručně (s asistencí AI, README „Ruční kontrola – kdo hodnotil“) byl ohodnocen náhodný výběr 20 "
             "z 27 zařazených (seed 20261027, `data/vzorek_kontroly.csv`), deset polí na firmu, a sloučení "
             "Nation1 → N1.")
    o.append("- Sedm zařazených mimo vzorek a všech 29 vyřazených, hraničních a nevyřešených kandidátů z výstupu "
             "agenta ručně kontrolováno nebylo. V opravené verzi zůstávají obsahově beze změny.")
    o.append("- `hodnocena_pole_ano` znamená, že všechna hodnocená pole dostala `ano` v hodnocení s asistencí "
             "AI. Neznamená potvrzení všech údajů: nevyplněná pole se hodnotila jen z hlediska úplnosti "
             "a u poslední investice jde o nejnovější doloženou, ne o záruku úplnosti.")
    o.append("- Stav kontroly, neověřená pole a výhrady každého výsledného id jsou v `stav_kontroly.csv`. "
             "Do `investori.json` se nové pole nepřidává, schéma zůstává podle PLAN.md bod 4.")
    o.append("")
    o.append("## Přesuny")
    o.append("")
    o.append("Původní úplný záznam každého přesunutého id zůstává v `data/vystup_agenta/investori.json` "
             "(stejné id). Řádek v novém souboru na něj odkazuje ve sloupci `duvod`.")
    o.append("")
    o.append("| id | původní stav | nový stav | důvod | důkaz (hodnoceni.csv) | URL |")
    o.append("|---|---|---|---|---|---|")
    for id_, p in PRESUNY.items():
        refy = ", ".join(text_odkazu(id_, pole, v) for pole, v in p["hodnoceni"][:1])
        dalsi = ", ".join(f"ř. {odkaz(id_, pole, v)}" for pole, v in p["hodnoceni"][1:])
        urls = "<br>".join(p["radek"]["zdroj_url"].split(SEP))
        o.append(f"| {id_} | investori.json, zařazen | {p['novy_stav']} | {md_bunka(p['popis'])} | "
                 f"{refy}; dále {dalsi} | {urls} |")
    o.append("")
    o.append("U i&i Prague a Presta chybí důkaz (nástroj, resp. přiřazení investice). Chybějící důkaz "
             "neznamená, že subjekt není investor; oba čekají na ruční rozhodnutí v `nevyresene.csv`.")
    o.append("")
    o.append("## Opravy poslední investice")
    o.append("")
    o.append("Původní poslední investice je přesunutá na začátek `dalsi_investice` beze změny. `datum_investice` "
             "zůstává `null` (zdroje datum transakce jednoznačně neuvádějí), `datum_pro_filtr` = `oznameni`. "
             "Status je přepočítaný podle PLAN.md bod 2 k referenčnímu datu "
             f"{REFERENCNI_DATUM.isoformat()}. `jistota` se nemění (nová investice má jednu zprávu "
             "o transakci nebo zprávy s nedoloženou nezávislostí).")
    o.append("")
    o.append("| id | původní stav | nový stav | kolo × vklad | doklad data | důkaz (hodnoceni.csv) | URL |")
    o.append("|---|---|---|---|---|---|---|")
    for id_, op in OPRAVY_INVESTIC.items():
        stare = podle_id[id_]["posledni_investice"]
        nova = op["investice"]
        nz = next(z for z in investori if z["id"] == id_)
        n = nova["nastroj"]
        o.append(
            f"| {id_} | {md_bunka(stare['firma'])}, oznámení {stare['datum_oznameni']}, status "
            f"{podle_id[id_]['status']} | {md_bunka(nova['firma'])}, oznámení {nova['datum_oznameni']}, "
            f"datum_investice null, nástroj {n['doklad']}, kolo {n['kolo'] or 'null'}, status {nz['status']} | "
            f"{md_bunka(op['kolo_vklad'])} | {md_bunka(op['doklad_data'])} | "
            f"{text_odkazu(id_, *op['hodnoceni'])} | {nova['zdroje'][0]['url']} |")
    o.append("")
    o.append("### Změny v `poznamka`")
    o.append("")
    o.append("Části poznámky, které popisovaly původní poslední investici jako nejnovější, by opraveným "
             "hodnotám odporovaly. Jsou nahrazené, ostatní text poznámky je beze změny. Původní znění je "
             "v `data/vystup_agenta/investori.json`.")
    o.append("")
    for id_, op in OPRAVY_INVESTIC.items():
        o.append(f"- **{id_}**:")
        for stary, novy in op["nahrady"]:
            o.append(f"  - „{stary}“ → „{novy}“")
    o.append("")
    o.append("## Opravy zaznamenané jen v přehledu (záznam je mimo pilot)")
    o.append("")
    o.append("| id | pole | původně | doložená hodnota | důkaz (hodnoceni.csv) | URL |")
    o.append("|---|---|---|---|---|---|")
    for op in OPRAVY_MIMO_PILOT:
        o.append(f"| {op['id']} | {op['pole']} | {md_bunka(op['puvodne'])} | {md_bunka(op['nove'])} | "
                 f"{text_odkazu(op['id'], op['pole'], op['verdikt'])} | {op['url']} |")
    o.append("")
    o.append("Do `vyrazeni.csv` se ticket nezapisuje (schéma CSV ho nemá), je uvedený ve sloupci `duvod`. "
             "U i&i Biotech se nevytváří společný interval.")
    o.append("")
    o.append("## Ověření v kroku 8")
    o.append("")
    o.append("Doplňující fakta z ruční kontroly ověřil Claude načtením stránek 27. 10. 2026 (bez dalšího "
             "plošného dohledávání):")
    o.append("")
    o.append("- Look AI: https://lookai.vc/look-ai-ventures-backs-embodied-ai-robots-manufacturing/ má v hlavičce "
             "článku „Eva Slonkova / September 22, 2026“ a v metadatech article:published_time "
             "2026-09-22T23:59:13+00:00. Pulse 2.0 "
             "(https://pulse2.com/embodied-ai-launches-with-funding-to-automate-european-manufacturing/) má "
             "datePublished 2026-09-16 a jmenuje Look AI Ventures mezi investory; ponecháno jako výhrada.")
    o.append("- Purple: https://www.thesaasnews.com/news/fl-robotics-raises-1m-seed/ má v metadatech "
             "datePublished 2026-10-15T06:28:15Z, na stránce „Updated October 14, 2026“ a pole agregátoru "
             "„Funding Date: October 14, 2026“; jako zdroj uvádí EU-Startups. Nordic9 uvádí 12. 10. 2026. "
             "Použito datum_oznameni 2026-10-15, datum_investice null.")
    o.append("- Reflex: článek CzechCrunch o ArtMasteru má datePublished 2026-10-21; kolo neoznačuje.")
    o.append("- ZAKA: https://zaka.vc/news/ vrátila v kroku 8 HTTP 466 a znovu načtena nebyla. FinalDose "
             "a datum 16. 7. 2026 vycházejí z hodnocení (ř. "
             f"{odkaz('cz-zaka-vc', 'posledni_investice', 'ne')}) a z kontrolního agenta (fáze A).")
    o.append("")
    o.append("## Rozšíření schématu")
    o.append("")
    o.append("- `nevyresene.csv`, sloupec `otazka`: nové hodnoty `sidlo` (nevyřešené sídlo správce, cz-tensor-"
             "ventures) a `investice` (nevyřešené přiřazení investice, cz-presto-ventures), doplněné do PLAN.md "
             "bod 3 a do `scripts/zkontroluj_data.py`. Pravidla zařazení se nemění.")
    o.append("- `stav_kontroly.csv` (nový soubor jen v `data/opraveno/`): sloupce "
             + ", ".join(f"`{s}`" for s in STAV_SLOUPCE) + ". `kontrola` je `hodnoceno_s_asistenci_ai` "
             "nebo `nekontrolovano`; `vysledek` je `s_opravou`, `hodnocena_pole_ano`, "
             "`s_vyhradou_nelze_overit` (některé pole `nelze_overit`), `presunuto` nebo `nehodnoceno`.")
    o.append("")
    o.append("## Zbývající neověřené případy")
    o.append("")
    o.append("| id | výsledný soubor | pole nelze_overit | výhrady |")
    o.append("|---|---|---|---|")
    for r in stav:
        if r["pole_nelze_overit"] or r["id"] in VYHRADY or r["id"] in PRESUNY:
            vyh = r["vyhrady"].replace("; " + UPLNOST_OBECNE, "").replace(UPLNOST_OBECNE, "")
            o.append(f"| {r['id']} | {r['vysledny_soubor']} | {md_bunka(r['pole_nelze_overit']) or '–'} | "
                     f"{md_bunka(vyh) or '–'} |")
    o.append("")
    o.append("Dále: sedm zařazených mimo vzorek (" + ", ".join(
        r["id"] for r in zar if r["kontrola"] == "nekontrolovano") + ") a 29 vyřazených, hraničních "
             "a nevyřešených kandidátů z výstupu agenta ručně kontrolováno nebylo. U všech zařazených platí, "
             "že poslední investice je nejnovější doložená, ne záruka úplnosti.")
    o.append("")
    o.append("## Automatická kontrola opravené verze")
    o.append("")
    o.append("`scripts/zkontroluj_data.py` čte jen `data/vystup_agenta/`. Pro kontrolu opravené verze se spouští "
             "nad dočasným kořenem mimo repozitář: kopie `data/kandidati.csv`, čtyř výsledkových souborů "
             "z `data/opraveno/` jako `data/vystup_agenta/` a kopie `ai-log/02-obohaceni/mapovani_id.csv`, "
             "ve které je u pěti přesunutých id změněný sloupec `soubor`. Původní data se nepřesouvají "
             "ani nepřepisují. Kontrola URL (`--over-url`) se nespouštěla.")
    o.append("")
    o.append("- `--datum 2026-10-26` (výchozí, den kroku 2): chyby struktury 0, metodický nesoulad 10, "
             "upozornění 8. Devět nálezů „datum není v budoucnosti“ má jedinou příčinu: zdroje čtené "
             "v kroku 8 mají `stazeno` 2026-10-27, tedy po referenčním datu. Desátý je známý nález u KAYA.")
    o.append("- `--datum 2026-10-27` (den ruční kontroly): chyby struktury 0, metodický nesoulad 1 (známý nález "
             "u cz-kaya-vc: `kapital[2].fond` u druhu `committed_capital`, mimo vzorek, bez dokončeného hodnocení "
             "neopraveno), upozornění 8 (stejná jako při 2026-10-26). Statusy se posunem referenčního data "
             "nemění.")
    o.append("- Upozornění je 8 místo 16 v `ai-log/03-kontrola/automaticka_kontrola.md` ze dvou důvodů: kontrola "
             "URL se nespouštěla (5 nedostupných URL v původní zprávě) a upozornění k `cvca.cz` a `plati_k` "
             "u N1 a i&i Biotech zmizela s přesunem jejich záznamů z `investori.json` do `vyrazeni.csv` "
             "(3 nálezy).")
    o.append("")
    o.append("## Jak opravenou verzi znovu vytvořit")
    o.append("")
    o.append("`python3 scripts/oprav.py` (bez sítě, deterministický; přepíše jen soubory v `data/opraveno/`).")
    o.append("")
    return "\n".join(o)


def main():
    soubory, vysledky, stav = vyrob()
    VYSTUP.mkdir(parents=True, exist_ok=True)
    for nazev, obsah in soubory.items():
        (VYSTUP / nazev).write_bytes(obsah)
    c = pocty(vysledky)
    print("Výsledná id:", sum(c.values()), {n: c.get(n, 0) for n in SOUBORY})
    zar = [r for r in stav if r["vysledny_soubor"] == "investori.json"]
    vys = {}
    for r in zar:
        vys[r["vysledek"]] = vys.get(r["vysledek"], 0) + 1
    print("Zařazení podle výsledku kontroly:", dict(sorted(vys.items())))


if __name__ == "__main__":
    main()
