

def main(x):
    H = x >> 30
    x = x - (H << 30)
    G = x >> 29
    x = x - (G << 29)
    F = x >> 25
    x = x - (F << 25)
    E = x >> 24
    x = x - (E << 24)
    D = x >> 11
    x = x - (D << 11)
    C = x >> 5
    x = x - (C << 5)
    B = x >> 1
    x = x - (B << 1)
    A = x
    return G + (B << 1) + (D << 5) + (H << 18) + (F << 20) + (A << 24) + (E << 25) + (C << 26)

print (hex(main(0x1e8630ff)))
