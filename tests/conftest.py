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
def route_set(main_page):
    main_page.set_from_address(FROM_ADDRESS)
    main_page.set_to_address(TO_ADDRESS)
    main_page.wait_for_route_panel()
    return main_page