"""  
Built-in functions like len(), min(), sum(), and sorted() are applicable to all container classes like lists, tuples, sets, and dictionaries, while methods like split(), join(), items(), and keys() are specific to certain container classes like strings, lists, and dictionaries.
"""
# len() function works for strings, lists, sets, and dictionaries
string_length = len("Hello World")
list_length = len([1, 2, 3, 4])
set_length = len({1, 2, 3, 4})
dict_length = len({'a': 1, 'b': 2, 'c': 3})

# sorted() function works for lists, tuples, and sets
sorted_list = sorted([4, 2, 3, 1])
sorted_tuple = sorted((4, 2, 3, 1))
sorted_set = sorted({4, 2, 3, 1})

# split() method only works for strings
my_string = "Hello World"
my_list = my_string.split()

# join() method only works for strings
my_list = ['Hello', 'World']
my_string = ' '.join(my_list)

# items() and keys() methods only work for dictionaries
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_items = my_dict.items()
my_keys = my_dict.keys()


"""  
As you can see from these examples, built-in functions like len() and sorted() are applicable to a wide range of container classes, 
while methods like split(), join(), items(), and keys() are specific to certain container classes.
"""
