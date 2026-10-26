# Plán: spolehlivá databáze investorů

## 1. Co databáze obsahuje

Databáze investorů, kteří vkládají vlastní nebo svěřený kapitál do soukromých firem výměnou za podíl. U každého investora chci vědět:

- kdo to je (právní subjekt, země, web),
- jaký je to typ investora,
- do jakých sektorů a fází investuje,
- kolik typicky dává do jedné firmy (ticket),
- jaký má investiční kapitál, a to s rozlišením, o jaký ukazatel jde (AUM, upsaný kapitál, velikost fondu),
- kdy naposledy prokazatelně investoval,
- a u každého z těchto údajů odkud pochází a k jakému datu.

Záznam bez doložené investice do databáze nepatří, i kdyby se subjekt sám označoval za investora.

## 2. Kdo do databáze patří

Subjekt zařadím, jen když splní **všechny** tři podmínky:

1. **Je dohledatelný jako právní subjekt nebo veřejně vystupující osoba.** U firem zápis v obchodním rejstříku (v ČR justice.cz, IČO), u zahraničních ekvivalent nebo regulatorní registr. U fyzických osob veřejné vystupování jako investor pod vlastním jménem.
2. **Má doloženou přímou investici do soukromé firmy za posledních 24 měsíců.** Nutným dokladem je aspoň jedna zpráva o konkrétní transakci: tisková zpráva, zpráva v médiích, nebo záznam v databázi transakcí s odkazem na takovou zprávu. Portfolio na webu investora stačí jen tehdy, když ho potvrzuje zpráva o transakci, samo podmínku nesplní. Zápis investora jako společníka v rejstříku portfoliové firmy dokládá jen to, že investor podíl drží. Datum investice sám nedokládá (zápis může proběhnout se zpožděním a podíl mohl být nabytý dřív nebo převodem), proto ho beru jen jako podpůrný doklad vedle zprávy o transakci. Jak se v tomto okně určuje datum, popisuje bod 4.
3. **Investuje za podíl (equity nebo konvertibilní nástroj).** Ne úvěr, ne nemovitosti, ne veřejně obchodované akcie.

Typy, které rozlišuji:

| Typ | Popis |
|---|---|
| VC | Fond nebo firma investující do startupů a rychle rostoucích firem, typicky menšinové podíly |
| CVC | Korporátní venture capital, samostatná investiční jednotka velké firmy |
| PE | Kupuje podíly v zavedených, ziskových firmách, často většinové |
| Family office | Spravuje majetek jedné rodiny a investuje ho mimo jiné přímo do firem |
| Angel | Fyzická osoba investující vlastní peníze, typicky v raných fázích |
| Velký soukromý investor | Investiční holding jednoho podnikatele, který není family office v užším smyslu |

Aktivita: investor s doloženou investicí za posledních 12 měsíců má status `aktivni`, s nejnovější doloženou investicí starou 12–24 měsíců `investice_dolozena_12_24_mesicu`. Starší než 24 měsíců do vzorku nezařazuji. Hranice 12 a 24 měsíců je moje vlastní pracovní definice. Nepřebírám ji z CEE Funding Map (Warsaw Equity Group s CzechInvestem), která používá jiné kritérium: za aktivní VC považuje fond s alespoň dvěma investicemi za rok.

Status popisuje jen veřejnou stopu, ne skutečnou aktivitu. Investor může investovat, aniž by o tom vyšla zpráva, a naopak zpráva může vyjít se zpožděním. Status `investice_dolozena_12_24_mesicu` proto neznamená, že investor přestal investovat, jen že novější investici jsem nedoložil.

## 3. Kdo do databáze nepatří

- **Zprostředkovatelé a poradci:** M&A poradci, právní kanceláře, investiční zprostředkovatelé, crowdfundingové platformy. Investice zprostředkovávají, samy neinvestují.
- **Fondy fondů a čistí LP:** investují do fondů, ne do firem. Patří do jiné databáze.
- **Banky a úvěrové fondy**, včetně venture debt. Financují firmy dluhem, nekupují podíl.
- **Realitní a nemovitostní fondy**, včetně většiny „patnáctek“ (správců podle § 15 ZISIF), které investují do nemovitostí.
- **Akcelerátory a inkubátory bez vlastního kapitálu.** Pokud akcelerátor investuje vlastní peníze za podíl a má doložené investice, zařadím ho jako VC.
- **Subjekty bez doložené investice** za posledních 24 měsíců.
- **Duplicity:** jedna investiční firma = jeden záznam. Jednotlivé fondy pod jedním správcem vedu jako podřízené údaje, ne jako samostatné investory.

### Hraniční případy a jak je rozhoduji

