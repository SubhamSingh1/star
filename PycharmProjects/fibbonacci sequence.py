n= int(input("Enter the limit of series:"))
a= 0
b= 1
limit =0
s=0

while limit<=n:
    print(a, end = ' ')
    c= a+b
    s=s+a
    a=b
    b=c
    limit = limit+1
print(s)