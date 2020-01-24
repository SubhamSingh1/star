class first:
    def func1(self):
        self.f=1
        self.x=int(input("Enter a number-->"))
        for i in range(1,self.x+1):
            self.f=self.f*i
class second(first):
    def func2(self):
        print(self.f)
obj=second()
obj.func1()
obj.func2()
