employee = {"name":"john","age":29,"salary":25000,"company":"Google"}
print(type(employee))
print("printing employee data....")
print(employee)
print("deleting employee data")
del employee["name"]
del employee["company"]
print("printing the modified data")
print(employee)
print("deleting the dict.")
print(employee)