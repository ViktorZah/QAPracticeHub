from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NavBar(BasePage):
    """The side bar. Appears on the page; scroll to a sertain location."""

    SIDE_BAR_INPUTS = (By.CSS_SELECTOR, "[data-testid='nav-inputs']")
    SIDE_BAR_FORMS = (By.CSS_SELECTOR, "[data-testid='nav-forms']")
    SIDE_BAR_OTP_LOGIN = (By.CSS_SELECTOR, "[data-testid='nav-otp-login']")
    SIDE_BAR_SELECTION = (By.CSS_SELECTOR, "[data-testid='nav-selection']")
    SIDE_BAR_BUTTONS = (By.CSS_SELECTOR, "[data-testid='nav-buttons']")
    SIDE_BAR_TABLES = (By.CSS_SELECTOR, "[data-testid='nav-tables']")
    SIDE_BAR_DYNAMIC = (By.CSS_SELECTOR, "[data-testid='nav-dynamic']")
    SIDE_BAR_CHANGING_ATTRIBUTES = (By.CSS_SELECTOR, "[data-testid='nav-changing-attrs']")
    SIDE_BAR_ALERTS = (By.CSS_SELECTOR, "[data-testid='nav-alerts']")
    SIDE_BAR_ADVANCED = (By.CSS_SELECTOR, "[data-testid='nav-advanced']")
    SIDE_BAR_SHOPPING = (By.CSS_SELECTOR, "[data-testid='nav-shopping']")
    SIDE_BAR_PRACTICE_LAB = (By.CSS_SELECTOR, "[data-testid='nav-practice-lab']")

    def go_to_inputs(self):
        self.click(self.SIDE_BAR_INPUTS)

    def go_to_forms(self):
        self.click(self.SIDE_BAR_FORMS)

    def go_to_otp_login(self):
        self.click(self.SIDE_BAR_OTP_LOGIN)

    def go_to_selection(self):
        self.click(self.SIDE_BAR_SELECTION)

    def go_to_buttons(self):
        self.click(self.SIDE_BAR_BUTTONS)

    def go_to_tabs(self):
        self.click(self.SIDE_BAR_TABLES)

    def go_to_changing_attributes(self):
        self.click(self.SIDE_BAR_CHANGING_ATTRIBUTES)