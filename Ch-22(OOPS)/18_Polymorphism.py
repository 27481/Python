""" 

Poly - Many
morphism - Behaviour

"""

""" 
Poymorphism can be implemented in 2 ways given below 

1> Method Overloading 
2> Method Overrding
"""

""" 

!Method Overloading (method name is same, different args)
            (Not applicable in python but can be implemented by programmer) 

  add(n1,n2):
  n1+n2

  add(n1,n2,n3):
   n1+n2+n3

 add(4,5,7)

"""

""" 

!Method OVerriding 

class Father:
    def getPhone(self):
    return "Nokia"

class Child(Father):    
   def getPhone(self):   #! here this method of child is overridding the method of father class
     return "Motorola"   #! depends upon the class type of the object 
   

obj=Child()
obj.getPhone()

"""

class OS1:
    def call(self):
        print("calling")

    def getNotification(self):
        print("Notification on Top, 15")

class OS2(OS1): # here OS2 is inheriting freatures from OS1
    def getNotification(self):
        print("notification at Bottom, 16")

class Iphone:
    def getOsVersion(self,os):
        os.getNotification()
    
    def phoneLagao(self,os):
        os.call()


os=OS2() # making object of OS1 class 

obj=Iphone()
obj.getOsVersion(os) # method overridding 
obj.phoneLagao(os)

# HAS-A relationship
# IS-A relation 

# A-> 2 freatures