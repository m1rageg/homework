import pytest
import json
from things_to_test_hw import Storage


@pytest.fixture()
def file_for_test():
    lines = ['first_line\n', 'second_line\n', 'third_line\n']
    with open('some', 'w') as file:
        file.writelines(lines)


@pytest.fixture()
def json_for_test():
    data = {'a': 3, 'b': -7, 'c': 0}
    with open('some.json', 'w') as file:
        json.dump(data, file)


@pytest.fixture(scope='module')
def storage_for_tests():
    car_storage = Storage()
    return car_storage

