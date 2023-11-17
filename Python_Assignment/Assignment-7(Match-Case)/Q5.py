""" 
Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number
"""


num=int(input("Enter the number:\n"))
match num:
    case 1: 
        if(num%2=0):
            print("Saurabh Shukla")
    case 2:
        if(0>num and num%2!==0):
            print("Prateek Jain")
    case 3:
        if(num>0 and num%2!=0):
           print("Aditya Choudhary")


