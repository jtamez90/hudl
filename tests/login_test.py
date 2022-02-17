"""Test cases for the login page."""

import os
from dotenv import load_dotenv

load_dotenv()


def test_need_help_display(login_page):
    login_page.open_help()
    assert login_page.help_displayed()
    login_page.test_cleanup()

def test_organization_login_page(login_page, organization_login_page):
    """I don't have organization credentials so I can only test whether the element loads"""
    login_page.go_to_organization_login_page()
    assert organization_login_page.is_at()
    login_page.test_cleanup()

def test_sign_up_page(login_page, sign_up_page):
    """Verify that the sign up page link is working"""
    login_page.go_to_sign_up_page()
    assert sign_up_page.is_at()
    login_page.test_cleanup()

def test_login_with_valid_credentials(login_page, home_page):
    """Logs in as a regular user"""
    login_page.go_to_and_login_as(os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD"))
    assert home_page.is_at()
    login_page.test_cleanup()

def test_login_and_logout(login_page, home_page, base_page):
    """Logs in as a regular user and then logs out"""
    login_page.go_to_and_login_as(os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD"))
    assert home_page.is_at()
    home_page.logout()
    assert base_page.is_at()
    login_page.test_cleanup()

def test_login_with_invalid_password(login_page, home_page):
    """Attempst login with invalid credentials"""
    login_page.go_to_and_login_as(os.getenv("TEST_USERNAME"), "invalid_password")
    assert home_page.is_not_at()
    login_page.test_cleanup()

def test_login_with_blank_fields(login_page, home_page):
    """Attempst login with blank credentials"""
    login_page.go_to_and_login_as("","")
    assert home_page.is_not_at()
    login_page.test_cleanup()

def test_popup_for_invalid_login(login_page):
    """Checks whether the invalid credentials notification pops up"""
    login_page.go_to_and_login_as("","")
    assert login_page.invalid_login_message_displayed()
    login_page.test_cleanup()

def test_remember_me_functionality(login_page, home_page):
    """Logs in with the 'Remember Me' checkbox and makes sure the feature works"""
    login_page.go_to_and_enter_credentials(os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD"))
    login_page.check_remember_me()
    login_page.login()
    assert home_page.is_at()
    home_page.simulate_browser_restart_and_navigate_home()
    assert home_page.is_at()
    login_page.test_cleanup()
