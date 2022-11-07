# a
NUMBER_ONE = 2
NUMBER_TWO = 3


def biggest_number(number_one, number_two):
    if number_one > number_two:
        return number_one
    if number_two > number_one:
        return number_two
    return None


biggest_number(NUMBER_ONE, NUMBER_TWO)


# b
FIRST = 4
SECOND = 2
THIRD = 3


def smallest_number(first, second, third):
    if first < second and first < third:
        return first
    if second < first and second < third:
        return second
    if third < first and third < second:
        return third
    return None


smallest_number(FIRST, SECOND, THIRD)


# c
NUMBER = -3


def module_of_number(number):
    return abs(int(number))


module_of_number(NUMBER)


# d
FIRST_NUMBER = 2
SECOND_NUMBER = 4


def sum_of_numbers(first_number, second_number):
    result = first_number + second_number
    print('Sum of your numbers is: ', result)


sum_of_numbers(FIRST_NUMBER, SECOND_NUMBER)


# e
input_number = input('Type a number: ')


def is_positive_number(number):
    if int(number) > 0:
        print('Positive')
    elif int(number) == 0:
        print('Zero, neither negative nor positive')
    else:
        print('Negative')


is_positive_number(input_number)
