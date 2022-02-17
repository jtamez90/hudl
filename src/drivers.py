from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def chromedriver(headless=False):
    chrome_options = ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument("--ignore-certificate-errors")
    return Chrome(options=chrome_options)


def geckodriver(headless=False):
    firefox_options = FirefoxOptions()
    if headless:
        firefox_options.add_argument("--headless")
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    return Firefox(options=firefox_options)