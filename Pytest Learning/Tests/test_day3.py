import pytest

@pytest.mark.parametrize("user", ["qa", "123456"])
@pytest.mark.smoke

def test_login(user):
    assert user in ["qa", "123456"]


@pytest.mark.parametrize("client", ["admin", "12345678"])
@pytest.mark.regression

def test_client(client):
    assert client in ["admin", "12345678"]

@pytest.mark.parametrize("hacker", ["GODword", "852654"])
@pytest.mark.xfail(reason="He is Hacker")

def test_hacker(hacker):
    assert hacker not in ["GODword", "852654"]

