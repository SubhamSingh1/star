import time
print("Tick")
print(time.time())
print()

print("Local time")
print(time.localtime(time.time()))
print()

print("Formatted time")
print(time.asctime(time.localtime(time.time())))
print()

print("SLeep time")
for i in range(0,5):
    print(i,end=" ")
    time.sleep(1)