from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os


class BasePage:
    """
    Base class for all page objects.
    Provides shared explicit wait wrappers and navigation utilities.
    All page classes inherit from this.
    """

    BASE_URL = os.getenv("BASE_URL", "https://example.qa.gameaccount.com/")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, path: str = ""):
        self.driver.get(f"{self.BASE_URL}{path}")

    def find(self, *locator):
        return self.wait.until(
            EC.presence_of_element_located(locator),
            f"Element {locator} did not appear"
        )

    def find_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            f"Element {locator} not visible"
        )

    def click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, text: str, *locator):
        field = self.find(*locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, *locator) -> str:
        return self.find_visible(*locator).text

    def wait_for_url(self, url_fragment: str):
        self.wait.until(
            EC.url_contains(url_fragment),
            f"URL did not contain '{url_fragment}'"
        )

    def is_element_visible(self, *locator) -> bool:
        try:
            self.find_visible(*locator)
            return True
        except Exception:
            return False
