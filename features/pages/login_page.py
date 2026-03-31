from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the player login flow."""

    # Locators
    LOGIN_LINK      = (By.XPATH, "//a[@href='/login.shtml']")
    USERNAME_INPUT  = (By.NAME, "map(username)")
    PASSWORD_INPUT  = (By.NAME, "map(password)")
    SUBMIT_BTN      = (By.XPATH, "//input[@type='submit'][@value='Login']")
    ERROR_MESSAGE   = (By.XPATH, "//div[@class='error-message']")
    WELCOME_MSG     = (By.XPATH, "//span[@class='welcome-user']")

    def open_login(self):
        self.open("login.shtml")

    def enter_username(self, username: str):
        self.type_text(username, *self.USERNAME_INPUT)

    def enter_password(self, password: str):
        self.type_text(password, *self.PASSWORD_INPUT)

    def submit(self):
        self.click(*self.SUBMIT_BTN)

    def get_error_message(self) -> str:
        return self.get_text(*self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        return self.is_element_visible(*self.WELCOME_MSG)
