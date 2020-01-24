from tkinter import *
from tkinter import messagebox
import mysql.connector
t = Tk()
t.title("Forgot password")
t.geometry("400x200")

class fgtpsd:
    def __init__(self, t):
        self.email = Label(t, text="   Email  ")
        self.email.place(x=100,y=50)
        self.e1=Entry(t)
        self.e1.place(x=150,y=50)

        self.submit=Button(t,text="   SUBMIT   ",padx=5,pady=5,command=self.submit)
        self.submit.place(x=170,y=120)

    def submit(self):
        a=self.e1.get()
        m = mysql.connector.connect(host="localhost", user="root", passwd="root", database="star1")
        con = m.cursor()

        try:
            con.execute("select email from register")
            result = con.fetchall()
            v=0
            for x in result:
                if x[0]==a:
                    v=1
                    break
            if v==1:
                print("Succes")
                messagebox.showinfo("Succes","Details have been sent to your register email")
            else:
                print("Fail")
                messagebox.showinfo("Fail","Email not Found")
        except:
            m.rollback()
t2=fgtpsd(t)
t.mainloop()