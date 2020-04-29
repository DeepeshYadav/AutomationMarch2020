from tkinter import *

parent = Tk()
parent.geometry("400x500")
c = Canvas(parent, bg="grey", height="200")
c.create_arc(())
c.pack()
parent.mainloop()
