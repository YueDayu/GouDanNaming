from .pinyin import Pinyin
from .word import Word


class WordLibrary:
    def __init__(self):
        self.library = {}

    def load_from_file(self, path):
        with open(path) as infile:
            lines = infile.readlines()
            infile.close()
            for line in lines:
                tmp_word = Word()
                tmp_word.from_str(line)
                self.library[tmp_word.word] = tmp_word
        return True

    def save_to_file(self, path):
        with open(path, 'w') as outfile:
            for word in self.library:
                outfile.write(str(self.library[word]) + '\n')

    @property
    def data(self):
        return self.library
