import re


def main(x):
    slovar = {}
    x = re.findall('do(.*?)od', x)[0]
    x = re.findall('.do local(.*?).end.', x)
    for i in range(len(x)):
        temp_mass = re.split(':', x[i])
        name = re.findall(r'\w+', temp_mass[0])[0]
        cost = re.findall('-?[0-9]+', temp_mass[1])
        slovar[name] = cost
    return slovar

print(main("do .do local'vege': #( #-4537 #-2322). .end. .do local 'xegeer' :#(#-1214 #-3346 #6951 #-892 ). .end. od"))
