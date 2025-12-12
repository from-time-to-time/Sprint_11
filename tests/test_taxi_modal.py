import allure
import pytest
from src.taxi_ui.data.taxi_tariffs import TAXI_TARIFFS, TARIFF_DESCRIPTIONS
class TestTaxiModal:

    @allure.title('Проверка модального окна совершенного заказа')
    @pytest.mark.xfail(reason="BUG: кнопка 'Отменить' не закрывает окно заказа")
    def test_taxi_modal(self, route_set):
        main_page = route_set

        taxi_order = main_page.click_call_taxi()
        taxi_order.select_tariff(TAXI_TARIFFS[0])
        expected_price = taxi_order.get_tariff_price(TAXI_TARIFFS[0])
        taxi_order.open_requirements()
        taxi_order.enable_laptop_table()

        modal = taxi_order.click_submit()

        assert modal.has_search_modal_elements(), "Модальное окно 'Поиск машины' отображается некорректно"

        modal.wait_for_order_assigned()
        assert modal.has_assigned_modal_elements(), "Модальное окно совершенного заказа отображается некорректно"

        details = modal.click_details()
        actual_price = details.get_price_value()

        assert actual_price == expected_price, (f"Стоимость в деталях ({actual_price}) не совпадает с ценой выбранного тарифа ({expected_price})")

        modal.click_cancel()
        assert modal.is_closed(), "Окно заказа не закрылось после нажатия 'Отмена'"