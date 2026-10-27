"""Měření přesnosti na ručně zkontrolovaném vzorku (krok 7, PLAN.md bod 7).

Čte data/hodnoceni.csv, data/vzorek_kontroly.csv, ai-log/02-obohaceni/mapovani_id.csv,
ai-log/04-kontrola-zdroju/slepa_kontrola.csv
a ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv, nic z nich nemění.
Bez síťových přístupů, deterministický. Výstup: data/mereni_vzorku.md a souhrn na stdout.
Výsledky se nikdy nesčítají do jednoho čísla.

Spuštění z kořene repa: python3 scripts/mereni.py
"""
import csv
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

koren = Path(__file__).resolve().parent.parent
HODNOCENI = koren / "data" / "hodnoceni.csv"
VZOREK = koren / "data" / "vzorek_kontroly.csv"
MAPOVANI = koren / "ai-log" / "02-obohaceni" / "mapovani_id.csv"
SLEPA = koren / "ai-log" / "04-kontrola-zdroju" / "slepa_kontrola.csv"
PRED_AI = koren / "ai-log" / "05-rucni-kontrola" / "hodnoceni_pred_nalezy_ai.csv"
VYSTUP = koren / "data" / "mereni_vzorku.md"

Z = 1.959964  # 95 %
CELKEM_ZARAZENYCH = 27

POLE = ["existence", "investicni_cinnost", "je_investor", "typ", "rozsah_pilotu",
        "posledni_investice", "nezavislost_zdroju", "sektory", "ticket", "kapital"]
POLE_ZARAZENI = ["existence", "investicni_cinnost", "je_investor", "typ", "rozsah_pilotu"]
POLE_UPLNOST = ["sektory", "ticket", "kapital"]
JEN_UPLNOST = "nevyplneno – pouze úplnost"
POTVRZENE_CHYBENI = "Potvrzené chybění"
ZMENA_PO_AI = "Změna po přečtení nálezů AI"

# Skupina každého konečného „ne“ podle id/pole (PLAN.md bod 7, Druhy „ne“).
# Řádek „ne“, který tu chybí, skript odmítne.
SKUPINA_NE = {
    ("cz-look-ai-ventures", "posledni_investice"): "chyba_vystupu",
    ("cz-purple-ventures", "posledni_investice"): "chyba_vystupu",
    ("cz-reflex-capital", "posledni_investice"): "chyba_vystupu",
    ("cz-zaka-vc", "posledni_investice"): "chyba_vystupu",
    ("cz-n1-ventures", "rozsah_pilotu"): "upresneni_metodiky",
    ("cz-ii-biotech-investments", "rozsah_pilotu"): "upresneni_metodiky",
    ("cz-ii-biotech-investments", "ticket"): "omezeni_schematu",
}
SKUPINY = ["chyba_vystupu", "upresneni_metodiky", "omezeni_schematu"]

# Výklad pricina_chyby, kde hodnota v CSV nestačí. Prázdná příčina u „ne“ = „neurčeno“
# (z logu nejde doložit, zda agent zdroj viděl).
PRICINA_VYKLAD = {
    ("cz-zaka-vc", "posledni_investice"):
        "chybne_pouziti_pravidla (agent odmítl přípustný zdroj)",
}

# Mapování polí kontrolního agenta (fáze A) na pole ručního hodnocení.
MAPOVANI_PLNE = {
    "pravni_subjekt": "existence", "investicni_cinnost": "investicni_cinnost", "typ": "typ",
    "sidlo": "rozsah_pilotu", "posledni_investice": "posledni_investice", "sektory": "sektory",
    "ticket": "ticket", "kapital": "kapital", "slouceni": "slouceni",
}
MAPOVANI_CASTECNE = {"nastroj": "je_investor", "jistota_investice": "nezavislost_zdroju"}
NEZMAPOVANE = ["web", "faze", "status", "dalsi_investice"]

