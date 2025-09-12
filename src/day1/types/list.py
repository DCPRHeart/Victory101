# Lists
# DOCS: https://docs.python.org/3/tutorial/introduction.html#lists

# Lists are ordered collections of items (like arrays in other languages)
# They are mutable, meaning you can change their content without changing their identity
# Lists can contain items of different types, including other lists

# primarily, lists can be indexed, added to, removed from, altered, and sliced

# Tuples are similar to lists but are immutable (cannot be changed after creation)
# DOCS: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
# Tuples are defined using parentheses ( ) instead of square brackets [ ]

# here we will focus on lists

my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("First item:", my_list[0])  # Accessing first item
print("Last item:", my_list[-1])  # Accessing last item
print("List length:", len(my_list))  # Length of the list
my_list.append(6)  # Adding an item to the end
print("After appending 6:", my_list)
my_list.remove(3)  # Removing an item (searches for the first occurrence)
print("After removing 3:", my_list)
x = my_list.pop()  # Removing the last item
print(f"After popping last item (which was: {x}):", my_list)
my_list.insert(2, 10)  # Inserting 10 at index 2
print("After inserting 10 at index 2:", my_list)
my_list[1] = 20  # Changing the second item
print("After changing second item to 20:", my_list)
print("Slicing list (items 1 to 3):", my_list[1:4])  # Slicing the list


nested_list = [1, [2, 3], [4, [5, 6]]]
print("Nested list:", nested_list)
print("Accessing nested item (5):", nested_list[2][1][0])  # Accessing nested item
