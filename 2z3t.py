a=5
c='H'
d=range(6)
r=range(3)
b=23
for i in range(a):
    print((c*i).rjust(a-1)+c+(c*i).ljust(a-1))

for i in d:
    print((c*0).rjust(2)+(a*c).ljust(2),(c*a).rjust(17))

for i in r:
    print ((c*0).rjust(2)+(23*c))
    
for i in d:
    print((c*0).rjust(2)+(a*c).ljust(2),(c*a).rjust(17))
    
for i in range(4,-1,-1):
    print((c*i).rjust(22)+c+(c*i).ljust(a-1))