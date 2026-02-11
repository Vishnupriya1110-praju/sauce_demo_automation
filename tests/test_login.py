from pages.login_page import LoginPage
from utils.logger import get_logger

def test_valid_login(driver):
    logger = get_logger()
    logger.info("Test started")
    
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "Swag Labs" in driver.title
    login.take_screenshot("valid_login")
    logger.info("Test completed")
    