#  Built-in function 

""" 
len()
min()
max()
sum()
sorted()
"""

s1="utkarshPandey"
print(min(s1), s1.count('e'), s1.isdigit(), s1.isalpha())

s2="utkarsh pandey"
print(min(s2))  # It will print space becuase space has smallest ascii code
                # ascii code for space character is 32 which is smallest 

print(min(s1))
print(max(s1))  # print character with highest ascii value 

testing="Mysirg education Services"
print(min(testing));

# print(sum(list((s1)))

print(int(e) for e in s2)
print(s2)

print(int(e) for e in s2 if eval(e)==int and ord(e)<=57)

# print(sorted(testing))
