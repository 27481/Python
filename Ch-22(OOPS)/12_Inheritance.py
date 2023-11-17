class Iphone13:        # 25 freatures 
    def f1(self):
        print("In A f1");

class Iphone14(Iphone13):        # 27 freatures 
    def f2(self): 
        print("In B f2");

class Iphone15(Iphone14):
    def f3(self):
        print("In C f3")

obj1=Iphone14()
obj1.f1()
obj1.f2()
obj1.f3()

#! Inheritence -> Parent class(aka base class, super class) , Child class(derived class, sub class)

""" 

Inheritace is of 5 types 

1> Single level Inheritance
2> Multi-level Inheritance
3> Mulitple Inheritance
4> Hierarchial level Inheritance
5> Hybrid level Inheritance 
"""