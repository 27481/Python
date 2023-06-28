# Write a python script to use IS operator to display if both variables are the same both variable are same object or not ? 

list_1=[1,2,3,4,5,6]
list_2=[1,2,3,4,5,6]

print(list_1 in list_2) # False  because both lists are same but memory locations different 

print(list_1 == list_2) # True because the elements are same in both the list 