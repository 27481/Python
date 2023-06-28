# Rercursion Tree

def f1(n):
    if (n==1):
      return 1
    s=n+f1(n-1)
    return s


print("Enter the number upto which you want to find sum:\n")
num=int(input("Enter the number:\n"))
call=f1(num)
print(call)

