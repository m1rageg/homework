# a
def biggest_number():
    print('1) Функция выводит большее число.')
    a = input('Type 1st number: ')
    b = input('Type 2nd number: ')
    if a > b:
        return a
    else:
        return b


biggest_number()


# b
def smallest_number():
    print('2) Функция выводит меньшее число.')
    a = input('Type 1st number: ')
    b = input('Type 2nd number: ')
    c = input('Type 3rd number: ')
    if a < b and a < c:
        print('The smallest number is: ', a)
    elif b < a and b < c:
        print('The smallest number is: ', b)
    else:
        print('The smallest number is: ', c)


smallest_number()


# c
def module_of_number():
    print('3)Функция выводит модуль числа.')
    a = input('Type a number: ')
    print('Module of your number is: ', abs(int(a)))


module_of_number()


# d
def sum_of_numbers():
    print('4)Функция выводит сумму двух чисел.')
    a = input('Type 1st number: ')
    b = input('Type 2nd number: ')
    c = int(a) + int(b)
    print('Sum of your numbers is: ', c)


sum_of_numbers()


# e
def is_positive_number():
    print('5)Функция выводит информацию про знак числа.')
    a = input('Type a number: ')
    if int(a) > 0:
        print('Positive')
    elif int(a) == 0:
        print('Zero, neither negative nor positive')
    else:
        print('Negative')


is_positive_number()

