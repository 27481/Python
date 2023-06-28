# Duplicate case in python 

"""
! Duplicate case is not an error but first match will only work 
"""

# example ======>>>>>>>

x=eval(input("Enter a number:\n"));
match x:
    case 1.1:
        print("one")
    case "two":
        print("Two")
    case 3+4j:
        print("Four");

print()

#! match was introduced in 3.10
