from .word_library import WordLibrary
from .word import Word
from .pinyin import Pinyin


def load_standard_chinese_words(filepath):
    words = set()
    with open(filepath) as infile:
        lines = infile.readlines()
        infile.close()
        for line in lines:
            w = line.strip()
            if len(w) > 0:
                words.add(w)
    return words


def load_chinese_stroke_num(filepath, filter_set):
    words = {}
    with open(filepath) as infile:
        lines = infile.readlines()
        infile.close()
        for line in lines:
            parts = line.strip().split()
            if parts[0] in filter_set:
                words[parts[0]] = (int(parts[6]), parts[7])
    return words


def build_basic_word_library(filepath, stork_data):
    words = WordLibrary()
    with open(filepath) as infile:
        lines = infile.readlines()
        infile.close()
        for line in lines:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            if parts[1] in stork_data:
                it = stork_data[parts[1]]
                pinyin_parts = parts[4].split('/')
                pinyin = []
                for pinyin_str in pinyin_parts:
                    pinyin.append(Pinyin(pinyin_str))
                meaning = ''
                if len(parts) > 5:
                    meaning = ' '.join(parts[5:])
                words.data[parts[1]] = Word(parts[1], it[0], int(parts[0]), pinyin, it[1], meaning)
    return words


if __name__ == '__main__':
    basic_word = load_standard_chinese_words("word_library/data/the_table_of_general_standard_chinese_character.txt")
    print("standard words size: ", len(basic_word))
    word_stroke = load_chinese_stroke_num("word_library/data/chinese_unicode_table.txt", basic_word)
    print("word stroke num: ", len(word_stroke))
    wl = build_basic_word_library("word_library/data/CharFreq.txt", word_stroke)
    print("basic word library size: ", len(wl.data))
    wl.save_to_file("word_library/output/basic_word_library.txt")
