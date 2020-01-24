from tkinter import *
from tkinter import messagebox
import mysql.connector

t = Tk()
t.title("Register/Signup")
t.geometry("400x300")


class test:
    def __init__(self, t):
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
        self.e3 = Entry(t, show="*")
        self.e3.place(x=170, y=135)

        self.confirm = Label(t, text="Confirm password *")
        self.confirm.place(x=60, y=180)
        self.e4 = Entry(t)
        self.e4.place(x=170, y=180)

        self.mand = Label(t, text=" * MARKED FIELDS ARE MANDATORY", fg="red")
        self.mand.place(x=80, y=270)

        self.b1 = Button(t, text="Register", command=self.data, padx=5, pady=5)
        self.b1.place(x=100, y=220)
        self.b2 = Button(t, text="Login", padx=5, pady=5, command=self.login)
        self.b2.place(x=200, y=220)

    def data(self):
        a = self.e1.get()
        b = self.e2.get()
        c = self.e3.get()
        d = self.e4.get()
        if (len(a)>0 and len(b)>0) and (len(c)>0 and len(d)>0):
            if c==d:
                m = mysql.connector.connect(host="localhost", user="root", passwd="root", database="star1")
                con = m.cursor()
                e = "insert into register(name,email,password)values(%s,%s,%s)"
                f = (a, b, c)
                try:
                    g = con.execute(e, f)
                    m.commit()
                except:
                    m.rollback()
                print(con.rowcount, ("record inserted"))
                messagebox.showinfo("", "registration sucessful")

            else:
                messagebox.showinfo("Error","Passwords Don't match")

        else:
            messagebox.showinfo("Error","Please fill all * marked fields")



    def login(self):
        import mysql.connector
        t = Tk()
        t.title("Login")
        t.geometry("400x250")

        class login:
            def fun1(self):
                a = self.e1.get()
                b = self.e2.get()

                m = mysql.connector.connect(host="localhost", user="root", passwd="root", database="star1")
                con = m.cursor()
                print(a, b)
                try:
                    con.execute("select email,password from register")
                    result = con.fetchall()
                    f = 0
                    for x in result:
                        print(x)
                        if a == x[0] and b == x[1]:
                            f = 1
                            break
                    if f == 1:
                        print("Success")
                        messagebox.showinfo("Approved", "Login sucessful")
                    else:
                        print("Fail")
                        messagebox.showinfo("Error", "Invalid login id or password")
                except:
                    m.rollback()

            def __init__(self, t):

                self.email = Label(t, text="Email")
                self.e1 = Entry(t)
                self.email.place(x=120, y=35)
                self.e1.place(x=170, y=35)

                self.password = Label(t, text="Password")
                self.e2 = Entry(t, show="x")
                self.password.place(x=100, y=80)
                self.e2.place(x=170, y=80)

                self.checkvar1 = IntVar
                self.chkbtn1 = Checkbutton(t, text="Remember me", variable=self.checkvar1)
                self.chkbtn1.place(x=150, y=120)

                self.b1 = Button(t, text="      Login      ", command=self.fun1, fg="magenta", pady=5)
                self.b1.place(x=100, y=160)

                self.b2 = Button(t, text="      Forgot password      ", activeforeground="yellow", command=self.forgot,
                                 activebackground="green", pady=5)
                self.b2.place(x=180, y=160)

            def forgot(self):

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

        obj = login(t)
        t.mainloop()


tt = test(t)
t.mainloop()
