# Mutability and Hashability in a List 

""" 
Mutability objects are changeable 
immmutable objects are not changeable

*All immutable objects are hashable, but not all hashable objects are immutable 

Hashable is a freature of Python objects that tells if the object has a hash value
or not . If the object has a hash value or not.
If it has a hash value that does not change during its entire lifetime 
"""

# hash means mapping 

#! i should know 4 things 
"""
1>Objects which are immutable Mutability and immutabilty
2>Objects which are hashable and objects which are not hashable
3>Object which are sequence and objects which are not a sequence 
4>Objects which are iterable and objects which are not a sequence 
"""
#! we have already seen difference b/w iterable and sequence 
#! Now we will discuss about mutability and hashability


#! Hashability chart =======>>>>>>

""" 

"""


utkarsh=[10,30,50,40,20];
print(hash(utkarsh))  #  TypeError: unhashable type: 'list'

