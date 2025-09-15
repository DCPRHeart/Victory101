#DOCS: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

f = open("hw/test.txt", "r+")
print(f.readlines()[4])
