import pytest

@pytest.mark.parametrize("number", [1, 2, -1, 3])
def test_is_positive(number):
    assert number > 0
