# Write a python script to check whether a given number is prime or not 

num=int(input("Enter the number which you want to check is prime or not:\n"))
cnt=0

for i in range(1,num+1):
    if(i%num==0):
        cnt+=1;

if(cnt>2):
    print(num,"is not a prime number:\n")
else:
    print(num,"is prime number:\n")