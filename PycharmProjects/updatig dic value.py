employee = {"name":"john","age":29,"salary":25000,"company":"Google"}
print(type(employee))
print("Enter the details of new employee....")
employee["name"] = input("name:")
employee["age"] = int(input("age:"))
employee["salary"] = int(input("salary:"))
employee["company"] = input("company:")
print(employee)