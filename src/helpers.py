from enum import IntEnum

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Timeout(IntEnum):
    """An enum helper class for wait timeout values in seconds."""

    THREE_SECONDS = 3
    TEN_SECONDS = 10
    THIRTY_SECONDS = 30
    SIXTY_SECONDS = 60


class Waits:
    """Contains wait methods to be used by pages"""

    def __init__(self, driver):
        self.driver = driver

    def for_all_elements_visible(self, locator):
        """Checks if elements are visible. Returns the list of elements or False"""
        return self._wait_for(
            ec.visibility_of_all_elements_located, Timeout.TEN_SECONDS, locator
        )

    def for_element_clickable(self, locator):
        """Checks if element is clickable. Returns the element or False"""
        return self._wait_for(ec.element_to_be_clickable, Timeout.TEN_SECONDS, locator)

    def for_element_visible(self, locator):
        """Checks if element is visible. Returns the element or False"""
        return self._wait_for(
            ec.visibility_of_element_located, Timeout.THREE_SECONDS, locator
        )

    def for_text_presence(self, locator, text):
        """Checks if the given text is visible within the element. Returns the element
        or False"""
        return self._wait_for_with_arg(
            ec.text_to_be_present_in_element, Timeout.THIRTY_SECONDS, locator, text
        )

    def _wait_for(self, expected_condition, timeout, locator=None):
        """Waits for expected condition with a given timeout and locator (optional
        depending on the condition). Returns the element(s) or False"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(
                expected_condition(locator) if locator else expected_condition()
            )
            return element
        except TimeoutException:
            return False

    def _wait_for_with_arg(self, expected_condition, timeout, locator, argument):
        """Waits for expected condition with a given timeout, locator, and additional
        argument required by the expected condition. Returns element(s) or False"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(expected_condition(locator, argument))
            return element
        except TimeoutException:
            return False


class Hovers:
    """Contains a Hover method to be used by pages"""

    def __init__(self, driver):
        self.driver = driver

    def hover(self, locator):
        """Creates the hover action based on a selector"""
        self.hover_element = self.driver.find_element(*locator)
        self.hover_action= ActionChains(self.driver).move_to_element(self.hover_element)
        self.hover_action.perform()
