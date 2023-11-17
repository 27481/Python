""" 
No, duck typing and function overriding are distinct concepts in programming, although they both relate to polymorphism.

"""

""" 


Duck Typing:

Duck typing is a concept where the type or class of an object is determined by its behavior (specifically, the methods or properties it possesses) rather than by its explicit type or class. The idea is that "if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." In duck typing, the focus is on what an object can do rather than what it is. It allows different types or classes to be used interchangeably if they support a common set of methods or attributes.




Function Overriding:

Function overriding, on the other hand, 
      is a concept related to inheritance and object-oriented programming.

      When a subclass provides a specific implementation for a method that is already defined in its superclass, it is said to override that method. This allows a subclass to provide its own behavior for a method inherited from a superclass. Function overriding is a way to achieve polymorphism in an object-oriented context.

"""



class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!


#! Duck Typing example 

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!




#! Function Overriding:

class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!


""" 

In the function overriding example, 
             the Dog and Cat classes override the speak method inherited from the Animal class. 
             This is a form of polymorphism achieved through inheritance and method overriding. 
             Duck typing, on the other hand, is more about how an object behaves rather than formalizing it through class hierarchies and explicit method overriding.

"""