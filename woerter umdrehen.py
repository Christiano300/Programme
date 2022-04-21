from tkinter import *
import sys

def turn():
    eingabe = entry.get
    output = ""
    liste = eingabe.split()
    for i in range(len(liste)):
        liste[i] = liste[i][::-1]
    for i in range(len(liste)):
        output = output + liste[i] + " "
    output.strip()
    op = Label(root, text=output)
    op.grid(row=6, column=2)

root = Tk()
root.geometry('250x200')
entry = Entry(root,font=("arial", 15))
entry.grid(row=2, column=2)
btn = Button(root,text="Wörter umdrehen", command=turn)
btn.grid(row=4, column=2)

root.mainloop()
