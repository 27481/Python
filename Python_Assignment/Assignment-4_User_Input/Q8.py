# Write a python script to calcuate simple interest 

print("To calculate simple interest you have to give Princple value , Rate and Time PRT")

principle=int(input("Enter the principle value:\n"))
rate=int(input("Enter the rate of the value:\n"))
time=int(input("Enter the time duration of the interest:\n"))


principle_interest=(principle*rate*time)/100;


print(principle_interest)