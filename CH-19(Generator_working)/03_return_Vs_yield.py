# No, yield and return are not interchangeable in Python

# !While both keywords can be used to send a value back to the caller, they have   different behaviors and purposes:

"""
return is used to exit a function and send a final value back to the caller. Once a return statement is encountered, the function exits immediately, and no further code in the function is executed.

yield is used to define a generator function that produces a sequence of values, rather than a single value. When a yield statement is encountered, the function temporarily pauses and sends a value back to the caller. The function can then be resumed later, from where it left off, and continue producing values in the sequence.
"""


""" 
So, if you want to define a regular function that returns a single value, you should use the return keyword. If you want to define a generator function that produces a sequence of values, you should use the yield keyword.
"""

#! example :=>

def sum(a,b):
    return a+b

def generate_numbers(n):
    for i in range(n):
     yield i

""" 
The sum function uses the return keyword to send the final sum of a and b back to the caller. Once the return statement is encountered, the function exits immediately.
"""



"""  
The generate_numbers function uses the yield keyword to send a sequence of numbers back to the caller, one at a time. The function can be paused and resumed as needed, and it will continue producing numbers in the sequence until the end of the loop is reached.
"""