import allure

from src.taxi_ui.data import addresses, texts


class TestRoute:
    @allure.title('Проверка отображения точек начала и конца маршрута на карте')
    def test_route_has_two_points_for_different_addresses(self, main_page):
        main_page.set_from_address(addresses.FROM_ADDRESS)
        main_page.set_to_address(addresses.TO_ADDRESS)

        assert main_page.wait_for_start_point()
        assert main_page.wait_for_finish_point()

    @allure.title('Проверка отображения блока с выбором маршрута')
    def test_route_panel_visible_for_different_addresses(self, main_page):
        main_page.set_from_address(addresses.FROM_ADDRESS)
        main_page.set_to_address(addresses.TO_ADDRESS)

        assert main_page.wait_for_route_panel()

    @allure.title('Проверка отображения блока с выбором маршрута при вводе одинакового адреса')
    def test_route_panel_visible_for_same_addresses(self, main_page):
        main_page.set_from_address(addresses.FROM_ADDRESS)
        main_page.set_to_address(addresses.SAME_ADDRESS)
        main_page.wait_for_route_panel()

        actual_text = main_page.get_same_route_text()

        assert actual_text == texts.ROUTE_FREE_TEXT
