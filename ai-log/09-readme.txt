
❯ Krok 9: finální README pro odevzdání praktické úlohy.

  Přečti současné README.md, PLAN.md, NAKLADY.md, LICENSE,
  data/mereni_vzorku.md, data/opraveno/ZMENY.md,
  data/opraveno/stav_kontroly.csv, relevantní exporty v ai-log/
  a pracovní podklad ~/Downloads/CHYBY.md (chyby, zpřesnění
  a rozhodnutí z kroků 0–8; do repa ho nekopíruj ani necommituj).

  Přepiš README do konečné podoby. Piš česky, v první osobě (já = Petr),
  stručně a konkrétně, bez reklamních a výplňových frází a bez emoji.
  Čtenář má během několika minut pochopit výsledek, postup, naměřenou
  kvalitu a omezení. README nemá opakovat celé PLAN.md ani NAKLADY.md.

  Zahrň:

  1. Výsledek a odkazy:
     57 vstupních kandidátů, po jednom sloučení 56 subjektů.
     Původní výstup: 27 zařazených.
     Opravený výstup: 22 zařazených, 19 vyřazených,
     14 nevyřešených, 1 hraniční.
     22 zařazených neznamená 22 plně ověřených: 7 nebylo v kontrolním
     vzorku a další mají popsané výhrady (stav_kontroly.csv).
     Odkazy na plán, původní a opravená data, stav kontroly, hodnocení,
     měření a náklady. Rozliš skutečné investory mimo pilot a neinvestory.

  2. Pravidla a zdroje:
     stručně rozsah českého VC/CVC pilotu, sídlo správce,
     doložená investice v posledních 24 měsících, nástroje,
     práce s kapitálem a chybějícími údaji.
     Zachovej atribuci Tech.eu Funding Explorer, odkaz
     na použité API a licenci CC BY 4.0. LICENSE neměň.

  3. Měření:
     náhodný výběr 20 z 27 původně zařazených, seed 20261027
     (scripts/vyber_vzorku.py, data/vzorek_kontroly.csv). Uveď skutečný
     postup výběru podle dostupných podkladů: výběr je reprodukovatelný
     ze seedu; okamžik losování log nedokládá.
     Přesnost zařazení 15/17 = 88,2 %, další 3 případy
     neověřené; konzervativní podíl 15/20 = 75 %.
     Správnost vyplněných polí 156/163 = 95,7 %,
     dalších 12 polí nelze ověřit; nejslabší posledni_investice.
     Wilsonovy intervaly převezmi z výstupu skriptu.
     Sloučení Nation1 vykazuj odděleně.
     Rozliš dvě změny výkladu metodiky od chyb agenta.
     Nevykazuj 100% kvalitu databáze.
     Recall ani úplnost českého trhu nebyly změřeny.
     Měření platí pro původní výstup, opravená verze
     nemá nové nezávislé hodnocení.

  4. Jak jsem pracoval s AI:
     první návrh plánu vznikl v chatu, implementace a sběr v Claude Code;
     práce byla rozdělena do session, jejichž exporty jsou v ai-log/
     (přesné rozdělení ověř podle historie); ChatGPT a Claude v chatu
     pomáhaly s recenzemi, vyhledáním, překladem a návrhy hodnocení.
     Popiš konkrétní pokyny agentům po krocích 0–8 a kontroly jejich
     výstupů.
     Zachovej oddíl „Ruční kontrola – kdo hodnotil“: štítek
     „Petr Šťastný (asistence AI)“ znamená schválení navržených verdiktů,
     nikoli osobní otevření všech zdrojů. Stav před přečtením nálezů
     kontrolního agenta je uložen zvlášť (commit 35583d9).
     Kontrola není nezávislý referenční standard.
     Druhý agent byl stejný model v jiné konverzaci.
     Srovnání jeho přínosu je orientační; 3 ze 4 chyb výstupu ruční
     kontrola našla až po přečtení jeho nálezů.

  5. Chyby a opravy (podle CHYBY.md, ověřené v repu):
     shrň doložené chyby návrhu, sběru, obohacení, kontroly a měření.
     Zahrň zejména kapitálové ukazatele, vlastní definici aktivity,
     použití API přes původní zákaz náhradního nástroje
     a následné schválení, historický zápis i&i Prague,
     nedoložené přiřazení investic fondu Tech Horizons k Presto Ventures
     (vazba není doložena, ale ani vyvrácena),
     přehlédnuté novější investice Look AI/Purple/Reflex/ZAKA,
     chybějící ticket N1, sloučené intervaly i&i Biotech
     a tokeny v mereni.txt (velikost kontextu, ne spotřeba).
     Zahrň chyby postupu a bezpečnosti: stažení přes curl -k bez ověření
     TLS, přepsané surové odpovědi a pokus obejít ochranu proti botům
     na zaka.vc. U každé uveď odkaz na konkrétní místo v logu (soubor
     v ai-log/ a hledatelný úsek), rozliš provedenou akci od zamítnutého
     pokusu a pokud náprava neproběhla, napiš „nenapraveno, uvedeno jako
     omezení“. Co v logu nedohledáš, neuváděj jako doložené.
     Odděl chybu pravidel, chybnou aplikaci pravidla,
     omezení schématu a nezjištěnou příčinu.
     Uveď i chyby kontrolující AI (Claude v chatu i ChatGPT): původně
     schválené údaje následně opravené podle dalších důkazů, přehlédnuté
     investice, chybný kontrolní součet 157/156.
     U každé chyby: co, kdo našel, jak vyřešeno.
     Nevymýšlej nedoložené chyby ani osobní kontroly.

  6. Náklady:
     krátké shrnutí pilotu a tří globálních variant podle aktuálního
     NAKLADY.md. Odliš API přepočet od zaplaceného předplatného,
     měření od modelových předpokladů a známou spotřebu
     od nezachycené. Globální rozsah je scénář, ne změřený počet investorů.

  7. Omezení a nedokončené části:
     sedm zařazených mimo kontrolní vzorek,
     nekontrolovaná původní vyřazení a nevyřešené případy,
     výhrady k sídlu, nezávislosti zdrojů a nejnovější investici,
     KAYA (lucemburský AIFM, stejné pravidlo sídla, neposouzeno;
     a známý nález u kapitálu), PerfectBit u ZAKA.
     ZAKA FinalDose se při tvorbě oprav nepodařilo znovu načíst;
     oprava vychází z předchozího hodnocení s asistencí AI
     a z kontroly druhým agentem.
     Pozdější datum stažení zdroje samo neznamená,
     že informace neplatila k referenčnímu datu.

  8. Spuštění:
     ověř skutečné argumenty skriptů a uveď funkční příkazy
     pro výběr vzorku, kontrolu dat, měření, náklady a opravy.
     Rozliš běh bez sítě od kontroly URL.
     Upozorni na skripty, které přepisují generované výstupy.
     Agregace lokálních Claude logů vyžaduje původní logy;
     výpočet nákladů musí fungovat z uloženého spotreba.csv.

  9. Struktura repa (podle git ls-files) a licence.

  Čísla, commity a cesty ověřuj v repu, nic nepiš zpaměti. Kde se
  CHYBY.md a repo liší, platí repo a rozdíl mi vypiš.
  Data, plán a výsledky měření neměň, měň jen README.md.
  Zkontroluj relativní odkazy a soulad čísel.
  Ukaž celé navržené README a seznam rozdílů mezi CHYBY.md a repem.
  Zatím necommituj.

⏺ Začnu průzkumem repa a podkladů.

⏺ Bash(git ls-files && echo ---- && git log --oneline | head -60 && echo ---- &&
      wc -c README.md PLAN.md NAKLADY.md LICENSE data/mereni_vzorku.md
      data/opraveno/ZMENY.m…)
  ⎿  Error: Exit code 1
     .gitignore
     LICENSE
     NAKLADY.md
     PLAN.md
     README.md
     ai-log/.gitkeep
     ai-log/00-plan-a-zalozeni.txt
     ai-log/01-kandidati.txt
     ai-log/01-kandidati/mimo_rozsah.csv
     … +202 lines (ctrl+o to expand)

  Listed 1 directory (ctrl+o to expand)

⏺ Bash(mdfind -name CHYBY 2>/dev/null | head; find ~/Downloads ~/Desktop
      ~/Documents -maxdepth 4 -iname "*chyb*" 2>/dev/null | head; ls ~/Downloads
      | head -50)
  ⎿  (No output)

  Listed 1 directory (ctrl+o to expand)

⏺ Soubor ~/Downloads/CHYBY.md jsem nenašel (ani jinde v domovském adresáři).
  Budu tedy postupovat podle bodů ze zadání jako podle kontrolního seznamu a
  každý ověřím v repu a logu, výsledky shrnu na konci.

  Read 2 files (ctrl+o to expand)

