from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ChangingAtrTab(BasePage):
    """ Changing Attributes Section test """

    CLOCK_BUTTON = (By.ID, "attrs-clock-btn")
    CLOCK_BUTTON_INFO_BOX = (By.ID, "attrs-clock-readout")
    ROTATING_STATUS_BADGE = (By.ID, "attrs-status-badge")
    ROTATING_STATUS_BADGE_INFO_BOX = (By.ID, "attrs-status-output")
    CHANGING_ID_TRAP_FILLER = (By.CSS_SELECTOR, "[data-testid='flip-id-input']")
    CHANGING_ID_TRAP_INFO = (By.CSS_SELECTOR, "[data-testid='flip-id-readout']")
    COUNTDOWN_BUTTON = (By.ID, "attrs-countdown-btn")
    COUNTDOWN_INFO_BOX = (By.ID, "attrs-countdown-output")
    DYNAMIC_LINK = (By.ID, "attrs-mutating-link")



    def get_clock_button_atr(self):
        return self.get_attribute(self.CLOCK_BUTTON, "data-timestamp")

    def get_clock_info_box(self):
        return self.get_attribute(self.CLOCK_BUTTON_INFO_BOX, "data-timestamp")

    def wait_for_clock_to_change(self, old_timestamp):
        def clock_changed(_):
            current_timestamp = self.get_clock_button_atr()
            return current_timestamp != old_timestamp

        self.wait.until(clock_changed)

    def get_badge_button_status(self):
        return self.get_attribute(self.ROTATING_STATUS_BADGE, "data-status")
        # has multiple cases, error, idle, loading, and ready.

    def get_badge_info_box_message(self):
        return self.get_attribute(self.ROTATING_STATUS_BADGE_INFO_BOX, "innerText")

    def wait_for_status_ready(self):
        def status_is_ready(_):
            return self.get_badge_button_status() == "ready"

        self.wait.until(status_is_ready)

    def get_changing_id(self):
        return self.get_attribute(self.CHANGING_ID_TRAP_FILLER, "id")

    def wait_for_id_to_change(self, old_id):
        def id_changed(_): # the "_" tells selenium that we know it gives us an argument but we dont need it.
            current_id = self.get_changing_id()
            return current_id != old_id

        self.wait.until(id_changed)

    def get_countdown_output(self):
        return self.get_text(self.COUNTDOWN_INFO_BOX)

    def wait_for_countdown(self):
        def countdown_finished(_):
            return self.get_attribute(self.COUNTDOWN_BUTTON, "data-ready") == "true"

        self.wait.until(countdown_finished)

    def get_link_href(self):
        self.scroll_into_view(self.DYNAMIC_LINK, self.DYNAMIC_LINK)
        return self.get_attribute(self.DYNAMIC_LINK, "href")


    def wait_for_link_to_change(self, old_href):
        def link_changed(_):
            current_href = self.get_attribute(self.DYNAMIC_LINK, "href")
            return current_href != old_href

        self.wait.until(link_changed)