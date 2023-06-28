# next()

#! we have a function called next(), which returns us the element of the iterable container class which is pointed by iter() function
#! next() also increments the iter() object i.e iter() will point to second element of the iterbale container class 

l1=[2,1,0,0,5,4,1,5,3,0,0,5,1]
it=iter(l1)   #* here iter() function, is used to input the iterable container class

print(type(it)) #! Each iter() function has a different type depends upon the type of the container classs which we are giving to the iter() function

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


print("By using For loop")
for i in range(0,len(l1)):
    print(next(it))