"""Sets up project-wide fixtures and command line options."""

import pytest

from src.drivers import geckodriver, chromedriver


def pytest_addoption(parser):
    """Adds pytest command line options for specifying the browser, whether to run it
    headless, and the URL for the test server."""
    parser.addoption(
        "--browser",
        action="store",
        default="Chrome",
        help="Browser options: Chrome, Firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Runs tests in a headless browser.",
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser").capitalize()


@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope="session")
def driver(browser, headless):
    """Returns a webdriver instance for the browser specified and safely quits the
    driver after use."""
    if browser == "Chrome":
        driver = chromedriver(headless)
        yield driver
        driver.quit()
    elif browser == "Firefox":
        driver = geckodriver(headless)
        yield driver
        driver.quit()
    else:
        raise ValueError("Browser type must be 'Chrome' or 'Firefox'.")
