#ГЛАВНАЯ СТРАНИЦА САЙТА
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage): #класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
    def go_to_login_page(self): #нужно указать аргумент self , чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    # открыть страницу логина
    def go_to_login_page(browser):
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

