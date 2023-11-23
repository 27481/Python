class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        total_m1 = self.m1 + other.m1
        total_m2 = self.m2 + other.m2

        s3 = Student(total_m1, total_m2)
        return s3
    
    def __str__(self):
        return str(self.m1) + " : " + str(self.m2)


s1 = Student(45, 35)
s2 = Student(99, 77)
s3 = s1 + s2 

print(s3)

""" 
This revised version ensures that the __str__ method of the Student class is properly indented and aligns with the other methods within the class. 

Now, when you create s3 by adding s1 and s2, the __add__ method will be called, and the resulting s3 object will contain the total marks from both s1 and s2. Finally, printing s3 will display the result using the __str__ method, showing the total marks.

"""