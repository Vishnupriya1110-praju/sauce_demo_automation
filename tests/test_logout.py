from pages.login_page import LoginPage
from utils.logger import get_logger

def test_logout(driver):
    logger = get_logger()
    logger.info("Test started")
    
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "Swag Labs" in driver.title
    
    login.logout()
    login.take_screenshot("logout menu")
    logger.info("Test completed")
    