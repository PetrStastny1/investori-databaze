"""Odhad nákladů na databázi investorů pro celý svět (krok 7, PLAN.md bod 10).

Čte jen ai-log/07-naklady/spotreba.csv (agregovanou spotřebu pilotu ze scripts/spotreba_z_logu.py),
nic dalšího. Bez síťových přístupů, deterministický. Výstup: ai-log/07-naklady/vypocet.md
a totéž na stdout. Všechny předpoklady jsou v parametrech níže; naměřené hodnoty jsou označené.

Spuštění z kořene repa: python3 scripts/naklady.py
"""
import csv
import math
from collections import defaultdict
from pathlib import Path

koren = Path(__file__).resolve().parent.parent
SPOTREBA = koren / "ai-log" / "07-naklady" / "spotreba.csv"
VYSTUP = koren / "ai-log" / "07-naklady" / "vypocet.md"

# ---------------------------------------------------------------- ceník (dohledaný)
# USD za milion tokenů. Zdroj: https://platform.claude.com/docs/en/about-claude/pricing
# (přesměrováno z docs.claude.com), načteno 27. 10. 2026. inference_geo v logu je „global“,
# násobek 1,1 za US-only se proto nepoužije.
CENIK = {
    "claude-opus-5-5": {"input_tokens": 4.00, "cache_creation_5m": 5.00, "cache_creation_1h": 8.00,
                        "cache_read_input_tokens": 0.20, "output_tokens": 20.00},
}
CENA_WEB_SEARCH = 10.00 / 1000  # USD za vyhledávání, týž ceník; WebFetch bez příplatku

# ---------------------------------------------------------------- naměřeno v pilotu
KANDIDATU = 56  # výsledných kandidátů (57 vstupních, Nation1 sloučeno do N1 Ventures)
ZARAZENYCH = 27
NEVYRESENYCH_A_HRANICNICH = 11 + 1  # README, výsledek agenta před ruční kontrolou
RUCNE_KONTROLOVANYCH = 20
SPRAVNOST_POSLEDNI_INVESTICE = 15 / 19  # data/mereni_vzorku.md

# Fáze pilotu → kroky ve spotreba.csv. Režie = jednorázová práce na metodice.
FAZE = [
    ("sběr kandidátů", ["01"]),
    ("obohacení", ["02"]),
    ("automatická kontrola", ["03"]),
    ("kontrola druhým agentem", ["04"]),
    ("ruční kontrola: podpora AI v Claude Code", ["05"]),
    ("režie: plán, zkušební dávka a úprava pravidel, měření", ["00", "02z", "06"]),
]
# Čas fáze v sekundách. Z mereni.txt, kde je naměřený; jinak None = rozpětí volání v logu.
CAS_MERENI = {
    "02": 62 * 60 + 30,  # součet dob 6 dávek, ai-log/02-obohaceni/mereni.txt
    "04": 13 * 60 + 51 + 10 * 60 + 41,  # fáze A 18:30:18–18:44:09, fáze B 18:44:13–18:54:54 CET
}
# Webové požadavky z mereni.txt. None = neměřeno.
WEB = {
    "01": None,  # README uvádí jen „zhruba 120“ požadavků na funding.tech.eu, ostatní neměřeny
    "02": {"WebSearch": 318, "WebFetch": 446 + 1, "ARES": 225, "funding.tech.eu": 85, "curl": 46},
    "02z": {"WebSearch": 9, "WebFetch": 20, "ARES": 11, "funding.tech.eu": 11},
    "03": None, "05": None, "06": None, "00": None,
    "04": {"WebSearch": 24 + 10, "WebFetch": 3 + 2, "curl": 385 + 21},
}
RUCNI_MIN_NA_FIRMU = (10, 15)  # MODELOVÝ PŘEDPOKLAD s asistencí AI, ne naměřený čas

