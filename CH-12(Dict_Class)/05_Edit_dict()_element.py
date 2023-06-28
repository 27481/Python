# How to edit dict element ?

""" 
Editing dict element means you want to change 
data-value of the element and not the key
"""

#! Syntax is   =====>>>>>>   dict_object[key-value]=newdata


d1={102:"Rahul",105:"Royal",106:"Arjun",107:"Prachi"}

d1[102]="hello"
print(d1)

#! Yes we can add more than one data , for the same key ,then we can't use str data for key ,we have to use tupple or list 

d1[102]=(2100541530051,"NITM",2100541530048,"BBD",2100541530046)
print(d1)

