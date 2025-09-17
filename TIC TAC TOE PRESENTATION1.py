import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TIC-TAC-TOE")

chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mark = ''
count = 0

panneaux = ['panneau'] + ['' for _ in range(9)]

print("chiffres :", chiffres)
print("mark :", mark)
print("count :", count)
print("panneaux :", panneaux)

# Création des 9 boutons du plateau
buttons = [None]  # index 0 ignoré
for i in range(1,10):
    b = tk.Button(root, text='', font=('Arial',20), width=5, height=2,
                  command=lambda x=i: check(x))
    buttons.append(b)

# Positionner les boutons en grille 3x3
r,c = 0,0
for i in range(1,10):
    buttons[i].grid(row=r, column=c)
    c += 1
    if c == 3:
        r += 1
        c = 0

# Fonction pour vérifier si un joueur gagne
def win(symbol):
    b = [buttons[i]['text'] for i in range(10)]
    return (
        (b[1] == b[2] == b[3] == symbol) or
        (b[4] == b[5] == b[6] == symbol) or
        (b[7] == b[8] == b[9] == symbol) or
        (b[1] == b[4] == b[7] == symbol) or
        (b[2] == b[5] == b[8] == symbol) or
        (b[3] == b[6] == b[9] == symbol) or
        (b[1] == b[5] == b[9] == symbol) or
        (b[3] == b[5] == b[7] == symbol)
    )

# 1. Définir la fonction de vérification
def check(digit):
    # 2. Déclarer les variables globales
    global count, mark, chiffres

    # 3-11 : série d’instructions if pour 1 à 9
    if digit == 1 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[1].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 2 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[2].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 3 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[3].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 4 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[4].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 5 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[5].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 6 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[6].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 7 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[7].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 8 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[8].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return
    if digit == 9 and digit in chiffres:
        chiffres.remove(digit)
        if count % 2 == 0:
            mark = 'X'
        else:
            mark = 'O'
        buttons[9].config(text=mark, state='disabled')
        count += 1
        if win(mark):
            if mark == 'X':
                messagebox.showinfo("Résultat", "Le joueur 1 gagne")
            else:
                messagebox.showinfo("Résultat", "Le joueur 2 gagne")
            root.destroy()
            return

    # 12-13 : vérifier égalité
    if count > 8:
        messagebox.showinfo("Résultat", "Match à égalité")
        root.destroy()

root.mainloop()
