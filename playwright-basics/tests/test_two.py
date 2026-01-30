from playwright.sync_api import Page, expect

def test_open_playwright_site(page: Page):
    page.goto("https://google.com")
    expect(page).to_have_title("Google")#Will check Title of the Page

  # page.get_by_text("Get started").click()
    page.get_by_title("Google")
    page.get_by_role("button", name="Google apps").hover()
    page.get_by_role("combobox", name="Search").fill("hello world")
    page.get_by_label("Google Search").first.click()
  # page.get_by_test_id("login-btnI").first.click()
