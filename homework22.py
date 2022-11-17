import random


def retry(attempts=5, desired_value=None):

    def decorator(func):

        def wrapper(*args, **kwargs):

            if args:
                _ = args
            if kwargs.get('size') is not None:
                kwargs.get('size')
            if isinstance(desired_value, int):
                for name in range(attempts):
                    name = func(*args, **kwargs)
                    if name == desired_value:
                        return name
            elif isinstance(desired_value, list):
                result = []
                for name in range(attempts):
                    name = func(*args, **kwargs)
                    result.append(name)
                return result

            return f'Не удалось получить желаемое значение с {attempts} попыток'

        return wrapper

    return decorator


@retry(attempts=5, desired_value=4)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


# examples of function usages
print(get_random_value())
print(get_random_values([1, 2, 3, 4]))
print(get_random_values([1, 2, 3, 4], 3))
print(get_random_values([1, 2, 3, 4], size=1))


# Квадраты из звёздочек
def print_square(size, k=0):
    if k in (0, size - 1):
        print(size * '*')
    else:
        print('*' + ' ' * (size - 2) + '*')
    if k < size - 1:
        print_square(size, k + 1)


print_square(1)
