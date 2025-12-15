import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.taxi_ui import config


class BasePage:
    def __init__(self, driver, timeout=config.DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открыть страницу сайта')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент по локатору')
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Найти видимый элемент')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Проверить, что элемент видим')
    def _is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Ожидать пока элемент станет видимым в течение N секунд')
    def wait_visible_with_timeout(self, locator, timeout: int):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скроллить страницу к элементу')
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидать возможности клика по элементу')
    def is_clickable(self, locator) -> bool:
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Нажать на элемент')
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввести текст')
    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    @allure.step('Навести курсор на элемент')
    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Проверить, что элемент скрылся')
    def is_disappeared(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