- **Správce vs. fond.** Záznam je investiční firma (správce, značka). Důvod: obchodník oslovuje lidi z firmy, ne právní obal fondu.
- **Venture debt** (například fondy, které startupům půjčují): vyřazeno ze základní databáze, vedu je v samostatném seznamu `data/vystup_agenta/hranicni.csv`. Důvod: zadání mluví o investorech do firem a úvěr není podíl.
- **Investiční kapitál.** AUM (spravovaná aktiva), upsaný kapitál (committed capital) a velikost fondu (fund size) nejsou totéž, proto je nezaměňuji. U každého údaje ukládám částku, původní měnu, datum, ke kterému údaj platí, a druh ukazatele (`aum` / `committed_capital` / `fund_size`), jak ho uvádí sám investor nebo regulatorní registr. Částky nesčítám, pokud není jasné, že se nepřekrývají (například AUM správce obvykle zahrnuje jeho jednotlivé fondy a pozdější fond může obsahovat kapitál z dřívějšího). Když údaj nikde nenajdu, pole zůstane prázdné. Nedopočítávám ho z investic.
- **Andělé:** jen ti, kteří veřejně vystupují jako investoři pod svým jménem a mají doloženou investici. Ukládám jen pracovní údaje (jméno, role, veřejný profil), žádné soukromé kontakty. Důvod: GDPR, oprávněný zájem obstojí jen u veřejně dostupných pracovních údajů.

### Pravidla pilotu

- **Cílová skupina pilotu jsou VC/CVC se sídlem v ČR.** Jde o můj zvolený rozsah, zadání VC fondy v jedné zemi uvádí jen jako příklad menšího vzorku.
- **Pravidla pilotu splní kandidát**, který je investor podle bodů 2 a 3, jeho typ je VC nebo CVC a investiční firma (správce, značka) má sídlo v ČR.
- **Mimo rozsah pilotu, ne neinvestor.** Skutečného investora podle bodů 2 a 3, který má jiný typ (PE, family office, anděl, velký soukromý investor) nebo sídlo mimo ČR, označím jako mimo rozsah pilotu. Do pilotní databáze ho nezařadím, ale nevydávám ho za subjekt, který není investor.
- **Kategorie ve `vyrazeni.csv`.** Každý vyřazený kandidát má ve sloupci `kategorie` jednu z hodnot:
  - `neni_investor`: nesplňuje body 2 a 3 (zprostředkovatel, bez doložené investice v okně 24 měsíců, úvěr místo podílu a podobně),
  - `mimo_rozsah_pilotu`: investor podle bodů 2 a 3, ale nesplňuje typ nebo sídlo podle pravidel pilotu.

  Konkrétní důvod je ve sloupci `duvod`.
- **Měření.** Správnost zařazení a recall pilotu se vztahují ke splnění pravidel pilotu včetně typu a sídla, ne jen k bodům 2 a 3 (viz bod 7).

## 4. Struktura záznamu

Každý údaj nese vlastní zdroj. Bez URL se pole nevyplňuje. Důkazy o existenci subjektu a o investicích mají místo jednoho zdroje seznam `zdroje`, aby šlo doložit nezávislé potvrzení.

```json
{
  "id": "cz-credo-ventures",
  "nazev": "Credo Ventures",
  "typ": "VC",
  "zeme": "CZ",
  "pravni_subjekt": {
    "hodnota": "...", "ico": "...",
    "zdroje": [{"url": "...", "druh_zdroje": "rejstrik", "vydavatel": "justice.cz", "puvod": null, "zdroj_datum": "2026-05-01", "stazeno": "2026-10-23"}]
  },
  "web": {"hodnota": "...", "zdroj_url": "...", "stazeno": "..."},
  "sektory": {"hodnota": ["software", "AI"], "zdroj_url": "...", "zdroj_datum": "...", "stazeno": "..."},
  "faze": {"hodnota": ["seed", "series A"], "zdroj_url": "...", "zdroj_datum": "...", "stazeno": "..."},
  "ticket": {"min": null, "max": null, "mena": "...", "zdroj_url": "...", "zdroj_datum": "...", "stazeno": "..."},
  "kapital": [
    {"castka": null, "mena": "...", "plati_k": "...", "druh": "aum", "fond": null, "zdroj_url": "...", "zdroj_datum": "...", "stazeno": "..."}
  ],
  "posledni_investice": {
    "firma": "...", "datum_investice": null, "datum_oznameni": "2026-03-12", "datum_pro_filtr": "oznameni",
    "zdroje": [
      {"url": "...", "druh_zdroje": "zprava_o_transakci", "vydavatel": "CzechCrunch", "puvod": "https://.../tiskova-zprava", "zdroj_datum": "2026-03-12", "stazeno": "..."},
      {"url": "...", "druh_zdroje": "portfolio_web", "vydavatel": "web investora", "puvod": null, "zdroj_datum": null, "stazeno": "..."}
    ]
  },
  "dalsi_investice": [{"firma": "...", "datum_investice": "...", "datum_oznameni": "...", "datum_pro_filtr": "investice", "zdroje": ["..."]}],
  "status": "aktivni",
  "jistota": {"existence": "vysoka", "investice": "stredni"},
  "poznamka": ""
}
```

