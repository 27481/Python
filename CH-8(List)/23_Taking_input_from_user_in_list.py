# Taking input from user in list so that list can be filled


print("How many elements you want to enter:\n");
n=int(input())
print("Enter some numbers")
l4=[]
i=0;

while i<n:
    l4.append(int(input()))
    i+=1;
print(l4)

