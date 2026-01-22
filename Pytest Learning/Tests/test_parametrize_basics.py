import pytest
#
# @pytest.mark.parametrize("a, b, expected", [
#     (1, 2, 3),
#     (2, 3, 5),
#     (10, 5, 15),
#     (11, 13, 24)
# ])
#
# def test_addition(a, b, expected):
#     assert a + b == expected
#
# @pytest.mark.parametrize("a, b, expected", [
#     (3, 2, 1),
#     (8, 3, 5),
#     (20, 5, 15),
#     (37, 13, 24)
# ])
#
# def test_subtraction(a, b, expected):
#     assert a - b == expected

# @pytest.mark.parametrize("username, password, expected", [
#     ("admin", "admin123", True),
#     ("user", "wrongpass", False),
#     ("", "", False)
# ])
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_login(username, password, expected):
#     result = (username == "admin" and password == "admin123")
#     assert result == expected
#
#
# @pytest.mark.smoke
# def test_smoke_login():
#     assert True
#
# @pytest.mark.regression
# def test_regression_profile():
#     assert True
#
# """
# To Execute
# pytest test_parametrize_basics.py -v -s -m regression
# pytest test_parametrize_basics.py -v -s -m smoke
# """
#
# @pytest.mark.skip(reason="Feature not implemented")
# def test_future_feature():
#     assert False

# @pytest.mark.xfail(reason="Known defect in login API")
# def test_known_bug():
#     assert 1 == 2

@pytest.mark.smoke
@pytest.mark.parametrize("user", ["admin", "superuser"])
@pytest.mark.parametrize("password", ["Pass", "Word123"])

def test_smoke_users(user, password):
    assert user in ["admin", "superuser"]
    assert password in ["Pass", "Word123"]
