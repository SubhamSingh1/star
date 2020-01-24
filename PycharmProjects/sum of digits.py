
def reverse(Num):
    s = 0
    while (Num > 0):
        r = Num % 10
        s=s+r
        Num = Num // 10
    return s
s=reverse(123)
print("The reversed number is ",s)