from pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


class ButtonsTab(BasePage):
    """The side bar buttons section"""

    SIDE_BAR_BUTTONS_PRIMARY = (By.ID, "btn-primary")
    SIDE_BAR_BUTTONS_SECONDARY = (By.ID, "btn-secondary")
    SIDE_BAR_BUTTONS_LEFT_CLICK_ME = (By.ID, "btn-left-click")
    SIDE_BAR_BUTTONS_OUTLINE_BUTTON = (By.ID, "btn-outline")
    SIDE_BAR_BUTTONS_DISABLED_BUTTON = (By.ID, "btn-disabled")
    SIDE_BAR_BUTTONS_CLICK_ME_COUNT_BUTTON = (By.ID, "btn-click-counter")
    SIDE_BAR_BUTTONS_DOUBLE_CLICK_BUTTON = (By.ID, "btn-double-click")
    SIDE_BAR_BUTTONS_RIGHT_CLICK_BUTTON = (By.ID, "btn-right-click")
    SIDE_BAR_BUTTONS_HOVER_BUTTON = (By.ID , "btn-hover")
    SIDE_BAR_BUTTONS_DANGER_CLICK_BUTTON = (By.ID, "btn-danger")
    SIDE_BAR_BUTTONS_NEXT_PAGE_CLICK_BUTTON = (By.ID, "btn-next-page")
    SIDE_BAR_BUTTONS_DOWNLOAD_SAMPLE_CLICK_BUTTON = (By.ID, "btn-download")
    SIDE_BAR_BUTTONS_OPEN_POPUP_CLICK_BUTTON = (By.ID, "btn-open-popup")
    SIDE_BAR_BUTTONS_INFO_POPUP_CLICK_BUTTON = (By.ID, "info-btn-click")
    SIDE_BAR_BUTTONS_INFO_POPUP_TEXT_MESSAGE = (By.ID, "info-popup-click")
    SIDE_BAR_BUTTONS_INFO_POPUP_HOVER_BUTTON = (By.ID, "info-btn-hover")
    SIDE_BAR_BUTTONS_INFO_POPUP_HOVER_TEXT_MESSAGE = (By.ID, "into-popup-hover")
    SIDE_BAR_BUTTONS_RESULT_MESSAGE_GLOBAL = (By.ID, "button-output")
    NEW_PAGE_TEXT_MESSAGE = (By.CLASS_NAME, "card")
    POPUP_CLOSE_MESSAGE = (By.ID, "buttons-popup-close")
    HOVER_INFO_APPEARING_BOX = (By.ID, "info-popup-hover")

    def press_primary_button(self):
        self.click(self.SIDE_BAR_BUTTONS_PRIMARY)
        return self

    def press_secondary_button(self):
        self.click(self.SIDE_BAR_BUTTONS_SECONDARY)
        return self

    def press_left_click_button(self):
        self.left_mouse_click(self.SIDE_BAR_BUTTONS_LEFT_CLICK_ME)
        return self

    def press_outline_button(self):
        self.click(self.SIDE_BAR_BUTTONS_OUTLINE_BUTTON)
        return self

    def press_disabled_button(self):
        with pytest.raises(WebDriverException):
                self.click(self.SIDE_BAR_BUTTONS_DISABLED_BUTTON)
        return self

    def press_counter_button(self):
        self.click(self.SIDE_BAR_BUTTONS_CLICK_ME_COUNT_BUTTON)
        return self

    def press_counter_count(self):
        return self.get_text(self.SIDE_BAR_BUTTONS_CLICK_ME_COUNT_BUTTON)

    def press_button_twice(self):
        self.double_click(self.SIDE_BAR_BUTTONS_DOUBLE_CLICK_BUTTON)
        return self

    def press_right_click_button(self):
        self.right_click(self.SIDE_BAR_BUTTONS_RIGHT_CLICK_BUTTON)
        return self

    def hover_over_button(self):
        self.actions_move_to_element(self.SIDE_BAR_BUTTONS_HOVER_BUTTON)
        return self

    def press_danger_button(self):
        self.click(self.SIDE_BAR_BUTTONS_DANGER_CLICK_BUTTON)
        return self

    def press_next_page(self):
        original_tab = self.driver.current_window_handle
        new_tabs = self.driver.window_handles.copy()
        self.switch_to_new_tab(new_tabs)

        assert "Site not available" in self.get_text(self.NEW_PAGE_TEXT_MESSAGE)

        self.driver.switch_to.window(original_tab)

        return self

    def press_download_sample_file(self):
        #later
        return self

    def press_open_popup(self):
        self.click(self.SIDE_BAR_BUTTONS_OPEN_POPUP_CLICK_BUTTON)
        self.click(self.POPUP_CLOSE_MESSAGE)
        return self

    def press_click_info(self):
        self.click(self.SIDE_BAR_BUTTONS_INFO_POPUP_CLICK_BUTTON)
        return self

    def info_button_message(self):
        return self.get_text(self.SIDE_BAR_BUTTONS_INFO_POPUP_TEXT_MESSAGE)

    def hover_info(self):
        self.actions_move_to_element(self.SIDE_BAR_BUTTONS_INFO_POPUP_HOVER_BUTTON)
        return self

    def info_hover_message(self):
        return self.get_text(self.HOVER_INFO_APPEARING_BOX)

    def get_global_result_info_message(self):
        return self.get_text(self.SIDE_BAR_BUTTONS_RESULT_MESSAGE_GLOBAL)