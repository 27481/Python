#! Python is famous for presize coding ie we can code in very less codes 

#! [expression for variable in iterable]    (it is a single line statement)


pandey=[40,20,30,10,50,60];
l4=[x*3 for x in range(5)];
print(l4);


l5=[x**2 for x in range(5)];
print(l5)

l6=[ x for x in input("Enter your name:\n")]
print(l6);


# List comprehension is a concise and powerful way to create a new list by applying an expression to each element of an existing list, while optionally filtering the elements that satisfy a certain condition. It is a syntactic construct available in Python.

# List comprehension in Python consists of an expression followed by a for clause and an optional if clause. The basic syntax of list comprehension is:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)


# In this example, the expression is simply x, the variable is x, and the condition is x % 2 == 0. This creates a new list even_numbers that contains only the even numbers from the original list numbers.


#! so list comprehension means applying some kind of filtering on the existing string and storing it in new list  ????

#* Yes, that's correct! List comprehension is a way to apply a filter or transformation to an existing iterable object (such as a list) and create a new list that contains the results of the transformation.

#* The filter or transformation can be any expression or function that operates on the elements of the iterable object, and the resulting list can be filtered further by adding an optional if clause to the list comprehension.

#* List comprehension is a powerful feature of Python that can make code more concise and readable, especially for simple operations on lists. However, it's important to use it judiciously and avoid making it too complex, as it can quickly become difficult to read and understand.
