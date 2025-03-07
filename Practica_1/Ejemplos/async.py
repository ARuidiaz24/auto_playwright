import asyncio
from logging import handlers
from playwright.async_api import async_playwright, expect # type: ignore

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        page.goto("https://playwright.dev/python/")

        button_GetStarted = page.locator("text = Get started")
        expect(button_GetStarted).to_have_attribute("href", "/python/docs/intro")
        await button_GetStarted.click()
        await browser.close()

asyncio.run(main())