# Plattformen
- Windows, macOS, Ubuntu/Linux
- Python 3.12, Python 3.13, Python 3.14
    fuer Review/Revision
        Ubuntu + Python 3.12
        Ubuntu + Python 3.13
        Ubuntu + Python 3.14
        Windows + Python 3.13
        macOS + Python 3.13
- keine absolute Pfade
- ruff in CI

# Nur erlaubte Libaries verwenden
Erlaubte Libaries:  csv, datetime, collections, os, pytest, ruff
Nicht verwenden:  externe Libaries (bspw. pandas, numpy, etc.)

# Eingabedatei
CSV-Datei im Format: 
    id,name,datum
- id ist eine positive ganze Zahl,
- jede id kommt höchstens einmal vor,
- Namen müssen nach Entfernen äußerer Leerzeichen nicht leer sein,
- Namen müssen nicht eindeutig sein,
- äußere Leerzeichen in Feldern werden ignoriert,
- ungültige Pflichtdaten führen zu ValueError ,
- die exakte Formulierung der Fehlermeldung ist nicht vorgegeben.

# Erlaubte Datumsformate
Unterstuetzte Formate:
    YYYY-MM-DD
    DD.MM.YYYY


# Oeffliche API
pase_date, load_people, find_age_neighbors, find_birthday_groups