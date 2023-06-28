# Write a menu driven program to perform the follolwing operations:

""" 
a> Check whether a given set of three numbers are lengths of an isosceles
triangle or not

b> Check whether a given set of three numbers are lengths of sides of right angled traingled or not 

c> Check whether a given set of three numbers are equilateral traingle or not 
d> Exit 
"""

print("1.Addition","2.Subtraction","3.Multiplication","4.Division","5.Modulo\n","Enter your choice",sep="\n")

choice=int(input())
match choice:
    case 1:
        print("Enter two numbers:\n")
        a,b=int(input()),int(input())
        c=a+b
        print("Sum is",c)
    case 2:
        print("Enter two numbers:\n")
        a,b=int(input()),int(input())
        c=a-b
        print("Difference is",c)
    case 3:
        print("Enter two numbers:\n")
        a,b=int(input()),int(input())
        c=a*b
        print("Product is",c)
    case 4:
        print("Enter two numbers:\n")
        a,b=int(input()),int(input())
        c=a/b
        print("Division is",c)
    case 5:
        print("Enter the 2 number whose modulo you want to findout:\n")
        a,b=int(input()),int(input())
        c=a%b
        print("Modulo is",c)
    case _:
        print("Invalid Choice Fuck you:\n")
    
print()