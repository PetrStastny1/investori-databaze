"""Automatická kontrola výstupu agenta (PLAN.md, bod 6 „Automaticky (skript)“ a bod 9, krok 4).

Použití:
    python3 scripts/zkontroluj_data.py [--datum 2026-10-26] [--over-url] [--vystup CESTA]

Vstupy (jen čte, nic neopravuje):
- data/kandidati.csv: všech 57 vstupních id,
- data/vystup_agenta/: investori.json, vyrazeni.csv, hranicni.csv, nevyresene.csv,
- ai-log/02-obohaceni/mapovani_id.csv: kam každé vstupní id skončilo, včetně sloučení duplicit.

Výstup: ai-log/03-kontrola/automaticka_kontrola.md.

Nálezy mají tři kategorie:
- struktura: soubor nebo pole neodpovídá schématu (chybějící klíč, typ, nepovolená hodnota,
  chybějící nebo zdvojený výsledek kandidáta),
- metodika: data mají správný tvar, ale odporují pravidlům plánu (okno 24 měsíců, status,
  jistota, nástroj, pravidla pilotu, zdroj u vyplněného pole),
- upozorneni: nejde o porušení pravidla, ale zdroj nebo údaj je potřeba zkontrolovat ručně
  (zkrácené datum u hranice okna, zdroj stažený bez ověření TLS, nedostupná URL a podobně).

Referenční datum je parametr (výchozí 2026-10-26, den běhu kroku 2), aby šel výsledek
zopakovat. Kontrola URL je volitelná (--over-url). HTTP 200 nepotvrzuje správnost údaje
a neúspěšné stažení nedokazuje, že je údaj nepravdivý, proto obojí jde nanejvýš do upozornění.

Návratový kód je 1, když kontrola najde chybu struktury, jinak 0.
"""
import argparse
import csv
import hashlib
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
VYCHOZI_DATUM = "2026-10-26"
OCEKAVANY_POCET = 57
SEP = " | "

STRUKTURA, METODIKA, UPOZORNENI = "struktura", "metodika", "upozorneni"
KATEGORIE = {
    STRUKTURA: "Chyby struktury",
    METODIKA: "Metodický nesoulad",
    UPOZORNENI: "Upozornění vyžadující kontrolu zdroje",
}

TYPY = {"VC", "CVC", "PE", "Family office", "Angel", "Velký soukromý investor",
        "Korporátní investor bez samostatné jednotky"}
TYPY_PILOT = {"VC", "CVC"}
ZEME_PILOT = "CZ"
STATUSY = {"aktivni", "investice_dolozena_12_24_mesicu"}
JISTOTY = {"vysoka", "stredni", "nizka"}
PORADI_JISTOTY = {"nizka": 0, "stredni": 1, "vysoka": 2}
DRUH_EXIST = {"rejstrik", "regulator", "asociace", "media", "web_subjektu"}
DRUH_INV = {"zprava_o_transakci", "portfolio_web", "rejstrik_spolecnik"}
DRUH_KAPITAL = {"aum", "committed_capital", "fund_size"}
NASTROJ_HODNOTA = {"podil", "konvertibilni", None}
NASTROJ_DOKLAD = {"dolozeno", "neprima_indicie", "nezjisteno"}
DATUM_PRO_FILTR = {"investice", "oznameni"}
KATEGORIE_VYRAZENI = {"neni_investor", "mimo_rozsah_pilotu"}
OTAZKY = {"typ", "nastroj"}
MOZNOSTI = {"zarazen", "mimo_rozsah_pilotu", "neni_investor"}
SOUBORY_VYSTUPU = ("investori.json", "vyrazeni.csv", "hranicni.csv", "nevyresene.csv")
SLOUCENO = "slouceno"

# Kola, u kterých plán (bod 4, Nástroj) připouští neprima_indicie jako pracovní předpoklad.
RE_KOLO = re.compile(r"^(pre-seed|seed|series [a-z])$", re.IGNORECASE)
# Označení, která jsou zjevně varianta seed nebo series kola, ale nejsou v kanonickém tvaru.
RE_KOLO_VARIANTA = re.compile(r"\b(seed|series [a-z])\b", re.IGNORECASE)
RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_DATUM = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
RE_URL_V_TEXTU = re.compile(r"https?://[^\s\"'„“”)<>|]+")

SLOUPCE = {
    "kandidati.csv": ["id", "nazev", "web", "zdroj_seznamu", "zdroj_url", "stazeno"],
    "vyrazeni.csv": ["id", "nazev", "web", "kategorie", "duvod", "zdroj_url", "stazeno"],
    "hranicni.csv": ["id", "nazev", "web", "druh", "duvod", "zdroj_url", "stazeno"],
    "nevyresene.csv": ["id", "nazev", "web", "otazka", "moznosti", "duvod", "zdroj_url", "stazeno"],
    "mapovani_id.csv": ["id", "vysledne_id", "soubor", "davka", "poznamka"],
}
KLICE_ZAZNAMU = ["id", "nazev", "typ", "zeme", "pravni_subjekt", "web", "sektory", "faze", "ticket",
                 "kapital", "posledni_investice", "dalsi_investice", "status", "jistota", "poznamka"]
KLICE_ZDROJE = ["url", "druh_zdroje", "vydavatel", "puvod", "zdroj_datum", "stazeno"]
KLICE_INVESTICE = ["firma", "datum_investice", "datum_oznameni", "datum_pro_filtr", "nastroj", "zdroje"]
KLICE_NASTROJE = ["hodnota", "doklad", "kolo", "zdroj_url"]
KLICE_KAPITALU = ["castka", "mena", "plati_k", "druh", "fond", "zdroj_url", "zdroj_datum", "stazeno"]

# Domény s neplatným certifikátem TLS a známá stažení bez ověření certifikátu v kroku 2.
# Zdroj: ai-log/02-obohaceni/nejasnosti.md (dávka 6, bod 5 a „Napříč dávkami“)
# a ai-log/02-obohaceni.txt (profil CVCA u Theinu stažený přes curl -k).
NEPLATNY_CERTIFIKAT = {"cvca.cz"}
STAZENO_BEZ_TLS = {("cz-thein", "cvca.cz")}

# Aktivní kódy ISO 4217 (bez XTS a XXX, které měnu neoznačují).
ISO_4217 = set("""
AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BOV BRL BSD BTN BWP
BYN BZD CAD CDF CHE CHF CHW CLF CLP CNY COP COU CRC CUC CUP CVE CZK DJF DKK DOP DZD EGP ERN ETB
EUR FJD FKP GBP GEL GHS GIP GMD GNF GTQ GYD HKD HNL HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY
KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LYD MAD MDL MGA MKD MMK MNT MOP MRU MUR
MVR MWK MXN MXV MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB
RWF SAR SBD SCR SDG SEK SGD SHP SLE SLL SOS SRD SSP STN SVC SYP SZL THB TJS TMT TND TOP TRY TTD
TWD TZS UAH UGX USD USN UYI UYU UYW UZS VED VES VND VUV WST XAF XAG XAU XBA XBB XBC XBD XCD XCG
XDR XOF XPD XPF XPT XSU XUA YER ZAR ZMW ZWG ZWL
""".split())


@dataclass(frozen=True)
class Nalez:
    kategorie: str
    soubor: str
    id: str
    pravidlo: str
    detail: str


def posun_mesice(d, mesice):
    """Datum o daný počet měsíců zpět; 29. 2. v nepřestupném roce → 28. 2."""
    m = d.month - 1 - mesice
    rok, mesic = d.year + m // 12, m % 12 + 1
    for den in (d.day, 30, 29, 28):
        try:
            return date(rok, mesic, den)
        except ValueError:
            continue


