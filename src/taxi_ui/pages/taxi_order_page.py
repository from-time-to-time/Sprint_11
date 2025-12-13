import re

import allure

from src.taxi_ui.locators.taxi_order_locators import TaxiOrderLocators as L
from .base_page import BasePage


class TaxiOrderPage(BasePage):
    @allure.step('Дождаться отображения списка тарифов такси')
    def wait_tariffs(self):
        self.wait_visible(L.TARIFF_LIST)

    @allure.step('Проверить, что на форме присутствуют все тарифы такси')
    def has_all_taxi_tariffs(self) -> bool:
        return all(
            self._is_visible(locator)
            for locator in L.TARIFF_CARD.values()
        )

    @allure.step('Определить активные тарифы такси')
    def get_active_tariff_names(self) -> list[str]:
        active = []
        for name, locator in L.TARIFF_CARD.items():
            if self._is_tariff_active_by_locator(locator):
                active.append(name)
        return active

    @allure.step('Проверить, что тариф по локатору активен')
    def _is_tariff_active_by_locator(self, locator) -> bool:
        el = self.find(locator)
        return "active" in el.get_attribute("class").split()

    @allure.step('Выбрать тариф такси по названию')
    def select_tariff(self, name: str):
        locator = L.TARIFF_CARD[name]
        self.click(locator)
        return self

    @allure.step('Навести курсор на иконку информации о тарифе')
    def hover_tariff_info_icon(self, name: str):
        locator = L.TARIFF_INFO_ICON[name]
        self.hover(locator)
        return self

    @allure.step('Получить описание тарифа такси (подзаголовок)')
    def get_tariff_description(self, name: str) -> str:

        self.select_tariff(name)
        self.hover_tariff_info_icon(name)

        desc_el = self.wait_visible(L.TOOLTIP_DESCRIPTION)
        return desc_el.text.strip()

    @allure.step('Получить стоимость тарифа такси')
    def get_tariff_price(self, name: str) -> int:
        locator = L.TARIFF_PRICE[name]
        text = self.find(locator).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    @allure.step('Открыть блок "Требования к заказу"')
    def open_requirements(self):
        self.click(L.REQUIREMENTS_DROPDOWN)

    @allure.step('Проверить, включен ли параметр "Столик для ноутбука"')
    def is_laptop_table_enabled(self) -> bool:
        el = self.find(L.LAPTOP_TABLE_INPUT)
        return el.is_selected()

    @allure.step('Включить параметр "Столик для ноутбука", если он выключен')
    def enable_laptop_table(self):
        checkbox = self.wait_visible(L.LAPTOP_TABLE_TOGGLE)
        if not checkbox.is_selected():
            checkbox.click()

    @allure.step('Нажать кнопку "Ввести номер и заказать" и открыть модальное окно поиска машины')
    def click_submit(self):
        self.click(L.ORDER_BUTTON)
        from src.taxi_ui.pages.taxi_modal_page import TaxiModal
        return TaxiModal(self.driver)

    @allure.step('Проверить наличие поля "Телефон" в форме заказа')
    def is_phone_field_visible(self) -> bool:
        return self._is_visible(L.PHONE)

    @allure.step('Проверить наличие поля "Способ оплаты" в форме заказа')
    def is_payment_method_visible(self) -> bool:
        return self._is_visible(L.PAYMENT_METHOD)

    @allure.step('Проверить наличие поля "Комментарий водителю" в форме заказа')
    def is_comment_field_visible(self) -> bool:
        return self._is_visible(L.COMMENT_INPUT)

    @allure.step('Проверить наличие блока "Требования к заказу" в форме заказа')
    def is_requirements_block_visible(self) -> bool:
        return self._is_visible(L.REQUIREMENTS_BUTTON)
