# добавляем класс для базовой страницы. в нем будут храниться методы для работы с браузером. Прям базовая базовая страница. удет по сути предком для всех остальных
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # добавили конструктор-метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__. Атрибуты класса - браузер и урл
    def __init__(self, browser, url, timeout=10):
        # в метод в качестве параметров добавляем экземпляр браузера и урл,
        # а в аргументах класса сохраняем эти параметры
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод open для открытия нужной страницы в браузере
    def open(self):
        self.browser.get(self.url)

    #здесь описано как перехватывать исключение. В него будем передавать два аргумента:
    # как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
