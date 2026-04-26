import keyring
from playwright.sync_api import sync_playwright

CONDECO_URL = "https://boeing.condecosoftware.com"

def main():
    username = keyring.get_password("condeco", "username")
    password = keyring.get_password("condeco", "password")

    if not username or not password:
        raise ValueError("Could not load credentials from Windows Credential Manager.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(CONDECO_URL, wait_until="domcontentloaded")

        page.get_by_label("Username").fill(username)
        page.get_by_label("Password").fill(password)
        page.get_by_role("button", name="Sign in").click()

        page.wait_for_timeout(6000)

        dashboard_frame = None
        for frame in page.frames:
            if "EnterpriseLite/#/app/dashboard" in frame.url:
                dashboard_frame = frame
                break

        if not dashboard_frame:
            print("Dashboard frame not found.")
            browser.close()
            return

        check_in = dashboard_frame.locator("text=Check in").first
        if check_in.count() > 0:
            check_in.click()
            print("Clicked Check in.")
        else:
            print("No Check in button found.")

        page.wait_for_timeout(3000)
        browser.close()

if __name__ == "__main__":
    main()