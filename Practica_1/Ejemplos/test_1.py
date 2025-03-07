import re
from playwright.sync_api import Page, expect, sync_playwright

def test_uno():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        expect(page).to_have_title(re.compile("Fast and reliable end-to-end testing for modern web apps | Playwright Python"))
        browser.close()

def test_dos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev/python/")
        button_GetStarted = page.locator("a.getStarted_Sjon:text('Get started')")
        expect(button_GetStarted).to_have_attribute("class", "getStarted_Sjon")
        expect(button_GetStarted).to_have_attribute("href", "/python/docs/intro")
        button_GetStarted.click()
        browser.close()

