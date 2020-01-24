class cal1:
    def input1(self):
        self.a=int(input("Enter a "))
    def check_even_odd(self):
        if self.a%2==0:
            print(self.a,"is a even number")
        else:
            print(self.a,"is odd number")
class cal2:
    def input2(self):
        self.b=int(input("Enter b"))
    def check_pos_neg(self):
        if self.b>0:
            print("positive number")
        elif self.b==0:
            print("Whole number")
        elif self.b<0:
            print("Negative number")

class cal3:
    def input3(self):
        self.c=int(input("Enter c"))
    def print_square(self):
        print(self.c**2)
class derive(cal1,cal2,cal3):
    def call(self):
        self.input1()
        self.input2()
        self.input3()
        self.check_even_odd()
        self.check_pos_neg()
        self.print_square()


d = derive()
d.call()



