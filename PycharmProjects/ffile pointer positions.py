fileptr = open("file1.txt","r")
print("the file pointer is at byte:",fileptr.tell())
content = fileptr.read()
print("After reading , the filepointer is at :",fileptr.tell())