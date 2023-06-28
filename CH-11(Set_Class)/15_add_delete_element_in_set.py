s1={1,2,3,4,5}
s1.add((11,22))
print(s1)

#! Elements of these iterable are added into the set 
s1.update([10,20],'ABC',range(20,24,1)) 
print(s1)

s1.discard(10)  #! discard() Remove an element from a set if it is a member.
                #!If the element is not a member, do nothing.

s1.remove(1)
print(s1)
