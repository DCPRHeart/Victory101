#TODO Make a recursive function that returns a list
# of the first n Fibonacci numbers

#ask user for value n
n=input("Enter a number: ")
n=int(n)
#make recersive function of fibinocci sequence that stops at n
def Fib(n):
    a=1
    b=1
    if n <=1:
        return [a]
    #end
    if n ==2:
        return [a,b]
    #end
    f=Fib(n-1)
    item=f[-1]+f[-2]
    f.append(item)
    return f
#end

#print sequence
b= Fib(n)
print(b)