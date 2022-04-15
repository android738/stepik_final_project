import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.login_page import LoginPage


def pytest_addoption(parser):
    # выбираем браузер, дефолтный - chrome
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    # выбираем язык браузера, дефолтный - русский
    parser.addoption('--language', default='en', help='Choose browser language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    # chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # firefox
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    # choose browser
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..\n")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..\n")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..\n")
    browser.quit()


@pytest.fixture
def setup(browser):
    link = "https://selenium1py.pythonanywhere.com/accounts/login/"

    email = str(time.time()) + "@fakemail.org"
    password = str(time.time()) + "LOLOLO"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.register_new_user(email, password)
    login_page.should_be_authorized_user()
