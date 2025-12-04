from selenium.webdriver.common.by import By
class MainPageLocators:
    FROM_INPUT = (By.CSS_SELECTOR, "input[placeholder='Откуда']")
    TO_INPUT = (By.CSS_SELECTOR, "input[placeholder='Куда']")
    # Таб «Оптимальный», «Быстрый», «Свой»
    TAB_OPTIMAL = (...)
    TAB_FAST = (...)
    TAB_CUSTOM = (...)
    # Блок выбора маршрута
    ROUTE_PANEL = (...)
    # Кнопки Вызвать такси / Забронировать
    CALL_TAXI_BUTTON = (...)
    BOOK_DRIVE_BUTTON = (...)
    # Маркеры на карте (иконки начала/конца маршрута)
    MAP_START_POINT = (...)
    MAP_FINISH_POINT = (...)