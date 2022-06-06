import re


class main():
    now_letter = 'A'
    dict_stop = {
        'A': '0B'
    }
    dict_shade = {
        'A': '2C',
        'B': '4C',
        'C': '5D',
        'D': '6E',
        'E': '7F',
    }
    dict_spin = {
        'A': '1D',
        'E': '8E'
    }
    dict_stash = {
        'A': '3G',
        'F': '9G'
    }

    def stop(self):
        temp_stop = self.now_letter
        if temp_stop in self.dict_stop:
            self.now_letter = re.findall(r'[A-Z]', self.dict_stop.get(
                temp_stop, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_stop.get(
                temp_stop, "KeyError"))[0])
        else:
            raise KeyError

    def shade(self):
        temp_shade = self.now_letter
        if temp_shade in self.dict_shade:
            self.now_letter = re.findall(r'[A-Z]', self.dict_shade.get(
                temp_shade, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_shade.get(
                temp_shade, "KeyError"))[0])
        else:
            raise KeyError

    def stash(self):
        temp_stash = self.now_letter
        if temp_stash in self.dict_stash:
            self.now_letter = re.findall(r'[A-Z]', self.dict_stash.get(
                temp_stash, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_stash.get(
                temp_stash, "KeyError"))[0])
        else:
            raise KeyError

    def spin(self):
        temp_spin = self.now_letter
        if temp_spin in self.dict_spin:
            self.now_letter = re.findall(r'[A-Z]', self.dict_spin.get(
                temp_spin, "KeyError"))[0]
            return int(re.findall(r'[0-9]+', self.dict_spin.get(
                temp_spin, "KeyError"))[0])
        else:
            raise KeyError
