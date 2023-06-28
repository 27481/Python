""" 
In Python, you can use the dot operator to call methods of an object, and to add or modify its attributes, like this:
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person = Person("John", 30)

# Call the "say_hello" method using the dot operator
person.say_hello()  # Output: "Hello, my name is John and I'm 30 years old."

# Access or modify the "name" attribute using the dot operator
print(person.name)   # Output: "John"
person.name = "Mary"
print(person.name)   # Output: "Mary"

# Add a new attribute using the dot operator
person.height = 175
print(person.height)  # Output: 175

