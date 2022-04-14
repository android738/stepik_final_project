from selenium.common.exceptions import NoSuchElementException
import re

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_text_of_element(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except Exception:
            return ""

    def alert_get_text(self):
        alert = self.browser.switch_to.alert
        return alert.text

    def alert_type_text(self, text):
        alert = self.browser.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def alert_accept(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        alert = self.browser.switch_to.alert
        alert.dismiss()

    def replace_all_except_numbers(self, text):
        result = re.sub(",", ".", text)
        return re.sub("/[^0-9.]/g", "", result)