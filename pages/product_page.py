import math
from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        x = self.alert_get_text().split(" ")[2]
        print(f"X: {x}\n")
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(f"Answer: {x}\n")
        self.alert_type_text(answer)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_now_price(self):
        price = self.get_text_of_element(*ProductPageLocators.PRICE_ELEMENT)
        if price:
            return self.replace_all_except_numbers(price)
        else:
            raise ValueError("Не удалось получить текущую цену продукта.")

    def get_now_title(self):
        title = self.get_text_of_element(*ProductPageLocators.TITLE_ELEMENT)
        if title:
            return title
        else:
            raise ValueError("Не удалось получить текущий заголовок продукта.")

    def check_price_is_correct(self, price):
        new_price = self.get_text_of_element(*ProductPageLocators.INFO_ALERT_WITH_PRICE)
        if new_price:
            assert price in self.replace_all_except_numbers(new_price), f"Нет текущей цены продукта ({price}) в уведомлении."
        else:
            raise ValueError("Не удалось получить уведомление с ценой продукта после оформления заказа.")

    def check_title_is_correct(self, title):
        new_title = self.get_text_of_element(*ProductPageLocators.SUCCESS_ALERT_WITH_TITLE)
        if new_title:
            assert title == new_title, f"Нет текущего заголовка продукта ({title}) в уведомлении."
        else:
            raise ValueError("Не удалось получить уведомление с заголовоком продукта после оформления заказа.")

    def should_be_success_message(self, timeout=4):
        assert self.wait_element_is_not_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self, timeout=4):
        assert self.wait_element_is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout), \
            "Success message is presented, but should not be"