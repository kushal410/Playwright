from playwright.sync_api import sync_playwright
import os

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

EMAIL = os.getenv("KEEPME_EMAIL")
PASSWORD = os.getenv("KEEPME_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    os.makedirs("screenshots/pass", exist_ok=True)

    # IMPORTANT: same as Selenium flow → login at /clients
    page.goto(BASE_URL + "/clients")

    try:
        # EMAIL
        page.wait_for_selector('input', timeout=15000)
        page.locator('xpath=//*[@id="root"]/div[1]/div/div/div/form/div[1]/input').fill(EMAIL)

        page.locator('xpath=//*[@id="root"]/div[1]/div/div/div/form/div[2]/button').click()

        # PASSWORD
        page.wait_for_selector('input', timeout=15000)
        page.locator('xpath=//*[@id="root"]/div[1]/div/div/div/form/div[1]/div/input').fill(PASSWORD)

        page.locator('xpath=//*[@id="root"]/div[1]/div/div/div/form/div[3]/button').click()

        page.wait_for_load_state("networkidle")

        print("LOGIN SUCCESS")

    except Exception as e:
        page.screenshot(path="screenshots/login_fail.png")
        print("LOGIN FAILED:", e)
        browser.close()
        exit()

    # -------------------------
    # PAGE LOOP
    # -------------------------
    for path in PAGES:
        url = BASE_URL + path
        print("Opening:", url)

        try:
            page.goto(url)
            page.wait_for_load_state("networkidle")

            name = path.strip("/").replace("/", "_")
            page.screenshot(path=f"screenshots/pass/{name}.png", full_page=True)

            print("PASS:", path)

        except Exception as e:
            page.screenshot(path=f"screenshots/pass/{name}_fail.png", full_page=True)
            print("FAIL:", path, e)

    browser.close()
