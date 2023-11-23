class A:      
    def __init__(self):
        self.m1=9

class B(A):
    def __init__(self):
        super().__init__() # Super is a method by this we can call the init of  its parent class
        print(super())
        self.m2=8


obj=B()
print(obj.m1)
print(obj.m2)
