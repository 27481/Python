# Break Keyword in python 

""" 
! Break is a keyword 
! Break is used to transfer control outisde the loop body
! Break can only be used in the body of the loop
! Break terminates the executions of the loop 
"""


""" 
WAP to ask user to enter an even number at most 3 times
If user failed to enter an even number in all three chances
then he has lost the game. If user enter an even number
then no more chances will be given and announced him 
a winner
"""

#* Program ====>>>

i=1;

while(i<=3):
    enter=int(input("User please enter the number:\n"))
    if(enter%2==0): break
    i+=1;
    if(i==4): print("Looser:");
    else: print("Winner");