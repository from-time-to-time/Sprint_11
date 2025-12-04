from .base_page import BasePage
from src.taxi_ui.locators.taxi_order_locators import TaxiOrderLocators as L

class TaxiOrderPage(BasePage):

    def visible(self):
        self.find(L.TARIFF_LIST)

    def select_tariff(self, name: str):
        # например, по тексту тарифа
        ...

    def hover_tariff_info(self, name: str):
        # ховер по иконке "i" у нужного тарифа
        ...

    def get_tariff_description(self, name: str) -> str:
        ...

    def set_phone(self, phone):
        self.type(L.PHONE_INPUT, phone)

    def set_payment_method(self, method):
        # раскрыть список и выбрать нужный элемент
        ...

    def set_driver_comment(self, text):
        self.type(L.DRIVER_COMMENT_INPUT, text)

    def open_requirements(self):
        self.click(L.REQUIREMENTS_DROPDOWN)

    def toggle_laptop_table(self):
        self.click(L.LAPTOP_TABLE_CHECKBOX)

    def click_submit(self):
        self.click(L.SUBMIT_BUTTON)
