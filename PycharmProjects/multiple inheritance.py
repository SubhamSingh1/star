class calc1:
    def summation(self,a,b):
        return a+b
class calc2:
    def multiplication(self,a,b):
        return a+b
class derived(calc1,calc2):
    def divide(self,a,b):
        return a/b
d=derived()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))
