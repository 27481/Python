# Write a python script to check whether a given number is positive , negative or not

num=int(input("Enter the number you want to check is +Ve, -Ve or not:\n"))

if (num>0):
    print(num,"is +Ve\n")
elif (num<0):
    print(num,"is -Ve\n")
else:
    print(num,"is 0")