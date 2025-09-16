import tkinter as tk

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

root.mainloop()
