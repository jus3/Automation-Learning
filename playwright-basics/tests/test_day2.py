from playwright.sync_api import Page, expect

def test_valid_login(page: Page):

    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")

    page.get_by_text("Login", exact=True).click()

    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()


def test_invalid_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword")

    page.get_by_text("Login").click()

    expect(page.get_by_title("You logged into a secure area!")).to_be_visible()