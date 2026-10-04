from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OTPTab(BasePage):
    """The side bar OTP Login section"""

    SIDE_BAR_OTP_LOGIN_USERNAME_FIELD = (By.ID, "otp-username")
    SIDE_BAR_OTP_LOGIN_OTP_FIELD = (By.CSS_SELECTOR, "#otp-inputs input")
    SIDE_BAR_OTP_LOGIN_SUBMIT_BUTTON = (By.ID, "otp-submit")
    SIDE_BAR_OTP_LOGIN_FETCH_OTP_BUTTON = (By.ID, "btn-fetch-otp")
    SIDE_BAR_OTP_LOGIN_RESEND_OTP_BUTTON = (By.ID, "btn-resend-otp")
    SIDE_BAR_OTP_LOGIN_FORM_MESSAGE = (By.ID, "otp-countdown")
    SIDE_BAR_OTP_LOGIN_FORM_MESSAGE_SUCCESS = (By.ID, "otp-login-message")
    SIDE_BAR_OTP_LOGIN_FORM_OTP_CODE = (By.ID, "otp-display")


    def submit_button_otp_click(self):
        self.click(self.SIDE_BAR_OTP_LOGIN_SUBMIT_BUTTON)
        return self

    def fetch_otp_button_click(self):
        self.click(self.SIDE_BAR_OTP_LOGIN_FETCH_OTP_BUTTON)
        return self

    def resend_otp_button_click(self):
        wait_element = self.custom_wait_driver(40)
        wait_element.until(EC.text_to_be_present_in_element(self.SIDE_BAR_OTP_LOGIN_FORM_MESSAGE, "OTP has expired. Click Resend OTP to get a new code."))
        self.click(self.SIDE_BAR_OTP_LOGIN_RESEND_OTP_BUTTON)
        return self

    def get_success_message_text(self):
        return self.get_text(self.SIDE_BAR_OTP_LOGIN_FORM_MESSAGE_SUCCESS)

    def get_countdown_message(self):
        return self.get_text(self.SIDE_BAR_OTP_LOGIN_FORM_MESSAGE)

    def fill_username(self, username):
        self.type_text(self.SIDE_BAR_OTP_LOGIN_USERNAME_FIELD, username)
        return self
    
    def get_otp_code(self):
        return self.get_text(self.SIDE_BAR_OTP_LOGIN_FORM_OTP_CODE)
