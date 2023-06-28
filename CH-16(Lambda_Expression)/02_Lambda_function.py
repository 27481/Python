# Writing a function without any name by using lambda function

f=(lambda a,b:a+b)(3,4)  #! here f-> is a name which is going to represent lambda object

def add(a,b):
    return a+b;


x=add     #! This is not a function call, here x contains the id of the function 
print(x)  #! This is the function call 

print()