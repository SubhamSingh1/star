class prime:
    def __init__(self,n):
        print("Checking prime by  parameterized cons.")
        self.n=n
    def chek(self):
        f=1
        for i in range(2,self.n):
            if self.n%i==0:
                f=0
                break
        if f==0:
            print(self.n, "is not a prime number")
        else:
            print(self.n, "is a prime number")  

num=int(input("Enter a number"))
st=prime(num)
st.chek()