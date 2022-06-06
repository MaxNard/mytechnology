def main(x):
    a = (((87*x - 49*x**2)**2+98)/(x**7))**(0.5)
    b = 62*(x**2 - 1 - (x**3)/47)**2
    return a + b
print (main(0.27))
