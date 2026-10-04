from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SelectionTab(BasePage):
    """The side bar Selection section"""

    SIDE_BAR_SELECTION_GENDER_OUTPUT_FIELD = (By.ID, "gender-output")

    SIDE_BAR_SELECTION_SKILLS_OUTPUT_FIELD = (By.ID, "skills-output")

    SIDE_BAR_SELECTION_SINGLE_SELECT_DROPDOWN = (By.ID, "country-select")
    SIDE_BAR_SELECTION_SINGLE_SELECT_DROPDOWN_OUTPUT_FIELD = (By.ID, "country-output")

    SIDE_BAR_SELECTION_NATIVE_MULTI_SELECT_LANGUAGE = (By.ID, "languages-select")
    SIDE_BAR_SELECTION_NATIVE_MULTI_SELECT_LANGUAGE_FIELD = (By.ID, "languages-output")

    SIDE_BAR_SELECTION_MULTI_SELECT_DROPDOWN = (By.ID, "frameworks-multi-select-trigger")
    SIDE_BAR_SELECTION_MULTI_SELECT_DROPDOWN_OUTPUT_FIELD = (By.ID, "frameworks-multi-output")

    SIDE_BAR_SELECTION_EXPERIENCE_RANGE_SLIDER = (By.ID, "experience-range")
    SIDE_BAR_SELECTION_EXPERIENCE_RANGE_SLIDER_OUTPUT_FIELD = (By.ID, "experience-output")

    SIDE_BAR_SELECTION_ENABLE_NOTIFICATION = (By.CLASS_NAME, "toggle-track")
    SIDE_BAR_SELECTION_ENABLE_NOTIFICATION_FIELD = (By.ID, "toggle-output")

    SIDE_BAR_SELECTION_AUTO_COMPLETE_INPUT = (By.ID, "autocomplete-input")
    SIDE_BAR_SELECTION_AUTO_COMPLETE_OUTPUT_FIELD = (By.ID, "autocomplete-output")


    def pick_gender(self, gender):
        self.wait.until(EC.element_to_be_clickable((By.ID, f"gender-{gender}"))).click()    
        return self

    def get_gender_selection_output(self):
        return self.get_text(self.SIDE_BAR_SELECTION_GENDER_OUTPUT_FIELD)

    def pick_skills(self,skills):
        for skill in skills:
            self.wait.until(EC.element_to_be_clickable((By.ID, f"skill-{skill}"))).click()

        return self

    def unpick_skills(self,skills):
        for skill in skills:
            self.wait.until(EC.element_to_be_clickable((By.ID, f"skill-{skill}"))).click()
    
        return self

    def get_skills_output(self):
        return self.get_text(self.SIDE_BAR_SELECTION_SKILLS_OUTPUT_FIELD)

    def select_country(self, country):
        Select(self.find(self.SIDE_BAR_SELECTION_SINGLE_SELECT_DROPDOWN)).select_by_visible_text(country)
        return self

    def get_country_output(self):
        return self.get_attribute(self.SIDE_BAR_SELECTION_SINGLE_SELECT_DROPDOWN_OUTPUT_FIELD, "innerText")

    def select_multi_languages(self, languages):
        select = Select(self.find(self.SIDE_BAR_SELECTION_NATIVE_MULTI_SELECT_LANGUAGE))

        for language in languages:
            select.select_by_visible_text(language)

        return self

    def get_languages_output(self):
        return self.get_text(self.SIDE_BAR_SELECTION_NATIVE_MULTI_SELECT_LANGUAGE_FIELD)

    def select_multi_framework(self, frameworks):
        self.scroll_into_view(self.SIDE_BAR_SELECTION_MULTI_SELECT_DROPDOWN, self.SIDE_BAR_SELECTION_MULTI_SELECT_DROPDOWN)
        self.find(self.SIDE_BAR_SELECTION_MULTI_SELECT_DROPDOWN).click()

        for framework in frameworks:
            self.wait.until(EC.element_to_be_clickable((By.ID, f"framework-{framework.lower()}"))).click()

        return self
    
    def get_framework_output(self):
        return self.get_text(self.SIDE_BAR_SELECTION_MULTI_SELECT_DROPDOWN_OUTPUT_FIELD)

    def experience_slider(self, experience):
        current = int(self.get_text(self.SIDE_BAR_SELECTION_EXPERIENCE_RANGE_SLIDER_OUTPUT_FIELD).split()[0])
        slider = self.find(self.SIDE_BAR_SELECTION_EXPERIENCE_RANGE_SLIDER)

        while current < experience:
            slider.send_keys(Keys.ARROW_RIGHT)
            current += 1

        while current > experience:
            slider.send_keys(Keys.ARROW_LEFT)
            current -= 1

        return self

    def experience_output(self):
        return self.get_text(self.SIDE_BAR_SELECTION_EXPERIENCE_RANGE_SLIDER_OUTPUT_FIELD)

    def toggle_button(self):
        self.scroll_into_view(self.SIDE_BAR_SELECTION_ENABLE_NOTIFICATION_FIELD, self.SIDE_BAR_SELECTION_ENABLE_NOTIFICATION_FIELD)
        self.click(self.SIDE_BAR_SELECTION_ENABLE_NOTIFICATION)
        return self

    def get_toggle_message(self):
        return self.get_text(self.SIDE_BAR_SELECTION_ENABLE_NOTIFICATION_FIELD)

    def set_auto_complete(self, trio, country):
        self.scroll_into_view(self.SIDE_BAR_SELECTION_AUTO_COMPLETE_INPUT, self.SIDE_BAR_SELECTION_AUTO_COMPLETE_INPUT)
        self.type_text(self.SIDE_BAR_SELECTION_AUTO_COMPLETE_INPUT, trio)
        self.click(self.find((By.CSS_SELECTOR, f"[data-country='{country}']")))
        return self

    def get_auto_complete(self):
        self.scroll_into_view(self.SIDE_BAR_SELECTION_AUTO_COMPLETE_INPUT, self.SIDE_BAR_SELECTION_AUTO_COMPLETE_INPUT)
        return self.get_text(self.SIDE_BAR_SELECTION_AUTO_COMPLETE_OUTPUT_FIELD)