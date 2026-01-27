from playwright.sync_api import sync_playwright  #using SYNC Function
from playwright.sync_api import Page
from playwright.sync_api import expect

def test_navigate_to_main_page():  #Function
    with sync_playwright() as playwright:  #Starts Playwright Engine
        #for browser_type in ["chrome", "firefox", "Edge"]: #Not Compulsory it Loops multiple browsers but can be done in Config.ts
        browser=playwright.chromium.launch(headless=False) #Launches Chromium only and Choose Headless option
        context = browser.new_context() #Create a NEW browser context (fresh user / incognito)
        page=context.new_page() #Creates a new browser tab ok

        page.goto("https://playwright.dev/") #Will open this page
        expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")#Will check Title of the Page

        browser.close() #Closes the browser