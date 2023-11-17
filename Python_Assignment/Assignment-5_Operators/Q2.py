# Write a python script to get the last digit from a given number (for example , if user enters 2534 then your output should be 253)

num=int(input("Enter the number:\n"))

num=num%10#performing modulo division will give us the last of the number as remainder

print(num)