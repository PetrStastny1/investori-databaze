# Automatická kontrola výstupu agenta

Vygenerováno skriptem `scripts/zkontroluj_data.py` (PLAN.md, bod 6 „Automaticky (skript)“). Kontrola jen čte, původní data neopravuje. Neověřuje, jestli zdroje opravdu dokládají údaje: to je úkol kontroly druhým agentem a ruční kontroly.

## Parametry

- referenční datum: 2026-10-26
- okno 24 měsíců: od 2024-10-26 do 2026-10-26 včetně
- hranice statusu `aktivni`: datum pro filtr od 2025-10-26 včetně
- kontrola dostupnosti URL: ano
- příkaz: `python3 scripts/zkontroluj_data.py --datum 2026-10-26 --over-url`
- opakovatelnost: při stejném referenčním datu a stejných vstupech (otisky níže) dají kontroly stejný výsledek; jen výsledek kontroly URL závisí na době běhu a stavu webů

Vstupní soubory (SHA-256, prvních 12 znaků):

- `data/kandidati.csv`: 4ba3f64afc89
- `ai-log/02-obohaceni/mapovani_id.csv`: 7dbb277e879f
- `data/vystup_agenta/investori.json`: 03fa0ab4f904
- `data/vystup_agenta/vyrazeni.csv`: 39a7d00f15d9
- `data/vystup_agenta/hranicni.csv`: 6ad44ce3630a
- `data/vystup_agenta/nevyresene.csv`: a8b30944fa94

## Souhrn

| Kategorie | Nálezů | Záznamů |
|---|---|---|
| Chyby struktury | 0 | 0 |
| Metodický nesoulad | 1 | 1 |
| Upozornění vyžadující kontrolu zdroje | 16 | 9 |

- **Chyba struktury:** soubor nebo pole neodpovídá schématu z PLAN.md (klíče, typy, povolené hodnoty, chybějící nebo zdvojený výsledek kandidáta).
- **Metodický nesoulad:** tvar je správný, ale údaj odporuje pravidlům plánu (okno 24 měsíců, status, nástroj, jistota, pravidla pilotu, zdroj u vyplněného pole).
- **Upozornění:** pravidlo porušené není, ale zdroj nebo údaj je potřeba zkontrolovat ručně.

### Pokrytí vstupních id

Vstupních id v `data/kandidati.csv`: 57, v `mapovani_id.csv`: 57.

| Výsledek | Podle mapování | Záznamů ve výstupu |
|---|---|---|
| investori.json | 27 | 27 |
| vyrazeni.csv | 17 | 17 |
| hranicni.csv | 1 | 1 |
| nevyresene.csv | 11 | 11 |
| slouceno | 1 | – |

Pokrytí je úplné: každé vstupní id má právě jeden výsledek nebo je sloučené do zpracovaného záznamu.

### Přehledy pro ruční kontrolu

- Investic v `investori.json` (poslední i další): 64, z toho s `datum_pro_filtr` = oznameni: 64 (PLAN.md bod 4: tyto záznamy mají jít spočítat a zvlášť zkontrolovat).
- Zařazené záznamy, které opírají podmínku 3 jen o `neprima_indicie` (pracovní předpoklad, jistota nejvýš `stredni`): 19 (cz-credo-ventures, cz-cs-seed-starter, cz-czech-founders-vc, cz-depo-ventures, cz-ii-biotech-investments, cz-inven-capital, cz-jt-ventures, cz-jic-ventures, cz-kaya-vc, cz-lighthouse-ventures, cz-look-ai-ventures, cz-n1-ventures, cz-purple-ventures, cz-purposetech, cz-soulmates-ventures, cz-startupyard, cz-tensor-ventures, cz-tilia-impact-ventures, cz-zaka-vc).
- URL zkontrolováno: 354, HTTP 200: 349, jinak: 5. HTTP 200 znamená jen, že stránka odpověděla, ne že údaj sedí. Neúspěšné stažení nedokazuje, že údaj je nepravdivý.

## Chyby struktury (0)

Žádné.

## Metodický nesoulad (1)

| Soubor | Id | Pravidlo | Detail |
|---|---|---|---|
| investori.json | cz-kaya-vc | `fond` jen u fund_size | `kapital[2].fond` = 'pátý fond (po first closingu)' u druhu committed_capital. |

## Upozornění vyžadující kontrolu zdroje (16)

