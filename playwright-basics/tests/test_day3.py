import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    yield page
    page.close()

def test_valid_login(page):

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")

    expect(page.locator(":text-is('Login')")).to_be_visible()
    page.get_by_text("Login", exact=True).click()


    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()

    expect(page.locator("h2")).to_have_text("Secure Area")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    expect(page.get_by_text("Powered by Elemental Selenium")).to_be_visible()

def test_invalid_login(page):

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")

    page.get_by_text("Login").first.click()




