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
    #Тултип с информацией о тарифе
    TOOLTIP_DESCRIPTION = (By.CSS_SELECTOR, "div.i-floating-tooltip.show div.i-dPrefix")
    #Цены тарифов
    TARIFF_PRICE = {
        "Рабочий": (By.XPATH, "//div[.='Рабочий']/following-sibling::div[contains(@class,'price')]"),
    }
    #Блок под тарифами
    PHONE = (By.XPATH, "//div[@class = 'np-button']")
    PAYMENT_METHOD = (By.XPATH, "//div[@class = 'form']/div[contains(@class, 'pp-button')]")
    COMMENT_INPUT =  (By.XPATH, "//div[@class = 'form']//div[contains(@class, 'input-container')]")
    REQUIREMENTS_BUTTON = (By.CSS_SELECTOR, 'div[class=reqs]')
    REQUIREMENTS_DROPDOWN = (By.CSS_SELECTOR, 'div[class=reqs]')
    LAPTOP_TABLE_INPUT = (
        By.XPATH,
        "//div[contains(@class,'r-sw-label') and normalize-space()='Столик для ноутбука']"
        "/ancestor::div[contains(@class,'r-sw-container')]"
        "//input[@type='checkbox' and contains(@class,'switch-input')]"
    )
    LAPTOP_TABLE_TOGGLE = (
        By.XPATH,
        "//div[contains(@class,'r-sw-label') and normalize-space()='Столик для ноутбука']"
        "/ancestor::div[contains(@class,'r-sw-container')]"
        "//span[contains(@class,'slider')]"
    )
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button[class=smart-button]')


