# How to access list elements ?
#! There are so many ways to do it in python



l1= [50,20,"string",60,40]     #* Counting of index starts from 0 in the list element

print(l1);              # [50,20,80,10,60,40]

print(l1[0])            # 50

print(l1[1],l1[2]);     # 20 80


#! when try to access the index in the list which does not exits 
#! we get the following error : IndexError:list index is out of range

#* To know the type of an individual element in an list is 
print(type(l1[1]));