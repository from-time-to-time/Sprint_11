import allure
import pytest
from src.taxi_ui.data.taxi_tariffs import TAXI_TARIFFS, TARIFF_DESCRIPTIONS
class TestTaxiOrder:
    @allure.title('Проверка смены времени и стоимости маршрута при переключении между табами "Оптимальный" и "Быстрый"')
    def test_optimal_fast_switch_updates_active_tab_and_price_time(self, route_set):
        main_page = route_set

        assert main_page.is_fast_tab_active(), 'Таб "Быстрый" не активен'

        fast_price = main_page.get_route_price()
        fast_time = main_page.get_route_time()

        main_page.select_optimal_route()

        assert main_page.is_optimal_tab_active(), 'Таб "Оптимальный" не активен'

        optimal_price = main_page.get_route_price()
        optimal_time = main_page.get_route_time()

        assert fast_price != optimal_price, 'Стоимость тарифов совпадает'
        assert fast_time != optimal_time, 'Время в пути совпадает'

        main_page.select_fast_route()

        assert main_page.is_fast_tab_active(), 'Таб "Быстрый" не активен'

    @allure.title('Проверка активности типов передвижения при переключении на таб "Свой"')
    def test_switch_to_custom_activates_types_of_movement(self, route_set):
        main_page = route_set
        main_page.select_custom_route()
        assert main_page.is_custom_tab_active(), 'Таб "Свой" не активен'
        assert main_page.are_all_transport_types_enabled(), 'Не все типы передвижения активны внутри таба "Свой"'

    @allure.title('Проверка активности кнопки "Вызвать такси" при выборе тарифа "Быстрый"')
    def test_set_fast_tariff_activate_call_taxi_button(self, route_set):
        main_page = route_set
        assert main_page.is_call_taxi_button_active(), 'Кнопка "Вызвать такси" не активна'

    @allure.title('Проверка активности кнопки "Забронировать" при выборе тарифа "Свой" и типа передвижения "Драйв"')
    def test_set_custom_drive_activate_reserve_button(self, route_set):
        main_page = route_set
        main_page.select_custom_route()
        main_page.wait_types()
        main_page.select_drive()
        assert main_page.is_book_drive_button_active(), 'Кнопка "Забронировать" не активна'

    @allure.title('Проверка заказа тарифа "Такси"')
    def test_taxi_order(self, route_set):
        main_page = route_set

        taxi_order = main_page.click_call_taxi()
        taxi_order.wait_tariffs()

        assert taxi_order.has_all_taxi_tariffs(), 'Отображаются не все 6 тарифов такси'

        active = taxi_order.get_active_tariff_names()
        assert active == [TAXI_TARIFFS[0]]

    @allure.title('Проверка описаний тарифов такси')
    @pytest.mark.xfail(reason="BUG: Некорректные описания тарифов 'Разговорчивый' и 'Сонный '")
    @pytest.mark.parametrize("tariff_name", TAXI_TARIFFS)
    def test_taxi_tariff_tooltips_show_correct_description(self, route_set, tariff_name):
        main_page = route_set

        taxi_order = main_page.click_call_taxi()
        taxi_order.wait_tariffs()

        actual_description = taxi_order.get_tariff_description(tariff_name)

        expected_description = TARIFF_DESCRIPTIONS[tariff_name]

        assert actual_description == expected_description

    @allure.title('Проверка отображения блока с полями под тарифами')
    def test_taxi_order_form_fields_visible(self, route_set):
        main_page = route_set

        taxi_order = main_page.click_call_taxi()
        taxi_order.wait_tariffs()

        assert taxi_order.is_phone_field_visible(), 'Поле "Телефон" не отображается'
        assert taxi_order.is_payment_method_visible(), 'Поле "Способ оплаты" не отображается'
        assert taxi_order.is_comment_field_visible(), 'Поле "Комментарий водителю" не отображается'
        assert taxi_order.is_requirements_block_visible(), 'Блок "Требования к заказу" не отображается'