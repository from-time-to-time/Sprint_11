import re

import allure

from src.taxi_ui.locators.main_page_locators import MainPageLocators as L
from .base_page import BasePage


class MainPage(BasePage):

    @allure.step('Задать адрес "Откуда"')
    def set_from_address(self, address):
        self.type(L.FROM_INPUT, address)
        return self

    @allure.step('Задать адрес "Куда"')
    def set_to_address(self, address):
        self.type(L.TO_INPUT, address)
        return self

    @allure.step('Дождаться отображения точки стартого адреса на карте')
    def wait_for_start_point(self):
        self.wait_visible(L.MAP_START_POINT)
        return self

    @allure.step('Дождаться отображения точки финального адреса на карте')
    def wait_for_finish_point(self):
        self.wait_visible(L.MAP_FINISH_POINT)
        return self

    @allure.step('Дождаться отображения блока с выбором маршрута')
    def wait_for_route_panel(self):
        self.wait_visible(L.ROUTE_PANEL)
        return self

    @allure.step('Получить текст маршрута для одинаковых адресов')
    def get_same_route_text(self) -> str:
        part1 = self.wait_visible(L.ROUTE_PRICE_TEXT).text
        part2 = self.wait_visible(L.ROUTE_DURATION_TEXT).text
        return f"{part1} {part2}"

    @allure.step('Выбрать маршрут "Оптимальный"')
    def select_optimal_route(self):
        self.click(L.TAB_OPTIMAL)

    @allure.step('Выбрать маршрут "Быстрый"')
    def select_fast_route(self):
        self.click(L.TAB_FAST)

    @allure.step('Выбрать маршрут "Свой"')
    def select_custom_route(self):
        self.click(L.TAB_CUSTOM)

    @allure.step('Проверить активность кнопки "Вызвать такси"')
    def is_call_taxi_button_active(self) -> bool:
        return self.is_clickable(L.CALL_TAXI_BUTTON)

    @allure.step('Проверить активность кнопки "Забронировать"')
    def is_book_drive_button_active(self) -> bool:
        btn = self.wait_visible(L.BOOK_DRIVE_BUTTON)
        classes = btn.get_attribute("class").split()
        return "disabled" not in classes

    @allure.step('Проверить, что таб активен')
    def _is_tab_active(self, tab_locator) -> bool:
        el = self.find(tab_locator)
        classes = el.get_attribute("class").split()
        return "active" in classes

    @allure.step('Проверить, что таб "Оптимальный" активен')
    def is_optimal_tab_active(self) -> bool:
        return self._is_tab_active(L.TAB_OPTIMAL)

    @allure.step('Проверить, что таб "Быстрый" активен')
    def is_fast_tab_active(self) -> bool:
        return self._is_tab_active(L.TAB_FAST)

    @allure.step('Проверить, что таб "Свой" активен')
    def is_custom_tab_active(self) -> bool:
        return self._is_tab_active(L.TAB_CUSTOM)

    @allure.step('Выбрать тип передвижения "Драйв"')
    def select_drive(self):
        self.click(L.DRIVE_TYPE)

    @allure.step('Дождаться появления блока типов передвижения')
    def wait_types(self):
        self.wait_visible(L.TYPES_CONTAINER)
        return self

    @allure.step('Проверить, что тип передвижения активен')
    def _is_transport_type_enabled(self, locator) -> bool:
        el = self.find(locator)
        classes = el.get_attribute("class").split()
        return "disabled" not in classes

    @allure.step('Проверить, что все типы передвижения активны')
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

    @allure.step('Получить стоимость текущего маршрута')
    def get_route_price(self) -> int:
        text = self.find(L.ROUTE_PRICE_TEXT).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    @allure.step('Получить время в пути для текущего маршрута')
    def get_route_time(self) -> int:
        text = self.find(L.ROUTE_DURATION_TEXT).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    @allure.step('Нажать кнопку "Вызвать такси" и открыть форму заказа')
    def click_call_taxi(self):
        self.click(L.CALL_TAXI_BUTTON)
        from src.taxi_ui.pages.taxi_order_page import TaxiOrderPage
        return TaxiOrderPage(self.driver)
