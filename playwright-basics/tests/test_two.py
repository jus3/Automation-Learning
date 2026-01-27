from playwright.sync_api import Page, expect

def test_open_playwright_site(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")#Will check Title of the Page

    # page.get_by_text("Get started").click()

    page.get_by_role("button", name="Get started").click()
    # page.get_by_role('link', name = 'Get started').click()
    