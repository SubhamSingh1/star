list = ["Shubham","Ashish","Singh"]
for i in list:
    print(i)

I = []
n = int (input("Enter the number of elements"))
for i in range(0,n):
    I.append(input("Enter elements"))
print(I)
print("Printing the list items")
for i in I:
    print(i, end="")