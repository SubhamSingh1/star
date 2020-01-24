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

        self.b2 = Button(t, text="      Forgot password      ",command=self.new,activeforeground="yellow",activebackground="green" ,pady=5)
        self.b2.place(x=180, y=160)

    def new(self):

        t = Tk()
        t.title("Forgot password")
        t.geometry("400x200")

        class fgtpsd:
            def __init__(self, t):
                self.email = Label(t, text="   Email  ")
                self.email.place(x=100, y=50)
                self.e1 = Entry(t)
                self.e1.place(x=150, y=50)

                self.submit = Button(t, text="   SUBMIT   ", padx=5, pady=5, command=self.submit)
                self.submit.place(x=170, y=120)

            def submit(self):
                a = self.e1.get()
                m = mysql.connector.connect(host="localhost", user="root", passwd="root", database="star1")
                con = m.cursor()

                try:
                    con.execute("select email,password from register")
                    result = con.fetchall()
                    v = 0
                    for x in result:
                        if x[0] == a:
                            v = 1
                            break
                    if v == 1:
                        print("Succes")
                        messagebox.showinfo("Succes", "Details have been sent to your register email")
                    else:
                        print("Fail")
                        messagebox.showinfo("Fail", "Email not Found")
                except:
                    m.rollback()

        t2 = fgtpsd(t)
        t.mainloop()

obj=login(t)
t.mainloop()
