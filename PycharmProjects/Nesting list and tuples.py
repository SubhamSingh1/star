Employees = [(101,"Ayush",22),("john",102,29),(103,"james",45),(104,"ben",34)]
print(">>>>>>Printing list<<<<<<<<")
print()
for i in Employees:
    print(i,end = " ")
Employees[0]= (110,"David",23)
print("\n\n")

print(">>>>>>Printing list after modification")
print()
for i in Employees:
    print(i,end="")
