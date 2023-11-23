#  Write a python script to reverse a number 

print("Program is staring")
num=int(input("Enter the number which you want to reverse:\n"))
l=len(str(num))
rev_num=0

while (num>0):
    last_digit=num%10
    rev_num=rev_num*10+last_digit
    num=int(num/10)
print(rev_num)