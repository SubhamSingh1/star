class prime1:
    def input(self):
        self.n = int(input("Enter the number:"))

class prime2(prime1):
    def check(self):
        self.f = 1
        for i in range(2, self.n):
            if self.n % i == 0:
                self.f = 0
                break
        if self.f == 0:
            print(self.n, "is not a prime number")
        else:
            print(self.n, "is a prime number")
obj1=prime2()
obj1.input()
obj1.check()