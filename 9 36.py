import re


class main():
    sost = 'A'
    dict_hurry = {
        'A': '2A'
    }
    dict_pose = {
        'A': '0B',
        'B': '4C',
        'F': '8D'
    }
    dict_split = {
        'A': '3C',
        'E': '7F'
    }
    dict_mask = {
        'A': '1F',
        'C': '5D',
        'D': '6E'
    }
    def hurry(self):
        temp = self.sost
        if temp in self.dict_hurry:
            self.sost = re.findall(r'[A-Z]', self.dict_hurry.get(temp, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_hurry.get(temp, "KeyError"))[0])
        else:
            raise KeyError
    def pose(self):
        temp = self.sost
        if temp in self.dict_pose:
            self.sost = re.findall(r'[A-Z]', self.dict_pose.get(temp, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_pose.get(temp, "KeyError"))[0])
        else:
            raise KeyError
    def split(self):
        temp = self.sost
        if temp in self.dict_split:
            self.sost = re.findall(r'[A-Z]', self.dict_split.get(temp, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_split.get(temp, "KeyError"))[0])
        else:
            raise KeyError
    def mask(self):
        temp = self.sost
        if temp in self.dict_mask:
            self.sost = re.findall(r'[A-Z]', self.dict_mask.get(temp, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_mask.get(temp, "KeyError"))[0])
        else:
            raise KeyError
o = main()

print(o.hurry()) # 2
print(o.hurry()) # 2
print(o.pose()) # 0
print(o.pose()) # 4
print(o.mask()) # 5
print(o.mask()) # 6
print(o.split()) # 7
#print(o.hurry()) # KeyError
print(o.pose()) # 8

    
