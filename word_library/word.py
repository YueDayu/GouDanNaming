from typing import List
from .pinyin import Pinyin


class Word:
    def __init__(self, m_word="", stroke_num=0, freq_sort=0, pinyin: List[Pinyin] = None, parts="", english_meaning=""):
        self.word = m_word
        self.stroke_num = stroke_num
        self.freq_sort = freq_sort
        self.parts = parts
        if pinyin:
            self.pinyin = pinyin
        else:
            self.pinyin = []
        self.english_meaning = english_meaning

    def __str__(self):
        return self.word + " " + str(self.stroke_num) + " " + str(self.freq_sort) + " " + "/".join(
            map(str, self.pinyin)) + " " + self.parts + " " + self.english_meaning

    def from_str(self, word_line: str):
        parts = word_line.strip().split()
        if len(parts) < 5:
            return False
        self.word = parts[0]
        self.stroke_num = int(parts[1])
        self.freq_sort = int(parts[2])
        pinyin_parts = parts[3].split('/')
        for pinyin_str in pinyin_parts:
            self.pinyin.append(Pinyin(pinyin_str))
        self.parts = parts[4]
        if len(parts) > 5:
            self.english_meaning = ' '.join(parts[5:])
        return True


if __name__ == '__main__':
    word = Word("t", 2, 3, [Pinyin("zhi1"), Pinyin("chi2"), Pinyin("de")], "t", "test 1 2 3")
    print(word)
    new_word = Word()
    new_word.from_str(str(word))
    print(new_word)
