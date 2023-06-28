# Endless_Generator is used to generate an endless series 

#! Fibonacci series 
# 0 1 1 2 3 5 8 13 21 ....................

def fib(n):
    a,b=0,1
    while(n>0):
        yield a
        a,b=b,a+b
        n-=1

it=fib()
fib_list=[]

while True:
 print("Do you want to generate another element[y\n]")
 ans=input()
 if ans=='y':
     fib_list.append(next(it))