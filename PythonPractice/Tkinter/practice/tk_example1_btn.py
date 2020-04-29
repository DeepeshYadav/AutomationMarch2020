from tkinter import *
from tkinter import Message
root = Tk()
root.geometry("200x100")
def my_function():
    Message.info()
namelable = Label(root, text="Name").place(x=30, y=40)
simplebtn = Button(root, text="Simple Button", fg="red")
simplebtn.pack()
root.mainloop()

