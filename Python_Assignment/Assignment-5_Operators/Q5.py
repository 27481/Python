# write a python script which takes a three digit number from the user and displays only its first digit

number=int(input("Enter the number:\n"))

result=int(number/100);  #dividing by 10 will remove its last digit 
                         #similarly dividing by 100 will remove its last 2 digit
                         # and so on 

print(result)
