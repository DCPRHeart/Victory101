# Strings
#DOCS: https://docs.python.org/3/library/stdtypes.html#textsequence-type-str
#ALSO: https://docs.python.org/3/tutorial/introduction.html

# Strings are sequences of characters, used to store and represent text-based information
# Strings in Python are immutable, meaning once created, their content cannot be changed
# Strings can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """)
#  - Triple quotes are used for multi-line strings or docstrings

# Common string operations include concatenation (+), repetition (*), and membership testing (in, not in)
# Strings support various methods for manipulation and querying:
#   .lower(),
#   .upper(),
#   .find(),
#   .replace(),
#   .split(),
#   .join()
#   .strip()
#   and many more

# you can also check if a string is a number with .isdigit() or sometimes .isnumeric()
# Strings can be indexed and sliced like lists, with indexing starting at 0
my_string = "Hello, World!"
print("Original string:", my_string)
print("First character:", my_string[0])  # Accessing first character
print("Last character:", my_string[-1])  # Accessing last character
print("Substring (0-4):", my_string[0:5])  # Slicing the string
print("String length:", len(my_string))  # Length of the string
print("Lowercase:", my_string.lower())  # Convert to lowercase
print("Uppercase:", my_string.upper())  # Convert to uppercase
print("Find 'World':", my_string.find("World"))  # Find substring
print("Replace 'World' with 'Python':", my_string.replace("World", "Python"))  # Replace substring
print("Split by comma:", my_string.split(","))  # Split string
# Joining a list of strings into a single string
words = ["Hello", "from", "Python"]
print("List of words:", words)
joined_string = "_".join(words) or str.join("_", words)
print("Joined list of words:", joined_string)
# Stripping whitespace
whitespace_string = "   Hello, World!   "
print("Before strip:", repr(whitespace_string)) #repr shows the whitespace in the terminal
print("After strip:", repr(whitespace_string.strip()))  # Remove leading/trailing whitespace

# Check if string is numeric
numeric_string = "12345"
print("Numeric string:", numeric_string)
print("Is numeric:", numeric_string.isnumeric())  # True
print("Is digit:", numeric_string.isdigit())  # True
non_numeric_string = "123abc"
print("Non-numeric string:", non_numeric_string)
print("Is numeric:", non_numeric_string.isnumeric())  # False
print("Is digit:", non_numeric_string.isdigit())  # False
# Show difference between isnumeric and isdigit
fraction_string = "½"
fraction_string2 = "0.5"
print("Fraction string:", fraction_string)
print("Is numeric (½):", fraction_string.isnumeric())  # True
print("Is digit (½):", fraction_string.isdigit())  # False
print("Fraction string 2:", fraction_string2)
print("Is numeric (0.5):", fraction_string2.isnumeric())  # False
print("Is digit (0.5):", fraction_string2.isdigit())  # False