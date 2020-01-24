def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function",list)

print()
list1 = [10,30,40,50]
change_list(list1)           
print("list outside function",list1)

print("\n")

def change_string(str):
    str = str + ",Hows you"
    print("printing the string inside function:",str)
string1 = "Hi I am there"
change_string(string1)
print("printing the string outside function:",string1)



