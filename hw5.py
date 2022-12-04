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
    context = WORDS

    for letter in word:
        if letter not in context:
            context[letter] = {}
        context = context[letter]

    if 'TERM' not in context:
        context['TERM'] = word


def get_words(char):
    context = WORDS
    res = []

    for letter in char:
        if letter not in context:
            return res
        context = context[letter]

    iterable = iter(context.items())
    stack = [0]

    while len(stack) > 0:
        for key, value in iterable:
            if key == 'TERM':
                res.append(value)
                if len(res) == 10:
                    return res
            else:
                stack.append(iterable)
                iterable = iter(value.items())
                break
        else:
            iterable = stack.pop()

    return res
