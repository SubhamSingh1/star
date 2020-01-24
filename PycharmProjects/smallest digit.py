x= int(input("enter a number"))
rev = 0
sm=9

while x>0:
    r= x%10
    if sm>r:
        sm=r
    x=int(x/10)
print("smallest is ",sm)
print()
