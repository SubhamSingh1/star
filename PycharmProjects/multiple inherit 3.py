class class1:
    def input1(self):
        self.a = int(input("Enter a ="))

    def factorial(self):
        self.f = 1
        for i in range(1, self.a + 1):
            self.f = self.f * i
        print(self.f)


class class2:
    def input2(self):
        self.b = int(input("Enter b="))

    def prime(self):
        self.x = 1
        for i in range(2, self.b):
            if self.b % i == 0:
                self.x = 0
                break
        if self.x == 0:
            print(self.b, "is not a prime number")
        else:
            print(self.b, "is a prime number")


class class3:
    def input3(self):
        self.c = int(input("Enter c="))
        self.num=self.c

    def palindrome(self):
        self.rev = 0
        while self.c > 0:
            r = self.c % 10
            self.rev = (self.rev * 10) + r
            self.c = self.c // 10
        if self.rev == self.num:
            print("Palindrome")
        else:
            print("Not a palindrome")


class Main_class(class1, class2, class3):
    def main_func(self):
        self.input1()
        self.factorial()
        self.input2()
        self.prime()
        self.input3()
        self.palindrome()


obj1 = Main_class()
obj1.main_func()
