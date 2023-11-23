class MyClass:
    def __init__(self,x) -> None:
        self.x=x;
     
    def print_value(self):
        print(self.x);

# Creating an instance of MyClass
obj=MyClass(42);

#Callin the method using the instance 
obj.print_value()


#! If we dont use self keyword we can not call the method with object 
