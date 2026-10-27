"""Naměřená spotřeba tokenů pilotu z lokálních logů Claude Code (krok 7, PLAN.md bod 10).

Čte jen pole usage, model, časové značky a identifikátory (message.id, requestId) ze záznamů
typu assistant. Obsah zpráv nečte do výstupu a neukládá. Výstup jsou jen agregovaná čísla
v ai-log/07-naklady/spotreba.csv a souhrn na stdout. Bez síťových přístupů, deterministický
pro dané logy.

Deduplikace: Claude Code zapisuje každý blok obsahu odpovědi (text, volání nástroje…) jako
samostatný záznam se shodnou usage celé odpovědi. Záznam se počítá jednou podle dvojice
(message.id, requestId); další výskyty se vyřadí. Skript kontroluje, že vyřazené výskyty mají
shodnou usage a že se žádná dvojice neopakuje napříč soubory.

Session kroků 0 a 1 běžely s pracovním adresářem domovské složky, jejich logy jsou proto
v ~/.claude/projects/-Users-petrstastny/. Přiřazení session ke krokům je v tabulce SESSIONY
(podle času, commitů a exportů v ai-log/).

Spuštění z kořene repa: python3 scripts/spotreba_z_logu.py
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

koren = Path(__file__).resolve().parent.parent
PROJEKTY = Path.home() / ".claude" / "projects"
ADRESARE_LOGU = [
    PROJEKTY / "-Users-petrstastny-Documents-Projekty-investori-databaze",
    PROJEKTY / "-Users-petrstastny",
]
VYSTUP = koren / "ai-log" / "07-naklady" / "spotreba.csv"

# Session → krok. Hodnota je seznam (hranice UTC, krok, část): záznam patří k první položce,
# jejíž hranice je větší než jeho časová značka (None = bez horní hranice). U pomocných agentů
# rozhoduje čas jejich prvního volání.
SESSIONY = {
    "8454bd15-ff88-4ff7-94cf-a26f4976263c": [(None, "00", "plán a založení")],
    "c326ece4-90fd-403f-9680-a719004e7300": [(None, "01", "sběr kandidátů")],
    # zkušební dávka 14:56:41Z–15:02:30Z (ai-log/02-zkusebni-davka/mereni.txt), pak úprava pravidel
    "c4487a53-7396-4e0f-b79a-5aad58692ecd": [("2026-10-26T15:02:31Z", "02z", "zkušební dávka"),
                                             (None, "02z", "úprava pravidel")],
    "f3cfc496-ee98-4858-a626-6212ecaf4d8c": [(None, "02", "obohacení 57 kandidátů")],
    "050be588-3490-4bf3-a698-1fd45f93b8ea": [(None, "03", "automatická kontrola")],
    # fáze A do commitu 967cb97 (18:44:07 CET), fáze B od 18:44:13 CET
    "e7a27589-eb01-4d71-a21a-353aded4990d": [("2026-10-26T17:44:12Z", "04", "fáze A (slepá kontrola)"),
                                             (None, "04", "fáze B (cílené otázky)")],
    # 26. 10. příprava podkladů, 27. 10. pokračování: uložení ručního hodnocení
    "e68ef0bc-6278-4c08-8ece-aa8b6481f4b8": [("2026-10-27T00:00:00Z", "05", "příprava podkladů"),
                                             (None, "05", "uložení ručního hodnocení")],
    "c87fffba-6ae0-4c5b-9332-cc5575fa1b55": [(None, "06", "měření")],
}
# Probíhající session kroku 7 (tento výpočet) se nezapočítává, její spotřeba by se při každém
# spuštění měnila.
VYNECHANE = {"9a0a849c-e9fc-4de7-91f5-8787caee1261"}

# Spotřeba, kterou logy nezachycují. Zapisuje se s prázdnými čísly (neznámé), ne jako 0.
NEZNAME = [
    ("05", "ruční kontrola: asistence AI mimo Claude Code",
     "README: zdroje a návrhy verdiktů zčásti od Claude a ChatGPT mimo tyto logy; spotřeba neznámá"),
    ("01–06", "WebFetch: zpracování stránek pomocným modelem",
     "nástroj WebFetch předává stránku pomocnému modelu; tyto požadavky v logu nejsou"),
    ("01–06", "WebSearch: samostatné požadavky vyhledávání",
     "usage.server_tool_use je ve všech záznamech 0; vyhledávání běží mimo zalogované požadavky"),
]

POLE = ["input_tokens", "cache_creation_5m", "cache_creation_1h", "cache_read_input_tokens",
        "output_tokens"]


def chyba(text):
    sys.exit(f"CHYBA: {text}")


def cast_podle_casu(session, cas):
    for hranice, krok, cast in SESSIONY[session]:
        if hranice is None or cas < hranice:
            return krok, cast
    chyba(f"čas {cas} session {session} nespadá do žádné části")


def nacti_soubor(cesta):
    """Vrátí (počet záznamů usage, {(message.id, requestId): [čas, model, usage, výskytů]})."""
    zaznamu = 0
    unikatni = {}
    with open(cesta, encoding="utf-8") as f:
        for radek in f:
            r = json.loads(radek)
            m = r.get("message")
            if r.get("type") != "assistant" or not isinstance(m, dict) or "usage" not in m:
                continue
            zaznamu += 1
            u = m["usage"]
            cc = u.get("cache_creation") or {}
            c5, c1 = cc.get("ephemeral_5m_input_tokens", 0), cc.get("ephemeral_1h_input_tokens", 0)
            if c5 + c1 != u["cache_creation_input_tokens"]:
                chyba(f"{cesta.name}: rozpad cache_creation nesedí na součet")
            hodnoty = (u["input_tokens"], c5, c1, u["cache_read_input_tokens"], u["output_tokens"])
            klic = (m.get("id"), r.get("requestId"))
            if klic == (None, None):
                chyba(f"{cesta.name}: záznam usage bez message.id i requestId")
            if klic in unikatni:
                if unikatni[klic][2] != hodnoty:
                    chyba(f"{cesta.name}: duplicitní záznam {klic} s jinou usage")
                unikatni[klic][3] += 1
                continue
            unikatni[klic] = [r["timestamp"], m.get("model"), hodnoty, 1]
    return zaznamu, unikatni


def soubory():
    """(session, druh, cesta) pro všechny přiřazené logy; nepřiřazená session v projektu = chyba."""
    vysledek = []
    for adresar in ADRESARE_LOGU:
        for cesta in sorted(adresar.glob("*.jsonl")):
            session = cesta.stem
            if session in VYNECHANE:
                continue
            if session not in SESSIONY:
                if adresar == ADRESARE_LOGU[0]:
                    chyba(f"session {session} v logu projektu není přiřazená ke kroku")
                continue
            vysledek.append((session, "hlavní konverzace", cesta))
            for sub in sorted((adresar / session / "subagents").glob("*.jsonl")):
                vysledek.append((session, "pomocný agent", sub))
    nalezene = {s for s, _, _ in vysledek}
    if nalezene != set(SESSIONY):
        chyba(f"chybí logy session: {sorted(set(SESSIONY) - nalezene)}")
    return vysledek


def main():
    radky = defaultdict(lambda: {"agentu": set(), "zaznamu": 0, "pozadavku": 0, "soucty": [0] * 5,
                                 "od": None, "do": None, "kontext_posledni": 0})
    videne = {}
    vyrazeno_celkem = 0
    for session, druh, cesta in soubory():
        zaznamu, unikatni = nacti_soubor(cesta)
        vyrazeno_celkem += zaznamu - len(unikatni)
        for klic in unikatni:
            if klic in videne:
                chyba(f"dvojice {klic} je v {videne[klic]} i v {cesta.name}")
            videne[klic] = cesta.name
        polozky = sorted(unikatni.values())
        if not polozky:
            continue
        # pomocný agent celý do části podle prvního volání, hlavní konverzace po záznamech
        skupiny = defaultdict(list)
        for cas, model, hodnoty, vyskytu in polozky:
            krok, cast = cast_podle_casu(session, polozky[0][0] if druh == "pomocný agent" else cas)
            skupiny[(krok, cast, session[:8], druh, model)].append((cas, hodnoty, vyskytu))
        for klic, seznam in skupiny.items():
            r = radky[klic]
            r["agentu"].add(cesta.name)
            r["zaznamu"] += sum(v for _, _, v in seznam)
            r["pozadavku"] += len(seznam)
            r["soucty"] = [a + b for a, b in zip(r["soucty"], (sum(h[i] for _, h, _ in seznam) for i in range(5)))]
            r["od"] = min(filter(None, [r["od"], seznam[0][0]]))
            r["do"] = max(filter(None, [r["do"], seznam[-1][0]]))
            if druh == "pomocný agent":
                r["kontext_posledni"] += sum(seznam[-1][1])

    VYSTUP.parent.mkdir(parents=True, exist_ok=True)
    hlavicka = ["krok", "cast", "session", "druh", "model", "agentu", "zaznamu_usage",
                "vyrazenych_duplicit", "pozadavku_api"] + POLE + \
               ["tokenu_celkem", "prvni_volani_utc", "posledni_volani_utc",
                "kontext_poslednich_volani", "poznamka"]
    with open(VYSTUP, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(hlavicka)
        for (krok, cast, session, druh, model), r in sorted(radky.items()):
            w.writerow([krok, cast, session, druh, model,
                        len(r["agentu"]) if druh == "pomocný agent" else "",
                        r["zaznamu"], r["zaznamu"] - r["pozadavku"], r["pozadavku"],
                        *r["soucty"], sum(r["soucty"]), r["od"], r["do"],
                        r["kontext_posledni"] if druh == "pomocný agent" else "", ""])
        for krok, cast, poznamka in NEZNAME:
            w.writerow([krok, cast, "", "", "", "", "", "", "", *[""] * 5, "", "", "", "", "neznámé: " + poznamka])

    print(f"Zapsáno {VYSTUP.relative_to(koren)}")
    print(f"Vyřazeno duplicitních záznamů usage: {vyrazeno_celkem}, unikátních požadavků: {len(videne)}")
    po_krocich = defaultdict(lambda: [0] * 6)
    for (krok, _, _, _, _), r in radky.items():
        po_krocich[krok] = [a + b for a, b in zip(po_krocich[krok], [r["pozadavku"], *r["soucty"]])]
    print(f"{'krok':5} {'pozad.':>7} " + " ".join(f"{p[:14]:>14}" for p in POLE))
    for krok in sorted(po_krocich):
        print(f"{krok:5} {po_krocich[krok][0]:7d} " + " ".join(f"{x:14,d}" for x in po_krocich[krok][1:]))


if __name__ == "__main__":
    main()
