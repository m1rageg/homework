from dataclasses import dataclass

import pytest


@dataclass
class Car:
    name: str
    model: str
    quantity_of_doors: int
    type_of_gas: str


def test_a_pos_storage(storage_for_tests):
    audi = Car('Audi', 'Q7', 4, '95')
    mercedes = Car('Mercedes', 'E500', 4, '95')
    cars_storage = storage_for_tests
    cars_storage.add_table('Car', Car)
    cars_storage.add_to_table('Car', mercedes, audi)
    cars_storage.get_from_table('Car')


def test_b1_neg_storage_cannot_override_table(storage_for_tests):
    with pytest.raises(ValueError):
        storage_for_tests.add_table('Car', Car)


def test_b2_neg_storage_no_such_a_table(storage_for_tests):
    with pytest.raises(ValueError):
        storage_for_tests.add_to_table('Bicycle', Car)


def test_b3_neg_storage_no_such_a_table(storage_for_tests):
    with pytest.raises(ValueError):
        storage_for_tests.get_from_table('Plane')


def test_b4_neg_storage_no_such_a_table_invalid_data(storage_for_tests):
    with pytest.raises(ValueError):
        storage_for_tests.add_to_table('Car', 4)
