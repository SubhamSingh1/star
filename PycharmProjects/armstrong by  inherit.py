class arm1:
    def input(self):
        self.n=int(input("ENter the number"))
        self.num=self.n
class arm2(arm1):
    def campare(self):
        self.rev=0
        while(self.n>0):
            r=self.n%10
            self.rev=self.rev+r**3
            self.n=self.n//10
class arm3(arm2):
    def compare(self):
        if self.rev==self.num:
            print("YES")
        else:
            print("NO")
obj1=arm3()
obj1.input()
obj1.campare()
obj1.compare()
