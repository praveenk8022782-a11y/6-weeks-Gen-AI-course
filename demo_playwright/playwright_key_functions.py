from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open automation practice website
        page.goto("https://practicetestautomation.com/practice-test-login/")

        # Fill username
        page.fill("#username", "student")

        # Fill password
        page.fill("#password", "Password123")

        # Click login button
        page.click("#submit")

        # Wait for page load
        page.wait_for_timeout(3000)

        # Print title
        print("Page Title:", page.title())

        # Screenshot
        page.screenshot(path="login_success.png")

        print("Automation completed successfully!")

        browser.close()


run()