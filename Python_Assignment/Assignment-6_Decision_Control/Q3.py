# Write a python script to check whether a given number is even or not 

num=int(input("Enter the number:\n"))

if num%2==0:
    print("even\n")
else:
    print("odd")


#! one liner 
print("Odd" if int(input("Enter a number"))%2 else "even")