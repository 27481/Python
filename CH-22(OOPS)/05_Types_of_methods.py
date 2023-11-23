# """ 
# !Types of methods 
# !1> Encapsulation 
# !2> Inheritance 
# """

# #! Object is created by classes 


class Student:

    school="bbdNITM"; # This a variable of class


    def __init__(self):  # instance method (in which self is passed)
        self.marks=10      
    
    @classmethod
    def get_school(cls): # class method (works with class method)
     return cls.school
    
    @staticmethod
    def add(x,y):   # Static method (works with itself)
       return x+y;


s1=Student();
s2=Student();

print(s1.marks)
print(Student.get_school());
print(s1.add(3,5))

#* class methods are called by using .operator with class name 
#* instant methods are called by using object of class DataType 