#2 second way of achieving polymorphism i.e (Overator Overloading)

class calculator:
    def add(self,n1=None,n2=None,n3=None):
       s=0

       if n2!=None and n3!=None:
           s=n1+n2+n3
       elif n2!=None:
           s=n1+n2
       else:
           s=n1
       if n3!=None:
           s=n1+n2+n3
       elif n2!=None:
         s=n1+n2  
         return s

c1=calculator();
print(c1.add(4,5,6))