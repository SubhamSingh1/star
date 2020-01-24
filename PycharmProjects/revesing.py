Num = int(input("Please Enter any Number: "))
rev = 0
while (Num > 0):
    r = Num % 10
    rev = (rev * 10) + r
    Num = Num // 10

print("\n Reverse of entered number is = %d" % rev)
