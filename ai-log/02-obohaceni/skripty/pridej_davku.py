"""Zkontroluje výsledky pomocných agentů pro jednu dávku a připíše je do data/vystup_agenta/.

Použití: python3 pridej_davku.py <adresar_vysledku> <cislo_davky> <id> [<id> ...]
         python3 pridej_davku.py <adresar_vysledku> <cislo_davky> --jen-kontrola <id> ...

Kontroly jsou jen formální (povolené hodnoty, zdroje, okno 24 měsíců, nástroj, jistota).
Obsah zdrojů nekontrolují.
"""
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
OUT = REPO / "data" / "vystup_agenta"
MAPA = REPO / "ai-log" / "02-obohaceni" / "mapovani_id.csv"
OKNO_24 = "2024-10-26"
OKNO_12 = "2025-10-26"
TYPY = {"VC", "CVC", "PE", "Family office", "Angel", "Velký soukromý investor",
        "Korporátní investor bez samostatné jednotky"}
DRUH_EXIST = {"rejstrik", "regulator", "asociace", "media", "web_subjektu"}
DRUH_INV = {"zprava_o_transakci", "portfolio_web", "rejstrik_spolecnik"}
SLOUPCE = {
    "vyrazen": ("vyrazeni.csv", ["id", "nazev", "web", "kategorie", "duvod", "zdroj_url", "stazeno"]),
    "hranicni": ("hranicni.csv", ["id", "nazev", "web", "druh", "duvod", "zdroj_url", "stazeno"]),
    "nevyresene": ("nevyresene.csv", ["id", "nazev", "web", "otazka", "moznosti", "duvod", "zdroj_url", "stazeno"]),
}


def konec_obdobi(d):
    if len(d) == 4:
        return d + "-12-31"
    if len(d) == 7:
        return d + "-31" if d[5:] in ("01", "03", "05", "07", "08", "10", "12") else d + ("-28" if d[5:] == "02" else "-30")
    return d


def datum_filtru(inv):
    d = inv.get("datum_investice") if inv.get("datum_pro_filtr") == "investice" else inv.get("datum_oznameni")
    return konec_obdobi(d) if d else None


def kontrola_investice(inv, chyby, kde):
    if inv.get("datum_pro_filtr") not in ("investice", "oznameni"):
        chyby.append(f"{kde}: datum_pro_filtr")
    if inv.get("datum_pro_filtr") == "investice" and not inv.get("datum_investice"):
        chyby.append(f"{kde}: datum_pro_filtr=investice bez datum_investice")
    n = inv.get("nastroj") or {}
    if n.get("doklad") not in ("dolozeno", "neprima_indicie", "nezjisteno"):
        chyby.append(f"{kde}: nastroj.doklad")
    if n.get("doklad") == "nezjisteno" and (n.get("hodnota") or n.get("zdroj_url")):
        chyby.append(f"{kde}: nezjisteno s hodnotou nebo zdrojem")
    if n.get("hodnota") not in ("podil", "konvertibilni", None):
        chyby.append(f"{kde}: nastroj.hodnota")
    zdroje = inv.get("zdroje") or []
    if not zdroje:
        chyby.append(f"{kde}: bez zdrojů")
    for z in zdroje:
        if not isinstance(z, dict) or not z.get("url") or z.get("druh_zdroje") not in DRUH_INV:
            chyby.append(f"{kde}: neplatný zdroj {z}")


def nastroj_splnen(inv):
    n = inv.get("nastroj") or {}
    if n.get("doklad") == "dolozeno" and n.get("zdroj_url"):
        return True
    kolo = (n.get("kolo") or "").lower()
    return (n.get("doklad") == "neprima_indicie" and n.get("zdroj_url")
            and any(k in kolo for k in ("pre-seed", "seed", "series")))


