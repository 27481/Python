# Write a recursive function to calculate sum of squares of first n natural numbers


def squareSum(num):
    if(num==1):
        return 1
    else:
        squaresum= num*num + squareSum(num-1)
        return squaresum;



num=int(input("Enter the number upto which you want to print the sum of squares:\n"))

result=squareSum(num);
print(result);