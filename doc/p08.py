import pytest

@pytest.mark.parametrize('passwd', ['123456', 'abcdefdfs', 'as52345fasdf4'])
def test_password_length(passwd):
    assert len(passwd) >= 8