⏺ Bash(wc -c ai-log/*.txt && for f in scripts/*.py; do echo "=== $f"; head -40
      "$f" | grep -n -E '"""|^#|Použití|python3' ; grep -n -E
      "add_argument|sys.argv|open\(.*[…)
  ⎿  (No output)

⏺ Čtu skripty a logy; zatím jsem nic neměnil.

⏺ Bash(cat scripts/vyber_vzorku.py; sed -n 1,30p scripts/zkontroluj_data.py; sed
      -n 1,20p scripts/oprav.py; sed -n 1,32p scripts/spotreba_z_logu.py; sed
      -n 1,16p scrip…)
  ⎿  (No output)

⏺ Ověřím, že skripty bez sítě reprodukují uložené výstupy (spouštím v dočasné
  kopii repa, aby se nic v repu nepřepsalo).

⏺ Bash(S=/private/tmp/claude-501/-Users-petrstastny-Documents-Projekty-investori
      -databaze/e91dd674-49a9-425e-8727-f62590611dd3/scratchpad/kopie && rm -rf
      $S && mkdir -…)
  ⎿  (No output)

⏺ Bash(cd /private/tmp/claude-501/-Users-petrstastny-Documents-Projekty-investor
      i-databaze/e91dd674-49a9-425e-8727-f62590611dd3/scratchpad/kopie && git
      diff --stat; gi…)
  ⎿  (No output)

⏺ Skripty bez sítě vrací uložené výstupy beze změny, kromě zkontroluj_data.py
  bez --over-url, který přepíše zprávu automaticka_kontrola.md vytvořenou s
  kontrolou URL. Teď dohledám jednotlivé chyby v logu.

⏺ Bash(cd /Users/petrstastny/Documents/Projekty/investori-databaze/ai-log &&
      head -60 00-plan-a-zalozeni.txt; for f in *.txt; do echo "== $f"; head -c
      600 "$f" | head…)
  ⎿  (No output)

⏺ Bash(for f in *.txt; do echo "=========== $f"; awk '/^❯ /{p=1} /^⏺ /{p=0} p'
      "$f" | grep -v "ide_opened_file\|may or may not\|in the IDE\|^  /Users" |
      head -c 6000;…)
  ⎿  (No output)

  Read 1 file (ctrl+o to expand)

⏺ Bash(cd /Users/petrstastny/Documents/Projekty/investori-databaze && git log
      --format='%h %ad %s' --date=iso --name-only --diff-filter=AM --
      'ai-log/*.txt' && cmp <(h…)
  ⎿  (No output)

⏺ Bash(cd /Users/petrstastny/Documents/Projekty/investori-databaze/ai-log &&
      diff <(head -260 05-priprava.txt) <(head -260
      05-rucni-kontrola-ulozeni.txt) | head -30; g…)
  ⎿  (No output)

⏺ Exporty odpovídají sessionům 0–8; krok 5 je jedna session exportovaná dvakrát
  (05-priprava.txt je začátek, 05-rucni-kontrola-ulozeni.txt celá). Hledám
  jednotlivé chyby v logu.

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 4280,4330p 02-obohaceni.txt; echo ----; sed -n 4775,4795p
      02-obohaceni.txt; grep -n -i "curl -k\|TLS\|certifik"
      02-obohaceni/nejasnosti.md 02-obohaceni/m…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 1370,1385p 02-obohaceni.txt; echo ----; sed -n 2265,2280p
      02-obohaceni.txt; echo ----; sed -n 2464,2476p 02-obohaceni.txt; echo; sed
      -n 5148,5158p 02-obo…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)
⏺ Bash(sed -n 2850,2860p 02-obohaceni.txt; echo; sed -n 5135,5175p
      02-obohaceni.txt)
  ⎿  (No output)

⏺ Ověřuji v gitu přepsané soubory ARES a dál hledám zaka.vc a ostatní body.

⏺ Bash(cd /Users/petrstastny/Documents/Projekty/investori-databaze && for f in
      ares_hledani_iiPrague.json ares_vr_06058485.json; do git log --format='%h
      %s' -- "ai-log…)
  ⎿  (No output)

⏺ Bash(sed -n 400,422p ai-log/08-opraveno.txt)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 95,112p ai-log/00-plan-a-zalozeni.txt; sed -n 130,140p
      ai-log/00-plan-a-zalozeni.txt; sed -n 360,366p
      ai-log/00-plan-a-zalozeni.txt)
  ⎿  (No output)

⏺ Bash(python3 - <<'E'
      import csv…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Kontrolní součet 157/156 je doložený v 06-mereni.txt. Teď ověřuji v logu kroku
  2 ZAKA/FinalDose, N1 ticket, i&i Biotech a i&i Prague.

⏺ Bash(grep -n "FinalDose\|Typical 1st\|100K\|business creation\|150 000\|150
      tis\|ticket" ai-log/02-obohaceni.txt | head -30; sed -n 241,256p
      ai-log/06-mereni.txt)
  ⎿  (No output)

⏺ Bash(sed -n 4455,4475p ai-log/02-obohaceni.txt; python3 -c "
      import json;d=json.load(open('data/vystup_agenta/investori.json'))…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n '10,11p;12p' data/hodnoceni.csv; grep -n "cz-nation1"
      data/hodnoceni.csv; grep -n -i "api/v1\|429\|Vercel\|náhradní\|robots"
      ai-log/01-kandidati.txt | he…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 4402,4410p ai-log/02-obohaceni.txt; sed -n 2880,2890p
      ai-log/02-obohaceni.txt)
  ⎿  (No output)

⏺ Mám doklady k většině bodů. Dohledávám ještě i&i Prague (rejstřík 2020) a
  KAYA, pak píšu README.

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 2226,2260p ai-log/02-obohaceni.txt)
  ⎿  (No output)

⏺ Bash(python3 -I - <<'E'
      import json,re…)
  ⎿  (No output)

⏺ Bash(python3 - <<'E'
      import csv,collections…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Ověřuji ještě závislosti skriptů a chování spotreba_z_logu.py bez logů.

⏺ Bash(grep -h -E "^(import|from) " scripts/*.py | sort -u; python3 --version;
      sed -n 130,165p scripts/spotreba_z_logu.py | grep -n -i
      "exit\|exists\|nenalez\|chyb" ;…)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(cd /private/tmp/claude-501/-Users-petrstastny-Documents-Projekty-investor
      i-databaze/e91dd674-49a9-425e-8727-f62590611dd3/scratchpad/kopie && git
      checkout -q . &…)
  ⎿  (No output)

⏺ Skript spotreba_z_logu.py teď skončí chybou na kroku 8 a dalších, aniž by
  přepsal spotreba.csv — zmíním to v README. Teď ověřím, že odkazované úseky
  jsou v logu doslovně.
⏺ Bash(chk(){ n=$(grep -c -F -- "$2" "$1"); echo "$n | $1 | $2"; }
      chk ai-log/00-plan-a-zalozeni.txt "Kapitál: AUM, upsaný kapitál a velikost
      fondu nejsou totéž"…)
  ⎿  (No output)

⏺ Bash(chk(){ n=$(grep -c -F -- "$2" "$1"); echo "$n | $1 | $2"; }
      chk ai-log/04-kontrola-zdroju.txt "Embodied"…)
  ⎿  (No output)

⏺ Kontroluji ještě, co se v kroku 5 změnilo ve vyber_vzorku.py, abych správně
  popsal výběr vzorku.

⏺ Bash(grep -n -i "vyber_vzorku\|seed\|liší\|shodn"
      ai-log/05-rucni-kontrola-ulozeni.txt | sed -n 1,40p)
  ⎿  (No output)

⏺ Bash(sed -n 690,745p ai-log/05-rucni-kontrola-ulozeni.txt)
  ⎿  (No output)

⏺ Bash(python3 -c "
      import csv,collections…)
  ⎿  (No output)

⏺ Bash(python3 -c "
      import csv…)
  ⎿  (No output)

⏺ Mám podklady ke všem bodům. Zbývá přečíst LICENSE a pak README napíšu.

⏺ Bash(cat LICENSE; echo; sed -n 55,80p README.md | head -5; git ls-files | awk
      -F/ '{print $1"/"$2}' | sort | uniq -c)
  ⎿  (No output)

⏺ Píšu README.

⏺ Write(README.md)
  ⎿  Added 218 lines, removed 71 lines
        1  # Databáze investorů
        2  
        3 -Praktická úloha ve výběrovém řízení na pozici Junior AI Develo
          -per ve společnosti Clientelo.                                 
        3 +Praktická úloha ve výběrovém řízení na pozici Junior AI Develo
          +per ve společnosti Clientelo. Zadání: pomocí AI agentů sestavi
          +t spolehlivou databázi investorů, kteří vkládají vlastní nebo 
          +svěřený kapitál do soukromých firem za podíl, ověřit postup na
          + pilotu a změřit jeho přesnost, odhadnout počet investorů ve s
          +větě a náklady na zpracování celého světa.                    
        4  
        5 -## Zadání                                                     
        5 +Pilot jsem udělal pro VC a CVC se sídlem v ČR. Pravidla, schém
          +a záznamu a metodika měření jsou v [PLAN.md](PLAN.md), odhad n
          +ákladů v [NAKLADY.md](NAKLADY.md).                            
        6  
        7 -Sestavit pomocí AI agentů spolehlivou databázi investorů, kteř
          -í vkládají vlastní nebo svěřený kapitál do soukromých firem vý
          -měnou za podíl (VC, CVC, PE, family office, andělé). Databáze 
          -nesmí obsahovat náhodné firmy. Každý údaj musí mít doložený zd
          -roj a datum.                                                  
        7 +## Výsledek                                                   
        8  
        9 -Součástí úlohy je:                                            
        9 +Ze 4 zdrojů jsem sestavil 57 kandidátů. Po sloučení Nation1 do
          + N1 Ventures zbylo 56 subjektů.                               
       10  
       11 -- ověřit postup na pilotním vzorku (VC a CVC v ČR) a změřit je
          -ho přesnost,                                                  
       12 -- odhadnout, kolik investorů lze z veřejných zdrojů dohledat v
          -e světě,                                                      
       13 -- odhadnout náklady na zpracování celého světa.               
       11 +| | původní výstup agenta | opravená verze (krok 8) |         
       12 +|---|---|---|                                                 
       13 +| zařazení (VC/CVC se sídlem v ČR) | 27 | **22** |            
       14 +| vyřazení, z toho `mimo_rozsah_pilotu` / `neni_investor` | 17
          + (15 / 2) | **19** (17 / 2) |                                 
       15 +| nevyřešení (k ručnímu rozhodnutí) | 11 | **14** |           
       16 +| hraniční (venture debt) | 1 | **1** |                       
       17 +| celkem | 56 | 56 |                                          
       18  
       15 -Postup, pravidla zařazení, struktura záznamu a způsob měření j
          -sou popsané v [PLAN.md](PLAN.md).                             
       19 +- **22 zařazených neznamená 22 plně ověřených.** 7 z nich neby
          +lo v kontrolním vzorku a ručně je nikdo nekontroloval. U zbylý
          +ch 15 je stav v [stav_kontroly.csv](data/opraveno/stav_kontrol
          +y.csv): 4 s opravou poslední investice, 2 s polem, které nešlo
          + ověřit, a 9 se všemi hodnocenými poli `ano`. I mezi nimi mají
          + některé záznamy výhrady, například Credo, Rockaway nebo Start
          +upYard.                                                       
       20 +- **Mimo pilot není totéž co neinvestor.** `mimo_rozsah_pilotu
          +` (17) znamená, že agent subjekt vyhodnotil jako investora jin
          +ého typu (PE, family office…) nebo se sídlem mimo ČR. Ručně to
          + bylo potvrzené jen u N1 a i&i Biotech. `neni_investor` (Espir
          +a, McWin) znamená jen to, že investice za posledních 24 měsíců
          + není veřejně doložená. Kontrolní agent upozornil, že to samo 
          +nedokazuje, že nejde o investora ([cilene_otazky.md](ai-log/04
          +-kontrola-zdroju/cilene_otazky.md), oddíl „Espira a McWin“).  
       21 +- Pět přesunů z opravené verze: N1 a i&i Biotech jsem přesunul
          + mimo pilot (správce fondu je v Lucembursku). Tensor (sídlo sp
          +rávce), i&i Prague (nástroj investice) a Presto (přiřazení inv
          +estic) jsem přesunul mezi nevyřešené. U i&i Prague a Presta ch
          +ybí důkaz, ale nic nedokládá, že nejde o investory.           
       22  
       17 -## Stav                                                       
       23 +Odkazy:                                                       
       24  
       19 -Cílová skupina pilotu jsou VC/CVC se sídlem v ČR. Jde o můj zv
          -olený rozsah, zadání VC fondy v jedné zemi uvádí jen jako přík
          -lad menšího vzorku. Pravidla pilotu jsou v [PLAN.md](PLAN.md),
          - bod 3.                                                       
       25 +| co | kde |                                                  
       26 +|---|---|                                                     
       27 +| plán, pravidla, schéma | [PLAN.md](PLAN.md) |               
       28 +| kandidáti | [data/kandidati.csv](data/kandidati.csv) |      
       29 +| původní výstup agenta (beze změn, na něm se měřilo) | [data/
          +vystup_agenta/](data/vystup_agenta/) |                        
       30 +| opravená verze a přehled změn | [data/opraveno/](data/oprave
          +no/), [ZMENY.md](data/opraveno/ZMENY.md) |                    
       31 +| stav kontroly každého id | [data/opraveno/stav_kontroly.csv]
          +(data/opraveno/stav_kontroly.csv) |                           
       32 +| ruční hodnocení | [data/hodnoceni.csv](data/hodnoceni.csv) |
       33 +| vzorek kontroly | [data/vzorek_kontroly.csv](data/vzorek_kon
          +troly.csv) |                                                  
       34 +| měření | [data/mereni_vzorku.md](data/mereni_vzorku.md) |   
       35 +| náklady | [NAKLADY.md](NAKLADY.md) |                        
       36 +| exporty konverzací a podklady | [ai-log/](ai-log/) |        
       37  
       21 -Hotový je krok 1 z bodu 9 plánu: seznam kandidátů pro pilot v 
          -`data/kandidati.csv`. Pro další zpracování jsem vybral všech 5
          -7 kandidátů, menší vzorek nevzniká. Jde o kandidáty, ne o ověř
          -ené investory.                                                
       38 +## Pravidla a zdroje                                          
       39  
       23 -Krok 2 proběhl ve dvou bězích:                                
       40 +Zkrácená verze, plné znění je v [PLAN.md](PLAN.md), body 2–4. 
       41  
       25 -- **Zkušební dávka** prvních 5 kandidátů podle abecedy podle p
          -ravidel platných před úpravami popsanými níže. Její původní vý
          -stup je archivovaný beze změn v [ai-log/02-zkusebni-davka/vyst
          -up_pravidla_v1/](ai-log/02-zkusebni-davka/vystup_pravidla_v1/)
          - (shodný s commitem f4cd74d). Naměřená doba dávky je 5 min 49 
          -s a zahrnuje jen zpracování agentem, bez kontroly, oprav a ruč
          -ního ověřování ([ai-log/02-zkusebni-davka/](ai-log/02-zkusebni
          --davka/)). Do měření nevstupuje.                              
       26 -- **Vyhodnocení po úpravě metodiky:** všech 57 kandidátů včetn
          -ě prvních pěti znovu podle aktuálních pravidel, v dávkách po 1
          -0 podle abecedy. Měří se jen tento běh, jeho výstup je v `data
          -/vystup_agenta/` a podklady v [ai-log/02-obohaceni/](ai-log/02
          --obohaceni/). **Nejde o nezávislý test na dosud neviděných dat
          -ech:** prvních pět kandidátů ovlivnilo návrh upravených pravid
          -el, takže výsledek u nich (a tím i celkový výsledek) může vych
          -ázet lépe, než by vyšel na nových datech.                     
       42 +- **Rozsah pilotu:** VC nebo CVC, jehož investiční firma (sprá
          +vce, značka) sídlí v ČR. Tento rozsah jsem zvolil já, zadání u
          +vádí VC fondy v jedné zemi jen jako příklad. Skutečného invest
          +ora jiného typu nebo se sídlem jinde vedu jako `mimo_rozsah_pi
          +lotu`, ne jako neinvestora.                                   
       43 +- **Sídlo správce:** při ruční kontrole jsem rozhodl, že rozho
          +duje sídlo správce (GP/AIFM), ne kancelář nebo tým. Původní te
          +xt pravidla tento případ neřešil (viz [Chyby a opravy](#chyby-
          +a-opravy)).                                                   
       44 +- **Doložená investice:** aspoň jedna zpráva o konkrétní trans
          +akci za posledních 24 měsíců k referenčnímu datu 26. 10. 2026.
          + Portfolio na webu ani zápis společníka v rejstříku samy nesta
          +čí. Datum investice a datum oznámení se zapisují zvlášť a filt
          +r pracuje s oznámením, když datum investice zdroj neuvádí.    
       45 +- **Nástroj:** podíl nebo konvertibilní nástroj. Účast v pre-s
          +eed, seed nebo series kole je přijatý pracovní předpoklad, ne 
          +doložený nástroj. Záznam opřený jen o něj má jistotu investice
          + nejvýš `stredni`. Jak často je předpoklad chybný, změřené nen
          +í.                                                            
       46 +- **Aktivita:** `aktivni` (investice do 12 měsíců) a `investic
          +e_dolozena_12_24_mesicu` je moje vlastní pracovní definice. Po
          +pisuje veřejnou stopu, ne skutečnou aktivitu.                 
       47 +- **Kapitál:** AUM, upsaný kapitál a velikost fondu se nezaměň
          +ují ani nesčítají. Ukládá se částka v původní měně, datum plat
          +nosti a druh ukazatele.                                       
       48 +- **Chybějící údaje:** zůstávají `null`, nic se neodhaduje. Úd
          +aj bez URL se nevyplňuje. Rozporné nebo nedostatečné důkazy o 
          +typu, nástroji, sídle nebo přiřazení investice vedou do `nevyr
          +esene.csv`.                                                   
       49  
       28 -  Výsledek agenta (před ruční kontrolou): zařazeno 27, mimo ro
          -zsah pilotu 15, není investor 2, hraniční 1, nevyřešené 11, sl
          -oučeno 1 (Nation1 → N1 Ventures). Kandidáty zpracovávali soubě
          -žně pomocní agenti stejného modelu podle [zadání](ai-log/02-ob
          -ohaceni/zadani_pomocneho_agenta.md), hlavní agent výsledky for
          -málně zkontroloval ([skript](ai-log/02-obohaceni/skripty/pride
          -j_davku.py)) a zapsal. Čas a počty požadavků po dávkách jsou v
          - [mereni.txt](ai-log/02-obohaceni/mereni.txt), nejasnosti prav
          -idel v [nejasnosti.md](ai-log/02-obohaceni/nejasnosti.md), roz
          -hodnutí o duplicitách v [duplicity.md](ai-log/02-obohaceni/dup
          -licity.md) a mapování všech 57 vstupních id na výsledek v [map
          -ovani_id.csv](ai-log/02-obohaceni/mapovani_id.csv).           
       50 +### Zdroje kandidátů                                          
       51  
       30 -Ruční hodnocení zatím neproběhlo.                             
       52 +Staženo 26. 10. 2026. Kandidát může být ve více zdrojích (ve d
          +vou a více je 20, v jednom 37).                               
       53  
       32 -### Pravidla upravená po zkušební dávce                       
       54 +| zdroj | kandidátů |                                         
       55 +|---|---|                                                     
       56 +| [CVCA, řádní členové](https://cvca.cz/en/category/full-membe
          +rs/) | 19 |                                                   
       57 +| [CEE Funding Map](https://www.pampam.city/funds-poland-BJpHb
          +ykKoXoBaILayYBs) | 38 |                                       
       58 +| [funding.tech.eu](https://funding.tech.eu/api-docs), kola če
          +ských firem 2025–2026 (60 kol) | 26 |                         
       59 +| [Dealroom, veřejný manifest](https://dealroom.co/investors/m
          +anifest.json) | 1 |                                           
       60  
       34 -Dávka ukázala nejasnosti v určení typu a v doložení nástroje i
          -nvestice. Pravidla v [PLAN.md](PLAN.md) jsem upravil takto:   
       61 +Omezení sběru: u 8 organizací z funding.tech.eu se sídlo nepod
          +ařilo doložit. Vedu je jako nevyřešené (`nevyreseno_sidlo` v [
          +opravy_sberu.csv](ai-log/01-kandidati/opravy_sberu.csv)), kand
          +idátů tak mohlo být až 65. Aplikace Dealroomu vracela HTTP 403
          +. Dataset funding.tech.eu pokrývá jen 60 kol. Ověření sídel a 
          +výňatky ze zdrojů jsou v [ai-log/01-kandidati/](ai-log/01-kand
          +idati/).                                                      
       62  
       36 -- **Typ:** určuje se podle vlastního popisu subjektu a doložen
          -ého fungování, ne podle toho, do čeho investuje. Family office
          - spravuje majetek jedné nebo několika rodin a VC může být jeho
          - investiční strategie. Samotné financování penězi rodiny pro t
          -yp family office nestačí. Přibyl typ korporátní investor bez s
          -amostatné jednotky (provozní firma investující z vlastní spole
          -čnosti), který není CVC a je mimo rozsah pilotu.              
       37 -- **Nevyřešená rozhodnutí:** když jsou důkazy o typu nebo nást
          -roji rozporné nebo nedostatečné, agent kandidáta nezařadí ani 
          -nevyřadí a zapíše ho do `data/vystup_agenta/nevyresene.csv` k 
          -ručnímu rozhodnutí.                                           
       38 -- **Nástroj (podmínka 3):** u každé investice se zapisuje, jes
          -tli je podíl nebo konvertibilní nástroj doložený (zdroj ho výs
          -lovně uvádí, nebo investor je zapsaný jako společník portfolio
          -vé firmy), jestli jde jen o nepřímou indicii, nebo jestli je n
          -ezjištěný. Podmínku splní doložený nástroj a také nepřímá indi
          -cie, když zdroj dokládá účast konkrétního investora v pre-seed
          -, seed nebo series kole a nejsou zjištěné informace, že jeho ú
          -čast byla výhradně nekonvertibilní dluh. U smíšených kol neroz
          -hoduje jen označení celého kola.                              
       63 +**Nástroje:** Claude Code (Claude Opus 5.5) s WebSearch a WebF
          +etch, veřejné API [ARES](https://ares.gov.cz/) pro identitu a 
          +IČO a veřejné bezklíčové API funding.tech.eu. Skripty jsou v P
          +ythonu jen se standardní knihovnou.                           
       64  
       40 -**Riziko tohoto rozhodnutí.** Účast v pre-seed, seed nebo seri
          -es kole je přijatý pracovní předpoklad, ne doložený nástroj. I
          -nvestor, který se kola účastnil úvěrem nebo jiným nekonvertibi
          -lním dluhem, o čemž zdroj nic neuvádí, tak může být chybně zař
          -azen. Proto má záznam opřený jen o tento předpoklad jistotu in
          -vestice nejvýš `stredni` a lze ho při ruční kontrole spočítat 
          -a zkontrolovat zvlášť. Jak často zdroje nástroj neuvádějí a ja
          -k často je předpoklad chybný, zatím změřené není.             
       65 +### Data funding.tech.eu: licence a atribuce                  
       66  
       42 -## Sběr kandidátů (krok 1)                                    
       67 +Podmínky jsem ověřil 26. 10. 2026 na [funding.tech.eu/for-ai](
          +https://funding.tech.eu/for-ai), [api-docs](https://funding.te
          +ch.eu/api-docs) a v [llms.txt](https://funding.tech.eu/llms.tx
          +t). Stránka /terms vracela HTTP 429, nečetl jsem ji.          
       68  
       44 -Staženo 26. 10. 2026. Výsledek: **57 unikátních kandidátů**.  
       69 +- **Zdroj:** „Tech.eu Funding Explorer“, https://funding.tech.
          +eu/api-docs. Použité API: `https://funding.tech.eu/api/v1` (`/
          +rounds` a `/investors/{name}`), bezklíčové, pouze pro čtení, l
          +imit 120 požadavků za 60 s, 600 za hodinu a 2 000 denně na IP.
          + Ve sběru šlo zhruba o 120 požadavků.                         
       70 +- **Licence dat:** [CC BY 4.0](https://creativecommons.org/lic
          +enses/by/4.0/).                                               
       71 +- **Úpravy:** [fundingtecheu_kola_cz_2025_2026.json](ai-log/01
          +-kandidati/zdroje/fundingtecheu_kola_cz_2025_2026.json) je nez
          +měněná odpověď `/api/v1/rounds` (Czech Republic, 2025-01-01 až
          + 2026-12-31), jen spojená ze stránek. [fundingtecheu_investori
          +.json](ai-log/01-kandidati/zdroje/fundingtecheu_investori.json
          +) je zkrácený výtah z `/api/v1/investors/{name}`. Z jmen inves
          +torů jsem odvodil seznam kandidátů. Částky ani data jsem neměn
          +il a do `kandidati.csv` jsem je nepřebíral. U kandidátů z toho
          +to zdroje je v `zdroj_url` URL záznamu v API.                 
       72 +- **Použití API:** původní pokyn pro sběr zakazoval po nedostu
          +pnosti webu použít náhradní nástroj. Použití API ho tedy nedod
          +rželo. Schválil jsem ho dodatečně, až po dokončení sběru.     
       73  
       46 -### Zdroje                                                    
       74 +## Měření                                                     
       75  
       48 -| Zdroj | Co jsem převzal | Kandidátů | Mimo rozsah |         
       76 +Podrobně v [data/mereni_vzorku.md](data/mereni_vzorku.md) (gen
          +eruje [scripts/mereni.py](scripts/mereni.py)).                
       77 +                                                              
       78 +**Vzorek.** Ručně (s asistencí AI, viz [Ruční kontrola – kdo h
          +odnotil](#ruční-kontrola--kdo-hodnotil)) jsem hodnotil náhodný
          + výběr 20 z 27 původně zařazených, deset polí na firmu. Výběr 
          +dělá `random.Random(20261027).sample(sorted(ids), 20)` ve [scr
          +ipts/vyber_vzorku.py](scripts/vyber_vzorku.py), výsledek je v 
          +[data/vzorek_kontroly.csv](data/vzorek_kontroly.csv). Skript i
          + seznam vznikly mimo Claude Code. Do repa přišly až v commitu 
          +35583d9, spolu s rozpracovaným hodnocením. Agent v něm opravil
          + jen cestu k souboru a načítání a ověřil, že ze seedu vychází 
          +tentýž seznam ([05-rucni-kontrola-ulozeni.txt](ai-log/05-rucni
          +-kontrola-ulozeni.txt), úsek „its output matches data/vzorek_k
          +ontroly.csv byte for byte“). Výběr je tedy reprodukovatelný ze
          + seedu. Kdy losování proběhlo vzhledem k začátku hodnocení, al
          +e log nedokládá.                                              
       79 +                                                              
       80 +**Správnost zařazení** (jednotka = firma, 95% Wilsonův interva
          +l):                                                           
       81 +                                                              
       82 +| | výsledek |                                                
       83 +|---|---|                                                     
       84 +| správně / chybně / neověřeno | 15 / 2 / 3 |                 
       85 +| přesnost na ověřitelných | 15/17 = **88,2 %** (65,7–96,7 %) 
          +|                                                             
       86 +| konzervativně, neověřené jako chyba | 15/20 = **75,0 %** (53
          +,1–88,8 %) |                                                  
       87 +                                                              
       88 +Obě chybná zařazení (N1, i&i Biotech) jsou **změny výkladu met
          +odiky**, ne chyby agenta. Agent použil sídlo značky a týmu, já
          + jsem při ruční kontrole rozhodl podle sídla správce. Bez nich
          + je dolní mez 15/18 = 83,3 % (60,8–94,2 %). Neověřené jsou Ten
          +sor (sídlo správce), i&i Prague (nástroj) a Presto (přiřazení 
          +investic).                                                    
       89 +                                                              
       90 +**Správnost vyplněných polí** (jednotka = pole firmy, 20 firem
          + × 10 polí):                                                  
       91 +                                                              
       92 +| pole | přesnost ano/(ano+ne) | dolní mez s `nelze_overit` | 
       93 +|---|---|---|                                                 
       94 +| **celkem** | 156/163 = **95,7 %** (91,4–97,9 %) | 156/175 = 
          +89,1 % (83,7–92,9 %) |                                        
       95 +| posledni_investice (nejslabší) | 15/19 = 78,9 % (56,7–91,5 %
          +) | 15/20 = 75,0 % (53,1–88,8 %) |                            
       96 +| rozsah_pilotu | 17/19 = 89,5 % (68,6–97,1 %) | 17/20 = 85,0 
          +% (64,0–94,8 %) |                                             
       97 +| nezavislost_zdroju | 14/14 = 100 % (78,5–100 %) | 14/20 = 70
          +,0 % (48,1–85,5 %) |                                          
       98 +| ostatní pole | bez `ne` | viz mereni_vzorku.md |            
       99 +                                                              
      100 +- `ne` je 7: 4 chyby výstupu (vždy přehlédnutá novější posledn
          +í investice: Look AI, Purple, Reflex, ZAKA), 2 změny výkladu m
          +etodiky (rozsah N1 a i&i Biotech) a 1 omezení schématu (dva in
          +tervaly ticketu i&i Biotech). Dalších 12 polí nešlo ověřit (`n
          +elze_overit`), nejvíc u nezávislosti zdrojů (6). Když se počít
          +ají jen chyby výstupu, vychází 156/160 = 97,5 % (93,7–99,0 %).
      101 +- Úplnost: sektory vyplněné u 16/20 firem, ticket 11/20 (1 pot
          +vrzené chybění, N1), kapitál 8/20.                            
      102 +- Souhrnný interval přes pole je optimistický, protože pole je
          +dné firmy nejsou nezávislá.                                   
      103 +- **Sloučení Nation1 → N1** jsem hodnotil zvlášť (1 případ, sp
          +rávně) a do přesnosti polí nevstupuje.                        
      104 +                                                              
      105 +**Co měření neříká.**                                         
      106 +                                                              
      107 +- Neříká, že databáze je ze 100 % správná.                    
      108 +- Recall ani úplnost českého trhu změřené nejsou. Vyřazené, hr
          +aniční a nevyřešené kandidáty nikdo ručně nekontroloval a orie
          +ntační srovnání se seznamy neproběhlo.                        
      109 +- Měření platí pro původní výstup agenta. Opravená verze vychá
          +zí ze stejného hodnocení a nové nezávislé hodnocení nemá.     
      110 +- Hodnocení vzniklo s asistencí AI a zčásti po přečtení nálezů
          + kontrolního agenta. Není to nezávislý referenční standard.   
      111 +                                                              
      112 +## Náklady                                                    
      113 +                                                              
      114 +Podrobně v [NAKLADY.md](NAKLADY.md).                          
      115 +                                                              
      116 +- **Pilot (kroky 0–6), změřeno z logů Claude Code:** 193,3 mil
          +. tokenů v 1 879 požadavcích, 96 % tvoří čtení z cache. **V př
          +epočtu na ceny API zhruba 108 USD.** Pilot jsem ale nezaplatil
          + přes API, běžel v rámci předplatného Claude, takže jde o přep
          +očet, ne o zaplacenou částku. Na kandidáta to dělá 1,67 USD, n
          +a zařazený záznam 3,46 USD.                                   
      117 +- **Nezachycená spotřeba** v součtu chybí a není nulová: token
          +y pomocného modelu WebFetch, výsledky WebSearch, asistence Cla
          +ude a ChatGPT v chatu, webové požadavky ve sběru a kroky 7–9. 
      118 +- **Svět je scénář, ne změřený počet investorů:** 5 600–11 000
          + zařazených podle [PLAN.md](PLAN.md), bod 8.2. Poměr kandidátů
          + k zařazeným (56/27), čas člověka 10–15 min na firmu, sazba 25
          + USD/h, násobky pro jazyky a rejstříky a podíl nevyřešených js
          +ou modelové předpoklady.                                      
      119 +                                                              
      120 +| svět, USD | nízká | střední | vysoká |                      
      121  |---|---|---|---|
       50 -| [CVCA, řádní členové](https://cvca.cz/en/category/full-membe
          -rs/) | 27 řádných členů (PE/VC investoři podle CVCA); přidruže
          -ní členové jsou podle CVCA poradci a banky, nepřebíral jsem je
          - | 19 | 8 (sídlo mimo ČR) |                                   
       51 -| [CEE Funding Map](https://www.pampam.city/funds-poland-BJpHb
          -ykKoXoBaILayYBs) (Warsaw Equity Group, CzechInvest, Czech Foun
          -ders) | 95 položek mapy ČR a Polska s adresou | 38 | 55 (sídlo
          - v Polsku, u Tachles VC v USA) |                              
       52 -| [funding.tech.eu](https://funding.tech.eu/api-docs), kola če
          -ských firem 2025–2026 | 60 kol, 113 jmen investorů | 26 | 84 (
          -z toho 8 s nevyřešeným sídlem, viz Omezení) |                 
       53 -| [Dealroom, veřejná část](https://dealroom.co/investors/manif
          -est.json) | manifest 609 investorů, jen Credo Ventures má zemi
          - Czechia | 1 | – |                                            
      122 +| sestavení s kontrolním vzorkem (AI + člověk) | 33 696 | 73 9
          +01 | 151 418 |                                                
      123 +| sestavení s plnou ruční kontrolou | 55 029 | 125 450 | 253 6
          +28 |                                                          
      124 +| roční aktualizace poslední investice | 5 415 | 18 370 | 54 5
          +70 |                                                          
      125  
       55 -Kandidát může být ve více zdrojích, proto součet sloupce nedáv
          -á 57. Ve dvou a více zdrojích je 20 kandidátů, jen v jednom 37
          - (CVCA 9, mapa 19, funding.tech.eu 9).                        
      126 +Většinu lidských hodin tvoří ruční rozhodnutí nevyřešených kan
          +didátů. Je to zároveň nejméně podložená položka, protože v pil
          +otu je nikdo ručně nerozhodoval.                              
      127  
       57 -### Postup                                                    
      128 +## Jak jsem pracoval s AI                                     
      129  
       59 -1. **Rozsah = sídlo v ČR podle zdroje.** U CVCA a mapy rozhodu
          -je adresa, kterou uvádí sám zdroj. funding.tech.eu sídlo inves
          -tora neeviduje (`countries` jsou země portfolia), proto jsem j
          -ména rozdělil takto:                                          
       60 -   - jména shodná s kandidátem z CVCA nebo z mapy jsem přiřadi
          -l k němu,                                                     
       61 -   - fyzické osoby (typ `Angel` ve zdroji) a popisy typu „exis
          -ting shareholders“ jsou mimo rozsah pilotu,                   
       62 -   - u zbylých 65 organizací (a u Tachles VC, který na mapě ne
          -má adresu) jsem sídlo dohledal ve veřejném zdroji s URL a cita
          -cí (vlastní web, rejstřík, tisková zpráva). Všech 9 českých sí
          -del jsem ověřil v obchodním rejstříku (or.justice.cz).        
       63 -2. **Bez posuzování.** Typ (VC, CVC, PE, family office…) ani a
          -ktivitu jsem neposuzoval. Mezi kandidáty jsou proto i subjekty
          -, které zdroj označuje jako PE nebo family office, provozní fi
          -rmy (Braiins, Botanique Hospitality), fond J&T Investiční spol
          -ečnosti (Fond Naše Česko) a klub andělů (Garage Angels). O jej
          -ich zařazení se rozhodne v kroku 3.                           
       64 -3. **Deduplikace.** Ručně podle shodného názvu nebo jeho varia
          -nty (aliasy z funding.tech.eu) a domény webu, explicitně v tab
          -ulce ve [scripts/sestav_kandidaty.py](scripts/sestav_kandidaty
          -.py). Shoda adresy sama o sobě nestačí.                       
       65 -4. **Dohledatelnost.** `zdroj_seznamu` a `zdroj_url` jsou u ka
          -ndidáta z více zdrojů seznamy oddělené ` | ` ve stejném pořadí
          -, jeden pár na každý výskyt. U funding.tech.eu je `zdroj_url` 
          -záznam investora v API, ze kterého jsem jméno převzal.        
       66 -5. **`id`** má tvar `cz-nazev-bez-diakritiky`, je stabilní a v
          - dalších krocích se nemění.                                   
       67 -6. **`web`** je převzatý ze zdroje (CVCA, mapa). U kandidátů j
          -en z funding.tech.eu pochází z ověření sídla. Kde jsem web ned
          -oložil, je prázdný.                                           
      130 +První návrh plánu vznikl v chatu. Implementaci, sběr a zpracov
          +ání jsem dělal v Claude Code. Každý krok měl vlastní session, 
          +exporty jsou v [ai-log/](ai-log/). Krok 5 je jedna session exp
          +ortovaná dvakrát: [05-priprava.txt](ai-log/05-priprava.txt) ob
          +sahuje přípravu, [05-rucni-kontrola-ulozeni.txt](ai-log/05-ruc
          +ni-kontrola-ulozeni.txt) celou session včetně uložení hodnocen
          +í. Pomocní agenti (3 ve sběru, 31 v obohacení, 13 v kontrole z
          +drojů) jsou v exportech zachycení jen svými závěrečnými zpráva
          +mi hlavnímu agentovi. ChatGPT a Claude v chatu mi pomáhali s r
          +ecenzí plánu, vyhledáním a překladem zdrojů a s návrhy verdikt
          +ů ruční kontroly.                                             
      131  
       69 -Podklady jsou v [ai-log/01-kandidati/](ai-log/01-kandidati/): 
          -extrakty zdrojů (`zdroje/`), ověření sídel s URL a citacemi (`
          -sidla_overeni.json`), všechny vynechané výskyty s důvodem, jak
          - je sběr původně zapsal (`mimo_rozsah.csv`, beze změn), dodate
          -čné opravy sběru (`opravy_sberu.csv`) a sběrné skripty (`skrip
          -ty/`). Výsledné CSV vytváří `python3 scripts/sestav_kandidaty.
          -py`.                                                          
      132 +Agent podle zadání po každém kroku zastavil a vypsal výsledek.
          + Commit dělal až po mém schválení.                            
      133  
       71 -### Omezení                                                   
      134 +| krok, export | co jsem agentovi zadal | jak jsem výstup kont
          +roloval |                                                     
      135 +|---|---|---|                                                 
      136 +| 0 [plán a založení](ai-log/00-plan-a-zalozeni.txt) | opravit
          + PLAN.md podle externí recenze v ChatGPT a mé kontroly (kapitá
          +l, aktivita, důkazy, měření, odhad rozsahu, druhý agent), zalo
          +žit repo a ověřit git identitu | dvě kola diffu PLAN.md před s
          +chválením |                                                   
      137 +| 1 [kandidáti](ai-log/01-kandidati.txt) | jen veřejné zdroje,
          + nedostupnost zaznamenat a neobcházet, stabilní id, deduplikac
          +e bez zařazování, počet nepřizpůsobovat hypotéze | souhrn zdro
          +jů a duplicit, dodatečné schválení API, ověření licence, 8 nev
          +yřešených sídel, pravidla pilotu |                            
      138 +| 2 [zkušební dávka](ai-log/02-zkusebni-davka.txt) | 5 kandidá
          +tů podle schématu, pak úprava pravidel typu a nástroje | diff 
          +pravidel a dopad na 5 kandidátů, výstup dávky archivovaný beze
          + změn |                                                       
      139 +| 2 [obohacení](ai-log/02-obohaceni.txt) | všech 57 v dávkách 
          +po 10, pravidla neměnit, nejasnosti zapisovat, surové odpovědi
          + ARES a funding.tech.eu ukládat, měřit čas a požadavky | souhr
          +n a commit po každé dávce, formální kontrola skriptem, [nejasn
          +osti.md](ai-log/02-obohaceni/nejasnosti.md) |                 
      140 +| 3 [automatická kontrola](ai-log/03-kontrola.txt) | validátor
          + struktury, pokrytí id, okna, nástroje a jistoty, upozornění n
          +a zdroje stažené bez ověření TLS, testy | testy na umělých chy
          +bách, zpráva [automaticka_kontrola.md](ai-log/03-kontrola/auto
          +maticka_kontrola.md) |                                        
      141 +| 4 [kontrola zdrojů](ai-log/04-kontrola-zdroju.txt) | druhý a
          +gent (stejný model, nová konverzace): fáze A naslepo bez READM
          +E a historie, fáze B cílené otázky | závěry po polích v [slepa
          +_kontrola.csv](ai-log/04-kontrola-zdroju/slepa_kontrola.csv), 
          +oprava vlastních chyb fáze A v [cilene_otazky.md](ai-log/04-ko
          +ntrola-zdroju/cilene_otazky.md) |                             
      142 +| 5 [ruční kontrola](ai-log/05-rucni-kontrola-ulozeni.txt) | p
          +řipravit průvodce a předvyplněné hodnocení bez verdiktů, nález
          +y AI oddělit, pak uložit hodnocení z mé kontroly | počty verdi
          +ktů a změn proti mým očekávaným hodnotám, při rozdílu bez comm
          +itu |                                                         
      143 +| 6 [měření](ai-log/06-mereni.txt) | PLAN.md sladit se skutečn
          +ým postupem, deterministický mereni.py, oddělit tři druhy `ne`
          + | moje nezávislé kontrolní počty, rozdíl 157/156 dohledán pře
          +d commitem |                                                  
      144 +| 7 [náklady](ai-log/07-naklady.txt) | spotřeba jen z polí usa
          +ge v lokálních logech, ceník z oficiálního zdroje, předpoklady
          + výslovně označit | souhrn před commitem, druhé kolo úprav (sa
          +zba, rozsah aktualizace, význam vzorku) |                     
      145 +| 8 [opravená verze](ai-log/08-opraveno.txt) | oprav.py jen po
          +dle dokončeného hodnocení, přesuny a opravy s odkazem na řádek
          + hodnocení | návrh přesunů před provedením, zamítnuté nové pol
          +e v investori.json, validace v dočasné kopii |                
      146  
       73 -- **funding.tech.eu:** webové rozhraní vracelo HTTP 429 s bezp
          -ečnostní kontrolou Vercelu. Agent ji neprolomil, data ale vzal
          - z oficiálního bezklíčového API téhož zdroje (`/api/v1`, robot
          -s.txt ho povoluje). Původní pokyn zakazoval po nedostupnosti z
          -droje použít náhradní nástroj, takže použití API ho nedodrželo
          -. Schválil jsem ho dodatečně, až po dokončení sběru. Dataset o
          -bsahuje jen 60 kol českých firem za 2025–2026, pokrytí je tedy
          - neúplné.                                                     
       74 -- **Dealroom:** aplikace (app.dealroom.co, czechia.dealroom.co
          -) vrací HTTP 403, neobcházel jsem ji. Veřejná část (stránky ze
          -mí a měst, market mapy) investory v ČR nevypisuje. Manifest ob
          -sahuje jen top investory světa.                               
       75 -- **CEE Funding Map:** typ fondu (VC, PE, family office…) je n
          -a mapě jen v poškozených fragmentech importu, proto jsem ho ne
          -přebíral. ARX Equity má na mapě polskou adresu, v CVCA pražsko
          -u, a je veden jako kandidát.                                  
       76 -- **Nevyřešená sídla:** u 8 organizací z funding.tech.eu (Crea
          -ndum, Decibel, Lumiere AI Ventures, Northzone, Puzzle Ventures
          -, Riverside Acceleration Capital, SCI Ventures, University2Ven
          -tures) se sídlo nepodařilo doložit. Nejsou prokazatelně zahran
          -iční ani prokazatelně české, vedu je jako nevyřešené (`nevyres
          -eno_sidlo`) v `opravy_sberu.csv`. Původní `mimo_rozsah.csv` je
          - uvádí mezi vynechanými výskyty a zůstává beze změny. Počet ka
          -ndidátů, místní rozsah pilotu i recall se proto vztahují jen k
          - 57 kandidátům. Kdyby některá z 8 organizací sídlila v ČR, kan
          -didátů by bylo až 65.                                         
       77 -- **Sídla:** U Tachles VC vlastní web uvádí jen adresu v USA. 
          -U Botanique Hospitality je zdrojem sídla kromě rejstříku jen a
          -gregátor CB Insights. U QQ Capital rejstřík uvádí jediný subje
          -kt toho jména, jeho totožnost s investorem v kole Navigara jse
          -m ale nepotvrdil.                                             
       78 -- **Možné duplicity, které jsem nesloučil** (doložená je jen s
          -hodná adresa nebo vazba): Nation1 (nation1.vc, doména se nepře
          -kládá) a N1 Ventures (n1.rocks) na adrese Národní 135/14; i&i 
          -Biotech Investments a i&i Prague (i&i Prague podle svého webu 
          -založil i&i Biotech Fund); Tilia Impact Ventures a PurposeTech
          - na adrese Drtinova 557/10; Fond Naše Česko a J&T Ventures na 
          -adrese Sokolovská 700/113a. Zatím zůstávají samostatně, v krok
          -u 2 o nich rozhodne pravidlo „jedna investiční firma = jeden z
          -áznam“.                                                       
       79 -- **Ověření sídel** dělali pomocní agenti stejného modelu z ve
          -řejných webů. Česká sídla jsem znovu ověřil v rejstříku, zahra
          -niční jen u agentů. Několik zahraničních sídel opírají jen agr
          -egátory (CB Insights, Caplight), viz `sidla_overeni.json`.    
      147 +### Ruční kontrola – kdo hodnotil                             
      148  
       81 -### Licence a atribuce dat funding.tech.eu                    
      149 +„Petr Šťastný (asistence AI)“: zdroje vyhledal, přeložil a ver
          +dikt navrhl Claude, u části polí ChatGPT. Každý verdikt jsem s
          +chválil já a sporné výkladové otázky (sídlo správce, přiřazení
          + přes fondy, chybějící údaje) jsem rozhodl sám. Štítek znamená
          + schválení navržených verdiktů, ne to, že jsem osobně otevřel 
          +všechny zdroje. U všech polí jsem je neotevíral.              
      150  
       83 -Podmínky jsem ověřil 26. 10. 2026 na [funding.tech.eu/for-ai](
          -https://funding.tech.eu/for-ai), [api-docs](https://funding.te
          -ch.eu/api-docs) a v [llms.txt](https://funding.tech.eu/llms.tx
          -t). Stránka /terms vracela HTTP 429, nečetl jsem ji.          
      151 +Stav před přečtením nálezů kontrolního agenta je uložen zvlášť
          + v [hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hod
          +noceni_pred_nalezy_ai.csv) (commit 35583d9). V něm je ještě ro
          +zlišeno, kdo verdikt navrhl: 194 řádků Claude, 7 ChatGPT. Změn
          +y po přečtení nálezů mají v poznámce „Změna po přečtení nálezů
          + AI“.                                                         
      152  
       85 -- **Licence:** data jsou pod [CC BY 4.0](https://creativecommo
          -ns.org/licenses/by/4.0/). API je bezklíčové a pouze pro čtení,
          - s limitem 120 požadavků za 60 s, 600 za hodinu a 2 000 denně 
          -na IP adresu. Sběr udělal zhruba 120 požadavků s pauzou mezi n
          -imi.                                                          
       86 -- **Atribuce:** zdroj: „Tech.eu Funding Explorer“, https://fun
          -ding.tech.eu/api-docs. U každého kandidáta z tohoto zdroje je 
          -v `zdroj_url` URL záznamu v API, ze kterého údaj pochází (např
          -. https://funding.tech.eu/api/v1/investors/Credo%20Ventures). 
       87 -- **Úpravy dat:**                                             
       88 -  - `ai-log/01-kandidati/zdroje/fundingtecheu_kola_cz_2025_202
          -6.json` je nezměněná odpověď `/api/v1/rounds` (filtr country =
          - Czech Republic, 2025-01-01 až 2026-12-31), jen spojená ze str
          -ánek.                                                         
       89 -  - `fundingtecheu_investori.json` je zkrácený výtah z `/api/v
          -1/investors/{name}` (jen `name`, `types`, `aliases`, `deals` a
          - HTTP status).                                                
       90 -  - Z jmen investorů jsem odvodil seznam kandidátů: varianty j
          -men jsem sloučil s kandidáty z jiných zdrojů a rozdělil je pod
          -le sídla.                                                     
       91 -  - Částky, data ani jiné hodnoty jsem neměnil a do `data/kand
          -idati.csv` jsem je nepřebíral.                                
      153 +Kontrola proto není nezávislý referenční standard. Druhý agent
          + byl stejný model v jiné konverzaci a hodnocení jsem dělal v p
          +ořadí podle jeho nálezů. Srovnání jeho přínosu je jen orientač
          +ní: ze 4 chyb výstupu našla ruční kontrola 3 (Purple, Reflex, 
          +ZAKA) až po přečtení jeho nálezů. Po přečtení se také 6 verdik
          +tů změnilo z `ano` na `nelze_overit` ([mereni_vzorku.md](data/
          +mereni_vzorku.md), oddíl 5.4).                                
      154  
       93 -## Ruční kontrola – kdo hodnotil                              
      155 +## Chyby a opravy                                             
      156  
       95 -„Petr Šťastný (asistence AI)“: zdroje vyhledal, přeložil a ver
          -dikt navrhl Claude, u části polí ChatGPT. Každý verdikt jsem s
          -chválil já a sporné výkladové otázky (sídlo správce, přiřazení
          - přes fondy, chybějící údaje) jsem rozhodl sám. Zdroje jsem sá
          -m neotevíral u všech polí. Stav před přečtením nálezů druhého 
          -agenta je uložen v ai-log/05-rucni-kontrola/hodnoceni_pred_nal
          -ezy_ai.csv (commit 35583d9); změny po jejich přečtení mají v p
          -oznámce „Změna po přečtení nálezů AI“.                        
      157 +Uvádím jen chyby doložené v repu a logu. Úsek v uvozovkách jde
          + v uvedeném souboru vyhledat doslova. Druh chyby:             
      158  
       97 -## Struktura                                                  
      159 +- **pravidla:** chyba nebo mezera v mých pravidlech,          
      160 +- **aplikace:** chybné použití existujícího pravidla,         
      161 +- **schéma:** schéma neumí hodnotu zapsat,                    
      162 +- **neurčeno:** příčinu z logu nejde zjistit.                 
      163  
       99 -| Cesta | Obsah |                                             
      164 +### Návrh a pravidla                                          
      165 +                                                              
      166 +| chyba | druh | kdo našel | řešení | doklad |                
      167 +|---|---|---|---|---|                                         
      168 +| Plán z chatu definoval kapitál jako součet upsaného kapitálu
          + nebo AUM, takže zaměňoval a sčítal různé ukazatele. | pravidl
          +a | externí recenze v ChatGPT | v kroku 0 nahrazeno seznamem `
          +kapital` s druhem ukazatele a datem, bez sčítání | [00-plan-a-
          +zalozeni.txt](ai-log/00-plan-a-zalozeni.txt): „Celkový investi
          +ční kapitál** = součet upsaného kapitálu“ |                   
      169 +| Hranici aktivity 12 měsíců plán připisoval CEE Funding Map, 
          +ta ale měří dvě investice za rok. | pravidla | recenze v ChatG
          +PT | v kroku 0 označeno jako moje vlastní pracovní definice, s
          +tatus přejmenován | tamtéž: „Hranici 12 měsíců přebírám od CEE
          +“ |                                                           
      170 +| Odhad pro ČR byl odvozený z počtu investičních kol, částky s
          +e převáděly na EUR. | pravidla | recenze v ChatGPT | v kroku 0
          + hypotéza bez odvození, původní měna | tamtéž: „Odhad vychází 
          +z počtu kol“ |                                                
      171 +| Pravidlo „investiční firma (správce, značka) sídlí v ČR“ neu
          +rčuje, co platí, když správce sídlí v cizině a tým v Praze. | 
          +pravidla | kontrolní agent (fáze B), rozhodnuto při ruční kont
          +role | rozhodnuto podle sídla správce: N1 a i&i Biotech mimo p
          +ilot, Tensor nevyřešený. Text pravidla v PLAN.md upřesněný nen
          +í a KAYA neposouzená, **nenapraveno, uvedeno jako omezení** | 
          +[cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md)
          +: „PLAN.md neříká, co platí, když správce (GP/AIFM) sídlí jind
          +e než značka a tým“ |                                         
      172 +                                                              
      173 +### Sběr a obohacení (agent)                                  
      174 +                                                              
      175 +| chyba | druh | kdo našel | řešení | doklad |                
      176 +|---|---|---|---|---|                                         
      177 +| Agent ve sběru použil API funding.tech.eu, i když pokyn zaka
          +zoval po nedostupnosti webu náhradní nástroj (provedená akce).
          + | aplikace | agent to sám uvedl v souhrnu, rozhodl jsem já | 
          +dodatečně schváleno a zapsáno výše | [01-kandidati.txt](ai-log
          +/01-kandidati.txt): „neobcházej ho přes cache, mirror ani jiný
          + nástroj“, „API funding.tech.eu dodatečně schvaluji“ |        
      178 +| Look AI, Purple, Reflex: agent přehlédl novější doloženou in
          +vestici. | neurčeno | Look AI ruční kontrola před nálezy AI, P
          +urple a Reflex kontrolní agent (fáze A) | v opravené verzi nov
          +á poslední investice, původní přesunutá do `dalsi_investice` |
          + [hodnoceni.csv](data/hodnoceni.csv) ř. 127, 147, 157; [04-kon
          +trola-zdroju.txt](ai-log/04-kontrola-zdroju.txt): „Embodied“, 
          +„ArtMaster“ |                                                 
      179 +| ZAKA: agent FinalDose znal, ale vlastní oznámení investora n
          +epřijal jako zprávu o transakci, přestože ho PLAN.md připouští
          +. | aplikace | kontrolní agent (fáze A) | v opravené verzi Fin
          +alDose, stránka v kroku 8 znovu načtena nebyla (viz Omezení) |
          + poznámka záznamu v [vystup_agenta/investori.json](data/vystup
          +_agenta/investori.json): „ty jsem nezávislou zprávou o transak
          +ci neověřil“; hodnoceni.csv ř. 48 |                           
      180 +| i&i Prague: agent označil nástroj jako `dolozeno` podle rejs
          +tříku CasInvent. Podle hodnocení zápis uvádí i&i Prague jako a
          +kcionáře jen v roce 2020 (historický zápis) a nástroj u kola 2
          +025 nedokládá. Kandidát měl jít do nevyřešených. | aplikace | 
          +ruční kontrola (kontrolní agent pole označil jako sedící) | př
          +esun do `nevyresene.csv` (otázka `nastroj`) | [02-obohaceni.tx
          +t](ai-log/02-obohaceni.txt): „Podíl dokládá výpis z rejstříku 
          +CasInvent“; hodnoceni.csv ř. 65 |                             
      181 +| Presto: agent připsal Prestu investice fondu Tech Horizons (
          +lucemburský správce). Vazba není doložená, ale ani vyvrácená. 
          +| neurčeno | ruční kontrola (kontrolní agent pole označil jako
          + sedící) | přesun do `nevyresene.csv` (otázka `investice`) | 0
          +2-obohaceni.txt: „investice SatVu a Occam přičítám Presto Vent
          +ures“; hodnoceni.csv ř. 293 |                                 
      182 +| N1: chybí ticket, který web uvádí („Typical 1st investment $
          +100K–$1M“). | neurčeno | ruční kontrola | zapsáno v ZMENY.md, 
          +záznam je mimo pilot | hodnoceni.csv ř. 10 |                  
      183 +| i&i Biotech: dva intervaly ticketu sloučené do jednoho 150 t
          +is.–2 mil. EUR. | schéma | ruční kontrola (návrh verdiktu Chat
          +GPT) | v ZMENY.md oba intervaly, společný interval se nepoužij
          +e | 02-obohaceni.txt: „Ticket podle webu je 150 tis. až 2 mil.
          + EUR.“; hodnoceni.csv ř. 41 |                                 
      184 +                                                              
      185 +### Postup a bezpečnost                                       
      186 +                                                              
      187 +| chyba | provedeno / zamítnuto | kdo našel | řešení | doklad 
          +|                                                             
      188 +|---|---|---|---|---|                                         
      189 +| Stažení profilu CVCA (Thein) přes `curl -k`, tedy bez ověřen
          +í TLS. | provedeno u Theinu, u Tensoru pokus zablokovalo opráv
          +nění | agent sám v souhrnu dávky | automatická kontrola to hlá
          +sí jako upozornění. Zdroj se znovu neověřoval a Thein ručně ko
          +ntrolovaný není, **nenapraveno, uvedeno jako omezení** | 02-ob
          +ohaceni.txt: „stáhl přes curl -k kvůli chybě certifikátu“, „Cu
          +rl bez ověření certifikátu zablokovala oprávnění“ |           
      190 +| Přepsané surové odpovědi ARES: agent dávky 3 znovu stáhl `ar
          +es_hledani_iiPrague.json` a `ares_vr_06058485.json` z dávky 2.
          + | provedeno | hlavní agent | git eviduje oba soubory jen v co
          +mmitu 19ed337, přepsaný obsah byl tedy shodný. Přepsání varian
          +ty hledání v dávce 2 agent opravil sám přejmenováním. Jiný age
          +nt smazal prázdnou chybovou odpověď funding.tech.eu, ta obnove
          +ná není | 02-obohaceni.txt: „Přepsané surové soubory ARES“, „p
          +řepsala soubor“, „Odstraněný soubor:“ |                       
      191 +| Pokus obejít ochranu proti botům: curl s jiným User-Agent (k
          +rok 2, zdroje CasInvent) a opakované načtení zaka.vc po HTTP 4
          +66 (krok 8). | oba zamítnuté klasifikátorem, neproběhly | klas
          +ifikátor oprávnění Claude Code | agent pokračoval bez stránek,
          + FinalDose proto znovu načtené není | 02-obohaceni.txt: „zamít
          +l klasifikátor (obcházení ochrany proti botům)“; [08-opraveno.
          +txt](ai-log/08-opraveno.txt): „Bot Check Circumvention“ |     
      192 +                                                              
      193 +### Kontrola a měření                                         
      194 +                                                              
      195 +| chyba | druh | kdo našel | řešení | doklad |                
      196 +|---|---|---|---|---|                                         
      197 +| Kontrolní agent ve fázi A nezachytil lucemburský AIFM u KAYA
          +. Označil také 5 dvojic, které konečné hodnocení nepotvrdilo, 
          +a neoznačil Presto, nástroj i&i Prague ani ticket i&i Biotech.
          + | aplikace | sám ve fázi B; srovnání v mereni_vzorku.md | KAY
          +A zůstává zařazená a neposouzená, **nenapraveno, uvedeno jako 
          +omezení** | cilene_otazky.md: „U Kaya to první agent ani fáze 
          +A nezachytili“ |                                              
      198 +| Claude v chatu (asistence ruční kontroly) navrhl `ano` u pos
          +lední investice Purple, Reflex a ZAKA a přehlédl novější inves
          +tice. Schválil jsem to. | aplikace | kontrolní agent, převzato
          + po přečtení jeho nálezů | změna na `ne`, oprava v kroku 8 | [
          +hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hodnoce
          +ni_pred_nalezy_ai.csv); 05-rucni-kontrola-ulozeni.txt: „Očekáv
          +ám přesně 9 změn“ |                                           
      199 +| Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem,
          + kde agent vedl zdroje s neznámým původem. | aplikace | kontro
          +lní agent | změna na `nelze_overit`, `puvod` ani `jistota` se 
          +v opravené verzi nemění | tamtéž |                            
      200 +| Kontrolní počet 157 `ano` v mém zadání kroku 6 započítal i ř
          +ádek sloučení Nation1 → N1, správně je 156 pro pole 20 firem. 
          +Kdo počet připravil, log nedokládá. | neurčeno | agent kroku 6
          + | potvrdil jsem 156, sloučení se vykazuje zvlášť | [06-mereni
          +.txt](ai-log/06-mereni.txt): „Skript dává 156 ano místo kontro
          +lních 157“ |                                                  
      201 +| [mereni.txt kontroly zdrojů](ai-log/04-kontrola-zdroju/meren
          +i.txt) uvádí jako „tokeny subagentů“ velikost kontextu posledn
          +ího volání, ne spotřebu. | aplikace | agent kroku 7 | NAKLADY.
          +md počítá s kumulativní spotřebou z logů. mereni.txt zůstal be
          +ze změny, rozdíl je vysvětlený v NAKLADY.md | [07-naklady.txt]
          +(ai-log/07-naklady.txt): „nejsou spotřeba, ale“ |             
      202 +                                                              
      203 +U ChatGPT repo ani log chybu nedokládají. Jeho 7 navržených ve
          +rdiktů zůstalo po přečtení nálezů beze změny.                 
      204 +                                                              
      205 +## Omezení a nedokončené části                                
      206 +                                                              
      207 +- **Sedm zařazených mimo vzorek** (ČS Seed Starter, Fazole, JI
          +C Ventures, J&T Ventures, KAYA, Lighthouse, Tilia) ručně kontr
          +olovaných není.                                               
      208 +- **Vyřazení, hraniční a nevyřešení** z původního výstupu (29 
          +kandidátů) ručně kontrolovaní nejsou. Žádný nevyřešený případ 
          +jsem ručně nerozhodl, ani původní 11, ani 3 nové.             
      209 +- **Sídlo správce:** KAYA má podle kaya.vc/sustainability sprá
          +vce registrovaného jako lucemburský AIFM. Podle pravidla použi
          +tého u N1 by patřila mimo pilot, ale posouzená není a zůstává 
          +zařazená. Má i známý nález automatické kontroly: `fond` vyplně
          +ný u `committed_capital`. U Credo je neověřená role nové správ
          +covské a.s.                                                   
      210 +- **Nezávislost zdrojů** nešla ověřit u 6 z 20 firem (zdroje s
          + neznámým původem mohou vycházet z jedné tiskové zprávy).     
      211 +- **Poslední investice** je nejnovější doložená, ne záruka, že
          + novější neexistuje. Byla to nejslabší kategorie polí.        
      212 +- **ZAKA:** stránku zaka.vc/news se při tvorbě oprav nepodařil
          +o znovu načíst. Oprava na FinalDose vychází z dřívějšího hodno
          +cení s asistencí AI a z kontroly druhým agentem. PerfectBit (t
          +isková zpráva 18. 8. 2026) nikdo neposoudil a zapsaný není.   
      213 +- **Datum stažení:** zdroje čtené v kroku 8 mají `stazeno` 27.
          + 10. 2026, tedy den po referenčním datu. Pozdější datum stažen
          +í samo neznamená, že informace k 26. 10. 2026 neplatila. Autom
          +atická kontrola to při referenčním datu 26. 10. hlásí jako nes
          +oulad (podrobnosti v ZMENY.md).                               
      214 +- **Ostatní:** Thein stažený bez ověření TLS. Pracovní předpok
          +lad u nástroje (účast v seed kole) změřený není. Prvních 5 kan
          +didátů ovlivnilo úpravu pravidel, takže běh není test na nevid
          +ěných datech. Recall a úplnost trhu změřené nejsou. Globální p
          +očty i náklady jsou scénáře.                                  
      215 +                                                              
      216 +## Spuštění                                                   
      217 +                                                              
      218 +Python 3 jen se standardní knihovnou, spouští se z kořene repa
          +. Všechny skripty kromě `--over-url` běží bez sítě a jsou dete
          +rministické. Skripty v tabulce **přepisují svůj výstup v repu*
          +*. Při stejných vstupech vznikne stejný obsah, výjimky jsou uv
          +edené.                                                        
      219 +                                                              
      220 +| účel | příkaz | přepisuje |                                 
      221 +|---|---|---|                                                 
      222 +| seznam kandidátů | `python3 scripts/sestav_kandidaty.py` | `
          +data/kandidati.csv`, `ai-log/01-kandidati/mimo_rozsah.csv` |  
      223 +| výběr vzorku | `python3 scripts/vyber_vzorku.py` | `data/vzo
          +rek_kontroly.csv` |                                           
      224 +| kontrola dat bez sítě | `python3 scripts/zkontroluj_data.py 
          +--vystup /tmp/kontrola.md` | nic (s `--vystup` mimo repo) |   
      225 +| kontrola dat včetně URL | `python3 scripts/zkontroluj_data.p
          +y --over-url` | `ai-log/03-kontrola/automaticka_kontrola.md` |
      226 +| testy validátoru | `python3 -m unittest scripts/test_zkontro
          +luj_data.py` | nic |                                          
      227 +| měření | `python3 scripts/mereni.py` | `data/mereni_vzorku.m
          +d` |                                                          
      228 +| spotřeba z logů | `python3 scripts/spotreba_z_logu.py` | `ai
          +-log/07-naklady/spotreba.csv` |                               
      229 +| náklady | `python3 scripts/naklady.py` | `ai-log/07-naklady/
          +vypocet.md` |                                                 
      230 +| opravená verze | `python3 scripts/oprav.py` | soubory v `dat
          +a/opraveno/` |                                                
      231 +                                                              
      232 +- **zkontroluj_data.py:** uložená zpráva vznikla s `--over-url
          +` (354 URL). Běh bez tohoto přepínače bez `--vystup` ji přepíš
          +e verzí bez kontroly URL. Výsledek kontroly URL se mění s čase
          +m a stavem webů. Další parametry jsou `--datum` (referenční da
          +tum, výchozí 2026-10-26) a `--koren`. Skript čte jen `data/vys
          +tup_agenta/`. Postup kontroly opravené verze v dočasném kořeni
          + popisuje [ZMENY.md](data/opraveno/ZMENY.md). Návratový kód 1 
          +znamená chybu struktury.                                      
      233 +- **spotreba_z_logu.py** potřebuje původní lokální logy Claude
          + Code v `~/.claude/projects/`, jinde nepůjde zopakovat. Skript
          + skončí chybou, když v adresáři logů projektu je session, kter
          +ou jeho tabulka `SESSIONY` nezná. To dnes platí pro session kr
          +oku 8 a pozdější, `spotreba.csv` se pak nepřepíše.            
      234 +- **naklady.py** čte jen uložený [spotreba.csv](ai-log/07-nakl
          +ady/spotreba.csv), takže výpočet nákladů funguje i bez logů.  
      235 +                                                              
      236 +## Struktura repa                                             
      237 +                                                              
      238 +| cesta | obsah |                                             
      239  |---|---|
      101 -| `PLAN.md` | plán projektu |                                 
      102 -| `data/kandidati.csv` | kandidáti ze seznamů |               
      103 -| `data/vystup_agenta/` | původní výstup agenta (zařazení, vyř
          -azení, hraniční a nevyřešené případy), beze změn |            
      104 -| `data/hodnoceni.csv` | ruční hodnocení všech kandidátů |    
      105 -| `data/opraveno/` | opravená verze po ručním hodnocení |     
      106 -| `scripts/` | skripty pro automatickou kontrolu a měření |   
      107 -| `ai-log/` | exporty konverzací s agenty |                   
      240 +| `PLAN.md`, `NAKLADY.md`, `README.md`, `LICENSE` | plán, nákl
          +ady, tento přehled, licence |                                 
      241 +| `data/kandidati.csv` | 57 kandidátů |                       
      242 +| `data/vystup_agenta/` | původní výstup agenta: `investori.js
          +on`, `vyrazeni.csv`, `hranicni.csv`, `nevyresene.csv` |       
      243 +| `data/hodnoceni.csv`, `data/vzorek_kontroly.csv` | ruční hod
          +nocení, vzorek 20 firem |                                     
      244 +| `data/mereni_vzorku.md` | výsledky měření |                 
      245 +| `data/opraveno/` | opravená verze, `stav_kontroly.csv`, `ZME
          +NY.md` |                                                      
      246 +| `scripts/` | sběr, výběr vzorku, validátor a testy, měření, 
          +spotřeba, náklady, opravy |                                   
      247 +| `ai-log/00-…08-*.txt` | exporty session kroků 0–8 |         
      248 +| `ai-log/01-kandidati/` | výňatky zdrojů sběru, ověření sídel
          +, opravy sběru, sběrné skripty |                              
      249 +| `ai-log/02-zkusebni-davka/` | archiv zkušební dávky, měření,
          + surové odpovědi |                                            
      250 +| `ai-log/02-obohaceni/` | mapování 57 id, duplicity, nejasnos
          +ti, měření, zadání pomocného agenta, surové odpovědi ARES a fu
          +nding.tech.eu |                                               
      251 +| `ai-log/03-kontrola/` | zpráva automatické kontroly |       
      252 +| `ai-log/04-kontrola-zdroju/` | slepá kontrola, cílené otázky
          +, měření, log požadavků |                                     
      253 +| `ai-log/05-rucni-kontrola/` | průvodce, nálezy AI, stav hodn
          +ocení před nálezy, skript přípravy |                          
      254 +| `ai-log/07-naklady/` | agregovaná spotřeba a výpočet nákladů
          + |                                                            
      255  
      256  ## Licence
      257  
      111 -Viz [LICENSE](LICENSE).                                       
      258 +Na autorskou práci v repozitáři (plán, kód, dokumentace, výběr
          + a uspořádání dat) se vztahuje [LICENSE](LICENSE): prohlížení 
          +je dovolené jen pro hodnocení ve výběrovém řízení, jiné použit
          +í jen s mým písemným souhlasem. Data z veřejných zdrojů se říd
          +í podmínkami svých vlastníků. Data z funding.tech.eu jsou pod 
          +CC BY 4.0, atribuci uvádím [výše](#data-fundingtecheu-licence-
          +a-atribuce).                                                  

❯ Do README doplň k části o měření (bod 3) odůvodnění postupu.
  Piš věcně, ne jako omluvu:

  - Plán počítal s ruční kontrolou všech záznamů. Kvůli termínu
    odevzdání (30. 10.) a rozsahu jsem kontrolu zúžil na náhodný
    vzorek 20 z 27 zařazených, aby šla udělat pořádně a výsledek
    měl změřitelnou nejistotu (Wilsonův interval).
  - Většina zdrojů je anglicky nebo ukrajinsky, proto jsem při
    vyhledávání a překladu použil AI. Verdikty jsem schvaloval
    a sporné výklady rozhodoval já.
  - Zeptal jsem se zadavatele, zda je kontrola s asistencí AI
    přijatelná. Kvůli termínu jsem na odpověď nečekal a postup jsem
    místo toho podrobně zdokumentoval, aby ho šlo posoudit.
  - Aby šlo posoudit, co udělala AI a co já, je to u každého řádku
    označené, stav před nálezy kontrolního agenta je uložený zvlášť
    a srovnání jeho přínosu je v měření.

  Nic jiného neměň. Ukaž celé upravené README, zatím necommituj.

⏺ Update(README.md)
  ⎿  Added 7 lines
      77  
      78  **Vzorek.** Ručně (s asistencí AI, viz [Ruční kontrola – kdo ho
          dnotil](#ruční-kontrola--kdo-hodnotil)) jsem hodnotil náhodný v
          ýběr 20 z 27 původně zařazených, deset polí na firmu. Výběr děl
          á `random.Random(20261027).sample(sorted(ids), 20)` ve [scripts
          /vyber_vzorku.py](scripts/vyber_vzorku.py), výsledek je v [data
          /vzorek_kontroly.csv](data/vzorek_kontroly.csv). Skript i sezna
          m vznikly mimo Claude Code. Do repa přišly až v commitu 35583d9
          , spolu s rozpracovaným hodnocením. Agent v něm opravil jen ces
          tu k souboru a načítání a ověřil, že ze seedu vychází tentýž se
          znam ([05-rucni-kontrola-ulozeni.txt](ai-log/05-rucni-kontrola-
          ulozeni.txt), úsek „its output matches data/vzorek_kontroly.csv
           byte for byte“). Výběr je tedy reprodukovatelný ze seedu. Kdy 
          losování proběhlo vzhledem k začátku hodnocení, ale log nedoklá
          dá.
      79  
      80 +**Proč vzorek a asistence AI.**                                
      81 +                                                               
      82 +- Plán počítal s ruční kontrolou všech záznamů. Kvůli termínu o
         +devzdání (30. 10.) a rozsahu práce jsem kontrolu zúžil na náhod
         +ný vzorek 20 z 27 zařazených. Vzorek šlo zkontrolovat pořádně a
         + výsledek má změřitelnou nejistotu (Wilsonův interval).        
      83 +- Většina zdrojů je anglicky nebo ukrajinsky, proto jsem při vy
         +hledávání a překladu použil AI. Verdikty jsem schvaloval a spor
         +né výklady rozhodoval já.                                      
      84 +- Zadavatele jsem se zeptal, jestli je kontrola s asistencí AI 
         +přijatelná. Kvůli termínu jsem na odpověď nečekal a postup jsem
         + místo toho podrobně zdokumentoval, aby ho šlo posoudit.       
      85 +- Podíl AI a můj jde rozlišit: každý hodnocený řádek v `hodnoce
         +ni.csv` má ve sloupci `hodnotil` označení. Stav před přečtením 
         +nálezů kontrolního agenta je uložený zvlášť a v něm je u každéh
         +o řádku uvedeno, jestli verdikt navrhl Claude, nebo ChatGPT. Sr
         +ovnání přínosu kontrolního agenta je v [mereni_vzorku.md](data/
         +mereni_vzorku.md), oddíl 5.                                    
      86 +                                                               
      87  **Správnost zařazení** (jednotka = firma, 95% Wilsonův interval
          ):
      88  
      89  | | výsledek |

⏺ Bash(python3 - <<'E'
      import re,os,unicodedata…)
  ⎿  (No output)

⏺ Written for: hodnotitelé praktické úlohy v Clientelu.

  README je přepsané a doplněné o odůvodnění u měření. Změnil jsem jen
  README.md. Necommitoval jsem. Relativní odkazy i kotvy jsem zkontroloval,
  všechny vedou na existující soubory a nadpisy. Čísla v README odpovídají
  mereni_vzorku.md, ZMENY.md, stav_kontroly.csv a NAKLADY.md.

  Všechny skripty jsem spustil bez sítě v dočasné kopii repa a dávají stejné
  výstupy jako soubory v repu. Výjimky jsou dvě:
  - zkontroluj_data.py bez --over-url přepíše uloženou zprávu verzí bez kontroly
    URL.
  - spotreba_z_logu.py teď skončí chybou, protože nezná session kroku 8
    (66ed04b9…). spotreba.csv přitom nepřepíše. V README je to uvedené, skript
    jsem neměnil.

  Rozdíly proti CHYBY.md a zadání

  ~/Downloads/CHYBY.md neexistuje a nenašel jsem ho nikde v domovské složce.
  Rozdíly níže jsou proto mezi body tvého zadání a repem.

  1. Chyby ChatGPT: repo ani log žádnou nedokládají. ChatGPT navrhl 7 verdiktů
     (sektory a ticket) a žádný se později nezměnil. Všechny později opravené
     verdikty navrhl Claude v chatu. V README to tak stojí.
  2. Kontrolní součet 157/156: podle zadání je to chyba kontrolující AI. V
     06-mereni.txt ale stojí, že počty jsi „spočítal nezávisle“. README uvádí,
     že původ čísla log nedokládá. Číslo 157 v kroku 5 bylo správné, protože
     zahrnovalo řádek sloučení. Chybné bylo až v kroku 6 pro pole dvaceti firem.
  3. Obcházení ochrany proti botům: log dokládá dva zamítnuté pokusy, ne jeden.
     Kromě zaka.vc v kroku 8 ještě curl s jiným User-Agent u zdrojů CasInvent v
     kroku 2. Uvedené jsou oba.
  4. Přepsané surové odpovědi: git eviduje oba přepsané soubory ARES jen v
     commitu 19ed337, přepsaný obsah byl tedy shodný a data se neztratila. Navíc
     log dokládá smazanou prázdnou chybovou odpověď funding.tech.eu a přepsání
     v dávce 2, které agent sám opravil.
  5. curl -k: proběhl u Theinu. U Tensoru stejný pokus zablokovalo oprávnění.
  6. i&i Prague: surová odpověď ARES
     ai-log/02-obohaceni/zdroje/ares_vr_09684221.json obsahuje text usnesení o
     nabídnutí 48 nových akcií i&i Prague. Hodnocení ř. 65 to nezmiňuje. README
     popisuje stav podle hodnocení, zvaž, jestli to chceš dořešit.
  7. Chyba kontrolního agenta: dokládá ji log, v zadání chyběla. Ve fázi A
     nezachytil lucemburský AIFM u KAYA, zachytil ho až ve fázi B. Uvedená je.
  8. Odhad pro ČR z počtu kol: doložená chyba návrhu z recenze, v zadání nebyla.
     Uvedená je stručně.
  9. Nový doplněk: tvrzení o jazyku zdrojů („většina anglicky nebo ukrajinsky“)
     a o dotazu na zadavatele jsou tvoje informace. V repu ani logu je ověřit
     nejde. Ukrajinské zdroje (Forbes UA, AIN.UA) se v datech vyskytují.

  Celé README

  # Databáze investorů

  Praktická úloha ve výběrovém řízení na pozici Junior AI Developer ve
  společnosti Clientelo. Zadání: pomocí AI agentů sestavit spolehlivou databázi
  investorů, kteří vkládají vlastní nebo svěřený kapitál do soukromých firem za
  podíl, ověřit postup na pilotu a změřit jeho přesnost, odhadnout počet
  investorů ve světě a náklady na zpracování celého světa.

  Pilot jsem udělal pro VC a CVC se sídlem v ČR. Pravidla, schéma záznamu a
  metodika měření jsou v [PLAN.md](PLAN.md), odhad nákladů v
  [NAKLADY.md](NAKLADY.md).

  ## Výsledek

  Ze 4 zdrojů jsem sestavil 57 kandidátů. Po sloučení Nation1 do N1 Ventures
  zbylo 56 subjektů.

  | | původní výstup agenta | opravená verze (krok 8) |
  |---|---|---|
  | zařazení (VC/CVC se sídlem v ČR) | 27 | **22** |
  | vyřazení, z toho `mimo_rozsah_pilotu` / `neni_investor` | 17 (15 / 2) |
  **19** (17 / 2) |
  | nevyřešení (k ručnímu rozhodnutí) | 11 | **14** |
  | hraniční (venture debt) | 1 | **1** |
  | celkem | 56 | 56 |

  - **22 zařazených neznamená 22 plně ověřených.** 7 z nich nebylo v kontrolním
  vzorku a ručně je nikdo nekontroloval. U zbylých 15 je stav v
  [stav_kontroly.csv](data/opraveno/stav_kontroly.csv): 4 s opravou poslední
  investice, 2 s polem, které nešlo ověřit, a 9 se všemi hodnocenými poli `ano`.
  I mezi nimi mají některé záznamy výhrady, například Credo, Rockaway nebo
  StartupYard.
  - **Mimo pilot není totéž co neinvestor.** `mimo_rozsah_pilotu` (17) znamená,
  že agent subjekt vyhodnotil jako investora jiného typu (PE, family office…)
  nebo se sídlem mimo ČR. Ručně to bylo potvrzené jen u N1 a i&i Biotech.
  `neni_investor` (Espira, McWin) znamená jen to, že investice za posledních 24
  měsíců není veřejně doložená. Kontrolní agent upozornil, že to samo
  nedokazuje, že nejde o investora
  ([cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md), oddíl „Espira
  a McWin“).
  - Pět přesunů z opravené verze: N1 a i&i Biotech jsem přesunul mimo pilot
  (správce fondu je v Lucembursku). Tensor (sídlo správce), i&i Prague (nástroj
  investice) a Presto (přiřazení investic) jsem přesunul mezi nevyřešené. U i&i
  Prague a Presta chybí důkaz, ale nic nedokládá, že nejde o investory.

  Odkazy:

  | co | kde |
  |---|---|
  | plán, pravidla, schéma | [PLAN.md](PLAN.md) |
  | kandidáti | [data/kandidati.csv](data/kandidati.csv) |
  | původní výstup agenta (beze změn, na něm se měřilo) |
  [data/vystup_agenta/](data/vystup_agenta/) |
  | opravená verze a přehled změn | [data/opraveno/](data/opraveno/),
  [ZMENY.md](data/opraveno/ZMENY.md) |
  | stav kontroly každého id |
  [data/opraveno/stav_kontroly.csv](data/opraveno/stav_kontroly.csv) |
  | ruční hodnocení | [data/hodnoceni.csv](data/hodnoceni.csv) |
  | vzorek kontroly | [data/vzorek_kontroly.csv](data/vzorek_kontroly.csv) |
  | měření | [data/mereni_vzorku.md](data/mereni_vzorku.md) |
  | náklady | [NAKLADY.md](NAKLADY.md) |
  | exporty konverzací a podklady | [ai-log/](ai-log/) |

  ## Pravidla a zdroje

  Zkrácená verze, plné znění je v [PLAN.md](PLAN.md), body 2–4.

  - **Rozsah pilotu:** VC nebo CVC, jehož investiční firma (správce, značka)
  sídlí v ČR. Tento rozsah jsem zvolil já, zadání uvádí VC fondy v jedné zemi
  jen jako příklad. Skutečného investora jiného typu nebo se sídlem jinde vedu
  jako `mimo_rozsah_pilotu`, ne jako neinvestora.
  - **Sídlo správce:** při ruční kontrole jsem rozhodl, že rozhoduje sídlo
  správce (GP/AIFM), ne kancelář nebo tým. Původní text pravidla tento případ
  neřešil (viz [Chyby a opravy](#chyby-a-opravy)).
  - **Doložená investice:** aspoň jedna zpráva o konkrétní transakci za
  posledních 24 měsíců k referenčnímu datu 26. 10. 2026. Portfolio na webu ani
  zápis společníka v rejstříku samy nestačí. Datum investice a datum oznámení se
  zapisují zvlášť a filtr pracuje s oznámením, když datum investice zdroj
  neuvádí.
  - **Nástroj:** podíl nebo konvertibilní nástroj. Účast v pre-seed, seed nebo
  series kole je přijatý pracovní předpoklad, ne doložený nástroj. Záznam opřený
  jen o něj má jistotu investice nejvýš `stredni`. Jak často je předpoklad
  chybný, změřené není.
  - **Aktivita:** `aktivni` (investice do 12 měsíců) a
  `investice_dolozena_12_24_mesicu` je moje vlastní pracovní definice. Popisuje
  veřejnou stopu, ne skutečnou aktivitu.
  - **Kapitál:** AUM, upsaný kapitál a velikost fondu se nezaměňují ani
  nesčítají. Ukládá se částka v původní měně, datum platnosti a druh ukazatele.
  - **Chybějící údaje:** zůstávají `null`, nic se neodhaduje. Údaj bez URL se
  nevyplňuje. Rozporné nebo nedostatečné důkazy o typu, nástroji, sídle nebo
  přiřazení investice vedou do `nevyresene.csv`.

  ### Zdroje kandidátů

  Staženo 26. 10. 2026. Kandidát může být ve více zdrojích (ve dvou a více je
  20, v jednom 37).

  | zdroj | kandidátů |
  |---|---|
  | [CVCA, řádní členové](https://cvca.cz/en/category/full-members/) | 19 |
  | [CEE Funding Map](https://www.pampam.city/funds-poland-BJpHbykKoXoBaILayYBs)
  | 38 |
  | [funding.tech.eu](https://funding.tech.eu/api-docs), kola českých firem
  2025–2026 (60 kol) | 26 |
  | [Dealroom, veřejný manifest](https://dealroom.co/investors/manifest.json) |
  1 |

  Omezení sběru: u 8 organizací z funding.tech.eu se sídlo nepodařilo doložit.
  Vedu je jako nevyřešené (`nevyreseno_sidlo` v
  [opravy_sberu.csv](ai-log/01-kandidati/opravy_sberu.csv)), kandidátů tak mohlo
  být až 65. Aplikace Dealroomu vracela HTTP 403. Dataset funding.tech.eu
  pokrývá jen 60 kol. Ověření sídel a výňatky ze zdrojů jsou v
  [ai-log/01-kandidati/](ai-log/01-kandidati/).

  **Nástroje:** Claude Code (Claude Opus 5.5) s WebSearch a WebFetch, veřejné
  API [ARES](https://ares.gov.cz/) pro identitu a IČO a veřejné bezklíčové API
  funding.tech.eu. Skripty jsou v Pythonu jen se standardní knihovnou.

  ### Data funding.tech.eu: licence a atribuce

  Podmínky jsem ověřil 26. 10. 2026 na
  [funding.tech.eu/for-ai](https://funding.tech.eu/for-ai),
  [api-docs](https://funding.tech.eu/api-docs) a v
  [llms.txt](https://funding.tech.eu/llms.txt). Stránka /terms vracela HTTP 429,
  nečetl jsem ji.

  - **Zdroj:** „Tech.eu Funding Explorer“, https://funding.tech.eu/api-docs.
  Použité API: `https://funding.tech.eu/api/v1` (`/rounds` a
  `/investors/{name}`), bezklíčové, pouze pro čtení, limit 120 požadavků za 60
  s, 600 za hodinu a 2 000 denně na IP. Ve sběru šlo zhruba o 120 požadavků.
  - **Licence dat:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  - **Úpravy:** [fundingtecheu_kola_cz_2025_2026.json](ai-log/01-kandidati/zdroj
  e/fundingtecheu_kola_cz_2025_2026.json) je nezměněná odpověď `/api/v1/rounds`
  (Czech Republic, 2025-01-01 až 2026-12-31), jen spojená ze stránek. [fundingte
  cheu_investori.json](ai-log/01-kandidati/zdroje/fundingtecheu_investori.json)
  je zkrácený výtah z `/api/v1/investors/{name}`. Z jmen investorů jsem odvodil
  seznam kandidátů. Částky ani data jsem neměnil a do `kandidati.csv` jsem je
  nepřebíral. U kandidátů z tohoto zdroje je v `zdroj_url` URL záznamu v API.
  - **Použití API:** původní pokyn pro sběr zakazoval po nedostupnosti webu
  použít náhradní nástroj. Použití API ho tedy nedodrželo. Schválil jsem ho
  dodatečně, až po dokončení sběru.

  ## Měření

  Podrobně v [data/mereni_vzorku.md](data/mereni_vzorku.md) (generuje
  [scripts/mereni.py](scripts/mereni.py)).

  **Vzorek.** Ručně (s asistencí AI, viz [Ruční kontrola – kdo
  hodnotil](#ruční-kontrola--kdo-hodnotil)) jsem hodnotil náhodný výběr 20 z 27
  původně zařazených, deset polí na firmu. Výběr dělá
  `random.Random(20261027).sample(sorted(ids), 20)` ve
  [scripts/vyber_vzorku.py](scripts/vyber_vzorku.py), výsledek je v
  [data/vzorek_kontroly.csv](data/vzorek_kontroly.csv). Skript i seznam vznikly
  mimo Claude Code. Do repa přišly až v commitu 35583d9, spolu s rozpracovaným
  hodnocením. Agent v něm opravil jen cestu k souboru a načítání a ověřil, že ze
  seedu vychází tentýž seznam
  ([05-rucni-kontrola-ulozeni.txt](ai-log/05-rucni-kontrola-ulozeni.txt), úsek
  „its output matches data/vzorek_kontroly.csv byte for byte“). Výběr je tedy
  reprodukovatelný ze seedu. Kdy losování proběhlo vzhledem k začátku hodnocení,
  ale log nedokládá.

  **Proč vzorek a asistence AI.**

  - Plán počítal s ruční kontrolou všech záznamů. Kvůli termínu odevzdání (30.
  10.) a rozsahu práce jsem kontrolu zúžil na náhodný vzorek 20 z 27 zařazených.
  Vzorek šlo zkontrolovat pořádně a výsledek má změřitelnou nejistotu (Wilsonův
  interval).
  - Většina zdrojů je anglicky nebo ukrajinsky, proto jsem při vyhledávání a
  překladu použil AI. Verdikty jsem schvaloval a sporné výklady rozhodoval já.
  - Zadavatele jsem se zeptal, jestli je kontrola s asistencí AI přijatelná.
  Kvůli termínu jsem na odpověď nečekal a postup jsem místo toho podrobně
  zdokumentoval, aby ho šlo posoudit.
  - Podíl AI a můj jde rozlišit: každý hodnocený řádek v `hodnoceni.csv` má ve
  sloupci `hodnotil` označení. Stav před přečtením nálezů kontrolního agenta je
  uložený zvlášť a v něm je u každého řádku uvedeno, jestli verdikt navrhl
  Claude, nebo ChatGPT. Srovnání přínosu kontrolního agenta je v
  [mereni_vzorku.md](data/mereni_vzorku.md), oddíl 5.

  **Správnost zařazení** (jednotka = firma, 95% Wilsonův interval):

  | | výsledek |
  |---|---|
  | správně / chybně / neověřeno | 15 / 2 / 3 |
  | přesnost na ověřitelných | 15/17 = **88,2 %** (65,7–96,7 %) |
  | konzervativně, neověřené jako chyba | 15/20 = **75,0 %** (53,1–88,8 %) |

  Obě chybná zařazení (N1, i&i Biotech) jsou **změny výkladu metodiky**, ne
  chyby agenta. Agent použil sídlo značky a týmu, já jsem při ruční kontrole
  rozhodl podle sídla správce. Bez nich je dolní mez 15/18 = 83,3 % (60,8–94,2
  %). Neověřené jsou Tensor (sídlo správce), i&i Prague (nástroj) a Presto
  (přiřazení investic).

  **Správnost vyplněných polí** (jednotka = pole firmy, 20 firem × 10 polí):

  | pole | přesnost ano/(ano+ne) | dolní mez s `nelze_overit` |
  |---|---|---|
  | **celkem** | 156/163 = **95,7 %** (91,4–97,9 %) | 156/175 = 89,1 %
  (83,7–92,9 %) |
  | posledni_investice (nejslabší) | 15/19 = 78,9 % (56,7–91,5 %) | 15/20 = 75,0
  % (53,1–88,8 %) |
  | rozsah_pilotu | 17/19 = 89,5 % (68,6–97,1 %) | 17/20 = 85,0 % (64,0–94,8 %)
  |
  | nezavislost_zdroju | 14/14 = 100 % (78,5–100 %) | 14/20 = 70,0 % (48,1–85,5
  %) |
  | ostatní pole | bez `ne` | viz mereni_vzorku.md |

  - `ne` je 7: 4 chyby výstupu (vždy přehlédnutá novější poslední investice:
  Look AI, Purple, Reflex, ZAKA), 2 změny výkladu metodiky (rozsah N1 a i&i
  Biotech) a 1 omezení schématu (dva intervaly ticketu i&i Biotech). Dalších 12
  polí nešlo ověřit (`nelze_overit`), nejvíc u nezávislosti zdrojů (6). Když se
  počítají jen chyby výstupu, vychází 156/160 = 97,5 % (93,7–99,0 %).
  - Úplnost: sektory vyplněné u 16/20 firem, ticket 11/20 (1 potvrzené chybění,
  N1), kapitál 8/20.
  - Souhrnný interval přes pole je optimistický, protože pole jedné firmy nejsou
  nezávislá.
  - **Sloučení Nation1 → N1** jsem hodnotil zvlášť (1 případ, správně) a do
  přesnosti polí nevstupuje.

  **Co měření neříká.**

  - Neříká, že databáze je ze 100 % správná.
  - Recall ani úplnost českého trhu změřené nejsou. Vyřazené, hraniční a
  nevyřešené kandidáty nikdo ručně nekontroloval a orientační srovnání se
  seznamy neproběhlo.
  - Měření platí pro původní výstup agenta. Opravená verze vychází ze stejného
  hodnocení a nové nezávislé hodnocení nemá.
  - Hodnocení vzniklo s asistencí AI a zčásti po přečtení nálezů kontrolního
  agenta. Není to nezávislý referenční standard.

  ## Náklady

  Podrobně v [NAKLADY.md](NAKLADY.md).

  - **Pilot (kroky 0–6), změřeno z logů Claude Code:** 193,3 mil. tokenů v 1 879
  požadavcích, 96 % tvoří čtení z cache. **V přepočtu na ceny API zhruba 108
  USD.** Pilot jsem ale nezaplatil přes API, běžel v rámci předplatného Claude,
  takže jde o přepočet, ne o zaplacenou částku. Na kandidáta to dělá 1,67 USD,
  na zařazený záznam 3,46 USD.
  - **Nezachycená spotřeba** v součtu chybí a není nulová: tokeny pomocného
  modelu WebFetch, výsledky WebSearch, asistence Claude a ChatGPT v chatu,
  webové požadavky ve sběru a kroky 7–9.
  - **Svět je scénář, ne změřený počet investorů:** 5 600–11 000 zařazených
  podle [PLAN.md](PLAN.md), bod 8.2. Poměr kandidátů k zařazeným (56/27), čas
  člověka 10–15 min na firmu, sazba 25 USD/h, násobky pro jazyky a rejstříky a
  podíl nevyřešených jsou modelové předpoklady.

  | svět, USD | nízká | střední | vysoká |
  |---|---|---|---|
  | sestavení s kontrolním vzorkem (AI + člověk) | 33 696 | 73 901 | 151 418 |
  | sestavení s plnou ruční kontrolou | 55 029 | 125 450 | 253 628 |
  | roční aktualizace poslední investice | 5 415 | 18 370 | 54 570 |

  Většinu lidských hodin tvoří ruční rozhodnutí nevyřešených kandidátů. Je to
  zároveň nejméně podložená položka, protože v pilotu je nikdo ručně
  nerozhodoval.

  ## Jak jsem pracoval s AI

  První návrh plánu vznikl v chatu. Implementaci, sběr a zpracování jsem dělal v
  Claude Code. Každý krok měl vlastní session, exporty jsou v
  [ai-log/](ai-log/). Krok 5 je jedna session exportovaná dvakrát:
  [05-priprava.txt](ai-log/05-priprava.txt) obsahuje přípravu,
  [05-rucni-kontrola-ulozeni.txt](ai-log/05-rucni-kontrola-ulozeni.txt) celou
  session včetně uložení hodnocení. Pomocní agenti (3 ve sběru, 31 v obohacení,
  13 v kontrole zdrojů) jsou v exportech zachycení jen svými závěrečnými
  zprávami hlavnímu agentovi. ChatGPT a Claude v chatu mi pomáhali s recenzí
  plánu, vyhledáním a překladem zdrojů a s návrhy verdiktů ruční kontroly.

  Agent podle zadání po každém kroku zastavil a vypsal výsledek. Commit dělal až
  po mém schválení.

  | krok, export | co jsem agentovi zadal | jak jsem výstup kontroloval |
  |---|---|---|
  | 0 [plán a založení](ai-log/00-plan-a-zalozeni.txt) | opravit PLAN.md podle
  externí recenze v ChatGPT a mé kontroly (kapitál, aktivita, důkazy, měření,
  odhad rozsahu, druhý agent), založit repo a ověřit git identitu | dvě kola
  diffu PLAN.md před schválením |
  | 1 [kandidáti](ai-log/01-kandidati.txt) | jen veřejné zdroje, nedostupnost
  zaznamenat a neobcházet, stabilní id, deduplikace bez zařazování, počet
  nepřizpůsobovat hypotéze | souhrn zdrojů a duplicit, dodatečné schválení API,
  ověření licence, 8 nevyřešených sídel, pravidla pilotu |
  | 2 [zkušební dávka](ai-log/02-zkusebni-davka.txt) | 5 kandidátů podle
  schématu, pak úprava pravidel typu a nástroje | diff pravidel a dopad na 5
  kandidátů, výstup dávky archivovaný beze změn |
  | 2 [obohacení](ai-log/02-obohaceni.txt) | všech 57 v dávkách po 10, pravidla
  neměnit, nejasnosti zapisovat, surové odpovědi ARES a funding.tech.eu ukládat,
  měřit čas a požadavky | souhrn a commit po každé dávce, formální kontrola
  skriptem, [nejasnosti.md](ai-log/02-obohaceni/nejasnosti.md) |
  | 3 [automatická kontrola](ai-log/03-kontrola.txt) | validátor struktury,
  pokrytí id, okna, nástroje a jistoty, upozornění na zdroje stažené bez ověření
  TLS, testy | testy na umělých chybách, zpráva
  [automaticka_kontrola.md](ai-log/03-kontrola/automaticka_kontrola.md) |
  | 4 [kontrola zdrojů](ai-log/04-kontrola-zdroju.txt) | druhý agent (stejný
  model, nová konverzace): fáze A naslepo bez README a historie, fáze B cílené
  otázky | závěry po polích v
  [slepa_kontrola.csv](ai-log/04-kontrola-zdroju/slepa_kontrola.csv), oprava
  vlastních chyb fáze A v
  [cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md) |
  | 5 [ruční kontrola](ai-log/05-rucni-kontrola-ulozeni.txt) | připravit
  průvodce a předvyplněné hodnocení bez verdiktů, nálezy AI oddělit, pak uložit
  hodnocení z mé kontroly | počty verdiktů a změn proti mým očekávaným hodnotám,
  při rozdílu bez commitu |
  | 6 [měření](ai-log/06-mereni.txt) | PLAN.md sladit se skutečným postupem,
  deterministický mereni.py, oddělit tři druhy `ne` | moje nezávislé kontrolní
  počty, rozdíl 157/156 dohledán před commitem |
  | 7 [náklady](ai-log/07-naklady.txt) | spotřeba jen z polí usage v lokálních
  logech, ceník z oficiálního zdroje, předpoklady výslovně označit | souhrn před
  commitem, druhé kolo úprav (sazba, rozsah aktualizace, význam vzorku) |
  | 8 [opravená verze](ai-log/08-opraveno.txt) | oprav.py jen podle dokončeného
  hodnocení, přesuny a opravy s odkazem na řádek hodnocení | návrh přesunů před
  provedením, zamítnuté nové pole v investori.json, validace v dočasné kopii |

  ### Ruční kontrola – kdo hodnotil

  „Petr Šťastný (asistence AI)“: zdroje vyhledal, přeložil a verdikt navrhl
  Claude, u části polí ChatGPT. Každý verdikt jsem schválil já a sporné
  výkladové otázky (sídlo správce, přiřazení přes fondy, chybějící údaje) jsem
  rozhodl sám. Štítek znamená schválení navržených verdiktů, ne to, že jsem
  osobně otevřel všechny zdroje. U všech polí jsem je neotevíral.

  Stav před přečtením nálezů kontrolního agenta je uložen zvlášť v [hodnoceni_pr
  ed_nalezy_ai.csv](ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv)
  (commit 35583d9). V něm je ještě rozlišeno, kdo verdikt navrhl: 194 řádků
  Claude, 7 ChatGPT. Změny po přečtení nálezů mají v poznámce „Změna po přečtení
  nálezů AI“.

  Kontrola proto není nezávislý referenční standard. Druhý agent byl stejný
  model v jiné konverzaci a hodnocení jsem dělal v pořadí podle jeho nálezů.
  Srovnání jeho přínosu je jen orientační: ze 4 chyb výstupu našla ruční
  kontrola 3 (Purple, Reflex, ZAKA) až po přečtení jeho nálezů. Po přečtení se
  také 6 verdiktů změnilo z `ano` na `nelze_overit`
  ([mereni_vzorku.md](data/mereni_vzorku.md), oddíl 5.4).

  ## Chyby a opravy

  Uvádím jen chyby doložené v repu a logu. Úsek v uvozovkách jde v uvedeném
  souboru vyhledat doslova. Druh chyby:

  - **pravidla:** chyba nebo mezera v mých pravidlech,
  - **aplikace:** chybné použití existujícího pravidla,
  - **schéma:** schéma neumí hodnotu zapsat,
  - **neurčeno:** příčinu z logu nejde zjistit.

  ### Návrh a pravidla

  | chyba | druh | kdo našel | řešení | doklad |
  |---|---|---|---|---|
  | Plán z chatu definoval kapitál jako součet upsaného kapitálu nebo AUM, takže
  zaměňoval a sčítal různé ukazatele. | pravidla | externí recenze v ChatGPT |
  v kroku 0 nahrazeno seznamem `kapital` s druhem ukazatele a datem, bez sčítání
  | [00-plan-a-zalozeni.txt](ai-log/00-plan-a-zalozeni.txt): „Celkový
  investiční kapitál** = součet upsaného kapitálu“ |
  | Hranici aktivity 12 měsíců plán připisoval CEE Funding Map, ta ale měří dvě
  investice za rok. | pravidla | recenze v ChatGPT | v kroku 0 označeno jako
  moje vlastní pracovní definice, status přejmenován | tamtéž: „Hranici 12
  měsíců přebírám od CEE“ |
  | Odhad pro ČR byl odvozený z počtu investičních kol, částky se převáděly na
  EUR. | pravidla | recenze v ChatGPT | v kroku 0 hypotéza bez odvození, původní
  měna | tamtéž: „Odhad vychází z počtu kol“ |
  | Pravidlo „investiční firma (správce, značka) sídlí v ČR“ neurčuje, co platí,
  když správce sídlí v cizině a tým v Praze. | pravidla | kontrolní agent (fáze
  B), rozhodnuto při ruční kontrole | rozhodnuto podle sídla správce: N1 a i&i
  Biotech mimo pilot, Tensor nevyřešený. Text pravidla v PLAN.md upřesněný není
  a KAYA neposouzená, **nenapraveno, uvedeno jako omezení** |
  [cilene_otazky.md](ai-log/04-kontrola-zdroju/cilene_otazky.md): „PLAN.md
  neříká, co platí, když správce (GP/AIFM) sídlí jinde než značka a tým“ |

  ### Sběr a obohacení (agent)

  | chyba | druh | kdo našel | řešení | doklad |
  |---|---|---|---|---|
  | Agent ve sběru použil API funding.tech.eu, i když pokyn zakazoval po
  nedostupnosti webu náhradní nástroj (provedená akce). | aplikace | agent to
  sám uvedl v souhrnu, rozhodl jsem já | dodatečně schváleno a zapsáno výše |
  [01-kandidati.txt](ai-log/01-kandidati.txt): „neobcházej ho přes cache, mirror
  ani jiný nástroj“, „API funding.tech.eu dodatečně schvaluji“ |
  | Look AI, Purple, Reflex: agent přehlédl novější doloženou investici. |
  neurčeno | Look AI ruční kontrola před nálezy AI, Purple a Reflex kontrolní
  agent (fáze A) | v opravené verzi nová poslední investice, původní přesunutá
  do `dalsi_investice` | [hodnoceni.csv](data/hodnoceni.csv) ř. 127, 147, 157;
  [04-kontrola-zdroju.txt](ai-log/04-kontrola-zdroju.txt): „Embodied“,
  „ArtMaster“ |
  | ZAKA: agent FinalDose znal, ale vlastní oznámení investora nepřijal jako
  zprávu o transakci, přestože ho PLAN.md připouští. | aplikace | kontrolní
  agent (fáze A) | v opravené verzi FinalDose, stránka v kroku 8 znovu načtena
  nebyla (viz Omezení) | poznámka záznamu v
  [vystup_agenta/investori.json](data/vystup_agenta/investori.json): „ty jsem
  nezávislou zprávou o transakci neověřil“; hodnoceni.csv ř. 48 |
  | i&i Prague: agent označil nástroj jako `dolozeno` podle rejstříku CasInvent.
  Podle hodnocení zápis uvádí i&i Prague jako akcionáře jen v roce 2020
  (historický zápis) a nástroj u kola 2025 nedokládá. Kandidát měl jít do
  nevyřešených. | aplikace | ruční kontrola (kontrolní agent pole označil jako
  sedící) | přesun do `nevyresene.csv` (otázka `nastroj`) |
  [02-obohaceni.txt](ai-log/02-obohaceni.txt): „Podíl dokládá výpis z rejstříku
  CasInvent“; hodnoceni.csv ř. 65 |
  | Presto: agent připsal Prestu investice fondu Tech Horizons (lucemburský
  správce). Vazba není doložená, ale ani vyvrácená. | neurčeno | ruční kontrola
  (kontrolní agent pole označil jako sedící) | přesun do `nevyresene.csv`
  (otázka `investice`) | 02-obohaceni.txt: „investice SatVu a Occam přičítám
  Presto Ventures“; hodnoceni.csv ř. 293 |
  | N1: chybí ticket, který web uvádí („Typical 1st investment $100K–$1M“). |
  neurčeno | ruční kontrola | zapsáno v ZMENY.md, záznam je mimo pilot |
  hodnoceni.csv ř. 10 |
  | i&i Biotech: dva intervaly ticketu sloučené do jednoho 150 tis.–2 mil. EUR.
  | schéma | ruční kontrola (návrh verdiktu ChatGPT) | v ZMENY.md oba intervaly,
  společný interval se nepoužije | 02-obohaceni.txt: „Ticket podle webu je 150
  tis. až 2 mil. EUR.“; hodnoceni.csv ř. 41 |

  ### Postup a bezpečnost

  | chyba | provedeno / zamítnuto | kdo našel | řešení | doklad |
  |---|---|---|---|---|
  | Stažení profilu CVCA (Thein) přes `curl -k`, tedy bez ověření TLS. |
  provedeno u Theinu, u Tensoru pokus zablokovalo oprávnění | agent sám v
  souhrnu dávky | automatická kontrola to hlásí jako upozornění. Zdroj se znovu
  neověřoval a Thein ručně kontrolovaný není, **nenapraveno, uvedeno jako
  omezení** | 02-obohaceni.txt: „stáhl přes curl -k kvůli chybě certifikátu“,
  „Curl bez ověření certifikátu zablokovala oprávnění“ |
  | Přepsané surové odpovědi ARES: agent dávky 3 znovu stáhl
  `ares_hledani_iiPrague.json` a `ares_vr_06058485.json` z dávky 2. | provedeno
  | hlavní agent | git eviduje oba soubory jen v commitu 19ed337, přepsaný obsah
  byl tedy shodný. Přepsání varianty hledání v dávce 2 agent opravil sám
  přejmenováním. Jiný agent smazal prázdnou chybovou odpověď funding.tech.eu, ta
  obnovená není | 02-obohaceni.txt: „Přepsané surové soubory ARES“, „přepsala
  soubor“, „Odstraněný soubor:“ |
  | Pokus obejít ochranu proti botům: curl s jiným User-Agent (krok 2, zdroje
  CasInvent) a opakované načtení zaka.vc po HTTP 466 (krok 8). | oba zamítnuté
  klasifikátorem, neproběhly | klasifikátor oprávnění Claude Code | agent
  pokračoval bez stránek, FinalDose proto znovu načtené není | 02-obohaceni.txt:
  „zamítl klasifikátor (obcházení ochrany proti botům)“;
  [08-opraveno.txt](ai-log/08-opraveno.txt): „Bot Check Circumvention“ |

  ### Kontrola a měření

  | chyba | druh | kdo našel | řešení | doklad |
  |---|---|---|---|---|
  | Kontrolní agent ve fázi A nezachytil lucemburský AIFM u KAYA. Označil také 5
  dvojic, které konečné hodnocení nepotvrdilo, a neoznačil Presto, nástroj i&i
  Prague ani ticket i&i Biotech. | aplikace | sám ve fázi B; srovnání v
  mereni_vzorku.md | KAYA zůstává zařazená a neposouzená, **nenapraveno, uvedeno
  jako omezení** | cilene_otazky.md: „U Kaya to první agent ani fáze A
  nezachytili“ |
  | Claude v chatu (asistence ruční kontroly) navrhl `ano` u poslední investice
  Purple, Reflex a ZAKA a přehlédl novější investice. Schválil jsem to. |
  aplikace | kontrolní agent, převzato po přečtení jeho nálezů | změna na `ne`,
  oprava v kroku 8 | [hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hod
  noceni_pred_nalezy_ai.csv); 05-rucni-kontrola-ulozeni.txt: „Očekávám přesně 9
  změn“ |
  | Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem, kde agent vedl
  zdroje s neznámým původem. | aplikace | kontrolní agent | změna na
  `nelze_overit`, `puvod` ani `jistota` se v opravené verzi nemění | tamtéž |
  | Kontrolní počet 157 `ano` v mém zadání kroku 6 započítal i řádek sloučení
  Nation1 → N1, správně je 156 pro pole 20 firem. Kdo počet připravil, log
  nedokládá. | neurčeno | agent kroku 6 | potvrdil jsem 156, sloučení se
  vykazuje zvlášť | [06-mereni.txt](ai-log/06-mereni.txt): „Skript dává 156 ano
  místo kontrolních 157“ |
  | [mereni.txt kontroly zdrojů](ai-log/04-kontrola-zdroju/mereni.txt) uvádí
  jako „tokeny subagentů“ velikost kontextu posledního volání, ne spotřebu. |
  aplikace | agent kroku 7 | NAKLADY.md počítá s kumulativní spotřebou z logů.
  mereni.txt zůstal beze změny, rozdíl je vysvětlený v NAKLADY.md |
  [07-naklady.txt](ai-log/07-naklady.txt): „nejsou spotřeba, ale“ |

  U ChatGPT repo ani log chybu nedokládají. Jeho 7 navržených verdiktů zůstalo
  po přečtení nálezů beze změny.

  ## Omezení a nedokončené části

  - **Sedm zařazených mimo vzorek** (ČS Seed Starter, Fazole, JIC Ventures, J&T
  Ventures, KAYA, Lighthouse, Tilia) ručně kontrolovaných není.
  - **Vyřazení, hraniční a nevyřešení** z původního výstupu (29 kandidátů) ručně
  kontrolovaní nejsou. Žádný nevyřešený případ jsem ručně nerozhodl, ani
  původní 11, ani 3 nové.
  - **Sídlo správce:** KAYA má podle kaya.vc/sustainability správce
  registrovaného jako lucemburský AIFM. Podle pravidla použitého u N1 by patřila
  mimo pilot, ale posouzená není a zůstává zařazená. Má i známý nález
  automatické kontroly: `fond` vyplněný u `committed_capital`. U Credo je
  neověřená role nové správcovské a.s.
  - **Nezávislost zdrojů** nešla ověřit u 6 z 20 firem (zdroje s neznámým
  původem mohou vycházet z jedné tiskové zprávy).
  - **Poslední investice** je nejnovější doložená, ne záruka, že novější
  neexistuje. Byla to nejslabší kategorie polí.
  - **ZAKA:** stránku zaka.vc/news se při tvorbě oprav nepodařilo znovu načíst.
  Oprava na FinalDose vychází z dřívějšího hodnocení s asistencí AI a z kontroly
  druhým agentem. PerfectBit (tisková zpráva 18. 8. 2026) nikdo neposoudil a
  zapsaný není.
  - **Datum stažení:** zdroje čtené v kroku 8 mají `stazeno` 27. 10. 2026, tedy
  den po referenčním datu. Pozdější datum stažení samo neznamená, že informace k
  26. 10. 2026 neplatila. Automatická kontrola to při referenčním datu 26. 10.
  hlásí jako nesoulad (podrobnosti v ZMENY.md).
  - **Ostatní:** Thein stažený bez ověření TLS. Pracovní předpoklad u nástroje
  (účast v seed kole) změřený není. Prvních 5 kandidátů ovlivnilo úpravu
  pravidel, takže běh není test na neviděných datech. Recall a úplnost trhu
  změřené nejsou. Globální počty i náklady jsou scénáře.

  ## Spuštění

  Python 3 jen se standardní knihovnou, spouští se z kořene repa. Všechny
  skripty kromě `--over-url` běží bez sítě a jsou deterministické. Skripty v
  tabulce **přepisují svůj výstup v repu**. Při stejných vstupech vznikne stejný
  obsah, výjimky jsou uvedené.

  | účel | příkaz | přepisuje |
  |---|---|---|
  | seznam kandidátů | `python3 scripts/sestav_kandidaty.py` |
  `data/kandidati.csv`, `ai-log/01-kandidati/mimo_rozsah.csv` |
  | výběr vzorku | `python3 scripts/vyber_vzorku.py` |
  `data/vzorek_kontroly.csv` |
  | kontrola dat bez sítě | `python3 scripts/zkontroluj_data.py --vystup
  /tmp/kontrola.md` | nic (s `--vystup` mimo repo) |
  | kontrola dat včetně URL | `python3 scripts/zkontroluj_data.py --over-url` |
  `ai-log/03-kontrola/automaticka_kontrola.md` |
  | testy validátoru | `python3 -m unittest scripts/test_zkontroluj_data.py` |
  nic |
  | měření | `python3 scripts/mereni.py` | `data/mereni_vzorku.md` |
  | spotřeba z logů | `python3 scripts/spotreba_z_logu.py` |
  `ai-log/07-naklady/spotreba.csv` |
  | náklady | `python3 scripts/naklady.py` | `ai-log/07-naklady/vypocet.md` |
  | opravená verze | `python3 scripts/oprav.py` | soubory v `data/opraveno/` |

  - **zkontroluj_data.py:** uložená zpráva vznikla s `--over-url` (354 URL). Běh
  bez tohoto přepínače bez `--vystup` ji přepíše verzí bez kontroly URL.
  Výsledek kontroly URL se mění s časem a stavem webů. Další parametry jsou
  `--datum` (referenční datum, výchozí 2026-10-26) a `--koren`. Skript čte jen
  `data/vystup_agenta/`. Postup kontroly opravené verze v dočasném kořeni
  popisuje [ZMENY.md](data/opraveno/ZMENY.md). Návratový kód 1 znamená chybu
  struktury.
  - **spotreba_z_logu.py** potřebuje původní lokální logy Claude Code v
  `~/.claude/projects/`, jinde nepůjde zopakovat. Skript skončí chybou, když v
  adresáři logů projektu je session, kterou jeho tabulka `SESSIONY` nezná. To
  dnes platí pro session kroku 8 a pozdější, `spotreba.csv` se pak nepřepíše.
  - **naklady.py** čte jen uložený
  [spotreba.csv](ai-log/07-naklady/spotreba.csv), takže výpočet nákladů funguje
  i bez logů.

  ## Struktura repa

  | cesta | obsah |
  |---|---|
  | `PLAN.md`, `NAKLADY.md`, `README.md`, `LICENSE` | plán, náklady, tento
  přehled, licence |
  | `data/kandidati.csv` | 57 kandidátů |
  | `data/vystup_agenta/` | původní výstup agenta: `investori.json`,
  `vyrazeni.csv`, `hranicni.csv`, `nevyresene.csv` |
  | `data/hodnoceni.csv`, `data/vzorek_kontroly.csv` | ruční hodnocení, vzorek
  20 firem |
  | `data/mereni_vzorku.md` | výsledky měření |
  | `data/opraveno/` | opravená verze, `stav_kontroly.csv`, `ZMENY.md` |
  | `scripts/` | sběr, výběr vzorku, validátor a testy, měření, spotřeba,
  náklady, opravy |
  | `ai-log/00-…08-*.txt` | exporty session kroků 0–8 |
  | `ai-log/01-kandidati/` | výňatky zdrojů sběru, ověření sídel, opravy sběru,
  sběrné skripty |
  | `ai-log/02-zkusebni-davka/` | archiv zkušební dávky, měření, surové odpovědi
  |
  | `ai-log/02-obohaceni/` | mapování 57 id, duplicity, nejasnosti, měření,
  zadání pomocného agenta, surové odpovědi ARES a funding.tech.eu |
  | `ai-log/03-kontrola/` | zpráva automatické kontroly |
  | `ai-log/04-kontrola-zdroju/` | slepá kontrola, cílené otázky, měření, log
  požadavků |
  | `ai-log/05-rucni-kontrola/` | průvodce, nálezy AI, stav hodnocení před
  nálezy, skript přípravy |
  | `ai-log/07-naklady/` | agregovaná spotřeba a výpočet nákladů |

  ## Licence

  Na autorskou práci v repozitáři (plán, kód, dokumentace, výběr a uspořádání
  dat) se vztahuje [LICENSE](LICENSE): prohlížení je dovolené jen pro hodnocení
  ve výběrovém řízení, jiné použití jen s mým písemným souhlasem. Data z
  veřejných zdrojů se řídí podmínkami svých vlastníků. Data z funding.tech.eu
  jsou pod CC BY 4.0, atribuci uvádím
  [výše](#data-fundingtecheu-licence-a-atribuce).

❯ README přijímám s těmito úpravami, nic dalšího neměň:

  1. i&i Prague: cíleně zkontroluj pouze již uložený výpis
     ai-log/02-obohaceni/zdroje/ares_vr_09684221.json (CasInvent):
     pasáž o nabídce 48 nových akcií i&i Prague, její datum
     a případné doložení upsání nebo nabytí.
     Rozliš nabídku akcií od skutečně uskutečněné investice.
     Pokud pasáž mění závěr hodnocení, vypiš důkaz a zastav
     před commitem. Hodnocení ani data zatím neměň.
     Pokud závěr nemění, doplň tuto skutečnost do výhrady
     a netvrď, že výpis obsahuje pouze historický zápis z roku 2020.
  2. U nákladů upřesni, že 1,67 USD na kandidáta a 3,46 USD
     na zařazený záznam zahrnuje jen produkční část:
     sběr, obohacení a kontrolu druhým agentem.
     Nejde o rozpočítání celých 108 USD.
  3. Nahraď „moje nezávislé kontrolní počty“ formulací
     „kontrolní počty dodané v zadání, následně porovnané
     s výstupem skriptu“. Kontrolní počty pro krok 6 připravil
     Claude v chatu a započítal do nich řádek sloučení; uveď to
     u chyby 157/156 (druh: aplikace, kdo našel: agent kroku 6).
  4. Smaž odstavec „U ChatGPT repo ani log chybu nedokládají…“.
     Sedm nezměněných návrhů nedokládá bezchybnost modelu.
  5. Nezávislost zdrojů u 6 firem: „kdo našel“ = kontrolní agent
     u Y Soft, u ostatních pěti Claude v chatu při sjednocení výkladu.
  6. Věta „hodnocení jsem dělal v pořadí podle jeho nálezů“: firmy
     byly vybrané náhodně, pořadí v průvodci kontroly bylo seřazené
     podle nálezů kontrolního agenta. Formuluj přesně.
  7. „Commit dělal až po mém schválení“: popiš dva režimy. Buď jsem
     výsledek schválil po jeho vypsání, nebo jsem v zadání předem určil
     kontroly (očekávané počty, shodný výstup při dvou bězích, nezměněný
     původní výstup) a agent commitoval jen tehdy, když všechny prošly;
     jinak měl zastavit a vypsat rozdíl. Ověř v exportech, který krok
     běžel v jakém režimu.
  8. Do „Sběr a obohacení (agent)“ doplň tři doložené chyby z kroků 1–2
     (ověř v ai-log/01-kandidati.txt a ai-log/02-zkusebni-davka.txt,
     uveď doklad; co nedohledáš, nepiš):
     - 8 subjektů s nedoloženým sídlem zařazených mezi mimo rozsah
       (skryté vyřazení), opraveno v opravy_sberu.csv jako nevyřešené,
     - BD Partners zařazený jako VC, ačkoli se ve zdroji označuje jako
       „joint family office“; vedlo k pravidlu typu podle fungování
       a vlastního popisu,
     - tvrzení, že všech 5 kandidátů zkušební dávky splňuje podmínky,
       ačkoli nástroj nebyl doložen; vedlo ke třem úrovním dokladu
       nástroje a pravidlu neprima_indicie.
  9. Zkontroluj, že oddíl Licence není prázdný (vlastní práce podle
     LICENSE, data podle podmínek zdrojů, funding.tech.eu CC BY 4.0
     s odkazem na oddíl o atribuci).

  Pak ukaž změněné úseky a počet řádků, zkontroluj odkazy. Pokud bod 1
  nezastavil práci, commitni „Krok 9: README podle skutečného průběhu“
  a pushni.

⏺ Začínám bodem 1: projdu uložený výpis ARES u CasInvent.

⏺ Bash(python3 -I - <<'E'
      import json…)
  ⎿  (No output)

⏺ Bash(python3 -I - <<'E'
      import json…)
  ⎿  (No output)

⏺ Bod 1 mění závěr hodnocení, takže před commitem zastavím. Podrobnosti uvedu na
  konci. Teď ověřuji v exportech režimy commitů (bod 7).

⏺ Bash(cd /Users/petrstastny/Documents/Projekty/investori-databaze/ai-log && for
      f in *.txt; do echo "=== $f"; awk '/^❯ /{p=1} /^⏺ /{p=0} p' "$f" | grep
      -n -i -E "comm…)
  ⎿  (No output)

⏺ Exporty ukazují ještě třetí režim, kdy agent commitoval podle zadání bez
  předchozího schválení. Teď hledám tři chyby z bodu 8.

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 695,752p 02-zkusebni-davka.txt; echo -----; sed -n 1080,1090p
      01-kandidati.txt; sed -n 1328,1336p 01-kandidati.txt; sed -n 1410,1425p
      01-kandidati.txt)
  ⎿  (No output)

⏺ Bash(cd /Users/petrstastny/Documents/Projekty/investori-databaze && grep -n
      "cz-bd-partners" data/vystup_agenta/vyrazeni.csv | cut -c1-200; grep -c -F
      "8 se sídlem n…)
  ⎿  (No output)
⏺ Všechny tři chyby z bodu 8 jsou v logu doložené. Provádím úpravy 2–9.

⏺ Update(README.md)
  ⎿  Added 1 line, removed 1 line
      120  
      121  Podrobně v [NAKLADY.md](NAKLADY.md).
      122  
      123 -- **Pilot (kroky 0–6), změřeno z logů Claude Code:** 193,3 mil
          -. tokenů v 1 879 požadavcích, 96 % tvoří čtení z cache. **V př
          -epočtu na ceny API zhruba 108 USD.** Pilot jsem ale nezaplatil
          - přes API, běžel v rámci předplatného Claude, takže jde o přep
          -očet, ne o zaplacenou částku. Na kandidáta to dělá 1,67 USD, n
          -a zařazený záznam 3,46 USD.                                   
      123 +- **Pilot (kroky 0–6), změřeno z logů Claude Code:** 193,3 mil
          +. tokenů v 1 879 požadavcích, 96 % tvoří čtení z cache. **V př
          +epočtu na ceny API zhruba 108 USD.** Pilot jsem ale nezaplatil
          + přes API, běžel v rámci předplatného Claude, takže jde o přep
          +očet, ne o zaplacenou částku. Samotná produkční část (sběr, ob
          +ohacení a kontrola druhým agentem) stojí 1,67 USD na kandidáta
          + a 3,46 USD na zařazený záznam. To není rozpočítání celých 108
          + USD, plán, zkušební dávka, vývoj skriptů a měření v tom nejso
          +u.                                                            
      124  - **Nezachycená spotřeba** v součtu chybí a není nulová: token
           y pomocného modelu WebFetch, výsledky WebSearch, asistence Cla
           ude a ChatGPT v chatu, webové požadavky ve sběru a kroky 7–9.
      125  - **Svět je scénář, ne změřený počet investorů:** 5 600–11 000
            zařazených podle [PLAN.md](PLAN.md), bod 8.2. Poměr kandidátů
            k zařazeným (56/27), čas člověka 10–15 min na firmu, sazba 25
            USD/h, násobky pro jazyky a rejstříky a podíl nevyřešených js
           ou modelové předpoklady.
      126  

⏺ Update(README.md)
  ⎿  Added 1 line, removed 1 line
      147  | 3 [automatická kontrola](ai-log/03-kontrola.txt) | validátor
            struktury, pokrytí id, okna, nástroje a jistoty, upozornění n
           a zdroje stažené bez ověření TLS, testy | testy na umělých chy
           bách, zpráva [automaticka_kontrola.md](ai-log/03-kontrola/auto
           maticka_kontrola.md) |
      148  | 4 [kontrola zdrojů](ai-log/04-kontrola-zdroju.txt) | druhý a
           gent (stejný model, nová konverzace): fáze A naslepo bez READM
           E a historie, fáze B cílené otázky | závěry po polích v [slepa
           _kontrola.csv](ai-log/04-kontrola-zdroju/slepa_kontrola.csv), 
           oprava vlastních chyb fáze A v [cilene_otazky.md](ai-log/04-ko
           ntrola-zdroju/cilene_otazky.md) |
      149  | 5 [ruční kontrola](ai-log/05-rucni-kontrola-ulozeni.txt) | p
           řipravit průvodce a předvyplněné hodnocení bez verdiktů, nález
           y AI oddělit, pak uložit hodnocení z mé kontroly | počty verdi
           ktů a změn proti mým očekávaným hodnotám, při rozdílu bez comm
           itu |
      150 -| 6 [měření](ai-log/06-mereni.txt) | PLAN.md sladit se skutečn
          -ým postupem, deterministický mereni.py, oddělit tři druhy `ne`
          - | moje nezávislé kontrolní počty, rozdíl 157/156 dohledán pře
          -d commitem |                                                  
      150 +| 6 [měření](ai-log/06-mereni.txt) | PLAN.md sladit se skutečn
          +ým postupem, deterministický mereni.py, oddělit tři druhy `ne`
          + | kontrolní počty dodané v zadání, následně porovnané s výstu
          +pem skriptu; rozdíl 157/156 dohledán před commitem |          
      151  | 7 [náklady](ai-log/07-naklady.txt) | spotřeba jen z polí usa
           ge v lokálních logech, ceník z oficiálního zdroje, předpoklady
            výslovně označit | souhrn před commitem, druhé kolo úprav (sa
           zba, rozsah aktualizace, význam vzorku) |
      152  | 8 [opravená verze](ai-log/08-opraveno.txt) | oprav.py jen po
           dle dokončeného hodnocení, přesuny a opravy s odkazem na řádek
            hodnocení | návrh přesunů před provedením, zamítnuté nové pol
           e v investori.json, validace v dočasné kopii |
      153  

⏺ Update(README.md)
  ⎿  Added 1 line, removed 1 line
      204  | Kontrolní agent ve fázi A nezachytil lucemburský AIFM u KAYA
           . Označil také 5 dvojic, které konečné hodnocení nepotvrdilo, 
           a neoznačil Presto, nástroj i&i Prague ani ticket i&i Biotech.
            | aplikace | sám ve fázi B; srovnání v mereni_vzorku.md | KAY
           A zůstává zařazená a neposouzená, **nenapraveno, uvedeno jako 
           omezení** | cilene_otazky.md: „U Kaya to první agent ani fáze 
           A nezachytili“ |
      205  | Claude v chatu (asistence ruční kontroly) navrhl `ano` u pos
           lední investice Purple, Reflex a ZAKA a přehlédl novější inves
           tice. Schválil jsem to. | aplikace | kontrolní agent, převzato
            po přečtení jeho nálezů | změna na `ne`, oprava v kroku 8 | [
           hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hodnoce
           ni_pred_nalezy_ai.csv); 05-rucni-kontrola-ulozeni.txt: „Očekáv
           ám přesně 9 změn“ |
      206  | Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem,
            kde agent vedl zdroje s neznámým původem. | aplikace | kontro
           lní agent | změna na `nelze_overit`, `puvod` ani `jistota` se 
           v opravené verzi nemění | tamtéž |
      207 -| Kontrolní počet 157 `ano` v mém zadání kroku 6 započítal i ř
          -ádek sloučení Nation1 → N1, správně je 156 pro pole 20 firem. 
          -Kdo počet připravil, log nedokládá. | neurčeno | agent kroku 6
          - | potvrdil jsem 156, sloučení se vykazuje zvlášť | [06-mereni
          -.txt](ai-log/06-mereni.txt): „Skript dává 156 ano místo kontro
          -lních 157“ |                                                  
      207 +| Kontrolní počty pro krok 6 připravil Claude v chatu a do 157
          + `ano` započítal i řádek sloučení Nation1 → N1. Pro pole 20 fi
          +rem je správně 156. | aplikace | agent kroku 6 | potvrdil jsem
          + 156, sloučení se vykazuje zvlášť | [06-mereni.txt](ai-log/06-
          +mereni.txt): „Skript dává 156 ano místo kontrolních 157“ |    
      208  | [mereni.txt kontroly zdrojů](ai-log/04-kontrola-zdroju/meren
           i.txt) uvádí jako „tokeny subagentů“ velikost kontextu posledn
           ího volání, ne spotřebu. | aplikace | agent kroku 7 | NAKLADY.
           md počítá s kumulativní spotřebou z logů. mereni.txt zůstal be
           ze změny, rozdíl je vysvětlený v NAKLADY.md | [07-naklady.txt]
           (ai-log/07-naklady.txt): „nejsou spotřeba, ale“ |
      209  
      210  U ChatGPT repo ani log chybu nedokládají. Jeho 7 navržených ve
           rdiktů zůstalo po přečtení nálezů beze změny.

⏺ Update(README.md)
  ⎿  Removed 3 lines
      206  | Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem,
            kde agent vedl zdroje s neznámým původem. | aplikace | kontro
           lní agent | změna na `nelze_overit`, `puvod` ani `jistota` se 
           v opravené verzi nemění | tamtéž |
      207  | Kontrolní počty pro krok 6 připravil Claude v chatu a do 157
            `ano` započítal i řádek sloučení Nation1 → N1. Pro pole 20 fi
           rem je správně 156. | aplikace | agent kroku 6 | potvrdil jsem
            156, sloučení se vykazuje zvlášť | [06-mereni.txt](ai-log/06-
           mereni.txt): „Skript dává 156 ano místo kontrolních 157“ |
      208  | [mereni.txt kontroly zdrojů](ai-log/04-kontrola-zdroju/meren
           i.txt) uvádí jako „tokeny subagentů“ velikost kontextu posledn
           ího volání, ne spotřebu. | aplikace | agent kroku 7 | NAKLADY.
           md počítá s kumulativní spotřebou z logů. mereni.txt zůstal be
           ze změny, rozdíl je vysvětlený v NAKLADY.md | [07-naklady.txt]
           (ai-log/07-naklady.txt): „nejsou spotřeba, ale“ |
      209 -                                                              
      210 -U ChatGPT repo ani log chybu nedokládají. Jeho 7 navržených ve
          -rdiktů zůstalo po přečtení nálezů beze změny.                 
      211 -                                                              
      209  ## Omezení a nedokončené části
      210  
      211  - **Sedm zařazených mimo vzorek** (ČS Seed Starter, Fazole, JI
           C Ventures, J&T Ventures, KAYA, Lighthouse, Tilia) ručně kontr
           olovaných není.

⏺ Update(README.md)
  ⎿  Added 1 line, removed 1 line
      203  |---|---|---|---|---|
      204  | Kontrolní agent ve fázi A nezachytil lucemburský AIFM u KAYA
           . Označil také 5 dvojic, které konečné hodnocení nepotvrdilo, 
           a neoznačil Presto, nástroj i&i Prague ani ticket i&i Biotech.
            | aplikace | sám ve fázi B; srovnání v mereni_vzorku.md | KAY
           A zůstává zařazená a neposouzená, **nenapraveno, uvedeno jako 
           omezení** | cilene_otazky.md: „U Kaya to první agent ani fáze 
           A nezachytili“ |
      205  | Claude v chatu (asistence ruční kontroly) navrhl `ano` u pos
           lední investice Purple, Reflex a ZAKA a přehlédl novější inves
           tice. Schválil jsem to. | aplikace | kontrolní agent, převzato
            po přečtení jeho nálezů | změna na `ne`, oprava v kroku 8 | [
           hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hodnoce
           ni_pred_nalezy_ai.csv); 05-rucni-kontrola-ulozeni.txt: „Očekáv
           ám přesně 9 změn“ |
      206 -| Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem,
          - kde agent vedl zdroje s neznámým původem. | aplikace | kontro
          -lní agent | změna na `nelze_overit`, `puvod` ani `jistota` se 
          -v opravené verzi nemění | tamtéž |                            
      206 +| Claude v chatu navrhl `ano` u nezávislosti zdrojů u 6 firem,
          + kde agent vedl zdroje s neznámým původem. | aplikace | u Y So
          +ft kontrolní agent, u ostatních pěti Claude v chatu při sjedno
          +cení výkladu | změna na `nelze_overit`, `puvod` ani `jistota` 
          +se v opravené verzi nemění | tamtéž |                         
      207  | Kontrolní počty pro krok 6 připravil Claude v chatu a do 157
            `ano` započítal i řádek sloučení Nation1 → N1. Pro pole 20 fi
           rem je správně 156. | aplikace | agent kroku 6 | potvrdil jsem
            156, sloučení se vykazuje zvlášť | [06-mereni.txt](ai-log/06-
           mereni.txt): „Skript dává 156 ano místo kontrolních 157“ |
      208  | [mereni.txt kontroly zdrojů](ai-log/04-kontrola-zdroju/meren
           i.txt) uvádí jako „tokeny subagentů“ velikost kontextu posledn
           ího volání, ne spotřebu. | aplikace | agent kroku 7 | NAKLADY.
           md počítá s kumulativní spotřebou z logů. mereni.txt zůstal be
           ze změny, rozdíl je vysvětlený v NAKLADY.md | [07-naklady.txt]
           (ai-log/07-naklady.txt): „nejsou spotřeba, ale“ |
      209  ## Omezení a nedokončené části

⏺ Update(README.md)
  ⎿  Added 1 line, removed 1 line
      157  
      158  Stav před přečtením nálezů kontrolního agenta je uložen zvlášť
            v [hodnoceni_pred_nalezy_ai.csv](ai-log/05-rucni-kontrola/hod
           noceni_pred_nalezy_ai.csv) (commit 35583d9). V něm je ještě ro
           zlišeno, kdo verdikt navrhl: 194 řádků Claude, 7 ChatGPT. Změn
           y po přečtení nálezů mají v poznámce „Změna po přečtení nálezů
            AI“.
      159  
      160 -Kontrola proto není nezávislý referenční standard. Druhý agent
          - byl stejný model v jiné konverzaci a hodnocení jsem dělal v p
          -ořadí podle jeho nálezů. Srovnání jeho přínosu je jen orientač
          -ní: ze 4 chyb výstupu našla ruční kontrola 3 (Purple, Reflex, 
          -ZAKA) až po přečtení jeho nálezů. Po přečtení se také 6 verdik
          -tů změnilo z `ano` na `nelze_overit` ([mereni_vzorku.md](data/
          -mereni_vzorku.md), oddíl 5.4).                                
      160 +Kontrola proto není nezávislý referenční standard. Druhý agent
          + byl stejný model v jiné konverzaci. Firmy vzorku byly vybrané
          + náhodně, ale průvodce kontroly je řadil podle závažnosti nále
          +zů kontrolního agenta. Srovnání jeho přínosu je jen orientační
          +: ze 4 chyb výstupu našla ruční kontrola 3 (Purple, Reflex, ZA
          +KA) až po přečtení jeho nálezů. Po přečtení se také 6 verdiktů
          + změnilo z `ano` na `nelze_overit` ([mereni_vzorku.md](data/me
          +reni_vzorku.md), oddíl 5.4).                                  
      161  
      162  ## Chyby a opravy
      163  

⏺ Update(README.md)
  ⎿  Added 5 lines, removed 1 line
      136  
      137  První návrh plánu vznikl v chatu. Implementaci, sběr a zpracov
           ání jsem dělal v Claude Code. Každý krok měl vlastní session, 
           exporty jsou v [ai-log/](ai-log/). Krok 5 je jedna session exp
           ortovaná dvakrát: [05-priprava.txt](ai-log/05-priprava.txt) ob
           sahuje přípravu, [05-rucni-kontrola-ulozeni.txt](ai-log/05-ruc
           ni-kontrola-ulozeni.txt) celou session včetně uložení hodnocen
           í. Pomocní agenti (3 ve sběru, 31 v obohacení, 13 v kontrole z
           drojů) jsou v exportech zachycení jen svými závěrečnými zpráva
           mi hlavnímu agentovi. ChatGPT a Claude v chatu mi pomáhali s r
           ecenzí plánu, vyhledáním a překladem zdrojů a s návrhy verdikt
           ů ruční kontroly.
      138  
      139 -Agent podle zadání po každém kroku zastavil a vypsal výsledek.
          - Commit dělal až po mém schválení.                            
      139 +Commity probíhaly podle exportů ve třech režimech:            
      140  
      141 +- **Schválení po vypsání:** agent výsledek vypsal a commitoval
          + až po mém schválení. Tak běžel krok 0 (diff PLAN.md), úprava 
          +pravidel po zkušební dávce, krok 7 (souhrn spotřeby a variant)
          + a krok 8 (návrh přesunů a oprav).                            
      142 +- **Předem určené kontroly:** v zadání jsem určil kontroly, na
          +příklad očekávané počty, shodný výstup při dvou bězích nebo ne
          +změněný původní výstup. Agent commitoval, jen když všechny pro
          +šly, jinak měl zastavit a vypsat rozdíl. Tak běželo uložení ru
          +ční kontroly v kroku 5, krok 6 (zastavil na rozdílu 157/156 a 
          +commitoval po mém potvrzení) a závěrečné commity kroků 7 a 8. 
      143 +- **Commit podle zadání bez předchozího schválení:** agent výs
          +ledek sám zkontroloval, commitoval a pak vypsal souhrn. Tak bě
          +žel krok 1, výstup zkušební dávky, dávky obohacení (s ověřením
          + shody archivu zkušební dávky s commitem f4cd74d), kroky 3 a 4
          + a příprava podkladů v kroku 5. Výstup jsem kontroloval až po 
          +commitu a opravy šly do dalších commitů.                      
      144 +                                                              
      145  | krok, export | co jsem agentovi zadal | jak jsem výstup kont
           roloval |
      146  |---|---|---|
      147  | 0 [plán a založení](ai-log/00-plan-a-zalozeni.txt) | opravit
            PLAN.md podle externí recenze v ChatGPT a mé kontroly (kapitá
           l, aktivita, důkazy, měření, odhad rozsahu, druhý agent), zalo
           žit repo a ověřit git identitu | dvě kola diffu PLAN.md před s
           chválením |

⏺ Update(README.md)
  ⎿  Added 3 lines
      185  
      186  | chyba | druh | kdo našel | řešení | doklad |
      187  |---|---|---|---|---|
      188 +| Ve sběru agent zařadil 8 organizací s nedoloženým sídlem mez
          +i výskyty mimo rozsah, takže je skrytě vyřadil, přestože nebyl
          +y prokazatelně zahraniční. | aplikace | já při kontrole výsled
          +ku kroku 1 | vedeny jako nevyřešené v [opravy_sberu.csv](ai-lo
          +g/01-kandidati/opravy_sberu.csv), původní `mimo_rozsah.csv` be
          +ze změny | 01-kandidati.txt: „8 se sídlem nedoloženým“, „Osm s
          +ubjektů s nedoloženým sídlem zachovej jako nevyřešené“ |      
      189 +| Ve zkušební dávce agent zařadil BD Partners jako VC, i když 
          +se ve zdroji sám označuje jako „joint family office“. | pravid
          +la | agent sám jako nejasnost, rozhodl jsem já | nové pravidlo
          +: typ podle doloženého fungování a vlastního popisu. V měřeném
          + běhu je BD Partners `mimo_rozsah_pilotu` (family office) | [0
          +2-zkusebni-davka.txt](ai-log/02-zkusebni-davka.txt): „joint fa
          +mily office, nejsme klasický“ |                               
      190 +| Ve zkušební dávce agent prohlásil všech 5 kandidátů za inves
          +tory podle podmínek plánu, i když nástroj investice doložený n
          +ebyl. | aplikace | agent sám jako nejasnost, rozhodl jsem já |
          + tři úrovně dokladu nástroje (`dolozeno`, `neprima_indicie`, `
          +nezjisteno`) a pravidlo pro `neprima_indicie`. Výstup dávky je
          + archivovaný a neměřil se | tamtéž: „Všech pět kandidátů je in
          +vestor podle bodů 2 a 3“ |                                    
      191  | Agent ve sběru použil API funding.tech.eu, i když pokyn zaka
           zoval po nedostupnosti webu náhradní nástroj (provedená akce).
            | aplikace | agent to sám uvedl v souhrnu, rozhodl jsem já | 
           dodatečně schváleno a zapsáno výše | [01-kandidati.txt](ai-log
           /01-kandidati.txt): „neobcházej ho přes cache, mirror ani jiný
            nástroj“, „API funding.tech.eu dodatečně schvaluji“ |
      192  | Look AI, Purple, Reflex: agent přehlédl novější doloženou in
           vestici. | neurčeno | Look AI ruční kontrola před nálezy AI, P
           urple a Reflex kontrolní agent (fáze A) | v opravené verzi nov
           á poslední investice, původní přesunutá do `dalsi_investice` |
            [hodnoceni.csv](data/hodnoceni.csv) ř. 127, 147, 157; [04-kon
           trola-zdroju.txt](ai-log/04-kontrola-zdroju.txt): „Embodied“, 
           „ArtMaster“ |
      193  | ZAKA: agent FinalDose znal, ale vlastní oznámení investora n
           epřijal jako zprávu o transakci, přestože ho PLAN.md připouští
           . | aplikace | kontrolní agent (fáze A) | v opravené verzi Fin
           alDose, stránka v kroku 8 znovu načtena nebyla (viz Omezení) |
            poznámka záznamu v [vystup_agenta/investori.json](data/vystup
           _agenta/investori.json): „ty jsem nezávislou zprávou o transak
           ci neověřil“; hodnoceni.csv ř. 48 |

⏺ Bash(python3 - <<'E'
      import re,os…)
  ⎿  (No output)

⏺ Úpravy 2–9 jsou v README hotové. Necommitoval jsem, protože bod 1 mění závěr
  hodnocení u i&i Prague. Hodnocení ani data jsem neměnil. README má 269 řádků a
  všechny relativní odkazy a kotvy fungují.

  Bod 1: i&i Prague, výpis ARES u CasInvent

  Ve výpisu jsou tři relevantní místa:

  - Usnesení valné hromady z 22. 5. 2025, zapsané do rejstříku 30. 5. 2025
    (ostatniSkutecnosti[3]). Kapitál se zvyšuje o 768 000 Kč upsáním 384 akcií
    třídy C. Píše se v něm:
    - „48 ks Nových akcií … bude nabídnuto předem určenému zájemci, kterým je
      společnost i&i Prague, s.r.o., … IČO: 060 58 485“,
    - „každý z předem určených zájemců … nabídnuté Nové akcie upíše na základě
      smlouvy o úpisu akcií v den konání této valné hromady“,
    - emisní kurs akcií pro i&i Prague jde splatit započtením pohledávky 100 000
      EUR „z titulu Smlouvy o konvertibilní zápůjčce … ze dne 4. 3. 2025“.
  - Zapsaný stav k 30. 5. 2025: základní kapitál 9 408 000 Kč (8 640 000 +
    768 000), splaceno 100 %. Zapsaných je i všech 384 akcií třídy C.
  - Akcionáři: i&i Prague je ve výpisu jako akcionář zapsaná jen 18. 11.
    – 15. 12. 2020. Akcie jsou listinné na jméno, takže další akcionáře rejstřík
    neeviduje. Chybějící zápis proto nic nevyvrací.

  Nabídka a uskutečněná investice: samotné usnesení je jen nabídka. Rejstřík ale
  zapsal celé zvýšení jako splacené a všech 384 akcií třídy C. Usnesení přitom
  rozděluje všech 384 akcií mezi šest jmenovitě určených zájemců. Z toho plyne,
  že i&i Prague svých 48 akcií upsala a splatila, nejspíš převodem konvertibilní
  zápůjčky. Smlouvu o úpisu ani dohodu o započtení výpis neobsahuje, takže jde
  o nepřímý důkaz. Je ale mnohem silnější, než předpokládá hodnocení (ř. 65),
  podle kterého rejstřík i&i Prague dokládá jen v roce 2020.

  Dopad: pokud důkaz uznáš, splňuje i&i Prague nástroj podle PLAN.md (akcie a
  konvertibilní zápůjčka). Verdikt je_investor by se pak změnil z nelze_overit
  na ano a s ním:

  - i&i Prague by se z nevyresene.csv vrátila mezi zařazené,
  - zařazených by bylo 23, nevyřešených 13,
  - v měření by byla 16 správně zařazených a 2 neověřené.

  Prvotní závěr agenta v kroku 2 (akcie třídy C splacené započtením
  konvertibilní zápůjčky) by tím byl v podstatě potvrzený. Řádek o i&i Prague v
  README jsem zatím nechal beze změny, dokud se nerozhodneš.

  Bod 7: zjištění z exportů

  Exporty ukazují tři režimy, ne dva. V README jsou popsané všechny tři:

  - Schválení po vypsání: krok 0, úprava pravidel po zkušební dávce a první fáze
    kroků 7 a 8.
  - Předem určené kontroly: uložení ruční kontroly v kroku 5, krok 6 a závěrečné
    commity kroků 7 a 8.
  - Commit podle zadání bez předchozího schválení: krok 1, výstup zkušební
    dávky, dávky obohacení, kroky 3 a 4 a příprava podkladů v kroku 5. V
    zadáních stálo „commitni a pushni“ bez podmínek, takže agent commitoval sám.

  Změněné úseky

  1. Náklady: „Samotná produkční část (sběr, obohacení a kontrola druhým
     agentem) stojí 1,67 USD na kandidáta a 3,46 USD na zařazený záznam. To není
     rozpočítání celých 108 USD, plán, zkušební dávka, vývoj skriptů a měření v
     tom nejsou.“
  2. Tabulka kroků, krok 6: „kontrolní počty dodané v zadání, následně porovnané
     s výstupem skriptu; rozdíl 157/156 dohledán před commitem“.
  3. Chyba 157/156: „Kontrolní počty pro krok 6 připravil Claude v chatu a do
     157 ano započítal i řádek sloučení Nation1 → N1. Pro pole 20 firem je
     správně 156.“ Druh: aplikace, kdo našel: agent kroku 6.
  4. Odstavec o ChatGPT je smazaný.
  5. Nezávislost zdrojů, kdo našel: „u Y Soft kontrolní agent, u ostatních pěti
     Claude v chatu při sjednocení výkladu“.
  6. Pořadí kontroly: „Firmy vzorku byly vybrané náhodně, ale průvodce kontroly
     je řadil podle závažnosti nálezů kontrolního agenta.“
  7. Režimy commitů: nový odstavec se třemi režimy podle exportů, jak je popsáno
     výše.
  8. Tři nové řádky v „Sběr a obohacení (agent)“:
     - 8 organizací s nedoloženým sídlem skrytě vyřazených mezi výskyty mimo
       rozsah. Doklad v 01-kandidati.txt: „8 se sídlem nedoloženým“, „Osm
       subjektů s nedoloženým sídlem zachovej jako nevyřešené“.
     - BD Partners zařazený jako VC, i když se označuje jako „joint family
       office“. Doklad: „joint family office, nejsme klasický“. V měřeném běhu
       skončil jako mimo_rozsah_pilotu.
     - Všech 5 kandidátů zkušební dávky prohlášeno za investory bez doloženého
       nástroje. Doklad: „Všech pět kandidátů je investor podle bodů 2 a 3“.
  9. Licence: oddíl prázdný není. Obsahuje podmínky z LICENSE pro vlastní práci,
     podmínky zdrojů pro data a CC BY 4.0 u funding.tech.eu s odkazem na oddíl
     o atribuci.

  Jak chceš u i&i Prague pokračovat? Buď hodnocení a opravenou verzi upravíme
  podle tohoto výpisu, nebo do README doplním jen výhradu a nechám závěr
  nelze_overit. Pak commitnu a pushnu.

❯ U i&i Prague přijímám je_investor = ano na základě uloženého
  výpisu: výslovně uvedená konvertibilní zápůjčka z 4. 3. 2025,
  nabídka akcií a zapsané splacené zvýšení kapitálu.
  Neoznačuj samostatnou smlouvu o úpisu za přímo ověřenou.

  1. Před změnou zachovej současné hodnoceni.csv v
     ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv.
     Původní zálohu před nálezy AI neměň.
  2. Oprav verdikt je_investor u i&i Prague. Do poznámky uveď
     konkrétní části výpisu a vysvětli, že předchozí kontrola
     přehlédla údaje z roku 2025. Jde o opravu hodnocení, nikoli
     změnu pravidel. U posledni_investice téhož záznamu verdikt nech,
     jen v poznámce oprav tvrzení, že nastroj „dolozeno“ je chybně
     (doklad je nepřímý, ale existuje).
  3. Přepočítej měření a regeneruj opravená data.
     Očekávaný dopad:
     - zařazení ve vzorku: 16 správně, 2 chybně kvůli
       upřesnění metodiky, 2 neověřené (Tensor, Presto);
     - pole: 157 ano, 7 ne, 11 nelze_overit, 25 jen úplnost;
       je_investor 19 ano / 1 nelze_overit;
     - opravená data: 23 zařazených, 19 vyřazených,
       13 nevyřešených, 1 hraniční, všech 56 id právě jednou.
       Při jiném výsledku výpočet neupravuj, dohledej a vypiš rozdíl.
  4. Aktualizuj README, ZMENY.md a stav kontroly.
     Původní údaj o chybě agenta u i&i Prague nahraď
     popisem chyby následné kontroly s asistencí AI.
     Přepočítej také srovnání s kontrolním agentem:
     jeho původní souhlas u tohoto pole se nyní potvrdil.
     Staré hodnoty nahrazuj pouze tam, kde popisují změněný celkový
     výsledek (zařazení ve vzorku, souhrn polí, je_investor, počty
     opravené verze). Stejná čísla mohou zůstat správná u jiných
     ukazatelů – například 15/20 = 75 % u posledni_investice; ty neměň.
     Historická srovnání (stav před nálezy AI, stav před opravou
     i&i Prague) zachovej s označením, že jde o původní stav.
     Zkontroluj, jestli dotčená čísla z měření nejsou i v PLAN.md
     nebo NAKLADY.md, a uprav je podle stejného pravidla.
  5. Původní data/vystup_agenta/ a historické exporty neměň.
     Odhad nákladů ponech založený na původních 27 zařazených.

  Spusť příslušné kontroly: mereni.py a oprav.py dvakrát se shodným
  výstupem, validace opravené verze, odkazy v README, prázdný git diff
  data/vystup_agenta/. Pokud vše odpovídá, commitni dvěma commity:
  „Ruční kontrola: oprava hodnocení i&i Prague podle výpisu CasInvent,
  přepočet měření a opravené verze“ a „Krok 9: README podle skutečného
  průběhu“, pushni a vypiš souhrn a oba commity.

⏺ Začínám zálohou hodnocení a prohlídkou míst ve skriptech, která se týkají i&i
  Prague.

⏺ Bash(mkdir -p ai-log/09-readme && cp data/hodnoceni.csv
      ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv && cmp
      data/hodnoceni.csv ai-log/09-readme/hodnoceni_pr…)
  ⎿  Created ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv (+377
     -0)
        1 +soubor,id,pole,hodnoceni,pricina_chyby,poznamka,hodnotil,datum
        2 +investori.json,cz-n1-ventures,existence,nelze_overit,,"Značka 
          +doložena (web, CVCA, CzechCrunch), právní subjekty Nation 1 GP
          + S.à r.l. a GP II neověřeny v registru",Petr Šťastný (asistenc
          +e AI),2026-10-27                                              
        3 +investori.json,cz-n1-ventures,investicni_cinnost,ano,,"The VC 
          +Corner 4. 11. 2025: Novoflow, „with participation from N1 Vent
          +ures“",Petr Šťastný (asistence AI),2026-10-27                 
        4 +investori.json,cz-n1-ventures,je_investor,ano,,Forbes UA 3. 7.
          + 2025 jmenuje N1 Ventures v Series A Liki24. Web N1 řadí inves
          +tici pod U-Tech; přesný investiční subjekt a správcovská vazba
          + neověřeny,Petr Šťastný (asistence AI),2026-10-27             
        5 +investori.json,cz-n1-ventures,typ,ano,,n1.rocks: „Early-Stage 
          +VC“,Petr Šťastný (asistence AI),2026-10-27                    
        6 +investori.json,cz-n1-ventures,rozsah_pilotu,ne,chyba_pravidel,
          +"Upřesnění metodiky při ruční kontrole, ne jednoznačná chyba a
          +genta: správci (GP/AIFM) v Lucembursku, v Praze tým",Petr Šťas
          +tný (asistence AI),2026-10-27                                 
        7 +investori.json,cz-n1-ventures,posledni_investice,ano,,"Novoflo
          +w a datum oznámení sedí; nejnovější nalezená, úplnost neověřen
          +a",Petr Šťastný (asistence AI),2026-10-27                     
        8 +investori.json,cz-n1-ventures,nezavislost_zdroju,ano,,"Forbes 
          +UA uvádí tiskovou zprávu Liki24, Inventure přebírá Forbes",Pet
          +r Šťastný (asistence AI),2026-10-27                           
        9 +investori.json,cz-n1-ventures,sektory,ano,,n1.rocks: „AI · Hea
          +lthtech · Frontier Tech“,Petr Šťastný (asistence AI),2026-10-2
          +7                                                             
       10 +investori.json,cz-n1-ventures,ticket,,,"nevyplneno – pouze úpl
          +nost. Potvrzené chybění: agent nechal null, web n1.rocks uvádí
          + „Typical 1st investment $100K–$1M“ (hodnota i zdroj doloženy)
          +. Do přesnosti vyplněných hodnot nevstupuje.",Petr Šťastný (as
          +istence AI),2026-10-27                                        
       11 +investori.json,cz-n1-ventures,kapital,ano,,"n1.rocks: „we mana
          +ge $60M across two funds“, aum bez data",Petr Šťastný (asisten
          +ce AI),2026-10-27                                             
       12 +mapovani_id.csv,cz-nation1,slouceni,ano,,"CzechCrunch 18. 9. 2
          +023: „Přejmenovává se na N1“, stejní managing partneři",Petr Š
          +ťastný (asistence AI),2026-10-27                              
       13 +investori.json,cz-tensor-ventures,existence,ano,,"ARES: Tensor
          + Ventures a.s., Pernerova 635/57, Praha 8, VR aktivní; neověře
          +no, že je správcem fondů",Petr Šťastný (asistence AI),2026-10-
          +27                                                            
       14 +investori.json,cz-tensor-ventures,investicni_cinnost,ano,,"Sez
          +nam Zprávy 24. 2. 2026: ValkaAI pre-seed, „přidaly se také … T
          +ensor Ventures“",Petr Šťastný (asistence AI),2026-10-27       
       15 +investori.json,cz-tensor-ventures,je_investor,ano,,"TheSaaSNew
          +s: AppFactor seed 4 mil. USD, „The round was led by Tensor Ven
          +tures“; nástroj nepřímá indicie",Petr Šťastný (asistence AI),2
          +026-10-27                                                     
       16 +investori.json,cz-tensor-ventures,typ,ano,,tensor.ventures: „W
          +e participate in Seed and Series A rounds“,Petr Šťastný (asist
          +ence AI),2026-10-27                                           
       17 +investori.json,cz-tensor-ventures,rozsah_pilotu,nelze_overit,,
          +Web: Tensor Ventures GP S.à r.l. a Fund I SCSp v Lucembursku; 
          +správce druhého fondu (EIF) nedoložen,Petr Šťastný (asistence 
          +AI),2026-10-27                                                
       18 +investori.json,cz-tensor-ventures,posledni_investice,ano,,"Val
          +kaAI 24. 2. 2026 sedí; nejnovější nalezená, úplnost neověřena"
          +,Petr Šťastný (asistence AI),2026-10-27                       
       19 +investori.json,cz-tensor-ventures,nezavislost_zdroju,nelze_ove
          +rit,,"ValkaAI: Seznam Zprávy a Startbase (oba 24. 2. 2026, puv
          +od null). Původ zdrojů nedoložen: agent má u zdrojů puvod null
          + (vedené jako nezávislé), ale sám v poznámce uvádí, že nezávis
          +lost nedoložena / pravděpodobně společný podklad. Důkaz společ
          +ného původu nemám, proto nelze_overit; správná jistota stredni
          + správnost pole puvod nepotvrzuje. Opraveno pro konzistenci s 
          +Look AI, Miton, Purple a Y Soft (původní poznámka chybně uvádě
          +la, že zdroje nejsou označeny jako nezávislé). Změna po přečte
          +ní nálezů AI.",Petr Šťastný (asistence AI),2026-10-27         
       20 +investori.json,cz-tensor-ventures,sektory,ano,,"tensor.venture
          +s: AI, Quantum Revolution, Computational Biotech, Sustainable 
          +Tech",Petr Šťastný (asistence AI),2026-10-27                  
       21 +investori.json,cz-tensor-ventures,ticket,,,nevyplneno – pouze 
          +úplnost,Petr Šťastný (asistence AI),2026-10-27                
       22 +investori.json,cz-tensor-ventures,kapital,,,nevyplneno – pouze
          + úplnost,Petr Šťastný (asistence AI),2026-10-27               
       23 +investori.json,cz-kaya-vc,existence,,,,,                      
       24 +investori.json,cz-kaya-vc,investicni_cinnost,,,,,             
       25 +investori.json,cz-kaya-vc,je_investor,,,,,                    
       26 +investori.json,cz-kaya-vc,typ,,,,,                            
       27 +investori.json,cz-kaya-vc,rozsah_pilotu,,,,,                  
       28 +investori.json,cz-kaya-vc,posledni_investice,,,,,             
       29 +investori.json,cz-kaya-vc,nezavislost_zdroju,,,,,             
       30 +investori.json,cz-kaya-vc,sektory,,,,,                        
       31 +investori.json,cz-kaya-vc,ticket,,,,,                         
       32 +investori.json,cz-kaya-vc,kapital,,,,,                        
       33 +investori.json,cz-ii-biotech-investments,existence,ano,,"ARES:
          + Biotech Investments s.r.o., Pobřežní 394/12, Praha 8, VR akti
          +vní",Petr Šťastný (asistence AI),2026-10-27                   
       34 +investori.json,cz-ii-biotech-investments,investicni_cinnost,an
          +o,,"Lupa.cz 27. 3. 2026: Theorema pre-seed 3,3 mil. USD, inves
          +toři „NAVEC Investment Management, i&i Biotech Fund“",Petr Šťa
          +stný (asistence AI),2026-10-27                                
       35 +investori.json,cz-ii-biotech-investments,je_investor,ano,,"Pre
          +-seed, nástroj nepřímá indicie",Petr Šťastný (asistence AI),20
          +26-10-27                                                      
       36 +investori.json,cz-ii-biotech-investments,typ,ano,,ÚOCHB 30. 11
          +. 2022: „Luxemburg-based venture capital firm“,Petr Šťastný (a
          +sistence AI),2026-10-27                                       
       37 +investori.json,cz-ii-biotech-investments,rozsah_pilotu,ne,chyb
          +a_pravidel,"Upřesnění metodiky při ruční kontrole: fond i&i Bi
          +otech Fund I SCSp v Lucembursku („Luxemburg-based“), česká Bio
          +tech Investments s.r.o. je poradce a tým",Petr Šťastný (asiste
          +nce AI),2026-10-27                                            
       38 +investori.json,cz-ii-biotech-investments,posledni_investice,an
          +o,,Theorema 27. 3. 2026 sedí; nejnovější nalezená,Petr Šťastný
          + (asistence AI),2026-10-27                                    
       39 +investori.json,cz-ii-biotech-investments,nezavislost_zdroju,ne
          +lze_overit,,"Theorema: Lupa.cz, CzechCrunch, Vestbee (puvod nu
          +ll). Původ zdrojů nedoložen: agent má u zdrojů puvod null (ved
          +ené jako nezávislé), ale sám v poznámce uvádí, že nezávislost 
          +nedoložena / pravděpodobně společný podklad. Důkaz společného 
          +původu nemám, proto nelze_overit; správná jistota stredni sprá
          +vnost pole puvod nepotvrzuje. Opraveno pro konzistenci s Look 
          +AI, Miton, Purple a Y Soft (původní poznámka chybně uváděla, ž
          +e zdroje nejsou označeny jako nezávislé). Změna po přečtení ná
          +lezů AI.",Petr Šťastný (asistence AI),2026-10-27              
       40 +investori.json,cz-ii-biotech-investments,sektory,ano,,"Web: dr
          +ug discovery, medtech, diagnostics, AI",Petr Šťastný (asistenc
          +e AI),2026-10-27                                              
     … 337 more lines (ctrl+o to expand)
  ⎿  (files that changed while this command ran, by the command or by
     another process; a convenience view, not a review or audit of the
     command)

⏺ Bash(sed -n 20,200p scripts/oprav.py)
  ⎿  (No output)

⏺ Bash(sed -n 200,778p scripts/oprav.py | grep -n -i "VYHRADY\|def
      \|vysledek\|hodnocena_pole_ano\|s_vyhradou\|nelze_overit\|OCEKAV\|assert\|
      raise\|ZMENY\|U i&i Prague…)
  ⎿  (No output)

⏺ Bash(sed -n 330,385p scripts/oprav.py; sed -n 400,420p scripts/oprav.py; sed
      -n 515,600p scripts/oprav.py; sed -n 640,660p scripts/oprav.py; sed -n
      690,778p scripts/…)
  ⎿  (No output)

⏺ Plán: z oprav.py vyjmu přesun i&i Prague a přidám k ní výhradu o nepřímém
  dokladu. V mereni.py oddělím historické srovnání od opravy. Čtu mereni.py.

⏺ Bash(sed -n 17,120p scripts/mereni.py)
  ⎿  (No output)

  Searched for 1 pattern (ctrl+o to expand)

⏺ Bash(sed -n 120,130p scripts/mereni.py; sed -n 465,512p scripts/mereni.py)
  ⎿  (No output)

⏺ Bash(python3 - <<'E'
      import csv,io…)
  ⎿  (No output)

⏺ Bash(python3 - <<'E'
      import csv,io…)
  ⎿  Updated data/hodnoceni.csv (+2 -2)
      62  investori.json,cz-startupyard,kapital,,,nevyplneno – pouze úpln
          ost,Petr Šťastný (asistence AI),2026-10-27
      63  investori.json,cz-ii-prague,existence,ano,,"ARES: i&i Prague, s
          .r.o., Pobřežní 394/12, Praha 8, VR aktivní",Petr Šťastný (asis
          tence AI),2026-10-27
      64  investori.json,cz-ii-prague,investicni_cinnost,ano,,"KHAN-I 2. 
          7. 2025: „The remaining investment was backed by longstanding i
          nvestors including KHAN-I, i&i Prague“; Positiv.cz 26. 6. 2025 
          (TZ CasInvent)",Petr Šťastný (asistence AI),2026-10-27
      65 -investori.json,cz-ii-prague,je_investor,nelze_overit,,"Nástroj 
         -u kola 2025 nedoložen (kolo bez označení fáze). Agentem uvedený
         - doklad z rejstříku dokládá i&i Prague jako jediného akcionáře 
         -jen 18. 11.–15. 12. 2020 (založení), ne tuto investici. Podle p
         -ravidel měl kandidát jít do nevyřešených",Petr Šťastný (asisten
         -ce AI),2026-10-27                                              
      65 +investori.json,cz-ii-prague,je_investor,ano,,"Oprava hodnocení 
         +v kroku 9 (ne změna pravidel): předchozí kontrola s asistencí A
         +I přehlédla údaje z roku 2025 v uloženém výpisu ARES CasInvent 
         +(ai-log/02-obohaceni/zdroje/ares_vr_09684221.json, IČO 09684221
         +). Usnesení valné hromady z 22. 5. 2025, zapsané 30. 5. 2025: z
         +výšení základního kapitálu o 768 000 Kč upsáním 384 akcií třídy
         + C, z toho „48 ks Nových akcií … bude nabídnuto předem určenému
         + zájemci, kterým je společnost i&i Prague, s.r.o.“, s možností 
         +započtení pohledávky 100 000 EUR z „Smlouvy o konvertibilní záp
         +ůjčce … ze dne 4. 3. 2025“. Zapsaný stav k 30. 5. 2025: základn
         +í kapitál 9 408 000 Kč, splaceno 100 %, zapsáno 384 akcií třídy
         + C. Nástroj (konvertibilní zápůjčka a akcie) je tedy doložen, u
         +psání akcií i&i Prague je doloženo nepřímo (usnesení a zapsané 
         +splacené zvýšení); samostatná smlouva o úpisu ani dohoda o zapo
         +čtení přímo ověřeny nejsou. Zápis i&i Prague jako jediného akci
         +onáře 18. 11.–15. 12. 2020 je jiný, historický údaj. Původní ve
         +rdikt nelze_overit: ai-log/09-readme/hodnoceni_pred_opravou_ii_
         +prague.csv.",Petr Šťastný (asistence AI),2026-10-27            
      66  investori.json,cz-ii-prague,typ,ano,,Inkubátor a venture builde
          r s vlastním kapitálem a doloženou investicí = VC podle bodu 3 
          plánu,Petr Šťastný (asistence AI),2026-10-27
      67  investori.json,cz-ii-prague,rozsah_pilotu,ano,,"Česká s.r.o. v 
          Praze, investuje z vlastní společnosti",Petr Šťastný (asistence
           AI),2026-10-27
      68 -investori.json,cz-ii-prague,posledni_investice,ano,,"CasInvent 
         -Pharma, oznámení 26. 6. 2025 sedí; pozor: nastroj „dolozeno“ ch
         -ybně, viz je_investor",Petr Šťastný (asistence AI),2026-10-27  
      68 +investori.json,cz-ii-prague,posledni_investice,ano,,"CasInvent 
         +Pharma, oznámení 26. 6. 2025 sedí. Nástroj: agentův „dolozeno“ 
         +se opírá o výpis ARES CasInvent (konvertibilní zápůjčka 4. 3. 2
         +025, nabídka 48 akcií třídy C, zapsané splacené zvýšení kapitál
         +u 30. 5. 2025); doklad je nepřímý, ale existuje, viz je_investo
         +r (oprava v kroku 9; dřívější poznámka tvrdila, že dolozeno je 
         +chybně).",Petr Šťastný (asistence AI),2026-10-27               
      69  investori.json,cz-ii-prague,nezavislost_zdroju,ano,,Positiv.cz 
          i KHAN-I správně zapsány s původem TZ CasInvent,Petr Šťastný (a
          sistence AI),2026-10-27
      70  investori.json,cz-ii-prague,sektory,ano,,"Web: drug development
          , diagnostics, medical technologies, life sciences",Petr Šťastn
          ý (asistence AI),2026-10-27
      71  investori.json,cz-ii-prague,ticket,,,nevyplneno – pouze úplnost
          ,Petr Šťastný (asistence AI),2026-10-27
⏺ Hodnocení je opravené. Teď upravím mereni.py: oprava v kroku 9 se vykáže
  zvlášť a nebude se míchat se změnami po nálezech AI.

⏺ Bash(python3 - <<'E'
      p='scripts/mereni.py'; t=open(p,encoding='utf-8').read()…)
  ⎿  Updated data/mereni_vzorku.md (+24 -15)
      14  
      15  Pole: existence, investicni_cinnost, je_investor, typ, rozsah_p
          ilotu. Aspoň jedno `ne` → chybně zařazen; jinak aspoň jedno `ne
          lze_overit` → neověřeno; jinak správně.
      16  
      17 -- správně 15, chybně 2, neověřeno 3                            
      17 +- správně 16, chybně 2, neověřeno 2                            
      18  
      19  | firma | stav | pole `ne` (skupina) | pole `nelze_overit` |
      20  |---|---|---|---|
      21  | cz-ii-biotech-investments | chybne | rozsah_pilotu (upresneni
          _metodiky) | – |
      22 -| cz-ii-prague | neovereno | – | je_investor |                 
      22  | cz-n1-ventures | chybne | rozsah_pilotu (upresneni_metodiky) 
          | existence |
      23  | cz-presto-ventures | neovereno | – | investicni_cinnost, je_i
          nvestor |
      24  | cz-tensor-ventures | neovereno | – | rozsah_pilotu |
      25  
      26  a) Všechna `ne`:
      27  
      29 -- přesnost správně/(správně+chybně): 15/17 = 88,2 % (95% CI 65,
         -7 %–96,7 %)                                                    
      30 -- dolní mez správně/20: 15/20 = 75,0 % (95% CI 53,1 %–88,8 %)  
      28 +- přesnost správně/(správně+chybně): 16/18 = 88,9 % (95% CI 67,
         +2 %–96,9 %)                                                    
      29 +- dolní mez správně/20: 16/20 = 80,0 % (95% CI 58,4 %–91,9 %)  
      30  
      31  b) Jen vůči chybám výstupu: firmy, jejichž chybné zařazení je j
          en `upresneni_metodiky` (cz-ii-biotech-investments, cz-n1-ventu
          res), jsou z jmenovatele vynechané, nepočítají se jako správné.
      32  
      34 -- správnost mezi 15 rozhodnutelnými případy po vyloučení 2 změn
         - metodiky: 15/15 = 100,0 % (95% CI 79,6 %–100,0 %); vedle toho 
         -3 neověřené (cz-ii-prague, cz-presto-ventures, cz-tensor-ventur
         -es). Nejde o 100% ověřenou databázi.                           
      35 -- dolní mez, jmenovatel 18: 15/18 = 83,3 % (95% CI 60,8 %–94,2 
         -%)                                                             
      33 +- správnost mezi 16 rozhodnutelnými případy po vyloučení 2 změn
         + metodiky: 16/16 = 100,0 % (95% CI 80,6 %–100,0 %); vedle toho 
         +2 neověřené (cz-presto-ventures, cz-tensor-ventures). Nejde o 1
         +00% ověřenou databázi.                                         
      34 +- dolní mez, jmenovatel 18: 16/18 = 88,9 % (95% CI 67,2 %–96,9 
         +%)                                                             
      35  
      36  ## 2. Správnost vyplněných polí (jednotka = řádek id/pole)
      37  
     ...
      41  |---|---|---|---|---|---|---|---|---|
      42  | existence | 19 | 0 | 0 | 0 | 1 | 0 | 19/19 = 100,0 % (95% CI 
          83,2 %–100,0 %) | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %) |
      43  | investicni_cinnost | 19 | 0 | 0 | 0 | 1 | 0 | 19/19 = 100,0 %
           (95% CI 83,2 %–100,0 %) | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %
          ) |
      45 -| je_investor | 18 | 0 | 0 | 0 | 2 | 0 | 18/18 = 100,0 % (95% C
         -I 82,4 %–100,0 %) | 18/20 = 90,0 % (95% CI 69,9 %–97,2 %) |    
      44 +| je_investor | 19 | 0 | 0 | 0 | 1 | 0 | 19/19 = 100,0 % (95% C
         +I 83,2 %–100,0 %) | 19/20 = 95,0 % (95% CI 76,4 %–99,1 %) |    
      45  | typ | 20 | 0 | 0 | 0 | 0 | 0 | 20/20 = 100,0 % (95% CI 83,9 %
          –100,0 %) | 20/20 = 100,0 % (95% CI 83,9 %–100,0 %) |
      46  | rozsah_pilotu | 17 | 0 | 2 | 0 | 1 | 0 | 17/19 = 89,5 % (95% 
          CI 68,6 %–97,1 %) | 17/20 = 85,0 % (95% CI 64,0 %–94,8 %) |
      47  | posledni_investice | 15 | 4 | 0 | 0 | 1 | 0 | 15/19 = 78,9 % 
          (95% CI 56,7 %–91,5 %) | 15/20 = 75,0 % (95% CI 53,1 %–88,8 %) 
          |
     ...
      49  | sektory | 16 | 0 | 0 | 0 | 0 | 4 | 16/16 = 100,0 % (95% CI 80
          ,6 %–100,0 %) | 16/16 = 100,0 % (95% CI 80,6 %–100,0 %) |
      50  | ticket | 10 | 0 | 0 | 1 | 0 | 9 | 10/11 = 90,9 % (95% CI 62,3
           %–98,4 %) | 10/11 = 90,9 % (95% CI 62,3 %–98,4 %) |
     … 64 more lines (ctrl+o to expand)
  ⎿  Updated scripts/mereni.py (+36 -3)
      2  
      3  Čte data/hodnoceni.csv, data/vzorek_kontroly.csv, ai-log/02-oboh
         aceni/mapovani_id.csv,
      4  ai-log/04-kontrola-zdroju/slepa_kontrola.csv
      5 -a ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv, nic z n
        -ich nemění.                                                     
      5 +ai-log/05-rucni-kontrola/hodnoceni_pred_nalezy_ai.csv           
      6 +a ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv, nic z n
        +ich nemění.                                                     
      7  Bez síťových přístupů, deterministický. Výstup: data/mereni_vzor
         ku.md a souhrn na stdout.
      8  Výsledky se nikdy nesčítají do jednoho čísla.
      9  
     ...
      21  MAPOVANI = koren / "ai-log" / "02-obohaceni" / "mapovani_id.csv
          "
      22  SLEPA = koren / "ai-log" / "04-kontrola-zdroju" / "slepa_kontro
          la.csv"
      23  PRED_AI = koren / "ai-log" / "05-rucni-kontrola" / "hodnoceni_p
          red_nalezy_ai.csv"
      24 +PRED_OPRAVOU = koren / "ai-log" / "09-readme" / "hodnoceni_pred
         +_opravou_ii_prague.csv"                                        
      25  VYSTUP = koren / "data" / "mereni_vzorku.md"
      26  
      27  Z = 1.959964  # 95 %
     ...
      35  POTVRZENE_CHYBENI = "Potvrzené chybění"
      36  ZMENA_PO_AI = "Změna po přečtení nálezů AI"
      37  
      38 +# Opravy hodnocení po uložení stavu po nálezech AI (krok 9), id
         +/pole → popis. Jiný rozdíl                                     
      39 +# proti PRED_OPRAVOU skript odmítne.                           
      40 +OPRAVY_KROK_9 = {                                              
      41 +    ("cz-ii-prague", "je_investor"): "výpis ARES CasInvent: kon
         +vertibilní zápůjčka 4. 3. 2025, nabídka 48 akcií třídy C (VH 22
         +. 5. 2025), zapsané splacené zvýšení kapitálu 30. 5. 2025",    
      42 +}                                                              
      43 +                                                               
      44  # Skupina každého konečného „ne“ podle id/pole (PLAN.md bod 7, 
          Druhy „ne“).
      45  # Řádek „ne“, který tu chybí, skript odmítne.
      46  SKUPINA_NE = {
     ...
      130  hod = {(r["id"], r["pole"]): r for r in hodnoceni}
      131  assert len(hod) == len(hodnoceni), "duplicitní id/pole v hodno
           ceni.csv"
      132  pred_ai = {(r["id"], r["pole"]): r for r in nacti_csv(PRED_AI)
           }
      133 +pred_opravou = {(r["id"], r["pole"]): r for r in nacti_csv(PRE
          +D_OPRAVOU)}                                                   
      134 +opravy_9 = sorted(k for k, r in hod.items() if r["hodnoceni"] 
          +!= pred_opravou[k]["hodnoceni"])                              
      135 +assert opravy_9 == sorted(OPRAVY_KROK_9), f"neočekávané změny 
          +proti stavu před opravou: {opravy_9}"                         
      136  
      137  # Sloučená id (cz-nation1 → cz-n1-ventures) patří k firmě, do 
           které byla sloučena.
      138  vysledne_id = {r["id"]: r["vysledne_id"] for r in nacti_csv(MA
           POVANI)}
     ...
      492  for k in ne_po + ano_nl:
      493      assert ZMENA_PO_AI in radky[k]["poznamka"], f"změna bez po
           známky: {k}"
      494  jine = [k for k, r in radky.items() if r["hodnoceni"] != pred_
           ai[k]["hodnoceni"]
     … 40 more lines (ctrl+o to expand)

⏺ Měření sedí s očekáváním: 16/2/2 a 157/7/11/25. Kontroluji ještě v
  mereni_vzorku.md řádek je_investor a historické oddíly.

  Searched for 1 pattern (ctrl+o to expand)

⏺ Teď oprav.py: i&i Prague zůstává zařazená a dostane výhradu, že doklad
  nástroje je nepřímý.

⏺ Bash(python3 - <<'E'
      import re…)
  ⎿  Updated scripts/oprav.py (+16 -29)
      119              ]),
      120          },
      121      },
      122 -    "cz-ii-prague": {                                         
      123 -        "soubor": "nevyresene.csv",                           
      124 -        "hodnoceni": [("je_investor", "nelze_overit"), ("inves
          -ticni_cinnost", "ano"), ("typ", "ano"),                       
      125 -                      ("rozsah_pilotu", "ano"), ("posledni_inv
          -estice", "ano")],                                             
      126 -        "novy_stav": "nevyresene.csv, otazka nastroj",        
      127 -        "popis": "nástroj u jediné investice v okně nedoložen 
          -(PLAN.md bod 3, Nevyřešená rozhodnutí)",                      
      128 -        "radek": {                                            
      129 -            "otazka": "nastroj",                              
      130 -            "moznosti": SEP.join(["zarazen", "neni_investor"])
          -,                                                             
      131 -            "duvod": (                                        
      132 -                "Ruční kontrola (krok 8; hodnoceni.csv {r:je_i
          -nvestor}, je_investor = nelze_overit): jediná "               
      133 -                "zapsaná investice v okně (CasInvent Pharma, o
          -známení 26. 6. 2025, TZ CasInvent přes Positiv.cz "           
      134 -                "a KHAN-I) neuvádí nástroj ani označení kola. 
          -Doklad z rejstříku, o který agent opřel "                     
      135 -                "nastroj = dolozeno, ukazuje i&i Prague jako j
          -ediného akcionáře CasInvent jen 18. 11.–15. 12. 2020 "        
      136 -                "(založení), ne tuto investici ({r:posledni_in
          -vestice}). Podmínka 3 tedy doložená není a podle "            
      137 -                "PLAN.md (bod 3, Nevyřešená rozhodnutí) jde ka
          -ndidát k ručnímu rozhodnutí. Chybějící důkaz "                
      138 -                "o nástroji neznamená, že i&i Prague není inve
          -stor: investice je doložená ({r:investicni_cinnost}), "       
      139 -                "typ VC a sídlo v ČR sedí ({r:typ}, {r:rozsah_
          -pilotu}). Rozhodne zdroj, který uvede nástroj účasti "        
      140 -                "i&i Prague v kole 2025: podíl nebo konvertibi
          -lní nástroj → zarazen, výhradně dluh → neni_investor. "       
      141 -                "Původní úplný záznam: " + PUVODNI + ", id cz-
          -ii-prague."),                                                 
      142 -            "zdroj_url": SEP.join([                           
      143 -                "https://positiv.cz/business/casinvent-pharma-
          -ziskava-silnou-investicni-podporu-pro-vyvoj-cilene-lecby-nador
          -u/",                                                          
      144 -                "https://khanu.de/2025/07/02/casinvent-pharma-
          -secures-next-investment-round-with-strong-support-from-existin
          -g-and-local-investors-to-advance-ck1-inhibitor-development-for
          --treatment-resistant-cancer-patients/",                       
      145 -                "https://ares.gov.cz/ekonomicke-subjekty-v-be/
          -rest/ekonomicke-subjekty-vr/09684221",                        
      146 -            ]),                                               
      147 -        },                                                    
      148 -    },                                                        
      122      "cz-presto-ventures": {
      123          "soubor": "nevyresene.csv",
      124          "hodnoceni": [("investicni_cinnost", "nelze_overit"), 
           ("je_investor", "nelze_overit"),
     ...
      341          ("poslední investice: citovaný zdroj Lupa.cz nedostupn
           ý, firma a datum potvrzeny náhradním zdrojem "
      342           "CzechCrunch", ("posledni_investice", "ano")),
      343      ],
      344 +    "cz-ii-prague": [                                         
      345 +        ("nástroj: oprava hodnocení v kroku 9 (původně je_inve
          +stor = nelze_overit a přesun do nevyresene.csv); "            
      346 +         "výpis ARES CasInvent uvádí konvertibilní zápůjčku i&
          +i Prague z 4. 3. 2025, nabídku 48 akcií třídy C "             
      347 +         "(VH 22. 5. 2025) a zapsané splacené zvýšení kapitálu
          + 30. 5. 2025; upsání akcií i&i Prague je doloženo "           
     … 23 more lines (ctrl+o to expand)

⏺ Bash(sed -i '' 's/# Přehled změn opravené verze (krok 8)"/# Přehled změn
      opravené verze (krok 8, oprava hodnocení i\&i Prague v kroku 9)"/; s/ve
      které je u pěti přes…)
  ⎿  Updated data/opraveno/ZMENY.md (+9 -8)
      1 -# Přehled změn opravené verze (krok 8)                          
      1 +# Přehled změn opravené verze (krok 8, oprava hodnocení i&i Prag
        +ue v kroku 9)                                                   
      2  
      3  Vygenerováno skriptem `scripts/oprav.py` z `data/vystup_agenta/`
          a `data/hodnoceni.csv`. Nepřepisovat ručně. Původní výstup agen
         ta, hodnocení i měření zůstávají beze změny.
      4  
     ...
       8  
       9  | soubor | původně | opraveno | změna |
      10  |---|---|---|---|
      11 -| investori.json | 27 | 22 | -5 |                              
      11 +| investori.json | 27 | 23 | -4 |                              
      12  | vyrazeni.csv | 17 | 19 | +2 |
      13  | hranicni.csv | 1 | 1 | +0 |
      14 -| nevyresene.csv | 11 | 14 | +3 |                              
      14 +| nevyresene.csv | 11 | 13 | +2 |                              
      15  | **celkem výsledných id** | 56 | 56 | |
      16  
      17  Stav kontroly zařazených (`stav_kontroly.csv`, sloupec `vyslede
          k`):
      18  
      19  - `s_opravou`: 4
      20 -- `hodnocena_pole_ano`: 9                                      
      20 +- `hodnocena_pole_ano`: 10                                     
      21  - `s_vyhradou_nelze_overit`: 2
      22  - `nehodnoceno`: 7
      23  
     ...
      37  | cz-n1-ventures | investori.json, zařazen | vyrazeni.csv, mimo
          _rozsah_pilotu | sídlo správce mimo ČR (GP v Lucembursku); skut
          ečný investor, ne neinvestor | ř. 6 (cz-n1-ventures, rozsah_pil
          otu); dále ř. 3, ř. 4, ř. 2, ř. 10 | https://n1.rocks/disclosur
          e<br>https://www.thevccorner.com/p/novoflow-ai-healthcare-start
          up<br>https://n1.rocks/ |
      38  | cz-ii-biotech-investments | investori.json, zařazen | vyrazen
          i.csv, mimo_rozsah_pilotu | fond se sídlem v Lucembursku, česká
           s.r.o. je poradce a tým; skutečný investor, ne neinvestor | ř.
           37 (cz-ii-biotech-investments, rozsah_pilotu); dále ř. 34, ř. 
          35, ř. 41, ř. 39 | https://www.inibio.eu/<br>https://www.lupa.c
          z/aktuality/ai-agenti-noveho-ceskeho-startupu-maji-desitky-mili
          onu-aby-urychlily-vedecky-vyzkum-a-vyvoj/ |
      39  | cz-tensor-ventures | investori.json, zařazen | nevyresene.csv
          , otazka sidlo | sídlo správce neověřené, pravidla pilotu vyžad
          ují správce v ČR | ř. 17 (cz-tensor-ventures, rozsah_pilotu); d
          ále ř. 13, ř. 14, ř. 15, ř. 19 | https://tensor.ventures/<br>ht
          tps://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subj
          ekty-vr/06257241 |
      40 -| cz-ii-prague | investori.json, zařazen | nevyresene.csv, otaz
         -ka nastroj | nástroj u jediné investice v okně nedoložen (PLAN.
         -md bod 3, Nevyřešená rozhodnutí) | ř. 65 (cz-ii-prague, je_inve
         -stor); dále ř. 64, ř. 66, ř. 67, ř. 68 | https://positiv.cz/bus
         -iness/casinvent-pharma-ziskava-silnou-investicni-podporu-pro-vy
         -voj-cilene-lecby-nadoru/<br>https://khanu.de/2025/07/02/casinve
         -nt-pharma-secures-next-investment-round-with-strong-support-fro
         -m-existing-and-local-investors-to-advance-ck1-inhibitor-develop
         -ment-for-treatment-resistant-cancer-patients/<br>https://ares.g
         -ov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty-vr/0968
         -4221 |                                                         
      40  | cz-presto-ventures | investori.json, zařazen | nevyresene.csv
          , otazka investice | přiřazení investic v okně k Prestu nedolož
          ené (ne vyvrácené) | ř. 293 (cz-presto-ventures, investicni_cin
          nost); dále ř. 294, ř. 297, ř. 292, ř. 296 | https://pulse2.com
          /satvu-raises-30-million-in-nato-innovation-fund-backed-round-t
          o-scale-multi-satellite-constellation/amp/<br>https://csg.com/e
          n/news/pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-stre
          ngthening-space-and-thermal-intelligence-capabilities<br>https:
          //techhorizons.eu/<br>https://www.prestoventures.com/ |
      41  
      43 -U i&i Prague a Presta chybí důkaz (nástroj, resp. přiřazení inv
         -estice). Chybějící důkaz neznamená, že subjekt není investor; o
         -ba čekají na ruční rozhodnutí v `nevyresene.csv`.              
      42 +U Presta chybí důkaz o přiřazení investice. Chybějící důkaz nez
         +namená, že subjekt není investor; čeká na ruční rozhodnutí v `n
         +evyresene.csv`.                                                
      43 +                                                               
      44 +i&i Prague zůstává zařazená (oprava hodnocení v kroku 9, hodnoc
         +eni.csv ř. 65): uložený výpis ARES CasInvent (`ai-log/02-obohac
         +eni/zdroje/ares_vr_09684221.json`) uvádí konvertibilní zápůjčku
         + z 4. 3. 2025, nabídku 48 akcií třídy C i&i Prague (valná hroma
         +da 22. 5. 2025) a zapsané splacené zvýšení kapitálu k 30. 5. 20
         +25. Upsání je doloženo nepřímo, smlouva o úpisu přímo ověřena n
         +ení. Původní stav (je_investor = nelze_overit, přesun do `nevyr
         +esene.csv` s otázkou `nastroj`) je v `ai-log/09-readme/hodnocen
         +i_pred_opravou_ii_prague.csv` a v historii gitu (commit 0641e6a
         +).                                                             
      45  
      46  ## Opravy poslední investice
      47  
     ...
      101  |---|---|---|---|
      102  | cz-credo-ventures | investori.json | – | rozsah pilotu: role
            Credo Ventures Management II a.s. jako správce nového fondu n
           eověřena [ř. 226, rozsah_pilotu] |
      103  | cz-ii-biotech-investments | vyrazeni.csv | nezavislost_zdroj
           u | fond se sídlem v Lucembursku, česká s.r.o. je poradce a tý
           m; skutečný investor, ne neinvestor (podrobně sloupec duvod v 
           vyrazeni.csv); nezávislost zdrojů neověřena: zprávy vedené s p
           uvod null mohou mít společný podklad, společný původ ani nezáv
           islost nejsou doložené; puvod ani jistota se nemění [ř. 39, ne
           zavislost_zdroju] |
     … 13 more lines (ctrl+o to expand)
  ⎿  Updated data/opraveno/investori.json (+114 -0)
      764      },
      765      "poznamka": "Typ VC: web 'Fazole Ventures jsme založili pr
           oto, abychom pomohli chytrým lidem uspět... Podporujeme je v p
           očáteční fázi růstu jejich firem tím, že poskytujeme financová
           ní', tým managing partner Pavel Přikryl a zakládající partneři
            Pavel Bouška a Luboš Černý; Forbes 12. 8. 2019 (https://forbe
           s.cz/novy-startupovy-fond-na-scene-vetsinu-penez-poskytne-mili
           ardar-bouska/) jej uvádí jako nový fond na 'české venture kapi
           tálové scéně' ('Nový vehikl... se zaměřuje na rané investice d
           o technologických startupů z oblasti B2B'; Přikryl: 'rodinnějš
           í povahou našeho fondu', 'Naší ambicí je vytvořit jakýsi ventu
           re kapitálový klub'). Většinu peněz podle Forbes přislíbil P. 
           Bouška, který své další investice spravuje přes vlastní family
            office Fermia; Fazole je samostatná investiční firma tří part
           nerů s menšinovými podíly ve startupech, ne holding jednoho po
           dnikatele ani family office. Identita: ARES Fazole Ventures s.
           r.o., IČO 07491492, sídlo Salvátorská 931/8, Praha 1 (shodné s
            adresou 'c/o Opero, Salvátorská 931/8' na webu), jednatelé Lu
           boš Černý a Pavel Přikryl = partneři podle webu; společníci Lu
           boš Černý 15 %, GROWTHGARAGE s.r.o. 25 % (poradenská firma, kt
           erou podle webu vede Přikryl), PABCO s.r.o. 60 % (vazba na P. 
           Bouška nepotvrzená). Předmět podnikání v ARES je jen 'pronájem
            nemovitostí, bytů a nebytových prostor' (obecný zápis). Ticke
           t: web 'Náš \"sweet spot\" se pohybuje mezi 1-20 mil. CZK, ale
            zvážíme i větší objemy financování'. Kapitál: Forbes 2019 'Pa
           lebnou sílu přesně stanovenou nemá', proto prázdné. Poslední i
           nvestice: Everbot (Opava), Forbes 16. 9. 2025: 'Do firmy míří 
           desítky milionů korun od skupiny investorů v čele s fondem Faz
           ole Ventures' a 'Fond Fazole Ventures získá v Everbotu výměnou
            za kapitál 12,2procentní podíl s možností navýšení až o 2,7 p
           rocentního bodu. Přesná výše investice v řádu desítek milionů 
           korun nebyla zveřejněna.' CzechCrunch týž den: 'Lídrem investi
           čního kola se stal fond Fazole Ventures', 'Everbot je nyní v p
           ořadí desátou in … [+744 chars]
      766    },
      767 +  {                                                           
      768 +    "id": "cz-ii-prague",                                     
      769 +    "nazev": "i&i Prague",                                    
      770 +    "typ": "VC",                                              
      771 +    "zeme": "CZ",                                             
      772 +    "pravni_subjekt": {                                       
      773 +      "hodnota": "i&i Prague, s.r.o.",                        
      774 +      "ico": "06058485",                                      
      775 +      "zdroje": [                                             
      776 +        {                                                     
      777 +          "url": "https://ares.gov.cz/ekonomicke-subjekty-v-be
          +/rest/ekonomicke-subjekty-vr/06058485",                       
      778 +          "druh_zdroje": "rejstrik",                          
      779 +          "vydavatel": "ARES (výpis z veřejného rejstříku)",  
      780 +          "puvod": null,                                      
      781 +          "zdroj_datum": "2026-10-25",                        
      782 +          "stazeno": "2026-10-26"                             
      783 +        },                                                    
      784 +        {                                                     
      785 +          "url": "https://www.iniprague.com/",                
      786 +          "druh_zdroje": "web_subjektu",                      
      787 +          "vydavatel": "web investora",                       
      788 +          "puvod": null,                                      
      789 +          "zdroj_datum": null,                                
      790 +          "stazeno": "2026-10-26"                             
      791 +        },                                                    
      792 +        {                                                     
      793 +          "url": "https://uochb.cz/en/ini-prague",            
      794 +          "druh_zdroje": "web_subjektu",                      
      795 +          "vydavatel": "ÚOCHB (mateřská instituce)",          
      796 +          "puvod": null,                                      
      797 +          "zdroj_datum": null,                                
      798 +          "stazeno": "2026-10-26"                             
      799 +        }                                                     
      800 +      ]                                                       
      801 +    },                                                        
      802 +    "web": {                                                  
      803 +      "hodnota": "https://www.iniprague.com/",                
     … 80 more lines (ctrl+o to expand)
  ⎿  Updated data/opraveno/nevyresene.csv (+0 -1)
      11  cz-rockawayx,RockawayX,https://rockawayx.com/,typ,zarazen | mim
          o_rozsah_pilotu,"Investice doložena: RockawayX spoluvedla Serie
          s A 5 mil. USD (velikost kola) do OnRe, Cointelegraph 5. 5. 202
          6 'they co-led OnRe's $5 million Series A round' (nástroj nepri
          ma_indicie, series A); existence: Blockad s.r.o., IČO 08006458 
          (provozovatel webu podle patičky, jednatel Viktor Fischer, spol
          ečník RockawayX a.s. IČO 17457009), sídlo Generála Píky 430/26,
           Praha 6. Typ ale nejednoznačný: sama se popisuje jako 'multi-s
          trategy digital asset investment firm' a 'global digital asset 
          investment firm' (AUM 1,5–2 mld. USD podle téže stránky), Czech
          Crunch 27. 8. 2026 uvádí strategie 'venture fondy, tržně neutrá
          lní fond, takzvané vaulty přímo na blockchainu a nyní hedgeový 
          fond' a web člení činnost na Investments, Liquidity a Infrastru
          cture (validátory). Oba venture fondy (RockawayX VC I z r. 2021
          , VC II) jsou na webu 'Closed'; aktivní jsou hedge fond Liquid 
          Opportunities (Kajmanské ostrovy, CIMA) a Market Neutral Fund (
          Lichtenštejnsko, 'provides capital to digital asset protocols a
          nd companies'). Není tedy jasné, zda jde o VC, nebo o multistra
          tegického správce kryptoaktiv, pro kterého typ v PLAN.md chybí.
           Nejisté je i sídlo: kanceláře Praha, Londýn, New York, Dubaj, 
          české entity jsou v Praze, fondy v zahraničí. Rozhodlo by: z ja
          kého vehiklu a v jaké podobě (equity vs. token vs. úvěr) šla in
          vestice do OnRe, zda RockawayX otevírá nový VC fond, a kde sídl
          í správce fondů.",https://cointelegraph.com/news/forward-indust
          ries-rockawayx-onre-solana-reinsurance | https://www.rockawayx.
          com/insights/rockawayx-and-forward-industries-co-lead-strategic
          -investment-in-onre | https://rockawayx.com/funds | https://roc
          kawayx.com/ | https://cc.cz/cesi-krypto-a-40-miliard-pro-invest
          ice-nic-takoveho-zatim-jeste-nikdo-nepostavil-rika-sef-rockaway
          x/ | https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomic
          ke-subjekty-vr/08006458,2026-10-26
      12  cz-tarpan-capital,Tarpan Capital,https://www.tarpangroup.net/ta
          rpan-partners,typ,zarazen | mimo_rozsah_pilotu,"Investice dolož
          ena: Filuta AI, seed 4,2 mil. USD (velikost celého kola, ne vkl
          ad), oznámeno 2025-06-24 (Rockaway Ventures: „The round also in
          cluded participation from LionBeat Capital, TARPAN Partners…“; 
          CzechStartups.gov.cz/Startup Kitchen podle Czech P.R.: Ladislav
           Šelepa „of Tarpan Partners, which was the manager of the inves
          tment round and invested in FILUTA AI itself“) – nástroj neprim
          a_indicie (seed), status by byl investice_dolozena_12_24_mesicu
          . Typ si odporuje: vlastní web TARPAN Partners se popisuje jako
           „nezávislá poradenská společnost zaměřená na ekonomické a fina
          nční poradenství“ (M&A, kapitálové poradenství, investice formo
          u „společné investování se svými klienty“), reference jsou jen 
          poradenské mandáty a v kole Filuta byla zároveň manažerem kola;
           naproti tomu agregátor Caplight uvádí „TARPAN.VC is a venture 
          capital fund based in Prague“ (založeno 2018, jediné portfolio 
          Filuta AI). Nejasný je i investující subjekt: TARPAN Partners s
          .r.o. (IČO 24733792) nebo TARPAN Capital s.r.o. (IČO 09228497, 
          předmět „Správa vlastního majetku“, společník TARPAN Group v.o.
          s.), oba se sídlem Václavské nám. 773/4, Praha 1. Pokud jde o V
          C (samostatný fond/značka TARPAN.VC se sídlem v ČR) → zarazen; 
          pokud poradenská firma spoluinvestující z vlastní společnosti (
          korporátní investor bez samostatné jednotky) → mimo_rozsah_pilo
          tu. Rozhodlo by: vlastní popis TARPAN.VC/TARPAN Capital (web, r
          ozhovor), doklad, který subjekt drží podíl ve Filutě (Filuta AI
           CZ s.r.o. má jediného společníka Filuta AI Inc., takže český r
          ejstřík nepomůže), a další doložené vlastní investice.",https:/
          /rockawayventures.com/rockaway-ventures-leads-4-2m-seed-round-i
          n-czech-ai-startup-filuta-ai/ | https://czechstartups.gov.cz/en
          /novinky/investors-believe-in-ai-investment-seed-round-brings-f
          iluta-ai-startup-4-2-million/ | https://www.tarpangroup.net/tar
          pan-partners | https://www.tarpangroup.net/sluz … [+262 chars]
      13  cz-tensor-ventures,Tensor Ventures,https://tensor.ventures/,sid
          lo,zarazen | mimo_rozsah_pilotu,"Ruční kontrola (krok 8; hodnoc
          eni.csv ř. 17 (cz-tensor-ventures, rozsah_pilotu), rozsah_pilot
          u = nelze_overit): web uvádí jako adresu Tensor Ventures GP S.à
           r.l. a Tensor Ventures Fund I SCSp v Lucembursku; česká Tensor
           Ventures a.s. (IČO 06257241, Praha 8) existuje (ř. 13 (cz-tens
          or-ventures, existence)), ale není doloženo, že je správcem fon
          dů, a správce druhého fondu (s EIF) doložen není. Pravidla pilo
          tu vyžadují sídlo investiční firmy (správce) v ČR, neověřené sí
          dlo proto zařazení brání. Investor podle bodů 2 a 3 je doložen 
          (ř. 14 (cz-tensor-ventures, investicni_cinnost), ř. 15 (cz-tens
          or-ventures, je_investor)). Rozhodne doložení správce (GP/AIFM)
           obou fondů: správce v ČR → zarazen, správce v Lucembursku → mi
          mo_rozsah_pilotu (stejně jako N1 a i&i Biotech). Výhrada: nezáv
          islost zdrojů u ValkaAI neověřena (ř. 19 (cz-tensor-ventures, n
          ezavislost_zdroju)). Původní úplný záznam: data/vystup_agenta/i
          nvestori.json, id cz-tensor-ventures.",https://tensor.ventures/
           | https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke
          -subjekty-vr/06257241,2026-10-27
      14 -cz-ii-prague,i&i Prague,https://www.iniprague.com/,nastroj,zara
         -zen | neni_investor,"Ruční kontrola (krok 8; hodnoceni.csv ř. 6
         -5 (cz-ii-prague, je_investor), je_investor = nelze_overit): jed
         -iná zapsaná investice v okně (CasInvent Pharma, oznámení 26. 6.
         - 2025, TZ CasInvent přes Positiv.cz a KHAN-I) neuvádí nástroj a
         -ni označení kola. Doklad z rejstříku, o který agent opřel nastr
         -oj = dolozeno, ukazuje i&i Prague jako jediného akcionáře CasIn
         -vent jen 18. 11.–15. 12. 2020 (založení), ne tuto investici (ř.
         - 68 (cz-ii-prague, posledni_investice)). Podmínka 3 tedy dolože
         -ná není a podle PLAN.md (bod 3, Nevyřešená rozhodnutí) jde kand
         -idát k ručnímu rozhodnutí. Chybějící důkaz o nástroji neznamená
         -, že i&i Prague není investor: investice je doložená (ř. 64 (cz
         --ii-prague, investicni_cinnost)), typ VC a sídlo v ČR sedí (ř. 
         -66 (cz-ii-prague, typ), ř. 67 (cz-ii-prague, rozsah_pilotu)). R
         -ozhodne zdroj, který uvede nástroj účasti i&i Prague v kole 202
         -5: podíl nebo konvertibilní nástroj → zarazen, výhradně dluh → 
         -neni_investor. Původní úplný záznam: data/vystup_agenta/investo
         -ri.json, id cz-ii-prague.",https://positiv.cz/business/casinven
         -t-pharma-ziskava-silnou-investicni-podporu-pro-vyvoj-cilene-lec
         -by-nadoru/ | https://khanu.de/2025/07/02/casinvent-pharma-secur
         -es-next-investment-round-with-strong-support-from-existing-and-
         -local-investors-to-advance-ck1-inhibitor-development-for-treatm
         -ent-resistant-cancer-patients/ | https://ares.gov.cz/ekonomicke
         --subjekty-v-be/rest/ekonomicke-subjekty-vr/09684221,2026-10-27 
      14  cz-presto-ventures,Presto Ventures,https://www.prestoventures.c
          om/,investice,zarazen | mimo_rozsah_pilotu | neni_investor,"Ruč
          ní kontrola (krok 8; hodnoceni.csv ř. 293 (cz-presto-ventures, 
          investicni_cinnost), ř. 294 (cz-presto-ventures, je_investor), 
          ř. 297 (cz-presto-ventures, posledni_investice), vše nelze_over
          it): investice v okně zapsané agentem (SatVu 18. 2. 2026, Occam
           11. 2. 2026) provedl fond (Presto) Tech Horizons – Tech Horizo
          ns SCSp v Lucembursku se správcem Tech Horizons GP S.à r.l. a v
          lastní governance (techhorizons.eu); vazba jeho správy na Prest
          o Ventures ani vztah v době investic nejsou doložené. Cílené ov
          ěření 27. 10. 2026 (Outfindo, Elin.ai) investici Presta v okně 
          nedoložilo. Podmínka 2 tak pro subjekt záznamu (Presto Ventures
           II a.s., Praha 1, ř. 292 (cz-presto-ventures, existence), ř. 2
          96 (cz-presto-ventures, rozsah_pilotu)) doložená není. Přiřazen
          í je nedoložené, ne vyvrácené: chybějící důkaz neznamená, že Pr
          esto Ventures není investor. Rozhodne doklad, kdo investice pro
          vedl a kdo fond spravuje: Presto jako investor se správcem v ČR
           → zarazen; investice jen přes fond se správcem v Lucembursku →
           mimo_rozsah_pilotu; bez jakékoli doložené investice Presta v o
          kně → neni_investor. Původní úplný záznam: data/vystup_agenta/i
          nvestori.json, id cz-presto-ventures.",https://pulse2.com/satvu
          -raises-30-million-in-nato-innovation-fund-backed-round-to-scal
          e-multi-satellite-constellation/amp/ | https://csg.com/en/news/
          pth-vc-fund-backed-by-csg-invests-in-uk-based-satvu-strengtheni
          ng-space-and-thermal-intelligence-capabilities | https://techho
          rizons.eu/ | https://www.prestoventures.com/,2026-10-27
  ⎿  Updated data/opraveno/stav_kontroly.csv (+1 -1)
      19  cz-genesis-capital,vyrazeni.csv,vyrazeni.csv,ne,nekontrolovano,
          nehodnoceno,,,"původní rozhodnutí agenta, ručně nekontrolováno 
          (PLAN.md bod 7)",
      20  cz-gi21-capital,nevyresene.csv,nevyresene.csv,ne,nekontrolovano
          ,nehodnoceno,,,"původní rozhodnutí agenta, ručně nekontrolováno
           (PLAN.md bod 7)",
      21  cz-ii-biotech-investments,vyrazeni.csv,investori.json,ano,hodno
          ceno_s_asistenci_ai,presunuto,nezavislost_zdroju,zarazeni,"fond
           se sídlem v Lucembursku, česká s.r.o. je poradce a tým; skuteč
          ný investor, ne neinvestor (podrobně sloupec duvod v vyrazeni.c
          sv); nezávislost zdrojů neověřena: zprávy vedené s puvod null m
          ohou mít společný podklad, společný původ ani nezávislost nejso
          u doložené; puvod ani jistota se nemění [ř. 39, nezavislost_zdr
          oju]",hodnoceni.csv ř. 33–42
      22 -cz-ii-prague,nevyresene.csv,investori.json,ano,hodnoceno_s_asis
         -tenci_ai,presunuto,je_investor,zarazeni,"nástroj u jediné inves
         -tice v okně nedoložen (PLAN.md bod 3, Nevyřešená rozhodnutí) (p
         -odrobně sloupec duvod v nevyresene.csv)",hodnoceni.csv ř. 63–72
      22 +cz-ii-prague,investori.json,investori.json,ano,hodnoceno_s_asis
         +tenci_ai,hodnocena_pole_ano,,,"nástroj: oprava hodnocení v krok
         +u 9 (původně je_investor = nelze_overit a přesun do nevyresene.
         +csv); výpis ARES CasInvent uvádí konvertibilní zápůjčku i&i Pra
         +gue z 4. 3. 2025, nabídku 48 akcií třídy C (VH 22. 5. 2025) a z
         +apsané splacené zvýšení kapitálu 30. 5. 2025; upsání akcií i&i 
         +Prague je doloženo nepřímo, smlouva o úpisu přímo ověřena není 
         +[ř. 65, je_investor]; Poslední investice je nejnovější doložená
         + nebo nalezená, ne záruka, že novější investice neexistuje.",ho
         +dnoceni.csv ř. 63–72                                           
      23  cz-inven-capital,investori.json,investori.json,ano,hodnoceno_s_
          asistenci_ai,hodnocena_pole_ano,,,"Poslední investice je nejnov
          ější doložená nebo nalezená, ne záruka, že novější investice ne
          existuje.",hodnoceni.csv ř. 212–221
      24  cz-jet-investment,nevyresene.csv,nevyresene.csv,ne,nekontrolova
          no,nehodnoceno,,,"původní rozhodnutí agenta, ručně nekontrolová
          no (PLAN.md bod 7)",
      25  cz-jic-ventures,investori.json,investori.json,ne,nekontrolovano
          ,nehodnoceno,,,"mimo náhodný vzorek 20 z 27 zařazených (seed 20
          261027), údaje ručně nekontrolované; Poslední investice je nejn
          ovější doložená nebo nalezená, ne záruka, že novější investice 
          neexistuje.",
  ⎿  Updated scripts/oprav.py (+2 -2)
      572      for r in zar:
      573          vys[r["vysledek"]] = vys.get(r["vysledek"], 0) + 1
      574      o = []
      575 -    o.append("# Přehled změn opravené verze (krok 8)")        
      575 +    o.append("# Přehled změn opravené verze (krok 8, oprava ho
          +dnocení i&i Prague v kroku 9)")                               
      576      o.append("")
      577      o.append("Vygenerováno skriptem `scripts/oprav.py` z `data
           /vystup_agenta/` a `data/hodnoceni.csv`. "
      578               "Nepřepisovat ručně. Původní výstup agenta, hodno
           cení i měření zůstávají beze změny.")
     ...
      725      o.append("`scripts/zkontroluj_data.py` čte jen `data/vystu
           p_agenta/`. Pro kontrolu opravené verze se spouští "
      726               "nad dočasným kořenem mimo repozitář: kopie `data
           /kandidati.csv`, čtyř výsledkových souborů "
      727               "z `data/opraveno/` jako `data/vystup_agenta/` a 
           kopie `ai-log/02-obohaceni/mapovani_id.csv`, "
      728 -             "ve které je u pěti přesunutých id změněný sloupe
          -c `soubor`. Původní data se nepřesouvají "                    
      728 +             "ve které je u čtyř přesunutých id změněný sloupe
          +c `soubor`. Původní data se nepřesouvají "                    
      729               "ani nepřepisují. Kontrola URL (`--over-url`) se 
           nespouštěla.")
      730      o.append("")
      731      o.append("- `--datum 2026-10-26` (výchozí, den kroku 2): c
           hyby struktury 0, metodický nesoulad 10, "

⏺ Opravená data sedí (23/19/1/13, 56 id). Spouštím validaci opravené verze v
  dočasném kořeni.

⏺ Bash(S=/private/tmp/claude-501/-Users-petrstastny-Documents-Projekty-investori
      -databaze/e91dd674-49a9-425e-8727-f62590611dd3/scratchpad/val && rm -rf $S
      && mkdir -p…)
  ⎿  (No output)

⏺ Validace: 0 chyb struktury. Nesouladů je 9, protože i&i Prague už není
  přesunutá. Upravuji text v oprav.py.

⏺ Bash(python3 - <<'E'
      p='scripts/oprav.py'; t=open(p,encoding='utf-8').read()…)
  ⎿  Updated data/opraveno/ZMENY.md (+1 -1)
      121  
      122  `scripts/zkontroluj_data.py` čte jen `data/vystup_agenta/`. Pr
           o kontrolu opravené verze se spouští nad dočasným kořenem mimo
            repozitář: kopie `data/kandidati.csv`, čtyř výsledkových soub
           orů z `data/opraveno/` jako `data/vystup_agenta/` a kopie `ai-
           log/02-obohaceni/mapovani_id.csv`, ve které je u čtyř přesunut
           ých id změněný sloupec `soubor`. Původní data se nepřesouvají 
           ani nepřepisují. Kontrola URL (`--over-url`) se nespouštěla.
      123  
      124 -- `--datum 2026-10-26` (výchozí, den kroku 2): chyby struktury
          - 0, metodický nesoulad 10, upozornění 8. Devět nálezů „datum n
          -ení v budoucnosti“ má jedinou příčinu: zdroje čtené v kroku 8 
          -mají `stazeno` 2026-10-27, tedy po referenčním datu. Desátý je
          - známý nález u KAYA.                                          
      124 +- `--datum 2026-10-26` (výchozí, den kroku 2): chyby struktury
          + 0, metodický nesoulad 9, upozornění 8. Osm nálezů „datum není
          + v budoucnosti“ má jedinou příčinu: zdroje čtené v kroku 8 maj
          +í `stazeno` 2026-10-27, tedy po referenčním datu. Devátý je zn
          +ámý nález u KAYA. Před opravou i&i Prague v kroku 9 bylo nález
          +ů 10 (navíc `stazeno` přesunutého záznamu i&i Prague).        
      125  - `--datum 2026-10-27` (den ruční kontroly): chyby struktury 0
           , metodický nesoulad 1 (známý nález u cz-kaya-vc: `kapital[2].
           fond` u druhu `committed_capital`, mimo vzorek, bez dokončenéh
           o hodnocení neopraveno), upozornění 8 (stejná jako při 2026-10
           -26). Statusy se posunem referenčního data nemění.
      126  - Upozornění je 8 místo 16 v `ai-log/03-kontrola/automaticka_k
           ontrola.md` ze dvou důvodů: kontrola URL se nespouštěla (5 ned
           ostupných URL v původní zprávě) a upozornění k `cvca.cz` a `pl
           ati_k` u N1 a i&i Biotech zmizela s přesunem jejich záznamů z 
           `investori.json` do `vyrazeni.csv` (3 nálezy).
      127  
  ⎿  Updated scripts/oprav.py (+4 -3)
      728               "ve které je u čtyř přesunutých id změněný sloupe
           c `soubor`. Původní data se nepřesouvají "
      729               "ani nepřepisují. Kontrola URL (`--over-url`) se 
           nespouštěla.")
      730      o.append("")
      731 -    o.append("- `--datum 2026-10-26` (výchozí, den kroku 2): c
          -hyby struktury 0, metodický nesoulad 10, "                    
      732 -             "upozornění 8. Devět nálezů „datum není v budoucn
          -osti“ má jedinou příčinu: zdroje čtené "                      
      733 -             "v kroku 8 mají `stazeno` 2026-10-27, tedy po ref
          -erenčním datu. Desátý je známý nález u KAYA.")                
      731 +    o.append("- `--datum 2026-10-26` (výchozí, den kroku 2): c
          +hyby struktury 0, metodický nesoulad 9, "                     
      732 +             "upozornění 8. Osm nálezů „datum není v budoucnos
          +ti“ má jedinou příčinu: zdroje čtené "                        
      733 +             "v kroku 8 mají `stazeno` 2026-10-27, tedy po ref
          +erenčním datu. Devátý je známý nález u KAYA. "                
      734 +             "Před opravou i&i Prague v kroku 9 bylo nálezů 10
          + (navíc `stazeno` přesunutého záznamu i&i Prague).")          
      735      o.append("- `--datum 2026-10-27` (den ruční kontroly): chy
           by struktury 0, metodický nesoulad 1 (známý nález "
      736               "u cz-kaya-vc: `kapital[2].fond` u druhu `committ
           ed_capital`, mimo vzorek, bez dokončeného hodnocení "
      737               "neopraveno), upozornění 8 (stejná jako při 2026-
           10-26). Statusy se posunem referenčního data "

⏺ Kontroluji, jestli dotčená čísla nejsou v PLAN.md nebo NAKLADY.md.

  Searched for 1 pattern, read 1 file (ctrl+o to expand)

⏺ Update(NAKLADY.md)
  ⎿  Added 1 line, removed 1 line
      204  1. **Poslední investice.** Ze všech polí má nejnižší správnost
           : 15/19 = 78,9 % (95% CI 56,7–91,5 %). Všechny 4 chyby výstupu
            mají stejný vzor: agent uvedl doloženou investici, ale přehlé
           dl novější (Look AI, Purple, Reflex, ZAKA). Kontrolor by měl u
            každého záznamu, nebo aspoň u celého kontrolního vzorku, proj
           ít novinky na webu investora a nejnovější zprávy po datu, kter
           é uvedl agent. Totéž pole je předmětem čtvrtletní aktualizace 
           a jejího kontrolního vzorku.
      205  2. **Sídlo a příslušnost u fondů se zahraničním správcem.** Z 
           20 firem byly 2 `ne` (i&i Biotech, N1: GP/AIFM v Lucembursku, 
           tým v Praze) a 1 `nelze_overit` (Tensor). Šlo o upřesnění meto
           diky, ne o chybu agenta. Před škálováním je potřeba pravidlo s
           ídla rozhodnout (správce × fond × tým). Ručně pak zkontrolovat
            záznamy, kde agent najde zahraniční GP/AIFM nebo fondovou str
           ukturu (SCSp, S.à r.l., LP). Mimo ČR bude takových případů víc
           .
      206  3. **Nezávislost zdrojů.** U 6/20 firem ji nešlo ověřit: agent
            měl `puvod` null a zprávy mohly vycházet z jedné tiskové zprá
           vy. Lidská kontrola by měla jít na záznamy, jejichž investice 
           stojí jen na zdrojích s neznámým původem. Systémovější řešení 
           je vyžadovat původ zdroje už ve schématu.
      207 -4. **Přiřazení investice přes fondy** (Presto: investice prove
          -dl lucemburský fond jiného správce) a **nástroj investice** (i
          -&i Prague): `je_investor` a `investicni_cinnost` nešlo ověřit 
          -u 2 a 1 z 20 firem.                                           
      207 +4. **Přiřazení investice přes fondy** (Presto: investice prove
          +dl lucemburský fond jiného správce) a **nástroj investice** (i
          +&i Prague: nástroj doložil až výpis z rejstříku portfoliové fi
          +rmy, nepřímo): `je_investor` a `investicni_cinnost` nešlo ověř
          +it u 1 a 1 z 20 firem (před opravou hodnocení i&i Prague v kro
          +ku 9 u 2 a 1).                                                
      208  5. **Nevyřešení a hraniční kandidáti** (21 % kandidátů) vyžadu
           jí rozhodnutí člověka vždy. V pilotu je zatím nikdo ručně neko
           ntroloval.
      209  
      210  **Omezení:** Netvrdím, kde by lidskou kontrolu mohl nahradit k
           ontrolní agent. Konečné hodnocení vznikalo s asistencí AI a zč
           ásti podle nálezů kontrolního agenta: 3 ze 4 chyb výstupu se n
           ašly až po přečtení jeho nálezů a 6 verdiktů se po nich změnil
           o z `ano` na `nelze_overit` (mereni_vzorku.md, 5.4). Kontrolní
            agent proto nebyl měřen proti nezávislému standardu a měření 
           nahraditelnost lidské kontroly nedokládá. Ruční kontrola navíc
            pokryla jen zařazené. Recall (kolik investorů agent chybně vy
           řadil) změřený není a kontrola vyřazených by k hodinám výše je
           ště přibyla.

⏺ Bash(grep -n "hodnoceni\|mereni_vzorku\|i&i\|156\|nelze" scripts/naklady.py |
      head; python3 scripts/naklady.py >/dev/null && git status --short)
  ⎿  (No output)

⏺ Skripty a data jsou hotové. Upravuji README podle nových výsledků.

  Searched for 1 pattern, read 1 file (ctrl+o to expand)

⏺ Bash(python3 - <<'E'
      p='README.md'; t=open(p,encoding='utf-8').read()…)
  ⎿  Updated README.md (+18 -15)
      10  
      11  | | původní výstup agenta | opravená verze (krok 8) |
      12  |---|---|---|
      13 -| zařazení (VC/CVC se sídlem v ČR) | 27 | **22** |             
      13 +| zařazení (VC/CVC se sídlem v ČR) | 27 | **23** |             
      14  | vyřazení, z toho `mimo_rozsah_pilotu` / `neni_investor` | 17 
          (15 / 2) | **19** (17 / 2) |
      15 -| nevyřešení (k ručnímu rozhodnutí) | 11 | **14** |            
      15 +| nevyřešení (k ručnímu rozhodnutí) | 11 | **13** |            
      16  | hraniční (venture debt) | 1 | **1** |
      17  | celkem | 56 | 56 |
      18  
      19 -- **22 zařazených neznamená 22 plně ověřených.** 7 z nich nebyl
         -o v kontrolním vzorku a ručně je nikdo nekontroloval. U zbylých
         - 15 je stav v [stav_kontroly.csv](data/opraveno/stav_kontroly.c
         -sv): 4 s opravou poslední investice, 2 s polem, které nešlo ově
         -řit, a 9 se všemi hodnocenými poli `ano`. I mezi nimi mají někt
         -eré záznamy výhrady, například Credo, Rockaway nebo StartupYard
         -.                                                              
      19 +- **23 zařazených neznamená 23 plně ověřených.** 7 z nich nebyl
         +o v kontrolním vzorku a ručně je nikdo nekontroloval. U zbylých
         + 16 je stav v [stav_kontroly.csv](data/opraveno/stav_kontroly.c
         +sv): 4 s opravou poslední investice, 2 s polem, které nešlo ově
         +řit, a 10 se všemi hodnocenými poli `ano`. I mezi nimi mají něk
         +teré záznamy výhrady, například Credo, Rockaway, StartupYard ne
         +bo i&i Prague (nástroj doložený nepřímo).                      
      20  - **Mimo pilot není totéž co neinvestor.** `mimo_rozsah_pilotu`
           (17) znamená, že agent subjekt vyhodnotil jako investora jinéh
          o typu (PE, family office…) nebo se sídlem mimo ČR. Ručně to by
          lo potvrzené jen u N1 a i&i Biotech. `neni_investor` (Espira, M
          cWin) znamená jen to, že investice za posledních 24 měsíců není
           veřejně doložená. Kontrolní agent upozornil, že to samo nedoka
          zuje, že nejde o investora ([cilene_otazky.md](ai-log/04-kontro
          la-zdroju/cilene_otazky.md), oddíl „Espira a McWin“).
      21 -- Pět přesunů z opravené verze: N1 a i&i Biotech jsem přesunul 
         -mimo pilot (správce fondu je v Lucembursku). Tensor (sídlo sprá
         -vce), i&i Prague (nástroj investice) a Presto (přiřazení invest
         -ic) jsem přesunul mezi nevyřešené. U i&i Prague a Presta chybí 
         -důkaz, ale nic nedokládá, že nejde o investory.                
      21 +- Čtyři přesuny z opravené verze: N1 a i&i Biotech jsem přesunu
         +l mimo pilot (správce fondu je v Lucembursku). Tensor (sídlo sp
         +rávce) a Presto (přiřazení investic) jsem přesunul mezi nevyřeš
         +ené. U Presta chybí důkaz, ale nic nedokládá, že nejde o invest
         +ora. i&i Prague byla v kroku 8 také přesunutá mezi nevyřešené. 
         +V kroku 9 jsem hodnocení opravil podle již uloženého výpisu z r
         +ejstříku a vrátil ji mezi zařazené (viz [Chyby a opravy](#chyby
         +-a-opravy)). Původní stav byl 22 zařazených a 14 nevyřešených. 
      22  
      23  Odkazy:
      24  
     ...
       88  
       89  | | výsledek |
       90  |---|---|
       91 -| správně / chybně / neověřeno | 15 / 2 / 3 |                 
       92 -| přesnost na ověřitelných | 15/17 = **88,2 %** (65,7–96,7 %) 
          -|                                                             
       93 -| konzervativně, neověřené jako chyba | 15/20 = **75,0 %** (53
          -,1–88,8 %) |                                                  
       91 +| správně / chybně / neověřeno | 16 / 2 / 2 |                 
       92 +| přesnost na ověřitelných | 16/18 = **88,9 %** (67,2–96,9 %) 
          +|                                                             
       93 +| konzervativně, neověřené jako chyba | 16/20 = **80,0 %** (58
          +,4–91,9 %) |                                                  
       94  
       95 -Obě chybná zařazení (N1, i&i Biotech) jsou **změny výkladu met
          -odiky**, ne chyby agenta. Agent použil sídlo značky a týmu, já
          - jsem při ruční kontrole rozhodl podle sídla správce. Bez nich
          - je dolní mez 15/18 = 83,3 % (60,8–94,2 %). Neověřené jsou Ten
          -sor (sídlo správce), i&i Prague (nástroj) a Presto (přiřazení 
          -investic).                                                    
       95 +Obě chybná zařazení (N1, i&i Biotech) jsou **změny výkladu met
          +odiky**, ne chyby agenta. Agent použil sídlo značky a týmu, já
          + jsem při ruční kontrole rozhodl podle sídla správce. Bez nich
          + je dolní mez 16/18 = 88,9 % (67,2–96,9 %). Neověřené jsou Ten
          +sor (sídlo správce) a Presto (přiřazení investic). Původní sta
          +v před opravou hodnocení i&i Prague v kroku 9: 15 / 2 / 3, ted
          +y 15/17 = 88,2 % a 15/20 = 75,0 %.                            
       96  
       97  **Správnost vyplněných polí** (jednotka = pole firmy, 20 firem
            × 10 polí):
       98  
       99  | pole | přesnost ano/(ano+ne) | dolní mez s `nelze_overit` |
      100  |---|---|---|
      101 -| **celkem** | 156/163 = **95,7 %** (91,4–97,9 %) | 156/175 = 
          -89,1 % (83,7–92,9 %) |                                        
      101 +| **celkem** | 157/164 = **95,7 %** (91,5–97,9 %) | 157/175 = 
          +89,7 % (84,3–93,4 %) |                                        
      102  | posledni_investice (nejslabší) | 15/19 = 78,9 % (56,7–91,5 %
           ) | 15/20 = 75,0 % (53,1–88,8 %) |
      103 +| je_investor | 19/19 = 100 % (83,2–100 %) | 19/20 = 95,0 % (7
          +6,4–99,1 %) |                                                 
     … 51 more lines (ctrl+o to expand)

⏺ Bash(python3 -c "
      import csv…)
  ⎿  (No output)

⏺ Všechny kontroly prošly. Commituji dvěma commity a pushuji.

⏺ Bash(git add data/hodnoceni.csv
      ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv scripts/mereni.py
      scripts/oprav.py data/mereni_vzorku.md data/opraveno NAKLADY.…)
  ⎿  (No output)

⏺ Oprava hodnocení i&i Prague je hotová, výsledky sedí s tvými očekáváními a oba
  commity jsou pushnuté. Pracovní strom je čistý.

  Výsledky

  Měření vzorku:
  - Zařazení: 16 správně, 2 chybně (N1 a i&i Biotech, změna výkladu metodiky), 2
    neověřené (Tensor, Presto). Přesnost na ověřitelných 16/18 = 88,9 %
    (67,2–96,9 %), konzervativně 16/20 = 80,0 % (58,4–91,9 %).
  - Pole: 157 ano, 7 ne, 11 nelze_overit, 25 jen úplnost. Přesnost 157/164 =
    95,7 % (91,5–97,9 %), dolní mez 157/175 = 89,7 %.
  - je_investor: 19 ano, 1 nelze_overit.

  Opravená data: 23 zařazených, 19 vyřazených, 13 nevyřešených, 1 hraniční.
  Všech 56 id je tam právě jednou.

  Co se změnilo

  - Záloha: současné hodnocení jsem před změnou uložil do
    ai-log/09-readme/hodnoceni_pred_opravou_ii_prague.csv. Zálohu před nálezy AI
    jsem neměnil.
  - Hodnocení (ř. 65 a 68): je_investor je teď ano. Poznámka cituje konkrétní
    části výpisu a výslovně uvádí, že smlouva o úpisu přímo ověřená není. U
    posledni_investice zůstal verdikt, poznámka teď říká, že doklad nástroje je
    nepřímý, ale existuje.
  - mereni.py: oprava se vykazuje v novém oddílu 5.5. Ve srovnání před a po
    nálezech AI zůstal zachovaný původní stav s označením. U kontrolního agenta
    se jeho souhlas u nástroje i&i Prague teď započítává jako potvrzený.
  - oprav.py: i&i Prague už se nepřesouvá mezi nevyřešené a v stav_kontroly.csv
    má výhradu o nepřímém dokladu. Upravil jsem i ZMENY.md a čísla z validace.
  - README: chybu agenta u i&i Prague nahradil řádek o chybě následné kontroly s
    asistencí AI (ten verdikt navrhl Claude v chatu). Změnila jsem jen celkové
    počty. Údaje, které se nezměnily (třeba 15/20 = 75 % u posledni_investice),
    zůstaly. Původní čísla 15/2/3 a 156/12 jsou uvedená jako původní stav.
  - NAKLADY.md: jedna věta o počtu neověřených polí. Výpočet nákladů pořád
    vychází z původních 27 zařazených, vypocet.md se nezměnil. PLAN.md dotčená
    čísla neobsahuje.

  Kontroly

  - mereni.py i oprav.py dávají při dvou bězích shodný výstup.
  - Validace opravené verze: 0 chyb struktury a 9 metodických nesouladů. Z nich
    8 způsobuje datum stažení po referenčním dni a jeden je známý nález u KAYA.
  - Testy validátoru prošly, odkazy v README fungují (272 řádků).
  - data/vystup_agenta/, exporty a zálohy jsou beze změny.

  Commity

  - a1d62a6 Ruční kontrola: oprava hodnocení i&i Prague podle výpisu CasInvent,
    přepočet měření a opravené verze (10 souborů)
  - 38b4875 Krok 9: README podle skutečného průběhu

  Export této session (krok 9) zatím v ai-log/ není. Když ho budeš chtít přidat,
  README ho v přehledu exportů zatím nezmiňuje.