# U dvojic, kde agent pole označil a konečné hodnocení je „ne“ nebo „nelze_overit“:
# týká se nález agenta téže vady jako konečné hodnocení? Interpretační přiřazení
# provedené AI (Claude) porovnáním textů (vysvetleni agenta vs. poznámka v hodnoceni.csv),
# ne automaticky ani nezávisle ověřená skutečnost. Upozornění na jinou část pole
# se za zachycení nepočítá. Chybějící dvojici skript odmítne.
ZACHYCENI = {
    ("cz-look-ai-ventures", "posledni_investice"): (True, "obojí: novější investice Embodied AI 22. 9. 2026"),
    ("cz-purple-ventures", "posledni_investice"): (True, "obojí: novější FLÆ Robotics 14. 10. 2026"),
    ("cz-reflex-capital", "posledni_investice"): (True, "obojí: novější ArtMaster 21. 10. 2026"),
    ("cz-zaka-vc", "posledni_investice"): (True, "obojí: novější FinalDose 16. 7. 2026 na zaka.vc/news"),
    ("cz-n1-ventures", "rozsah_pilotu"): (True, "obojí: lucemburští správci (GP/AIFM)"),
    ("cz-ii-biotech-investments", "rozsah_pilotu"): (True, "obojí: lucemburský fond, česká s.r.o. jen poradce"),
    ("cz-n1-ventures", "existence"): (True, "obojí: GP v Lucembursku neověřeni v registru"),
    ("cz-tensor-ventures", "rozsah_pilotu"): (True, "obojí: lucemburský GP, sídlo správce sporné"),
    ("cz-y-soft-ventures", "nezavislost_zdroju"): (True, "obojí: puvod null u zpráv, nezávislost nedoložena"),
}


def wilson(k, n):
    if n == 0:
        return None
    p = k / n
    d = 1 + Z * Z / n
    stred = (p + Z * Z / (2 * n)) / d
    polosirka = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return max(0.0, stred - polosirka), min(1.0, stred + polosirka)


def pct(x):
    return f"{x * 100:.1f} %".replace(".", ",")


def podil(k, n):
    """„k/n = p % (95% CI a–b %)“, při n = 0 N/A."""
    if n == 0:
        return f"{k}/{n} = N/A"
    lo, hi = wilson(k, n)
    return f"{k}/{n} = {pct(k / n)} (95% CI {pct(lo)}–{pct(hi)})"


def zkrat(text, n=160):
    text = " ".join(text.split()).replace("|", "/")
    return text if len(text) <= n else text[: n - 1] + "…"


