
def reverse(Num):
    rev = 0
    while (Num > 0):
        r = Num % 10
        rev = (rev * 10) + r
        Num = Num // 10
    return rev
