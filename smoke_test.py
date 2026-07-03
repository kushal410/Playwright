from playwright.sync_api import sync_playwright

BASE_URL = "https://agentdev.keepme.ai"

PAGES = [
     "/clients",
    "/accounting",
    "/audit",
    "/workspace",
    "/insights",
    "/conversations",
    "/leads",
    "/agent-training",
    "/automations",
    "/re-engage-campaign",
    "/report",
    "/beacon",
    "/knowledge-base",
    "/pulse",
    "/account",
    "/team",
    "/integrations",
    "/api-keys-webhooks",
    "/billing",
    "/theme",
    "/support",
    "/release-notes",
    "/tickets"
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Placeholder login
    page.goto(f"{BASE_URL}/login")

    page.locator("input[type=email]").fill("kushalniraula41@gmail.com")
    page.locator("input[type=password]").fill("P-)SOmL!iu_9Pm!&n6")
    page.locator("button[type=submit]").click()

    page.wait_for_load_state("networkidle")

    for path in PAGES:
        url = BASE_URL + path
        page.goto(url)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=f"screenshots/{path.strip('/')}.png", full_page=True)
        print(f"PASS - {path}")

    browser.close()
