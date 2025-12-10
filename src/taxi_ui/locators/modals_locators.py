from selenium.webdriver.common.by import By
class ModalsLocators:
    MODAL = (By.CSS_SELECTOR, "div[class=order-body]")
    MODAL_TITLE = (By.XPATH, "//div[@class = 'order-header-title']")
    SEARCH_TIMER = (By.XPATH, "//div[@class = 'order-header-time']")
    CANCEL_BUTTON = (By.XPATH, "//div[text()='Отменить']/preceding-sibling::button")
    DETAILS_BUTTON = (By.XPATH, "//div[text()='Детали']/preceding-sibling::button")

    CAR_NUMBER = (By.CSS_SELECTOR, 'div[class=number]')
    CAR_IMAGE = (By.CSS_SELECTOR, 'img[alt=Car]')
    DRIVER_INFO = (By.XPATH, "//div[@class='order-btn-group' and .//div[@class='order-btn-rating']]")
    DRIVER_PHOTO = (By.XPATH, "//div[@class='order-btn-group' and .//div[@class='order-btn-rating']]//img")
    DRIVER_RATING = (By.XPATH, "//div[@class='order-btn-group'][.//div[@class='order-btn-rating']]")
    DRIVER_NAME = (By.XPATH, "//div[@class='order-btn-group'][.//div[@class='order-btn-rating']]//div[text()!='' and not(@class)]")

    DETAILS_PRICE_TEXT = (By.XPATH, "//div[contains(@class,'order-body')]//div[@class='o-d-h' and text()='Еще про поездку']/following-sibling::div[contains(@class,'o-d-sh')]")