`zdroj_datum` je datum publikace zdroje, `stazeno` je den, kdy jsme zdroj četli. Částky ukládám v původní měně (kód ISO 4217) a na jinou měnu je nepřevádím.

`kapital` je seznam, protože jeden investor může mít více údajů různého druhu a k různým datům. `druh` je jedna z hodnot `aum` / `committed_capital` / `fund_size`, `plati_k` je datum, ke kterému údaj platí (může se lišit od data publikace), `fond` je název fondu u `fund_size`, jinak `null`. Údaje se nesčítají, viz bod 3.

`status` je `aktivni` nebo `investice_dolozena_12_24_mesicu`, viz bod 2.

**Zdroje důkazů.** Každá položka v `zdroje` má `url`, `druh_zdroje`, `vydavatel` (kdo zdroj zveřejnil), `puvod`, `zdroj_datum` a `stazeno`. `druh_zdroje` je u existence `rejstrik`, `regulator`, `asociace`, `media` nebo `web_subjektu`. U investice je to `zprava_o_transakci` (tisková zpráva, média, databáze transakcí s odkazem na zprávu), `portfolio_web` (web investora) nebo `rejstrik_spolecnik` (zápis společníka v rejstříku portfoliové firmy).

**Nezávislost zdrojů.** `puvod` je URL nebo název původního zdroje, ze kterého zpráva vychází, například tiskové zprávy, kterou médium převzalo. Když zpráva vychází z vlastního zjištění vydavatele, je `puvod` = `null` a původem je zdroj sám. Za nezávislé považuji jen zdroje s různým původem. Stejnou tiskovou zprávu převzatou více médii nebo databází počítám jako jeden zdroj. Společnou tiskovou zprávu investora a portfoliové firmy také počítám jako jeden zdroj.

**Datum investice a datum oznámení.** `datum_investice` je den, kdy se investice uskutečnila (podpis nebo uzavření kola), a vyplňuji ho jen tehdy, když ho zdroj výslovně uvádí. `datum_oznameni` je den, kdy byla investice poprvé veřejně oznámena. Datum publikace zdroje (`zdroj_datum`) automaticky nepovažuji za datum investice. Kola se často oznamují týdny až měsíce po uzavření. Když známe jen oznámení, zůstane `datum_investice` = `null` a datum se uloží výslovně jako `datum_oznameni`. Pokud zdroj uvádí jen měsíc nebo rok, ukládám datum ve zkráceném tvaru ISO 8601 (`2025-03`, `2025`).

**Filtr 24 měsíců.** Filtr i status z bodu 2 pracují s datem v `datum_pro_filtr`:
- `investice`: použije se `datum_investice`, když je známé,
- `oznameni`: jinak se použije `datum_oznameni`. Investice tak může být ve skutečnosti o něco starší než 24 měsíců. Toto riziko přijímám, protože oznámení je nejbližší doložitelný okamžik. Hodnotu `oznameni` ale zapisuji, aby šlo takové záznamy spočítat a zvlášť zkontrolovat.

U zkráceného data (jen měsíc nebo rok) beru pro filtr poslední den daného období a záznam označím k ruční kontrole, pokud by výsledek filtru závisel na přesném dni.

**Jistota.** `jistota` hodnotím zvlášť pro existenci subjektu a zvlášť pro investiční činnost, protože je dokládají jiné zdroje.

`jistota.existence`:
- **vysoka:** zápis v rejstříku nebo regulatorním registru,
- **stredni:** jen jiný důvěryhodný zdroj (asociace, média),
- **nizka:** jediným zdrojem je web samotného subjektu, nebo si zdroje odporují.

`jistota.investice` navazuje na podmínku 2. Záznam bez zprávy o transakci podmínku 2 nesplňuje, do databáze nepatří a jde do `data/vystup_agenta/vyrazeni.csv`. Pro zařazené záznamy tedy existují jen dvě úrovně:
- **vysoka:** investice v okně 24 měsíců doložená aspoň dvěma zprávami o transakci s různým původem,
- **stredni:** doložená jednou zprávou o transakci, případně spolu s portfoliem na webu investora nebo zápisem v rejstříku. Ty jsou jen podpůrné a nezávislé potvrzení pro úroveň `vysoka` nenahradí.

Když si zdroje k investici odporují (firma, datum, investor), záznam nezařadím, dokud rozpor ručně nevyřeším.

