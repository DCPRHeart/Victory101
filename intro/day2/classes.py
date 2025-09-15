import random

class Pet:
    say = "Snuffle"
    max_age = 20
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True

    def speak(self):
        return print(self.say)
    
    def die(self):
        if self.is_alive:
            print(f"{self.name} has passed away peacefully. age: {self.age}")
        self.is_alive = False
    
    # This function is an example of a function that modifies the dog's age and alive status
    def pass_time(self, years):
        if self.is_alive and years < self.max_age:
            self.age += years
            if self.age > self.max_age//2:
                return print(f"{self.name} has grown older and wiser. age: {self.age}")
            #does the pet die
            if self.age == random.randint(1, 20) or self.age == random.randint(10, self.max_age):
                self.die()
            if self.age > self.max_age:
                self.die()
        else:
            self.is_alive = False
            return f"{self.name} live to the good old age of: {self.age}"
        return f"{self.name} is now {self.age} years old."

    def get_info(self):
        return f"{self.name} is {self.age} years old."
    
    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, is_alive={self.is_alive})"

class Dog(Pet):
    name: str
    age: int
    is_alive: bool
    max_age = 10
    say = "Woof! Woof! ... Hello"
    
    ### This constructor initializes the dog's name, age, and alive status
    def __init__(self, name:str, age:int):
        super().__init__(name,age)

    # This function is an example of a simple method that returns a string
    def bark(self):
        return print("Woof!")
    
    def squirrel(self):
        for i in range(3):
            print("Squirrel!")

martha = Dog("Martha", 5)
martha.speak()

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True

    def meow(self):
        return print("Meow!")
    
    def nap(self):
        for i in range(3):
            for _ in range(i):
                print("Zzz...")
    
# James = Cat("James",5)

# James.meow()
# James.nap()
# while James.is_alive:
#     James.pass_time(1)