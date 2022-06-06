def main(x):
    d = x >> 31
    x = x - (d << 31)
    c = x >> 17
    x = x - (c << 17)
    b = x >> 10
    a = x - (b << 10)
    x = (c << 18) + (a << 8) + (b << 1) + d
    return x

print(hex(main(0xfcbcf54c)))
