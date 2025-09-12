import time

#Your "first" python program!

a: int = 1
b: float = 1000

c: bool = a <= b
d: str = "This is a String"

x: list = [1,2,3]
str.join(",", x)
y: dict = {
    "thing1":"This is a thing",
    "thing2": 2}
z: tuple = ("1","2",3)

print("Hello World")

x = int(input("Enter Any Number:"))
print()
#for, while loops
# while a <= x:
#     print(a)
#     a += 1

for i in range(0,min(20, x)):
    time.sleep(0.5)
    # if (i>20):
    #     break
    #endif
    print(i+1)

#endwhile