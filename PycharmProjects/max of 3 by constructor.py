class student:
    def __init__(self):
        print("This is non parameterized constructor")
    def show(self):

        print(max(3,4,5),"is the largest.")
st=student()
st.show()


class Student:
    def __init__(self,name1,name2,name3):
        print("This is a parameterized constructor")
        self.name1=name1
        self.name2 = name2
        self.name3 = name3

    def show(self):
        print("Largest is ",max(self.name1,self.name2,self.name3))
student = Student(1,2,3)
student.show()
