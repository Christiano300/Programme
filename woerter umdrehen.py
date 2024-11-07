# from tkinter import *
# import sys

# def turn():
#     eingabe = entry.get
#     output = ""
#     liste = eingabe.split()
#     for i in range(len(liste)):
#         liste[i] = liste[i][::-1]
#     for i in range(len(liste)):
#         output = output + liste[i] + " "
#     output.strip()
#     op = Label(root, text=output)
#     op.grid(row=6, column=2)

# root = Tk()
# root.geometry('550x200')
# entry = Entry(root,font=("arial", 15))
# entry.grid(row=3, column=3)
# btn = Button(root,text="Wörter umdrehen", command=turn)
# btn.grid(row=4, column=2)

# root.mainloop()
# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("200x200")

# Change the label text


def show():
    label.config(text=clicked.get())


# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Monday")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

# Create button, it will change label text
button = Button(root, text="click Me", command=show).pack()

# Create Label
label = Label(root, text=" ")
label.pack()

# Execute tkinter
root.mainloop()