def obdobi(text):
    """Vrátí (první den, poslední den) data v plném nebo zkráceném tvaru ISO 8601, jinak None."""
    if not isinstance(text, str) or not RE_DATUM.match(text):
        return None
    try:
        if len(text) == 4:
            return date(int(text), 1, 1), date(int(text), 12, 31)
        if len(text) == 7:
            rok, mesic = int(text[:4]), int(text[5:])
            prvni = date(rok, mesic, 1)
            dalsi = date(rok + mesic // 12, mesic % 12 + 1, 1)
            return prvni, dalsi - timedelta(days=1)
        d = date.fromisoformat(text)
        return d, d
    except ValueError:
        return None


def domena(url):
    host = (urlsplit(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def je_url(text):
    if not isinstance(text, str):
        return False
    casti = urlsplit(text)
    return casti.scheme in ("http", "https") and bool(casti.netloc)


def normalizuj_url(url):
    casti = urlsplit(url.strip())
    return (domena(url) + casti.path.rstrip("/") + ("?" + casti.query if casti.query else "")).lower()


def normalizuj_nazev(nazev):
    text = unicodedata.normalize("NFKD", nazev or "").encode("ascii", "ignore").decode().lower()
    text = re.sub(r"\b(s\.?\s?r\.?\s?o\.?|a\.?\s?s\.?|se|sicav|ltd|gmbh|inc|llc)\b", " ", text)
    return re.sub(r"[^a-z0-9]+", "", text)


def je_cislo(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def sha256(cesta):
    return hashlib.sha256(cesta.read_bytes()).hexdigest()[:12]


class Kontrola:
    def __init__(self, koren, referencni_datum, ocekavany_pocet=OCEKAVANY_POCET):
        self.koren = Path(koren)
        self.ref = referencni_datum
        self.hranice_24 = posun_mesice(referencni_datum, 24)
        self.hranice_12 = posun_mesice(referencni_datum, 12)
        self.ocekavany_pocet = ocekavany_pocet
        self.nalezy = []
        self.urls = {}  # url → {(soubor, id)}
        self.prehled = {}
        self.kandidati = []
        self.mapovani = []
        self.vystup = {s: [] for s in SOUBORY_VYSTUPU}

    # ---------- pomocné ----------

    def pridej(self, kategorie, soubor, id_, pravidlo, detail):
        self.nalezy.append(Nalez(kategorie, soubor, id_ or "", pravidlo, detail))

    def cesta(self, nazev):
        if nazev == "kandidati.csv":
            return self.koren / "data" / "kandidati.csv"
        if nazev == "mapovani_id.csv":
            return self.koren / "ai-log" / "02-obohaceni" / "mapovani_id.csv"
        return self.koren / "data" / "vystup_agenta" / nazev

    def nacti_csv(self, nazev):
        cesta = self.cesta(nazev)
        if not cesta.exists():
            self.pridej(STRUKTURA, nazev, "", "soubor existuje", f"Soubor {cesta} chybí.")
            return []
        with cesta.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != SLOUPCE[nazev]:
                self.pridej(STRUKTURA, nazev, "", "sloupce podle PLAN.md",
                            f"Sloupce {reader.fieldnames}, očekávané {SLOUPCE[nazev]}.")
            radky = []
            for cislo, radek in enumerate(reader, start=2):
                if None in radek or any(v is None for v in radek.values()):
                    self.pridej(STRUKTURA, nazev, radek.get("id"), "počet polí v řádku",
                                f"Řádek {cislo} má jiný počet polí než hlavička.")
                radky.append({k: (v or "") for k, v in radek.items() if k is not None})
            return radky

    def zaregistruj_url(self, url, soubor, id_):
        if je_url(url):
            self.urls.setdefault(url.strip(), set()).add((soubor, id_))

    def over_datum(self, hodnota, soubor, id_, pole, povinne=False, nejpozdeji=None):
        """Zkontroluje formát data; vrátí (první, poslední den) nebo None."""
        if hodnota in (None, ""):
            if povinne:
                self.pridej(METODIKA, soubor, id_, "datum u zdroje", f"`{pole}` chybí.")
            return None
        rozsah = obdobi(hodnota)
        if rozsah is None:
            self.pridej(STRUKTURA, soubor, id_, "datum ve tvaru ISO 8601",
                        f"`{pole}` = {hodnota!r} není platné datum (RRRR, RRRR-MM nebo RRRR-MM-DD).")
            return None
        mez = nejpozdeji or self.ref
        if rozsah[0] > mez:
            self.pridej(METODIKA, soubor, id_, "datum není v budoucnosti",
                        f"`{pole}` = {hodnota} je po {mez.isoformat()}.")
        return rozsah

    # ---------- načtení ----------

    def nacti(self):
        self.kandidati = self.nacti_csv("kandidati.csv")
        self.mapovani = self.nacti_csv("mapovani_id.csv")
        for nazev in SOUBORY_VYSTUPU[1:]:
            self.vystup[nazev] = self.nacti_csv(nazev)
        cesta = self.cesta("investori.json")
        if not cesta.exists():
            self.pridej(STRUKTURA, "investori.json", "", "soubor existuje", f"Soubor {cesta} chybí.")
            return
        try:
            data = json.loads(cesta.read_text(encoding="utf-8"))
        except json.JSONDecodeError as chyba:
            self.pridej(STRUKTURA, "investori.json", "", "platný JSON", str(chyba))
            return
        if not isinstance(data, list):
            self.pridej(STRUKTURA, "investori.json", "", "seznam záznamů",
                        f"Kořen je {type(data).__name__}, očekávaný seznam.")
            return
        for i, zaznam in enumerate(data):
            if not isinstance(zaznam, dict):
                self.pridej(STRUKTURA, "investori.json", "", "záznam je objekt", f"Položka {i} není objekt.")
            else:
                self.vystup["investori.json"].append(zaznam)

    # ---------- pokrytí id a mapování ----------

    def kontroluj_pokryti(self):
        soubor = "mapovani_id.csv"
        vstupni = [r["id"] for r in self.kandidati]
        for id_ in sorted({i for i in vstupni if vstupni.count(i) > 1}):
            self.pridej(STRUKTURA, "kandidati.csv", id_, "unikátní vstupní id", "Id je v kandidati.csv vícekrát.")
        for id_ in vstupni:
            if not RE_ID.match(id_):
                self.pridej(STRUKTURA, "kandidati.csv", id_, "tvar id", "Id neodpovídá tvaru `cz-nazev`.")
        if self.ocekavany_pocet is not None and len(set(vstupni)) != self.ocekavany_pocet:
            self.pridej(STRUKTURA, "kandidati.csv", "", "počet vstupních id",
                        f"{len(set(vstupni))} unikátních id, očekávaných {self.ocekavany_pocet}.")
        vstupni_mnozina = set(vstupni)

        # Kde se které id ve výstupu vyskytuje.
        vyskyty = {}
        for nazev, zaznamy in self.vystup.items():
            for zaznam in zaznamy:
                id_ = zaznam.get("id")
                if not isinstance(id_, str) or not id_:
                    self.pridej(STRUKTURA, nazev, "", "vyplněné id", f"Záznam bez id: {str(zaznam.get('nazev'))[:60]}.")
                    continue
                vyskyty.setdefault(id_, []).append(nazev)
        for id_, kde in sorted(vyskyty.items()):
            if id_ not in vstupni_mnozina:
                self.pridej(STRUKTURA, kde[0], id_, "id pochází z kandidati.csv",
                            f"Id není mezi vstupními kandidáty (výskyt: {', '.join(kde)}).")
            if len(kde) > 1:
                self.pridej(STRUKTURA, kde[0], id_, "jeden výsledek na kandidáta",
                            f"Duplicitní výsledek: id je ve výstupu {len(kde)}× ({', '.join(kde)}).")

        mapa = {}
        for radek in self.mapovani:
            id_ = radek["id"]
            if id_ in mapa:
                self.pridej(STRUKTURA, soubor, id_, "jeden řádek mapování na id", "Id je v mapování vícekrát.")
            mapa[id_] = radek
            if id_ not in vstupni_mnozina:
                self.pridej(STRUKTURA, soubor, id_, "id pochází z kandidati.csv", "Mapované id není mezi kandidáty.")
            if radek["soubor"] not in SOUBORY_VYSTUPU + (SLOUCENO,):
                self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `soubor`", f"`soubor` = {radek['soubor']!r}.")

        for id_ in vstupni:
            radek = mapa.get(id_)
            kde = vyskyty.get(id_, [])
            if radek is None:
                self.pridej(STRUKTURA, soubor, id_, "pokrytí všech vstupních id", "Id chybí v mapování.")
                if not kde:
                    self.pridej(STRUKTURA, "data/vystup_agenta", id_, "pokrytí všech vstupních id",
                                "Chybí výsledek: id není v žádném výstupním souboru.")
                continue
            if radek["soubor"] == SLOUCENO:
                cil = radek["vysledne_id"]
                cil_radek = mapa.get(cil)
                if cil == id_ or not cil:
                    self.pridej(STRUKTURA, soubor, id_, "sloučení míří na jiné id",
                                f"`vysledne_id` = {cil!r} u sloučeného kandidáta.")
                elif cil_radek is None or cil_radek["soubor"] == SLOUCENO:
                    self.pridej(STRUKTURA, soubor, id_, "sloučení míří na zpracovaný záznam",
                                f"Cíl sloučení {cil} nemá vlastní výsledek.")
                elif cil not in vyskyty:
                    self.pridej(STRUKTURA, soubor, id_, "sloučení míří na zpracovaný záznam",
                                f"Cíl sloučení {cil} není v žádném výstupním souboru.")
                if kde:
                    self.pridej(STRUKTURA, kde[0], id_, "sloučené id nemá vlastní výsledek",
                                f"Sloučené id je přesto ve výstupu ({', '.join(kde)}).")
                if not radek["poznamka"].strip():
                    self.pridej(METODIKA, soubor, id_, "zdůvodnění sloučení duplicity",
                                "Sloučení bez zdůvodnění v `poznamka`.")
                elif not RE_URL_V_TEXTU.search(radek["poznamka"]):
                    self.pridej(UPOZORNENI, soubor, id_, "zdůvodnění sloučení duplicity",
                                "Zdůvodnění sloučení neuvádí žádnou URL zdroje.")
                continue
            if radek["vysledne_id"] != id_:
                self.pridej(STRUKTURA, soubor, id_, "nesloučené id se nemění",
                            f"`vysledne_id` = {radek['vysledne_id']!r}, ale `soubor` není {SLOUCENO}.")
            if not kde:
                self.pridej(STRUKTURA, radek["soubor"], id_, "pokrytí všech vstupních id",
                            f"Chybí výsledek: podle mapování má být v {radek['soubor']}, ve výstupu není.")
            elif radek["soubor"] not in kde:
                self.pridej(STRUKTURA, soubor, id_, "mapování odpovídá výstupu",
                            f"Mapování uvádí {radek['soubor']}, id je ve {', '.join(kde)}.")

        souhrn = {}
        for radek in self.mapovani:
            souhrn[radek["soubor"]] = souhrn.get(radek["soubor"], 0) + 1
        self.prehled["pokryti"] = {
            "vstupnich_id": len(vstupni_mnozina),
            "v_mapovani": len(mapa),
            "podle_mapovani": souhrn,
            "ve_vystupu": {n: len(z) for n, z in self.vystup.items()},
        }

    # ---------- CSV výstupy ----------

    def kontroluj_csv(self):
        for nazev in SOUBORY_VYSTUPU[1:]:
            for radek in self.vystup[nazev]:
                id_ = radek["id"]
                if id_ and not RE_ID.match(id_):
                    self.pridej(STRUKTURA, nazev, id_, "tvar id", "Id neodpovídá tvaru `cz-nazev`.")
                if not radek["nazev"].strip():
                    self.pridej(STRUKTURA, nazev, id_, "vyplněný název", "`nazev` je prázdný.")
                if radek["web"] and not je_url(radek["web"]):
                    self.pridej(STRUKTURA, nazev, id_, "platná URL", f"`web` = {radek['web']!r}.")
                if not radek["duvod"].strip():
                    self.pridej(METODIKA, nazev, id_, "rozhodnutí má důvod", "`duvod` je prázdný.")
                urls = [u.strip() for u in radek["zdroj_url"].split(SEP) if u.strip()]
                if not urls:
                    self.pridej(METODIKA, nazev, id_, "rozhodnutí má zdroj", "`zdroj_url` je prázdné.")
                for url in urls:
                    if not je_url(url):
                        self.pridej(STRUKTURA, nazev, id_, "platná URL", f"`zdroj_url` obsahuje {url!r}.")
                    self.zaregistruj_url(url, nazev, id_)
                self.over_datum(radek["stazeno"], nazev, id_, "stazeno", povinne=True)
                for url in RE_URL_V_TEXTU.findall(radek["duvod"]):
                    self.zkontroluj_tls(url.rstrip(".,;:"), nazev, id_, "duvod")
                for url in urls:
                    self.zkontroluj_tls(url, nazev, id_, "zdroj_url")

                if nazev == "vyrazeni.csv" and radek["kategorie"] not in KATEGORIE_VYRAZENI:
                    self.pridej(STRUKTURA, nazev, id_, "povolená hodnota `kategorie`",
                                f"`kategorie` = {radek['kategorie']!r}.")
                if nazev == "hranicni.csv":
                    if not radek["druh"].strip():
                        self.pridej(STRUKTURA, nazev, id_, "vyplněný `druh`", "`druh` je prázdný.")
                    elif radek["druh"] != "venture_debt":
                        self.pridej(UPOZORNENI, nazev, id_, "hraniční případy jsou venture debt",
                                    f"`druh` = {radek['druh']!r}; plán vede v hranicni.csv jen venture debt.")
                if nazev == "nevyresene.csv":
                    otazky = [o.strip() for o in radek["otazka"].split(SEP)]
                    if not otazky or any(o not in OTAZKY for o in otazky):
                        self.pridej(STRUKTURA, nazev, id_, "povolená hodnota `otazka`",
                                    f"`otazka` = {radek['otazka']!r}, povolené {sorted(OTAZKY)}.")
                    moznosti = [m.strip() for m in radek["moznosti"].split(SEP)]
                    if any(m not in MOZNOSTI for m in moznosti):
                        self.pridej(STRUKTURA, nazev, id_, "povolená hodnota `moznosti`",
                                    f"`moznosti` = {radek['moznosti']!r}, povolené {sorted(MOZNOSTI)}.")
                    elif len(set(moznosti)) < 2:
                        self.pridej(METODIKA, nazev, id_, "nevyřešené rozhodnutí má alternativy",
                                    f"`moznosti` = {radek['moznosti']!r}: rozhoduje se aspoň mezi dvěma výsledky.")

    # ---------- investori.json ----------

    def kontroluj_klice(self, objekt, klice, soubor, id_, kde):
        if not isinstance(objekt, dict):
            self.pridej(STRUKTURA, soubor, id_, "tvar objektu", f"`{kde}` není objekt.")
            return False
        chybi = [k for k in klice if k not in objekt]
        navic = [k for k in objekt if k not in klice]
        if chybi:
            self.pridej(STRUKTURA, soubor, id_, "povinné klíče", f"`{kde}`: chybí {chybi}.")
        if navic:
            self.pridej(STRUKTURA, soubor, id_, "povinné klíče", f"`{kde}`: navíc {navic}.")
        return not chybi

    def kontroluj_zdroj(self, zdroj, povolene, soubor, id_, kde):
        if not self.kontroluj_klice(zdroj, KLICE_ZDROJE, soubor, id_, kde):
            return None
        if not je_url(zdroj["url"]):
            self.pridej(STRUKTURA, soubor, id_, "platná URL", f"`{kde}.url` = {zdroj['url']!r}.")
        else:
            self.zaregistruj_url(zdroj["url"], soubor, id_)
            self.zkontroluj_tls(zdroj["url"], soubor, id_, kde)
        if zdroj["druh_zdroje"] not in povolene:
            self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `druh_zdroje`",
                        f"`{kde}.druh_zdroje` = {zdroj['druh_zdroje']!r}, povolené {sorted(povolene)}.")
        if not isinstance(zdroj["vydavatel"], str) or not zdroj["vydavatel"].strip():
            self.pridej(STRUKTURA, soubor, id_, "vyplněný vydavatel", f"`{kde}.vydavatel` chybí.")
        if zdroj["puvod"] is not None and not (isinstance(zdroj["puvod"], str) and zdroj["puvod"].strip()):
            self.pridej(STRUKTURA, soubor, id_, "`puvod` je URL, název nebo null", f"`{kde}.puvod` = {zdroj['puvod']!r}.")
        stazeno = self.over_datum(zdroj["stazeno"], soubor, id_, f"{kde}.stazeno", povinne=True)
        self.over_datum(zdroj["zdroj_datum"], soubor, id_, f"{kde}.zdroj_datum",
                        nejpozdeji=stazeno[1] if stazeno else None)
        return zdroj

    def kontroluj_pole_se_zdrojem(self, pole, nazev, soubor, id_, klice, vyplneno):
        """Pole se zdrojem (`web`, `sektory`, `faze`, `ticket`): vyplněné pole musí mít URL a datum stažení."""
        if not self.kontroluj_klice(pole, klice, soubor, id_, nazev):
            return
        url = pole.get("zdroj_url")
        if vyplneno:
            if not url:
                self.pridej(METODIKA, soubor, id_, "vyplněné pole má zdroj", f"`{nazev}` je vyplněné bez `zdroj_url`.")
            elif not je_url(url):
                self.pridej(STRUKTURA, soubor, id_, "platná URL", f"`{nazev}.zdroj_url` = {url!r}.")
            if not pole.get("stazeno"):
                self.pridej(METODIKA, soubor, id_, "vyplněné pole má datum stažení", f"`{nazev}.stazeno` chybí.")
        elif url:
            self.pridej(UPOZORNENI, soubor, id_, "prázdné pole bez zdroje",
                        f"`{nazev}` je prázdné, ale má `zdroj_url`; ověř, jestli údaj ve zdroji není.")
        if url and je_url(url):
            self.zaregistruj_url(url, soubor, id_)
            self.zkontroluj_tls(url, soubor, id_, nazev)
        stazeno = self.over_datum(pole.get("stazeno"), soubor, id_, f"{nazev}.stazeno")
        if "zdroj_datum" in pole:
            self.over_datum(pole["zdroj_datum"], soubor, id_, f"{nazev}.zdroj_datum",
                            nejpozdeji=stazeno[1] if stazeno else None)

    def kontroluj_mena(self, mena, soubor, id_, kde):
        if not isinstance(mena, str) or mena not in ISO_4217:
            self.pridej(STRUKTURA, soubor, id_, "měna je kód ISO 4217", f"`{kde}` = {mena!r}.")

    def kontroluj_ticket(self, ticket, soubor, id_):
        klice = ["min", "max", "mena", "zdroj_url", "zdroj_datum", "stazeno"]
        if not isinstance(ticket, dict):
            self.pridej(STRUKTURA, soubor, id_, "tvar objektu", "`ticket` není objekt.")
            return
        meze = {}
        for k in ("min", "max"):
            hodnota = ticket.get(k)
            if hodnota is None:
                continue
            if not je_cislo(hodnota):
                self.pridej(STRUKTURA, soubor, id_, "částka je číslo", f"`ticket.{k}` = {hodnota!r}.")
            elif hodnota < 0:
                self.pridej(STRUKTURA, soubor, id_, "částka není záporná", f"`ticket.{k}` = {hodnota}.")
            else:
                meze[k] = hodnota
        vyplneno = bool(meze)
        if vyplneno:
            self.kontroluj_mena(ticket.get("mena"), soubor, id_, "ticket.mena")
        elif ticket.get("mena") is not None:
            self.pridej(UPOZORNENI, soubor, id_, "měna bez částky", f"`ticket.mena` = {ticket['mena']!r} bez min i max.")
        if len(meze) == 2 and meze["min"] > meze["max"]:
            self.pridej(METODIKA, soubor, id_, "ticket min <= max",
                        f"`ticket.min` = {meze['min']} > `ticket.max` = {meze['max']}.")
        self.kontroluj_pole_se_zdrojem(ticket, "ticket", soubor, id_, klice, vyplneno)

    def kontroluj_kapital(self, kapital, soubor, id_):
        if not isinstance(kapital, list):
            self.pridej(STRUKTURA, soubor, id_, "`kapital` je seznam", f"`kapital` je {type(kapital).__name__}.")
            return
        for i, polozka in enumerate(kapital):
            kde = f"kapital[{i}]"
            if not self.kontroluj_klice(polozka, KLICE_KAPITALU, soubor, id_, kde):
                continue
            if not je_cislo(polozka["castka"]):
                self.pridej(STRUKTURA, soubor, id_, "částka je číslo", f"`{kde}.castka` = {polozka['castka']!r}.")
            elif polozka["castka"] <= 0:
                self.pridej(STRUKTURA, soubor, id_, "částka je kladná", f"`{kde}.castka` = {polozka['castka']}.")
            self.kontroluj_mena(polozka["mena"], soubor, id_, f"{kde}.mena")
            if polozka["druh"] not in DRUH_KAPITAL:
                self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `druh` kapitálu",
                            f"`{kde}.druh` = {polozka['druh']!r}, povolené {sorted(DRUH_KAPITAL)}.")
            if polozka["druh"] == "fund_size" and not polozka["fond"]:
                self.pridej(UPOZORNENI, soubor, id_, "`fond` u fund_size", f"`{kde}`: fund_size bez názvu fondu.")
            if polozka["druh"] in ("aum", "committed_capital") and polozka["fond"] is not None:
                self.pridej(METODIKA, soubor, id_, "`fond` jen u fund_size",
                            f"`{kde}.fond` = {polozka['fond']!r} u druhu {polozka['druh']}.")
            if polozka["plati_k"] is None:
                self.pridej(UPOZORNENI, soubor, id_, "`plati_k` u kapitálu",
                            f"`{kde}` ({polozka['castka']} {polozka['mena']}, {polozka['druh']}) nemá datum platnosti.")
            else:
                self.over_datum(polozka["plati_k"], soubor, id_, f"{kde}.plati_k")
            self.kontroluj_pole_se_zdrojem(polozka, kde, soubor, id_, KLICE_KAPITALU, True)

    @staticmethod
    def puvod(zdroj):
        """Původ zprávy o transakci: `puvod`, u null URL zdroje (PLAN.md bod 4 a 6)."""
        puvod = zdroj["puvod"]
        if not puvod:
            return normalizuj_url(zdroj["url"])
        return normalizuj_url(puvod) if je_url(puvod) else puvod.strip().lower()

    def puvody(self, zpravy):
        return {self.puvod(z) for z in zpravy}

    def kontroluj_investici(self, inv, soubor, id_, kde):
        """Vrátí slovník s odvozenými údaji o investici, nebo None při chybě struktury."""
        if not self.kontroluj_klice(inv, KLICE_INVESTICE, soubor, id_, kde):
            return None
        if not isinstance(inv["firma"], str) or not inv["firma"].strip():
            self.pridej(STRUKTURA, soubor, id_, "vyplněná firma", f"`{kde}.firma` chybí.")
        investice = self.over_datum(inv["datum_investice"], soubor, id_, f"{kde}.datum_investice")
        oznameni = self.over_datum(inv["datum_oznameni"], soubor, id_, f"{kde}.datum_oznameni")
        filtr = inv["datum_pro_filtr"]
        rozsah = None
        if filtr not in DATUM_PRO_FILTR:
            self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `datum_pro_filtr`",
                        f"`{kde}.datum_pro_filtr` = {filtr!r}.")
        elif filtr == "investice":
            if inv["datum_investice"] is None:
                self.pridej(METODIKA, soubor, id_, "`datum_pro_filtr` = investice jen s datem investice",
                            f"`{kde}`: `datum_pro_filtr` = investice, ale `datum_investice` je null.")
            rozsah = investice
        else:
            if inv["datum_investice"] is not None:
                self.pridej(METODIKA, soubor, id_, "filtr podle data investice, když je známé",
                            f"`{kde}`: `datum_investice` = {inv['datum_investice']} je vyplněné, "
                            f"ale filtr používá oznámení.")
            if inv["datum_oznameni"] is None:
                self.pridej(METODIKA, soubor, id_, "datum pro filtr je vyplněné",
                            f"`{kde}`: `datum_pro_filtr` = oznameni, ale `datum_oznameni` je null.")
            rozsah = oznameni
        if investice and oznameni and investice[0] > oznameni[1]:
            self.pridej(UPOZORNENI, soubor, id_, "investice před oznámením",
                        f"`{kde}`: datum investice {inv['datum_investice']} je po oznámení {inv['datum_oznameni']}.")

        nastroj = inv["nastroj"]
        kvalifikuje = False
        jen_neprima = False
        if self.kontroluj_klice(nastroj, KLICE_NASTROJE, soubor, id_, f"{kde}.nastroj"):
            hodnota, doklad, kolo, url = (nastroj[k] for k in KLICE_NASTROJE)
            if hodnota not in NASTROJ_HODNOTA:
                self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `nastroj.hodnota`",
                            f"`{kde}.nastroj.hodnota` = {hodnota!r}.")
            if doklad not in NASTROJ_DOKLAD:
                self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `nastroj.doklad`",
                            f"`{kde}.nastroj.doklad` = {doklad!r}.")
            if url is not None:
                if not je_url(url):
                    self.pridej(STRUKTURA, soubor, id_, "platná URL", f"`{kde}.nastroj.zdroj_url` = {url!r}.")
                else:
                    self.zaregistruj_url(url, soubor, id_)
                    self.zkontroluj_tls(url, soubor, id_, f"{kde}.nastroj")
                    zdroje_url = {normalizuj_url(z["url"]) for z in inv["zdroje"]
                                  if isinstance(z, dict) and je_url(z.get("url"))}
                    if normalizuj_url(url) not in zdroje_url:
                        self.pridej(UPOZORNENI, soubor, id_, "zdroj nástroje je mezi zdroji investice",
                                    f"`{kde}.nastroj.zdroj_url` není v `{kde}.zdroje`: {url}")
            if doklad == "dolozeno":
                if hodnota not in ("podil", "konvertibilni"):
                    self.pridej(METODIKA, soubor, id_, "doložený nástroj má hodnotu",
                                f"`{kde}`: doklad dolozeno, ale `hodnota` = {hodnota!r}.")
                if not url:
                    self.pridej(METODIKA, soubor, id_, "doložený nástroj má zdroj", f"`{kde}`: dolozeno bez `zdroj_url`.")
                kvalifikuje = bool(url) and hodnota in ("podil", "konvertibilni")
            elif doklad == "neprima_indicie":
                if not url:
                    self.pridej(METODIKA, soubor, id_, "nepřímá indicie má zdroj",
                                f"`{kde}`: neprima_indicie bez `zdroj_url`.")
                kolo_ok = isinstance(kolo, str) and bool(RE_KOLO.match(kolo.strip()))
                kolo_varianta = isinstance(kolo, str) and bool(RE_KOLO_VARIANTA.search(kolo))
                if kolo_varianta and not kolo_ok:
                    self.pridej(UPOZORNENI, soubor, id_, "označení kola u nepřímé indicie",
                                f"`{kde}.nastroj.kolo` = {kolo!r} není kanonické pre-seed/seed/series; "
                                f"započítáno jako seed nebo series kolo, ověř ve zdroji.")
                kvalifikuje = bool(url) and (kolo_ok or kolo_varianta)
                jen_neprima = kvalifikuje
            elif doklad == "nezjisteno":
                if hodnota is not None or url is not None:
                    self.pridej(METODIKA, soubor, id_, "nezjištěný nástroj nemá hodnotu ani zdroj",
                                f"`{kde}`: nezjisteno, ale `hodnota` = {hodnota!r}, `zdroj_url` = {url!r}.")

        zpravy = []
        if not isinstance(inv["zdroje"], list) or not inv["zdroje"]:
            self.pridej(STRUKTURA, soubor, id_, "investice má seznam zdrojů", f"`{kde}.zdroje` je prázdné nebo chybí.")
        else:
            for j, zdroj in enumerate(inv["zdroje"]):
                if self.kontroluj_zdroj(zdroj, DRUH_INV, soubor, id_, f"{kde}.zdroje[{j}]") and \
                        zdroj["druh_zdroje"] == "zprava_o_transakci" and je_url(zdroj["url"]):
                    zpravy.append(zdroj)
        return {
            "kde": kde,
            "rozsah": rozsah,
            "filtr": filtr,
            "zpravy": zpravy,
            "puvody": self.puvody(zpravy),
            "kvalifikuje": kvalifikuje,
            "dolozeno": kvalifikuje and not jen_neprima,
        }

    def v_okne(self, rozsah):
        """True / False / None (výsledek závisí na přesném dni u zkráceného data)."""
        prvni, posledni = rozsah
        if posledni < self.hranice_24 or prvni > self.ref:
            return False
        if prvni >= self.hranice_24:
            return True
        return None

    def kontroluj_okno_a_status(self, zaznam, soubor, id_, investice):
        posledni = investice[0]
        if posledni is None:
            return
        kde = posledni["kde"]
        if not posledni["zpravy"]:
            self.pridej(METODIKA, soubor, id_, "poslední investice má zprávu o transakci",
                        f"`{kde}` nemá zdroj s `druh_zdroje` = zprava_o_transakci.")
        rozsah = posledni["rozsah"]
        if rozsah is None:
            self.pridej(METODIKA, soubor, id_, "datum v okně 24 měsíců",
                        f"`{kde}` nemá použitelné datum podle `datum_pro_filtr`.")
        else:
            okno = self.v_okne(rozsah)
            popis = f"{rozsah[1].isoformat()} (hranice okna {self.hranice_24.isoformat()}, referenční datum {self.ref.isoformat()})"
            if okno is False:
                self.pridej(METODIKA, soubor, id_, "datum v okně 24 měsíců", f"`{kde}`: datum pro filtr {popis} je mimo okno.")
            elif okno is None:
                self.pridej(UPOZORNENI, soubor, id_, "zkrácené datum u hranice okna",
                            f"`{kde}`: výsledek filtru závisí na přesném dni, datum pro filtr {popis}.")

        # Poslední investice má být nejnovější doložená.
        for dalsi in investice[1:]:
            if dalsi and dalsi["rozsah"] and rozsah and dalsi["zpravy"] and dalsi["rozsah"][1] > rozsah[1]:
                self.pridej(METODIKA, soubor, id_, "poslední investice je nejnovější",
                            f"`{dalsi['kde']}` ({dalsi['rozsah'][1].isoformat()}) je novější než "
                            f"`posledni_investice` ({rozsah[1].isoformat()}).")

        status = zaznam.get("status")
        if status not in STATUSY:
            self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `status`", f"`status` = {status!r}.")
        elif rozsah is not None and self.v_okne(rozsah) is not False:
            prvni, posledni_den = rozsah
            if prvni >= self.hranice_12:
                ocekavany = "aktivni"
            elif posledni_den < self.hranice_12:
                ocekavany = "investice_dolozena_12_24_mesicu"
            else:
                ocekavany = None
                self.pridej(UPOZORNENI, soubor, id_, "zkrácené datum u hranice 12 měsíců",
                            f"Status závisí na přesném dni ({rozsah[0].isoformat()} až {posledni_den.isoformat()}, "
                            f"hranice {self.hranice_12.isoformat()}).")
            if ocekavany and status != ocekavany:
                self.pridej(METODIKA, soubor, id_, "status odpovídá datu poslední investice",
                            f"`status` = {status}, podle data {posledni_den.isoformat()} a hranice "
                            f"{self.hranice_12.isoformat()} má být {ocekavany}.")

    def kontroluj_nastroj_a_jistotu(self, zaznam, soubor, id_, investice):
        v_okne = [i for i in investice if i and i["rozsah"] and i["zpravy"] and self.v_okne(i["rozsah"]) is not False]
        kvalifikujici = [i for i in v_okne if i["kvalifikuje"]]
        dolozene = [i for i in v_okne if i["dolozeno"]]
        if not kvalifikujici:
            self.pridej(METODIKA, soubor, id_, "podmínka 3: nástroj",
                        "Žádná investice v okně se zprávou o transakci nemá nástroj dolozeno se `zdroj_url`, "
                        "ani neprima_indicie se `zdroj_url` a kolem pre-seed/seed/series.")

        jistota = zaznam.get("jistota")
        if not self.kontroluj_klice(jistota, ["existence", "investice"], soubor, id_, "jistota"):
            return
        for k in ("existence", "investice"):
            if jistota[k] not in JISTOTY:
                self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `jistota`", f"`jistota.{k}` = {jistota[k]!r}.")
        jist_inv = jistota["investice"]
        if jist_inv == "nizka":
            self.pridej(METODIKA, soubor, id_, "jistota investice u zařazeného záznamu",
                        "`jistota.investice` = nizka; zařazený záznam má jen úrovně vysoka nebo stredni.")
        if jist_inv == "vysoka":
            nezavisle = [i for i in v_okne if len(i["puvody"]) >= 2]
            if not nezavisle:
                self.pridej(METODIKA, soubor, id_, "vysoká jistota vyžaduje dva různé původy",
                            "`jistota.investice` = vysoka, ale žádná investice v okně nemá zprávy o transakci "
                            "aspoň se dvěma různými původy.")
            if not dolozene:
                self.pridej(METODIKA, soubor, id_, "nepřímý nástroj omezuje jistotu",
                            "`jistota.investice` = vysoka, ale žádná investice v okně nemá nástroj dolozeno; "
                            "záznam opírá podmínku 3 jen o neprima_indicie, jistota má být nejvýš stredni.")
        if kvalifikujici and not dolozene:
            self.prehled.setdefault("jen_neprima", []).append(id_)

    def kontroluj_existenci(self, zaznam, soubor, id_):
        ps = zaznam.get("pravni_subjekt")
        if not self.kontroluj_klice(ps, ["hodnota", "ico", "zdroje"], soubor, id_, "pravni_subjekt"):
            return
        if ps["ico"] is not None:
            if not isinstance(ps["ico"], str):
                self.pridej(STRUKTURA, soubor, id_, "IČO je řetězec", f"`pravni_subjekt.ico` = {ps['ico']!r}.")
            elif zaznam.get("zeme") == "CZ" and not re.fullmatch(r"\d{8}", ps["ico"]):
                self.pridej(STRUKTURA, soubor, id_, "české IČO má 8 číslic", f"`pravni_subjekt.ico` = {ps['ico']!r}.")
        druhy = set()
        if not isinstance(ps["zdroje"], list) or not ps["zdroje"]:
            if ps["hodnota"]:
                self.pridej(METODIKA, soubor, id_, "vyplněné pole má zdroj", "`pravni_subjekt` je vyplněný bez zdrojů.")
        else:
            for j, zdroj in enumerate(ps["zdroje"]):
                if self.kontroluj_zdroj(zdroj, DRUH_EXIST, soubor, id_, f"pravni_subjekt.zdroje[{j}]"):
                    druhy.add(zdroj["druh_zdroje"])
        if druhy & {"rejstrik", "regulator"}:
            nejvyssi = "vysoka"
        elif druhy & {"asociace", "media"}:
            nejvyssi = "stredni"
        else:
            nejvyssi = "nizka"
        jistota = (zaznam.get("jistota") or {}).get("existence") if isinstance(zaznam.get("jistota"), dict) else None
        if jistota in PORADI_JISTOTY:
            if PORADI_JISTOTY[jistota] > PORADI_JISTOTY[nejvyssi]:
                self.pridej(METODIKA, soubor, id_, "jistota existence odpovídá zdrojům",
                            f"`jistota.existence` = {jistota}, zdroje ({', '.join(sorted(druhy)) or 'žádné'}) "
                            f"dovolují nejvýš {nejvyssi}.")
            elif PORADI_JISTOTY[jistota] < PORADI_JISTOTY[nejvyssi]:
                self.pridej(UPOZORNENI, soubor, id_, "jistota existence nižší, než dovolují zdroje",
                            f"`jistota.existence` = {jistota}, zdroje ({', '.join(sorted(druhy))}) dovolují {nejvyssi}; "
                            f"v pořádku jen při rozporu zdrojů.")

    def kontroluj_zaznam(self, zaznam):
        soubor = "investori.json"
        id_ = zaznam.get("id") if isinstance(zaznam.get("id"), str) else ""
        self.kontroluj_klice(zaznam, KLICE_ZAZNAMU, soubor, id_, "záznam")
        if id_ and not RE_ID.match(id_):
            self.pridej(STRUKTURA, soubor, id_, "tvar id", "Id neodpovídá tvaru `cz-nazev`.")
        if not isinstance(zaznam.get("nazev"), str) or not zaznam.get("nazev", "").strip():
            self.pridej(STRUKTURA, soubor, id_, "vyplněný název", "`nazev` chybí.")
        typ, zeme = zaznam.get("typ"), zaznam.get("zeme")
        if typ not in TYPY:
            self.pridej(STRUKTURA, soubor, id_, "povolená hodnota `typ`", f"`typ` = {typ!r}.")
        elif typ not in TYPY_PILOT:
            self.pridej(METODIKA, soubor, id_, "pravidla pilotu: typ VC nebo CVC", f"Zařazený záznam má typ {typ}.")
        if not isinstance(zeme, str) or not re.fullmatch(r"[A-Z]{2}", zeme):
            self.pridej(STRUKTURA, soubor, id_, "země je kód ISO 3166-1 alpha-2", f"`zeme` = {zeme!r}.")
        elif zeme != ZEME_PILOT:
            self.pridej(METODIKA, soubor, id_, "pravidla pilotu: sídlo v ČR", f"Zařazený záznam má zemi {zeme}.")
        if not isinstance(zaznam.get("poznamka", ""), str):
            self.pridej(STRUKTURA, soubor, id_, "`poznamka` je text", "`poznamka` není řetězec.")

        self.kontroluj_existenci(zaznam, soubor, id_)

        web = zaznam.get("web")
        if isinstance(web, dict):
            if web.get("hodnota") is not None and not je_url(web["hodnota"]):
                self.pridej(STRUKTURA, soubor, id_, "platná URL", f"`web.hodnota` = {web['hodnota']!r}.")
            self.kontroluj_pole_se_zdrojem(web, "web", soubor, id_, ["hodnota", "zdroj_url", "stazeno"],
                                           bool(web.get("hodnota")))
        else:
            self.pridej(STRUKTURA, soubor, id_, "tvar objektu", "`web` není objekt.")
        for nazev in ("sektory", "faze"):
            pole = zaznam.get(nazev)
            if not isinstance(pole, dict):
                self.pridej(STRUKTURA, soubor, id_, "tvar objektu", f"`{nazev}` není objekt.")
                continue
            hodnota = pole.get("hodnota")
            if hodnota is not None and (not isinstance(hodnota, list) or
                                        not all(isinstance(h, str) and h.strip() for h in hodnota)):
                self.pridej(STRUKTURA, soubor, id_, "seznam textů nebo null", f"`{nazev}.hodnota` = {hodnota!r}.")
            self.kontroluj_pole_se_zdrojem(pole, nazev, soubor, id_, ["hodnota", "zdroj_url", "zdroj_datum", "stazeno"],
                                           bool(hodnota))
        self.kontroluj_ticket(zaznam.get("ticket"), soubor, id_)
        self.kontroluj_kapital(zaznam.get("kapital"), soubor, id_)

        investice = [self.kontroluj_investici(zaznam.get("posledni_investice"), soubor, id_, "posledni_investice")]
        dalsi = zaznam.get("dalsi_investice")
        if not isinstance(dalsi, list):
            self.pridej(STRUKTURA, soubor, id_, "`dalsi_investice` je seznam", "`dalsi_investice` není seznam.")
            dalsi = []
        for i, inv in enumerate(dalsi):
            investice.append(self.kontroluj_investici(inv, soubor, id_, f"dalsi_investice[{i}]"))
        for inv in investice:
            if inv and inv["filtr"] == "oznameni":
                self.prehled["oznameni"] = self.prehled.get("oznameni", 0) + 1
            if inv:
                self.prehled["investic"] = self.prehled.get("investic", 0) + 1
        self.kontroluj_okno_a_status(zaznam, soubor, id_, investice)
        self.kontroluj_nastroj_a_jistotu(zaznam, soubor, id_, investice)

    def kontroluj_duplicity(self):
        """Deduplikace podle IČO, domény webu a normalizovaného názvu (PLAN.md bod 6)."""
        klice = {}
        for nazev, zaznamy in self.vystup.items():
            for z in zaznamy:
                id_ = z.get("id")
                if not isinstance(id_, str):
                    continue
                if nazev == "investori.json":
                    ps = z.get("pravni_subjekt") if isinstance(z.get("pravni_subjekt"), dict) else {}
                    web = (z.get("web") or {}).get("hodnota") if isinstance(z.get("web"), dict) else None
                    if ps.get("ico"):
                        klice.setdefault(("IČO", ps["ico"]), set()).add(id_)
                else:
                    web = z.get("web")
                if je_url(web):
                    klice.setdefault(("doména webu", domena(web)), set()).add(id_)
                jmeno = normalizuj_nazev(z.get("nazev"))
                if jmeno:
                    klice.setdefault(("normalizovaný název", jmeno), set()).add(id_)
        for (druh, hodnota), ids in sorted(klice.items()):
            if len(ids) > 1:
                ids = sorted(ids)
                self.pridej(METODIKA, "data/vystup_agenta", ids[0], "deduplikace",
                            f"Shodná hodnota ({druh} = {hodnota}) u záznamů {', '.join(ids)}; "
                            f"jedna investiční firma = jeden záznam.")

    def zkontroluj_tls(self, url, soubor, id_, kde):
        d = domena(url)
        if not any(d == x or d.endswith("." + x) for x in NEPLATNY_CERTIFIKAT):
            return
        if any(id_ == i and (d == x or d.endswith("." + x)) for i, x in STAZENO_BEZ_TLS):
            self.pridej(UPOZORNENI, soubor, id_, "zdroj stažený bez ověření TLS",
                        f"`{kde}`: {url} byl v kroku 2 stažen přes `curl -k` (bez ověření certifikátu); "
                        f"obsah nemusí pocházet z pravého webu, ověř zdroj.")
        else:
            self.pridej(UPOZORNENI, soubor, id_, "zdroj na doméně s neplatným certifikátem",
                        f"`{kde}`: {url}; doména má neplatný certifikát TLS a způsob stažení není zapsaný, ověř zdroj.")

    # ---------- URL ----------

    def over_url(self, timeout=15, vlakna=8):
        def stahni(url):
            pozadavek = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (kontrola dostupnosti zdroje)"})
            try:
                with urllib.request.urlopen(pozadavek, timeout=timeout) as odpoved:
                    return url, odpoved.status, None
            except urllib.error.HTTPError as chyba:
                return url, chyba.code, None
            except Exception as chyba:  # síť, DNS, TLS, timeout
                return url, None, f"{type(chyba).__name__}: {str(chyba)[:120]}"

        with ThreadPoolExecutor(max_workers=vlakna) as pool:
            vysledky = sorted(pool.map(stahni, sorted(self.urls)))
        ok = 0
        for url, kod, chyba in vysledky:
            if kod == 200:
                ok += 1
                continue
            popis = f"HTTP {kod}" if kod else chyba
            for soubor, id_ in sorted(self.urls[url]):
                self.pridej(UPOZORNENI, soubor, id_, "dostupnost URL",
                            f"{url} → {popis}. Neúspěšné stažení nedokazuje, že údaj je nepravdivý; zkontroluj ručně.")
        self.prehled["url"] = {"celkem": len(vysledky), "http_200": ok, "jinak": len(vysledky) - ok}

    # ---------- běh ----------

    def spust(self, over_url=False):
        self.nacti()
        self.kontroluj_pokryti()
        self.kontroluj_csv()
        for zaznam in self.vystup["investori.json"]:
            self.kontroluj_zaznam(zaznam)
        self.kontroluj_duplicity()
        if over_url:
            self.over_url()
        self.nalezy = sorted(set(self.nalezy), key=lambda n: (list(KATEGORIE).index(n.kategorie), n.soubor, n.id,
                                                               n.pravidlo, n.detail))
        return self.nalezy