## 5. Zdroje

### Pro vzorek: VC v ČR

| Zdroj | K čemu |
|---|---|
| Seznam členů CVCA (Czech Private Equity & Venture Capital Association) | kandidáti, typ |
| CEE Funding Map (Warsaw Equity Group, CzechInvest, Czech Founders) | kandidáti, aktivita |
| funding.tech.eu, Dealroom (veřejná část) | doložené investice, data kol |
| Obchodní rejstřík a sbírka listin (justice.cz) | existence subjektu, IČO, výroční zprávy; společníci v portfoliových firmách jen jako podpůrný doklad, ne datum investice |
| Seznamy ČNB v databázi JERRS | licencované investiční společnosti a fondy, správci podle § 15 ZISIF |
| Registr EuVECA u ESMA | fondy s evropským označením rizikového kapitálu |
| Weby investorů | portfolio, deklarovaný ticket a sektory |
| Tiskové zprávy a média (CzechCrunch, Forbes, Hospodářské noviny) | doklad investice, částky |

Pozor na registr ČNB u „patnáctek“. ČNB tyto správce nedohlíží a údaje, které jí posílají, neověřuje. Zápis v seznamu tedy dokládá jen existenci, ne kvalitu ani investiční činnost.

### Pro rozšíření na celý svět

- **USA:** Form ADV u SEC. Poradci VC fondů, kteří nemusí registrovat, podávají zkrácený Form ADV jako exempt reporting advisers a SEC data zveřejňuje měsíčně ke stažení. Form D (oznámení o soukromých emisích) jako doklad investic.
- **EU:** registry národních regulátorů a ESMA (AIFM, EuVECA).
- **Velká Británie:** Companies House (předmět činnosti), FCA register.
- **Asociace:** Invest Europe, NVCA, BVCA a národní asociace jako CVCA, SLOVCA.
- **Otevřené agregátory:** Dealroom, funding.tech.eu, Crunchbase (omezená bezplatná část). Slouží k hledání kandidátů, ne jako jediný doklad.

## 6. Jak ověřím pravost a zařazení

Ověření má tři úrovně.

**Automaticky (skript)**
- každé vyplněné pole má `zdroj_url`, resp. aspoň jednu položku v `zdroje`,
- URL odpovídá (HTTP 200), jinak záznam spadne na kontrolu,
- poslední investice má aspoň jeden zdroj s `druh_zdroje` = `zprava_o_transakci` a datum podle `datum_pro_filtr` je v okně 24 měsíců,
- `datum_pro_filtr` = `investice` jen tehdy, když je vyplněné `datum_investice`,
- `jistota.investice` = `vysoka` jen tehdy, když mají zprávy o transakci aspoň dva různé původy (`puvod`, u `null` URL zdroje),
- deduplikace podle IČO, domény webu a normalizovaného názvu,
- typ, status, `druh` kapitálu a `druh_zdroje` jsou povolené hodnoty, částky jsou čísla, měna je kód ISO 4217.

**Kontrola druhým agentem (stejný model v nové konverzaci)**
Nová konverzace se stejným modelem, která neviděla, jak záznam vznikl, dostane jen záznam a zdroje. Má říct, jestli zdroj opravdu dokládá to, co v poli stojí. Nesoulad označí. Jde o stejný model, takže může dělat stejné chyby ve čtení zdrojů jako první agent. Jeho shoda proto není důkaz správnosti. Nenahrazuje ruční kontrolu, jen říká, kam se podívat dřív.

**Ručně (já)**
Ručně hodnotím všechny kandidáty ze vzorku, tedy zařazené i vyřazené a hraniční. Správnost zařazení a správnost vyřazení hodnotím zvlášť.

U každého zařazeného záznamu (`data/vystup_agenta/investori.json`) otevřu zdroje a vyplním plnou kontrolní tabulku:

| Pole v `hodnoceni.csv` | Otázka | `ano` / `ne` / `nelze_overit` |
|---|---|---|
| `existence` | Subjekt existuje (rejstřík nebo regulátor) | |
| `investicni_cinnost` | Investiční činnost je doložená zprávou o transakci v okně 24 měsíců | |
| `je_investor` | Je to investor podle pravidel z bodu 2 a 3 | |
| `typ` | Typ je zařazen správně | |
| `rozsah_pilotu` | Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) | |
| `posledni_investice` | Poslední investice sedí (firma, datum investice nebo oznámení podle zprávy o transakci, `datum_pro_filtr`) | |
| `nezavislost_zdroju` | Zdroje uvedené jako nezávislé mají opravdu různý původ | |
| `sektory` | Sektory odpovídají zdroji | |
| `ticket` | Ticket odpovídá zdroji | |
| `kapital` | Kapitál odpovídá zdroji (částka, měna, datum, druh ukazatele) | |

