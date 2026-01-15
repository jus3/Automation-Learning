import pytest

@pytest.fixture(scope="session")
def login_token():
    print("\nLogin once per session")
    return "fake-token-123"

@pytest.fixture(scope="session")
def login():
    print("\nLogging in...")
    user = {"username": "qa_user", "role": "admin"}
    yield user
    print("\nLogging out...")

