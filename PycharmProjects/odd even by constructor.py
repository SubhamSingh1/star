
class Student:
    def __init__(self,name):
        print("This is a parameterized constructor")
        self.name=name
    def show(self):
        if self.name%2==0:
            print(self.name, "Is a even number.")
        elif self.name%2!=0:
            print(self.name,"Is a odd number")

student = Student(21)
student.show()