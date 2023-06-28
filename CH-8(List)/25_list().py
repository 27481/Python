"""  
The list() function in Python is used to create a new list object, and it can take at most one argument. 
The reason for this design choice is that a list is a sequential container that can hold an arbitrary number of elements, 
but it is typically created by initializing it with a sequence of elements.

The list() function can take a single argument, which is an iterable object containing the elements to be added to the list. This iterable can be a sequence (such as a tuple or a string), a generator expression, or any other iterable object.

If you want to create a list with multiple elements, you can use the square bracket notation, which is a shorthand for creating a new list and initializing it with the specified elements:
"""


my_list = [1, 2, 3, 4, 5]


""" The square bracket notation is more commonly used to create lists because it is concise and easy to read, and it allows you to specify multiple elements at once. """

""" In summary, the list() function in Python takes at most one argument because a list is typically created by initializing it with a sequence of elements. If you need to create a list with multiple elements, you can use the square bracket notation instead, which is a shorthand for creating a new list and initializing it with the specified elements. """


my_tuple=(1,2,3,4,5)
my_list=list(my_tuple)

print(my_list)

my_list = [1, 2, 3, 4, 5]
print(my_list)  # prints [1, 2, 3, 4, 5]
