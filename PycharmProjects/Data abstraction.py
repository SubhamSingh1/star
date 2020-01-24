class employee:
    __count = 0

    def __init__(self):
        employee.__count = employee.__count + 1

    def display(self):
        print("The number of employess:", employee.__count)


emp = employee()
emp2 = employee()
try:
    print(emp.__count)
finally:
    emp.display()
