employee = {"name":"john","age":29,"salary":25000,"company":"Google"}
print(type(employee))
for x in employee:
    print(x)

employee = {"name":"john","age":29,"salary":25000,"company":"Google"}
print(type(employee))
for x in employee:
    print(employee[x])

employee = {"name":"john","age":29,"salary":25000,"company":"Google"}
print(type(employee))
for x in employee.values():
    print(x)

employee = {"name":"john","age":29,"salary":25000,"company":"Google"}
print(type(employee))
for x in employee.items():
    print(x)