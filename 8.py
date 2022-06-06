import re


def main(x):
    slovar = {}
    x = re.findall('<data>(.*?)</data>', x)[0]
    x = re.findall('do val(.*?)end;', x)
    print (x)
    print (" ")
    for i in range(len(x)):
        temp_mass = re.split(r'\bis\b', x[i])
        name = re.findall(r'\w+', temp_mass[0])[0]
        cost = re.sub(r'\bq\b', '', temp_mass[1])
        cost = re.findall(r'\w+', cost)[0]
        slovar[name] = cost
    return slovar

print(main("<data>do val `enma is q(leenat_880); end;do val `encebi_787 is q(ininge); end; do val `atiar is q(isbi_721); end; do val `veon is q(laxeer_803);end;</data>"))
