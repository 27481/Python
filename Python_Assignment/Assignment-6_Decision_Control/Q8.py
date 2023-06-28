# Write a python script to check whether a given quadratic equation has two real and distinct root, real and equal roots or imaginary roots

print("enter value of a,b and c of a quadtric equations:\n")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c;  #! Discriminant 

if d>0:
    print("Real and distinct roots")
elif d==0:
    print("Real and equal roots")
else:
    print("Imaginary roots")

    