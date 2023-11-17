# Create a list of n terms of fibonacci series 

#! we will use list comphrension 




def fibTill(num):
    a,b=0,1
    while n>0:
        yield a
        a,b=b,a+b
        n-=1

num=int(input("Enter the number upto which you want to print fiboncci series:\n"))
print(fibTill(num))
