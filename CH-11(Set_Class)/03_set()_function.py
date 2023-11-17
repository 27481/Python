# 
#! set() function can take only one argument and arugment should be iterable other it will throw an error 

s3={} # < class 'dict' > it will not be considered as tupple  
print(type(s3))

s3=set()
print(type(s3))

# s4=set(10,20,30) # set() function take atmost 1 argument   
# print(s4)

s5=set(10) # object "10" is not iterable as it is of int type 
print(s5)

