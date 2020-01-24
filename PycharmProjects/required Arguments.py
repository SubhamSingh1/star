def func(name):
    message = "Hi "+name
    return message
name = input("Enter the Name @")
print(func(name))

def SI(p,r,t):
    si = (p*r*t)/100
    return si

p = float(input("Enter the pricipal amount::::"))
r = float(input("Enter the rate of interest::::"))
t = float(input("Enter the time period::::"))
print("Simple interest:",SI(p,r,t))