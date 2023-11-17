#! Type Converison


a=5;     # Here a is int type 
b="5";   # here b is of string type

#! So , we can not perform any operation on it because both the variables have different dataType

# print(a+b); #! int + str ===>> unsupported operand type(s) for +: 'int' and 'str'
print(str(a)+b); #! str + str ===> 55   string are getting concetinated 

p=4;
q=False;

print(p+q);