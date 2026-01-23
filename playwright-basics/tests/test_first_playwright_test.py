from playwright.sync_api import sync_playwright  #using SYNC Function

def test_navigate_to_main_page():  #Function
    with sync_playwright() as playwright:  #Starts Playwright Engine
        #for browser_type in ["chrome", "firefox", "Edge"]: #Not Compulsory it Loops multiple browsers but can be done in Config.ts
        browser=playwright.chromium.launch(headless=False) #Launches Chromium only and Choose Headless option
        context = browser.new_context() #Create a NEW browser context (fresh user / incognito)
        page=context.new_page() #Creates a new browser tab

        page.goto("https://google.com/") #Will open this page
        assert "Google" in page.title()  #Will check Title of the Page

        page.click("//textarea[@id='APjFqb']")
        page.reload()

        browser.close() #Closes the browser