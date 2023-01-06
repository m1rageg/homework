from dataclasses import dataclass
import unittest
from things_to_test_hw import Storage


@dataclass()
class Car:
    name: str
    model: str
    quantity_of_doors: int
    type_of_gas: str


class TestStorage(unittest.TestCase):
    def setUp(self) -> None:
        self.car_storage = Storage()
        self.audi = Car("Audi", 'Q7', 4, '95')
        self.mercedes = Car('Mercedes', 'E500', 4, '95')
        self.car_storage.add_table('Car', Car)

    def test_pos(self):
        self.car_storage.add_to_table('Car', self.mercedes, self.audi)
        self.assertEqual(self.car_storage.get_from_table('Car'),
                         [Car(name='Mercedes', model='E500', quantity_of_doors=4, type_of_gas='95'),
                          Car(name='Audi', model='Q7', quantity_of_doors=4, type_of_gas='95')])

    def test_neg(self):
        with self.assertRaises(ValueError) as exc:
            self.car_storage.add_table('Car', Car)

        self.assertEqual(exc.exception.args, ('cannot override table',))

        with self.assertRaises(ValueError) as exc:
            self.car_storage.add_to_table('Bicycle', Car)

        self.assertEqual(exc.exception.args, ('no such a table',))

        with self.assertRaises(ValueError) as exc:
            self.car_storage.get_from_table('Plane')

        self.assertEqual(exc.exception.args, ('no such a table',))

        with self.assertRaises(ValueError) as exc:
            self.car_storage.add_to_table('Car', 4)

        self.assertEqual(exc.exception.args, ('invalid data',))