def nacti_csv(cesta):
    with open(cesta, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# --- načtení -------------------------------------------------------------------

vzorek = [r["id"] for r in nacti_csv(VZOREK)]
assert len(vzorek) == len(set(vzorek)) == 20, "vzorek má mít 20 unikátních id"
vzorek_set = set(vzorek)

hodnoceni = nacti_csv(HODNOCENI)
hod = {(r["id"], r["pole"]): r for r in hodnoceni}
assert len(hod) == len(hodnoceni), "duplicitní id/pole v hodnoceni.csv"
pred_ai = {(r["id"], r["pole"]): r for r in nacti_csv(PRED_AI)}

# Sloučená id (cz-nation1 → cz-n1-ventures) patří k firmě, do které byla sloučena.
vysledne_id = {r["id"]: r["vysledne_id"] for r in nacti_csv(MAPOVANI)}


def firma(id_):
    return vysledne_id.get(id_, id_)


radky = {}  # (id, pole) -> řádek, jen 10 polí zařazených firem ze vzorku
for r in hodnoceni:
    if r["soubor"] == "investori.json" and r["id"] in vzorek_set:
        assert r["pole"] in POLE, r
        radky[(r["id"], r["pole"])] = r
assert len(radky) == 20 * len(POLE), "u každé firmy vzorku má být všech 10 polí"


def verdikt(r):
    h = r["hodnoceni"]
    if h == "":
        assert r["poznamka"].startswith(JEN_UPLNOST), r
        assert r["pole"] in POLE_UPLNOST, r
        return "jen_uplnost"
    assert h in ("ano", "ne", "nelze_overit"), r
    return h


def skupina(id_, pole):
    k = (id_, pole)
    assert k in SKUPINA_NE, f"ne bez skupiny v SKUPINA_NE: {k}"
    return SKUPINA_NE[k]


def pricina(r):
    k = (r["id"], r["pole"])
    return PRICINA_VYKLAD.get(k) or r["pricina_chyby"] or "neurčeno"


for k, r in radky.items():
    if verdikt(r) == "ne":
        skupina(*k)
assert all(radky[k]["hodnoceni"] == "ne" for k in SKUPINA_NE), "SKUPINA_NE obsahuje řádek, který není ne"

out = []
souhrn = []
w = out.append

w("# Měření přesnosti na vzorku 20 firem")
w("")
w("Vygenerováno skriptem `scripts/mereni.py` z `data/hodnoceni.csv`. Nepřepisovat ručně.")
w("")
w("## Co čísla znamenají a co ne")
w("")
w(f"- Ručně byl ověřen náhodný výběr 20 z {CELKEM_ZARAZENYCH} zařazených (seed 20261027, "
  "`scripts/vyber_vzorku.py`, `data/vzorek_kontroly.csv`), s asistencí AI (README, "
  "„Ruční kontrola – kdo hodnotil“). Výsledky platí pro zařazené, ne pro všech 56 kandidátů. "
  "Nevyřešené a vyřazené kandidáty nikdo ručně nekontroloval, recall ze vzorku spočítat nejde.")
w("- `nelze_overit` není potvrzená chyba, vykazuje se zvlášť jako nedostatečný důkaz.")
w("- Konečná `ne` jsou rozdělená do skupin `chyba_vystupu` (skutečná chyba agenta), "
  "`upresneni_metodiky` (výklad upřesněný až při ruční kontrole) a `omezeni_schematu` "
  "(schéma hodnotu neumí zapsat). Zařazení do skupin je v tabulce `SKUPINA_NE` ve skriptu.")
w("- Wilsonův interval předpokládá nezávislá pozorování. Řádky po polích jsou seskupené po "
  "firmách, takže souhrnný interval přes všechna pole je optimistický. Interval je bez korekce "
  "na konečný soubor (20 z 27), v tomto ohledu je spíš konzervativní.")
w("- Přesnost = ano/(ano+ne), dolní mez = ano/(ano+ne+nelze_overit), tj. jako by každé "
  "`nelze_overit` bylo chybou.")
w("")

# --- 1. zařazení ---------------------------------------------------------------

stav_firmy = {}
ne_firmy = {}
for f in vzorek:
    v = {p: verdikt(radky[(f, p)]) for p in POLE_ZARAZENI}
    ne = [p for p in POLE_ZARAZENI if v[p] == "ne"]
    if ne:
        stav_firmy[f] = "chybne"
        ne_firmy[f] = ne
    elif any(x == "nelze_overit" for x in v.values()):
        stav_firmy[f] = "neovereno"
    else:
        stav_firmy[f] = "spravne"
pocty = Counter(stav_firmy.values())
sp, ch, no = pocty["spravne"], pocty["chybne"], pocty["neovereno"]

jen_metodika = [f for f, ne in ne_firmy.items()
                if all(skupina(f, p) == "upresneni_metodiky" for p in ne)]
n_b = sp + ch - len(jen_metodika)
n_b_dolni = len(vzorek) - len(jen_metodika)

w("## 1. Zařazení investorů (jednotka = firma, 20 firem)")
w("")
w(f"Pole: {', '.join(POLE_ZARAZENI)}. Aspoň jedno `ne` → chybně zařazen; jinak aspoň jedno "
  "`nelze_overit` → neověřeno; jinak správně.")
w("")
w(f"- správně {sp}, chybně {ch}, neověřeno {no}")
w("")
w("| firma | stav | pole `ne` (skupina) | pole `nelze_overit` |")
w("|---|---|---|---|")
for f in vzorek:
    if stav_firmy[f] == "spravne":
        continue
    ne = ", ".join(f"{p} ({skupina(f, p)})" for p in ne_firmy.get(f, []))
    nl = ", ".join(p for p in POLE_ZARAZENI if verdikt(radky[(f, p)]) == "nelze_overit")
    w(f"| {f} | {stav_firmy[f]} | {ne or '–'} | {nl or '–'} |")
w("")
w("a) Všechna `ne`:")
w("")
w(f"- přesnost správně/(správně+chybně): {podil(sp, sp + ch)}")
w(f"- dolní mez správně/20: {podil(sp, len(vzorek))}")
w("")
neovereno = [f for f in vzorek if stav_firmy[f] == "neovereno"]
w("b) Jen vůči chybám výstupu: firmy, jejichž chybné zařazení je jen `upresneni_metodiky` "
  f"({', '.join(jen_metodika) or 'žádné'}), jsou z jmenovatele vynechané, nepočítají se jako správné.")
w("")
w(f"- správnost mezi {n_b} rozhodnutelnými případy po vyloučení {len(jen_metodika)} změn "
  f"metodiky: {podil(sp, n_b)}; vedle toho {no} neověřené ({', '.join(neovereno)}). "
  "Nejde o 100% ověřenou databázi.")
w(f"- dolní mez, jmenovatel {n_b_dolni}: {podil(sp, n_b_dolni)}")
w("")
souhrn += [
    f"Zařazení: správně {sp}, chybně {ch}, neověřeno {no}",
    f"  přesnost {podil(sp, sp + ch)}; dolní mez {podil(sp, len(vzorek))}",
    f"  správnost mezi {n_b} rozhodnutelnými po vyloučení {len(jen_metodika)} změn metodiky: "
    f"{podil(sp, n_b)}, vedle toho {no} neověřené; dolní mez {podil(sp, n_b_dolni)}",
]

# --- 2. pole -------------------------------------------------------------------

def pocty_pole(klice):
    c = Counter()
    for k in klice:
        v = verdikt(radky[k])
        c["ne:" + skupina(*k) if v == "ne" else v] += 1
    c["ne"] = sum(c["ne:" + s] for s in SKUPINY)
    return c


w("## 2. Správnost vyplněných polí (jednotka = řádek id/pole)")
w("")
w("`jen úplnost` = pole agent nevyplnil, do přesnosti nevstupuje (oddíl 3).")
w("")
w("| pole | ano | ne: chyba_vystupu | ne: upresneni_metodiky | ne: omezeni_schematu | nelze_overit | jen úplnost | přesnost ano/(ano+ne) | dolní mez ano/(ano+ne+nelze) |")
w("|---|---|---|---|---|---|---|---|---|")
for p in POLE + ["celkem"]:
    klice = [k for k in radky if p == "celkem" or k[1] == p]
    c = pocty_pole(klice)
    jm = c["ano"] + c["ne"]
    nazev = "**celkem**" if p == "celkem" else p
    w(f"| {nazev} | {c['ano']} | {c['ne:chyba_vystupu']} | {c['ne:upresneni_metodiky']} | "
      f"{c['ne:omezeni_schematu']} | {c['nelze_overit']} | {c['jen_uplnost']} | "
      f"{podil(c['ano'], jm)} | {podil(c['ano'], jm + c['nelze_overit'])} |")
c = pocty_pole(radky)
jm_v = c["ano"] + c["ne:chyba_vystupu"]
w("")
w("Varianta jen vůči chybám výstupu: řádky `upresneni_metodiky` a `omezeni_schematu` "
  f"({c['ne:upresneni_metodiky'] + c['ne:omezeni_schematu']}) jsou z jmenovatele vynechané.")
w("")
w("| pole | jmenovatel přesnosti | přesnost | jmenovatel dolní meze | dolní mez |")
w("|---|---|---|---|---|")
for p in POLE + ["celkem"]:
    cp = pocty_pole([k for k in radky if p == "celkem" or k[1] == p])
    jm = cp["ano"] + cp["ne:chyba_vystupu"]
    nazev = "**celkem**" if p == "celkem" else p
    w(f"| {nazev} | {jm} | {podil(cp['ano'], jm)} | {jm + cp['nelze_overit']} | "
      f"{podil(cp['ano'], jm + cp['nelze_overit'])} |")
w("")
souhrn += [
    f"Pole: ano {c['ano']}, ne {c['ne']} (chyba_vystupu {c['ne:chyba_vystupu']}, "
    f"upresneni_metodiky {c['ne:upresneni_metodiky']}, omezeni_schematu {c['ne:omezeni_schematu']}), "
    f"nelze_overit {c['nelze_overit']}, jen úplnost {c['jen_uplnost']}",
    f"  přesnost {podil(c['ano'], c['ano'] + c['ne'])}; "
    f"dolní mez {podil(c['ano'], c['ano'] + c['ne'] + c['nelze_overit'])}",
    f"  jen chyby výstupu: přesnost {podil(c['ano'], jm_v)}; "
    f"dolní mez {podil(c['ano'], jm_v + c['nelze_overit'])}",
]

# Kontrola sloučení se vykazuje samostatně, do přesnosti polí nevstupuje.
slouceni = [r for r in hodnoceni if r["pole"] == "slouceni" and firma(r["id"]) in vzorek_set]
w("### Kontrola sloučení (samostatně)")
w("")
w(f"Řádků: {len(slouceni)}. Do přesnosti polí výše nevstupuje.")
w("")
for r in slouceni:
    w(f"- {r['id']} → {firma(r['id'])}: {r['hodnoceni']} ({zkrat(r['poznamka'])})")
w("")
souhrn.append("Sloučení (samostatně, mimo přesnost polí): "
              + ", ".join(f"{r['id']} {r['hodnoceni']}" for r in slouceni)
              + f" ({len(slouceni)} řádek)")

# --- 3. úplnost ----------------------------------------------------------------

w("## 3. Úplnost (sektory, ticket, kapitál)")
w("")
w("Potvrzené chybění = údaj ve zdroji existuje, agent ho nezapsal.")
w("")
w("| pole | vyplněno z 20 | podíl vyplněných | potvrzené chybění |")
w("|---|---|---|---|")
for p in POLE_UPLNOST:
    prazdne = [radky[(f, p)] for f in vzorek if verdikt(radky[(f, p)]) == "jen_uplnost"]
    vypl = len(vzorek) - len(prazdne)
    chybeni = [r["id"] for r in prazdne if POTVRZENE_CHYBENI in r["poznamka"]]
    w(f"| {p} | {vypl} | {podil(vypl, len(vzorek))} | {len(chybeni)}"
      f"{' (' + ', '.join(chybeni) + ')' if chybeni else ''} |")
    souhrn.append(f"Úplnost {p}: vyplněno {vypl}/20, potvrzené chybění {len(chybeni)}")
w("")

# --- 4. seznam ne a nelze_overit -----------------------------------------------

w("## 4. Všechna `ne` a `nelze_overit`")
w("")
w("| id | pole | skupina | příčina | poznámka (zkráceno) |")
w("|---|---|---|---|---|")
for k, r in radky.items():
    if verdikt(r) == "ne":
        w(f"| {k[0]} | {k[1]} | {skupina(*k)} | {pricina(r)} | {zkrat(r['poznamka'])} |")
w("")
w("Příčina `neurčeno`: z logu nejde doložit, zda agent zdroj viděl. U `upresneni_metodiky` "
  "a `omezeni_schematu` je `chyba_pravidel` hodnota z CSV, význam určuje skupina.")
w("")
w("| id | pole | poznámka (zkráceno) |")
w("|---|---|---|")
for k, r in radky.items():
    if verdikt(r) == "nelze_overit":
        w(f"| {k[0]} | {k[1]} | {zkrat(r['poznamka'])} |")
w("")

# --- 5. srovnání s kontrolním agentem ------------------------------------------

slepa = [r for r in nacti_csv(SLEPA) if firma(r["id"]) in vzorek_set]
nalezy = defaultdict(list)  # (id, pole hodnocení) -> řádky agenta
nezmapovane = Counter()
nezmapovane_oznacene = Counter()
for r in slepa:
    pole_a = re.sub(r"\[\d+\]$", "", r["pole"])
    if pole_a in MAPOVANI_PLNE:
        nalezy[(r["id"], MAPOVANI_PLNE[pole_a])].append(r)
    elif pole_a in MAPOVANI_CASTECNE:
        nalezy[(r["id"], MAPOVANI_CASTECNE[pole_a])].append(r)
    else:
        assert pole_a in NEZMAPOVANE, f"neznámé pole agenta: {r['pole']}"
        nezmapovane[pole_a] += 1
        nezmapovane_oznacene[pole_a] += r["zaver"] != "sedi"


def oznaceno(k):
    return any(r["zaver"] != "sedi" for r in nalezy.get(k, []))


def konecny(k):
    r = hod[k]
    return verdikt(r) if k in radky else (r["hodnoceni"] or "jen_uplnost")


def zachyceno(k):
    assert k in ZACHYCENI, f"chybí posouzení v ZACHYCENI: {k}"
    return ZACHYCENI[k]


def popis_nalezu(k):
    rr = [r for r in nalezy.get(k, []) if r["zaver"] != "sedi"]
    if not nalezy.get(k):
        return "agent pole nekontroloval"
    if not rr:
        return "vše `sedi`"
    return "; ".join(f"{r['pole']}: {r['zaver']} – {zkrat(r['vysvetleni'], 120)}" for r in rr)


def oddil_srovnani(nadpis, pole_hodnoceni):
    klice = sorted(k for k in hod if firma(k[0]) in vzorek_set and k[1] in pole_hodnoceni)
    w(nadpis)
    w("")
    w(f"Unikátních dvojic id/pole: {len(klice)}, s aspoň jedním řádkem agenta: "
      f"{sum(1 for k in klice if nalezy.get(k))}, označených (`zaver` ≠ `sedi`): "
      f"{sum(1 for k in klice if oznaceno(k))}.")
    w("")
    tridy = [
        ("Konečné `ne` – chyba_vystupu",
         [k for k in klice if konecny(k) == "ne" and skupina(*k) == "chyba_vystupu"]),
        ("Konečné `ne` – upresneni_metodiky",
         [k for k in klice if konecny(k) == "ne" and skupina(*k) == "upresneni_metodiky"]),
        ("Konečné `ne` – omezeni_schematu",
         [k for k in klice if konecny(k) == "ne" and skupina(*k) == "omezeni_schematu"]),
        ("Konečné `nelze_overit`", [k for k in klice if konecny(k) == "nelze_overit"]),
    ]
    w("| konečné hodnocení | dvojic | agent označil | z toho tutéž vadu | agent neoznačil |")
    w("|---|---|---|---|---|")
    vysledek = {}
    for nazev, kk in tridy:
        ozn = [k for k in kk if oznaceno(k)]
        tataz = [k for k in ozn if zachyceno(k)[0]]
        w(f"| {nazev} | {len(kk)} | {len(ozn)} | {len(tataz)} | {len(kk) - len(ozn)} |")
        vysledek[nazev] = (len(kk), len(ozn), len(tataz))
    nepotvrzene = [k for k in klice if oznaceno(k) and konecny(k) in ("ano", "jen_uplnost")]
    w(f"| Označení agenta, která konečné hodnocení nepotvrdilo (konečně `ano`) | "
      f"{len(nepotvrzene)} | {len(nepotvrzene)} | – | – |")
    w("")
    w("Podrobnosti ke všem dvojicím s konečným `ne` / `nelze_overit` nebo s označením agenta:")
    w("")
    w("| id | pole | konečně | tutéž vadu | nálezy agenta (zkráceno) |")
    w("|---|---|---|---|---|")
    for k in klice:
        kon = konecny(k)
        if kon not in ("ne", "nelze_overit") and not oznaceno(k):
            continue
        kon_txt = f"ne ({skupina(*k)})" if kon == "ne" else kon
        if oznaceno(k) and kon in ("ne", "nelze_overit"):
            ano_ne, duvod = zachyceno(k)
            taz = f"{'ano' if ano_ne else 'ne'} – {duvod}"
        else:
            taz = "–"
        w(f"| {k[0]} | {k[1]} | {kon_txt} | {taz} | {popis_nalezu(k)} |")
    w("")
    return vysledek, len(nepotvrzene)


w("## 5. Srovnání s kontrolním agentem (fáze A, jen 20 firem vzorku)")
w("")
w("Konečné hodnocení vzniklo s asistencí AI a část změn až po přečtení nálezů kontrolního "
  "agenta, takže není nezávislý referenční standard. Srovnání popisuje shodu s konečným "
  "hodnocením a změny po přečtení nálezů, ne nezávisle změřenou přesnost kontrolního agenta. "
  "Počítají se unikátní dvojice id/pole, ne řádky agenta (`kapital[0]`, `kapital[1]` … jsou "
  "jedna dvojice). „Tutéž vadu“ = nález agenta se týká téže vady jako konečné hodnocení. "
  "Jde o interpretační přiřazení provedené AI porovnáním textů (tabulka `ZACHYCENI` ve "
  "skriptu), ne o automaticky ani nezávisle ověřenou skutečnost; upozornění na jinou část "
  "pole se nepočítá.")
w("")
w("Mapování: " + ", ".join(f"{a}→{b}" for a, b in MAPOVANI_PLNE.items())
  .replace("kapital→kapital", "kapital[*]→kapital") + " (plně srovnatelná); "
  + ", ".join(f"{a}→{b}" for a, b in MAPOVANI_CASTECNE.items()) + " (částečná).")
w("")
vys_plne, nepotvrz_plne = oddil_srovnani(
    "### 5.1 Plně srovnatelná pole", set(MAPOVANI_PLNE.values()))
vys_cast, nepotvrz_cast = oddil_srovnani(
    "### 5.2 Částečná mapování (nastroj→je_investor, jistota_investice→nezavislost_zdroju)",
    set(MAPOVANI_CASTECNE.values()))

w("### 5.3 Nezmapovaná pole agenta")
w("")
w("| pole agenta | řádků ve vzorku | z toho `zaver` ≠ `sedi` |")
w("|---|---|---|")
for p in NEZMAPOVANE:
    w(f"| {p} | {nezmapovane[p]} | {nezmapovane_oznacene[p]} |")
w("")

w("### 5.4 Před a po přečtení nálezů AI")
w("")
w("Porovnání `data/hodnoceni.csv` se stavem před přečtením nálezů "
  "(`ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv`), 10 polí 20 firem.")
w("")
ne_pred = [k for k, r in radky.items() if verdikt(r) == "ne" and pred_ai[k]["hodnoceni"] == "ne"]
ne_po = [k for k, r in radky.items() if verdikt(r) == "ne" and pred_ai[k]["hodnoceni"] != "ne"]
nl_pred = [k for k, r in radky.items()
           if verdikt(r) == "nelze_overit" and pred_ai[k]["hodnoceni"] == "nelze_overit"]
ano_nl = [k for k, r in radky.items()
          if verdikt(r) == "nelze_overit" and pred_ai[k]["hodnoceni"] == "ano"]
for k in ne_po + ano_nl:
    assert ZMENA_PO_AI in radky[k]["poznamka"], f"změna bez poznámky: {k}"
jine = [k for k, r in radky.items() if r["hodnoceni"] != pred_ai[k]["hodnoceni"]
        and k not in ne_po and k not in ano_nl]


def seznam(kk):
    return ", ".join(f"{i}/{p}" + (f" ({skupina(i, p)})" if verdikt(radky[(i, p)]) == "ne" else "")
                     for i, p in kk) or "–"


w("| | počet | dvojice |")
w("|---|---|---|")
w(f"| konečné `ne` nalezené už před přečtením nálezů AI | {len(ne_pred)} | {seznam(ne_pred)} |")
w(f"| konečné `ne` nalezené až po nich | {len(ne_po)} | {seznam(ne_po)} |")
w(f"| konečné `nelze_overit`, už před přečtením | {len(nl_pred)} | {seznam(nl_pred)} |")
w(f"| změna `ano` → `nelze_overit` po přečtení | {len(ano_nl)} | {seznam(ano_nl)} |")
w(f"| jiné změny verdiktu | {len(jine)} | {seznam(jine)} |")
w("")

VYSTUP.write_text("\n".join(out), encoding="utf-8")

for nazev, (n, ozn, taz) in vys_plne.items():
    souhrn.append(f"Agent (plně srovnatelná) – {nazev}: {n}, označil {ozn}, tutéž vadu {taz}")
souhrn.append(f"Agent (plně srovnatelná) – označení nepotvrzená konečným hodnocením: {nepotvrz_plne}")
for nazev, (n, ozn, taz) in vys_cast.items():
    souhrn.append(f"Agent (částečná) – {nazev}: {n}, označil {ozn}, tutéž vadu {taz}")
souhrn.append(f"Agent (částečná) – označení nepotvrzená konečným hodnocením: {nepotvrz_cast}")
souhrn.append(f"Před/po AI: ne před {len(ne_pred)}, ne po {len(ne_po)}, "
              f"ano→nelze_overit {len(ano_nl)}, jiné změny {len(jine)}")
print("\n".join(souhrn))
print(f"Zapsáno: {VYSTUP.relative_to(koren)}")
