# WAP to check wheter a given number is positive or non-positive 

x=int(input("Enter the number which you want to check is even or not :\n"));

if x>0:
    print(x,"is not a non-zero number");
elif 0>x:
    print(x,"is a negative number");
elif x==0:
    print("It is 0");

