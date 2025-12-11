from selenium.webdriver.common.by import By
class MainPageLocators:
    #Инпуты адресов
    FROM_INPUT = (By.XPATH, "//input[@id = 'from']")
    TO_INPUT = (By.XPATH, "//input[@id = 'to']")
    # Маркеры на карте (пины начала/конца маршрута)
    MAP_START_POINT = (By.XPATH, "//ymaps[contains(@class,'route-pin')][.//ymaps[contains(@class,'PointSmallLetter0')]]")
    MAP_FINISH_POINT = (By.XPATH, "//ymaps[contains(@class,'route-pin')][.//ymaps[contains(@class,'PointSmallLetter1')]]")
    # Блок выбора маршрута
    ROUTE_PANEL = (By.XPATH, "//div[contains(@class, 'type-picker shown')]")
    ROUTE_RESULTS_CONTAINER = (By.XPATH, "//div[@class = 'results-container']")
    ROUTE_PRICE_TEXT = (By.CSS_SELECTOR, ".results-container .text")
    ROUTE_DURATION_TEXT = (By.CSS_SELECTOR, ".results-container .duration")
    # Табы "Оптимальный", "Быстрый", "Свой"
    TAB_OPTIMAL = (By.XPATH, "//div[@class='modes-container']/div[.='Оптимальный']")
    TAB_FAST =  (By.XPATH, "//div[@class='modes-container']/div[.='Быстрый']")
    TAB_CUSTOM = (By.XPATH, "//div[@class='modes-container']/div[.='Свой']")
    DRIVE_BUTTON = (By.XPATH, "//div[contains(@class, 'type drive')]")
    # Кнопки Вызвать такси / Забронировать
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(@type, 'button') and text() = 'Вызвать такси']")
    BOOK_DRIVE_BUTTON = (By.XPATH, "//button[contains(@type, 'button') and text() = 'Забронировать']")
    #Типы передвижения
    TYPES_CONTAINER = (By.CSS_SELECTOR, ".types-container")
    CAR_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'car')]]")
    WALK_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'walk')]]")
    TAXI_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'taxi')]]")
    BIKE_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'bike')]]")
    SCOOTER_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'scooter')]]")
    DRIVE_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'drive')]]")