# a
def biggest_number():
    print('1) Функция выводит большее число.')
    first = input('Type 1st number: ')
    second = input('Type 2nd number: ')
    if first > second:
        return first
    else:
        return second


biggest_number()


# b
def smallest_number():
    print('2) Функция выводит меньшее число.')
    first = input('Type 1st number: ')
    second = input('Type 2nd number: ')
    third = input('Type 3rd number: ')
    if first < second and first < third:
        return first
    elif second < first and second < third:
        return second
    else:
        return third


smallest_number()


# c
def module_of_number():
    print('3)Функция выводит модуль числа.')
    number = input('Type a number: ')
    return abs(int(number))


module_of_number()


# d
def sum_of_numbers():
    print('4)Функция выводит сумму двух чисел.')
    first = input('Type 1st number: ')
    second = input('Type 2nd number: ')
    result = int(first) + int(second)
    print('Sum of your numbers is: ', result)


sum_of_numbers()


# e
def is_positive_number():
    print('5)Функция выводит информацию про знак числа.')
    number = input('Type a number: ')
    if int(number) > 0:
        print('Positive')
    elif int(number) == 0:
        print('Zero, neither negative nor positive')
    else:
        print('Negative')


is_positive_number()
