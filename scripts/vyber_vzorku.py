"""Výběr vzorku pro ruční kontrolu.

Náhodně vybere 20 záznamů ze zařazených investorů (investori.json)
se seedem 20261027. Výstup: data/vzorek_kontroly.csv.

Spuštění z kořene repa: python3 scripts/vyber_vzorku.py
"""
import csv
import json
import random
from pathlib import Path

SEED = 20261027
VELIKOST = 20

koren = Path(__file__).resolve().parent.parent
# investori.json je seznam záznamů zařazených investorů (PLAN.md bod 4).
investori = json.loads((koren / "data" / "vystup_agenta" / "investori.json").read_text(encoding="utf-8"))
assert isinstance(investori, list), "investori.json má být seznam záznamů"
ids = sorted(z["id"] for z in investori)

vzorek = sorted(random.Random(SEED).sample(ids, VELIKOST))

with open(koren / "data" / "vzorek_kontroly.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id"])
    w.writerows([i] for i in vzorek)

print(f"{len(ids)} zařazených, vybráno {len(vzorek)} (seed {SEED})")
