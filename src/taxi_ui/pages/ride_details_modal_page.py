import re

import allure

from src.taxi_ui.locators.modals_locators import ModalsLocators as M
from .base_page import BasePage


class RideDetailsModal(BasePage):

    @allure.step('Получить стоимость поездки')
    def get_price_value(self) -> int:
        text = self.find(M.DETAILS_PRICE_TEXT).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    @allure.step('Нажать кнопку "Отменить"')
    def click_cancel(self):
        self.click(M.CANCEL_BUTTON)

    @allure.step('Проверить, что модальное окно закрылось')
    def is_closed(self) -> bool:
        return self.is_disappeared(M.MODAL)
