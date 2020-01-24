def smallest(n):
     rev = 0
     sm = 9
     while n > 0:
        r = n % 10
        if sm > r:
            sm = r
        x = int(n / 10)
        return sm
sm = smallest(1234591)
print("smallest is ", sm)