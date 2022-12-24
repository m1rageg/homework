import sys

def add(first, second):
    print(int(first) + int(second))


def subtraction(first, second):
    print(int(first) - int(second))


def divide(first, second):
    print(int(first)/int(second))


def multiply(first, second):
    print(int(first)*int(second))


functions = {'add': add,
             'subtraction': subtraction,
             'divide': divide,
             'multiply': multiply}

try:
    if len(sys.argv) == 3:
        add(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[1].startswith('FUNCTION'):
            function = sys.argv[1][9:]
            a = sys.argv[2]
            b = sys.argv[3]
            functions[function](a, b)
    else:
        sys.exit(2)
except ValueError and KeyError:
    sys.exit(2)