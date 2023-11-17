# iter and next

#! these two methods are in built-in module, and don't have to use import statement to use built-in module , all methods in built-in module are not in any class method this is why we dont write print() function as object.print() and for len() function we dont write it like object.len()

#! similarly we don't write object.itr
#! We pass iterable into the iter()funtion and it returns us (iterable objects)
#! means iter() will not accept non-iterables like int,float etc 

#! This iter() function involves use of abstraction due to which we dont know how an iterator object is able to contain 

#!  All methods in built-in module is not in any class method they can used directly

l1=[3,10,4,16,18,2] #* l1 is container object 

it=iter(l1) #! Here this iter() function takes one iterable as arugment and returns iterator object pointing to the first container of the object 

print(type(it)) #! This it is a list iterator 

#* What is iter() function?
#* sol ==>> iter() function takes one iterable as an argument and returns iterator  object which is pointing to the first element of the container object



#! in short iter() function returns iterator object also the iterator is data-structure specific operator
  #! for list its is <class 'list_iterator'> list_iterator


my_list = [1, 2, 3, 4, 5]

# Using a for loop
for element in my_list:
    print(element)
