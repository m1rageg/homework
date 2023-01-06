import pytest
import os
from things_to_test_hw import add_from_json


def test_neg_add_from_json(json_for_test):
    with pytest.raises(FileNotFoundError):
        add_from_json('other.json',  ('a', 'b', 'c'))
    with pytest.raises(KeyError):
        add_from_json('some.json',  ('a', 'b', 'd'))
    os.remove('some.json')


def test_pos_add_from_json(json_for_test):
    add_from_json('some.json',  ('a', 'b', 'c'))
    os.remove('some.json')
