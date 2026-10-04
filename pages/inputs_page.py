from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InputsTab(BasePage):
    """The side bar inputs section"""

    SIDE_BAR_INPUTS_NAME = (By.ID, "text-input")
    SIDE_BAR_INPUTS_EMAIL = (By.ID, "email-input")
    SIDE_BAR_INPUTS_PASSWORD = (By.ID, "password-input")
    SIDE_BAR_INPUTS_NUMBER = (By.ID, "number-input")
    SIDE_BAR_INPUTS_DATE = (By.ID, "date-input")
    SIDE_BAR_INPUTS_TIME = (By.ID, "time-input")
    SIDE_BAR_INPUTS_SEARCH = (By.ID, "search-input")
    SIDE_BAR_INPUTS_PHONE = (By.ID, "tel-input")
    SIDE_BAR_VALIDATION_PHONE = (By.ID, "tel-feedback")
    SIDE_BAR_INPUTS_TEXTAREA = (By.ID, "textarea-input")
    SIDE_BAR_INPUTS_READ_ONLY = (By.ID, "readonly-input")
    SIDE_BAR_INPUTS_DISABLED = (By.ID, "disabled-input")
    SIDE_BAR_INPUTS_INPUT_OUTPUT = (By.ID, "input-output")
    SIDE_BAR_INPUTS_INPUT_OUTPUT_RESULT = (By.ID, "input-output-result")
    PHONE_INOUT_SELECTION_EXPAND = (By.ID, "phone-country-btn")
    PHONE_INOUT_SELECTION_LIST = (By.ID, "phone-country-list")

    COUNTRIES = {
        "Canada": {"code": "ca", "phone_code": "+1"},
        "India": {"code": "in", "phone_code": "+91"},
        "United States": {"code": "us", "phone_code": "+1"},
        "United Kingdom": {"code": "uk", "phone_code": "+44"},
        "Australia": {"code": "au", "phone_code": "+61"},
        "Germany": {"code": "de", "phone_code": "+49"},
        "France": {"code": "fr", "phone_code": "+33"},
        "Japan": {"code": "jp", "phone_code": "+81"},
        "China": {"code": "cn", "phone_code": "+86"},
        "Portugal": {"code": "pt", "phone_code": "+351"},
        "Ireland": {"code": "ie", "phone_code": "+353"},
    }


    def fill_name(self, name):
        self.click(self.SIDE_BAR_INPUTS_NAME)
        self.type_text(self.SIDE_BAR_INPUTS_NAME, name)
        return self

    def fill_email(self, email):
        self.type_text(self.SIDE_BAR_INPUTS_EMAIL, email)
        return self

    def fill_password(self, password):
        self.type_text(self.SIDE_BAR_INPUTS_PASSWORD, password)
        return self

    def fill_number(self, number):
        self.type_text(self.SIDE_BAR_INPUTS_NUMBER, number)
        return self

    def fill_date(self, date):
        self.type_text(self.SIDE_BAR_INPUTS_DATE, date)
        return self

    def fill_time(self, time):
        self.type_text(self.SIDE_BAR_INPUTS_TIME, time)
        return self

    def fill_search(self, search):
        self.type_text(self.SIDE_BAR_INPUTS_SEARCH, search)
        return self

    def fill_phone(self, phone):
        self.type_text(self.SIDE_BAR_INPUTS_PHONE, phone)
        return self

    def fill_textarea(self, textarea):
        self.type_text(self.SIDE_BAR_INPUTS_TEXTAREA, textarea)
        return self
    
    def fill_read_only(self, read_only):
        self.type_text(self.SIDE_BAR_INPUTS_READ_ONLY, read_only)
        return self

    def click_disabled(self):
        self.click(self.SIDE_BAR_INPUTS_DISABLED)

    def fill_input_output(self, input_output):
        self.type_text(self.SIDE_BAR_INPUTS_INPUT_OUTPUT, input_output)
        return self    

    def fill_input_output_result(self):
        self.get_attribute(self.SIDE_BAR_INPUTS_INPUT_OUTPUT_RESULT, "value")
        return self

    def expand_phone_by_country(self, country):
        self.left_mouse_click(self.PHONE_INOUT_SELECTION_EXPAND)

        country_data = self.COUNTRIES.get(country)

        if not country_data:
            raise ValueError(f"Unsupported country: {country}")

        country_locator = (By.CSS_SELECTOR, f'[data-testid="phone-country-{country_data["code"]}"]')

        self.scroll_into_view(self.PHONE_INOUT_SELECTION_LIST, country_locator)
        self.left_mouse_click(country_locator)
        return self

    def get_country_phone_code(self, country):
        country_data = self.COUNTRIES.get(country)

        if not country_data:
            raise ValueError(f"Unsupported country: {country}")

        return country_data["phone_code"]

    def get_phone_validate_text(self):
        element = self.find(self.SIDE_BAR_VALIDATION_PHONE)
        return element.text
