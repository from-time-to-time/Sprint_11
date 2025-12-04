import pytest
from selenium import webdriver
from src.taxi_ui import config

@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    chrome.get(config.BASE_URL)
    yield chrome
    chrome.quit()

@pytest.fixture()
def main_page(self, url=None):
    if url is None:
        url = config.BASE_URL
        self.driver.get(url)
        return MainPage(driver)
