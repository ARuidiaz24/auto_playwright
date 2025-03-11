def rest_password(page, username):
    page.fill('input[placeholder="Username"]', username)
    page.click('button[type="submit"]')