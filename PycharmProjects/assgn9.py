s = input("Enter the char/symbol/digit:::")
x = ord(s)
print(x)
if x>=65 and x<=90:
    print("It's a CAPITAL letter.")
elif x>=97 and x<=122:
    print("It's a small letter.")
elif x>=48 and x<=57:
    print("It's a D!G!T.")
elif ((x>=0 and x<=47) or   (x>=58 and x<=64))  or   ((x>=91 and x<=96) or ( x>=123 and x<=127)):
    print("It's a Special Symbol.")
else:
    print("no result..")