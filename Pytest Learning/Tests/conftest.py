import pytest

# @pytest.fixture(scope="session")
# def login_token():
#     print("\nLogin once per session")
#     return "fake-token-123"
#
# @pytest.fixture(scope="session")
# def login():
#     print("\nLogging in...")
#     user = {"username": "qa_user", "role": "admin"}
#     yield user
#     print("\nLogging out...")

# @pytest.fixture(scope="session")
# def login():
#     print("\nLogging in...")
#     user = {"username": "qa_user", "role": "admin"}
#     yield user
#     print("\nLogging out...")
#
# def test_dashboard_access(login):
#     assert login["role"] == "admin"


import pytest

@pytest.fixture(scope="session")
def login_session():
    print("\n[SESSION SETUP] Login once")
    token = "session-token-abc123"
    yield token
    print("\n[SESSION TEARDOWN] Logout once")
