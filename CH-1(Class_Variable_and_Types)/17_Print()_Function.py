# Implementing all these example of print()
a="utkarsh";
b="Pandey";
c="2100541530051"

print("welcome");
print(a);
print(a,a*5,"Hello");
print(a,b,c);
print(a,b,c, sep='-');
print(a,b,c, sep=" ");
print(a,b,c, sep='Hello');
print(a,b,c, sep='\n');
print(a,b,c, end='hi');
print(a,b);
print("Hello",end='hi');#! This end="hi" will fill the remove the newline of print()
print(c);

#! After every print() function it gives us line change ie (new line) 
#! If we dont want that to happen then we will use end='' 
#! By default end='' is "\n" ie new line 
#!


#! Print()

"""
print simple text          ===========>>>>>>>                 print("welcome)
print variable value       ===========>>>>>>>                 print(x)
print expression           ===============>>>>>>>             print(x + 5*3)
print multiple ValueError  ===========>>>>>>>                 print(x,y)
sep                        ===========>>>>>>>                 print(x,y, sep='\n')
end                        ===========>>>>>>>             
"""


