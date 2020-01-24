from revfunc import reverse
Num= int(input("Enter Num"))
print("reverse is = ",reverse(Num))
x=reverse(Num)
if Num == x:
    print("Yes it's a palindrome")
else:
    print("not a palindrome")