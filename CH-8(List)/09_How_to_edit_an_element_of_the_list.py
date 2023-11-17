# How to edit an element of the list?

l1=[50,20,80,10,60,40]


#! Editing means changing the existing value of elements in the list 
#! Editing does not reduce/increase the length of the list 


#* Performing edting in the list
l1[2] = 45;
l1[3] = 50;

print(l1);

# Deleting element in the list whose value is 20 using for loop
l2=[40,20,30];
for x in l1:
    if(x==20):
        del l1[2];
print(l2)