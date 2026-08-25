import pytest

@pytest.fixture()
def db():
    print('Connection successful')
    yield
    print('Connection closed')

def search_user(user_id):
    d = {'001': 'ppando', '002': 'otrouser'}
    return d[user_id]

def test_search(db):
    assert search_user('001') == 'ppando'

def test_search2(db):
    assert search_user('002') == 'otrouser'
