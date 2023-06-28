# That's correct! Variables defined inside an indented block of code (such as a loop, conditional statement, or function) are only visible within that block and its nested sub-blocks. This means that they cannot be accessed from outside that block.

# For example, consider the following code:
x=int(input("Enter the number you want to put inside the function:\n"));
def my_function(x):
    y = 2 * x
    if y < 10:
        z = 3 * y
    return y, z

result = my_function(3)
print(y) # NameError: name 'y' is not defined 
print(z) # NameError: name 'z' is not defined

#! So, here i can not access the variable which are inside the indentation block



""" 
In this code, y and z are defined inside the function my_function in nested blocks of code. However, because y and z are only defined within the function, they cannot be accessed from outside the function.

If you try to print the values of y and z outside the function, you will get a NameError because those variables are not defined in the outer block of code.
"""