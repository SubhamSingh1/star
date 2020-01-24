from tkinter import *

class test:
    def __init__(self,tk):
        self.l1=Label(tk,text="Your fav. prog. language").place(x=100,y=90)
        self.e1=Entry(tk).place(x=350,y=90)
        self.b1=Button(tk,text="Add to listbox").place(x=300,y=250)

tk=Tk()
tk.title("Hello")
tk.geometry("600x500")
tt=test(tk)
tk.mainloop()