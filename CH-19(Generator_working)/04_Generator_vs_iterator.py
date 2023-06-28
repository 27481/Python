# Generator vs iterator

""" 
the iter() function and generator functions serve different purposes, and which one to use depends on your specific use case
"""

""" 
The iter() function is used to create an iterator object from an iterable. An iterator is an object that can be iterated (looped) over, and that returns one value at a time when its __next__() method is called. Iterators are useful when you want to iterate over a sequence of values that are generated on the fly or that are too large to fit into memory all at once.
"""

""" 
On the other hand, generator functions are used to define generators, which are a type of iterator that can be defined using a function. Generator functions allow you to define a sequence of values that are generated on the fly, using simple and readable Python code.
"""

#! Here are a few reasons why you might choose to use a generator function instead of iter():


#* 1> Generators can produce an infinite sequence of values, whereas iterators created with iter() must have a finite length.

#* 2> Generator functions are often easier to read and write than equivalent code using iter(), especially for complex or nested sequences.

#* 3> Generators are more memory-efficient than iter() because they produce values on the fly and only hold one value in memory at a time, whereas iter() may load the entire sequence into memory.


#! Here's an example of how a generator function might be more readable and easier to use than iter() for generating a sequence of numbers

# Using a generator function
def generate_numbers(n):
    for i in range(n):
        yield i

for num in generate_numbers(5):
    print(num)

# Using iter()
class NumberGenerator:
    def __init__(self, n):
        self.n = n
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in NumberGenerator(5):
    print(num)

#! In this example, the generate_numbers() function is simpler and easier to read than the NumberGenerator class, which uses iter() and __next__() to produce the same sequence of numbers.