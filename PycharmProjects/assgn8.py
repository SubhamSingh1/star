bs = int(input("Enter the basic salary"))
bs98 = (bs*(98/100))
bs10 = (bs*(10/100))
bs90= (bs*(90/100))
hra=500
if bs>1500:
    print("Gross salary is: ", bs+bs10+bs90)
elif bs<=1500:
    print("Gross salary is: ",bs+hra+bs98)
