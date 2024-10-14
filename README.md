# Automatisierte Datenerfassung ohne direkte Schnittstelle
# Robotic Process Automation (RPA)

![image](https://github.com/user-attachments/assets/145d5144-65ae-4f76-a969-6a8af60d191f)




Dieses Python-Projekt demonstriert die automatisierte Erfassung von Daten in ein Formular, bei dem keine direkte API oder Schnittstelle zu der Software existiert, in die die Daten eingetragen werden müssen. Stattdessen werden Maus- und Tastatureingaben simuliert, um die Daten aus einer Excel-Datei in die gewünschte Software einzutragen.

## Funktionen

- **Positionserkennung**: Der Benutzer klickt manuell auf die Felder im Formular, um deren Positionen zu markieren.
- **Automatische Dateneingabe**: Nach dem Erfassen der Feldpositionen werden die Daten aus einer Excel-Datei automatisch in die Formularfelder eingetragen.
- **Automatisches Absenden**: Nach dem Eintragen der Daten wird der "Senden"-Button automatisch gedrückt, dessen Position ebenfalls manuell erfasst wird.
- **Datenprotokollierung**: Jede Zeile aus der Excel-Datei wird in eine `.txt`-Datei gespeichert, wobei die Spaltenüberschriften aus der Excel-Datei verwendet werden, um die Eingaben zu protokollieren.

## Voraussetzungen

Bevor du das Projekt verwendest, stelle sicher, dass du die folgenden Abhängigkeiten installiert hast:

- **Python 3.x**
- **openpyxl** (zum Lesen von Excel-Dateien)
- **pyautogui** (zur Simulation von Maus- und Tastatureingaben)
- **pynput** (zur Erfassung von Maus- und Tastaturereignissen)

Du kannst diese Abhängigkeiten mit dem folgenden Befehl installieren:

```
pip install openpyxl pyautogui pynput
```

## Verwendung

1. **Excel-Datei vorbereiten**: Erstelle eine Excel-Datei (`formular_daten.xlsx`) mit den entsprechenden Spaltenüberschriften in der ersten Zeile und den Daten, die ab der zweiten Zeile erfasst werden sollen.

   Beispiel einer Excel-Datei:
   
   | Vorname | Nachname   | Geburtsdatum | Geburtsort | Straße       | Hausnummer | PLZ   | Ort    |
   |---------|------------|--------------|------------|--------------|------------|-------|--------|
   | Max     | Mustermann | 01.01.1990   | Berlin     | Musterstraße | 1          | 10115 | Berlin |
   | Anna    | Schmidt    | 02.02.1991   | Hamburg    | Beispielweg  | 2          | 20095 | Hamburg |

2. **Programm starten**: Führe das Python-Skript aus, um die Dateneingabe zu starten.

   ```bash
   python form_filler.py
   ```

3. **Feldpositionen erfassen**: 
   - Klicke mit der **linken Maustaste** auf die Formularfelder in der gewünschten Reihenfolge (z. B. Vorname, Nachname, etc.).
   - Sobald du alle Felder markiert hast, klicke mit der **rechten Maustaste** auf den "Senden"-Button, um dessen Position zu speichern.

4. **Automatische Eingabe**: Das Programm füllt die Formularfelder mit den Daten aus der Excel-Datei aus und klickt nach jedem Datensatz auf den "Senden"-Button.

5. **Ergebnis speichern**: Nach jedem Datensatz wird eine `.txt`-Datei mit den Daten erstellt. Die Datei enthält die Spaltenüberschriften und die entsprechenden Werte.

   Beispiel einer `.txt`-Datei:
   
   ```
   Vorname: Max
   Nachname: Mustermann
   Geburtsdatum: 01.01.1990
   Geburtsort: Berlin
   Straße: Musterstraße
   Hausnummer: 1
   PLZ: 10115
   Ort: Berlin
   ```

## Anwendungsfall

Dieses Projekt eignet sich besonders für Anwendungsfälle, in denen es keine API oder direkte Schnittstelle zur Software gibt, in die Daten eingegeben werden müssen. Es kann z.B. verwendet werden, um Daten aus einer Excel-Datei in eine veraltete Software einzutragen, die nur über ein grafisches Benutzerinterface bedient werden kann.

## Haftungsausschluss

Dieses Projekt ist als Demonstration gedacht und sollte nur in Übereinstimmung mit den Regeln und Richtlinien der Software verwendet werden, in die die Daten eingetragen werden. Automatisierte Eingaben können in einigen Softwareanwendungen unerwünscht sein.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der [LICENSE](LICENSE).
```


