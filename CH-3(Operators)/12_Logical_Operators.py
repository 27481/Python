# Logical Operators
  
      #! not and or 

#* Logical operators must be written in lowercase only 



#! not ===>  prints opposite of the actuall Result 
#! and ===>  prints TRUE if both the operands are TRUE other False

# example ===> 

print(not True);
print(True and False);
print(True and True);
print(False and False);
print(3 and 4);
print(3 or 4);
print("HELLO" or "WORLD");   #! empty str == false , non-empty str== true


a=5;
b=4;
# print(a>0 and b/0);   #! zero divison error 


"""

! Every non-zero value is ======>   TRUE
! ZERO ========================>>>  FALSE
! Non Empty string ============>>   TRUE
! Empty string ===============>>>   FALSE

when operands are (non-bool) then result will also be (non-bool)
"""