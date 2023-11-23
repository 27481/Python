class MyClass:
    def __init__(self, x):
        self.x = x

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x,y);

# This will result in an error because the second __init__ method overwrites the first one.
obj1=MyClass(10);

print(obj1)