class palindrome:
    def input(self):
        self.n=int(input("Enter Number"))
        self.num=self.n

class palindrome1(palindrome):
    def reverse(self):
        self.rev=0
        while self.n>0:
            r=self.n%10
            self.rev=(self.rev*10)+r
            self.n=self.n//10


class palindrome2(palindrome1):
    def compare(self):
        if self.rev==self.num:
            print("Palindrome")
        else:
            print("Not a palindrome")

obj1=palindrome2()
obj1.input()
obj1.reverse()
obj1.compare()