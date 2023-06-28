# reduce 

""" 
The reduce(function,iterable) function is defined in (functools) module 
Just like map function, argument function is applied to all the element of
argument iterable in reduced method 
"""

""" 
map returns an iterable,
whereas reduce returns an accumulated single value 
"""


#! ex===>


import functools

l1=[1,2,3,4]
def multiply(a,b):
    return a*b

r=reduce(multiply,l1)
print(r)