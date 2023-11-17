#     Accessing dict element 

d1={102:"Rahul",105:"Royal",106:"Arjun",107:"Prachi"}

#! 1> print(d1)
#! 2> print(d1[102],d1[105],d1[106],d1[107])

#! 3> for k in d1:
#!       print(k)

#! 4> for k in d1:
#!      print(k,d1[k])

print("\nPrinting dict element using print() built-in function:")
#* First method 
print(d1)                #! Print complete dict() 

print("Printing the dict class element using key indexing:")
#* Second method 
print(d1[102],d1[105])  #! If you know the key you can access data 

print("\nPrinting dict element using for loop:")

#* Using for loop (1st way)
for k in d1:     #! only keys are moving into k  not the data of the key 
    print(k,d1[k])

#* Using for loop (2nd way)
for k in d1:       
    print(k,d1[k])  #! Printing both key and the value

    