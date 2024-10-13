import tkinter as tk
from tkinter import messagebox

def submit_form():
    """ Funktion, die bei der Formulareinreichung ausgeführt wird """
    
    # Leere die Eingabefelder
    for entry in entries:
        entry.delete(0, tk.END)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Formular mit 8 Feldern")

# Erstelle eine globale Referenz für die Eingabefelder
entries = []

# Definiere die Labelnamen
labels = ["Vorname", "Nachname", "Geburtsdatum", "Geburtsort", 
          "Straße", "Hausnummer", "PLZ", "Ort"]

# Label und Eingabefelder (8 Felder)
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text + ":")
    label.grid(row=i, column=0, padx=10, pady=5)
    
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Button zum Absenden des Formulars
submit_button = tk.Button(root, text="Senden", command=submit_form)
submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# Hauptschleife starten
root.mainloop()
