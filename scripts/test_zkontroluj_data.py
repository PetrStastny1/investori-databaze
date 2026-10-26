"""Testy scripts/zkontroluj_data.py na malých umělých datech.

Spuštění: python3 -m unittest scripts/test_zkontroluj_data.py

Každý test vezme platný minimální projekt (3 kandidáti: jeden zařazený, jeden vyřazený,
jeden sloučený) a podstrčí do něj jednu skutečnou chybu. Ověřuje, že ji kontrola zachytí
ve správné kategorii.
"""
import copy
import csv
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import zkontroluj_data as zk  # noqa: E402

REF = date(2026, 10, 26)
STAZENO = "2026-10-26"


def zdroj(url, druh, puvod=None, datum="2026-03-12"):
    return {"url": url, "druh_zdroje": druh, "vydavatel": "test", "puvod": puvod,
            "zdroj_datum": datum, "stazeno": STAZENO}


ZAZNAM = {
    "id": "cz-alfa-ventures",
    "nazev": "Alfa Ventures",
    "typ": "VC",
    "zeme": "CZ",
    "pravni_subjekt": {"hodnota": "Alfa Ventures s.r.o.", "ico": "12345678",
                       "zdroje": [zdroj("https://ares.gov.cz/x/12345678", "rejstrik")]},
    "web": {"hodnota": "https://alfa.example/", "zdroj_url": "https://alfa.example/", "stazeno": STAZENO},
    "sektory": {"hodnota": ["software"], "zdroj_url": "https://alfa.example/", "zdroj_datum": None, "stazeno": STAZENO},
    "faze": {"hodnota": None, "zdroj_url": None, "zdroj_datum": None, "stazeno": None},
    "ticket": {"min": 100000, "max": 500000, "mena": "EUR", "zdroj_url": "https://alfa.example/",
               "zdroj_datum": None, "stazeno": STAZENO},
    "kapital": [{"castka": 50000000, "mena": "EUR", "plati_k": "2026-01-01", "druh": "fund_size", "fond": "Alfa I",
                 "zdroj_url": "https://alfa.example/fond", "zdroj_datum": "2026-01-05", "stazeno": STAZENO}],
    "posledni_investice": {
        "firma": "Beta s.r.o.", "datum_investice": None, "datum_oznameni": "2026-03-12", "datum_pro_filtr": "oznameni",
        "nastroj": {"hodnota": None, "doklad": "neprima_indicie", "kolo": "seed",
                    "zdroj_url": "https://cc.example/beta"},
        "zdroje": [zdroj("https://cc.example/beta", "zprava_o_transakci"),
                   zdroj("https://forbes.example/beta", "zprava_o_transakci")],
    },
    "dalsi_investice": [],
    "status": "aktivni",
    "jistota": {"existence": "vysoka", "investice": "stredni"},
    "poznamka": "",
}

KANDIDATI = [
    {"id": "cz-alfa-ventures", "nazev": "Alfa Ventures", "web": "https://alfa.example/"},
    {"id": "cz-gama-capital", "nazev": "Gama Capital", "web": "https://gama.example/"},
    {"id": "cz-alfa-stara", "nazev": "Alfa Stará", "web": "https://alfa-stara.example/"},
]
VYRAZENI = [{"id": "cz-gama-capital", "nazev": "Gama Capital", "web": "https://gama.example/",
             "kategorie": "mimo_rozsah_pilotu", "duvod": "Typ PE.", "zdroj_url": "https://gama.example/",
             "stazeno": STAZENO}]
MAPOVANI = [
    {"id": "cz-alfa-ventures", "vysledne_id": "cz-alfa-ventures", "soubor": "investori.json", "davka": "1", "poznamka": ""},
    {"id": "cz-gama-capital", "vysledne_id": "cz-gama-capital", "soubor": "vyrazeni.csv", "davka": "1", "poznamka": ""},
    {"id": "cz-alfa-stara", "vysledne_id": "cz-alfa-ventures", "soubor": "slouceno", "davka": "1",
     "poznamka": "Přejmenování, https://cc.example/prejmenovani"},
]


def zapis_csv(cesta, sloupce, radky):
    cesta.parent.mkdir(parents=True, exist_ok=True)
    with cesta.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=sloupce)
        w.writeheader()
        for r in radky:
            w.writerow({k: r.get(k, "") for k in sloupce})


