try:
    try:
        fileptr = open("file9.txt", "r")


    finally:
        fileptr.close()
        print("File closed")
except:
    print("Error")
