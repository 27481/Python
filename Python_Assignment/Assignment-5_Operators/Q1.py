# Write a python script to remove the last digit from a given number 
# for eg( if users enters 2534 then your output should be 253)

num=int(input("Enter the number:\n"))

num=(num/10);  # Diving any number by 10 will remove its last digit from the number 

print(int(num))