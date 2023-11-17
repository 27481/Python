#WAP to print first n even natural numbers 

num=int(input("Enter the number upto which you want to print the even natural number:\n"));

i=1;
while(i<=num):
    if(i%2==0): print("The number is:",i);
    i+=1;
