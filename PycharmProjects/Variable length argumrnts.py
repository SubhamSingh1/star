def printme(*names):
    print("Type of passed arguments is",type(names))
    print(names)
    print("printig the passed arguments....")
    for name in names:
        print(name)
printme("John","David","Smith","Nick")