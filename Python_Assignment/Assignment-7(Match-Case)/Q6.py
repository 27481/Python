""" 
Write a python program to check whether a given string is multiword string or single word string using match case statement 
"""

string=input("Enter a string:\n")
match string:
    case string if ' ' in string:
        print("Multiword String")
    case string if ' ' not in string:
        print("Single word String")
print()

