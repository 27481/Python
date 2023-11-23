a=7
b=1
c=0


try:
    print("File opened")
    b=int(input("enter a number"))
    c=a/b


except Exception:
    print("You cannot divide by zero")

except ValueError:
    print("Enter  a number bola tha ..Gadhe")

except Exception:
    print("Kuch toh gadbadh hai...")
else:
    print(c)
finally:
    print("File closed")


print(c)
print("Bye")