list = [0,1,2,3,4]
print("Printing Original list")
for i in list:
    print(i,end= " ")
list.remove(0)
print("\nprinting the list after removal of first element")
for i in list:
    print(i,end=" ")