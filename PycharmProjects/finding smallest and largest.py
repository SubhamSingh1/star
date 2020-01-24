def Digits(n):
    largest = 0
    smallest = 9
    while (n):
        r = n % 10
        largest = max(r, largest)
        smallest = min(r, smallest)
        n = n // 10
    print(largest, smallest)
n = int(input("Enter the number:::::::"))
Digits(n)


