import pytest

@pytest.mark.finished
def test_01():
    assert True

@pytest.mark.unfinished
def test_02():
    assert False

def test_03():
    assert (1, 2, 3) == (1, 2, 3)
