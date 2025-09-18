#DOCS: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
import os
local_dir = os.path.dirname(__file__)

f = open(local_dir + "/hw/test.txt", "r+")
print(f.readlines()[4])
f.write("\nThis was a new line")
f.seek(0)
print(f.read())