from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_basket_page(self):
        self.wait_element_is_present(*MainPageLocators.BASKET_MINI_LINK, 10)
        add_to_basket_button = self.browser.find_element(*MainPageLocators.BASKET_MINI_LINK)
        add_to_basket_button.click()