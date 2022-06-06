import re


class main():
    now_letter = 'A'
    dict_forge = {
        'A': '1A',
        'F': '8C',
        'H': '11E'
    }
    dict_cast = {
        'A': '0B',
        'E': '6A',
        'B': '2C'
    }
    dict_open = {
        'C': '3D',
        'D': '4E',
        'E': '5F',
        'G': '9H'
    }
    dict_crawl = {
        'G': '10B',
        'F': '7G'
    }

    def forge(self):
        temp_forge = self.now_letter
        if temp_forge in self.dict_forge:
            self.now_letter = re.findall(r'[A-Z]', self.dict_forge.get(
                temp_forge, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_forge.get(
                temp_forge, "KeyError"))[0])
        else:
            raise KeyError

    def cast(self):
        temp_cast = self.now_letter
        if temp_cast in self.dict_cast:
            self.now_letter = re.findall(r'[A-Z]', self.dict_cast.get(
                temp_cast, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_cast.get(
                temp_cast, "KeyError"))[0])
        else:
            raise KeyError

    def open(self):
        temp_open = self.now_letter
        if temp_open in self.dict_open:
            self.now_letter = re.findall(r'[A-Z]', self.dict_open.get(
                temp_open, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_open.get(
                temp_open, "KeyError"))[0])
        else:
            raise KeyError

    def crawl(self):
        temp_crawl = self.now_letter
        if temp_crawl in self.dict_crawl:
            self.now_letter = re.findall(r'[A-Z]', self.dict_crawl.get(
                temp_crawl, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_crawl.get(
                temp_crawl, "KeyError"))[0])
        else:
            raise KeyError
