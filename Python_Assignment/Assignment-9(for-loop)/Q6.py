#  Write a python script to print first 10 even natural numbers

n=100
count=0;
for i in range(1,n):
    if(i%2==0 and count<=10):
        count+=1
        print(i)