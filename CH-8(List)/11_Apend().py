# There are 2 ways to add elements in the list 

# 1> append()  =====>  append means adding element at the last of the list
                    #  so we dont have to specify the index number
                    #  append() function contains only 1 argument 

# 2> insert()  ====>
                    # It works same as append() but it can insert element in
                    # anywhere at any index in the list
                    # shifting of elments will be done by insert() function itself   


#! These 2 methods are the attributes of list class

# These 2 are the attributes are of list class this is why we are able to access and them by using dot(.) operator


""" 
Class is a group of variables and functions . These variables and functions are 
called attributes
"""


#! Syntax of append()    =====>>>>   listObject.append(value)
#! Syntax of insert()    =====>>>>   listObject.insert(index, value)


# ex ===>>>

l1=[2,1,0,0,5,4,1,5,3,0,0,5,1]
l1.append(52);                   # appending new element using using append() 
print(l1);

