from tkinter import *

tk = Tk()
tk.title("Simple Calculator")
tk.geometry("600x400")

class calc:
    def __init__(self, tk):
        self.var = IntVar()
        self.l1 = Label(tk, text="Enter first no.").place(x=150, y=110)
        self.l3 = Label(tk, text="Result").place(x=150, y=220)
        self.l4 = Label(tk, textvariable=self.var).place(x=400, y=220)
        self.e1 = Entry(tk)
        self.e1.place(x=400, y=110)
        self.e2 = Entry(tk)
        self.e2.place(x=400, y=160)
        self.b1 = Button(tk, text="+", padx=20, pady=20, command=self.add).place(x=120, y=280)
        self.b2 = Button(tk, text="-", padx=20, pady=20, command=self.substract).place(x=240, y=280)
        self.b3 = Button(tk, text="x", padx=20, pady=20, command=self.multiply).place(x=360, y=280)
        self.b4 = Button(tk, text="/", padx=20, pady=20, command=self.divide).place(x=480, y=280)

    def add(self):
        x = float(self.e1.get())
        y = float(self.e2.get())
        z = x + y
        self.var.set(z)

    def substract(self):
        x = float(self.e1.get())
        y = float(self.e2.get())
        z = x - y
        self.var.set(str(z))

    def multiply(self):
        x = float(self.e1.get())
        y = float(self.e2.get())
        z = x * y
        self.var.set(str(z))

    def divide(self):
        x = float(self.e1.get())
        y = float(self.e2.get())
        z = x / y
        self.var.set(str(z))

tt = calc(tk)
tk.mainloop()
