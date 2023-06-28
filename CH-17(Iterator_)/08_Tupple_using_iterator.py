# tuple using iterator 

t={2,1,0,0,5,4,1,5,3,0,0,5,1}
it=iter(t)

while (True):
    try:
      print(next(it),end='')
    expect StopIteration:
        break

print("Last line of the Program:\n")