fileptr = open("file.txt","r")
content = fileptr.read(9)
print(type(content))
print(content)
fileptr.close()