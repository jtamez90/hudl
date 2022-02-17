import os

import pytest
from dotenv import load_dotenv

from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.home.home_page import HomePage
from src.pages.sign_up.sign_up_page import SignUpPage
from src.pages.organization_login.organization_login_page import OrganizationLoginPage

load_dotenv()  # load local development variables from .env file


@pytest.fixture(scope="session")
def url():
    url = os.getenv("BASE_URL")
    return url

@pytest.fixture(scope="function")
def base_page(driver, url):
    return BasePage(driver, url)

@pytest.fixture(scope="function")
def login_page(driver, url):
    return LoginPage(driver, url)

@pytest.fixture(scope="function")
def home_page(driver, url):
    return HomePage(driver, url)

@pytest.fixture(scope="function")
def sign_up_page(driver, url):
    return SignUpPage(driver, url)

@pytest.fixture(scope="function")
def organization_login_page(driver, url):
    return OrganizationLoginPage(driver, url)