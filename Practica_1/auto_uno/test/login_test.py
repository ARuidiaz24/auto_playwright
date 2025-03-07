import pytest
from playwright.sync_api import sync_playwright, expect   # type: ignore
from utils.login_helper import login

@pytest.fixture(scope="function")
def config_browser():
    with sync_playwright() as p:  
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page 
        browser.close()
        
def test_login_Correct(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login(page, "Admin", "admin123")

    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"

def test_login_password(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login(page, "Admin", "admin12")
    alert = page.locator("div[role='alert']")
    expect(alert).to_be_visible()