S=$1
printf '# Rozhodnutí o možných duplicitách (krok 2)\n\nPravidlo: jedna investiční firma (správce, značka) = jeden záznam (PLAN.md bod 3). Mapování všech 57 vstupních id na výsledné id je v `mapovani_id.csv`.\n\n'
for f in $S/vysledky/par_*.md; do sed -e 's/^### /#### /' -e 's/^## /### /' -e 's/^# /## /' $f; echo; done
