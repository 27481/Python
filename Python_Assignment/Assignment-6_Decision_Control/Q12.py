# Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part


x=complex(input("Enter a complex number:\n"))
print(x.real) if (x.real>x.imag) else print(x.imag)

