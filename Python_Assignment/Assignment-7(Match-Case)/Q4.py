"""
Write a program which takes user’s age and display the category of person. 
Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen. 
"""

age=int(input("Enter your age:\n"))
match age:
    case _:
        if(age<10):
            print("Below 10 years\n")
        elif(age<20 and age>10):
            print("Teen")
        elif(age<40 and age>=20):
            print("young")
        elif(age<60 and age>40):
            print("Experienced")
        elif(age>=60):
            print("Senior Citizen")

print();