import re
from .base_page import BasePage
from src.taxi_ui.locators.modals_locators import ModalsLocators as M

class RideDetailsModal(BasePage):

    # def get_price_text(self) -> str:
    #     el = self.wait_visible(M.DETAILS_PRICE_TEXT)
    #     return el.text.strip()
    def get_price_value(self) -> int:
        text = self.find(M.DETAILS_PRICE_TEXT).text
        digits = re.findall(r"\d+", text)
        return int(digits[0])

    def click_cancel(self):
        self.click(M.CANCEL_BUTTON)

    def is_closed(self) -> bool:
        return self.is_disappeared(M.MODAL)
