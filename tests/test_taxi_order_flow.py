import allure

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

    # @pytest.mark.xfail(reason="BUG: 'Отменить' не закрывает окно заказа")
    # def test_order_cancel_closes_order_modal(taxi_order_page):
    #     # полный флоу до завершённого заказа
    #     taxi_order_page.select_tariff("Рабочий")
    #     taxi_order_page.enable_laptop_table()
    #     search_modal = taxi_order_page.click_submit().wait_visible()
    #     order_modal = search_modal.wait_until_order_completed().wait_visible()
    #
    #     order_modal.click_cancel()
    #     assert order_modal.is_closed()