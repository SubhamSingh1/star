months = set(["jan","feb","mar","apr","may","june"])
print("\n printing the original set")
print(months)
print("\nremoving items through dsicard method")
months.discard("february")
print("printing the modified set")
print(months)
print("\n removing items through remove() method ")
months.remove("janu")
print("\n printing the modified set")
print(months)