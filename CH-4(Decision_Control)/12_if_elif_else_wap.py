""" 
WAP to print grade obtained in a test. Take marks obtained from user and display the grade 

90 <  marks <= 100 A
80 <  marks <= 90 B
70 <  marks <= 80 C
60 <  marks <= 70 D
50 <= marks <= 60 E
below 50          F
"""


marks=int(input("Enter the marks:\n"));

if 90<marks<=100: print("A");
elif 80<marks<=90: print("B");
elif 70<marks<=80: print("C");
elif 60<marks<=70: print("D");
elif 50<=marks<=60: print("E");
else: print("F");