class TestKontrola(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.koren = Path(self.tmp.name)
        self.zaznamy = [copy.deepcopy(ZAZNAM)]
        self.kandidati = copy.deepcopy(KANDIDATI)
        self.vyrazeni = copy.deepcopy(VYRAZENI)
        self.mapovani = copy.deepcopy(MAPOVANI)

    def tearDown(self):
        self.tmp.cleanup()

    def spust(self):
        k = self.koren
        zapis_csv(k / "data" / "kandidati.csv", zk.SLOUPCE["kandidati.csv"],
                  [dict(r, zdroj_seznamu="test", zdroj_url=r["web"], stazeno=STAZENO) for r in self.kandidati])
        zapis_csv(k / "ai-log" / "02-obohaceni" / "mapovani_id.csv", zk.SLOUPCE["mapovani_id.csv"], self.mapovani)
        vystup = k / "data" / "vystup_agenta"
        zapis_csv(vystup / "vyrazeni.csv", zk.SLOUPCE["vyrazeni.csv"], self.vyrazeni)
        zapis_csv(vystup / "hranicni.csv", zk.SLOUPCE["hranicni.csv"], [])
        zapis_csv(vystup / "nevyresene.csv", zk.SLOUPCE["nevyresene.csv"], [])
        (vystup / "investori.json").write_text(json.dumps(self.zaznamy, ensure_ascii=False), encoding="utf-8")
        return zk.Kontrola(k, REF, ocekavany_pocet=len(self.kandidati)).spust()

    def najdi(self, nalezy, kategorie, pravidlo, id_=None):
        return [n for n in nalezy if n.kategorie == kategorie and n.pravidlo == pravidlo
                and (id_ is None or n.id == id_)]

    def test_platna_data_bez_chyb(self):
        nalezy = self.spust()
        chyby = [n for n in nalezy if n.kategorie in (zk.STRUKTURA, zk.METODIKA)]
        self.assertEqual(chyby, [])

    def test_chybejici_id(self):
        self.vyrazeni = []  # cz-gama-capital zmizí z výstupu, mapování ho dál uvádí
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.STRUKTURA, "pokrytí všech vstupních id", "cz-gama-capital"))

    def test_chybejici_id_i_v_mapovani(self):
        self.vyrazeni = []
        self.mapovani = [m for m in self.mapovani if m["id"] != "cz-gama-capital"]
        nalezy = self.spust()
        detaily = [n.detail for n in self.najdi(nalezy, zk.STRUKTURA, "pokrytí všech vstupních id", "cz-gama-capital")]
        self.assertIn("Id chybí v mapování.", detaily)
        self.assertTrue(any(d.startswith("Chybí výsledek") for d in detaily))

    def test_duplicitni_vysledek(self):
        self.vyrazeni.append(dict(self.vyrazeni[0], id="cz-alfa-ventures", nazev="Alfa Ventures"))
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.STRUKTURA, "jeden výsledek na kandidáta", "cz-alfa-ventures"))

    def test_slouceny_kandidat_s_vlastnim_vysledkem(self):
        self.vyrazeni.append(dict(self.vyrazeni[0], id="cz-alfa-stara", nazev="Alfa Stará"))
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.STRUKTURA, "sloučené id nemá vlastní výsledek", "cz-alfa-stara"))

    def test_datum_mimo_okno(self):
        inv = self.zaznamy[0]["posledni_investice"]
        inv["datum_oznameni"] = "2024-10-25"  # den před hranicí okna 2024-10-26
        for z in inv["zdroje"]:
            z["zdroj_datum"] = "2024-10-25"
        self.zaznamy[0]["status"] = "investice_dolozena_12_24_mesicu"
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.METODIKA, "datum v okně 24 měsíců", "cz-alfa-ventures"))

    def test_datum_na_hranici_okna_projde(self):
        inv = self.zaznamy[0]["posledni_investice"]
        inv["datum_oznameni"] = "2024-10-26"
        self.zaznamy[0]["status"] = "investice_dolozena_12_24_mesicu"
        nalezy = self.spust()
        self.assertFalse(self.najdi(nalezy, zk.METODIKA, "datum v okně 24 měsíců"))

    def test_zkracene_datum_u_hranice_je_upozorneni(self):
        self.zaznamy[0]["posledni_investice"]["datum_oznameni"] = "2024-10"
        self.zaznamy[0]["status"] = "investice_dolozena_12_24_mesicu"
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.UPOZORNENI, "zkrácené datum u hranice okna", "cz-alfa-ventures"))
        self.assertFalse(self.najdi(nalezy, zk.METODIKA, "datum v okně 24 měsíců"))

    def test_nesouhlasny_status(self):
        self.zaznamy[0]["status"] = "investice_dolozena_12_24_mesicu"  # oznámení 2026-03-12 je v posledních 12 měsících
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.METODIKA, "status odpovídá datu poslední investice", "cz-alfa-ventures"))

    def test_neprima_indicie_s_vysokou_jistotou(self):
        # Dvě zprávy s různým původem by jinak pro „vysoka“ stačily, nástroj je ale jen nepřímá indicie.
        self.zaznamy[0]["jistota"]["investice"] = "vysoka"
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.METODIKA, "nepřímý nástroj omezuje jistotu", "cz-alfa-ventures"))
        self.assertFalse(self.najdi(nalezy, zk.METODIKA, "vysoká jistota vyžaduje dva různé původy"))

    def test_vysoka_jistota_se_stejnym_puvodem(self):
        inv = self.zaznamy[0]["posledni_investice"]
        inv["nastroj"].update(hodnota="podil", doklad="dolozeno", kolo=None)
        for z in inv["zdroje"]:
            z["puvod"] = "https://alfa.example/tiskova-zprava"
        self.zaznamy[0]["jistota"]["investice"] = "vysoka"
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.METODIKA, "vysoká jistota vyžaduje dva různé původy", "cz-alfa-ventures"))

    def test_ticket_min_vetsi_nez_max(self):
        self.zaznamy[0]["ticket"].update(min=1000000, max=500000)
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.METODIKA, "ticket min <= max", "cz-alfa-ventures"))

    def test_zdroj_bez_overeni_tls(self):
        self.kandidati.append({"id": "cz-thein", "nazev": "Thein", "web": "https://thein.example/"})
        self.mapovani.append({"id": "cz-thein", "vysledne_id": "cz-thein", "soubor": "vyrazeni.csv", "davka": "6",
                              "poznamka": ""})
        self.vyrazeni.append(dict(self.vyrazeni[0], id="cz-thein", nazev="Thein", web="https://thein.example/",
                                  zdroj_url="https://cvca.cz/en/thein-2/"))
        nalezy = self.spust()
        self.assertTrue(self.najdi(nalezy, zk.UPOZORNENI, "zdroj stažený bez ověření TLS", "cz-thein"))


if __name__ == "__main__":
    unittest.main()
