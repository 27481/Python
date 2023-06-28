# Python does have a constructor method called __init__() that is called when an object is created from a class. The __init__() method is used to initialize the instance variables of the class.



#! Here is an example of a class with an __init__() method:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
In this example, the __init__() method takes two arguments (name and age) and initializes two instance variables (self.name and self.age) with the values of those arguments. 
"""


#! When an object of the Person class is created, the __init__() method is automatically called, and the name and age arguments are passed to it:



