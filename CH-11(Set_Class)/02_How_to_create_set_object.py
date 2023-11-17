# How to create set object 


#! curly brackets {} are used 

s1={1,5,8}
print(type(s1)) #! Order of values printed will not be same as inserted 

s2={10,2,8,10,10,8}
print(s2) #! Duplicate values are not allowed will be discarded without showing any error

s3={}
print(type(s3))

s3=set()
print(type(s3))

s4=set(10,20,30) # set() function take atmost 1 argument   
print(s4)  