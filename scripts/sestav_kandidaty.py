"""Sestaví data/kandidati.csv (krok 1 v PLAN.md, bod 9) z extraktů zdrojů v ai-log/01-kandidati/.

Vstupy jsou snímky zdrojů stažené 2026-10-26 (CVCA, CEE Funding Map, funding.tech.eu API,
Dealroom manifest) a ověření sídel (sidla_overeni.json). Deduplikace je ruční a explicitní
v tabulce ENTITY: jeden řádek = jeden kandidát, u každého seznam názvů, pod kterými se
vyskytl v jednotlivých zdrojích. Skript kontroluje, že každý odkazovaný název ve zdroji
existuje a že žádný výskyt není přiřazen dvěma kandidátům.

Výstupy:
- data/kandidati.csv: id,nazev,web,zdroj_seznamu,zdroj_url,stazeno; u kandidáta z více
  zdrojů jsou zdroj_seznamu a zdroj_url seznamy oddělené " | " ve stejném pořadí.
- ai-log/01-kandidati/mimo_rozsah.csv: výskyty ze zdrojů, které mezi kandidáty nejsou, s důvodem.
"""
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "ai-log" / "01-kandidati"
STAZENO = "2026-10-26"
SEP = " | "

CVCA = "CVCA"
MAPA = "CEE Funding Map"
FTECH = "funding.tech.eu"
DEALROOM = "Dealroom"

