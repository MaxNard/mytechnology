import math


def main(x, y):
    sum = 0
    n = len(x)
    for i in range(1, n+1):
        a = 34*(y[n - math.ceil(i/2)])**3
        b = 86*(y[n - math.ceil(i/2)])**2
        sum += (a - b - x[math.ceil(i/2) - 1])**5
    return sum*86

print(main([-0.22, 0.88, 0.94, 0.26, 0.37, 0.63, -0.96], [-0.16, 0.43, -0.13, 0.05, 0.11, 0.35, -0.48]))
