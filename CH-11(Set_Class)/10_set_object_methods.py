# set object methods  i.e  functions inside the set class 

"""
add()                #! add specified item in a set 
update()             #! add iterable(s) elements even str 
discard()            #! remove item 
remove()             #! 
intersection()
union()
clear()
is subset()
is superset()
pop()
"""

#! we can store any type of element in the set but it should be hashable
#! we can pass any iterable in the set function even str 
#! set can not store  list because list is unhashable and set can not store unhashable 

s1={1,2}
s1.add(2)
print(s1,"size of the list is:\n",len(s1),sep=" ")