# id, nazev, web, výskyty: cvca = název řádného člena, mapa = název místa na mapě,
# ftech = jméno investora v kolech českých firem 2025–2026, dealroom = slug profilu.
ENTITY = [
    ("cz-arx-equity-partners", "ARX Equity Partners", "https://www.arxequity.com/", {"cvca": ["ARX Equity Partners"], "mapa": ["ARX Equity"]}),
    ("cz-bd-partners", "BD Partners", "https://www.bdpartners.cz/", {"mapa": ["BD Partners"], "ftech": ["BD Partners"]}),
    ("cz-borovicka-capital", "Borovicka Capital", "https://borovickacapital.com/", {"ftech": ["Borovicka Capital"]}),
    ("cz-botanique-hospitality", "Botanique Hospitality", "", {"ftech": ["Botanique Hospitality"]}),
    ("cz-braiins", "Braiins", "https://braiins.com/", {"ftech": ["Braiins"]}),
    ("cz-central-europe-industry-partners", "Central Europe Industry Partners", "https://industrypartners.eu/en/", {"mapa": ["Central Europe Industry Partners"]}),
    ("cz-chilli-ventures", "Chilli Ventures", "https://www.chilliventures.cz/", {"ftech": ["Chilli Ventures"]}),
    ("cz-credo-ventures", "Credo Ventures", "https://credoventures.com/", {"cvca": ["Credo Ventures"], "mapa": ["Credo Ventures"], "ftech": ["Credo Ventures"], "dealroom": ["credo-ventures"]}),
    ("cz-cs-seed-starter", "ČS Seed Starter", "https://www.seedstarter.cz/", {"mapa": ["ČS Seed Starter a.s."]}),
    ("cz-czech-founders-vc", "Czech Founders VC", "https://czechfounders.vc/", {"mapa": ["Czech Founders VC"], "ftech": ["Czech Founders VC"]}),
    ("cz-depo-ventures", "Depo Ventures", "https://depoventures.com/", {"cvca": ["Depo Ventures"], "mapa": ["Depo Ventures"], "ftech": ["DEPO Ventures"]}),
    ("cz-emma-capital", "EMMA Capital", "https://www.emmacapital.cz/", {"mapa": ["EMMA CAPITAL"]}),
    ("cz-espira-investments", "Espira Investments", "https://www.espirainvestments.com/", {"cvca": ["Espira Investments"]}),
    ("cz-everita-capital", "EVERITA Capital", "https://everitacap.com/", {"cvca": ["EVERITA Capital"]}),
    ("cz-fazole-ventures", "Fazole Ventures", "https://www.fazole.vc/", {"mapa": ["Fazole Ventures"]}),
    ("cz-fond-nase-cesko", "Fond Naše Česko", "https://www.nase-cesko.cz/", {"ftech": ["Fond Naše Česko"]}),
    ("cz-garage-angels", "Garage Angels", "", {"ftech": ["Garage Angels"]}),
    ("cz-genesis-capital", "Genesis Capital", "https://www.genesis.cz/", {"cvca": ["Genesis Capital Equity s.r.o."], "mapa": ["Genesis Capital"]}),
    ("cz-gi21-capital", "Gi21 Capital", "https://gi21capital.com/", {"mapa": ["Gi21 Capital"], "ftech": ["Gi21 Capital", "Gi21 fund"]}),
    ("cz-ii-biotech-investments", "i&i Biotech Investments", "https://www.inibio.eu/", {"cvca": ["i&i Biotech Investments"]}),
    ("cz-ii-prague", "i&i Prague", "https://www.iniprague.com/", {"mapa": ["i&i Prague"]}),
    ("cz-inven-capital", "Inven Capital", "https://www.invencapital.cz/", {"cvca": ["Inven Capital"], "mapa": ["Inven Capital"]}),
    ("cz-jt-ventures", "J&T Ventures", "https://www.jtventures.cz/", {"mapa": ["J&T Ventures"], "ftech": ["J&T Ventures"]}),
    ("cz-jet-investment", "Jet Investment", "https://jetinvestment.eu/", {"cvca": ["Jet Investment"], "mapa": ["Jet Investments"], "ftech": ["Jet Investment", "Jet Investment Group"]}),
    ("cz-jic-ventures", "JIC Ventures", "https://www.jic.cz/en/potreby-a-sluzby/jic-ventures", {"mapa": ["JIC Ventures"], "ftech": ["JIC Ventures"]}),
    ("cz-kaya-vc", "KAYA VC", "https://www.kaya.vc/", {"cvca": ["KAYA  VC"], "mapa": ["KAYA VC"], "ftech": ["KAYA", "KAYA VC"]}),
    ("cz-kkcg", "KKCG", "https://kkcg.com/en/", {"mapa": ["KKCG"]}),
    ("cz-lighthouse-ventures", "Lighthouse Ventures", "https://lhv.vc/", {"mapa": ["Lighthouse"], "ftech": ["Lighthouse Ventures"]}),
    ("cz-lion-beat-capital", "Lion Beat Capital", "https://lionbeatcapital.com/", {"ftech": ["Lion Beat Capital"]}),
    ("cz-look-ai-ventures", "Look AI Ventures", "https://lookai.vc/", {"mapa": ["Look AI Ventures"]}),
    ("cz-lumus-investments", "LUMUS Investments", "https://www.lumusinvestment.com/", {"mapa": ["LUMUS Investments"]}),
    ("cz-mam-private-equity-fund", "MAM Private Equity Fund SICAV a.s.", "https://www.mam-equity.cz/", {"cvca": ["MAM Private Equity Fund SICAV a.s."]}),
    ("cz-mcwin-partners", "McWin Partners", "https://mcwin.cz/", {"mapa": ["McWin Partners"]}),
    ("cz-miton", "Miton", "https://www.miton.cz/", {"mapa": ["Miton"], "ftech": ["Miton"]}),
    ("cz-moonhill-capital", "Moonhill Capital", "https://www.moonhill.capital/", {"mapa": ["Moonhill Capital"]}),
    ("cz-n1-ventures", "N1 Ventures", "https://n1.rocks/", {"mapa": ["N1 Ventures"]}),
    ("cz-nation1", "Nation1", "https://www.nation1.vc/", {"cvca": ["Nation1"]}),
    ("cz-orbit-capital", "Orbit Capital", "https://orbitcapital.com/", {"cvca": ["Orbit Capital"], "mapa": ["ORBIT Capital", "Orbit Capital"], "ftech": ["Orbit Capital"]}),
    ("cz-presto-ventures", "Presto Ventures", "https://www.prestoventures.com/", {"mapa": ["Presto Ventures"]}),
    ("cz-purple-ventures", "Purple Ventures", "https://www.purple-ventures.com/", {"mapa": ["Purple Ventures"], "ftech": ["Purple Ventures"]}),
    ("cz-purposetech", "PurposeTech", "https://www.purposetech.vc/", {"mapa": ["PurposeTech", "PurposeTech / Purpose Ventures"]}),
    ("cz-qq-capital", "QQ Capital", "", {"ftech": ["QQ Capital"]}),
    ("cz-reflex-capital", "Reflex Capital", "https://www.reflexcapital.com/", {"mapa": ["Reflex Capital"], "ftech": ["Reflex Capital"]}),
    ("cz-rockaway-ventures", "Rockaway Ventures", "https://rockawayventures.com/", {"mapa": ["Rockaway Ventures"], "ftech": ["Rockaway Ventures"]}),
    ("cz-rockawayx", "RockawayX", "https://rockawayx.com/", {"mapa": ["RockawayX"]}),
    ("cz-skylimit-investments", "SkyLimit Investments", "https://www.skylimit.cz/", {"cvca": ["SkyLimit Investments"]}),
    ("cz-soulmates-ventures", "Soulmates Ventures", "https://www.soulmatesventures.com/", {"mapa": ["Soulmates Ventures"]}),
    ("cz-startupyard", "StartupYard", "https://startupyard.com/", {"mapa": ["StartupYard"]}),
    ("cz-stratum-partners", "Stratum Partners", "https://www.stratum.eu/", {"cvca": ["Stratum Partners"]}),
    ("cz-tarpan-capital", "Tarpan Capital", "", {"ftech": ["Tarpan Capital"]}),
    ("cz-tcf-capital", "TCF Capital", "https://www.tcfcap.com/", {"mapa": ["TCF Capital"]}),
    ("cz-tensor-ventures", "Tensor Ventures", "https://tensor.ventures/", {"cvca": ["Tensor Ventures"], "mapa": ["Tensor Ventures"], "ftech": ["Tensor Ventures"]}),
    ("cz-thein", "Thein", "https://www.thein.eu/", {"cvca": ["Thein"]}),
    ("cz-tilia-impact-ventures", "Tilia Impact Ventures", "https://tilia.vc/", {"cvca": ["Tilia Impact Ventures – Honorary Member"], "ftech": ["Tilia Impact Ventures"]}),
    ("cz-versute-investments", "Versute Investments", "https://www.versute.cz/", {"cvca": ["Versute Investments"]}),
    ("cz-y-soft-ventures", "Y Soft Ventures", "https://www.ysoft.com/ventures", {"mapa": ["Y Soft Ventures"]}),
    ("cz-zaka-vc", "ZAKA VC", "https://zaka.vc/", {"mapa": ["ZAKA VC"]}),
]

