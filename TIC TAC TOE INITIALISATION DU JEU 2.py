import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Jeu du Morpion")

# --- Phase 1 : Initialisation ---
joueur = 'X'  # joueur qui commence
compteur = 0  # nombre de coups joués

label_tour = tk.Label(root, text=f"Tour du joueur {joueur}", font=('Arial', 14))
label_tour.grid(row=0, column=0, columnspan=3, pady=5)
