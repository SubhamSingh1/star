List = {1,2,3,4,10,123,22}
oddlist =set(filter(lambda x:(x%3==0),List))
print(oddlist)
print()

List1 = {1,2,3,4,10,123,22}
new_list = list(map(lambda x:x*3,List))
print(new_list)