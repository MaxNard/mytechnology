import math


def main(x):
    sum = 0
    for i in range(1, len(x)+1):
        a = (x[math.ceil(i/3) - 1])**2
        b = 6*(x[math.ceil(i/3) - 1])**3
        c = x[math.ceil(i/3) - 1]
        sum += (math.floor(a + b + c))**7
    return sum*25/17
print (main([-0.84, -0.89, 0.08, -0.85, -0.75, -0.09, -0.23]))
    