def bunka(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def zprava(kontrola, over_url, vstupy):
    n = kontrola.nalezy
    pocty = {k: sum(1 for x in n if x.kategorie == k) for k in KATEGORIE}
    p = kontrola.prehled
    radky = [
        "# Automatická kontrola výstupu agenta",
        "",
        "Vygenerováno skriptem `scripts/zkontroluj_data.py` (PLAN.md, bod 6 „Automaticky (skript)“). "
        "Kontrola jen čte, původní data neopravuje. Neověřuje, jestli zdroje opravdu dokládají údaje: "
        "to je úkol kontroly druhým agentem a ruční kontroly.",
        "",
        "## Parametry",
        "",
        f"- referenční datum: {kontrola.ref.isoformat()}",
        f"- okno 24 měsíců: od {kontrola.hranice_24.isoformat()} do {kontrola.ref.isoformat()} včetně",
        f"- hranice statusu `aktivni`: datum pro filtr od {kontrola.hranice_12.isoformat()} včetně",
        f"- kontrola dostupnosti URL: {'ano' if over_url else 'ne (spusť s `--over-url`)'}",
        f"- příkaz: `python3 scripts/zkontroluj_data.py --datum {kontrola.ref.isoformat()}"
        f"{' --over-url' if over_url else ''}`",
        "- opakovatelnost: při stejném referenčním datu a stejných vstupech (otisky níže) dají kontroly stejný "
        "výsledek; jen výsledek kontroly URL závisí na době běhu a stavu webů",
        "",
        "Vstupní soubory (SHA-256, prvních 12 znaků):",
        "",
    ]
    radky += [f"- `{cesta}`: {otisk}" for cesta, otisk in vstupy]
    radky += [
        "",
        "## Souhrn",
        "",
        "| Kategorie | Nálezů | Záznamů |",
        "|---|---|---|",
    ]
    for k, nadpis in KATEGORIE.items():
        zaznamy = {(x.soubor, x.id) for x in n if x.kategorie == k}
        radky.append(f"| {nadpis} | {pocty[k]} | {len(zaznamy)} |")
    radky += [
        "",
        "- **Chyba struktury:** soubor nebo pole neodpovídá schématu z PLAN.md (klíče, typy, povolené hodnoty, "
        "chybějící nebo zdvojený výsledek kandidáta).",
        "- **Metodický nesoulad:** tvar je správný, ale údaj odporuje pravidlům plánu (okno 24 měsíců, status, "
        "nástroj, jistota, pravidla pilotu, zdroj u vyplněného pole).",
        "- **Upozornění:** pravidlo porušené není, ale zdroj nebo údaj je potřeba zkontrolovat ručně.",
        "",
        "### Pokrytí vstupních id",
        "",
    ]
    pok = p.get("pokryti", {})
    radky.append(f"Vstupních id v `data/kandidati.csv`: {pok.get('vstupnich_id', 0)}, "
                 f"v `mapovani_id.csv`: {pok.get('v_mapovani', 0)}.")
    radky += ["", "| Výsledek | Podle mapování | Záznamů ve výstupu |", "|---|---|---|"]
    for soubor in SOUBORY_VYSTUPU + (SLOUCENO,):
        radky.append(f"| {soubor} | {pok.get('podle_mapovani', {}).get(soubor, 0)} | "
                     f"{pok.get('ve_vystupu', {}).get(soubor, '–') if soubor != SLOUCENO else '–'} |")
    chyby_pokryti = [x for x in n if x.pravidlo in (
        "pokrytí všech vstupních id", "jeden výsledek na kandidáta", "mapování odpovídá výstupu",
        "id pochází z kandidati.csv", "sloučené id nemá vlastní výsledek", "sloučení míří na zpracovaný záznam")]
    radky += ["", "Pokrytí je úplné: každé vstupní id má právě jeden výsledek nebo je sloučené do zpracovaného záznamu."
              if not chyby_pokryti else f"Pokrytí má {len(chyby_pokryti)} chyb, viz Chyby struktury."]
    radky += [
        "",
        "### Přehledy pro ruční kontrolu",
        "",
        f"- Investic v `investori.json` (poslední i další): {p.get('investic', 0)}, z toho s "
        f"`datum_pro_filtr` = oznameni: {p.get('oznameni', 0)} (PLAN.md bod 4: tyto záznamy mají jít spočítat "
        f"a zvlášť zkontrolovat).",
    ]
    jen_neprima = p.get("jen_neprima", [])
    radky.append(f"- Zařazené záznamy, které opírají podmínku 3 jen o `neprima_indicie` "
                 f"(pracovní předpoklad, jistota nejvýš `stredni`): {len(jen_neprima)}"
                 + (f" ({', '.join(jen_neprima)})." if jen_neprima else "."))
    if over_url:
        u = p.get("url", {})
        radky.append(f"- URL zkontrolováno: {u.get('celkem', 0)}, HTTP 200: {u.get('http_200', 0)}, "
                     f"jinak: {u.get('jinak', 0)}. HTTP 200 znamená jen, že stránka odpověděla, ne že údaj sedí. "
                     f"Neúspěšné stažení nedokazuje, že údaj je nepravdivý.")
    for k, nadpis in KATEGORIE.items():
        radky += ["", f"## {nadpis} ({pocty[k]})", ""]
        vyber = [x for x in n if x.kategorie == k]
        if not vyber:
            radky.append("Žádné.")
            continue
        radky += ["| Soubor | Id | Pravidlo | Detail |", "|---|---|---|---|"]
        radky += [f"| {bunka(x.soubor)} | {bunka(x.id)} | {bunka(x.pravidlo)} | {bunka(x.detail)} |" for x in vyber]
    radky += [
        "",
        "## Co kontrola neověřuje",
        "",
        "- jestli zdroj opravdu dokládá údaj v poli (firma, datum, částka, typ, nástroj),",
        "- jestli jsou zdroje uvedené s různým `puvod` opravdu nezávislé; skript porovnává jen zapsané hodnoty,",
        "- správnost typu, sídla a rozhodnutí u vyřazených, hraničních a nevyřešených kandidátů "
        "(u nich kontroluje jen tvar, povolené hodnoty, důvod a zdroj),",
        "- stažení bez ověření TLS zná jen z logu kroku 2 (seznam `STAZENO_BEZ_TLS` ve skriptu); "
        "ostatní zdroje na doméně s neplatným certifikátem označuje obecně.",
        "",
    ]
    return "\n".join(radky)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--datum", default=VYCHOZI_DATUM, help=f"referenční datum (výchozí {VYCHOZI_DATUM})")
    parser.add_argument("--over-url", action="store_true", help="ověřit dostupnost všech URL (pomalé, síť)")
    parser.add_argument("--koren", default=str(ROOT), help="kořen projektu")
    parser.add_argument("--vystup", default=None, help="cesta ke zprávě (výchozí ai-log/03-kontrola/automaticka_kontrola.md)")
    args = parser.parse_args(argv)

    koren = Path(args.koren)
    kontrola = Kontrola(koren, date.fromisoformat(args.datum))
    kontrola.spust(over_url=args.over_url)
    vstupy = []
    for nazev in ("kandidati.csv", "mapovani_id.csv") + SOUBORY_VYSTUPU:
        cesta = kontrola.cesta(nazev)
        if cesta.exists():
            vstupy.append((cesta.relative_to(koren).as_posix(), sha256(cesta)))
    vystup = Path(args.vystup) if args.vystup else koren / "ai-log" / "03-kontrola" / "automaticka_kontrola.md"
    vystup.parent.mkdir(parents=True, exist_ok=True)
    vystup.write_text(zprava(kontrola, args.over_url, vstupy), encoding="utf-8")

    pocty = {k: sum(1 for x in kontrola.nalezy if x.kategorie == k) for k in KATEGORIE}
    print(f"Zpráva: {vystup}")
    for k, nadpis in KATEGORIE.items():
        print(f"  {nadpis}: {pocty[k]}")
    return 1 if pocty[STRUKTURA] else 0


if __name__ == "__main__":
    sys.exit(main())
