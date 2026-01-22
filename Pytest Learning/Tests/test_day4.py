import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# def test_login():
#     logger.info("Starting login test")
#     username = "admin"
#     password = "1234"
#
#     logger.debug(f"Username used: {username}")
#     assert username == "admin", "Username mismatch"
#     assert password == "1234", "Password mismatch"
#     logger.info("Login test passed")
#
#
# def test_addition():
#     result = 2 + 2
#     assert result == 4, f"Expected sum to be 5, but got {result}"
#
# def test_subtraction():
#     result = 2 - 2
#     assert result == 0, f"Expected sum to be 0, but got {result}"
#
# def test_checkout_flow():
#     logger.info("Step 1: Add item to cart")
#     logger.info("Step 2: Proceed to checkout")
#     logger.info("Step 3: Confirm payment")
#     assert True

# Task

def test_login():
    logger.info("Starting login test")
    username = "het"
    password = "123456789"

    logger.debug(f"Username used: {username}")
    assert username == "het", "Username mismatch"
    assert password == "12345678", "Password mismatch"
    logger.info("Login test passed")

def test_click():
    logger.info("Starting click test")
    tabname = "Submit 1"

    logger.debug(f"Tabname used: {tabname}")
    assert tabname == "Submit", "Tabname mismatch"
    logger.info("Click test passed")

def test_mainpage():
    logger.info("Starting dashboard test")
    dashboard = "Hello"

    logger.debug(f"Dashboard used: {dashboard}")
    assert dashboard == "Hello", "Dashboard mismatch"
    logger.info("Dashboard test passed")


