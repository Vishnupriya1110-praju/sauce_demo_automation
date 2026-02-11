from pages.login_page import LoginPage
from utils.logger import get_logger

def test_invalid_login(driver):
    logger = get_logger()
    logger.info("Test started")
    
    login = LoginPage(driver)
    login.login("erererer", "eerere")
    assert "do not match any user" in login.get_error_message()
    login.take_screenshot("invalid_login")
    logger.info("Test completed")