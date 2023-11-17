# write a python program to print first N odd natural numbers 

n=int(input("Enter the number upto which you want to print odd natural number:\n"))
print()
for i in range(1,n+1):
    if(i%2!=0):
        print(i)
