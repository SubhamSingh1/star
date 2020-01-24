class Animal:
    def speak(self):
        print("Speaking")
class Dog(Animal):
    def speak(self):
        print("Barking")
d=Dog()
d.speak()
print()
class bank:
    def getroi(self):
        return 10
class SBI(bank):
    def getroi(self):
        return 7
class ICICI(bank):
    def getroi(self):
        return 8
b1=bank()
b2=SBI()
b3=ICICI()
print("Bank rate of interest:",b1.getroi())
print("SBI rate of interest:",b2.getroi())
print("ICICI rate of interest:",b3.getroi())