
def reverse(Num):
    s = 0
    while (Num > 0):
        r = Num % 10
        if r%2 == 0:
            s=s+r
        Num = Num // 10
    return s

s=reverse(123456)
print("The sum of even digits is ",s)


def reverse(Num1):
    k = 0
    while (Num1> 0):
        r = Num1 % 10
        if r%2 != 0:
            k=k+r
        Num1 = Num1 // 10
    return k

k=reverse(123456)
print("The sum of odd digits is ",k,"\n")

