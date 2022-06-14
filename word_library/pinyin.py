class Pinyin:
    initial_table = {'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z',
                     'c', 's', 'y', 'w'}

    def __init__(self, raw_pinyin=""):
        self.tone = 0
        self.initial = ''
        self.final = ''
        if len(raw_pinyin) > 0:
            self.from_str(raw_pinyin)

    def __str__(self):
        return self.initial + self.final + (str(self.tone) if self.tone > 0 else '')

    def from_str(self, raw_pinyin):
        if len(raw_pinyin) > 2 and raw_pinyin[:2] in Pinyin.initial_table:
            self.initial = raw_pinyin[:2]
            raw_pinyin = raw_pinyin[2:]
        elif len(raw_pinyin) > 1 and raw_pinyin[0] in Pinyin.initial_table:
            self.initial = raw_pinyin[0]
            raw_pinyin = raw_pinyin[1:]
        else:
            self.initial = ""
        if raw_pinyin[-1].isdigit():
            self.tone = int(raw_pinyin[-1])
            raw_pinyin = raw_pinyin[:-1]
        else:
            self.tone = 0
        self.final = raw_pinyin


# unittest
if __name__ == '__main__':
    pinyin = Pinyin("de")
    print("pinyin: ", pinyin, pinyin.initial, pinyin.final, pinyin.tone)
