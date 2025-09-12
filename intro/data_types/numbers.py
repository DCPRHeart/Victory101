#integers and floats
#DOCS: https://docs.python.org/3/library/stdtypes.html#typesnumeric
#ALSO: https://docs.python.org/3/tutorial/introduction.html#numbers

# these are numbers... enough said?

# valid operators (and functions) are:
# x + y     sum
# x - y     difference
# x * y     multiplication
# x / y     quotiant
# x // y    floored quotiant, aka integer division
# x % y     remainder of x / y
# -x        x negated
# +x        x unchanged (lol)
# abs(x)    absolute value of x
# int(x)    x is converted to an integer also floors x
# float(x)  x is converted to a floating point / decimal
# pow(x, y) x to the power of y
# x ** y    x to the power of y

# also see the math module for more advanced mathematical functions
# https://docs.python.org/3/library/math.html

# Examples for each operation

x = 10.7
y = 3.3

print("x =", x)  # 10.7
print("y =", y)  # 3.3
print("x + y =", x + y)  # 14.0
print("x - y =", x - y)  # 7.4
print("x * y =", x * y)  # 35.309999999999995
print("x / y =", x / y)  # 3.242424242424242
print("x // y =", x // y)  # 3.0
# Modulo (remainder), its more usful on integers
print("x % y =", x % y)  # 0.7999999999999998
print("10 % 3 =", 10 % 3)  # 1
print("-x =", -x)  # -10.7
print("+x =", +x)  # 10.7
print("abs(-x) =", abs(-x))  # 10.7
print("int(x) =", int(x))  # 10
print("float(x) =", float(x))  # 10.7
print("float(10) =", float(10))  # 10.0
print("pow(x, y) =", pow(x, y))  # 2494.402116600139
print("x ** y =", x ** y)  # 2494.402116600139
