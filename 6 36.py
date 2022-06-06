

def main(x):
    if x[2]==2005:
        if x[0]=='P4':
            if x[1]==1991:
                return 0
            elif x[1]==1957:
                return 1
            else:
                return 2
        elif x[0]=='METAL':
            return 3
        else:
            return 4
    else:
        if x[3]==2004:
            return 5
        elif x[3]==1973:
            if x[1]==1991:
                return 6
            elif x[1]==1957:
                return 7
            else:
                return 8
        else:
            if x[0]=='P4':
                return 9
            elif x[0]=='METAL':
                return 10
            else:
                return 11

print(main(['P4', 1957, 2005, 2004]))
