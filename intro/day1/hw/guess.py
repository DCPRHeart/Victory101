import random
#TODO make a guessing game
# Users should be repeatedly prompted to input a guess from 0-100
# print if they are "hot", "cold", or "correct"
# if they are correct or input a negative number exit the program
## don't forget to check input data and cast input values as integers!

# I've filled target in for you already

target = random.choice(range(0,101))

g=input("Guess a number between 0 and 100: ")
while not g.isdigit():
    g=input("Silly Goose, This is not a number! Enter a number between 0 and 100: ")
g=int(g)

while target != g:
    if g <= target+5 and g >= target-5:
        print("Hot")
    else:
        print("Cold")
    g=input("Guess a number between 0 and 100: ")
    if not g.isdigit():
        print("Silly Goose, This is not a number! Goodbye")
        break
    g=int(g)
if target == g:
    print("Correct")
