from tkinter import *
from tkinter import messagebox
import mysql.connector
t = Tk()
t.title("Login")
t.geometry("400x250")

class login:
    def fun1(self):
        a=self.e1.get()
        b=self.e2.get()

        m = mysql.connector.connect(host="localhost", user="root", passwd="root", database="star1")
        con = m.cursor()
        print(a,b)
        try:
            con.execute("select email,password from register")
            result = con.fetchall()
            f=0
            for x in result:
                print(x)
                if a==x[0] and b==x[1]:
                    f=1
                    break
            if f==1:
                print("Success")
                messagebox.showinfo("Approved","Login sucessful")
            else:
                print("Fail")
                messagebox.showinfo("Error","Invalid login id or password")
        except:
            m.rollback()

    def __init__(self,t):

        self.email = Label(t, text="Email")
        self.e1 =Entry(t)
        self.email.place(x=120, y=35)
        self.e1.place(x=170, y=35)

        self.password = Label(t, text="Password")
        self.e2 = Entry(t,show="x")
        self.password.place(x=100, y=80)
        self.e2.place(x=170, y=80)

        self.checkvar1 = IntVar
        self.chkbtn1 = Checkbutton(t, text="Remember me", variable=self.checkvar1)
        self.chkbtn1.place(x=150, y=120)

        self.b1 = Button(t, text="      Login      ",command=self.fun1,fg="magenta", pady=5)
        self.b1.place(x=100, y=160)

        self.b2 = Button(t, text="      Forgot password      ",activeforeground="yellow",activebackground="green" ,pady=5)
        self.b2.place(x=180, y=160)



obj=login(t)
t.mainloop()
