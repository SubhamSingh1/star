try:
    a = int(int("Enter a:"))
    b = int(input("enter b"))
    c = a / b
    print("a/b = %d" % c)
except:
    print("Cant divide by zero")
else:
    print("Hi i am else block")

print()

try:
    fileptr = open("file22.txt","r")
except IOError:
    print("File not found")
else:
    print("File found opened succesfully")
    fileptr.close()
