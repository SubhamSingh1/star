n = int(input("ENter the number @"))
def first(n):
    s=0
    while n>0:
        s= s*10+n%10
        n = n//10
    return s
s=first(n)
i = s%10
def last(n):
    k=n%10
    return k
k = last(n)
print("\n The first and last digit are ",i," and",k," respectively")

