import pytest
import requests

def test_edad_homero():
    response = requests.get('https://thesimpsonsapi.com/api/characters/1')
    edad_actual = response.json()['age']
    assert 39 == edad_actual
