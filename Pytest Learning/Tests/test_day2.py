import pytest

"""
What Is a Fixture?
A fixture is a reusable setup component that:

It Runs before a test and Can run after a test (teardown)
"""

#-----------------------------------------------------

# Task 1

# @pytest.fixture
# def saved_data():
#     print("\nSetup: create data")
#     return {"CompanyName": "IBM", "salary": "Good"}
#
# def test_data_status(saved_data):
#     assert saved_data["salary"] == "Good"
#
# def test_partner_name(saved_data):
#     assert saved_data["CompanyName"] == "IBM"

#-----------------------------------------------------

# Task 2
# Setup + Teardown Using yield

# @pytest.fixture
# def resource():
#     print("\nSetup: connect to resource")
#     yield "CONNECTED"
#     print("\nTeardown: disconnect resource")
#
# def test_resource(resource):
#     assert resource == "CONNECTED"

#-----------------------------------------------------

# Task 3

@pytest.fixture(scope="module")
def module_data():
    print("\nSetup once per module")
    return 100

