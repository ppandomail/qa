import pytest

def make_a_dict(a, b):
    operation = a + b
    return {'a': a, 'b': b, 'result': operation}

def test_make_a_dict():
    actual = make_a_dict(2, 3)
    expected = {'a': 2, 'b': 3, 'result': 5}
    assert actual == expected
