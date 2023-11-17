# Write a python script to print all prime numbers under 100 

count=100
for i in range(1,101):
    if(i%count!=0):
        print(i)
    count-=1