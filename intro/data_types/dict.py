#Python Dictionaries
#DOCS: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#   Dictionaries are useful for when you want to store groups of information
# and to facilitate queries of data.
#
# - dictionaries can contain any type of data/expression,
# including other dictionaries and functions
#
# - to refrence a dictionary use square bracket indexing or .get()
# e.g. ex_dictionary["a"] ex_dictionary.get("a")
#
# .get() is handy as you can also specify a default to avoid getting
# an error should the id not exist in the dictionary
# ex_dictionary.get("a", "N/A")

a = 1
b = 2
def c():
    return 3

d: dict = { #aka: map, a mapping of an identifier to a data object (usually str -> data)
    "thing1": "This is a" + str(1),
    "thing2": 2,
    "abc4": a + b + c + 4,
    2: "22",
    "bruce": {
        "name": "Bruce Wayne",
        #"code_name": "Batman",
        "wealth": 1019519051859186,
    }
}

print(d["abc4"])
print(d.get("bruce"))
print(d["bruce"].get("name") + " " + d["bruce"].get("code_name", "nobody"))

#dictionaries are mutable
#the following loop will add ten entries to the dictionary
# new_dict = {"i0": 0, "i1": 1, "i2": 2, "i3": 3, ...}
new_dict = {}
for i in range(0,10):
    new_dict["i"+str(i+1)] = i

print(new_dict)

# perhaps a more practical dictionary would be a mapping of the names of months to their number
# apart from readability it doesn't matter what order entries are placed in a dictionary
months = {
    "december": 12,
    "janruary": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
}