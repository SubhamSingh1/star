def smallest(n):
    sm = 9
    while n>0:
        r = n%10
        if sm>r:
            sm = r
        n=n//10
    return sm
sm  = smallest(579)
print(sm)