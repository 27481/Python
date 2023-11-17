# WAP to count 'a' in a given string using for loop

given=input("Enter the string whose character you want to count:\n");
count=0;

for e in given:
    if (e=='a'):
        count+=1;
print("Count=", count);

print()

#! for loop runs as many times as the number of iterables present in the iterable container