# ---------------------------------------------------------------- předpoklady pro svět
# Zařazení podle PLAN.md bod 8.2, po typech (nízká / střední = středy rozpětí / vysoká).
ZARAZENI_PO_TYPECH = {
    "nízká": {"VC": 2400, "PE": 2800, "family office": 400},
    "střední": {"VC": 4000, "PE": 3500, "family office": 800},
    "vysoká": {"VC": 5600, "PE": 4200, "family office": 1200},
}
# Kandidátů na zařazený záznam: pilotní poměr 56/27, jen pracovní předpoklad.
POMER_KANDIDATU = KANDIDATU / ZARAZENYCH
CITLIVOST_POMERU = [0.5, 1.0, 2.0]
VARIANTY = {
    # nasobek_ai: tokeny na kandidáta mimo ČR vůči pilotu (jazyky, rejstříky bez API, méně médií)
    # nasobek_clovek: čas ruční kontroly vůči ČR (cizí jazyky a rejstříky)
    # vrstvy: 1 = jeden vzorek pro celou databázi, 3 = zvlášť VC, PE, family office
    # adaptaci: kolikrát se opakuje režie metodiky (nové typy investorů, jazykové oblasti)
    # podil_aktualizace: tokeny čtvrtletního přepočtu poslední investice vůči obohacení
    # min_posledni_investice: ruční kontrola jediného pole za čtvrtletí, min na záznam
    "nízká": dict(nasobek_ai=1.0, nasobek_clovek=1.0, min_na_firmu=10.0, vrstvy=3, adaptaci=5,
                  podil_aktualizace=0.20, min_posledni_investice=3.0),
    "střední": dict(nasobek_ai=1.5, nasobek_clovek=1.25, min_na_firmu=12.5, vrstvy=3, adaptaci=10,
                    podil_aktualizace=0.35, min_posledni_investice=4.0),
    "vysoká": dict(nasobek_ai=2.5, nasobek_clovek=1.5, min_na_firmu=15.0, vrstvy=3, adaptaci=20,
                   podil_aktualizace=0.50, min_posledni_investice=5.0),
}
Z = 1.959964  # 95 %
PRESNOST_VZORKU = 0.05  # ±5 p. b.
CTVRTLETI_ROCNE = 4
# Hodinová sazba člověka v USD: MODELOVÝ PŘEDPOKLAD, ne zjištěná tržní cena.
SAZBA_USD_H = 25.0

POLE = ["input_tokens", "cache_creation_5m", "cache_creation_1h", "cache_read_input_tokens",
        "output_tokens"]


def cislo(x, des=0):
    s = f"{x:,.{des}f}".replace(",", " ").replace(".", ",")
    return s


def usd(x):
    return "$" + cislo(x, 2 if x < 100 else 0)


def doba(s):
    s = round(s)
    return f"{s // 3600} h {s % 3600 // 60} min" if s >= 3600 else f"{s // 60} min {s % 60} s"


def cas_z_iso(t):
    from datetime import datetime
    return datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()


def nacti():
    """{krok: {"tokeny": [5], "cena": usd, "pozadavku": n, "rozpeti": s}}; neznámé řádky zvlášť."""
    kroky = defaultdict(lambda: {"tokeny": [0] * 5, "cena": 0.0, "pozadavku": 0, "intervaly": [],
                                 "hlavni": [0] * 5, "pomocni": [0] * 5})
    nezname = []
    for r in csv.DictReader(open(SPOTREBA, encoding="utf-8")):
        if not r["model"]:
            nezname.append(r)
            continue
        if r["model"] not in CENIK:
            raise SystemExit(f"Model {r['model']} nemá cenu v CENIK")
        k = kroky[r["krok"]]
        t = [int(r[p]) for p in POLE]
        k["tokeny"] = [a + b for a, b in zip(k["tokeny"], t)]
        druh = "hlavni" if r["druh"] == "hlavní konverzace" else "pomocni"
        k[druh] = [a + b for a, b in zip(k[druh], t)]
        k["cena"] += sum(t[i] * CENIK[r["model"]][p] for i, p in enumerate(POLE)) / 1e6
        k["pozadavku"] += int(r["pozadavku_api"])
        k["intervaly"].append((cas_z_iso(r["prvni_volani_utc"]), cas_z_iso(r["posledni_volani_utc"])))
    for k in kroky.values():
        # rozpětí volání: sjednocení intervalů částí (pomocní agenti běží uvnitř hlavní konverzace)
        iv = sorted(k["intervaly"])
        celkem, (od, do) = 0, iv[0]
        for a, b in iv[1:]:
            if a > do:
                celkem += do - od
                od, do = a, b
            else:
                do = max(do, b)
        k["rozpeti"] = celkem + do - od
    return kroky, nezname


def vzorek(n_pop, p=0.5):
    n0 = Z ** 2 * p * (1 - p) / PRESNOST_VZORKU ** 2
    return math.ceil(n0 / (1 + (n0 - 1) / n_pop))


