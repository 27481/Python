""" 
Write a program to display day name on the basis of user's liking of a colour.Ask user for his favorite color.
User can anser in sentence like "I like red color". 
    Assuming all color name entered by users is in lowercase. 
       Use match case to display day name associated with the color 

       
a Yellow - monday
b Blue - Tuseday
c Orange - Wednesday
d White - Thursday
e Black - Friday
f Red - Saturday
g All other colours - Sunday 

Assuming all the color name entered by the user is in lowercase
"""

s1=input("What is your favourite color:\n")
l1=["yellow","blue","orange,white,black,red"]

for color in l1:
    if color in s1:
        c=color
        break
else:
    c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thusday")
    case "Black":
        print("Friday")
    case "Red":
        print("Saturday")
    case "other":
        print("Sunday")