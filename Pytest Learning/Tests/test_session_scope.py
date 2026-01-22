def test_profile_access(login_session):
    assert "token" in login_session

def test_settings_access(login_session):
    assert login_session.startswith("session")
