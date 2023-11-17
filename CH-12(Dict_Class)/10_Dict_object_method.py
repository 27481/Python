# Some more dict object methods

""" 
pop(key)   -------> delete that specific element and return the data-value of elemetn
popitem()  -------> return element as a tuple and delete the last element and print the deleted element 
clear()    -------> clear up the entire dictionary 
"""

#! we can put data in dict object,delete data in dict object and edit in dict object


d={"hello":"world","king":"kong","god":"zilla"}
print(len(d))
print(sorted(d))
print(min(d))
print(max(d))

print("Poping the element from the dict:")
print(d.popitem())
print("Printing the element after the pop:")
print(d)

print("Performing the clear() operation on the dict d1:")
print(d.clear())

