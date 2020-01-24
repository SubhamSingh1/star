import math


a= int(input("Enter a:"))
b= int(input("Enter b:"))
c= int(input("Enter c:"))
if a!=0:
    root1 = ((-b+math.sqrt(b**2-4*a*c))/2*a)
    print(root1)
    root2 = ((-b-math.sqrt(b**2-4*a*c))/2*a)
    print(root2)
else:
    print("Enter valid a")