"""  
Print all the character of a string, but stop printing if 'r' appeared
in the sequence .If all the character successfully printed then print 
message "All the characters are processed"
"""

x=input("Enter a string:");

for i in x:
    if(i=='r'):
        break
    print(i,end='');
else:
    print("All the characters are processed:\n")

