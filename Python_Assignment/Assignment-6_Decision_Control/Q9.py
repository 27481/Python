#! Write a python script to check whether a given year is a leap year or not

year=int(input("Enter the year you want to check is leap year or not:\n"))

if ((year%4==0 and year%100!=0) or year%400==0):
    print(year,"is leap year\n")
else: print(year,"is not a leap year")
