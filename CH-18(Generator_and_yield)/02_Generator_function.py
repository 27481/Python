# What are generators 

# 1> Generators are special kind of functions 

# 2> A generator-function is defined like a normal function, 
#                                 but whenever it needs to generate a value , it does so with the yield keyword rather than return

# If the body of a def contains yield, the function automatically becomes a generator function


def f1():
    yield 10
    yield 20
    yield 30


it=f1() #! it is generator object f1 also it returns generator object is nothing but iterator object

print(next(it))
print(next(it))
print(next(it))


print(it)