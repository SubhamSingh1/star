from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

t = Tk()
t.title("CASHBOOK")
t.geometry("800x600")
class test:
    def __init__(self,t):
        self.l1=Label(t,text="DATE*")
        self.l1.place(x=50,y=50)

        self.e1=Entry(t,width=30)
        self.e1.place(x=200,y=50)

        self.l2=Label(t,text="SALESMAN*")
        self.l2.place(x=50,y=100)

        self.cb1=ttk.Combobox(t,values="course")
        self.cb1.place(x=200,y=100)

        self.l3=Label(t,text="CHEQUE AMOUNT*")
        self.l3.place(x=50,y=150)

        self.e3=Entry(t,width=30)
        self.e3.place(x=200,y=150)

        self.l4=Label(t,text="CHEQUE NO.")
        self.l4.place(x=50,y=200)

        self.e4=Entry(t,width=30)
        self.e4.place(x=200,y=200)

        self.l5=Label(t,text="SPT PARTY")
        self.l5.place(x=50,y=250)

        self.cb5=ttk.Combobox(t)
        self.cb5.place(x=200,y=250)

        self.l6 = Label(t, text="SPT CODE")
        self.l6.place(x=50, y=300)

        self.cb6 = ttk.Combobox(t)
        self.cb6.place(x=200, y=300)

        self.l7 = Label(t, text="BILL NO.")
        self.l7.place(x=50, y=350)

        self.e7 = Entry(t,width=30)
        self.e7.place(x=200, y=350)

        self.b1=Button(t,text='REGISTER',padx=30,pady=10,activebackground="red",activeforeground="green",fg="blue",bg="yellow")
        self.b1.place(x=220,y=400)

tt=test(t)
t.mainloop()

