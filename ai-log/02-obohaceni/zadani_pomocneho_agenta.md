<!-- Zadání, které dostal každý pomocný agent kroku 2. Po dávce 1 bylo doplněno upřesnění počítání WebFetch (bod 4) a bod 5 o nesloučených dvojicích; pravidla zařazení se neměnila. -->

# Zadání: obohacení a zařazení kandidátů (krok 2, vyhodnocení po úpravě metodiky)

Repozitář: /Users/petrstastny/Documents/Projekty/investori-databaze
Dnešní datum: 2026-10-26 (`stazeno` = 2026-10-26).

## 1. Nejdřív si přečti

- `PLAN.md` celý, hlavně body 2, 3 a 4. Pravidla v něm jsou finální a jsou jediným měřítkem. Neměň je, nevykládej je volněji a nepřidávej vlastní.
- `data/kandidati.csv`: řádky tvých kandidátů (id, nazev, web, zdroj_url).

Do `data/` ani do jiných souborů repozitáře nezapisuj. Zapisuješ jen:
- surové odpovědi API do `ai-log/02-obohaceni/zdroje/`,
- výsledek do `/private/tmp/claude-501/-Users-petrstastny-Documents-Projekty-investori-databaze/f3cfc496-ee98-4858-a626-6212ecaf4d8c/scratchpad/vysledky/<id>.json` (jeden soubor na kandidáta).

Negituj (žádný commit).

## 2. Povinné kroky u každého kandidáta

1. **ARES (IČO).** Hledání podle názvu a pak výpis z veřejného rejstříku:
   ```
   curl -s -X POST -H "Content-Type: application/json" -d '{"obchodniJmeno":"<název>","pocet":20}' https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat -o ai-log/02-obohaceni/zdroje/ares_hledani_<Nazev_bez_mezer>.json
   curl -s https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/<ICO> -o ai-log/02-obohaceni/zdroje/ares_vr_<ICO>.json
   ```
   Odpovědi ukládej surové, nezměněné (přímo `-o`). Pokud zkoušíš víc variant názvu, každou ulož pod vlastním názvem souboru (např. `ares_hledani_Nazev_varianta2.json`). IČO beru za ověřené, jen když ho vrátil ARES a obchodní firma/statutáři odpovídají investorovi podle jiného zdroje (média, web). Totožnost, kterou nedoložíš, napiš do poznámky jako nepotvrzenou. U zahraničního subjektu ARES jen zkus, a použij ekvivalentní rejstřík nebo regulátora, pokud je veřejně dostupný.
   URL do záznamu: `https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/<ICO>`, `druh_zdroje` `rejstrik`, `vydavatel` „ARES (výpis z veřejného rejstříku)“.
2. **funding.tech.eu.** Profil investora pro každé jméno z `zdroj_url` kandidáta v kandidati.csv (a jen pokud kandidát odtamtud není, zkus `https://funding.tech.eu/api/v1/investors/<URL-encoded název>`):
   ```
   curl -s "https://funding.tech.eu/api/v1/investors/<jméno>" -o ai-log/02-obohaceni/zdroje/fundingtecheu_inv_<Jmeno_bez_mezer>.json
   ```
   Mezi požadavky na funding.tech.eu dělej pauzu aspoň 1 s (limit 120/min, 600/h). Ukládej nezměněné. API u kol uvádí jen doménu zdroje, ne URL zprávy, takže samo o sobě **není zprávou o transakci**. Použij ho jako vodítko a zprávu dohledej.
3. **Zprávy o transakcích** (WebSearch, WebFetch): tiskové zprávy, CzechCrunch, Forbes, HN, E15, Vestbee, tech.eu, weby portfoliových firem a podobně. Hledej nejnovější doložené investice v okně 24 měsíců: datum pro filtr ≥ 2024-10-26. Status `aktivni` = datum pro filtr ≥ 2025-10-26, `investice_dolozena_12_24_mesicu` = 2024-10-26 až 2025-10-25. Zkrácené datum (jen měsíc nebo rok) ber pro filtr jako poslední den období, a pokud výsledek filtru nebo statusu závisí na přesném dni, napiš to do poznámky jako „k ruční kontrole“.
4. **Web investora** (typ podle vlastního popisu, sektory, fáze, ticket, kapitál, portfolio).

Čti zdroje sám. WebFetch vrací výtah pomocného modelu, proto u klíčových údajů (jméno investora v kole, datum, nástroj, částka, vlastní popis typu) chtěj v promptu doslovnou citaci a údaj bez citace nepřebírej. Nic neodhaduj. Co nenajdeš, je `null`. Údaj bez URL je chyba.

