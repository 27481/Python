""" 
Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
"""


import datetime

# getting current date and time 
now = datetime.datetime.now()

# store date in format: dd-mm-yyyy
date=now.strftime("%d-%m-%y")

# store time in format: hh:mm AM/PM
time = now.strftime("%I:%M %p")

# display date and time 
print("Current date:\n", date)
print("Current time:", time)


