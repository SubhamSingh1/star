class Addition:
    def input(self):
        self.a = int(input("Enter the first number"))
        self.b = int(input("Enter the second number"))
        self.z=self.a+self.b

class value_add(Addition):
    def print_value(self):
        print("The sum of two number is ",self.z)

obj = value_add()
obj.input()
obj.print_value()

