# Python has a module called builtins module which contains tons of function in itself
# To access these function we dont need to import any module as this builtins module 
# is predefined 

#ex print(),type(),id(),bin(),chr() etc we don not have use import statement to use them



#! Built-in-methods

# len() => return length of specified iterable
# min() => returns min value element
# max() => returnds max value element  (max() && min() uses comparison operator)
                                    #    so if the elements in list are of different 
                                    #    type then it will give us error

# sum() => returns sum of elements
# sorted() => returns a sorted list of elements


# example ==========>>>>>>>>>>>>>


utkarsh =[2,1,0,0,5,4,1,5,3,0,0,5,1];
length=len(utkarsh);
print(length);
print(len(utkarsh))
#! we can directly call len() function into print() function
#! or we can call len() function indirectly by storing it into another variable and then calling that variable into the print() function


print(len(range(5))); # Counting elements in the list within a range 

print(min(utkarsh));
print(max(utkarsh));
print(sum(utkarsh));




