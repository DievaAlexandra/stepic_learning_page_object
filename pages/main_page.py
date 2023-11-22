# ГЛАВНАЯ СТРАНИЦА САЙТА

from selenium.webdriver.common.by import By
from pages.base_page import BasePage  # наследование от BasePage  и теперь можем тут использовать всё что есть в классе предке
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):  # нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    #здесь проверка  на поиск наличие элемента на странице
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" #обращаем внимение на символ *, он означает
                                                                                                    # что передали именно пару и этот кортеж нужно распаковать
