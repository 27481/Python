# Positional vs keyword Arguments

def f1(a,b): #! here a and b will be taking the positional argument from function call
    print("a=",a,"b=",b)

f1(2,3)  #! here 2 and 3 are called positional argument 
print(f1)

f1(b=2, a=3) #! keyword argument as we can control the sequence of variable which will passed into the function


#* you can not have positional arugment after keyword arguments