U vyřazených (`data/vystup_agenta/vyrazeni.csv`) a hraničních (`data/vystup_agenta/hranicni.csv`) kandidátů stačí zkrácená kontrola bez jednotlivých polí:

| Pole v `hodnoceni.csv` | Otázka | `ano` / `ne` / `nelze_overit` |
|---|---|---|
| `je_investor` | Je kandidát investor podle pravidel z bodu 2 a 3 | |
| `rozsah_pilotu` | Splňuje pravidla pilotu (typ VC nebo CVC, sídlo v ČR) | |
| `kategorie` | Sedí kategorie vyřazení (`neni_investor` / `mimo_rozsah_pilotu`) | |
| `duvod` | Sedí důvod vyřazení, který agent uvedl | |

## 7. Měření přesnosti

Vzorek je malý, proto ho ručně ověřím celý, ne jen náhodný výběr.

Ukládám tři věci zvlášť a žádnou nepřepisuji:

- **původní výstup agenta** (`data/vystup_agenta/`): zařazené (`investori.json`), vyřazené (`vyrazeni.csv`) i hraniční (`hranicni.csv`), přesně tak, jak je agent vytvořil. Vyřazení je také rozhodnutí agenta, proto zůstává beze změn,
- **ruční hodnocení** (`data/hodnoceni.csv`), jeden řádek na kandidáta a pole s hodnotou `ano` / `ne` / `nelze_overit` a poznámkou. Sloupec `soubor` říká, ze kterého souboru výstupu agenta kandidát pochází,
- **opravenou verzi** (`data/opraveno/`), která vznikne až po ručním hodnocení. Má stejné soubory jako výstup agenta a kandidát se v ní může přesunout mezi zařazenými a vyřazenými.

Přesnost měřím na původním výstupu agenta, ne na opravené verzi.

Hodnotu `nelze_overit` vykazuji samostatně. Nepočítám ji jako správnou ani jako chybnou. U každého čísla uvedu počty `ano`, `ne` a `nelze_overit` a dvě přesnosti:

- **přesnost na ověřitelných:** `ano` / (`ano` + `ne`), tedy jen na záznamech, které šlo ověřit,
- **konzervativní spodní hranice:** `ano` / všechny posouzené, jako by každé `nelze_overit` bylo chybou.

Rozdíl mezi nimi ukazuje, jak moc výsledek závisí na tom, co nešlo ověřit.

Měřím čtyři věci:

1. **Přesnost zařazení (precision):** podíl zařazených záznamů, které splňují pravidla pilotu, tedy jsou investor podle bodů 2 a 3 (`je_investor` = `ano`), mají typ VC nebo CVC a sídlo v ČR (`rozsah_pilotu` = `ano`). Tohle je hlavní číslo, protože zadání říká, že databáze nesmí obsahovat náhodné firmy. Zvlášť uvedu, kolik chybně zařazených je skutečný investor mimo rozsah pilotu a kolik není investor vůbec.
2. **Přesnost po polích:** pro každé pole zařazených záznamů zvlášť podíl správných hodnot mezi vyplněnými a zvlášť podíl vyplněných. Ticket a kapitál budou vyplněné výrazně méně často než existence a poslední investice.
3. **Správnost vyřazení:** zvlášť pro vyřazené a hraniční podíl kandidátů, kteří podle ruční kontroly opravdu nesplňují pravidla pilotu (`je_investor` = `ne` nebo `rozsah_pilotu` = `ne`), zvlášť podíl, u kterých sedí kategorie vyřazení (u `neni_investor` musí být `je_investor` = `ne`, u `mimo_rozsah_pilotu` musí být `je_investor` = `ano` a `rozsah_pilotu` = `ne`), a zvlášť podíl, u kterých sedí důvod vyřazení. Skutečný investor vyřazený jako `neni_investor` je chyba kategorie, i když vyřazení z pilotu je správné.
4. **Úplnost (recall) v rámci prověřeného souboru kandidátů:** ze všech kandidátů, kteří podle ruční kontroly splňují pravidla pilotu (`je_investor` = `ano` a `rozsah_pilotu` = `ano` u zařazených, vyřazených i hraničních), podíl, který agent zařadil. Číslo platí jen pro kandidáty, které jsme prověřili. Neříká nic o investorech, kteří se mezi kandidáty vůbec nedostali, a proto ho nevykazuji jako úplnost všech investorů na trhu. Mezi kandidáty nejsou ani subjekty, jejichž sídlo se při sběru nepodařilo doložit (`nevyreseno_sidlo` v `ai-log/01-kandidati/opravy_sberu.csv`). Tuto nejistotu uvedu u recallu i u místního rozsahu (bod 8.3).

