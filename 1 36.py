import math


def main(n, x, b, a, y):
    buf = 0
    buf2 = 0
    for i in range (1,n+1):
        buf = buf + (1 - (i**2+1)**3 - math.exp(x))
    for j in range (1,a+1):
        for c in range (1,b+1):
            buf2 = buf2 + 68*y**4 - (93*c**2)**6 - 41*(math.sin(j))**3
    return buf - buf2
    
print (main(8, 0.16, 2, 4, -0.58))
    
