# Write a python script to display the number of days in a given month number 

month=int(input("Enter the month number:\n"))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 days")
    case month if month in (4,6,9,11):
        print("30 Days")
    case 2:
        print("28 or 29 days")
    case _:
        print("Invaild Month number")

print()