## 3. Pravidla, na která se nejčastěji chybuje (všechna jsou v PLAN.md)

- **Velikost kola ≠ vklad investora.** Částku kola nikdy nedávej do `ticket` ani `kapital`. Do poznámky ji můžeš uvést jako velikost celého kola.
- **`kapital`** jen `aum` / `committed_capital` / `fund_size` tak, jak ho uvádí sám investor nebo regulátor (případně médium, které ho cituje, s URL). Záměr investovat, „máme k dispozici“, alokované peníze apod. nejsou kapitál, nech prázdné a vysvětli v poznámce. Nesčítej.
- **Ticket** jen deklarovaný investorem (web, rozhovor), ne odvozený z kol.
- **`datum_investice`** jen když zdroj výslovně uvádí den/měsíc podpisu nebo uzavření. Jinak `null` a datum jde do `datum_oznameni` (první veřejné oznámení, ne datum přetisku). `datum_pro_filtr` = `investice` jen s vyplněným `datum_investice`.
- **Nástroj** u každé investice: `{"hodnota": "podil"|"konvertibilni"|null, "doklad": "dolozeno"|"neprima_indicie"|"nezjisteno", "kolo": "...|null", "zdroj_url": "...|null"}`. `dolozeno` jen když zdroj výslovně uvádí podíl/akcie/konvertibilní nástroj/SAFE (nebo zápis společníka v rejstříku). `neprima_indicie` když zdroj v `zdroj_url` dokládá účast konkrétního investora v pre-seed / seed / series kole (`kolo` vyplněné). `nezjisteno`: `hodnota` a `zdroj_url` null. U smíšených kol (equity + úvěr / venture debt) rozhoduje, co zdroj říká o účasti tohoto investora.
- **Zařazený záznam** musí mít aspoň u jedné investice `dolozeno` se `zdroj_url`, nebo `neprima_indicie` se `zdroj_url` a `kolo` pre-seed/seed/series. Pokud žádná investice nemá `dolozeno`, je `jistota.investice` = `stredni`.
- **Akvizice / koupě většinového či menšinového podílu** je doložený podíl (`dolozeno`), pokud to zdroj tak píše.
- **`jistota.investice` = `vysoka`** jen při dvou zprávách o transakci s různým `puvod` (stejná tisková zpráva převzatá víc médii = jeden zdroj, společná TZ investora a firmy = jeden zdroj). Pokud nezávislost nedoložíš, `stredni`.
- **Typ** podle vlastního popisu a doloženého fungování, ne podle toho, do čeho investuje (PLAN.md bod 2, „Typ a investiční strategie“). Family office jen když se tak subjekt výslovně označuje a fungování tomu odpovídá; samotné peníze jedné rodiny nestačí. Provozní firma investující z vlastní společnosti bez samostatné jednotky = „Korporátní investor bez samostatné jednotky“. CVC = samostatná investiční jednotka velké firmy. Akcelerátor s vlastním kapitálem a doloženými investicemi za podíl = VC. Když si důkazy o typu odporují nebo nestačí a na typu závisí výsledek → `nevyresene`.
- **Sídlo** pilotu = sídlo investiční firmy (správce, značky), ne fondu ani portfoliové firmy.
- **Kategorie vyřazení:** nejdřív posuď body 2 a 3 (je to investor?). `neni_investor` = nesplňuje body 2 a 3 (zprostředkovatel, fond fondů, banka, úvěr, nemovitosti, bez doložené investice v okně 24 měsíců…). `mimo_rozsah_pilotu` jen pro skutečného investora podle bodů 2 a 3 s jiným typem nebo sídlem mimo ČR. Investora mimo rozsah pilotu nevydávej za neinvestora a naopak.
- **Nevyřešené** (`nevyresene`): jen nevyřešený typ nebo nástroj, na kterém závisí výsledek (např. investor s typem mimo pilot, ale nástroj nezjištěný → `mimo_rozsah_pilotu | neni_investor`). Když kandidát investor není z jiného důvodu (žádná zpráva o transakci v okně), typ nevadí, je to `neni_investor`.
- **Venture debt** → `hranicni`.
- **Rozporné zdroje k investici** (firma, datum, investor): investici nepoužij jako doklad a popiš to v poznámce. Pokud kvůli tomu nezbude doklad, kandidát není zařazen (popiš).
- **Duplicity:** jedna investiční firma = jeden záznam. Fondy pod jedním správcem jsou podřízené údaje (`kapital[].fond`, poznámka), ne samostatní investoři.
- Výsledek nepřizpůsobuj očekávanému počtu zařazených.

