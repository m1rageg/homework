import unittest
import os
from things_to_test_hw import search_in_file


class TestSIF(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        lines = ['first_line\n', 'second_line\n', 'third_line\n']
        with open('some', 'w') as file:
            file.writelines(lines)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('some')

    def test_pos(self):
        self.assertEqual(search_in_file('some', 'first'), ['first_line\n'])
        self.assertEqual(search_in_file('some', 'sec'), ['second_line\n'])
        self.assertEqual(search_in_file('some', 'seventh'), [])
        self.assertEqual(search_in_file('some', ''), ['first_line\n', 'second_line\n', 'third_line\n'])

    def test_neg(self):
        with self.assertRaises(FileNotFoundError) as exc:
            search_in_file('same', 'first')

        self.assertEqual(exc.exception.args, (2, 'No such file or directory'))
