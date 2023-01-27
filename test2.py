import math
def eqn():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/ 2*a
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/ 2*a 
        print('x1 =',x1)
        print('x2 =',x2)
    elif delta == 0:
        print('x =', -b/2*a)
    else:
        print('delta < 0  ==>  x = NONE')
eqn()

