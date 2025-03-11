def login(page, username, password):
    page.fill('input[placeholder="Username"]', username)
    page.fill('input[placeholder="Password"]', password)
    page.click('button[type="submit"]')