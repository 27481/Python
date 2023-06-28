# Taking input from user 


#! input() can take at most one argument of str type 
#! input() always return (str) value

# Everything written by the user is returned by input() function in form of str  
x=input("Enter your name:\n");
y=input("Enter your surname:\n");

print(type(x),x+y, sep=" ");


""" 
The input() function in Python always returns a string, even if the user inputs a number or another data type. This is because Python cannot know in advance what type of data the user will input, so it assumes everything is a string.
"""


""" 
Python considers every input given by the user as a string because the input() function is designed to read input from the user as a sequence of characters, without any assumption about the data type of the input.

When you call the input() function, it reads a line of text from the standard input stream (usually the keyboard) and returns that line as a string. It is up to the programmer to then interpret the string as the appropriate data type, such as an integer or a float, using the appropriate conversion function like int() or float().

This approach provides a lot of flexibility and allows the programmer to handle a wide range of input types in a consistent way. It also simplifies the implementation of the input() function itself, since it only has to deal with strings and does not need to check for or convert different data types.

 """