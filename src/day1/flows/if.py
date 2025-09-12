# If statements allow you to execute code based on a condition
#DOCS: https://docs.python.org/3/tutorial/controlflow.html#if-statements

x = input("Enter a number: ")
while not x.isdigit():
    x = input("That's not a number! Enter a number: ")
x = int(x)
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
    