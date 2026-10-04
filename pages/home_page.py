from pages.base_page import BasePage
from pages.components.navbar import NavBar
from pages.inputs_page import InputsTab
from pages.forms_page import FormsTab
from pages.otp_login_page import OTPTab
from pages.selection_page import SelectionTab
from pages.buttons_page import ButtonsTab
from pages.tables_page import TablesTab
from pages.changing_atr_page import ChangingAtrTab
from utils.config_reader import get_config

class HomePage(BasePage):
    URL = get_config()["base_url"]

    def __init__(self, driver):
        super().__init__(driver)
        self.navbar = NavBar(driver)
        self.inputs_tab = InputsTab(driver)
        self.form_tab = FormsTab(driver)
        self.otp_login_tab = OTPTab(driver)
        self.selection_tab = SelectionTab(driver)
        self.buttons_tab = ButtonsTab(driver)
        self.tables_tab = TablesTab(driver)
        self.changing_attr_tab = ChangingAtrTab(driver)



    def load(self):
        self.open(self.URL)
        return self