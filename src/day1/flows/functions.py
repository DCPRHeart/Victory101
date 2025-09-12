#Functions
#DOCS: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#ALSO: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
# Functions are defined using the def keyword, followed by the function name and parentheses ( )
# Parameters can be specified within the parentheses, and the function body is indented below the definition

def listToStringRecursive(list: list) -> str: # -> str indicates the return type, but does not garantee it
    if len(list) == 0:
        return ""
    elif len(list) == 1:
        return str(list[0])
    item = str(list.pop())
    return listToStringRecursive(list) + "," + item


def listToString(x=[]):
    """
    Take as input a list\n
    Print comma separated
    """
    
    i = 0
    output = ""
    while (i < len(x)):
        output = output + str(x[i])
        i+=1
        if i<len(x):
            output = output + ","
        #end_if
    #end-while
    print(output)
#end-func

# __name__ is a special variable in Python that represents the name of the current module.
# When a Python file is run directly, __name__ is set to "__main__".
if __name__ == "__main__":
    print(listToStringRecursive([1,2,3,4,5]))