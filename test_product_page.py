from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    product_page = ProductPage(browser, link)
    product_page.open()
    old_price = product_page.get_now_price()
    old_title = product_page.get_now_title()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_price_is_correct(old_price)
    product_page.check_title_is_correct(old_title)
