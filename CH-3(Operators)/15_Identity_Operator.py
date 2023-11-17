# Identity operators 

# It checks whether the two references refering to the same object or no
# It results in True or False
#! The two identity operators are (is) and (is not) 
a=5;
b=5;


#! when reference count = 0 then object will become eligible for Garbage Collection

""" 
In Python, identity operators are used to compare the memory locations of two objects. The two identity operators are is and is not.
The is operator checks whether two variables refer to the same object in memory, while the is not operator checks whether they refer to different objects.
Here's an example:
 """

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)    # False, because x and y are different objects
print(x is z)    # True, because x and z refer to the same object
print(x is not y)  # True, because x and y are different objects


""" 
In this example, x and y are two different lists with the same values, so they are not the same object in memory. However, x and z are both references to the same list, so they are the same object in memory.

Identity operators are useful when you want to compare two objects to see if they are the same object, rather than just comparing their values. They are often used in control flow statements such as if, elif, and while. However, in general, it is more common to use the equality operator == to compare the values of two objects, rather than their identity in memory.

 """