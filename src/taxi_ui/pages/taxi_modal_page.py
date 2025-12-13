import allure

from src.taxi_ui.data.texts import SEARCH_HEADER
from src.taxi_ui.locators.modals_locators import ModalsLocators as M
from .base_page import BasePage


class TaxiModal(BasePage):
    @allure.step('Проверить, что модальное окно поиска такси содержит все элементы по ТЗ')
    def has_search_modal_elements(self) -> bool:
        return (
                self.wait_visible(M.MODAL_TITLE).text == SEARCH_HEADER
                and self.wait_visible(M.SEARCH_TIMER)
                and self.wait_visible(M.CANCEL_BUTTON)
                and self.wait_visible(M.DETAILS_BUTTON)
        )

    @allure.step('Дождаться отображения элементов модального окна с назначенным такси')
    def wait_for_order_assigned(self):
        self.wait_visible_with_timeout(M.CAR_NUMBER, timeout=60)
        return self

    @allure.step('Проверить, что модальное окно назначенного такси содержит все элементы по ТЗ')
    def has_assigned_modal_elements(self) -> bool:
        title_text = self.find(M.MODAL_TITLE).text
        has_title = "мин. и приедет" in title_text

        return (
                has_title
                and self._is_visible(M.CAR_NUMBER)
                and self._is_visible(M.CAR_IMAGE)
                and self._is_visible(M.DRIVER_INFO)
                and self._is_visible(M.DRIVER_NAME)
                and self._is_visible(M.DRIVER_PHOTO)
                and self._is_visible(M.DRIVER_RATING)
                and self._is_visible(M.CANCEL_BUTTON)
                and self._is_visible(M.DETAILS_BUTTON)
        )

    @allure.step('Нажать на кнопку "Детали" и открыть модальное окно деталей поездки')
    def click_details(self):
        self.click(M.DETAILS_BUTTON)
        from src.taxi_ui.pages.ride_details_modal_page import RideDetailsModal
        return RideDetailsModal(self.driver)

    @allure.step('Нажать на кнопку "Отменить"')
    def click_cancel(self):
        self.click(M.CANCEL_BUTTON)

    @allure.step('Убедиться, что модальное окно закрылось')
    def is_closed(self) -> bool:
        return self.is_disappeared(M.MODAL)
