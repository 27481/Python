# List of List 

# This concept is similar to 2-d array
#! As we know list is collection of hetrogeneous element ie element of any type 
#! so a list can have list type Object in itself 

l1=[[1,3,5],[2,1,8],[5,4,4]]

print(l1[1][2])   #! printing the element of a sub-list 


# using for loop
for row in l1:
    for e in row:
        print(e,end=' ');
    print()

