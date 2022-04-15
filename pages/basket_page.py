from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.wait_element_is_not_present(*BasketPageLocators.BASKET_PRODUCTS_FORM), \
            "В корзине есть товары, а она должна была быть пустой."

    def basket_should_be_empty_message(self):
        message = self.get_text_of_element(*BasketPageLocators.BASKET_EMPTY)
        if message:
            print(f"\nПолучили сообщение о пустой корзине: \"{message}\".\n")
        else:
            raise ValueError("Не удалось сообщение о пустой корзине.")
