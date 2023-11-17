# Both add() and update() functions are adding new element into the set 

#! But both of them works separetly 

""" 
add() function add element into the set if the given element's dataType is hashable we can pass both iterable and non-iterable 
while 
     In update() function we can only pass iterable like list,str

In add() function we can only 1 argument of any type 
 But 
    in update() function we can pass more than 1 argument but it should be iterable    
"""    

s1={1,2,3,4,5}
s1.add((11,22))
print(s1)

#! Elements of these iterable are added into the set 
s1.update([10,20],'ABC',range(20,24,1)) 
print(s1)
