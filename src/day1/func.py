
def listToStringRecursive(list: list) -> str:
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

if __name__ == "__main__":
    print(listToStringRecursive([1,2,3,4,5]))