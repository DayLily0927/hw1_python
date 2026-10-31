x,y,z=map(int,input().split())
if x>y:
    m=x
    x=y
    y=m
if x>z :
    m=x
    x=z
    z=m
if y>z:
    m=y
    y=z
    z=m
print(x,y,z)