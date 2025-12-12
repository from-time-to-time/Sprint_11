from .base_page import BasePage
from src.taxi_ui.locators.modals_locators import ModalsLocators as M
from src.taxi_ui.data.texts import SEARCH_HEADER

class TaxiModal(BasePage):
    def has_search_modal_elements(self) -> bool:
        return (
                self.wait_visible(M.MODAL_TITLE).text == SEARCH_HEADER
                and self.wait_visible(M.SEARCH_TIMER)
                and self.wait_visible(M.CANCEL_BUTTON)
                and self.wait_visible(M.DETAILS_BUTTON)
        )
    def wait_for_order_assigned(self):
        self.wait_visible(M.CAR_NUMBER)
        return self

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

    def click_details(self):
        self.click(M.DETAILS_BUTTON)
        from src.taxi_ui.pages.ride_details_modal import RideDetailsModal
        return RideDetailsModal(self.driver)

    def click_cancel(self):
        self.click(M.CANCEL_BUTTON)

    def is_closed(self) -> bool:
        return self.is_disappeared(M.MODAL)