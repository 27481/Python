""" 
The add() method in Python's set class is used to add a single element to the set. 
It takes only one argument, which is the element to be added. 
The reason for this design choice is that sets are designed to contain unique elements, 
and adding multiple elements at once could potentially result in duplicate elements being added.

If you need to add multiple elements to a set at once, you can use the update() method, which takes an iterable of elements as its argument. 
The update() method adds all the elements in the iterable to the set, while ensuring that duplicates are removed.

For example, 
if you have a set my_set containing the elements {1, 2, 3}, 
and you want to add the elements {4, 5, 6} to the set, 
you can use the update() method as follows: """

my_set={1,2,3}
my_set.update({4,5,6})
print(my_set) 


""" 
Note that the argument to update() is an iterable containing the elements {4, 5, 6} enclosed in curly braces, which creates a set. However, update() can also accept other types of iterables, such as lists or tuples.
"""

"""  
In summary, 
the add() method in Python's set class is designed to add a single element to the set, 
while the update() method is designed to add multiple elements to the set while ensuring that duplicates are removed.
"""

