class A:        # 25 freatures 
    def f1(self):
        print("In A f1");

class B:        # 27 freatures 
    def f1(self): 
        print("In B f1");
    def f2(self):
        print("In A f2");

class C(A,B):
    def f3(self):
        print("In C f3")

obj1=C()
obj1.f1()
obj1.f2()
obj1.f3()

# inheritance uses -> MRO(Method resolution Order) -> it follows a sequence of left to right if 

