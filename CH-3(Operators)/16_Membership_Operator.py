# Membership Operator 

#! in 
#! not in 

#* These operators are eligible applicable only on (containers)
#* by container, i mean container is a type which can contain multiple values
#* and it is also iterable but not every container is iterable 

#! (in) and (not in) operator will not work on non-iterable containers  
#! int,float,complex,bool are not iterable but str,range,tuple,set,dict are iterable
#! They result True or False same as identity operator

""" 
In Python, membership operators are used to test whether a value is a member of a sequence or collection of values. The two membership operators are in and not in.

The (in) operator checks whether a value is present in a sequence or collection, while the not in operator checks whether a value is not present in a sequence or collection.
 """

# example ===>>>
x = [1, 2, 3, 4, 5]
print(3 in x)       # True, because 3 is present in x
print(6 not in x)   # True, because 6 is not present in x

""" 
In this example, x is a list of integers, and the in operator is used to test whether the value 3 is present in the list. The result is True, because 3 is one of the values in the list. Similarly, the not in operator is used to test whether the value 6 is not present in the list. The result is True, because 6 is not one of the values in the list.

Membership operators are useful when you want to test whether a value is present in a sequence or collection of values, such as a list, tuple, set, or dictionary. They are often used in control flow statements such as if, elif, and while.

"""