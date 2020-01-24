nterms = int(input("How many terms? "))

a = 0
b = 1
i = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(a)
else:
    print("Fibonacci sequence upto", nterms, ":")
    while  i < nterms:
        c= a +b
        print(c, end=' , ')

        a = b
        b = c
        i = i+1