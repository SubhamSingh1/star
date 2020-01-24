class cal1:
    def sum(self,a,b):
        return a+b
class cal2:
    def multiply(self,a,b):
        return a*b
class derived (cal1,cal2):
    def divide(self,a,b):
        return a/b
d=derived()
print(issubclass(derived,cal2))
print(issubclass(cal1,cal2))