# The NoneType is also the return type of functions that don't explicitly return a value. For example:


def u():
    print("Hello")


result=u()       # Output : Hello            
print(result)    # Output : None

""" 
In this example, the function my_function does not return a value explicitly. When we assign the result of the function call to a variable result, the value of result is None, since the function doesn't return anything.
"""
