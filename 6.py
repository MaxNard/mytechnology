def main(x):
    if (x[2] == 'CSV'):
        return lv1(x)
    elif (x[2] == 'SVG'):
        return lv4(x)
    else:
        return 9


def lv1(x):
    if (x[0] == 'GLYPH'):
        return lv2(x)
    else:
        return lv3(x)


def lv2(x):
    if (x[3] == 1962):
        return 0
    elif (x[3] == 1977):
        return 1
    else:
        return 2


def lv3(x):
    if (x[3] == 1962):
        return 3
    elif (x[3] == 1977):
        return 4
    else:
        return 5


def lv4(x):
    if (x[1] == 'NIX'):
        return lv5(x)
    else:
        return 8


def lv5(x):
    if (x[0] == 'GLYPH'):
        return 6
    else:
        return 7


print(main(['GLYPH', 'NIX', 'CSV', 1962]))