U každého podílu s jasným čitatelem a jmenovatelem (obě přesnosti, správnost vyřazení, recall v rámci prověřeného souboru) uvedu 95% Wilsonův interval spolehlivosti, aby bylo vidět, jak moc se dá číslu věřit. Při 40 záznamech a přesnosti 90 % je interval zhruba 77–96 %. Při nulovém jmenovateli uvedu místo podílu i intervalu N/A. Interval popisuje jen nejistotu podílu v pilotu danou velikostí vzorku. Nevypovídá o úplnosti trhu ani o nejistotě globálního scénáře z bodu 8.

Pro každou chybu zapíšu do sloupce `pricina_chyby`, kde vznikla: `spatny_zdroj`, `chybne_cteni` (agent zdroj špatně přečetl), `zastaraly_udaj` nebo `chyba_pravidel`. To je podklad pro README.

## 8. Odhad rozsahu a spolehlivosti

Sekce má dvě oddělené části: doložené statistiky ze zdrojů a moje vlastní odhady počtu investorů, kteří splňují pravidla z bodů 2 a 3. Statistiky počítají subjekty podle definic svých autorů, ne podle našich pravidel, a nejsou tedy počtem záznamů, které databáze bude mít.

### 8.1 Doložené statistiky ze zdrojů

Údaje a definice jsem ověřil ve zdrojích 26. 10. 2026. U zdrojů, které rok dat neuvádějí, uvádím datum publikace.

| Údaj | Rok | Zdroj | Co se počítá |
|---|---|---|---|
| 2 271 poradců VC fondů v USA | 2025 | SEC, Investment Adviser Statistics, tabulka 1.1b (zpráva ze srpna 2026) | Exempt reporting advisers, kteří ve Form ADV uvedli výjimku pro poradce VC fondů. Řádky tabulky se mohou překrývat, protože poradce může uvést víc výjimek. Nezahrnuje poradce VC registrované u SEC jako RIA. Počítá správce, ne investice. |
| 4 000–7 000 VC firem ve světě, z toho zhruba 2 500 v USA | rok dat neuveden, článek z 4. 1. 2025 | Decile Group | Rozpětí cizích odhadů počtu „operating VC firms“, tedy firem, které získávají kapitál do fondu nebo ho investují. Nestanoví minimální počet investic za období. |
| zhruba 7 000 PE firem ve světě, z toho 6 000 v USA | rok neuveden | American Investment Council, citováno podle Vault (sekundární zdroj) | Firmy private equity. Definici zdroj neuvádí. |
| 8 030 single family office ve světě | 2024 | Deloitte, Defining the Family Office Landscape 2024 | Odhad počtu single family office celkem, bez ohledu na to, zda investují přímo do firem. Podklad je mimo jiné průzkum 354 SFO. |
| přes 10 000 aktivních firem v private capital | 2019 | Preqin, citováno podle Opalesque (sekundární zdroj) | Firmy v celém private capital. Které třídy aktiv zahrnuje, článek neuvádí. **Nejde o počet PE firem a jako odhad PE ho nepoužívám.** |

Pro anděly žádnou statistiku nemám, registr neexistuje.

### 8.2 Vlastní odhady (pracovní hypotézy)

Odhady se týkají jen subjektů, které splní pravidla z bodů 2 a 3, tedy i podmínku doložené investice za posledních 24 měsíců.

**ČR, VC a CVC se sídlem v ČR:** pracovní hypotéza 30–50 subjektů. Je to odhad bez výpočtu. Neodvozuji ho z počtu investičních kol, protože do kol vstupují i zahraniční investoři a jeden investor může být v několika kolech. Tuto hypotézu pilot přímo ověří.

**Svět: scénář s výpočtem.** Počet před filtrem beru ze statistik v 8.1, Preqin nepoužívám. Podíl, který projde pravidly z bodu 2, je **předpoklad**, ne změřená hodnota.

| Typ | Před filtrem (8.1) | Předpoklad: podíl, který projde bodem 2 | Scénář |
|---|---|---|---|
| VC | 4 000–7 000 (Decile Group) | 60–80 % | 2 400–5 600 |
| PE | zhruba 7 000 (American Investment Council) | 40–60 % | 2 800–4 200 |
| Family office | 8 030 (Deloitte 2024) | 5–15 % | 400–1 200 |
| **Celkem** | | | **zhruba 5 600–11 000** |

Proč takové předpoklady:
- **VC 60–80 %:** Decile počítá firmy, které získávají kapitál do fondu nebo ho investují. Část z nich za 24 měsíců neinvestovala (například mezi fondy). VC kola se ale zpravidla veřejně oznamují, startupy o nich samy informují.
- **PE 40–60 %:** PE firmy dělají méně transakcí a menší transakce se často neoznamují. Údaj AIC nemá definici ani rok, takže může zahrnovat i neaktivní firmy.
- **Family office 5–15 %:** většina family office investuje přes fondy nebo nic nezveřejňuje. Údaj Deloitte navíc počítá všechny single family office, ne jen ty, které investují přímo.

