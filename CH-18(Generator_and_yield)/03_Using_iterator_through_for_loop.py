# Accessing iterator through for loop 

#! we do not need to add any expection because for loop is implemented using iterator itself 

def f1():
    yield 10
    print("One")
    yield 20
    print("Two")
    yield 30
    print("Three")

it=f1()
a=next(it)
b=next(it)
c=next(it)
print(a,b,c,sep="\n",)

print("\niterating all the elements of the function using iterator through for-loop:")
for e in f1():
    print(e)