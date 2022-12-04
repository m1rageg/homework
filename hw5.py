def grep(pattern):
    while True:
        line = yield
        if pattern in line:
            yield line


def flatten(arr):
    for i in sum(arr, []):
        yield i


WORDS = {}


def add_word(word):
    def inner(word, tmp=''):
        if word == []:
            return {'TERM': tmp}
        else:
            key, *word = word
            return {key: inner(word, tmp + key)}

    if not WORDS:
        WORDS[word[0]] = inner(word)[word[0]]
    else:
        tmp = WORDS
        for k in word[:-1]:
            tmp = tmp[k]
        tmp[word[-1]] = {**tmp[word[-1]], **{'TERM': word}}


def get_words(char):
    res = set()
    tmp = WORDS
    while isinstance(tmp, dict):
        if 'TERM' in tmp and tmp['TERM'].startswith(char):
            res.add(tmp['TERM'])
        _, tmp = list(tmp.items())[0]
    return set(res) or []

