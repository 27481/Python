# Filter 

""" 
The filter method filters a given iterable with the help of a function that tests 
each elements in the iterable to be true
 or not 
"""

#! filter(funtion,iterable)

l1=[2,3,5,6,7,9,11,13,15]

def checkPrime(n):
    for i in range(2,n):
      if n%i==0:
       return False
    return True 

filteredList=filter(checkPrime,l1)
print(filteredList)


