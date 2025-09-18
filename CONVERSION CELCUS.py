import tkinter as tk  # importer le module Tkinter

# fonction de conversion Fahrenheit → Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_temperature.get())  # récupérer et convertir en float
        celsius = (fahrenheit - 32) * 5 / 9        # formule de conversion
        celsius = round(celsius, 2)                # arrondir à 2 décimales
        lbl_result["text"] = f"{celsius} \N{DEGREE CELSIUS}"  # afficher résultat
    except ValueError:
        lbl_result["text"] = "Entrée invalide"

# créer la fenêtre
window = tk.Tk()
window.title("Convertisseur de température")
window.resizable(width=False, height=False)

# cadre pour l’entrée
frm_entry = tk.Frame(master=window)

# widget d’entrée Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

# étiquette pour symbole °F
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# placer entrée et étiquette dans le cadre
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# bouton de conversion
btn_convert = tk.Button(
    master=window,
    text="\N{BLACK RIGHTWARDS ARROW}",  # flèche noire vers la droite
    command=fahrenheit_to_celsius
)

# étiquette résultat Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# placer tout dans la fenêtre
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# démarrer l’application
window.mainloop()
