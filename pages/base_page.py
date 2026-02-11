from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ------------------------------
    # Explicit Wait Methods
    # ------------------------------

    def wait_for_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    # ------------------------------
    # Common Actions
    # ------------------------------

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def send_keys(self, locator, value):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_title(self):
        return self.driver.title

    # ------------------------------
    # Screenshot Method
    # ------------------------------

    def take_screenshot(self, name="screenshot"):
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file_path = os.path.join(folder, f"{name}_{timestamp}.png")

        self.driver.save_screenshot(file_path)
        return file_path
