import random

class Dog:

    # This constructor initializes the dog's name, age, and alive status
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True

    # This function is an example of a simple method that returns a string
    def bark(self):
        return "Woof!"
    
    def squirrel(self):
        for i in range(3):
            for _ in range(i):
                print("Squirrel!")
    
    # This function is an example of a function that modifies the dog's age and alive status
    def pass_time(self, years):
        if self.is_alive and years < 20:
            self.age += years
            if self.age == 10:
                return f"{self.name} has grown older and wiser."
            if self.age == random.randint(1, 20) or self.age == random.randint(10, 20):
                self.is_alive = False
                return f"{self.name} has passed away peacefully. age: {self.age}"
            if self.age > 20:
                self.is_alive = False
                return f"{self.name} has passed away peacefully. age: {self.age}"
        else:
            self.is_alive = False
            return f"{self.name} live to the good old age of: {self.age}"
        return f"{self.name} is now {self.age} years old."

    # This function returns a string with the dog's information
    def get_info(self):
        return f"{self.name} is {self.age} years old."
    
    def __str__(self):
        return f"Dog(name={self.name}, age={self.age}, is_alive={self.is_alive})"