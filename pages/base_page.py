from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    """Parent class for HomePage and every standalone page."""

    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.actions = ActionChains(driver)

    def open(self, url):
        self.driver.get(url)
        return self

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def find_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def get_attribute(self, locator, name):
        element = self.find(locator)
        return element.get_attribute(name)

    def is_visible(self, locator):
        try:
            self.find(locator)
            return True
        
        except Exception:
            return False

    def is_present(self, locator):
            try:
                self.find_present(locator)
                return True
            
            except Exception:
                return False

    def accept_allert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def decline_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        #alert = self.driver.switch_to.alert
        alert.dismiss()
        return self

    def delete_all_selected_text(self, locator):
         element = self.find(locator)
         self.actions.move_to_element(element).click().key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).send_keys(Keys.DELETE).perform()

    def arrow_up_press(self, locator):
         element = self.find(locator)
         self.actions.move_to_element(element).key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()

    def arrow_down_press(self, locator):
         element = self.find(locator)
         self.actions.move_to_element(element).key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()

    def left_mouse_click(self, locator):
         element = self.find(locator)
         self.actions.move_to_element(element).click().perform()#imitates user with actions rather than using click()

    def double_click(self, locator):
        button = self.find(locator)
        self.actions.move_to_element(button).double_click().perform()

    def right_click(self, locator):
        button = self.find(locator)
        self.actions.move_to_element(button).context_click().perform()

    def actions_move_to_element(self, locator):
        element = self.find(locator)
        self.actions.move_to_element(element).perform()


    def scroll_into_view(self, locator, target_locator):
        container = self.find(locator)
        target = self.find(target_locator)

        self.actions.move_to_element(container).perform()
        self.actions.scroll_by_amount(0, 300).perform()
        self.actions.move_to_element(target).perform()

    def switch_to_new_tab(self, old_tabs):
        self.wait.until(EC.number_of_windows_to_be(len(old_tabs) + 1))

        new_tab = next(
            handle for handle in self.driver.window_handles
            if handle not in old_tabs
        )

        self.driver.switch_to.window(new_tab)
        return self

    def custom_wait_driver(self, custom_time = 30):
        return WebDriverWait(self.driver, custom_time)