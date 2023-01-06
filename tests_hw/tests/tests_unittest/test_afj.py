import unittest
import os
import json
from things_to_test_hw import add_from_json


class TestAFJ(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        data = {'a': 3, 'b': -7, 'c': 0}
        with open('some.json', 'w') as file:
            json.dump(data, file)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('some.json')

    def test_pos(self):
        self.assertEqual(add_from_json('some.json', ('a', 'b', 'c')), -4)

    def test_neg(self):
        with self.assertRaises(FileNotFoundError) as exc:
            add_from_json('other.json', ('a', 'b', 'c'))

        self.assertEqual(exc.exception.args, (2, 'No such file or directory',))
        with self.assertRaises(KeyError) as exc:
            add_from_json('some.json', ('a', 'b', 'd'))

        self.assertEqual(exc.exception.args, ('d',))
