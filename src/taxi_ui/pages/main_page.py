from .base_page import BasePage
from src.taxi_ui.locators.main_page_locators import MainPageLocators as L

class MainPage(BasePage):

    def set_from_address(self, address):
        self.type(L.FROM_INPUT, address)

    def set_to_address(self, address):
        self.type(L.TO_INPUT, address)

    def build_route(self, from_addr, to_addr):
        self.set_from_address(from_addr)
        self.set_to_address(to_addr)
        # если маршрут строится автоматически – просто ждём панель маршрута
        self.wait_for_route_panel()

    def wait_for_route_panel(self):
        self.find(L.ROUTE_PANEL)

    def select_optimal_route(self):
        self.click(L.TAB_OPTIMAL)

    def select_fast_route(self):
        self.click(L.TAB_FAST)

    def select_custom_route(self):
        self.click(L.TAB_CUSTOM)

    def is_call_taxi_button_enabled(self):
        return self.find(L.CALL_TAXI_BUTTON).is_enabled()

    def is_book_drive_button_enabled(self):
        return self.find(L.BOOK_DRIVE_BUTTON).is_enabled()

    def get_route_price_and_time(self):
        # верни текст/числа из блока Стоимость / Время
        ...

    def get_map_points(self):
        # верни булевые флаги или список найденных точек
        ...
