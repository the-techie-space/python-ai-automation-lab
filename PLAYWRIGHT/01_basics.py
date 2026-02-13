"""
01_basics.py

Goal:
- Launch browser
- Open website
- Print title
- Close browser
"""

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Create new page (tab)
        page = browser.new_page()

        # Open website
        page.goto("https://example.com")

        # Print page title
        print("Page Title:", page.title())

        # Close browser
        browser.close()


if __name__ == "__main__":
    run()


# 02_navigation_and_selectors

"""
Learn:
- Click
- Selectors
"""

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        # Example selectors
        # page.click("#login")
        # page.click(".button-class")
        # page.click("text=More information")

        print("Selectors explained in comments.")

        browser.close()


if __name__ == "__main__":
    run()

#03_forms_and_inputs

"""
Learn:
- Fill inputs
- Click buttons
"""

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        # Example form interaction
        # page.fill("#username", "admin")
        # page.fill("#password", "1234")
        # page.click("#submit")

        print("Form handling example")

        browser.close()


if __name__ == "__main__":
    run()


# 04_waits_and_assertions

"""
Learn:
- wait_for_selector
"""

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        # Wait for element
        page.wait_for_selector("text=Example Domain")

        print("Element appeared successfully!")

        browser.close()


if __name__ == "__main__":
    run()


# 05_screenshots_and_files

"""
Learn:
- Take screenshot
"""

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://example.com")

        page.screenshot(path="homepage.png")

        print("Screenshot saved as homepage.png")

        browser.close()


if __name__ == "__main__":
    run()


# 06_multiple_tabs_and_frames

"""
Learn:
- Multiple tabs
"""

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page1 = browser.new_page()
        page1.goto("https://example.com")

        page2 = browser.new_page()
        page2.goto("https://example.org")

        print("Opened two tabs")

        browser.close()


if __name__ == "__main__":
    run()


# 07_headless_vs_headed

"""
Difference between headless and headed mode
"""

from playwright.sync_api import sync_playwright


def run(headless_mode=True):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless_mode)
        page = browser.new_page()
        page.goto("https://example.com")

        print("Running in headless =", headless_mode)

        browser.close()


if __name__ == "__main__":
    run(headless_mode=False)


# 08_pytest_integration

"""
Run using:
pytest 08_pytest_integration.py
"""

from playwright.sync_api import sync_playwright


def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://example.com")

        assert "Example" in page.title()

        browser.close()


