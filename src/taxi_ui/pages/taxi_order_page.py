from .base_page import BasePage
from src.taxi_ui.locators.taxi_order_locators import TaxiOrderLocators as L

class TaxiOrderPage(BasePage):

    def visible(self):
        self.find(L.TARIFF_LIST)

    def select_tariff(self, name: str):
        locator = L.TARIFF_CARD[name]
        self.click(locator)

    def hover_tariff_info(self, name: str):
        locator = L.TARIFF_INFO_ICON[name]
        self.hover(locator)

    def get_tariff_description(self, name: str) -> str:
        locator = L.TARIFF_TOOLTIP[name]
        return self.find(locator).text

    def open_requirements(self):
        self.click(L.REQUIREMENTS_DROPDOWN)

    def is_laptop_table_enabled(self) -> bool:
        el = self.find(L.LAPTOP_TABLE_CHECKBOX)
        return el.is_selected()

    def enable_laptop_table(self):
        if not self.is_laptop_table_enabled():
            self.click(L.LAPTOP_TABLE_CHECKBOX)

    def click_submit(self):
        self.click(L.ORDER_BUTTON)
