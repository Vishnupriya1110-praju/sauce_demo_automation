import pytest
from selenium import webdriver
from utils.config_reader import get_url

@pytest.fixture(scope="function")
def driver():
    options.add_argument("--headless")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(get_url())
    yield driver
    driver.quit()