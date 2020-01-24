expenses = []
item = int(input("Enter the no. of items........"))
s=0
for i in range(item):
    expenses.append(int(input("Enter the price......")) * int(input('Enter quantity......')))

for j in expenses:
    s+=j

if s>=5000:
    print("You are eligible for 10% discount, Your total expense is ",s+0.1*s)
else:
    print("your total expense is ,",s)
