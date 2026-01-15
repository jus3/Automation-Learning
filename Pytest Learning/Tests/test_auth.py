def test_access(login_token):
    assert login_token.startswith("fake")

def test_dashboard_access(login):
    assert login["role"] == "admin"