def kontrola_zaznamu(z):
    chyby = []
    for pole in ("pravni_subjekt", "web", "sektory", "faze", "ticket", "posledni_investice", "jistota"):
        if not isinstance(z.get(pole), dict):
            chyby.append(f"{pole}: má být objekt podle schématu")
    for pole in ("kapital", "dalsi_investice"):
        if not isinstance(z.get(pole), list):
            chyby.append(f"{pole}: má být seznam")
    if chyby:
        return chyby
    if z.get("typ") not in ("VC", "CVC"):
        chyby.append(f"zařazen s typem {z.get('typ')}")
    if z.get("zeme") != "CZ":
        chyby.append(f"zařazen se zemí {z.get('zeme')}")
    for z2 in z["pravni_subjekt"].get("zdroje") or []:
        if z2.get("druh_zdroje") not in DRUH_EXIST or not z2.get("url"):
            chyby.append(f"pravni_subjekt: neplatný zdroj {z2}")
    for pole in ("web", "sektory", "faze"):
        p = z.get(pole) or {}
        if p.get("hodnota") and not p.get("zdroj_url"):
            chyby.append(f"{pole}: hodnota bez zdroj_url")
    t = z.get("ticket") or {}
    if (t.get("min") is not None or t.get("max") is not None) and not (t.get("zdroj_url") and t.get("mena")):
        chyby.append("ticket bez zdroje nebo měny")
    for k in z.get("kapital") or []:
        if k.get("druh") not in ("aum", "committed_capital", "fund_size") or not k.get("zdroj_url") \
                or not isinstance(k.get("castka"), (int, float)) or not k.get("mena"):
            chyby.append(f"kapital: neplatná položka {k}")
    investice = [z["posledni_investice"]] + (z.get("dalsi_investice") or [])
    for i, inv in enumerate(investice):
        kontrola_investice(inv, chyby, f"investice[{i}] {inv.get('firma')}")
    p = z["posledni_investice"]
    df = datum_filtru(p)
    if not df or df < OKNO_24:
        chyby.append(f"poslední investice mimo okno 24 měsíců ({df})")
    if not any(s.get("druh_zdroje") == "zprava_o_transakci" for s in p.get("zdroje") or []):
        chyby.append("poslední investice bez zprávy o transakci")
    novejsi = [datum_filtru(i) for i in investice if datum_filtru(i)]
    if novejsi and max(novejsi) != df:
        chyby.append("posledni_investice není nejnovější z uvedených")
    status = "aktivni" if df and df >= OKNO_12 else "investice_dolozena_12_24_mesicu"
    if z.get("status") != status:
        chyby.append(f"status {z.get('status')}, podle data má být {status}")
    if not any(nastroj_splnen(i) for i in investice):
        chyby.append("žádná investice nesplňuje podmínku 3 (nástroj)")
    if not any((i.get("nastroj") or {}).get("doklad") == "dolozeno" for i in investice) \
            and z["jistota"].get("investice") != "stredni":
        chyby.append("bez doloženého nástroje musí být jistota.investice stredni")
    if z["jistota"].get("investice") == "vysoka":
        puvody = {s.get("puvod") or s.get("url") for s in p["zdroje"] if s.get("druh_zdroje") == "zprava_o_transakci"}
        if len(puvody) < 2:
            chyby.append("jistota.investice vysoka bez dvou původů")
    if z["jistota"].get("existence") not in ("vysoka", "stredni", "nizka") \
            or z["jistota"].get("investice") not in ("vysoka", "stredni"):
        chyby.append("jistota: nepovolená hodnota")
    return chyby


def main():
    args = sys.argv[1:]
    adresar, davka = Path(args[0]), args[1]
    jen_kontrola = "--jen-kontrola" in args
    ids = [a for a in args[2:] if a != "--jen-kontrola"]
    vysledky, vse_ok = [], True
    for i in ids:
        v = json.loads((adresar / f"{i}.json").read_text())
        chyby = []
        if v.get("id") != i:
            chyby.append("id nesouhlasí")
        if v["vysledek"] == "zarazen":
            chyby += kontrola_zaznamu(v["zaznam"])
        elif v["vysledek"] in SLOUPCE:
            _, sloupce = SLOUPCE[v["vysledek"]]
            if set(v["radek"]) != set(sloupce):
                chyby.append(f"sloupce {sorted(v['radek'])}")
            if v["vysledek"] == "vyrazen" and v["radek"].get("kategorie") not in ("neni_investor", "mimo_rozsah_pilotu"):
                chyby.append("kategorie")
            if not v["radek"].get("zdroj_url"):
                chyby.append("řádek bez zdroj_url")
        elif v["vysledek"] != "slouceno" or not v.get("slouceno_do"):
            chyby.append(f"neznámý výsledek {v['vysledek']}")
        print(f"{i}: {v['vysledek']}" + ("" if not chyby else "  CHYBY: " + "; ".join(chyby)))
        vse_ok &= not chyby
        vysledky.append(v)
    if jen_kontrola or not vse_ok:
        sys.exit(0 if vse_ok else 1)

    zaznamy = json.loads((OUT / "investori.json").read_text())
    with MAPA.open("a", newline="") as fm:
        mapa = csv.writer(fm)
        for v in vysledky:
            if v["vysledek"] == "zarazen":
                zaznamy.append(v["zaznam"])
                mapa.writerow([v["id"], v["id"], "investori.json", davka, ""])
            elif v["vysledek"] == "slouceno":
                mapa.writerow([v["id"], v["slouceno_do"], "slouceno", davka, v["shrnuti"]])
            else:
                soubor, sloupce = SLOUPCE[v["vysledek"]]
                with (OUT / soubor).open("a", newline="") as f:
                    csv.writer(f).writerow([v["radek"][s] for s in sloupce])
                mapa.writerow([v["id"], v["id"], soubor, davka, ""])
    with (OUT / "investori.json").open("w") as f:
        json.dump(zaznamy, f, ensure_ascii=False, indent=2)
        f.write("\n")


if __name__ == "__main__":
    main()
