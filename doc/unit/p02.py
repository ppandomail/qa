import pytest

def increment_one(numero):
    return numero + 1

def test_increment():
    assert increment_one(1) == 2
