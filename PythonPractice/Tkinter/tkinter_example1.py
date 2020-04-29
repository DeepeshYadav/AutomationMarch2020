from tkinter import *
from tkinter import messagebox
parent = Tk()

parent.geometry("100*200")
def green_fun():
    messagebox.showinfo("Green", "Green Button Clicked")
    print("green button clicked")

def blue_fun():
    messagebox.showinfo("Blue", "Blue Button Clicked")

def red_fun():
    messagebox.showinfo("Red", "Red Button Clicked")
    print("Red Button Clicked")

def brown_fun():
    messagebox.showinfo("Brown", "Brown Button Clicked")

redbutton = Button(parent, command=lambda : red_fun(), activeforeground="red", text="Red", fg='red')

redbutton.pack(side = LEFT)

bluebutton = Button(parent, command=lambda : blue_fun(), text="Blue", fg='blue')
bluebutton.pack(side=RIGHT)

greenbutton = Button(parent, command=lambda : green_fun(), text="Green", fg='green')
greenbutton.pack(side = TOP)

brownbutton = Button(parent, command=lambda : brown_fun(), text="Brown", fg='brown')
brownbutton.pack(side= BOTTOM)

parent.mainloop()