from selenium.webdriver.common.by import By
class TaxiOrderLocators:
    TARIFF_PICKER_PANEL = (By.XPATH, "//div[@class = 'tariff-picker shown']")
    #Карточки тарифов
    TARIFF_LIST = (By.CSS_SELECTOR, 'div[class=tariff-cards]')
    TARIFF_CARD = {
        "Рабочий": (By.XPATH, "//div[@class = 'tcard-title' and text() = 'Рабочий']/ancestor::div[contains(@class,'tcard')]"),
        "Сонный": (By.XPATH, "//div[@class = 'tcard-title' and text() = 'Сонный']/ancestor::div[contains(@class,'tcard')]"),
        "Отпускной": (By.XPATH, "//div[@class = 'tcard-title' and text() = 'Отпускной']/ancestor::div[contains(@class,'tcard')]"),
        "Разговорчивый": (By.XPATH, "//div[@class = 'tcard-title' and text() = 'Разговорчивый']/ancestor::div[contains(@class,'tcard')]"),
        "Утешительный": (By.XPATH, "//div[@class = 'tcard-title' and text() = 'Утешительный']/ancestor::div[contains(@class,'tcard')]"),
        "Глянцевый": (By.XPATH, "//div[@class = 'tcard-title' and text() = 'Глянцевый']/ancestor::div[contains(@class,'tcard')]")
    }
    #Иконки "i" в тарифах
    TARIFF_INFO_ICON = {
        "Рабочий": (By.CSS_SELECTOR, "button[customclass='tcard-i'][data-for='tariff-card-0']"),
        "Сонный": (By.CSS_SELECTOR, "button[customclass='tcard-i'][data-for='tariff-card-1']"),
        "Отпускной": (By.CSS_SELECTOR, "button[customclass='tcard-i'][data-for='tariff-card-2']"),
        "Разговорчивый": (By.CSS_SELECTOR, "button[customclass='tcard-i'][data-for='tariff-card-3']"),
        "Утешительный": (By.CSS_SELECTOR, "button[customclass='tcard-i'][data-for='tariff-card-4']"),
        "Глянцевый": (By.CSS_SELECTOR, "button[customclass='tcard-i'][data-for='tariff-card-5']"),
    }
    #Поп-апы с информацией о тарифе
    TARIFF_TOOLTIP = {
        "Рабочий":  (By.XPATH, "//div[contains(@class,'__react_component_tooltip') and @data-id='tooltip' and @id='tariff-card-0']"),
        "Сонный": (By.XPATH, "//div[contains(@class,'__react_component_tooltip') and @data-id='tooltip' and @id='tariff-card-1']"),
        "Отпускной": (By.XPATH, "//div[contains(@class,'__react_component_tooltip') and @data-id='tooltip' and @id='tariff-card-2']"),
        "Разговорчивый": (By.XPATH, "//div[contains(@class,'__react_component_tooltip') and @data-id='tooltip' and @id='tariff-card-3']"),
        "Утешительный": (By.XPATH, "//div[contains(@class,'__react_component_tooltip') and @data-id='tooltip' and @id='tariff-card-4']"),
        "Глянцевый": (By.XPATH, "//div[contains(@class,'__react_component_tooltip') and @data-id='tooltip' and @id='tariff-card-5']")
    }
    #Цены тарифов
    TARIFF_PRICE = {
        "Рабочий": (By.XPATH, "//div[.='Рабочий']/following-sibling::div[contains(@class,'price')]"),
    }
    #Блок под тарифами
    PHONE = (By.XPATH, "//div[@class = 'np-button']")
    PAYMENT_METHOD = (By.XPATH, "//div[@class = 'form']/div[contains(@class, 'pp-button')]")
    COMMENT_INPUT =  (By.XPATH, "//div[@class = 'form']//div[contains(@class, 'input-container')]")
    REQUIREMENTS_BUTTON = (By.CSS_SELECTOR, 'div[class=reqs]')
    REQUIREMENTS_DROPDOWN = (By.CSS_SELECTOR, 'div[class=reqs-body]')
    LAPTOP_TABLE_CHECKBOX = (By.XPATH, "//div[contains(@class,'r-sw-label') and text()='Столик для ноутбука']/following::input[@type='checkbox' and contains(@class,'switch-input')][1]")
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button[class=smart-button]')
    #Типы передвижения
    TYPES_CONTAINER = (By.CSS_SELECTOR, ".types-container")
    CAR_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'car')]]")
    WALK_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'walk')]]")
    TAXI_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'taxi')]]")
    BIKE_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'bike')]]")
    SCOOTER_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'scooter')]]")
    DRIVE_TYPE = (By.XPATH, "//div[@class='types-container']//div[contains(@class,'type')][.//img[contains(@src,'drive')]]")


