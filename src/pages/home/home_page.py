from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class HomePage(BasePage):
    
    path = '/home'

    def simulate_browser_restart_and_navigate_home(self):
        self.simulate_browser_restart()
        self.go_to()

    def logout(self):
        self.log_out()