# Taking input for elements from the user


print("Taking input from the user by using dict comphrension")
s=input("Enter elements seperated by comma:\n")
s={eval(e) for e in s.split(',')}
print(s)




print("Taking input from the user without dict comprehension")
n=int(input("How many student data you want to store:\n"))
d3={}

for e in range(n):
    key=int(input("Enter roll number:\n"))
    data=input("Enter student name:\n")
    d3[key]=data
print(d3)


