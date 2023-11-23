#!  In short instance variable is a variable which is declared inside a class within an instant variable i.e a variable which contains attributes in itself whereas a class variable is declared inside the class as a normal variable and do not represent any instant 

""" 
Instance variables are declared within a class and represent attributes of each instance of the class. They are accessed using the self keyword within instance methods of the class.

Class variables, on the other hand, are declared within a class and represent attributes that are shared by all instances of the class. They are accessed using the class name within class methods or instance methods of the class.
"""



# accesser and mutators aka getters and setters 

class Person:

    def __init__(self):
        self.__age=None
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age=age


p1=Person()
p1.set_age(-2);
p1.set_age(19)

print(p1.age)