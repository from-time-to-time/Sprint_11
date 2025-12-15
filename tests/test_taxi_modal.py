import allure
import pytest

from src.taxi_ui.data.taxi_tariffs import TAXI_TARIFFS
from src.taxi_ui.pages.ride_details_modal_page import RideDetailsModal
from src.taxi_ui.pages.taxi_modal_page import TaxiModal
from src.taxi_ui.pages.taxi_order_page import TaxiOrderPage


class TestTaxiModal:

    @allure.title('Проверка модального окна совершенного заказа')
    @pytest.mark.xfail(reason='BUG: кнопка "Отменить" не закрывает окно заказа')
    def test_taxi_modal(self, driver, route_set):
        main_page = route_set
        main_page.click_call_taxi()

        taxi_order = TaxiOrderPage(driver)
        taxi_order.select_tariff(TAXI_TARIFFS[0])
        expected_price = taxi_order.get_tariff_price(TAXI_TARIFFS[0])
        taxi_order.open_requirements()
        taxi_order.enable_laptop_table()
        taxi_order.click_submit()

        modal = TaxiModal(driver)

        assert modal.has_search_modal_elements(), 'Модальное окно "Поиск машины" отображается некорректно'

        modal.wait_for_order_assigned()
        assert modal.has_assigned_modal_elements(), 'Модальное окно совершенного заказа отображается некорректно'

        modal.click_details()

        details_page = RideDetailsModal(driver)

        actual_price = details_page.get_price_value()

        assert actual_price == expected_price, (
            f'Стоимость в деталях ({actual_price}) не совпадает с ценой выбранного тарифа ({expected_price})')

        details_page.click_cancel()
        assert details_page.is_closed(), 'Окно заказа не закрылось после нажатия "Отмена"'
