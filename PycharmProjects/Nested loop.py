num=int(input("Enter the no. of rows"))
i,j=0,0
for i in range (0,num):
    for j in range (0,num-i-1):
        print(end=" ")

    for j in range (0,i+1):
        print( i,end= " ")
    print()


