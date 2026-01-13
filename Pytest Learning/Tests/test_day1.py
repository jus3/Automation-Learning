
"""
Install Pytest
pip install pytest

Check Pytest Version
pytest --version
"""

# ------------------------------------------

"""
Project Structure

pytest-learning/
│
├── tests/
│   └── test_sample.py
│
└── README.md

Pytest auto-discovers:

Files starting with test_
&
Functions starting with test_
"""

# ------------------------------------------

"""
Run all tests
pytest

Verbose output
pytest -v

Show print statements
pytest -s

Select a Particular Test in Exectuion
pytest -k

Example:
1) pytest -k addition
2) pytest -k "addition or division"
3) pytest -k "not addition" 

"""

# ------------------------------------------


# def test_addition():
#     assert 2 + 3 == 5
#
# def test_subtraction():
#     assert 3 - 2 == 1
#
# # ------------------------------------------
#
# def test_string_check():
#     assert "Friend" in "Friends forever"
#
# def test_list_length():
#     data = [1, 2, 3]
#     assert len(data) == 3
#
# # ------------------------------------------
#
# def test_failure():
#     assert 5>10

# ------------------------------------------
# MAIN TASK

def test_addition():
    assert 1 + 2 == 3

def test_subtraction():
    assert 1 - 2 == 3

def test_multiplication():
    assert 2 * 3 == 6

def test_division():
    assert 2 / 3 == 6

def test_login_status():
    status_code = 401
    assert status_code == 200, "Login failed: Unauthorized access"
























