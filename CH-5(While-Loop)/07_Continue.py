# Continue

""" 
! Continue is a keyword
! It can only be used in the body of loop 
! Continue transfers the control immediately to the (next iteration)
"""


#Example====>

i=1;
x=int(input("Enter a number:"));
while(i<=10):
    if(x%2==0): continue
    print(i,"x=",x)
    i+=1