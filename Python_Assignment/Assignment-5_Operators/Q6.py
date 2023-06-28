# Write a python script which takes a three digit number from the user and displays only its middle digit

num=int(input("Enter your three digit number :\n"))

result=int(num/10)  # This will remove last digit of the number 

result=result%10  # This will give last digit as remainder
print(result)
