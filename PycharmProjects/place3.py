from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("500x250")
def fun():
    messagebox.showinfo("Hello","Red button clicked")
def fun2():
    messagebox.showinfo("Hello","white button pressed")
b1=Button(top,text="Red",command=fun,activeforeground="red",activebackground="black",pady=10)
b2=Button(top,text="Blue",activeforeground="blue",activebackground="black",pady=10)
b3=Button(top,text="Green",activeforeground="green",activebackground="black",pady=10)
b4=Button(top,text="white",command=fun2,activeforeground="white",activebackground="black",pady=10)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
top.mainloop()