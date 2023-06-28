# Using iterations to print the sum of numbers upto the given numbers by the user 

num=int(input("Enter the number upto which you want to print the sum:\n"))
sum=0;

for i in range(1,num+1):
    sum+=i;

print(sum)