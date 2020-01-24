x=lambda a:a+10
print("Sum = ",x(20))

print()

x= lambda a,b:a+b
print("Sum is ",x(20,30))

print()

def table(n):
    x = lambda a:a*n
    return x
n=int(input("Enter the number"))
b=table(n)

for i in range(1,11):
    print(n,"x",i,"=",b(i))


#finding factorial of a number

print()


def factorial(n):
    x = lambda a:n*i
    return x
n=int(input("Enter the number"))
b=factorial(n)
f=1
for i in range(1,n+1):
    print(b(i))
