from playwright.sync_api import sync_playwright

BASE_URL = "https://your-app.example"

PAGES = [
    "/dashboard",
    "/reports",
    "/settings",
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Placeholder login
    page.goto(f"{BASE_URL}/login")

    page.locator("input[type=email]").fill("user@example.com")
    page.locator("input[type=password]").fill("password")
    page.locator("button[type=submit]").click()

    page.wait_for_load_state("networkidle")

    for path in PAGES:
        url = BASE_URL + path
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"screenshots/{path.strip('/')}.png", full_page=True)
        print(f"PASS - {path}")

    browser.close()
