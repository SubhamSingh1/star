from tkinter import *

parent = Tk()
e1 = Entry(parent).grid(row=0, column=1)

email = Label(parent, text="Email").grid(row=1, column=0)
e2 = Entry(parent).grid(row=1, column=1)

contact = Label(parent, text="Contact").grid(row=2, column=0)
e3 = Entry(parent).grid(row=2, column=1)

password = Label(parent, text="password").grid(row=3, column=0)
e4 = Entry(parent, show="*").grid(row=3, column=1)

submit = Button(parent, text="Submit").grid(row=5, column=0)
cancel = Button(parent, text="Cancel").grid(row=5, column=1)
parent.mainloop()
