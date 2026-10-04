from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class TablesTab(BasePage):

    SEARCH = (By.ID, "table-search")
    SORT_NAME = (By.ID, "table-sort-name")
    SORT_AGE = (By.ID, "table-sort-age")
    ADD_USER = (By.ID, "table-add-role")
    NAMES = (By.CSS_SELECTOR, "#users-table-body tr td:nth-child(3)")
    AGES = (By.CSS_SELECTOR, "#users-table-body tr td:nth-child(6)")

    def filter_names(self, name):
        self.type_text(self.SEARCH, name)

    def get_visible_names(self):
        elements = self.find_elements(self.NAMES)
        names = []

        for element in elements:
            names.append(element.text)

        return names

    def get_visible_ages(self):
        elements = self.find_elements(self.AGES)
        ages = []

        for element in elements:
            ages.append(int(element.text))

        return ages

    def sort_names(self):
        self.click(self.SORT_NAME)

    def sort_ages(self):
        self.click(self.SORT_AGE)

    def wait_for_names_sorted(self):
        def names_are_sorted(driver):
            names = [element.text for element in driver.find_elements(*self.NAMES)]
            return names == sorted(names, key=str.lower)

        self.wait.until(names_are_sorted)

    def wait_for_ages_sorted(self):
        def ages_are_sorted(driver):
            ages = [int(element.text) for element in driver.find_elements(*self.AGES)]
            return ages == sorted(ages)

        self.wait.until(ages_are_sorted)

    def select_user(self, user_id):
        locator = (By.CSS_SELECTOR, f'[data-testid="row-checkbox-{user_id}"]')
        self.click(locator)

    def is_user_selected(self, user_id):
        locator = (By.CSS_SELECTOR, f'[data-testid="row-checkbox-{user_id}"]')
        return self.find(locator).is_selected()

    def remove_user_by_id(self, user_id):
        locator = (By.CSS_SELECTOR, f'[data-testid="row-delete-{user_id}"]')
        self.click(locator)

    def is_user_visible(self, user_id):
        locator = (By.CSS_SELECTOR, f'tr[data-user-id="{user_id}"]')
        return self.is_present(locator)

    def wait_until_user_gone(self, user_id):
        locator = (By.CSS_SELECTOR, f'tr[data-user-id="{user_id}"]')
        self.wait.until(EC.invisibility_of_element_located(locator))

    def add_new_user(self, user_id, name, email, role, age):
        self.click(self.ADD_USER)
        self.type_text((By.ID, "role-id-1"), str(user_id))
        self.type_text((By.ID, "role-name-1"), name)
        self.type_text((By.ID, "role-email-1"), email)
        Select(self.find((By.ID, "role-role-1"))).select_by_visible_text(role)
        self.type_text((By.ID, "role-age-1"), str(age))
        self.click((By.ID, "add-role-save"))