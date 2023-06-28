# Create a generator to produce first n even natural numbers

def evenProducer(n):
    a=2
    while(n>0):
        yield a
        a+=2
        n-=1


n=int(input("Upto which number you want to print the even natural number:\n"))
for e in evenProducer(n):
    print("\n",e,sep=' ')

