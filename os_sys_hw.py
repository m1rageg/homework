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

if len(sys.argv)>4:
    print('len')
    sys.exit(2)
elif len(sys.argv) == 3:
    add(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    func_name = sys.argv[1]
    first = sys.argv[2]
    second = sys.argv[3]
    if func_name not in functions:
        print('not name')
        sys.exit(2)
    try:
        functions[func_name](first, second)
    except ValueError:
        print('value')
        sys.exit(2)
else:
    sys.exit(2)
