from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from src.taxi_ui import config
import allure

class BasePage:
    def __init__(self, driver, timeout=config.DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открываем страницу сайта')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ищем элемент по локатору')
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Ожидаем, пока элемент станет видимым')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Скроллим страницу к элементу')
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем возможности клика по элементу')
    def is_clickable(self, locator) -> bool:
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Нажимаем на элемент')
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Вводим текст')
    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    @allure.step('Наводим курсор на элемент')
    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Проверяем, что элемент скрылся')
    def is_disappeared(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
