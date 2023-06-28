# Comparision operator 

#! Two set objects are equal if their elements are same does not matter the order of elements


l1=(1,2,3,4)
l2=(2,3,1,4)
s1=set(l1)
s2=set(l2)

print(s1==s2)

print(s1>s2,s1>=s2)

s2={1,4,6,8}
print(s1>s2)

#! > or < is not reliable 
#! only equally == operator is reliable 

