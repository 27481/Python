# Write a recursion function to print first n natural numbers

def show(num):
    if num==0: return 0
    else:
        if num>0:
            show(num-1)
            print(num)




num=int(input("Enter the number upto which you want to print:\n"))
print("\n",show(num))

