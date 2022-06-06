import re

def main(x):
    slov = {}
    x = re.sub(r'declare', '', x)
    x = re.findall('do(.*?)done', x)[0]
    x = re.findall('\\(\\((.*?)\\)\\)', x)
    for i in x:
        i = re.split(r':=', i)
        name = re.findall('\'(.*?)\'', i[0])[0]
        data = re.findall('\w+', i[1])[0]
        slov[name] = data
    return slov
print(main("do (( declare 'rebiso' :=beza; )) (( declare 'tizaqu_162' :=enle_302;)) ((declare'ceerge_37':=bebies; ))done"))
