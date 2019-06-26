import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                         help="Choose browser")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose browser language")
    parser.addoption('--timeout', action='store', default=10,
                 help="Choose timeout time (seconds)")

@pytest.fixture(scope="function")
def browser(request):
    """
    Инициализируем указанный браузер с указанным языком.
    Defaults: browser_name=chrome, language=ru
    """
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=profile)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    browser.quit()