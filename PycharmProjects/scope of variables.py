def print_message():
    message="Hello !! I am going to print a message"
    print(message)
print_message()

print()
def calculate(*args):
    sum = 0
    for arg in args:
        sum = sum+arg
    print("The sum is ",sum)
sum = 0
calculate(10,20,30)
print("Value of sum outside the function ",sum)

