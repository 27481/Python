# dict Comprenhension


#! utkarsh={key-Epression : data-expression for v in seq}
#           becomes (key) : becomes (data-value)
#! So for each iteration of the loop it will generate one key-value element for the dict


utkarsh={e:e**2 for e in range(1,6)}
print(utkarsh)
