import pytest
from playwright.sync_api import sync_playwright, expect   # type: ignore
from test_login.utils.login_helper import login

@pytest.fixture(scope="function")
def config_browser():
    with sync_playwright() as p:  
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page 
        browser.close()

# -------------Login con credenciales correctas-------------
def test_login_Correct(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login(page, "Admin", "admin123")

    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    #Validación de URL
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"

# -------------Login con password incorrecta-------------
def test_login_password(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login(page, "Admin", "admin12")

    #Selecctores
    alert = page.locator("div[role='alert']")
    text_alert = page.locator(".oxd-text.oxd-text--p.oxd-alert-content-text")

    #Validación que el elemento sea visible
    expect(alert).to_be_visible()

    #Validación texto de alerta de validación
    expect(text_alert).to_have_text("Invalid credentials")

# -------------Login con user incorrecta-------------
def test_login_user(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    login(page, "prueba", "admin123")

    #Selecctores
    alert = page.locator("div[role='alert']")
    text_alert = page.locator(".oxd-text.oxd-text--p.oxd-alert-content-text")

    #Validación que el elemento sea visible
    expect(alert).to_be_visible()

    #Validación texto de alerta de validación
    expect(text_alert).to_have_text("Invalid credentials")

# -------------Login con campos nulos-------------
def test_login_null(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #Selecctores
    alert_user = page.locator("//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
    alert_password = page.locator("//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")

    #Click boton Login
    page.click('button[type="submit"]')

    #Validación que el elemento sea visible
    expect(alert_user).to_be_visible()
    expect(alert_password).to_be_visible()

    #Validación texto de alerta de validación
    expect(alert_user).to_have_text("Required")
    expect(alert_password).to_have_text("Required")

# -------------Redireccionar page recordar contraseña-------------  
def test_login_recor_password(config_browser):
    page = config_browser
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #Click forgot you password
    recor_password = page.locator("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    recor_password.click()

    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode'
    
    #Validación de URL
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"