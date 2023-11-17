# for loop

#! for loop only works on iterables 

""" #* for (variable) in (iterable):
           code
           code  
"""

""" 
A for loop in most programming languages, including Python, works by iterating over an iterable object. An iterable is any object that can be looped over, such as a list, tuple, set, or string. The for loop repeatedly calls the built-in next() function on the iterable until there are no more items to iterate over.

The reason why the for loop works only on iterables is because the next() function is not defined for non-iterable objects. When you try to use a for loop on a non-iterable object, you will get a TypeError because the interpreter does not know how to iterate over that object.

In summary, for loops work only on iterables because the next() function is only defined for iterable objects, and the for loop relies on this function to iterate over the iterable.
"""

#* example===>>
for x in "MySirG":
    print(x)