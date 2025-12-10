from .base_page import BasePage
from src.taxi_ui.locators.modals_locators import ModalsLocators as M
from src.taxi_ui.data.texts import SEARCH_HEADER

class TaxiModal(BasePage):
    def has_required_elements(self) -> bool:
        return (
                self.find(M.MODAL_TITLE).text == SEARCH_HEADER
                and self.find(M.SEARCH_TIMER)
                and self.find(M.CANCEL_BUTTON)
                and self.find(M.DETAILS_BUTTON)
        )

    def click_details(self):
        self.click(M.DETAILS_BUTTON)
        from src.taxi_ui.pages.ride_details_modal import RideDetailsModal
        return RideDetailsModal(self.driver)

    def click_cancel(self):
        self.click(M.CANCEL_BUTTON)

    def is_closed(self) -> bool:
        return self.is_disappeared(M.MODAL)