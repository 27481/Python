# Create a list of n terms of fibonacci series

#! we will use list comprenhension and then use generator function to generate the function which will print the series upto nth term


#* making fib function using generator function
def utkarsh(num):
    a,b=0,1
    while(num>0):
        yield a
        a,b=b,a+b
        num-=1


for e in utkarsh(int(input("Enter the number upto which you want to print fibonacci series:\n"))):
 print(e,end="",sep='')