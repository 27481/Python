# Default Argument 

""" 
Default value indicates that the function argument will take that values if no 
argument value is passed during the function call

The default value is assigned by using the assigment (=) operator 

! non-default argument follows default argument -Error 
"""



def add(a=0,b=0,c=0,d=0):  #! Note ==> you can not have default argument after non-default argument
    e=a+b+c+d
    return e

print()
print(5)
print("Sum is",add(2,3)) 
print("sum is",add(10,20,30))
print("sum is",add(77,88,10,20))


"""  
In Python and C++ as well, default arguments can only be specified for the rightmost parameters. This means that you can only have default arguments for the parameters on the right side of the parameter list. All the parameters to the left of the parameter with a default argument must not have default arguments.
"""

#! You can not have non-default argumemnt after default argument