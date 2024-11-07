from random import choice
from tkinter import *

fenster = Tk()
fenster.config(bg="green", menu=ConnectionAbortedError)
fenster.title("Titel")

icons = ["trek", "trek", "trek", "trek", "arrow", "man", "based_arrow_down", "middlebutton", "based_arrow_up", "mouse", "boat", "pencil", "bogosity", "pirate", "bottom_left_corner", "plus", "bottom_right_corner", "question_arrow", "bottom_side", "right_ptr", "bottom_tee", "right_side", "box_spiral", "right_tee", "center_ptr", "rightbutton", "circle", "rtl_logo", "clock", "sailboat", "coffee_mug", "sb_down_arrow", "cross", "sb_h_double_arrow", "cross_reverse", "sb_left_arrow", "crosshair", "sb_right_arrow", "diamond_cross", "sb_up_arrow", "dot", "sb_v_double_arrow", "dotbox", "shuttle", "double_arrow", "sizing", "draft_large", "spider", "draft_small", "spraycan", "draped_box", "star", "exchange", "target", "fleur", "tcross", "gobbler", "top_left_arrow", "gumby", "top_left_corner", "hand1", "top_right_corner", "hand2", "top_side", "heart", "top_tee", "icon", "trek", "iron_cross", "ul_angle", "left_ptr", "umbrella", "left_side", "ur_angle", "left_tee", "watch", "leftbutton", "xterm", "ll_angle", "X_cursor", "lr_angle "]

menubar = Menu(fenster)
filemenu = Menu(menubar)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="File", menu=filemenu)
fenster.config(menu=menubar)
fenster.geometry("500x500")

def change_icon():
    fenster.config(cursor=choice(icons))

testimage = PhotoImage(name="./files/colors.png", width=64, height=64)
image = Label(fenster, image=testimage).place(x=100, y=100)
Button(fenster, text="Hi", width=15, height=8, command=change_icon).place(x=300, y=300)

mainloop()

# import turtle

# t = turtle.Turtle()

# canvas = turtle.getcanvas()

# t.speed(0)

# while True:
#     mouseX, mouseY = canvas.winfo_pointerxy()
    
#     midpointX = canvas.winfo_width() / 2
#     midpointY = canvas.winfo_height() / 2
    
#     turtleX = mouseX - midpointX - canvas.winfo_rootx()
#     turtleY = -mouseY + midpointY + canvas.winfo_rooty()
    
#     t.goto(turtleX, turtleY)
