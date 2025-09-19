from playwright.sync_api import Page, expect
from pages.login_practise_page import LoginPractisePage
import pytest

test_data = [
    ("rahulshettyacademy", "learning"), #valid credentials
    (" ", " "),                         #invalid, wrong username, wrong password
    ("rahul", "learning"),              #invalid, wrong username, correct password
    ("rahulshettyacademy", "learn")     #invalid, correct username, wrong password
]

@pytest.mark.parametrize("username, password", test_data)
def test_login_as_admin(page: Page, username, password):
    run = LoginPractisePage(page)
    run.load_page()
    run.admin_scenario(username, password)
    
@pytest.mark.parametrize("username, password", test_data)   
def test_login_as_user(page: Page, username, password):
    run = LoginPractisePage(page)
    run.load_page()
    run.user_scenario(username, password)