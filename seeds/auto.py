import pyautogui
import openpyxl
import time
from pynput.mouse import Listener, Button

# Excel-Daten laden
def read_excel_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    
    # Spaltenüberschriften aus der ersten Zeile (Zeile 1)
    headers = [cell.value for cell in sheet[1]]
    
    # Daten ab der zweiten Zeile lesen (Zeile 2 und folgende)
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(list(row))
    
    return headers, data

# Daten in einer Textdatei speichern
def save_form_data_to_txt(headers, row_data, output_file):
    with open(output_file, 'w') as file:
        for header, value in zip(headers, row_data):
            file.write(f"{header}: {value}\n")
    print(f"Formulardaten in {output_file} gespeichert.")

# Formular ausfüllen
class FormFiller:
    def __init__(self, excel_file):
        # Excel-Daten und Spaltenüberschriften einlesen
        self.headers, self.data = read_excel_data(excel_file)
        self.current_row = 0  # Startet mit der ersten Datenzeile
        self.field_positions = []  # Speichert die Positionen der Felder
        self.submit_button_position = None  # Speichert die Position des Senden-Buttons
        self.is_collecting_positions = True  # True, solange wir Positionen sammeln
        self.output_file_template = "formulardaten_{}.txt"  # Dateiname für jede Zeile

    def click_handler(self, x, y, button, pressed):
        """Behandle Mausklicks für das Setzen der Felder und Starten der Verarbeitung."""
        if pressed:
            if self.is_collecting_positions and button == Button.left:
                # Sammle die Koordinaten der Felder mit Linksklicks
                self.field_positions.append((x, y))
                print(f"Feld {len(self.field_positions)} gespeichert: Position {x}, {y}")

            elif self.is_collecting_positions and button == Button.right:
                # Rechtsklick speichert die Position des Senden-Buttons
                self.submit_button_position = (x, y)
                print(f"Senden-Button Position gespeichert: {x}, {y}")
                # Beende die Sammlung der Felder und starte die Verarbeitung
                self.is_collecting_positions = False
                print("Felder und Senden-Button gesammelt. Beginne mit der Datenverarbeitung...")
                self.fill_and_save_data()  # Starte das Ausfüllen der Felder

    def fill_and_save_data(self):
        """Füllt die Felder automatisch mit Excel-Daten und speichert sie."""
        while self.current_row < len(self.data):
            print(f"Verarbeite Zeile {self.current_row + 2} aus der Excel-Datei...")  # Zeile 2 = erste Nutzdatenzeile
            row_data = self.data[self.current_row]

            # Fülle die Felder mit den aktuellen Excel-Daten
            for i, (x, y) in enumerate(self.field_positions):
                pyautogui.click(x, y)  # Klicke auf die gespeicherte Position
                pyautogui.write(str(row_data[i]))
                print(f"Feld {self.headers[i]} gefüllt mit Wert: {row_data[i]}")
                time.sleep(0.01)  # Kurze Pause, um das Einfügen zu verlangsamen

            # Klicke auf den Senden-Button
            if self.submit_button_position:
                pyautogui.click(self.submit_button_position)  # Klicke auf die gespeicherte Position des Senden-Buttons
                print(f"Senden-Button an Position {self.submit_button_position} gedrückt.")
                time.sleep(1)  # Kurze Pause, um das Absenden zu simulieren

            # Speichere die Daten in einer Textdatei mit den Spaltenüberschriften
            output_file = self.output_file_template.format(self.current_row + 1)
            save_form_data_to_txt(self.headers, row_data, output_file)

            # Gehe zur nächsten Zeile der Excel-Datei
            self.current_row += 1
            time.sleep(0.1)  # Optionale Pause zwischen den Zeilen

        print("Alle Daten wurden verarbeitet.")

# Hauptprogramm
if __name__ == "__main__":
    # Excel-Datei laden
    excel_file = "formular_daten.xlsx"  # Pfad zur Excel-Datei
    form_filler = FormFiller(excel_file)

    # Mouse Listener zum Überwachen der Klicks
    with Listener(on_click=form_filler.click_handler) as listener:
        listener.join()
