utkarsh=[1,2,3,"hello",3.4,"my",5.5,4.8]
b=[]


for i in utkarsh:
    if(type(i)!=int):
      utkarsh.remove(i)
      b.append(i)
a=b;

print(a)
