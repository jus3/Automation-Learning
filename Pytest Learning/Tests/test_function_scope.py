import pytest

@pytest.fixture
def user_data():
    print("\n[SETUP] Create user data")
    data = {"username": "qa_user", "active": True}
    yield data
    print("\n[TEARDOWN] Cleanup user data")

def test_user_is_active(user_data):
    assert user_data["active"] is True

def test_username_exists(user_data):
    assert user_data["username"] == "qa_user"


"""
Fixture runs twice (once per test).
This is function scope.
"""