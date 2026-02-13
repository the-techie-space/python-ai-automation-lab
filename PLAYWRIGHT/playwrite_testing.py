from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        page.fill("#username", "user")
        page.fill("#password", "pass")
        page.click("#login")
        page.wait_for_selector("text=Dashboard")
        browser.close()

from playwright.sync_api import sync_playwright

def test_open_example_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        browser.close()


