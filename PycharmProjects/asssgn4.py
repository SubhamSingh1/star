cp = int(input("Enter the cost price."))
sp = int(input("Enter the sale price."))

if cp>sp:
    print("The seller has incurred loss of rs.", (cp-sp))

else:
    print("The seller has made profit of rs.",sp-cp)