Omezení scénáře:
- **Překryv VC a PE:** firmy s více strategiemi mohou být v obou statistikách, součet je proto spíš horní odhad.
- **Co ve scénáři chybí:** CVC, andělé a velcí soukromí investoři, protože pro ně v 8.1 nemám statistiku. U CVC je proto scénář podhodnocený. Anděly bez registru početně neodhaduji a kvalitně pokryji jen ty z veřejných angel sítí a tiskových zpráv.
- **Nejistý základ:** statistiky z 8.1 mají různé definice a roky, AIC je navíc citovaný ze sekundárního zdroje.

Očekávaná spolehlivost záznamů podle typu (hypotéza):

| Typ | Očekávaná spolehlivost |
|---|---|
| VC | vysoká u existence a aktivity, střední u ticketu, nízká až střední u kapitálu |
| PE | vysoká u existence, střední u kapitálu (velké firmy ho zveřejňují) |
| Family office | nízká, jen ty, které se objeví ve zprávách o transakcích |
| Angel | nízká, kvalitně jen ti z veřejných angel sítí a tiskových zpráv |

### 8.3 Co ověří český pilot

Pilot (VC a CVC v ČR) ověří místní výsledky a náročnost zpracování:

1. **Místní rozsah:** kolik kandidátů ze seznamů CVCA, CEE Funding Map a dalších zdrojů z bodu 5 splní pravidla pilotu (body 2 a 3, typ VC nebo CVC, sídlo v ČR), tedy ověření hypotézy 30–50 pro ČR. Výsledek uvedu spolu s počtem subjektů s nevyřešeným sídlem ze sběru (`nevyreseno_sidlo`). Ty mezi kandidáty nejsou, takže skutečný počet může být vyšší, nejvýš o jejich počet.
2. **Místní přesnost:** přesnost zařazení a po polích podle bodu 7 a hypotéza z 8.4, obojí pro VC a CVC v ČR.
3. **Náročnost zpracování:** tokeny, počet stažených stránek a čas ručního ověření na jeden záznam a podíl záznamů, které potřebují ruční kontrolu (podklad pro bod 10).

Globální odhady z 8.2 pilot nepotvrdí ani nevyvrátí. Zůstanou scénáři s uvedenými omezeními. Naměřený podíl kandidátů, kteří v ČR projdou pravidly, je jen orientační vstup do scénáře: porovnám ho s předpoklady v 8.2, a pokud se výrazně liší, scénář přepočítám a uvedu oba výsledky. Proč český podíl nelze přenést přímo:

- pilot pokrývá jen VC a CVC, ne PE, family office ani anděly,
- ČR je malý trh s jinou strukturou investorů než USA nebo západní Evropa,
- dostupnost zdrojů se liší: ČR má veřejný obchodní rejstřík se sbírkou listin, USA Form ADV, jinde mohou být rejstříky placené nebo neúplné,
- mediální pokrytí transakcí se liší podle země a jazyka, a s ním i to, kolik investic půjde doložit,
- kandidáti v ČR pocházejí ze seznamů (CVCA, CEE Funding Map), ne ze statistik z 8.1, takže podíl se počítá z jiného základu,
- vzorek je malý, takže naměřený podíl má široký interval spolehlivosti (viz bod 7).

### 8.4 Hypotéza ke spolehlivosti po polích

Pilot ji ověří jen pro VC a CVC v ČR. Pro ostatní typy a země zůstává hypotézou:
- existence a typ: přes 90 % správně,
- poslední investice: přes 90 % správně tam, kde je vyplněná,
- sektory: kolem 80 %, protože investoři je popisují různě,
- ticket: vyplněný u menšiny, správnost střední,
- celkový kapitál: vyplněný u menšiny, často zastaralý.

## 9. Postup v Claude Code

1. **Kandidáti:** agent stáhne seznamy ze zdrojů v bodě 5 a vytvoří `data/kandidati.csv`. Bez posuzování.
2. **Obohacení:** pro každého kandidáta agent dohledá pole podle schématu. Pravidlo: když údaj nenajde, nechá `null`. Odhad nebo údaj bez URL je chyba.
3. **Zařazení:** agent rozhodne podle bodů 2 a 3 a podle pravidel pilotu (bod 3, Pravidla pilotu), jestli kandidát patří do databáze, a důvod zapíše. Zařazené jdou do `data/vystup_agenta/investori.json`, vyřazené do `data/vystup_agenta/vyrazeni.csv` s kategorií (`neni_investor` / `mimo_rozsah_pilotu`) a důvodem, venture debt do `data/vystup_agenta/hranicni.csv`.
4. **Automatická kontrola:** skript z bodu 6.
5. **Kontrola druhým agentem** (stejný model v nové konverzaci): kontrola zdrojů.
6. **Ruční ověření:** plná kontrolní tabulka u zařazených, zkrácená u vyřazených a hraničních, vše do `data/hodnoceni.csv`. Původní výstup agenta zůstává beze změny, opravy jdou do `data/opraveno/`.
7. **Měření a zápis výsledků.**

