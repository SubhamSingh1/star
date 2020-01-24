from tkinter import *
from tkinter import messagebox
import mysql.connector
t = Tk()
t.title("Register/Signup")
t.geometry("400x300")
class test:
    def __init__(self,t):
        self.name = Label(t, text="Name *")
        self.e1 = Entry(t)
        self.name.place(x=60, y=35)
        self.e1.place(x=170, y=35)

        self.email = Label(t, text="Email *")
        self.e2 = Entry(t)
        self.email.place(x=60, y=80)
        self.e2.place(x=170, y=80)

        self.passwd = Label(t, text="Password *")
        self.passwd.place(x=60, y=130)
        self.e3 = Entry(t,show="*")
        self.e3.place(x=170, y=135)

        self.confirm = Label(t, text="Confirm password *")
        self.confirm.place(x=60, y=180)
        self.e4 = Entry(t)
        self.e4.place(x=170, y=180)

        self.mand=Label(t,text=" * MARKED FIELDS ARE MANDATORY",fg="red")
        self.mand.place(x=80,y=270)

        self.b1=Button(t,text="Register",command=self.data,padx=5,pady=5)
        self.b1.place(x=100,y=220)
        self.b2=Button(t,text="Login",padx=5,pady=5)
        self.b2.place(x=200,y=220)

    def data(self):
        a = self.e1.get()
        b = self.e2.get()
        c = self.e3.get()
        d = self.e4.get()
        print(a,b,c,d)


        m=mysql.connector.connect(host="localhost",user="root",passwd="root",database="star1")
        con=m.cursor()
        e = "insert into register(name,email,password)values(%s,%s,%s)"
        f = (a,b,c)
        try:
            g = con.execute(e,f)
            m.commit()
        except:
            m.rollback()
        print(con.rowcount, ("record inserted"))
        messagebox.showinfo("","registration sucessful")
tt=test(t)
t.mainloop()
