# write a python script to print two given words in dictionary order

print("Enter two words:\n")
a,b=input(),input()
print(b,a if a>b else a,b)