try:
    a=int(input("enter a"))
    b=int(input("Enter b"))
    c=a/b
    print("a/b = %d"%c)
except Exception:
    print("cant divide y zero")
else:
    print("Hi I am else block")


