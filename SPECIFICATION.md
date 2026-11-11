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
- Tag und Monat ein- oder zweistellig
- nur existierende Daten --> sonst ValueError

# Altersaehnlichkeit
definiert als absoluter Abstand der Geburtsdaten
Es gilt:
- eine Person ist niemals ihr eigener Nachbar,
- standardmäßig werden maximal 10 Nachbarn geliefert,
- gibt es weniger andere Personen, werden alle verfügbaren Personen geliefert,
- zuerst wird nach kleinstem Datumsabstand sortiert,
- bei gleichem Abstand gewinnt die kleinere ID,
- das Ergebnis darf nicht von der Reihenfolge der CSV-Zeilen abhängen,
- für dieses Praktikum gilt n >= 0 ; bei n == 0 erhält jede Person eine leere Nachbarliste.

# Gleicher Geburtstag
"gleicher Monat und gleicher Tag, unabhaengig vom Jahr"
Zusaetzlich gilt:
- Gruppen mit nur einer Person werden nicht zurückgegeben,
- innerhalb einer Gruppe werden IDs aufsteigend sortiert,
- jede Person darf nur einmal in einer Gruppe vorkommen.

# Verhalten bei leerem Datensatz
- CSV-Datei mit korrektem Header, aber ohne Personen ist erlaubt
- Dann gilt:
    load_people(...) == [] --> leere Liste
    find_age_neighbors([]) == {} --> leeres Dictionary
    find_birthday_groups([]) == {} --> leeres Dictionary

# Oeffliche API
Funktionen erstellen:
pase_date --> rohe CSV-Zeilen lesen
dates.py → Datumsstrings interpretieren
people.py → Personen validieren und laden
analysis.py → Altersnachbarn und Geburtstagsgruppen