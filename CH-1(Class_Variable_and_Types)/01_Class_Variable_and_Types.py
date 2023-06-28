#! Variable and types


""" 
Comments
Data
Variable
Dynamic Type
Type() function
Data Types
Memory Management
Print() function
Special characters
 """

#! Python converts the .py file into .pyc file 
#!  .py ======compiler===========.pyc (Byte code)



"""
! So for compilation of .py file it is first converted into  .pyc which in byte code form and then it is executed  

Yes, that's correct. When you run a Python script, the Python interpreter first compiles the source code into bytecode, which is stored in .pyc files (if the .pyc file doesn't exist yet or is out of date with the corresponding .py file). The bytecode is a lower-level representation of the Python code that can be executed more efficiently by the interpreter.

When you run the script again, the Python interpreter checks the modification time of the .py file and compares it to the corresponding .pyc file. If the .pyc file is up-to-date, the interpreter loads the bytecode from the .pyc file instead of recompiling the source code, which can save time and improve performance.

It's worth nothing that the Python interpreter uses a bytecode compiler, not a JIT compiler. The bytecode compiler translates the Python code into a lower-level representation that can be executed more efficiently, but it does not perform dynamic optimizations at runtime like a JIT compiler does. However, there are third-party tools like PyPy that use a JIT compiler to improve the performance of Python code.
"""

#  1 comments

""" Python has two kind of comments
#! Single line comments  ===========>>>>> #(Pound Symbol)
#! Multiline comments    ===========>>>>> #"""( Closed in Triple quotes) """
"""
