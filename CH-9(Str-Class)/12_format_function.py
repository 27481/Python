s1="This is a string";

#! format function 
# In Python, the format() function is used to format a string by replacing placeholders in the string with specified values. The format() function is a very powerful tool for creating dynamic strings that can be customized based on specific inputs.

#! string.format(var1, var2,....)

string ="{}, welcome"
print(string.format("utkarsh"))

a=5;
b=4.5;

string1="Value of a is {} and b is {}"
print(string1.format(a,b))

#! We can also use numbered placeholders or named placeholders to specify the order of the arguments, or to use the same argument multiple times:

string2="value of a is {1} and b is {0} and ab is {0},{1}"
print(string2.format(a,b))

#! Sequencing the string and replacing placeholders in the string
print("{2},{1},{0},{4} these are the values",format(a,b,a+b,a-b))