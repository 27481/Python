# Map 

""" 
Map function returns a map object(iterable) of the result after applying the given function to each item of a given iterble(list,tuple,etc)
"""


#! map (function,iterable)
#! So map will simply pass all the iterable elements through the function 

# example 

l1=[1,2,3,4]

def square(a):
    return a*a;

print(l1)
l2=list(map(square,l1))
print(l2)


#! map(function, iterables) is a buit-in function so it does not requires to import any module
 
