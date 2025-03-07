import asyncio
from logging import handlers
from playwright.sync_api import sync_playwright # type: ignore

with sync_playwright() as p:
    browser =  p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
    print(page.title())

    button_search = page.locator("button[aria-label='Search (Ctrl+K)']")
    button_search.click()
    page.fill("//input[@id='docsearch-input']", "Prueba")
    page.wait_for_timeout(10000)

    browser.close()