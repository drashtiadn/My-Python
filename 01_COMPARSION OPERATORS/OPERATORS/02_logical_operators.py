# Logical Operators
a = 1 < 2 < 3
print(a)

# and (both should be true)
b = 1 < 3 > 2
print(b)
b = (4==4) and (4!=4)
print(b)

# or (one of them should be true)
c = (123>132) or (2>23)
print(c)
c =(22<=30) or (56<6)
print(c)

# not (opposite)
d = not (1==100)
print(d)
d = not(1==1)
print(d)