def main():
    kroky, nezname = nacti()
    out = []
    w = out.append

    w("# Výpočet nákladů (generováno skriptem scripts/naklady.py, nepřepisovat ručně)\n")
    w("Ceny API: Claude Opus 5.5, USD/MTok: vstup 4, zápis do cache 5 min 5, zápis do cache 1 h 8, "
      "čtení z cache 0,20, výstup 20; web search 10 USD / 1 000. Zdroj "
      "https://platform.claude.com/docs/en/about-claude/pricing, načteno 27. 10. 2026. "
      "Pilot běžel v předplatném Claude, ceny jsou přepočet na API, ne zaplacená částka.\n")

    # 1. spotřeba po krocích
    w("## 1. Naměřená spotřeba pilotu po krocích (deduplikované logy Claude Code)\n")
    w("| krok | požadavků API | vstup | zápis cache 5 min | zápis cache 1 h | čtení cache | výstup | "
      "tokenů celkem | z toho pomocní agenti | cena API | čas |")
    w("|---|---|---|---|---|---|---|---|---|---|---|")
    nazvy = {"00": "0 plán a založení", "01": "1 sběr kandidátů", "02z": "2 zkušební dávka + úprava pravidel",
             "02": "2 obohacení", "03": "3 automatická kontrola", "04": "4 kontrola druhým agentem",
             "05": "5 příprava a uložení ruční kontroly", "06": "6 měření"}
    soucet = [0] * 5
    cena_celkem = 0.0
    for krok in ["00", "01", "02z", "02", "03", "04", "05", "06"]:
        k = kroky[krok]
        soucet = [a + b for a, b in zip(soucet, k["tokeny"])]
        cena_celkem += k["cena"]
        cas = (doba(CAS_MERENI[krok]) + " (mereni.txt)") if krok in CAS_MERENI else \
            (doba(k["rozpeti"]) + " (rozpětí v logu)")
        if krok == "02z":
            cas = "5 min 49 s dávka (mereni.txt) + úprava pravidel; " + doba(k["rozpeti"]) + " v logu"
        w(f"| {nazvy[krok]} | {k['pozadavku']} | " + " | ".join(cislo(x) for x in k["tokeny"]) +
          f" | {cislo(sum(k['tokeny']))} | {cislo(sum(k['pomocni'])) if sum(k['pomocni']) else '–'}"
          f" | {usd(k['cena'])} | {cas} |")
    w(f"| **celkem 0–6** | {sum(kroky[x]['pozadavku'] for x in kroky)} | " +
      " | ".join(cislo(x) for x in soucet) + f" | {cislo(sum(soucet))} | | **{usd(cena_celkem)}** | |")
    w("")
    w("Podle druhu konverzace a modelu (kroky 0–6):\n")
    w("| druh | model | agentů | požadavků API | tokenů celkem | cena API |")
    w("|---|---|---|---|---|---|")
    po_druhu = defaultdict(lambda: [0, 0, 0, 0.0])
    for r in csv.DictReader(open(SPOTREBA, encoding="utf-8")):
        if r["model"]:
            d = po_druhu[(r["druh"], r["model"])]
            d[0] += int(r["agentu"] or 0)
            d[1] += int(r["pozadavku_api"])
            d[2] += int(r["tokenu_celkem"])
            d[3] += sum(int(r[p]) * CENIK[r["model"]][p] for p in POLE) / 1e6
    for (druh, model), d in sorted(po_druhu.items()):
        w(f"| {druh} | {model} | {d[0] or '–'} | {d[1]} | {cislo(d[2])} | {usd(d[3])} |")
    w("")
    w("Neznámé, do součtu nezahrnuto (není to nula):\n")
    for r in nezname:
        w(f"- krok {r['krok']}, {r['cast']}: {r['poznamka'].removeprefix('neznámé: ')}")
    w("")

    # webové požadavky
    w("Webové požadavky (mereni.txt; `–` = neměřeno):\n")
    w("| krok | WebSearch | WebFetch | ARES | funding.tech.eu | curl | celkem |")
    w("|---|---|---|---|---|---|---|")
    for krok in ["00", "01", "02z", "02", "03", "04", "05", "06"]:
        d = WEB.get(krok)
        if d is None:
            w(f"| {nazvy[krok]} | – | – | – | – | – | – |")
        else:
            w(f"| {nazvy[krok]} | " + " | ".join(str(d.get(x, 0)) for x in
                                                ["WebSearch", "WebFetch", "ARES", "funding.tech.eu", "curl"])
              + f" | {sum(d.values())} |")
    w("")

    # 2. jednotkové náklady
    w("## 2. Jednotkové náklady pilotu\n")
    w(f"Na kandidáta = děleno {KANDIDATU}, na zařazený záznam = děleno {ZARAZENYCH}. "
      "Cena web search je jen u kroků, kde je počet vyhledávání naměřený.\n")
    w("| fáze | tokenů / kandidáta | cena / kandidáta | čas / kandidáta | tokenů / zařazený | "
      "cena / zařazený | čas / zařazený |")
    w("|---|---|---|---|---|---|---|")
    jednotky = {}
    for nazev, ks in FAZE:
        tok = sum(sum(kroky[k]["tokeny"]) for k in ks)
        cena = sum(kroky[k]["cena"] for k in ks) + \
            sum((WEB.get(k) or {}).get("WebSearch", 0) for k in ks) * CENA_WEB_SEARCH
        cas = sum(CAS_MERENI.get(k, kroky[k]["rozpeti"]) for k in ks)
        jednotky[nazev] = (tok, cena, cas)
        w(f"| {nazev} | {cislo(tok / KANDIDATU)} | {usd(cena / KANDIDATU)} | {doba(cas / KANDIDATU)} | "
          f"{cislo(tok / ZARAZENYCH)} | {usd(cena / ZARAZENYCH)} | {doba(cas / ZARAZENYCH)} |")
    lo, hi = RUCNI_MIN_NA_FIRMU
    w(f"| ruční kontrola: čas člověka (**modelový předpoklad, ne měření**) | – | – | "
      f"{doba(lo * 60 * RUCNE_KONTROLOVANYCH / KANDIDATU)}–{doba(hi * 60 * RUCNE_KONTROLOVANYCH / KANDIDATU)} | "
      f"– | – | {doba(lo * 60 * RUCNE_KONTROLOVANYCH / ZARAZENYCH)}–"
      f"{doba(hi * 60 * RUCNE_KONTROLOVANYCH / ZARAZENYCH)} |")
    w("")
    w(f"Ruční kontrola: {lo}–{hi} min na firmu s asistencí AI, za {RUCNE_KONTROLOVANYCH} firem "
      f"{doba(lo * 60 * RUCNE_KONTROLOVANYCH)} až {doba(hi * 60 * RUCNE_KONTROLOVANYCH)}. "
      "Řádek výše to rozpočítává na všech 56 kandidátů / 27 zařazených, i když ručně bylo zkontrolováno "
      "jen 20 zařazených. Čas fází 0, 1, 3, 5, 6 je rozpětí volání v logu včetně čekání na uživatele.\n")

    # 3. svět
    produkce = ["sběr kandidátů", "obohacení", "kontrola druhým agentem"]
    cena_kand = sum(jednotky[f][1] for f in produkce) / KANDIDATU
    cas_kand = sum(jednotky[f][2] for f in produkce) / KANDIDATU
    cena_obohaceni_kand = jednotky["obohacení"][1] / KANDIDATU
    cena_rucni_ai_firma = jednotky["ruční kontrola: podpora AI v Claude Code"][1] / RUCNE_KONTROLOVANYCH
    cena_rezie = jednotky["režie: plán, zkušební dávka a úprava pravidel, měření"][1] + \
        jednotky["automatická kontrola"][1]
    podil_nevyresenych = NEVYRESENYCH_A_HRANICNICH / KANDIDATU

    w("## 3. Přepočet na svět\n")
    w(f"Pilotní vstupy: AI na kandidáta (sběr + obohacení + kontrola druhým agentem) {usd(cena_kand)}, "
      f"z toho obohacení {usd(cena_obohaceni_kand)}; podpora AI u ruční kontroly {usd(cena_rucni_ai_firma)} "
      f"na kontrolovanou firmu; režie metodiky (kroky 0, 2z, 3, 6) {usd(cena_rezie)} za jedno provedení; "
      f"čas agentů {doba(cas_kand)} na kandidáta při souběžnosti pilotu; nevyřešené a hraniční "
      f"{NEVYRESENYCH_A_HRANICNICH}/{KANDIDATU} = {cislo(100 * podil_nevyresenych, 1)} % kandidátů; "
      f"kandidátů na zařazený {KANDIDATU}/{ZARAZENYCH} = {cislo(POMER_KANDIDATU, 2)}.\n")

    w("### 3.1 Parametry variant (předpoklady, ne měření)\n")
    w("| parametr | " + " | ".join(VARIANTY) + " |")
    w("|---|---|---|---|")
    popisy = [("zařazených záznamů (PLAN.md 8.2)", lambda v, z: cislo(sum(z.values()))),
              ("násobek tokenů na kandidáta vůči ČR", lambda v, z: cislo(v["nasobek_ai"], 2)),
              ("násobek času člověka vůči ČR", lambda v, z: cislo(v["nasobek_clovek"], 2)),
              ("min na firmu, ruční kontrola (základ ČR)", lambda v, z: cislo(v["min_na_firmu"], 1)),
              ("vrstev kontrolního vzorku", lambda v, z: str(v["vrstvy"])),
              ("opakování režie metodiky", lambda v, z: str(v["adaptaci"])),
              ("aktualizace: podíl tokenů obohacení", lambda v, z: cislo(v["podil_aktualizace"], 2)),
              ("aktualizace: min na kontrolu poslední investice", lambda v, z: cislo(v["min_posledni_investice"], 1))]
    for nazev, f in popisy:
        w(f"| {nazev} | " + " | ".join(f(VARIANTY[x], ZARAZENI_PO_TYPECH[x]) for x in VARIANTY) + " |")
    w("")

    vysledky = {}
    for nazev, v in VARIANTY.items():
        z = ZARAZENI_PO_TYPECH[nazev]
        n = sum(z.values())
        kand = n * POMER_KANDIDATU
        min_firma = v["min_na_firmu"] * v["nasobek_clovek"]
        if v["vrstvy"] == 1:
            n_vzorek = vzorek(n)
        else:
            n_vzorek = sum(vzorek(x) for x in z.values())
        ai_produkce = kand * cena_kand * v["nasobek_ai"]
        ai_rezie = cena_rezie * v["adaptaci"]
        nevyresene_h = kand * podil_nevyresenych * min_firma / 60
        vzorek_h = n_vzorek * min_firma / 60
        plna_h = n * min_firma / 60
        ai_rucni_vzorek = n_vzorek * cena_rucni_ai_firma * v["nasobek_ai"]
        ai_rucni_plna = n * cena_rucni_ai_firma * v["nasobek_ai"]
        akt_ai = n * cena_obohaceni_kand * v["nasobek_ai"] * v["podil_aktualizace"] * CTVRTLETI_ROCNE
        n_akt = vzorek(n, SPRAVNOST_POSLEDNI_INVESTICE)
        akt_h = n_akt * v["min_posledni_investice"] * v["nasobek_clovek"] / 60 * CTVRTLETI_ROCNE
        cas_agentu_h = kand * cas_kand * v["nasobek_ai"] / 3600
        vysledky[nazev] = dict(n=n, kand=kand, n_vzorek=n_vzorek, ai_produkce=ai_produkce, ai_rezie=ai_rezie,
                               nevyresene_h=nevyresene_h, vzorek_h=vzorek_h, plna_h=plna_h,
                               ai_rucni_vzorek=ai_rucni_vzorek, ai_rucni_plna=ai_rucni_plna,
                               akt_ai=akt_ai, n_akt=n_akt, akt_h=akt_h, cas_agentu_h=cas_agentu_h,
                               min_firma=min_firma)

    w("### 3.2 Výsledky (jednorázové sestavení + roční aktualizace)\n")
    w("| položka | " + " | ".join(VARIANTY) + " |")
    w("|---|---|---|---|")
    radky = [
        ("zařazených záznamů", lambda r: cislo(r["n"])),
        ("kandidátů (× 56/27)", lambda r: cislo(r["kand"])),
        ("AI: sběr, obohacení, kontrola druhým agentem", lambda r: usd(r["ai_produkce"])),
        ("AI: režie metodiky", lambda r: usd(r["ai_rezie"])),
        ("AI: podpora ruční kontroly – vzorek", lambda r: usd(r["ai_rucni_vzorek"])),
        ("**AI celkem, varianta s kontrolním vzorkem**",
         lambda r: "**" + usd(r["ai_produkce"] + r["ai_rezie"] + r["ai_rucni_vzorek"]) + "**"),
        ("AI celkem, varianta s plnou ruční kontrolou",
         lambda r: usd(r["ai_produkce"] + r["ai_rezie"] + r["ai_rucni_plna"])),
        ("AI na zařazený záznam (vzorek)",
         lambda r: usd((r["ai_produkce"] + r["ai_rezie"] + r["ai_rucni_vzorek"]) / r["n"])),
        ("čas agentů při souběžnosti pilotu", lambda r: cislo(r["cas_agentu_h"]) + " h"),
        ("min člověka na firmu", lambda r: cislo(r["min_firma"], 1)),
        ("ruční rozhodnutí nevyřešených a hraničních", lambda r: cislo(r["nevyresene_h"]) + " h"),
        ("kontrolní vzorek: firem", lambda r: cislo(r["n_vzorek"])),
        ("kontrolní vzorek: hodin", lambda r: cislo(r["vzorek_h"]) + " h"),
        ("**člověk celkem, varianta se vzorkem**",
         lambda r: "**" + cislo(r["vzorek_h"] + r["nevyresene_h"]) + " h**"),
        ("plná ruční kontrola: hodin", lambda r: cislo(r["plna_h"]) + " h"),
        ("**člověk celkem, varianta s plnou kontrolou**",
         lambda r: "**" + cislo(r["plna_h"] + r["nevyresene_h"]) + " h**"),
        ("aktualizace: AI ročně (4× poslední investice)", lambda r: usd(r["akt_ai"])),
        ("aktualizace: vzorek poslední investice za čtvrtletí", lambda r: cislo(r["n_akt"])),
        ("aktualizace: člověk ročně", lambda r: cislo(r["akt_h"]) + " h"),
    ]
    for nazev, f in radky:
        w(f"| {nazev} | " + " | ".join(f(vysledky[x]) for x in VARIANTY) + " |")
    w("")
    w(f"Kontrolní vzorek: n₀ = z²·p(1−p)/E² pro p = 0,5, E = {cislo(PRESNOST_VZORKU * 100)} p. b., 95 % "
      f"(n₀ ≈ 385), s korekcí na konečný soubor, ve všech variantách zvlášť pro VC, PE a family office. "
      f"Vzorek poslední investice pro aktualizaci: p = {cislo(SPRAVNOST_POSLEDNI_INVESTICE, 2)} z pilotu.\n")

    w(f"### 3.3 Náklady v USD při sazbě {cislo(SAZBA_USD_H)} USD/h\n")
    w(f"Sazba {cislo(SAZBA_USD_H)} USD/h je modelový předpoklad, ne zjištěná tržní cena.\n")
    w("| položka | " + " | ".join(VARIANTY) + " |")
    w("|---|---|---|---|")
    for nazev, ai, h in [
        ("sestavení s kontrolním vzorkem", lambda r: r["ai_produkce"] + r["ai_rezie"] + r["ai_rucni_vzorek"],
         lambda r: r["vzorek_h"] + r["nevyresene_h"]),
        ("sestavení s plnou kontrolou", lambda r: r["ai_produkce"] + r["ai_rezie"] + r["ai_rucni_plna"],
         lambda r: r["plna_h"] + r["nevyresene_h"]),
        ("roční aktualizace", lambda r: r["akt_ai"], lambda r: r["akt_h"]),
    ]:
        w(f"| {nazev}: AI | " + " | ".join(usd(ai(vysledky[x])) for x in VARIANTY) + " |")
        w(f"| {nazev}: člověk | " + " | ".join(usd(h(vysledky[x]) * SAZBA_USD_H) for x in VARIANTY) + " |")
        w(f"| **{nazev}: celkem** | " + " | ".join(
            "**" + usd(ai(vysledky[x]) + h(vysledky[x]) * SAZBA_USD_H) + "**" for x in VARIANTY) + " |")
    w("")

    w("### 3.4 Citlivost na poměr kandidátů k zařazeným\n")
    w("Mění se jen položky úměrné počtu kandidátů (AI sběr, obohacení, kontrola druhým agentem; "
      "ruční rozhodnutí nevyřešených). Poměr × 0,5 = 1,04 je blízko spodní meze 1.\n")
    w("| varianta | poměr | kandidátů | AI celkem (vzorek) | člověk celkem (vzorek) | člověk celkem (plná) |")
    w("|---|---|---|---|---|---|")
    for nazev in VARIANTY:
        r = vysledky[nazev]
        for c in CITLIVOST_POMERU:
            ai = r["ai_produkce"] * c + r["ai_rezie"] + r["ai_rucni_vzorek"]
            w(f"| {nazev} | {cislo(POMER_KANDIDATU * c, 2)} | {cislo(r['kand'] * c)} | {usd(ai)} | "
              f"{cislo(r['vzorek_h'] + r['nevyresene_h'] * c)} h | {cislo(r['plna_h'] + r['nevyresene_h'] * c)} h |")
    w("")

    text = "\n".join(out)
    VYSTUP.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
