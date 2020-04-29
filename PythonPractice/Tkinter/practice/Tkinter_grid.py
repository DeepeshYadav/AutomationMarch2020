from tkinter import *

top = Tk()
top.geometry("500x300")

height = 5
length = 5

for i in range(height):
    for j in range(length):
        b = Entry(top, text="Hello")
        b.grid(row=i, column=j)
    b.insert(END, i)


top.mainloop()