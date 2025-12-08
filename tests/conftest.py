import pytest
from selenium import webdriver
from src.taxi_ui import config
from src.taxi_ui.pages.main_page import MainPage
from src.taxi_ui.data.addresses import FROM_ADDRESS, TO_ADDRESS

@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    chrome.get(config.BASE_URL)
    yield chrome
    chrome.quit()

@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.open(config.BASE_URL)
    return page
@pytest.fixture
def taxi_order_page(main_page):
    main_page.build_route(FROM_ADDRESS, TO_ADDRESS)
    main_page.select_fast_route()
    return main_page.click_call_taxi()