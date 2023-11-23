# Objects 
#! an object knows something - with the help of attributes 
#! an object does something - with the help of methods

#* attributes are the values/varibles passed into the class as it is  

#* methods are functions, but when a function belongs to an object we call it "method" 


class utkarsh:
    def __init__(self):
        print("Mein call hogaya")


    def show():
        print("Hello");



var1=utkarsh(); #! 1st Object of class Datatype 
var1.cpu="i7"
var1.ram="16"

var2=utkarsh(); #! 2nd Object of class Datatype  
var2.cpu="2100541530050"

print(var1.cpu," ",var2.cpu)

utkarsh.show() #! show is function here but technically its a method as it is declared inside the class

print(type(var1),end="\n")
print(type(var2),end="\n")


