""" 
Memory management in python =====>>>>>>>>>>
"""

# When we run a program it gets some memory in RAM it majorly has 2 parts
""" 
1> Private Heap Space ( in this session of memory, object of classes are created
                        these objects are created at the run time only)
                      (Objects created in private heap space dont have any 
                       name they are created dynamically)

                       Heap is used to store the objects 

2> Namespace or stack   (in this session of memory, it store the 
                        reference variables which are created 
                        which stores id of value)

                        (these reference variable which are createok now i am telling you something about python memory management so check and rectify me if im wrong about it d in this stack
                        area refers to the object which are created in heap space)

                    Stack is used to store the reference variable 
                    not the object itself . The object itself is stored in 
                    the heap, and the reference variable stores/contains the memory
                    address of the object 


In Python, the memory management system is responsible for allocating and deallocating memory in the heap area. 
Python uses a technique called (reference counting) to manage memory allocation and deallocation.


#! NOTE==>

if we change the value of x in our program 
like 
     x=5;
     x=6;

     now (id) in the x will change, now x will point to 6 which is created inside 
     the (Private Heap Space) by storing the id which of object (6) which is created
     inside the Private Heap Space  


     The older object and id of that object, which is still there in the private 
     heap space needs to deleted so that our heap area is properly utilized 
     and it does not get flooded with these objects called garbage block 
"""

""" 
! garbage block => they are those objects and ids of those objects which are still present inside the private heap space and no reference variable is storing there id ie no variable is pointing to them 
         So in this case it is important to delete these garbage blocks and release the memory.
    This will done by python garbage collector 
 """


""" 

 Note => del x; keyword does not destroy the object and id of the object it simply destroys the variable x which is present inside the stack , but the object and its id will still be there in the Private Heap Space 

 ! Programmer can delete/destroy the variable only but the object and dobject id will be deleted by python garbage collector 
 """

