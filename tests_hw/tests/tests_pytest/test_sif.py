import pytest
import os
from things_to_test_hw import search_in_file


def test_neg_search_in_file():
    with pytest.raises(FileNotFoundError):
        search_in_file('same', 'first')


@pytest.mark.parametrize(
    'pattern, expected_result', (('first', ['first_line\n']),('sec', ['second_line\n']),('eleventh', []),('twelfth', []), ('', ['first_line\n', 'second_line\n', 'third_line\n'])),)
def test_pos_search_in_file(pattern, expected_result, file_for_test):
    result = search_in_file('some', pattern)
    assert result == expected_result
    os.remove('some')
