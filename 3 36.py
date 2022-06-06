import math


def main(n):
    if n==0:
        return 0.27
    f = main(n-1)
    return f**2 - 1 - math.atan(f)
    
print (main(4))
    
