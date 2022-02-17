from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    _login_frm = (By.CLASS_NAME, "login-container")
    _user_id_input = (By.ID, "email")
    _password_input = (By.ID, "password")
    _login_btn = (By.ID, "logIn")
    _remember_me_checkbox = (By.ID, "remember-me")
    _need_help_link = (By.PARTIAL_LINK_TEXT, "Need help")
    _email_help_text = (By.CLASS_NAME, "email-help")
    _organization_login_btn = (By.ID, "logInWithOrganization")
    _sign_up_btn = (By.PARTIAL_LINK_TEXT, "Sign up")
    _back_btn = (By.CLASS_NAME, "icon-back")
    _invalid_cred_popup = (By.CLASS_NAME, "login-error-container")

    path = "/login"

    def login_form_displayed(self):
        """Checks if login form displayed and returns True or False"""
        return True if self.wait.for_element_visible(self._login_frm) else False

    def help_displayed(self):
        """Checks if help documentation is displayed and returns True or False"""
        return True if self.wait.for_element_visible(self._email_help_text) else False
    
    def invalid_login_message_displayed(self):
        """Checks if the message for invalid login attempts is displayed and returns True or False"""
        return True if self.wait.for_element_visible(self._invalid_cred_popup) else False

    def login(self):
        """Clicks login button"""
        login_button = self.wait.for_element_clickable(self._login_btn)

        login_button.click()

    def login_as_user(self, username, password):
        """Fills out the username and password fields and clicks login button"""
        user_id_field = self.wait.for_element_visible(self._user_id_input)
        password_field = self.wait.for_element_visible(self._password_input)
        login_button = self.wait.for_element_clickable(self._login_btn)

        user_id_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def enter_credentials(self, username, password):
        """Fills out the username and password fields but does not click login button"""
        user_id_field = self.wait.for_element_visible(self._user_id_input)
        password_field = self.wait.for_element_visible(self._password_input)

        user_id_field.send_keys(username)
        password_field.send_keys(password)

    def go_to_and_login_as(self, username, password):
        """Navigates to login page and logs in with the given username and password"""
        self.go_to()
        self.login_as_user(username, password)

    def go_to_and_enter_credentials(self, username, password):
        """Navigates to login page and enters the given username and password but does not log in"""
        self.go_to()
        self.enter_credentials(username, password)

    def check_remember_me(self):
        remember_me_checkbox = self.wait.for_element_clickable(self._remember_me_checkbox)
        remember_me_checkbox.send_keys(Keys.SPACE)

    def go_to_sign_up_page(self):
        """Navigates to login page and clicks on the Sign Up link"""
        self.go_to()
        sign_up_btn = self.wait.for_element_clickable(self._sign_up_btn)
        sign_up_btn.click()

    def go_to_organization_login_page(self):
        """Navigates to login page and clicks on the Log In with an Organization link"""
        self.go_to()
        org_login_btn = self.wait.for_element_clickable(self._organization_login_btn)
        org_login_btn.click()

    def open_help(self):
        self.go_to()
        help_btn = self.wait.for_element_clickable(self._need_help_link)
        help_btn.click()

    def test_cleanup(self):
        self.clear_all_cookies()
