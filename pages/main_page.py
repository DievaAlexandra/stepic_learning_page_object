# ГЛАВНАЯ СТРАНИЦА САЙТА

from selenium.webdriver.common.by import By
from pages.base_page import \
    BasePage  # наследование от BasePage  и теперь можем тут использовать всё что есть в классе предке


class MainPage(BasePage):
    def go_to_login_page(self):  # нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
