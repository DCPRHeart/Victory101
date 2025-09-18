#TODO Use objects to create a family tree
#Each person should have a name and an age
#Each person should be able to have children (other people)
#Create functions to add children to a person
#Finally, create a few people and print out their family tree
from typing import List
from datetime import date

class Person:
    name: str
    year_born: int
    spouse = None #is a Person
    children: list #of Persons
    parent1 = None
    parent2 = None

    def __init__(self, name, year_born, spouse=None,):
        self.name=name
        self.year_born=year_born
        if spouse:
            self.marry(spouse)
        self.children: List[Person] = []
        self.parent1 = None
        self.parent2 = None
    
    @property
    def age(self):
        this_year=date.today().year
        age=this_year-self.year_born
        return age
    
    def add_parents(self, parent1, parent2):
        self.parent1=parent1
        self.parent2=parent2
    
    def marry(self,spouse):
        if self == spouse:
            raise Exception("You cannot Marry yourself!")
        if spouse in self.children:
            raise Exception("You cannot Marry your children!")
        if (self.parent1 and spouse == self.parent1) and (self.parent2 and spouse == self.parent2):
            raise Exception("You cannot Marry your parents!")
        self.spouse=spouse
        spouse.spouse=self
        #str.format("{} has married {}, Congradulations!", self, self.spouse)
        print(f"{self.name} has married {self.spouse.name}, Congratulations!")
        
    def add_child(self,child):
        if not self.__class__.__instancecheck__(child):
            raise Exception("Children must be people!")
        if self.age <= child.age:
            raise Exception("Children must be youger than you!")
        self.children.append(child)
        self.spouse.children.append(child)
        child.add_parents(self,self.spouse)
        print(f"{child.name} has been born to {self.name} and {self.spouse.name}.")
    def __str__(self):
        return self.name + " age:" + self.age
#end-person 

john = Person("John", 1945)
sally = Person("Sally", 1946)
john.marry(sally)
hanah = Person("Hanah", 1970)
sally.add_child(hanah)


"""
         John + Mary
              |
     +--------+--------+
     |                 |
   Alice             Robert
                        |
                        +-- Emma + George, Max, Martin + Susan
                                 |
                            -----+ 
"""