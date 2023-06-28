# Recursion using lambda 


#!Calculate factorial of a number using recursive lambda expression 


f=lambda a:1 if a==0 else a*f(a-1)


num=int(input("Enter the number whose factorial you want to find out:\n"))
print(f(num))

