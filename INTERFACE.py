import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Jeu du Morpion")

# --- Phase 1 : Initialisation ---
joueur = 'X'  # joueur qui commence
compteur = 0  # nombre de coups joués

label_tour = tk.Label(root, text=f"Tour du joueur {joueur}", font=('Arial', 14))
label_tour.grid(row=0, column=0, columnspan=3, pady=5)

# --- Phase 2 : Vérification du gagnant ---
def victoire(symbole):
    b = [btns[i]['text'] for i in range(9)]
    return (
        (b[0] == b[1] == b[2] == symbole) or
        (b[3] == b[4] == b[5] == symbole) or
        (b[6] == b[7] == b[8] == symbole) or
        (b[0] == b[3] == b[6] == symbole) or
        (b[1] == b[4] == b[7] == symbole) or
        (b[2] == b[5] == b[8] == symbole) or
        (b[0] == b[4] == b[8] == symbole) or
        (b[2] == b[4] == b[6] == symbole)
    )

# --- Phase 3 : Gestion centralisée des clics ---
def clic_case(i):
    """Gère un clic sur le bouton i."""
    global joueur, compteur

    # ne rien faire si déjà marqué
    if btns[i]['text'] != '':
        return

    # marquer la case
    btns[i].config(text=joueur, state='disabled')
    compteur += 1

    # vérifier victoire
    if victoire(joueur):
        messagebox.showinfo("Résultat", f"Le joueur {joueur} gagne !")
        root.destroy()
        return

    # vérifier égalité
    if compteur == 9:
        messagebox.showinfo("Résultat", "Match nul !")
        root.destroy()
        return

    # changer de joueur
    joueur = 'O' if joueur == 'X' else 'X'
    label_tour.config(text=f"Tour du joueur {joueur}")

# --- Création du plateau ---
btns = []
for i in range(9):
    b = tk.Button(root, text='', font=('Arial', 20), width=5, height=2,
                  command=lambda x=i: clic_case(x))
    btns.append(b)

# Placement 3x3 avec grid
for i, b in enumerate(btns):
    row = i // 3 + 1
    col = i % 3
    b.grid(row=row, column=col)

root.mainloop()