# Jména z funding.tech.eu, která nejsou investiční subjekt (popis účastníků kola, ne investor).
FTECH_SUM = {"VCs", "existing shareholders", "company’s founders", "EU grants"}

# Jména z funding.tech.eu, která odpovídají položce CEE Funding Map s adresou mimo ČR.
MAPA_SHODA = {"Simpact Ventures": "Simpact Ventures", "Smartlink": "Smartlink Partners",
              "Smartlink Partners": "Smartlink Partners", "Inovo VC": "Inovo VC"}


def nacti(nazev):
    return json.loads((SRC / nazev).read_text(encoding="utf-8"))


def main():
    cvca = nacti("zdroje/cvca_radni_clenove.json")["clenove"]
    mapa = nacti("zdroje/cee_funding_map.json")["polozky"]
    ftech = nacti("zdroje/fundingtecheu_investori.json")
    dealroom = nacti("zdroje/dealroom_cz.json")["investori_se_zemi_czechia"]
    sidla = {r["name"]: r for r in nacti("sidla_overeni.json")}

    vyskyty = {
        "cvca": {m["nazev"]: [(CVCA, m["detail_url"])] for m in cvca},
        "mapa": {},
        "ftech": {n: [(FTECH, "https://funding.tech.eu/api/v1/investors/" + quote(n, safe=""))] for n in ftech},
        "dealroom": {d["slug"]: [(DEALROOM, d["profile_url"])] for d in dealroom},
    }
    for p in mapa:
        vyskyty["mapa"].setdefault(p["nazev"], []).append((MAPA, p["misto_url"]))

    chyby, pouzito, radky = [], set(), []
    for id_, nazev, web, zdroje in ENTITY:
        if not re.fullmatch(r"cz-[a-z0-9]+(-[a-z0-9]+)*", id_):
            chyby.append(f"neplatné id {id_}")
        pary = []
        for druh in ("cvca", "mapa", "ftech", "dealroom"):
            for jmeno in zdroje.get(druh, []):
                if jmeno not in vyskyty[druh]:
                    chyby.append(f"{id_}: {druh} '{jmeno}' ve zdroji není")
                    continue
                if (druh, jmeno) in pouzito:
                    chyby.append(f"{id_}: {druh} '{jmeno}' přiřazen dvakrát")
                pouzito.add((druh, jmeno))
                pary += vyskyty[druh][jmeno]
        radky.append({
            "id": id_, "nazev": nazev, "web": web,
            "zdroj_seznamu": SEP.join(z for z, _ in pary),
            "zdroj_url": SEP.join(u for _, u in pary),
            "stazeno": STAZENO,
        })
    if len({r["id"] for r in radky}) != len(radky):
        chyby.append("duplicitní id")
    if chyby:
        sys.exit("\n".join(chyby))

    with open(ROOT / "data" / "kandidati.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "nazev", "web", "zdroj_seznamu", "zdroj_url", "stazeno"])
        w.writeheader()
        w.writerows(sorted(radky, key=lambda r: r["id"]))

    # Výskyty, které se mezi kandidáty nedostaly, a proč.
    mimo = []
    for m in cvca:
        if ("cvca", m["nazev"]) not in pouzito:
            mimo.append((m["nazev"], CVCA, m["detail_url"], "sídlo mimo ČR podle CVCA: " + (m["adresa"] or ""), ""))
    for p in mapa:
        if ("mapa", p["nazev"]) in pouzito:
            continue
        if p["adresa"]:
            mimo.append((p["nazev"], MAPA, p["misto_url"], "sídlo mimo ČR podle mapy: " + p["adresa"], ""))
        else:
            s = sidla[p["nazev"]]
            mimo.append((p["nazev"], MAPA, p["misto_url"], f"adresa na mapě chybí; sídlo podle ověření {s['hq_country']}: {s['evidence_quote']}", s["evidence_url"]))
    for n, prof in ftech.items():
        if ("ftech", n) in pouzito:
            continue
        url = vyskyty["ftech"][n][0][1]
        if n in FTECH_SUM:
            duvod, dukaz = "není investiční subjekt (popis účastníků kola)", ""
        elif prof.get("types") == ["Angel"] and n != "NitroPack":
            duvod, dukaz = "fyzická osoba (typ Angel ve zdroji), mimo rozsah pilotu VC a CVC", ""
        elif n in sidla:
            s = sidla[n]
            if s["hq_country"]:
                duvod = f"sídlo mimo ČR ({s['hq_country']}): {s['evidence_quote']}"
            else:
                duvod = "sídlo nedoloženo, kancelář v ČR nenalezena: " + s["note"]
            dukaz = s["evidence_url"] or ""
        else:
            # Stejný investor je na CEE Funding Map s adresou mimo ČR.
            shoda = MAPA_SHODA[n]
            p = next(p for p in mapa if p["nazev"] == shoda)
            duvod, dukaz = f"sídlo mimo ČR podle CEE Funding Map ({shoda}): {p['adresa']}", p["misto_url"]
        mimo.append((n, FTECH, url, duvod, dukaz))

    with open(SRC / "mimo_rozsah.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nazev", "zdroj_seznamu", "zdroj_url", "duvod", "dukaz_url"])
        w.writerows(mimo)

    print(f"kandidátů: {len(radky)}, mimo rozsah: {len(mimo)}")


if __name__ == "__main__":
    main()
