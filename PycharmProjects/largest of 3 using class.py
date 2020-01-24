class Largest:
    def input(self):
        self.a = int(input("Enter a = "))
        self.b = int(input("Enter b = "))
        self.c = int(input("Enter c = "))

    def compare(self):
        self.r = max(self.a, self.b, self.c)

    def result(self):
        print("The largest is ", self.r)


object1 = Largest()
object1.input()
object1.compare()
object1.result()
