# what is <class 'NoneType' > in python

"""  
<class 'NoneType'> is a built-in data type in Python that represents the absence of a value. The NoneType object has only one possible value, which is the None object.

In Python, None is often used to represent the absence of a value, or to indicate that a variable or function does not return a value. It is also commonly used as a default value for function arguments and as a placeholder value in data structures.

Here is an example of using None as a default value for a function argument:
"""


def example_func(arg1, arg2=None):
    if arg2 is None:
        print("arg2 is not provided:")
    else:
        print("arg2 is provided:", arg2)

example_func(1)      #! OUTPUT : arg2 is not provided 
example_func(1,2)    #! OUPUT : arg2 is provided : 2


""" 
In this example, the second argument arg2 has a default value of None. If arg2 is not provided when calling the function, its value will be None. If arg2 is provided with a value, that value will be used instead.
"""

""" 
The NoneType is also the return type of functions that don't explicitly return a value. For example:
"""

def u():
    print("Hello")

result = u()      #! output : Hello
print(result)     #! output : None

#! In this, above example function u() does not a value explicilty. When we assign the result of the function call to a variable "result" the value of "result" is "None" since the function does not return anything
