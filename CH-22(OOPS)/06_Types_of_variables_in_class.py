# Types of variable inside a Class 

""" 
In Python, a class can have both 
instance variables 
                and 
class variables.

Instance variables are variables that are specific to each instance of the class. 
They are created when a new object is created from the class and are accessed using the self keyword. Here's an example
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#! In this example, name and age are instance variables of the Person class. They are specific to each instance of the class, and can be accessed using the self keyword.

#************************************************************************************
#************************************************************************************
#************************************************************************************


#! Class variables, on the other hand, are variables that are shared by all instances of the class. They are defined at the class level and are accessed using the class name. Here's an example:


class Person:
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

#! In this example, count is a class variable of the Person class. It is shared by all instances of the class, and can be accessed using the class name Person. Every time a new object is created from the Person class, the __init__ method increments the count variable by 1.

#* So, to summarize, in Python a class can have both instance variables (specific to each instance) and class variables (shared by all instances).

