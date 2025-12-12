from .base_page import BasePage
from src.taxi_ui.locators.main_page_locators import MainPageLocators as L
import re


class MainPage(BasePage):

    def set_from_address(self, address):
        self.type(L.FROM_INPUT, address)
        return self

    def set_to_address(self, address):
        self.type(L.TO_INPUT, address)
        return self

    def wait_for_start_point(self):
        self.wait_visible(L.MAP_START_POINT)
        return self

    def wait_for_finish_point(self):
        self.wait_visible(L.MAP_FINISH_POINT)
        return self

    def wait_for_route_panel(self):
        self.wait_visible(L.ROUTE_PANEL)
        return self
    def get_same_route_text(self) -> str:
        part1 = self.wait_visible(L.ROUTE_PRICE_TEXT).text
        part2 = self.wait_visible(L.ROUTE_DURATION_TEXT).text
        return f"{part1} {part2}"

    def select_optimal_route(self):
        self.click(L.TAB_OPTIMAL)

    def select_fast_route(self):
        self.click(L.TAB_FAST)

    def select_custom_route(self):
        self.click(L.TAB_CUSTOM)
    def is_call_taxi_button_active(self) -> bool:
        return self.is_clickable(L.CALL_TAXI_BUTTON)

    def is_book_drive_button_active(self) -> bool:
        btn = self.wait_visible(L.BOOK_DRIVE_BUTTON)
        classes = btn.get_attribute("class").split()
        return "disabled" not in classes

    def _is_tab_active(self, tab_locator) -> bool:
        el = self.find(tab_locator)
        classes = el.get_attribute("class").split()
        return "active" in classes

    def is_optimal_tab_active(self) -> bool:
        return self._is_tab_active(L.TAB_OPTIMAL)

    def is_fast_tab_active(self) -> bool:
        return self._is_tab_active(L.TAB_FAST)

    def is_custom_tab_active(self) -> bool:
        return self._is_tab_active(L.TAB_CUSTOM)

    def select_drive(self):
        self.click(L.DRIVE_TYPE)

    def wait_types(self):
        self.wait_visible(L.TYPES_CONTAINER)
        return self

    def _is_transport_type_enabled(self, locator) -> bool:
        el = self.find(locator)
        classes = el.get_attribute("class").split()
        return "disabled" not in classes

    def are_all_transport_types_enabled(self) -> bool:
        locators = [
            L.CAR_TYPE,
            L.WALK_TYPE,
            L.TAXI_TYPE,
            L.BIKE_TYPE,
            L.SCOOTER_TYPE,
            L.DRIVE_TYPE,
        ]
        return all(self._is_transport_type_enabled(l) for l in locators)

    def get_route_price(self) -> int:
        text = self.find(L.ROUTE_PRICE_TEXT).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    def get_route_time(self) -> int:
        text = self.find(L.ROUTE_DURATION_TEXT).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    def click_call_taxi(self):
        self.click(L.CALL_TAXI_BUTTON)
        from src.taxi_ui.pages.taxi_order_page import TaxiOrderPage
        return TaxiOrderPage(self.driver)