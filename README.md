# Databáze investorů

Praktická úloha ve výběrovém řízení na pozici Junior AI Developer ve společnosti Clientelo.

## Zadání

Sestavit pomocí AI agentů spolehlivou databázi investorů, kteří vkládají vlastní nebo svěřený kapitál do soukromých firem výměnou za podíl (VC, CVC, PE, family office, andělé). Databáze nesmí obsahovat náhodné firmy. Každý údaj musí mít doložený zdroj a datum.

Součástí úlohy je:

- ověřit postup na pilotním vzorku (VC a CVC v ČR) a změřit jeho přesnost,
- odhadnout, kolik investorů lze z veřejných zdrojů dohledat ve světě,
- odhadnout náklady na zpracování celého světa.

Postup, pravidla zařazení, struktura záznamu a způsob měření jsou popsané v [PLAN.md](PLAN.md).

## Stav

Projekt je založený, data se zatím nesbírají. Datové soubory v `data/` obsahují jen hlavičky (CSV) nebo prázdný seznam (JSON).

## Struktura

| Cesta | Obsah |
|---|---|
| `PLAN.md` | plán projektu |
| `data/kandidati.csv` | kandidáti ze seznamů |
| `data/vystup_agenta/` | původní výstup agenta (zařazení, vyřazení, hraniční případy), beze změn |
| `data/hodnoceni.csv` | ruční hodnocení všech kandidátů |
| `data/opraveno/` | opravená verze po ručním hodnocení |
| `scripts/` | skripty pro automatickou kontrolu a měření |
| `ai-log/` | exporty konverzací s agenty |

## Licence

Viz [LICENSE](LICENSE).
