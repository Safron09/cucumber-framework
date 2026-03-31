from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class RegistrationPage(BasePage):
    """Page object for the new player registration flow."""

    # Locators
    JOIN_NOW_LINK   = (By.XPATH, "//a[@href='/sign-up.shtml']")
    FIRST_NAME      = (By.NAME, "map(firstName)")
    LAST_NAME       = (By.NAME, "map(lastName)")
    TERMS_CHECKBOX  = (By.NAME, "map(terms)")
    SUBMIT_BTN      = (By.XPATH, "//fieldset[@class='underlay']//input[@id='form']")
    ERROR_DOB       = (By.XPATH, "//label[@for='dob'][text()='This field is required']")

    def open_home(self):
        self.open()

    def click_join_now(self):
        self.click(*self.JOIN_NOW_LINK)

    def enter_first_name(self, first_name: str):
        self.type_text(first_name, *self.FIRST_NAME)

    def enter_last_name(self, last_name: str):
        self.type_text(last_name, *self.LAST_NAME)

    def accept_terms(self):
        self.click(*self.TERMS_CHECKBOX)

    def submit_registration(self):
        self.click(*self.SUBMIT_BTN)

    def get_dob_error_message(self) -> str:
        return self.get_text(*self.ERROR_DOB)
