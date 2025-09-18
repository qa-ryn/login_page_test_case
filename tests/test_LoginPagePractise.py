from playwright.sync_api import Page, expect
from pages.login_practise_page import LoginPractisePage

def test_login_as_admin(page: Page):
    run = LoginPractisePage(page)
    run.load_page()
    run.admin_scenario("rahulshettyacademy", "learning")
    
def test_login_as_user(page: Page):
    run = LoginPractisePage(page)
    run.load_page()
    run.user_scenario("rahulshettyacademy", "learning")