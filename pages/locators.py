from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_PRODUCTS_FORM = (By.CSS_SELECTOR, "#content_inner #basket_formset")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_MINI_LINK = (By.CSS_SELECTOR, ".basket-mini a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=\"login_submit\"]")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_REPEAT_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_ELEMENT = (By.CSS_SELECTOR, ".price_color")
    TITLE_ELEMENT = (By.CSS_SELECTOR, "h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_ALERT_WITH_TITLE = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    INFO_ALERT_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info")
