# to calculate monthly mobile bill:
call = int(input("Enter the number of calls #"))
fix = 200
c56 = 30
c55 = 25
b1 = (fix + (call-100)*0.60)
b2 = (fix+ c56 + (call-150)*0.5)
b3 = (fix+ c56+ c55 + (call-200)*0.4)

if call>=0 and call<=100:
    print("Your monthly bill for ",call," calls is ", fix)

elif call>100 and call<=150:
    print("your monthly bill for ",call," calls is",b1)

elif call>150 and call<=200:
    print("your monthly bill for",call, "calls is ", b2)

elif call>200:
    print("your monthly bill for ",call," calls is",b3)