## 4. Formát výsledku

`vysledky/<id>.json`:

```json
{
  "id": "cz-...",
  "vysledek": "zarazen | vyrazen | hranicni | nevyresene | slouceno",
  "zaznam": { ... },
  "radek": { ... },
  "slouceno_do": null,
  "pozadavky": {"WebSearch": 0, "WebFetch": 0, "WebFetch_neuspesne": 0, "ARES": 0, "fundingtecheu": 0, "jine_curl": 0},
  "nejasnosti": ["…"],
  "shrnuti": "1–3 věty, proč tento výsledek"
}
```

- `zarazen`: `zaznam` je přesně schéma z PLAN.md bod 4 (klíče `id, nazev, typ, zeme, pravni_subjekt, web, sektory, faze, ticket, kapital, posledni_investice, dalsi_investice, status, jistota, poznamka`). `posledni_investice` i každá položka `dalsi_investice` má `firma, datum_investice, datum_oznameni, datum_pro_filtr, nastroj, zdroje` a `zdroje` jsou plné objekty (`url, druh_zdroje, vydavatel, puvod, zdroj_datum, stazeno`). `dalsi_investice` dej jen ty, které jsou doložené zprávou (nejvýš 3–4). Nevyplněné pole má hodnotu `null` (u `sektory`/`faze` `{"hodnota": null, "zdroj_url": null, ...}`, `kapital` `[]`). `radek` = null.
- `vyrazen`: `radek` = `{"id","nazev","web","kategorie","duvod","zdroj_url","stazeno"}`; `zdroj_url` je jedna nebo víc URL oddělených ` | `, které důvod dokládají. `duvod` je konkrétní (citace, data, IČO, sídlo).
- `hranicni`: `radek` = `{"id","nazev","web","druh","duvod","zdroj_url","stazeno"}`.
- `nevyresene`: `radek` = `{"id","nazev","web","otazka","moznosti","duvod","zdroj_url","stazeno"}` podle PLAN.md bod 3 (otazka `typ` / `nastroj` / `typ | nastroj`; moznosti např. `zarazen | mimo_rozsah_pilotu`; duvod = co si odporuje nebo chybí a co by otázku rozhodlo).
- `slouceno`: kandidát je duplicitou jiného kandidáta, `slouceno_do` = výsledné id, `shrnuti` = důvod s URL.
- `poznamka` v záznamu: typ a proč, identita/IČO, ticket/kapitál a proč chybí, velikosti kol (ne vklad), nástroj, jistota, „poslední investice je nejnovější nalezená, ne nutně skutečně poslední“.
- `pozadavky`: skutečně provedená volání nástrojů (spočítej je, neodhaduj). `WebFetch` = všechna volání WebFetch včetně neúspěšných, `WebFetch_neuspesne` = kolik z nich selhalo nebo vrátilo nepoužitelný obsah. `ARES` a `fundingtecheu` = počet curl požadavků na tato API. `jine_curl` = ostatní curl stažení.

## 5. Nesloučené dvojice (jen pokud ti je zadání přidělí)

Pravidlo: jedna investiční firma (správce, značka) = jeden záznam; fondy pod jedním správcem jsou podřízené údaje. Zjisti z rejstříku (ARES: statutáři, společníci, sídlo), webů a médií, jestli oba kandidáti jsou tatáž investiční firma, nebo dvě různé. Shodná adresa ani vazba (založil, spoluinvestuje) sama nestačí; rozhoduje, jestli jde o jeden investiční tým a značku, nebo jestli je jeden fondem spravovaným druhým.
- **Tatáž firma:** zpracuj jeden záznam pod id kandidáta, který představuje investiční firmu (správce/značku), do `vysledky/<to_id>.json`, a za druhého zapiš `vysledky/<druhe_id>.json` s `"vysledek": "slouceno"`, `slouceno_do` a důvodem v `shrnuti`. Zpracuj tedy oba soubory, i když druhý kandidát není v tvém seznamu.
- **Různé firmy:** zpracuj jen svého kandidáta, druhého ne.
V obou případech zapiš rozhodnutí do `vysledky/par_<id1>__<id2>.md`: rozhodnutí, důvod, doklady s URL (a jména souborů ARES, které jsi stáhl).
- `nejasnosti`: situace, kde pravidla nebyla jednoznačná, a jak jsi podle stávajících pravidel postupoval. Prázdné, pokud žádné.

Po zápisu soubor zkontroluj: `python3 -c "import json;json.load(open('<soubor>'))"`.

V závěrečné odpovědi uveď jen: id → vysledek, a nejasnosti (krátce).
