from selenium.webdriver.common.by import By

from src.helpers import Hovers, Waits


class BasePage:
    _logout_link = (By.PARTIAL_LINK_TEXT, "Log Out")
    _profile_element = (By.CLASS_NAME, "hui-globaluseritem__display-name")

    path = "/"

    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver
        self.wait = Waits(self.driver)
        self.hover_over = Hovers(self.driver)

    def clear_all_cookies(self):
        """Clears all browser cookies"""
        self.driver.delete_all_cookies()
    
    def get_current_url(self):
        return self.driver.current_url

    def go_to(self):
        """Navigates to specified page"""
        self.driver.get(self.base_url + self.path)

    def is_at(self):
        """Verifies webpage is at the specified page"""
        self.wait.for_all_elements_visible(self._profile_element)
        if self.get_current_url() == (self.base_url + self.path):
            return True
        else:
            return False
    
    def is_not_at(self):
        """Verifies webpage is NOT at the specified page (useful for negative tests)"""
        self.wait.for_all_elements_visible(self._profile_element)
        if self.get_current_url() == (self.base_url + self.path):
            return False
        else:
            return True

    def log_out(self):
        """Logs user out"""
        self.hover_over.hover(self._profile_element)
        log_out_link = self.wait.for_element_clickable(self._logout_link)
        log_out_link.click()

    def simulate_browser_restart(self):
        """Clears all non-persistent cookies to simulate a broswer restart upon page reload;
        This is mainly to test the Remember Me feature"""
        all_cookies = self.driver.get_cookies()

        for cookie in all_cookies:
            if cookie.get('expiry') == None:
                self.driver.delete_cookie(cookie.get('name'))