| Soubor | Id | Pravidlo | Detail |
|---|---|---|---|
| investori.json | cz-borovicka-capital | označení kola u nepřímé indicie | `dalsi_investice[1].nastroj.kolo` = 'late-seed' není kanonické pre-seed/seed/series; započítáno jako seed nebo series kolo, ověř ve zdroji. |
| investori.json | cz-ii-biotech-investments | dostupnost URL | https://cvca.cz/en/biotech-investments/ → URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.. Neúspěšné stažení nedokazuje, že údaj je nepravdivý; zkontroluj ručně. |
| investori.json | cz-ii-biotech-investments | zdroj na doméně s neplatným certifikátem | `pravni_subjekt.zdroje[1]`: https://cvca.cz/en/biotech-investments/; doména má neplatný certifikát TLS a způsob stažení není zapsaný, ověř zdroj. |
| investori.json | cz-jt-ventures | `plati_k` u kapitálu | `kapital[0]` (120000000 EUR, aum) nemá datum platnosti. |
| investori.json | cz-kaya-vc | `plati_k` u kapitálu | `kapital[0]` (500000000 USD, aum) nemá datum platnosti. |
| investori.json | cz-kaya-vc | `plati_k` u kapitálu | `kapital[1]` (85000000 USD, fund_size) nemá datum platnosti. |
| investori.json | cz-n1-ventures | `plati_k` u kapitálu | `kapital[0]` (60000000 USD, aum) nemá datum platnosti. |
| investori.json | cz-n1-ventures | dostupnost URL | https://cvca.cz/en/nation1-2/ → URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.. Neúspěšné stažení nedokazuje, že údaj je nepravdivý; zkontroluj ručně. |
| investori.json | cz-n1-ventures | zdroj na doméně s neplatným certifikátem | `pravni_subjekt.zdroje[1]`: https://cvca.cz/en/nation1-2/; doména má neplatný certifikát TLS a způsob stažení není zapsaný, ověř zdroj. |
| investori.json | cz-soulmates-ventures | `plati_k` u kapitálu | `kapital[0]` (62000000 EUR, aum) nemá datum platnosti. |
| nevyresene.csv | cz-jet-investment | dostupnost URL | https://cvca.cz/en/jet-investment-2/ → URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.. Neúspěšné stažení nedokazuje, že údaj je nepravdivý; zkontroluj ručně. |
| nevyresene.csv | cz-jet-investment | zdroj na doméně s neplatným certifikátem | `zdroj_url`: https://cvca.cz/en/jet-investment-2/; doména má neplatný certifikát TLS a způsob stažení není zapsaný, ověř zdroj. |
| vyrazeni.csv | cz-thein | dostupnost URL | https://cvca.cz/en/thein-2/ → URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.. Neúspěšné stažení nedokazuje, že údaj je nepravdivý; zkontroluj ručně. |
| vyrazeni.csv | cz-thein | zdroj stažený bez ověření TLS | `zdroj_url`: https://cvca.cz/en/thein-2/ byl v kroku 2 stažen přes `curl -k` (bez ověření certifikátu); obsah nemusí pocházet z pravého webu, ověř zdroj. |
| vyrazeni.csv | cz-versute-investments | dostupnost URL | https://cvca.cz/en/versute-investments-2/ → URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.. Neúspěšné stažení nedokazuje, že údaj je nepravdivý; zkontroluj ručně. |
| vyrazeni.csv | cz-versute-investments | zdroj na doméně s neplatným certifikátem | `zdroj_url`: https://cvca.cz/en/versute-investments-2/; doména má neplatný certifikát TLS a způsob stažení není zapsaný, ověř zdroj. |

## Co kontrola neověřuje

- jestli zdroj opravdu dokládá údaj v poli (firma, datum, částka, typ, nástroj),
- jestli jsou zdroje uvedené s různým `puvod` opravdu nezávislé; skript porovnává jen zapsané hodnoty,
- správnost typu, sídla a rozhodnutí u vyřazených, hraničních a nevyřešených kandidátů (u nich kontroluje jen tvar, povolené hodnoty, důvod a zdroj),
- stažení bez ověření TLS zná jen z logu kroku 2 (seznam `STAZENO_BEZ_TLS` ve skriptu); ostatní zdroje na doméně s neplatným certifikátem označuje obecně.
