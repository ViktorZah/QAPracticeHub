from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class FormsTab(BasePage):
    """The side bar froms section"""

    SIDE_BAR_FORM_USERNAME = (By.ID, "login-preview-username")
    SIDE_BAR_FORM_PASSWORD = (By.ID, "login-preview-password")
    SIDE_BAR_FORM_USERNAME_FIELD = (By.ID, "login-username")
    SIDE_BAR_FORM_PASSWORD_FIELD = (By.ID, "login-password")
    SIDE_BAR_FORM_PASSWORD_VISIBLE_TOGGLE = (By.ID, "login-password-toggle")
    SIDE_BAR_FORM_LOGIN_BUTTON = (By.ID, "login-submit")
    SIDE_BAR_FORM_LOGIN_MESSAGE_SUCCESS = (By.ID, "login-message")
    SIDE_BAR_FORM_FORGOT_PASSWORD_BUTTON = (By.ID, "forgot-password-trigger")
    SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_FIELD = (By.ID, "forgot-username")
    SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_BUTTON = (By.ID, "forgot-password-submit")
    SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_MESSAGE = (By.ID, "forgot-password-result")
    SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_SUBMIT_MESSAGE_FAIL = (By.ID, "forgot-password-message")
    SIDE_BAR_FORM_REGISTER_NAME = (By.ID, "reg-firstname")
    SIDE_BAR_FORM_REGISTER_LAST_NAME = (By.ID, "reg-lastname")
    SIDE_BAR_FORM_REGISTER_EMAIL = (By.ID, "reg-email")
    SIDE_BAR_FORM_REGISTER_COUNTRY = (By.ID, "reg-country")
    SIDE_BAR_FORM_REGISTER_BUTTON = (By.ID, "register-submit")
    SIDE_BAR_FORM_REGISTER_MESSAGE = (By.ID, "register-message")
    SIDE_BAR_FORM_REGISTER_CLEAR_BUTTON = (By.ID, "register-clear")


    def set_username(self):
        self.click(self.SIDE_BAR_FORM_USERNAME_FIELD)
        self.type_text(self.SIDE_BAR_FORM_USERNAME_FIELD, self.get_attribute(self.SIDE_BAR_FORM_USERNAME, "innerText"))
        return self

    def set_password(self):
        self.click(self.SIDE_BAR_FORM_PASSWORD_FIELD)
        self.type_text(self.SIDE_BAR_FORM_PASSWORD_FIELD, self.get_attribute(self.SIDE_BAR_FORM_PASSWORD, "innerText"))
        return self

    def set_username_forget_password_form(self):
        self.click(self.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_FIELD)
        self.type_text(self.SIDE_BAR_FORM_FORGOT_PASSWORD_WINDOW_USERNAME_FIELD, self.get_attribute(self.SIDE_BAR_FORM_USERNAME, "innerText"))
        return self

    def set_name_registration_form(self, name):
        self.click(self.SIDE_BAR_FORM_REGISTER_NAME)
        self.type_text(self.SIDE_BAR_FORM_REGISTER_NAME, name)
        return self

    def set_last_name_registration_form(self, last_name):
        self.click(self.SIDE_BAR_FORM_REGISTER_NAME)
        self.type_text(self.SIDE_BAR_FORM_REGISTER_LAST_NAME, last_name)
        return self

    def set_email_registration_form(self, email):
        self.click(self.SIDE_BAR_FORM_REGISTER_EMAIL)
        self.type_text(self.SIDE_BAR_FORM_REGISTER_EMAIL, email)
        return self

    def set_country(self, country):
        country_dropdown = self.find(self.SIDE_BAR_FORM_REGISTER_COUNTRY)
        Select(country_dropdown).select_by_visible_text(country)
        return self

    def form_complete_message(self):
        return self.get_attribute(self.SIDE_BAR_FORM_REGISTER_MESSAGE,"innerText")

    def clear_form(self):
        self.click(self.SIDE_BAR_FORM_REGISTER_NAME)
        self.type_text(self.SIDE_BAR_FORM_REGISTER_NAME, "")
        self.click(self.SIDE_BAR_FORM_REGISTER_NAME)
        self.type_text(self.SIDE_BAR_FORM_REGISTER_LAST_NAME, "")
        self.click(self.SIDE_BAR_FORM_REGISTER_EMAIL)
        self.type_text(self.SIDE_BAR_FORM_REGISTER_EMAIL, "")
        country_dropdown = self.find(self.SIDE_BAR_FORM_REGISTER_COUNTRY)
        Select(country_dropdown).select_by_visible_text("Select country")
        return self
    