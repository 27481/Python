# Editing a key in dict class element

""" 
Editing dict key_Value is not possible in python , we have deleted that element which we want to edit and then insert new one 
"""

#! Editing in keys is not possible only (value-part) can be edited (key:value) 

#! So to edit the key we have to have delete that key and then insert a new one


d1={102:"Rahul",105:"Royal",106:"Arjun",107:"Prachi"}

del d1[102];  # This will delete that particular element associated with that particular key value


d1[107]="king"
print(d1)

