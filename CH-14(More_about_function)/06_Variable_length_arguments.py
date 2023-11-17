# variable-length arguments

""" 
In python, variable-length arguments allow a function to accept any number of arugments.
"""
#! There are two kinds of variable-length arugments:

""" 
1> *args
2> **kwargs
"""

def avg(*t): # we want our function to handle variable number of arugments 
    sum=(a+b+c)/3
    return sum

print("Average is",avg(10,20))
print("Average is",avg(10,20,30,40,50,60,70,80))
print("Average is",avg(10,20,30))
print("Average is",avg(10,20,90,70,60))