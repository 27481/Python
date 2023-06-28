# Write a menu driven program with the following options 

""" 
a> check whethter a given set of three numbers are lengths of an isosceles 
   traingle or not 
b> Check whether a given set of three numbers are lengths of sides of a right 
   angled traingled or not 
c> Check whether a given set of three numbers are equilateral triangle or not
d> Exit 
"""




print('''1.To check  whethter a given set of three numbers are lengths of an isosceles 
   traingle or not''','''2. To check whether a given set of three numbers are lengths of sides of a right angled traingled or not''','''3.To check whehter a given set of three numbers are equilaterial traingle or not''',sep="\n")

menu=int(input()):
match menu:
    case 1:
        print("Give 3 number for the sides of the isosceles traingle:\n")
        a,b,c=int((input())),int((input())),int((input()))
        if(a==b or a==c or b==c):
            print("Traingle with given sides is an isosceles triangle:\n")
        else:
            print("Triangle is not an isoscales as any 2 sides are not equal:\n")

    case 2:
        print("Give 3 numbers to check whether a given set of three numbers are lengths of sides of a right angled traingled or not:\n")
        a,b,c=int((input())),int((input())),int((input()))
        if(rightAngledtrinagle(a,b,c)):
             print("Traingle is right angled traingle:\n")
        else:
             print("Traingle is not right angled traingled:\n")

    case 3:
          pass;
          
             
             

def rightAngledtrinagle(a,b,c):
            sides=[a,b,c]
            hypotenuse=max(sides)
            sides.remove(hypotenuse)
            if(hypotenuse**2==sides[0]**2+sides[1]**2):
                return True
            else:
                return False