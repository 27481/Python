# Some important methods of dict class attributes 

""" 
items()  -----> return collection of dict elements also each dict element will be in  form of tuple 
keys()   -----> returns collection of key only elements
values() -----> returns collection of data-values only of the dict elements 
"""

#! All these methods are dict class attributes

my_dict={"utkarsh":"pandey","Rahul":"pandey","Sting":"Energy drink","My_RoLL_number":"2100541530051"}



print(type(my_dict.items()))         

for t in my_dict.items():     # each dict element will in form of tuple 
    print("\n",t)



print("\nPrinting the elements of the tuple ")
# here we are doing tuple unpacking i.e assigning key in k and value in v
for k,v in my_dict.items():
    print(k,v)


print("\n Printing the collection of key only in the entire dict" )
print(my_dict.keys(),sep=" ")
print()
#Printing the collection of key only in the entire dict using for loop 
for k in my_dict.keys():
    print(k)

print()
for u in my_dict.keys():
    print(u,sep=" ")


