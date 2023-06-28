# write a python script which takes a three digit number from the user and displays on its last digit 

number=int(input("Enter the number whose last digit you want to print:\t"))

result=number%10;  # This will display last digit as remainder 

print("\nThe last digit of the number is", result);
