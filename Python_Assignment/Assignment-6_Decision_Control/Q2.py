#! Write a python script to check whether a given number is divisible by 5 or not

num=int(input("Enter the number which you want to check is divisible by 5 or not:\n"))

if num%5==0:
    print("\nyes")
else:
    print("No")


#! One liner 
print("Number is not divisible by 5" if int(input("Enter a number"))%5 else "Number is divisible by 5")