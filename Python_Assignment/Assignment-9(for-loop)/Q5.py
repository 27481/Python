# Write a python program to print N odd natural number in reverse order

n=int(input("Enter the number upto which you want to print N odd natural number in reverse order:\n"))

print()
for i in range(n,1):
    if(i%2!=0):
        print(i)
