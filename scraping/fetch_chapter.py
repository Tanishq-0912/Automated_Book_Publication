from playwright.sync_api import sync_playwright
import os

def fetch_and_screenshot(url, filename_prefix):
    screenshot_path = os.path.join("data", "screenshots", f"{filename_prefix}.png")
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

    print(f"[INFO] Saving screenshot to: {os.path.abspath(screenshot_path)}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()

    print("[SUCCESS] Screenshot saved!")

def fetch_chapter_text(url, filename_prefix):
    from bs4 import BeautifulSoup
    import requests

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Clean up text (customize for different websites)
    text = soup.get_text()
    clean_text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

    save_path = os.path.join("data", "raw", f"{filename_prefix}.txt")
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(clean_text)

    print(f"[SUCCESS] Chapter text saved to {os.path.abspath(save_path)}")
