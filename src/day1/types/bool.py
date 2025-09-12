#Booleans
#DOCS: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# Booleans represent one of two values: True or False
# They are often used in conditional (if) statements and loops to control the flow of a program

# Common boolean operations include:
#   and     Logical AND
#   or      Logical OR
#   not     Logical NOT
# Comparison operators that return boolean values include:
#   ==      Equal to
#   !=      Not equal to
#   >       Greater than
#   <       Less than
#   >=      Greater than or equal to
#   <=      Less than or equal to
# Booleans can be combined with other data types in expressions
# In Python, certain values are considered "falsy" (e.g., None, 0, empty collections) and others "truthy" (e.g., non-zero numbers, non-empty collections)
# You can convert other data types to boolean using the bool() function

a = True
b = False
print("a =", a)  # True
print("b =", b)  # False
print("a and b =", a and b)  # False
print("a or b =", a or b)  # True
print("not a =", not a)  # False
print("a == b =", a == b)  # False
print("a != b =", a != b)  # True
print("a > b =", a > b)  # True
print("a < b =", a < b)  # False
print("a >= b =", a >= b)  # True
print("a <= b =", a <= b)  # False
print("bool(0) =", bool(0))  # False
print("bool(1) =", bool(1))  # True
print("bool('') =", bool(''))  # False
print("bool('Hello') =", bool('Hello'))  # True
print("bool([]) =", bool([]))  # False
print("bool([1, 2, 3]) =", bool([1, 2, 3]))  # True
