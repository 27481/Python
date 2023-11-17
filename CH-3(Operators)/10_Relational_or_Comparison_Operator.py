#! In programming, the terms "relational operator" and "comparison operator" are often used interchangeably to refer to operators that are used to compare two values and return a Boolean result (True or False) based on the relationship between the values.


#! Result of relational operator is always either true or false 

#! it contains some operators like


""" 
    == (equal to)
    != (not equal to)
    < (less than)
    > (greater than)
    <= (less than or equal to)
    >= (greater than or equal to)
 """

# All of these operators are used to compare two values and determine whether they are equal, not equal, less than, greater than, less than or equal to, or greater than or equal to each other.

print(3>4);                            # Output => False 
print(10>8<6);                         # Output => False 
print(10>8>6);                         # Output => True 
print(10!=9);                          # Output => True
print("Ram">"Bharat"); #Output => True because string comparison works on Alphabetical order
print(4.5>4);
print(True<False);
print(True+True);
print(True+True+True+True);
print(False+False+False+False);


#! Comparison Operators 

#* These operators are technically divided into 2 parts 

# 1> inequality operators   like #! <,>,<=,>=  
# 2> equality operators     like #! ==,!=      ( it never gives error)


#! Note => Only == and != operators can be used between two complex type values
