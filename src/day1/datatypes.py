from func import listToString

a: int = 1
b: float = 1000.0001


c: bool = a <= b #true
c = a > b # false

#immutable
s: str = "This is a String"
s1 =     "0123456789012345"

s2 = s[5:10]
print(s2)
print(s.split("s"))

x_list: list = [1,2,3,"123"]
z_tuple: tuple = ("a","b","c") #immutable

x_list[0] = 100 #works
#z_tuple[0] = 1 #throws error
listToString(x_list)

y: dict = { #map
    "thing1":"This is a" + str(1),
    "thing2": 2,
    "abc": a + b + 1,
    2: "22",
    "bruce": {
        "name": "Bruce Wayne",
        "code_name": "Batman",
        "wealth": 1019519051859186,
    }
}

#adds items of x_list to dictionary y
for item in x_list:
    y["a"+str(item)] = item

print(y[2])
print(y["a3"])
print(y["thing2"])