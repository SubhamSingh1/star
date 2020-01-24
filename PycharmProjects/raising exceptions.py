'''try:
    age = int(input("enter the age@"))
    if age<18:
        raise ValueError
    else:
        print("Age is valid")
except ValueError:
    print("The age is invalid")'''

print()
try:
    a=int(input("Enter a?"))
    b=int(input("enter b?"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ",a/b)
except ArithmeticError:
    print("The value b cant't be 0")
