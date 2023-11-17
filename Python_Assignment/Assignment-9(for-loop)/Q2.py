# Write a python script to print first N natural numbers

n=int(input("Enter the limit upto which you want to print the numbers:\n"))

for i in range(0,n+1):
    print(i,end=' ')
    i-=1
