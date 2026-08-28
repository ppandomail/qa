import pytest

def some_calculation(a, b):
    return a + b

@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (3, 3, 6), (3, -2, 1)])
def test_some_calculation(a, b, expected):
    assert some_calculation(a, b) == expected
