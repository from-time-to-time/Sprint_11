from .base_page import BasePage
from src.taxi_ui.locators.taxi_order_locators import TaxiOrderLocators as L
import re

class TaxiOrderPage(BasePage):

    def wait_tariffs(self):
        self.wait_visible(L.TARIFF_LIST)

    def has_all_taxi_tariffs(self) -> bool:
        return all(
            self._is_visible(locator)
            for locator in L.TARIFF_CARD.values()
        )
    def get_active_tariff_names(self) -> list[str]:
        active = []
        for name, locator in L.TARIFF_CARD.items():
            if self._is_tariff_active_by_locator(locator):
                active.append(name)
        return active

    def _is_tariff_active_by_locator(self, locator) -> bool:
        el = self.find(locator)
        return "active" in el.get_attribute("class").split()

    def select_tariff(self, name: str):
        locator = L.TARIFF_CARD[name]
        self.click(locator)
        return self

    def hover_tariff_info_icon(self, name: str):
        locator = L.TARIFF_INFO_ICON[name]
        self.hover(locator)
        return self

    def get_tariff_description(self, name: str) -> str:

        self.select_tariff(name)
        self.hover_tariff_info_icon(name)

        desc_el = self.wait_visible(L.TOOLTIP_DESCRIPTION)
        return desc_el.text.strip()

    def get_tariff_price(self, name: str) -> int:
        locator = L.TARIFF_PRICE[name]
        text = self.find(locator).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    def open_requirements(self):
        self.click(L.REQUIREMENTS_DROPDOWN)

    def is_laptop_table_enabled(self) -> bool:
        el = self.find(L.LAPTOP_TABLE_INPUT)
        return el.is_selected()

    def enable_laptop_table(self):
        checkbox = self.wait_visible(L.LAPTOP_TABLE_TOGGLE)
        if not checkbox.is_selected():
            checkbox.click()

    def click_submit(self):
        self.click(L.ORDER_BUTTON)
        from src.taxi_ui.pages.taxi_modal import TaxiModal
        return TaxiModal(self.driver)

    def is_phone_field_visible(self) -> bool:
        return self._is_visible(L.PHONE)

    def is_payment_method_visible(self) -> bool:
        return self._is_visible(L.PAYMENT_METHOD)

    def is_comment_field_visible(self) -> bool:
        return self._is_visible(L.COMMENT_INPUT)

    def is_requirements_block_visible(self) -> bool:
        return self._is_visible(L.REQUIREMENTS_BUTTON)
