from array import *

utkarsh=array('i',[23,56,11])


for i in range(3):
    print(utkarsh[i],end='')


print()
print(utkarsh.count(11))
print(utkarsh.index(11))
print(utkarsh.pop(0))
print(utkarsh)

# print(utkarsh.remove(0))
print(reversed(utkarsh))  # <reversed object at 0x7f71abd91fc0>

ord_list=utkarsh.tolist()
print(ord_list) # 