from playwright.sync_api import Page, expect
class LoginPractisePage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.sign_in_btn = page.locator("#signInBtn")
        self.okay_btn = page.get_by_role("button", name="Okay")
        self.user_radio_btn = page.locator("label:nth-child(2) > .checkmark")
        
        
    def load_page(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
        print("\n")
        print(self.page.url)
    
    def admin_scenario(self, username, password):
        username_input = self.username_input
        password_input = self.password_input
        sign_in_btn = self.sign_in_btn
        
        username_input.fill(username)
        password_input.fill(password)
        sign_in_btn.click()
        
        new_url = "https://rahulshettyacademy.com/angularpractice/shop"
        self.page.wait_for_timeout(3000)
        print(self.page.url)
        expect(self.page).to_have_url(new_url)

        
    def user_scenario(self, username, password):
        username_input = self.username_input
        password_input = self.password_input
        sign_in_btn = self.sign_in_btn
        
        username_input.fill(username)
        password_input.fill(password)
        self.user_radio_btn.click()
        self.okay_btn.click()
            
        sign_in_btn.click()
        
        new_url = "https://rahulshettyacademy.com/angularpractice/shop"
        self.page.wait_for_timeout(3000)
        print(self.page.url)
        expect(self.page).to_have_url(new_url)
        self.page.close()
        