from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    Error_message = (By.XPATH, "//h3[contains(normalize-space(),'Epic sadface')]")
    hamburger_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    logout_menu = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def login(self, user, pwd):
        self.send_keys(self.username, user)
        self.send_keys(self.password, pwd)
        self.click(self.login_btn)
    def logout(self):
        hamburger_menu = self.wait_for_element_clickable(self.hamburger_menu)
        self.click(self.hamburger_menu)
        logout_menu = self.wait_for_element_clickable(self.logout_menu)
        self.click(self.logout_menu)
    
    def get_error_message(self):
        return self.wait_for_element_visible(self.Error_message).text
