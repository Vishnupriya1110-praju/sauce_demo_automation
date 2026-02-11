import pytest
from selenium import webdriver
from utils.config_reader import get_url

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(get_url())
    yield driver
    driver.quit()