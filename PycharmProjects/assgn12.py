s= input("enter:")
x= ord(s)
print(x)
if x>=65 and x<=90:
    print("UPPER CASE")

elif x >= 97 and x <= 122:
    print("lower case")

elif x>=48 and x<=57:
    print("D!G!T")

elif x >= 0 and x <= 47:
    print("Special Symbols")
elif  x>=58 and x<=64:
    print("Special Symbols")
elif x>=91 and x<=96:
    print("Special Symbols")
elif x>=123 and x<=127:
    print("Special Symbols")
else:
    print("Enter Valid input")