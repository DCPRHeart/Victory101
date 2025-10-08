#Loops, for loops, while loops, we all love them!
#FOR DOCS: https://docs.python.org/3/tutorial/controlflow.html#for-statements
#WHILE INTRO: https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming

# For loops are used to iterate over a sequence (like a list, string, or range)
# The syntax is: for variable in sequence:
for i in [1, "ad", 3, "bc", 5]:
    print("For loop iteration:", i)
# You can use the range() function to generate a sequence of numbers
for i in range(5):  # Generates numbers from 0 to 4
    print("Range loop iteration:", i)
for i in range(2, 6):  # Generates numbers from 2 to 5
    print("Range with start loop iteration:", i)
for i in range(1, 10, 2):  # Generates odd numbers from 1 to 9
    print("Range with step loop iteration:", i)

# While loops are used to repeat a block of code as long as a condition is true
# The syntax is: while condition:
count = 0
while count < 5:
    print("While loop count:", count)
    count += 1  # Increment the count to avoid infinite loop
    

# Be careful with while loops to ensure the condition will eventually become false