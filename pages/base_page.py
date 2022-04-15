from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_authorized_user(self):
        try:
            self.wait_element_is_present(*BasePageLocators.USER_ICON)
        except NoSuchElementException:
            raise ValueError("Не удалось найти иконку ")

    def go_to_basket_page(self):
        self.wait_element_is_present(*BasePageLocators.BASKET_MINI_LINK)
        add_to_basket_button = self.browser.find_element(*BasePageLocators.BASKET_MINI_LINK)
        add_to_basket_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link element is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def wait_element_is_present(self, how, what):
        try:
            WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def wait_element_is_not_present(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def wait_element_is_disappeared(self, how, what):
        try:
            WebDriverWait(self.browser, 15, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def get_text_of_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
            return element.text
        except NoSuchElementException:
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
