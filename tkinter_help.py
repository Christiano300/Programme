from tkinter import *
from tkinter import font

root = Tk()
root.geometry("400x900")

colors = ["red", "orange", "yellow", "green", "blue",
          "red", "pink", "black", "lime", "magenta"]


for i in range(10):
    if i:
        Button(root, bg=colors[i], width=i, height=0, text="Hallo", fg='#ff0', font=(
            "Segoe UI", 50, "")).pack()
    else:
        Button(root, width=i, height=1, text="Hallo", state=DISABLED).pack()
Button(root, text="iiiiiiiiii").pack()
Button(root, text="MMMMMMMMMM").pack()
mainloop()
