import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#обработчик считывающий имя браузера и язык
def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default="chrome"
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language'
    )


#здесь реализуется логика для запуска браузера
@pytest.fixture()
def browser(request):
    #инициализируем имя браузера из того, что получили в командной строке
    browser_name = request.config.getoption("browser_name")
    #инициализируем язык браузера из того, что получили в командной строке
    user_language = request.config.getoption("language")

    #в цикле смотрим хром и фф, иначе none
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

        #еще запишем какой конкретно браузер запустили
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    #второе или для фф
    elif browser_name == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
        browser = None
    yield browser
    print("\nquit browser...")
    browser.quit()
