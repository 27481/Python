# Take Nothing, Return Something 

def add():  #!Takes Nothing so this is why the formal arguments are empty 
    print("Enter two numbers:")
    a=int(input())
    b=int(input())
    c=a+b
    return c; #! when a function return something its values goes to exactly from where the function was called

s=add() 
print("Sum is",s)