Všechny konverzace exportuji do `ai-log/` a do README zapíšu, kde se agenti spletli.

### Soubory projektu

Každý soubor má jeden účel, souběžné verze pod jinými názvy nevznikají. `id` přidělí kandidátovi `data/kandidati.csv` a kandidát ho pak nese beze změny v `investori.json`, `vyrazeni.csv`, `hranicni.csv` i `hodnoceni.csv`.

| Soubor | Obsah |
|---|---|
| `data/kandidati.csv` | kandidáti ze seznamů, sloupce `id,nazev,web,zdroj_seznamu,zdroj_url,stazeno` |
| `data/vystup_agenta/investori.json` | původní výstup agenta: zařazení, seznam záznamů podle bodu 4, beze změn |
| `data/vystup_agenta/vyrazeni.csv` | původní výstup agenta: vyřazení kandidáti, sloupce `id,nazev,web,kategorie,duvod,zdroj_url,stazeno`, `kategorie` je `neni_investor` nebo `mimo_rozsah_pilotu`, beze změn |
| `data/vystup_agenta/hranicni.csv` | původní výstup agenta: hraniční případy (venture debt), sloupce `id,nazev,web,druh,duvod,zdroj_url,stazeno`, beze změn |
| `data/hodnoceni.csv` | ruční hodnocení všech kandidátů, sloupce `soubor,id,pole,hodnoceni,pricina_chyby,poznamka,hodnotil,datum` |
| `data/opraveno/` | opravená verze po ručním hodnocení, stejné soubory a schéma jako `data/vystup_agenta/` |
| `scripts/` | skripty pro automatickou kontrolu a měření |
| `ai-log/` | exporty konverzací s agenty |

## 10. Odhad nákladů na celý svět

Spočítám po vzorku, protože teprve tam změřím skutečné hodnoty:

- tokeny a počet stažených stránek na jeden záznam,
- čas ručního ověření na jeden záznam,
- podíl záznamů, které potřebují ruční kontrolu (jistota střední a nízká).

Vzorec:

```
náklady = počet záznamů × (cena tokenů na záznam + cena vyhledávání na záznam)
        + počet záznamů k ruční kontrole × čas na záznam × hodinová sazba
        + údržba (opakované ověření aktivity, např. každých 6 měsíců)
```

Předpokládám, že největší položkou nebude AI, ale ruční kontrola. Proto bude důležité, jak přesně umí automatická kontrola a kontrola druhým agentem vytřídit záznamy, které se ručně kontrolovat nemusí.

## Zdroje k číslům v plánu

- SEC, Investment Adviser Statistics, Number of Advisers (srpen 2026): https://www.sec.gov/data-research/statistics-data-visualizations/investment-adviser-statistics/investment-advisers-number-advisers
- SEC, data k tabulce 1.1b (srpen 2026): https://www.sec.gov/files/2026-08/Number_of_Advisers_08-12-2026.json
- Decile Group, odhad počtu VC firem (článek z 4. 1. 2025): https://decilegroup.com/posts/many-firms-united-states-approach-counting-number-firms-much-capital-deployed-2024
- Deloitte, Defining the Family Office Landscape 2024: https://www.deloitte.com/content/dam/assets-shared/docs/services/deloitte-private/2024/2024-defining-the-family-office-landscape-executive-report.pdf a https://www.deloitte.com/global/en/services/deloitte-private/research/defining-the-family-office-landscape.html
- Vault, Private Equity: The Industry Today (údaj American Investment Council): https://legacy.vault.com/industries-professions/industries/private-equity/the-industry-today
- Opalesque o Preqin 2019: https://www.opalesque.com/672699/250000_people_worldwide_working_in_the_private_equity269.html
- CzechInvest, CEE Funding Map (květen 2026): https://czechinvest.gov.cz/en/Homepage/Novinky/Kveten-2026/CEE-Funding-Map-prinasi-prehled-aktivnich-investor
- ČNB, role ČNB u správců podle § 15 ZISIF: https://www.cnb.cz/cs/o_cnb/vlog-cnb/Investovani-do-alternativnich-fondu
- SEC, data Form ADV pro exempt reporting advisers: https://sec.gov/help/foiadocsinvafoiahtm.html
