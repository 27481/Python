x=int(input("Enter a number:\n"));
0match x:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:#! This _(underscore) is known as wildcard match it is same as default case in switch case of c++
        print("Default", type(x));

#*Case can be of any type bool, int, str etc not like that in c++ where it is only in number 
#* two case name have same value python will not show any error , unlikely c++
x=eval(input("Enter a number:\n"));
match x:
    case 2.1:
        print("one")
    case 3:
        print("Two")
    case True:
        print("Three")
    case "king":
        print("Four")
    case _:#! This _(underscore) is known as wildcard match it is same as default case in switch case of c++
        print("zero");





""" 
1> Match and case are soft keywords 
2> They are not resevered words in other grammatical contexts
3> They are recognized as keywords when parts of a matach statement or case
   block only
   are allowed to be used in all other contexts as variables or argument names
"""



