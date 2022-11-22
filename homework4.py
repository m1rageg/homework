LONG_TEXT = """asdlknfasldkmfasdfasdf"""
a = []


def add_word(word):
    a.append(word)


def get_words(char):
    trent = []
    for i in sorted(a):
        if char in i:
            trent.append(i)
    return trent[:5]


def crop_text(length):
    for i in range(0, len(LONG_TEXT), length):
        yield LONG_TEXT[i:i + length]
